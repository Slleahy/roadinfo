#!/usr/bin/env python3
"""Builds facts/<state>/<county FIPS>.json: official numbers for one county, each with its
source table and year, so research sessions never have to fetch or guess them.

Sources (all free; none needs a key):
  Census ACS 5-year (via Census Reporter, which republishes the Census Bureau tables)
  NOAA NCEI 1991-2020 Climate Normals
  Census of Governments 2022: employment and finances, individual unit files
  Census TIGERweb (county outline, land area)
  USGS PAD-US 4.1 (land ownership; shares of the county by manager)
  USGS 3DEP Elevation Point Query Service (elevations along a corridor)

Usage:
  python3 scripts/build_facts.py --county 35031 --climate-station USW00023081 \
      --corridor corridors/i40-nm-west-points.json --data /tmp/rid
  --data holds the unzipped Census of Governments files (see download_govs below).
Needs shapely and pyproj for land shares.
"""
import argparse, json, math, os, time, urllib.parse, urllib.request
from datetime import date

UA = {"User-Agent": "roadinfo/0.1 (https://github.com/Slleahy/roadinfo)"}
TODAY = date.today().isoformat()


def get(url, data=None, tries=3):
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=UA), timeout=90) as r:
                return json.load(r)
        except Exception as error:
            last = error
            time.sleep(2 + attempt * 3)
    raise last


def fact(value, unit, year, title, url, table, note=None, sensitive=None):
    entry = {"value": value, "unit": unit, "year": year,
             "source": {"title": title, "url": url, "table": table, "retrieved": TODAY}}
    if note: entry["note"] = note
    if sensitive: entry["sensitive"] = sensitive
    return entry


# --- Census ACS via Census Reporter -------------------------------------------------------

ACS_TABLES = {
    "B01003": ("population", "B01003001", "people"),
    "B19013": ("median_household_income", "B19013001", "dollars"),
    "B01002": ("median_age", "B01002001", "years"),
    "B25077": ("median_home_value", "B25077001", "dollars"),
}


def acs_facts(fips, release="acs2024_5yr"):
    """Pinned to the 5-year release: "latest" silently switches to the 1-year survey for large
    counties, which is noisier and not available for small ones."""
    geo = f"05000US{fips}"
    url = f"https://api.censusreporter.org/1.0/data/show/{release}?table_ids={','.join(ACS_TABLES)}&geo_ids={geo}"
    data = get(url)
    name = data["release"]["name"]                         # "ACS 2024 5-year"
    year = name.split()[1]
    years = f"{int(year) - 4}-{year}"
    out = {}
    for table, (key, column, unit) in ACS_TABLES.items():
        value = data["data"][geo][table]["estimate"][column]
        out[key] = fact(value, unit, year, f"American Community Survey {years} 5-year estimates, table {table}",
                        f"https://censusreporter.org/tables/{table}/?geo_ids={geo}", f"Census ACS 5-year {years}, {table}")
    return out


# --- NOAA climate normals -----------------------------------------------------------------

