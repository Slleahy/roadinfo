#!/usr/bin/env python3
"""Packs checked cards into one compact JSON file for the Road Savant app.

Only cards that passed the checking pass are included. County cards are labeled with their
county and state names (the app's offline boundary file identifies counties by name), taken
from the corridor files.

Usage: python3 scripts/pack_cards.py [--out dist/roadinfo-cards.json]
"""
import argparse, glob, json, os
from datetime import date

STATES = {"06": "California", "35": "New Mexico", "04": "Arizona"}


def county_names():
    names = {}
    for path in glob.glob("corridors/*.json"):
        if path.endswith("-points.json"):
            continue
        corridor = json.load(open(path))
        for county in corridor.get("counties", []) + corridor.get("edgeCounties", []):
            names[county["fips"]] = county["name"].split(",")[0].strip()
    return names


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="dist/roadinfo-cards.json")
    args = parser.parse_args()

    names = county_names()
    packed, skipped = [], []
    for path in sorted(glob.glob("cards/**/*.json", recursive=True)):
        card = json.load(open(path))
        if "checked" not in card:
            skipped.append(card["id"])
            continue
        anchor = dict(card["anchor"])
        if anchor.get("type") == "place" and not anchor.get("state"):
            anchor["state"] = STATES.get(card["id"][:2].upper() and {"ca": "06", "nm": "35", "az": "04"}.get(card["id"][:2], ""))
        if anchor.get("type") == "county":
            fips = anchor.get("fips", "")
            anchor["county"] = names.get(fips)
            anchor["state"] = STATES.get(fips[:2])
        packed.append({
            "id": card["id"],
            "level": card["level"],
            "anchor": anchor,
            "title": card["title"],
            "text": card["text"],
            "topics": card.get("topics", []),
            "interest": card["scores"]["interest"],
            "relevance": card["scores"]["relevance"],
            "sensitive": card.get("sensitive", []),
            "asOf": card.get("asOf"),
            "themeKeys": card.get("themeKeys", []),
            "followOn": card.get("followOn", []),
            "pronunciations": card.get("pronunciations", {}),
            "direction": card.get("direction"),
            "near": {k: card["near"][k] for k in ("lat", "lon", "radiusMeters", "name") if k in card["near"]} if card.get("near") else None,
        })
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    json.dump({"version": date.today().isoformat(), "license": "CC BY-SA 4.0, https://github.com/Slleahy/roadinfo",
               "cards": packed}, open(args.out, "w"), ensure_ascii=False, separators=(",", ":"))
    print(f"packed {len(packed)} cards into {args.out} ({os.path.getsize(args.out) // 1024} KB); skipped {len(skipped)} unchecked")
    missing = [c["id"] for c in packed if c["anchor"].get("type") == "county" and not c["anchor"].get("county")]
    if missing:
        print("WARNING: no county name for", missing)


if __name__ == "__main__":
    main()
