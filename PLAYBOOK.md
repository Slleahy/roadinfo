# Playbook for research and writing agents

You are building cards for **roadinfo**, a database that a voice-only road-trip narrator plays
to drivers and passengers. Your job is to find what is true, interesting, and relevant to
someone driving past, and write it to be heard. Read this whole file before starting a batch.

## 0. Spending limits: read first

- Open [`BUDGET.md`](BUDGET.md). If its first line is not `STATUS: GO`, stop immediately and
  do nothing else.
- Work only the one batch you were given, and only if its phase is open in `BUDGET.md`.
- Page-fetch budgets in §2 are **hard limits**, not targets. When one is reached, finish the
  card in hand, commit, and stop.
- Never start another batch, schedule work, launch other agents, or retry a failed batch on
  your own. When the batch is done, commit and end the session.
- Prefer fewer, stronger cards over many weak ones. A subject's card count limits:
  county 40, town 8, sight 3, stretch 2, landscape unit 30, region 150.

## 1. The standard

- **Strictly factual.** Every sentence must be supported by a source you cite. No folklore
  presented as fact, no padding, no guesses. Legends may be told only when framed as legends
  ("According to local legend…") and when a reliable source reports the legend.
- **Engaging.** Prefer people, events, surprises, superlatives, firsts, disasters survived,
  odd facts, how a place got its name, why the road goes where it goes. A card should make a
  passenger say "huh."
- **Relevant from the road.** Prefer things a driver can see, is about to reach, or is
  driving through. Say where they are relative to the road only if a source supports it; the
  app adds side, distance, and clock bearing itself, so do not write directions.
- **Neutral.** No opinions, no praise ("beautiful", "must-see"), no salesmanship.

## 2. Research method

For each subject (a county, town, sight, stretch, or landscape unit):

1. **Start with the English Wikipedia article.** Read it fully, not just the opening.
2. **Follow links that look promising**: people born or active there, events, industries,
   disasters, nicknames, notable buildings, geology, film locations. Judge each detour by
   likely payoff; stop following a thread when it stops being about this place.
3. **Search the web for local and official sources**: county and city websites, historical
   societies, state geological surveys, National Park Service and Forest Service pages, state
   historic preservation offices, university pages, reputable newspapers. Use the web search
   tool you have; do not scrape search engines.
4. **Take numbers only from official data tables** (see §6), never from prose, and never from
   memory. If a number has no table source, leave it out.
5. **Do not rely on your own memory for any fact.** If you remember something interesting,
   find a source for it or drop it.

Budget per subject: about 15 page fetches for a county, 8 for a town, 4 for a sight or
stretch. Spend more only when a lead is unusually strong.

## 3. Card format

One JSON object per card, conforming to [`schema/card.schema.json`](schema/card.schema.json):

```json
{
  "id": "nm-mckinley-county-uranium-boom-01",
  "level": "county",
  "anchor": { "type": "county", "fips": "35031" },
  "title": "The uranium boom",
  "text": "Two to five sentences, written for the ear.",
  "sentences": [
    { "text": "First sentence.", "sources": ["s1"] },
    { "text": "Second sentence.", "sources": ["s1", "s2"] }
  ],
  "sources": {
    "s1": { "title": "Page title", "url": "https://…", "publisher": "…", "retrieved": "2026-10-02", "revision": "optional wiki revision id", "quote": "Short supporting passage." }
  },
  "topics": ["history", "mining"],
  "scores": { "relevance": 4, "interest": 5, "confidence": 5 },
  "sensitive": [],
  "asOf": null,
  "themeKeys": ["uranium", "grants mining district"],
  "pronunciations": { "Tsoodził": "tsoh-DZILTH" },
  "followOn": ["nm-cibola-county-uranium-legacy-01"],
  "direction": null
}
```

- `text` is exactly the `sentences` joined with spaces.
- Every sentence lists at least one source id. Each source has a short `quote` showing the
  passage that supports it.
- `asOf` is the year of any figure in the card ("2024"); null if the card has no figures.
- `direction` is used only for `stretch` cards: `"eastbound"`, `"westbound"`, or null for both.

## 4. Writing for the ear

- 2 to 5 sentences, 20 to 45 seconds spoken. One idea per card.
- Short sentences. No parentheses, no lists longer than three items, no footnote markers.
- Spell out what a voice would say: "about 1,600 people", "in the 1920s", "Interstate 40".
  No abbreviations a voice might misread (write "Mount", "Saint", "Junior").
- Round figures the way a person would ("about 72,000 people", "nearly 9 inches of rain a year").
- The card must stand alone: name the subject in the first sentence.
- Add `pronunciations` for any name a speech engine is likely to get wrong, with an
  English-friendly respelling and, where a source gives it, IPA.

## 5. Scoring (1 to 5)

- **relevance**: 5 = visible or underfoot from the road right now; 1 = only loosely tied to the place.
- **interest**: 5 = a passenger would retell it; 3 = solid but ordinary; 1 = dry.
- **confidence**: 5 = two or more independent reliable sources agree; 3 = one reliable source;
  below 3 = do not submit.

Anything surprising (a superlative, a "first", an unusual claim) needs **two independent
sources** or it is dropped.

## 6. Numbers come from tables

Use these, and record the table and year as the source:

| Fact | Source |
|---|---|
| Population, median household income | Census ACS 5-year estimates |
| Climate (rainfall, snowfall, temperatures) | NOAA 1991–2020 Climate Normals |
| County spending, revenue, employees | Census of Governments (finance, employment) |
| Elevation | USGS |
| Land ownership and protected areas | USGS PAD-US |
| Election results | MIT Election Data and Science Lab |

Always state the year in the sentence when the figure can change ("In 2023, …").

## 7. Sensitive topics

Tag, do not avoid. The app lets each listener turn these off. Put any that apply in `sensitive`:

- `crime`: crimes, prisons, notable criminal cases.
- `voting`: election results, party registration, political controversies.
- `demographics`: race, ethnicity, religion, immigration status breakdowns.
- `tragedy`: disasters with loss of life, massacres, accidents.

Median household income is **not** sensitive; include it as an ordinary fact.

## 8. Tribal lands and Native history

- Prefer each nation's or pueblo's own published sources, then official sources (National Park
  Service, Bureau of Indian Affairs, tribal museums and cultural centers), then scholarship.
- Use the names the nation uses for itself, and current place names, with pronunciations.
- **Never** describe ceremonies, sacred sites' religious details, or restricted cultural
  knowledge. It is fine to say a mountain is sacred to a people, if a source says so;
  stop there.
- Follow-on cards should note when a place is not open to visitors or needs permission.

## 9. Checking pass (a separate agent)

For every card, a checker who did not write it:

1. Opens each cited source and confirms the `quote` appears there and supports the sentence.
2. Confirms numbers against the named table and year.
3. Confirms two sources for anything surprising.
4. Removes any sentence that fails. If the card no longer stands on its own, drops the card.
5. Records the result in the card: `"checked": { "by": "checker", "date": "…", "removed": n }`.

Only checked cards are merged.

## 10. Output layout and commits

```
cards/<state>/<level>/<id>.json      one card per file
subjects/<state>/<level>/<slug>.md   research notes per subject (sources found, leads not used)
corridors/<name>.json                route definitions for pilots
```

Commit each finished subject separately: `Add cards: McKinley County (county, 38 cards)`.
