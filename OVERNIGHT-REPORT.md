# Overnight report: Ridgecrest to Paso Robles, P2 to P7

Run 2026-10-05 in the owner's local Claude Code session, not on cloud credit, so every ledger row is
`$0 cloud` and the $200 balance is unchanged. Each phase had two separate agents: a writer, then a
checker who had not written the cards (PLAYBOOK §9). The checkers reopened every cited source and
corrected quotes to their exact wording. They checked numbers against `facts/ca/*.json` or the named
official table, and gave every card the ear pass. `BUDGET.md` is back to `STATUS: HALT`.
`dist/roadinfo-cards.json` (302 cards) has been copied over `RoadSavant/Resources/RoadinfoCards.json`.

**A note on the rules.** BUDGET.md recommended stopping after P2 to drive the route before going
further, and says one session works one batch. This run did P2 to P7 in one sitting because the
owner asked for it in so many words. The three questions BUDGET.md wanted answered after a drive
are still open: is the density right, do the person cards clear the bar, and does the pipeline work
off the desert.

## Cards per phase

| Phase | Subject | Written | Survived check | Sentences removed | Commit |
|---|---|---|---|---|---|
| P2 | Caliente to Bakersfield, incl. 6 person cards | 24 | 24 | 2 | 3cf183e |
| P3 | West Kern and I-5 | 15 | 14 | 0 (1 card dropped) | 3cf183e |
| P4 | CA-46, Lost Hills to Shandon | 13 | 13 | 0 (20 rewrites) | 0ad749f |
| P5 | Paso Robles and Adelaida, incl. 1 person card | 20 | 20 | 5 | 2308653 |
| P6 | San Luis Obispo County deck | 15 | 15 | 0 (1 clause) | 7f92e39 |
| P7 | Road stretches, CA-58, I-5, CA-46 | 13 | 13 | 1 | 64a9255 |
| | **Total new** | **100** | **99** | | |

Infrastructure added: `facts/ca/06079.json`, built with `build_facts.py` using the Paso Robles
airport station for climate. Two corridor files: `corridors/ridgecrest-paso.json`, which lets the
packer label San Luis Obispo County cards, and `corridors/ridgecrest-paso-stretches.json`, six
stretches with geometry from the OSRM demo router on OpenStreetMap data, sampled about every 1 km.

**P2/P3 starting state.** The prompt said there were 42 uncommitted cards; there were 39. All 39
already carried a `checked` stamp dated 2026-10-04. That stamp was treated as unverified and every
card was checked again from scratch. About 40 quotes turned out to be paraphrased or stitched
together, and were corrected to the source's exact words.

**P7 directions.** Each direction gets 7 cards: 5 one-way cards plus the 2 cards written for both
directions. The drive home has only the shared card on the I-5 leg, because nothing southbound-only
could be sourced. Three cards on old US 466 all play on the way out, and the program director may
want to space them.

## Person cards (§3a)

All seven passed a checker given extra instructions on §3a.
- **Buck Owens:** did the work here.
- **Merle Haggard:** born in Oildale; the card says Oildale, near Bakersfield. Consider anchoring it on Oildale.
- **Earl Warren:** the card now says he was born in Los Angeles and moved here in 1896. "Grew up here" has two sources.
- **Rick Mears:** raised here.
- **Marc Davis:** born here. He is the weakest of the seven; the tie is birth only.
- **Jonathan Davis:** born and raised here. The card mentions a coroner's-assistant job, which the owner may find too morbid for the car.
- **Josh Brolin:** raised on a ranch near Adelaida.

Rejected at Paso Robles:
- **Paderewski:** his famous work was not done here. He has a town card instead.
- **King Vidor:** only died here.
- **Elena Verdugo:** born here but below the recognition bar.
- **Several others:** lived, retired or owned property here, which is not a tie.

Rejected at Bakersfield:
- **Kevin McCarthy and Vince Fong:** current politics.
- **The two Bushes:** lived here only briefly.
- **Lawrence Tibbett:** below the recognition bar.
- **Frank Gifford:** the tie was not plainly sourced, and he is worth one more fetch.
- **Kevin Harvick, the Carrs and Jordan Love:** held back to avoid a pile of sports cards. Harvick and Derek Carr are next if the density feels thin.

