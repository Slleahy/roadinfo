#!/usr/bin/env python3
"""Lists every word in the packed cards that the narrator voice has no dictionary entry for.

Those words are not silent: the voice guesses them with a neural model, and guesses are where
mangled place names come from. Run this after every new layer of cards, add the words that
matter to the app's Resources/Pronunciations.json, and have the owner confirm local names by ear.

Needs misaki in a Python 3.12 environment (see the Kokoro notes in ROAD_SAVANT_HANDOFF.md):
  /tmp/kokoro/venv312/bin/python scripts/scan_pronunciations.py
"""
import json, re, sys
from misaki import en
lex = json.load(open("/Users/scottleahy/Library/Developer/Xcode/UntitledProjects/Untitled Project/RoadSavant/Resources/Pronunciations.json"))
g = en.G2P(trf=False, british=False, fallback=None)
cards = json.load(open("/Users/scottleahy/Library/Developer/Xcode/UntitledProjects/roadinfo/dist/roadinfo-cards.json"))["cards"]
unknown = {}
for c in cards:
    for tok in g(c["text"])[1]:
        w = tok.text.strip()
        if not re.search(r"[A-Za-z]", w): continue
        if w in lex or w.lower() in lex: continue
        if tok.phonemes in (None, "", "❓"):
            unknown.setdefault(w, []).append(c["id"])
print(f"{len(unknown)} words the voice cannot pronounce, across {len(cards)} cards:\n")
for w, ids in sorted(unknown.items(), key=lambda kv: -len(kv[1])):
    print(f"  {w:28} in {len(ids)} card(s)  e.g. {ids[0]}")
