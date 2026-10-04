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
        # Match what KokoroVoice.applyPronunciations does: it looks words up case-insensitively,
        # splits on anything that is not a letter (so "Navajo-Gallup" is two words), and falls
        # back to the stem of a possessive ("Gallup's" -> "Gallup").
        parts = [p for p in re.split(r"[^A-Za-z\u00C0-\u024F']+", w) if p]
        def known(p):
            if p in lex or p.lower() in lex or p.capitalize() in lex: return True
            stem = p.rsplit("'", 1)[0]
            return bool(stem) and stem != p and (stem in lex or stem.lower() in lex)
        if parts and all(known(p) for p in parts): continue
        # A word can come back as several unknown markers ("McKinley" -> "❓❓"), so look
        # for the marker anywhere in the result, not just on its own.
        if tok.phonemes is None or tok.phonemes == "" or "❓" in tok.phonemes:
            unknown.setdefault(w, []).append(c["id"])
ordered = sorted(unknown.items(), key=lambda kv: -len(kv[1]))
print(f"{len(unknown)} words the voice cannot pronounce, across {len(cards)} cards:\n")
for w, ids in ordered:
    print(f"  {w:28} in {len(ids)} card(s)  e.g. {ids[0]}")

# Write the hand-over list. Anything left here after the obvious words have been added to
# Pronunciations.json goes to the owner, who sources local and Indigenous names from people
# who say them. Guessing is not allowed; a name we cannot source comes out of the sentence.
with open("PRONUNCIATIONS-NEEDED.md", "w") as f:
    f.write("# Pronunciations needed\n\n")
    f.write("Written by `scripts/scan_pronunciations.py`. Every word here is one the narrator\n")
    f.write("voice has to guess at, and guesses are where mangled names come from.\n\n")
    f.write("Workflow: add the ones you are sure of to the app's `RoadSavant/Resources/Pronunciations.json`,\n")
    f.write("then hand what is left to the owner, who will find or phone someone who says the word.\n")
    f.write("Never invent a pronunciation. If a word cannot be sourced, rewrite the sentence without it.\n\n")
    f.write(f"{len(unknown)} words across {len(cards)} cards.\n\n")
    f.write("| Word | Cards | Example card | Say it how? |\n|---|---|---|---|\n")
    for w, ids in ordered:
        f.write(f"| {w} | {len(ids)} | `{ids[0]}` |  |\n")
print("\nWrote PRONUNCIATIONS-NEEDED.md")