## Dropped, and why

- **P3 card:** `ca-landscape-southern-san-joaquin-valley-floor-san-joaquin-desert-01`. Its farm acreage came from Wikipedia prose, not the Census of Agriculture table, and without it the card was too thin to stand alone.
- **Single-source superlatives, removed or softened:**
  - Jack Ranch's "oldest brand still in use".
  - Parkfield as "most closely observed".
  - 1857 as "perhaps the largest", now "one of the largest", with a second USGS source.
  - Antelope Grade as the "southernmost road across the Diablo Range", and as carrying "the most trucks on the Central Coast".
  - "Steepest coastal slope", "most mountain lions", Paderewski bringing Zinfandel "first", and the "44th wine area".
  - Carrizo as the "largest native grassland", the "only L-shaped mission church", and two Camp Roberts superlatives.
  - "No multi-lane highway across the Sierra between Tehachapi and Donner", and "second rail crossing of the Sierras".
- **Numbers from prose with no table:**
  - Historic populations: Bakersfield in 1870, Caliente's 200, Adelaida's 500, and San Luis Obispo County's 336 in 1850.
  - Winery counts, wine-area acreage, Cabernet acreage, and Paso Robles' population.
  - The hot spring's flow (two sources give 1,300 and 350 gallons a minute).
  - Blood Alley crash and death counts, truck shares, and the climbing lane's size and cost.
  - Pass elevations of 3,771 and 4,031 feet, which are Wikipedia figures, not USGS.
  - "228 lots".
- **Sources in conflict, so worded around or left out:**
  - Ranch acreage: 58,000 or 73,000 acres.
  - Hearst's purchase: 1965 or 1966. The card says "the 1960s".
  - James Dean's speed: 85 or 55 mph.
  - The 2003 earthquake: magnitude 6.5 or 6.6. USGS confirms 6.5.
  - Nacimiento dam: 1956 or 1957. The card says "the 1950s".
  - Hotel architect and incorporation date, both left out.
  - Hearst Castle visitor numbers.
  - The Carrizo monument date. The card says only "2001".
  - The Salinan language's status.
  - Start of the Blood Alley widening: 2008 or 2009.
- **Left out on purpose:** the 2003 wrongful-death lawsuit, Dark Watchers folklore, the 1987 PSA crash, Morro Rock (sacred-site material), and "the last place Dean was seen alive", which is inaccurate.
- **Repeats of existing cards:** the Caliente tunnels sentence repeats the Tehachapi Loop card, the Buck Owens Mesa, Arizona sentence is not about here, and the Blood Alley head-on sentence repeats the Wye card.

## Corrections to the plan

- **"The 1886 hot springs" was wrong.** 1886 is when the railroad reached Paso Robles; the first train came on October 31, 1886. The first hotel at the springs dates from 1864. The fireproof hotel opened in 1891, burned in 1940, and the Paso Robles Inn opened in 1942.
- **The 46/41 overpass at Cholame** opened on June 12, 2025, and the card is in the past tense.

## Unsourceable or weak

- **Kern farm acreage and crop figures:** the official PDF tables could not be read.
- **Shandon's founding and the origin of its name:** the historical marker page returns 403, and the name stories conflict.
- **Estrella the town:** no source, so no town card. The adobe church card covers it.
- **The James Dean memorial:** whether it still stands in 2026 is unknown. The card uses Cholame's coordinates.
- **Lake Nacimiento:** the Monterey County water agency site blocks every request. One San Luis Obispo County source was added.
- **Single-source but not surprising, so kept with confidence 3:**
  - Pirates and White Sox spring training, and Paderewski's 1913 stay.
  - The Saint Lucy naming story, and Jenna's Bill.
  - Diablo Canyon's approval to run to 2030.
  - The age of the Carrizo rock paintings.
  - Several P7 stretch cards, sourced from Gribblenation, cahighways.org or Wikipedia.