def climate_facts(station):
    types = "ANN-PRCP-NORMAL,ANN-SNOW-NORMAL,ANN-TAVG-NORMAL"
    url = ("https://www.ncei.noaa.gov/access/services/data/v1?dataset=normals-annualseasonal-1991-2020"
           f"&stations={station}&dataTypes={types}&format=json")
    annual = get(url)[0]
    monthly_url = ("https://www.ncei.noaa.gov/access/services/data/v1?dataset=normals-monthly-1991-2020"
                   f"&stations={station}&dataTypes=MLY-TMAX-NORMAL,MLY-TMIN-NORMAL&format=json")
    try:
        name = get(f"https://www.ncei.noaa.gov/access/services/search/v1/data?dataset=normals-annualseasonal-1991-2020&stations={station}&limit=1")["results"][0]["stations"][0]["name"]
    except Exception:
        name = station
    src = (f"NOAA NCEI U.S. Climate Normals 1991-2020, station {station} ({name})", url, f"NOAA Climate Normals 1991-2020, {station}")
    monthly = {row["DATE"]: row for row in get(monthly_url)}
    def num(k):
        v = annual.get(k)
        return float(v) if v not in (None, "") else None
    def month(m, k):
        v = monthly.get(m, {}).get(k)
        return float(v) if v not in (None, "") else None
    out = {
        "climate_station": {"value": name, "unit": "station", "year": "1991-2020", "source": {"title": src[0], "url": url, "table": src[2], "retrieved": TODAY}},
        "annual_precipitation": fact(num("ANN-PRCP-NORMAL"), "inches", "1991-2020", *src),
        "annual_snowfall": fact(num("ANN-SNOW-NORMAL"), "inches", "1991-2020", *src),
        "annual_mean_temperature": fact(num("ANN-TAVG-NORMAL"), "degrees F", "1991-2020", *src),
        "july_average_high": fact(month("07", "MLY-TMAX-NORMAL"), "degrees F", "1991-2020", *src),
        "january_average_low": fact(month("01", "MLY-TMIN-NORMAL"), "degrees F", "1991-2020", *src),
    }
    return out


# --- Census of Governments ----------------------------------------------------------------

def government_facts(fips, data_dir):
    """County government employment and taxes and spending, 2022 Census of Governments."""
    state_fips, county = fips[:2], fips[2:]
    out = {}
    # Finance: IDs are FIPS state + type (1 = county) + county + unit. Amounts in thousands.
    fin_dir = os.path.join(data_dir, "fin", "2022_Individual_Unit_files")
    pid = os.path.join(fin_dir, "Fin_PID_2022.txt")
    county_id = None
    for line in open(pid, encoding="latin-1"):
        if line[:2] == state_fips and line[2] == "1" and line[3:6] == county:
            county_id, county_name = line[:12], line[12:76].strip()
            break
    if county_id:
        taxes = property_tax = sales_tax = spending = 0
        for line in open(os.path.join(fin_dir, "2022FinEstDAT_07152026modp.txt"), encoding="latin-1"):
            if not line.startswith(county_id):
                continue
            code, amount = line[12:15], int(line[15:27]) * 1000
            if code.startswith("T"):
                taxes += amount
                if code == "T01": property_tax += amount
                if code == "T09": sales_tax += amount
            # Direct expenditure: current operations (E), capital outlay (F, G), assistance (J),
            # interest (I), plus intergovernmental expenditure (M). Census classification manual.
            if code[0] in "EFGIJM":
                spending += amount
        src = ("Census of Governments 2022, Individual Unit File (finance)",
               "https://www2.census.gov/programs-surveys/gov-finances/tables/2022/2022_Individual_Unit_File.zip",
               f"Census of Governments 2022 finance, government ID {county_id} ({county_name})")
        out["county_government_taxes"] = fact(taxes, "dollars", "2022", *src, note="Sum of tax item codes (T*).")
        out["county_government_property_tax"] = fact(property_tax, "dollars", "2022", *src, note="Item T01.")
        out["county_government_gross_receipts_and_sales_tax"] = fact(sales_tax, "dollars", "2022", *src, note="Item T09, general sales or gross receipts.")
        out["county_government_spending"] = fact(spending, "dollars", "2022", *src,
                                                 note="Direct expenditure (E, F, G, I, J) plus intergovernmental expenditure (M), per the Census classification manual.")
    # Employment from the 2022 Census of Governments, which covers every government (the
    # yearly survey only samples). 14-character legacy IDs; county FIPS sits at columns 110-114.
    apes_dir = os.path.join(data_dir, "apes22")
    unit = None
    for line in open(os.path.join(apes_dir, "22empid.txt"), encoding="latin-1"):
        if line[2] == "1" and line[109:114] == fips:
            unit, unit_name = line[:14], line[14:78].strip()
            break
    if unit:
        for line in open(os.path.join(apes_dir, "22empst.txt"), encoding="latin-1"):
            if line.startswith(unit) and line[17:20] == "000":
                full_time, payroll, part_time = int(line[20:30]), int(line[32:44]), int(line[46:56])
                src = ("Census of Governments 2022: Employment, Individual Unit Files",
                       "https://www2.census.gov/programs-surveys/apes/datasets/2022/2022%20COG-E%20Individual%20Unit%20Files.zip",
                       f"Census of Governments 2022 employment, unit {unit} ({unit_name}), item 000 (total)")
                out["county_government_full_time_employees"] = fact(full_time, "people", "2022", *src)
                out["county_government_part_time_employees"] = fact(part_time, "people", "2022", *src)
                out["county_government_march_payroll_full_time"] = fact(payroll, "dollars per month", "2022", *src, note="March, 31-day equivalent.")
                break
    return out


