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
- **About this place.** A county card is about the county itself: its land, its towns and
  people, its history, its government, its economy, what a driver sees or crosses there. Facts
  about something that merely overlaps it (the internal structure of a tribal government, a
  national park's whole history) belong only where they explain what is here.
- **Neutral.** No opinions, no praise ("beautiful", "must-see"), no salesmanship.

## 2. Research method

For each subject (a county, town, sight, stretch, or landscape unit):

0. **Read what is already gathered**: the facts file `facts/<state>/<county FIPS>.json`
   (official numbers with their tables and years; use these, do not refetch them), the
   corridor file's `leadsToResearch`, and the subject's notes in `subjects/` (open issues and
   leads not yet used). **Work the strongest leads first**, so the budget goes to the best
   material.
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

Page-fetch limits per subject (hard limits; see §0): county 40, town 12, sight or stretch 5,
landscape unit 25, region 60. Do not spend fetches on numbers that are in the facts file.
The Census Bureau's own data API now requires a key; if a number is missing from the facts
file, note it in the subject notes rather than hunting for it.

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
- `near` says where a card belongs when it is about one spot. **Required** for town and sight
  cards, and for any county, landscape, or region card about a particular place (a dam, a mine,
  a base, a pass). Give the spot's latitude and longitude from a cited page (the Wikipedia
  article's coordinates or the GNIS record are fine), a `radiusMeters` (towns about 8,000;
  sights about 5,000, more if visible from far off; a spot in a county card about 40,000), and
  the page's URL in `source`. Leave `near` out of cards about the whole county or region.
- **Stretch cards** use `anchor` `{"type": "segment", "stretchId": …, "path": […], "bothDirections": …}`.
  Copy `path` from the stretches file, **in the order of travel the card is written for**
  (reverse it for the opposite direction). Set `bothDirections` to true when the card fits
  either direction (most history does) and false when it describes what lies ahead in one
  direction ("as the road climbs toward the pass…"). Stretch cards are about the road and what
  the driver sees along it: why the road goes here, its history, the land on each side, what
  is coming up. Do not repeat town or county cards. No `near` block on stretch cards.
- `direction` is used only for `stretch` cards: `"eastbound"`, `"westbound"`, or null for both.

## 3a. Biography cards (`"level": "person"`)

Almost every town in the country is somebody's home town, and a driver passing through has no
way of knowing. These cards fill that in. Source them from the "Notable people" section of a
town's Wikipedia article and from the `People from <place>` categories, then read the person's
own article for the facts.

**The bar.** A listener should recognise the name, or the reason should be interesting on its
own. Err towards leaving people out: a card about somebody nobody has heard of, who did nothing
the listener would find worth hearing, is dead air with a name in it. A state legislator from
1931 is not a card. The person who invented the thing in your glovebox is.

**The connection must be to this place, and real.** Born here, raised here, or did the work here.
Not "died here", not "briefly attended school here", not "owned property here". If the article
does not plainly say they are from this place, there is no card.

**What goes in.** Lead with why the listener knows the name, then the local tie, then one
concrete detail. Two to four sentences:

> "Mark Hoppus, bassist and singer of the rock band Blink one eighty two, was born in Ridgecrest
> on March 15, 1972. He left in the summer of 1992 for San Diego, to attend college and work at
> a local music store."

**Living people.** Stick to what is uncontroversial and plainly on the public record: what they
are known for, where they are from, when they left. No health, no family trouble, no legal
trouble, no politics, nothing a person would resent hearing said about them to strangers in a
car. If a fact would need a lawyer's eye, it is not going in a road narration.

**One card per person**, anchored with `near` on the town. Several people from one town means
several cards, and the program director spaces them out.

## 4. Writing for the ear

Write like a well-read friend in the passenger seat, or a good public-radio host: plain,
warm, specific, and never padded.

- **Lead with the hook.** The first sentence carries the surprising part, not the setup.
  Not "The county has a long history of mining." Instead, open on the event: who did what,
  when, and what it set off. (This file never names real people or places in its examples;
  every fact in a card comes from your sources, not from this playbook.)
- **Never name the source out loud.** No "according to the National Park Service", no "the
  county's website says". Attribution lives in the silent citations. The only exception is a
  claim that is genuinely disputed, where saying who claims it is part of the fact.
- **Tie it to the drive.** A fact about somewhere else is welcome, but only as an extension of
  something true where the car is. Two obligations, both required:
  1. **Open with here.** The card's first sentence is about what the listener is in or can see.
     The distant thing is the elaboration, never the subject.
  2. **Say how far.** The distant part carries `{distance}` (and optionally `{direction}`), which
     the app fills from the car's position as it speaks. Fill in the card's `elsewhere` field with
     that place's coordinates. Never write a distance as a fixed number — it is wrong as soon as
     the car moves, and the packer rejects it.

  The shape to copy, from the owner:

  > "The native vegetation here, creosote bush, is endemic to the Mojave Desert. One old example
  > was discovered by Professor Schmuckatelli in 1974, in the Lucerne Valley, {distance} from here."

  What this rule exists to stop: a card about the Lucerne Valley playing near Trona, a hundred
  miles away, with nothing said about why a driver there should care.
- **Only words the narrator can say.** Do not reach for an obscure term in another language
  when plain English carries the fact. A word in an Indigenous or foreign language earns its
  place only when it *is* the story (a town's own name for itself, a name on a road sign), and
  then it goes on the hand-over list in `PRONUNCIATIONS-NEEDED.md` for the owner to source from
  someone who says it. Never invent a pronunciation, and never spell a name with colons or
  other marks that a voice will read aloud ("A:shiwi"). If a term cannot be sourced, write the
  sentence without it.
- **Plain words.** A passenger is not a geologist. Explain a technical term in a few plain
  words the first time ("rhyolite, a pale volcanic rock"), or say the idea without it. Leave
  out formation names, epoch names, and units like kilometers unless they carry the story;
  give ages as "about 20 million years ago" and distances in miles.
- **No survey mechanics.** No margins of error, no "five-year estimate", no table names.
  Say "about 70,000 people live here", with the year when it matters ("as of 2024").
- **Every card needs a reason to listen**: a person, a turn of events, a number that
  surprises, a comparison that lands (one a source supports).
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

First use the facts file, citing the source recorded there. Elevations along the road in the
facts file are samples a few kilometers apart; for a named high point, use the official
figure (a state or federal source, or the sign's figure if a source reports it).
Otherwise use these, and record the table and year as the source:

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
5. **The ear pass.** Reads the card aloud as if sitting beside a driver at the spot it plays,
   and asks two questions. Does it open with something true *here* — a thing the listener is in
   or can see? And does anything far away say how far, with `{distance}`, rather than a number
   written into the text? A card that fails either is rewritten or dropped. The packer rejects
   the mechanical half of this, but only a reader can tell whether a fact earns its place.
6. Records the result in the card: `"checked": { "by": "checker", "date": "…", "removed": n }`.

Only checked cards are merged.

## 10. Output layout and commits

```
cards/<state>/<level>/<id>.json      one card per file
subjects/<state>/<level>/<slug>.md   research notes per subject (sources found, leads not used)
corridors/<name>.json                route definitions for pilots
```

Commit each finished subject separately: `Add cards: McKinley County (county, 38 cards)`.
