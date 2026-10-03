# Scripts

## build_facts.py

Builds `facts/<state>/<county FIPS>.json`: official numbers for a county, each with its source
table and year. Research sessions read these instead of fetching numbers themselves.

One-time setup (Census of Governments files, about 20 MB, and the geometry libraries):

```sh
mkdir -p /tmp/rid && cd /tmp/rid
curl -L -o fin2022.zip "https://www2.census.gov/programs-surveys/gov-finances/tables/2022/2022_Individual_Unit_File.zip"
curl -L -o apes2022.zip "https://www2.census.gov/programs-surveys/apes/datasets/2022/2022%20COG-E%20Individual%20Unit%20Files.zip"
unzip -oq fin2022.zip -d fin && unzip -oq apes2022.zip -d apes22
python3 -m venv venv && venv/bin/pip install shapely pyproj
```

Per county:

```sh
/tmp/rid/venv/bin/python scripts/build_facts.py --county 35031 --climate-station USW00023081 \
    --corridor corridors/i40-nm-west-points.json --data /tmp/rid
```

- `--climate-station` is a NOAA GHCN station with 1991–2020 normals, usually the county
  seat's airport. Some stations lack precipitation normals; those facts are listed under
  `missing`.
- ACS figures come from Census Reporter, pinned to the 2020–2024 5-year release (the Census
  Bureau's API now requires a key; "latest" on Census Reporter can switch to the 1-year survey).
- Election results (MIT Election Lab) are not included yet: the archive requires a
  registration form before download.