# --- County outline, area, and land ownership ---------------------------------------------

def county_geometry(fips):
    url = ("https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/State_County/MapServer/1/query?"
           + urllib.parse.urlencode({"where": f"GEOID='{fips}'", "outFields": "NAME,AREALAND,AREAWATER",
                                     "returnGeometry": "true", "outSR": "4326", "maxAllowableOffset": "0.001", "f": "json"}))
    feature = get(url)["features"][0]
    return feature, url


def land_facts(fips):
    from shapely.geometry import Polygon, MultiPolygon, mapping, shape
    from shapely.ops import transform, unary_union
    from shapely.validation import make_valid
    import pyproj

    feature, tiger_url = county_geometry(fips)
    attributes = feature["attributes"]
    def to_shape(rings):
        # Esri rings: outer boundaries run clockwise, holes counter-clockwise. Union the outers,
        # subtract the holes. (Pairwise combining is far too slow for checkerboard land.)
        outers, holes = [], []
        for ring in rings:
            if len(ring) < 4: continue
            signed = sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(ring, ring[1:]))
            (outers if signed < 0 else holes).append(make_valid(Polygon(ring)))
        geom = unary_union(outers)
        if holes: geom = geom.difference(unary_union(holes))
        return make_valid(geom)
    county = to_shape(feature["geometry"]["rings"])
    project = pyproj.Transformer.from_crs("EPSG:4326", "EPSG:5070", always_xy=True).transform  # equal-area
    county_area = transform(project, county).area

    out = {
        "land_area": fact(round(attributes["AREALAND"] / 2_589_988.11), "square miles", "2023",
                          "Census TIGERweb, State_County layer", tiger_url, "Census TIGER/Line county AREALAND"),
    }

    pad = "https://services.arcgis.com/v01gqwM5QqNysAAi/arcgis/rest/services/Fee_Managers_PADUS/FeatureServer/0/query"
    envelope = county.bounds
    body = urllib.parse.urlencode({
        "geometry": json.dumps({"xmin": envelope[0], "ymin": envelope[1], "xmax": envelope[2], "ymax": envelope[3], "spatialReference": {"wkid": 4326}}),
        "geometryType": "esriGeometryEnvelope", "inSR": 4326, "spatialRel": "esriSpatialRelIntersects",
        "outFields": "Unit_Nm,Mang_Name,Mang_Type,Des_Tp", "returnGeometry": "true", "outSR": 4326,
        "maxAllowableOffset": 0.002, "geometryPrecision": 4, "resultRecordCount": 2000, "f": "json"}).encode()
    features = get(pad, data=body).get("features", [])
    by_manager, by_unit = {}, {}
    for f in features:
        rings = (f.get("geometry") or {}).get("rings")
        if not rings: continue
        try:
            piece = to_shape(rings).intersection(county)
        except Exception:
            continue
        if piece.is_empty: continue
        area = transform(project, piece).area
        a = f["attributes"]
        manager = a.get("Mang_Name") or "UNK"
        by_manager[manager] = by_manager.get(manager, 0) + area
        name = (a.get("Unit_Nm") or "").strip()
        if name:
            by_unit[(name, manager)] = by_unit.get((name, manager), 0) + area
    src = ("USGS Protected Areas Database of the United States (PAD-US) 4.1, Fee Managers, clipped to the Census county outline",
           pad, "PAD-US 4.1 Fee Managers")
    shares = {m: round(100 * a / county_area, 1) for m, a in sorted(by_manager.items(), key=lambda kv: -kv[1]) if a / county_area >= 0.005}
    listed = sum(by_manager.values()) / county_area
    out["land_share_by_manager_percent"] = fact(shares, "percent of county area", "2024", *src,
                                                note="Manager codes as in PAD-US (TRIB tribal, BLM, USFS, NPS, DOD, SLB state land board, CITY, CNTY…). Remainder is private or unlisted.")
    out["land_share_unlisted_percent"] = fact(round(100 * max(0, 1 - listed), 1), "percent of county area", "2024", *src,
                                              note="Private land or land not in PAD-US.")
    out["largest_land_units"] = fact([{"name": n, "manager": m, "percent_of_county": round(100 * a / county_area, 1)}
                                      for (n, m), a in sorted(by_unit.items(), key=lambda kv: -kv[1])[:10]],
                                     "list", "2024", *src)
    return out