- **Will go stale:** the truck climbing lane (as of August 2026) and the Antelope Grade rebuild (as of early 2026).

## Decisions for the owner

1. **Numbers from prose.** Checkers kept physical measurements an agency states in prose: magnitude 7.9, 160 miles of rupture, the 4-inch pavement shift, aqueduct and pump dimensions, oil totals, acreages, subsidence rates, and visible lane counts. They removed counts and costs. §6's table list does not cover these, so confirm this reading or tighten it.
2. **The facts-file climate link is wrong.** `build_facts.py` points `july_average_high` and `january_average_low` at NOAA's annual dataset, which has no monthly figures. The values are right; the link should be the monthly normals. This likely affects every facts file.
3. **Adelaida or Adelaide.** The county's own page spells it "Adelaide", and the cards use "Adelaida".
4. **Northern Chumash name.** The tribe's own name is "yak titʸu titʸu yak tiłhini". The card uses only the English name. Decide whether to source a spoken form.
5. **Card length.** `antelope-grade-climb` runs about 128 words, slightly over the 45-second target.
6. **"Caltrans" spoken aloud.** Three P7 cards name it as the agency doing the work, not as attribution.
7. **A privacy slip.** The P6 writer's first Wikipedia request sent the owner's email address in its HTTP User-Agent header. It was removed at once, and every later agent was told to use a plain User-Agent.

## Pronunciations

**Added only where the cited page gives one:**
- **San Luis Obispo:** the Wikipedia county article's respelling and IPA, on all 15 county cards.
- **Santa Lucia:** IPA sæntə luˈsiːə from Wikipedia.
- **Brolin:** IPA ˈbroʊlɪn from Wikipedia.

**Removed:** the P5 writer had added "Adelaida → Adelaide", but the cited page gives no pronunciation, so the checker took it out.

The scanner checks the app's `Pronunciations.json`, not the entries on the cards, so it still lists Luis and Obispo. `PRONUNCIATIONS-NEEDED.md` now lists 93 words across 302 cards. Many of them are ordinary English names (Calvin, Coolidge, Roosevelt) that only need adding to the dictionary.

**Local and foreign names that need the owner, or someone who says them:**

| Word | Where | Note |
|---|---|---|
| Paso Robles, Robles, El Paso de Robles | all Paso Robles cards | Two local forms on record ("ROH-buhlz" and "ROH-blays", per Wikipedia citing KCBX 2015). **Owner must pick.** |
| Cholame | 24 cards | Wikipedia gives /ʃəˈlæm/, citing Kean, *Wide Places in the California Roads* (1993). Not added; owner to confirm. |
| Adelaida | 10 cards | No source gives a pronunciation. |
| Caliente, Agua Caliente | 11 cards | Spanish |
| Shandon | 10 cards | |
| Salinan, Salinas | 8 cards | Nation's name |
| Nacimiento | 7 cards | Spanish |
| Estrella | 7 cards | Spanish |
| Buttonwillow | 6 cards | |
| Diablo, Polonio, Temblor, Carrizo, Tejon | P4, P6, P7 | Spanish place names |
| Tulare, Yokuts, Kitanemuk, Chumash | various | Local and Indigenous names |
| Bena, Bealville, Beale, Tupman, Oildale, Weedpatch | P2/P3 | Local names |
| Klau, Las Tablas, Geneseo, Templeton, Atascadero, Whitley Gardens | P5, P7 | Local names |
| Tolosa, Arcángel, Esteban Munras, Junípero Serra, Pedro Fages, Vizcaíno, Portolá | P5, P6 | Spanish names |
| Avila, Cambria, San Simeon, Los Osos, Morro, Los Banos, Buena Vista | P5–P7 | |
| Paderewski, Ignacy, Seita Ohnishi, Edmonston, Jedediah, Drury | various | Personal names |
| Korn ("corn"), Mears ("meers"), Spyder, Porsche, Hee Haw, Cruella de Vil | P2, P4 | Names of bands, shows, cars and characters |
| diatomite, calcareous, paleoseismic, unreinforced | various | Technical words the voice may stumble on |
