#!/usr/bin/env python3
"""Packs checked cards into one compact JSON file for the Road Savant app.

Only cards that passed the checking pass are included. County cards are labeled with their
county and state names (the app's offline boundary file identifies counties by name), taken
from the corridor files.

Usage: python3 scripts/pack_cards.py [--out dist/roadinfo-cards.json]
"""
import argparse, glob, json, os, re, sys
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


# A distance written into a card goes stale the moment the car moves. Sentences must use the
# {distance} placeholder instead, which the app fills from the current position as it speaks.
BAKED_IN_DISTANCE = re.compile(
    r"\b\d[\d,.]*\s*(?:mi|mile|miles|km|kilometres|kilometers)\b[^.]{0,30}?"
    r"\b(?:from here|away|to the (?:north|south|east|west)|"
    r"(?:north|south|east|west|northeast|northwest|southeast|southwest) of (?:here|town))",
    re.IGNORECASE,
)
PLACEHOLDER = re.compile(r"\{(distance|direction)\}")


def tie_to_drive_faults(card):
    """Ways a card breaks the tie-it-to-the-drive rule in the playbook. Mechanical checks only:
    whether the card actually opens with something local, and whether a distant fact earns its
    place, are judgement calls that belong to the ear pass."""
    faults = []
    text = card["text"]
    placeholders = set(PLACEHOLDER.findall(text))
    elsewhere = card.get("elsewhere")

    if placeholders and not elsewhere:
        faults.append("uses {distance}/{direction} but has no elsewhere coordinates to measure to")
    if elsewhere and "distance" not in placeholders:
        faults.append(f"names elsewhere '{elsewhere.get('name')}' but never says how far it is")
    if match := BAKED_IN_DISTANCE.search(text):
        faults.append(f"has a distance written into the text ({match.group(0)!r}); use {{distance}}")
    return faults


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="dist/roadinfo-cards.json")
    args = parser.parse_args()

    names = county_names()
    packed, skipped, rejected = [], [], []
    for path in sorted(glob.glob("cards/**/*.json", recursive=True)):
        card = json.load(open(path))
        if "checked" not in card:
            skipped.append(card["id"])
            continue
        if faults := tie_to_drive_faults(card):
            rejected.append((card["id"], faults))
            continue
        anchor = dict(card["anchor"])
        if anchor.get("type") == "place" and not anchor.get("state"):
            # Card ids start with the state's postal code: ca-…, nm-….
            anchor["state"] = {"ca": "California", "nm": "New Mexico", "az": "Arizona"}.get(card["id"][:2])
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
            "elsewhere": {k: card["elsewhere"][k] for k in ("lat", "lon", "name") if k in card["elsewhere"]} if card.get("elsewhere") else None,
        })
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    json.dump({"version": date.today().isoformat(), "license": "CC BY-SA 4.0, https://github.com/Slleahy/roadinfo",
               "cards": packed}, open(args.out, "w"), ensure_ascii=False, separators=(",", ":"))
    print(f"packed {len(packed)} cards into {args.out} ({os.path.getsize(args.out) // 1024} KB); skipped {len(skipped)} unchecked")
    missing = [c["id"] for c in packed if c["anchor"].get("type") == "county" and not c["anchor"].get("county")]
    if missing:
        print("WARNING: no county name for", missing)
    for card_id, faults in rejected:
        print(f"REJECTED {card_id}")
        for fault in faults:
            print(f"    {fault}")
    if rejected:
        print(f"\n{len(rejected)} card(s) left out: see 'Tie it to the drive' in PLAYBOOK.md")
        sys.exit(1)


if __name__ == "__main__":
    main()