# --- Elevations along a corridor ----------------------------------------------------------

def corridor_elevations(points_path, fips):
    """Highest and lowest points of the road within this county, sampled about every 3 km."""
    from shapely.geometry import Point
    feature, _ = county_geometry(fips)
    from shapely.geometry import Polygon
    county = None
    for ring in feature["geometry"]["rings"]:
        p = Polygon(ring)
        county = p if county is None else county.symmetric_difference(p)
    from concurrent.futures import ThreadPoolExecutor
    inside = [(lon, lat) for lon, lat in json.load(open(points_path)) if county.contains(Point(lon, lat))]
    def elevation(point):
        lon, lat = point
        try:
            value = get(f"https://epqs.nationalmap.gov/v1/json?x={lon}&y={lat}&units=Feet&wkid=4326").get("value")
            return (float(value), lat, lon) if value not in (None, "") else None
        except Exception:
            return None
    with ThreadPoolExecutor(max_workers=6) as pool:
        samples = [s for s in pool.map(elevation, inside) if s]
    if not samples: return {}
    src = ("USGS 3D Elevation Program, Elevation Point Query Service (sampled along the corridor about every 3 km)",
           "https://epqs.nationalmap.gov/v1/docs", "USGS 3DEP EPQS")
    high, low = max(samples), min(samples)
    return {
        "corridor_highest_elevation": fact({"feet": round(high[0]), "lat": high[1], "lon": high[2]}, "feet", "current", *src),
        "corridor_lowest_elevation": fact({"feet": round(low[0]), "lat": low[1], "lon": low[2]}, "feet", "current", *src),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--county", required=True, help="5-digit county FIPS")
    parser.add_argument("--state", default="nm")
    parser.add_argument("--climate-station", required=True, help="GHCN station id for climate normals")
    parser.add_argument("--corridor", help="JSON list of [lon, lat] points along the road")
    parser.add_argument("--data", required=True, help="Directory with unzipped Census of Governments files")
    args = parser.parse_args()

    facts = {"fips": args.county, "built": TODAY, "facts": {}}
    for label, build in [("acs", lambda: acs_facts(args.county)),
                         ("climate", lambda: climate_facts(args.climate_station)),
                         ("government", lambda: government_facts(args.county, args.data)),
                         ("land", lambda: land_facts(args.county)),
                         ("elevation", lambda: corridor_elevations(args.corridor, args.county) if args.corridor else {})]:
        try:
            facts["facts"].update(build())
            print(f"  {label}: ok")
        except Exception as error:
            facts.setdefault("missing", []).append(f"{label}: {error}")
            print(f"  {label}: FAILED {error}")
    empty = [k for k, v in facts["facts"].items() if v.get("value") in (None, [], {})]
    for key in empty:
        del facts["facts"][key]
        facts.setdefault("missing", []).append(f"{key}: no value in source")
    path = os.path.join("facts", args.state, f"{args.county}.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    json.dump(facts, open(path, "w"), indent=2, ensure_ascii=False)
    print("wrote", path)


if __name__ == "__main__":
    main()
