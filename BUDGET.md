STATUS: HALT

# Budget

**Hard ceiling for the pilot: $250 of Claude cloud usage, total. Never exceed it.**
The credit expires 11:59 PM PST, November 4, 2026. Account extra usage is off ($0 spend limit).

Every research or checking session reads this file first. If the first line says
`STATUS: HALT`, the session does nothing and exits. Sessions run only when the first line
says `STATUS: GO` and the phase they were given is marked open below.

## Phases and caps

| Phase | Batch | Cap | Status | Actual |
|---|---|---|---|---|
| 1 | Calibration: McKinley County, county deck only | $15 | done: 25 checked cards (re-run in the local Xcode session) | $2 |
| 2 | McKinley County: towns, sights, road stretches | $55 | paused for Ridgecrest | |
| 3 | Cibola County: all levels | $55 | not started | |
| 4 | Landscape decks along the corridor (shared statewide) | $40 | not started | |
| 5 | New Mexico region deck | $35 | not started | |
| — | Reserve for fixes and re-checks | $50 | held | |

### Ridgecrest home drives (owner's real-drive test; see corridors/ridgecrest-home.json)

Funded from the New Mexico phases 2–5 above, which are paused. One layer at a time; cost checked before the next opens.

| Phase | Batch | Cap | Status | Actual |
|---|---|---|---|---|
| R1 | Kern County deck (county level, eastern Kern focus) | $10 | done: 30 checked cards | $5 |
| R2 | San Bernardino and Los Angeles county decks | $10 | not started | |
| R3 | Towns along the three drives | $25 | done: 60 checked cards, 16 towns | $18 |
| R4 | Road stretches, both directions | $20 | done: 21 checked cards, 12 stretches | $13 |
| R5 | Sights | $40 | not started | |
| R6 | Landscape units | $25 | done: 43 checked cards, 12 units | $12 |
| R7 | California and Mojave region deck | $20 | not started | |
| | **Total** | **$250** | | **$50** |

### Ridgecrest to Paso Robles (owner's route, 2026-10-04)

The route: Inyokern, CA-14 south past Red Rock Canyon and Mojave, CA-58 over Tehachapi Pass to
Bakersfield, I-5 north to exit 278, CA-46 west through Cholame and Shandon to Paso Robles, then
Nacimiento Lake Drive and Chimney Rock Road to Adelaide. 237 miles, about 4h15.

The first 70 miles are already covered by the Ridgecrest phases — 57 cards as far as Mojave.
Everything after Tehachapi is bare: **167 miles, about 2h50, with one card in it.**

Costs below are built on what the earlier phases actually ran: $0.31 a card on average, with
road stretches dearer at about $0.62.

| Phase | Batch | Cards | Cap | Status | Actual |
|---|---|---|---|---|---|
| P1 | Tehachapi Pass and crest: Mojave to Keene. Tehachapi and Keene towns, the Loop, the wind farm, the 1952 earthquake, Monolith, Cameron, the Cesar Chavez monument | ~22 | $12 | done: 23 checked cards, 7 subjects | $0 cloud |
| P2 | Caliente to Bakersfield: Caliente, Bena, Edison, the Bakersfield town deck, and the Bakersfield Sound as the first `person` cards | ~24 | $12 | done: 24 checked cards, 6 subjects (incl. 6 person cards) | $0 cloud |
| P3 | West Kern and I-5: Buttonwillow, Lost Hills oilfield, Kern National Wildlife Refuge, the California Aqueduct | ~14 | $8 | done: 14 checked cards, 7 subjects | $0 cloud |
| P4 | CA-46, Lost Hills to Shandon: Cholame and James Dean, the San Andreas crossing, Antelope Grade, Shandon, Estrella | ~14 | $8 | done: 13 checked cards, 6 subjects | $0 cloud |
| P5 | Paso Robles and Adelaide: the town, the 1886 hot springs, the 2003 earthquake, the wine district, the Santa Lucia Range, Nacimiento | ~18 | $10 | done: 20 checked cards, 7 subjects (incl. 1 person card) | $0 cloud |
| P6 | San Luis Obispo county deck (new county; the app has no county-level fallback west of Kern) | ~15 | $8 | done: 15 checked cards, 1 subject | $0 cloud |
| P7 | Road stretches, both directions: CA-58 over the pass, the I-5 leg, both CA-46 legs | ~12 | $10 | done: 13 checked cards, 6 stretches (7 per direction) | $0 cloud |
| | **Total** | **~119** | **$68** | | |

**Recommended first tranche: P1 and P2 only — about 46 cards, $24.** That fills Mojave to
Bakersfield, roughly 75 miles and an hour and a quarter of the gap, and it is the richest ground
on the route. Stop there, drive it, and judge three things before opening P3:

1. Whether the density feels right, which decides how many cards the rest of the route needs.
2. Whether the `person` cards clear the notability bar in PLAYBOOK.md §3a. Bakersfield is the
   right test: Buck Owens and Merle Haggard are obvious, and the long tail after them is not.
3. Whether the pipeline generalises off the Mojave. Every card so far is desert. Tehachapi crest,
   Central Valley farmland and the Coast Ranges are the first real test of that.

## Rules

1. Sessions are started by hand, one at a time, only after the owner's go-ahead. No
   scheduled, recurring, or parallel runs.
2. One session works one named batch, then commits and stops. It never starts another
   batch or retries in a loop.
3. Page-fetch budgets in `PLAYBOOK.md` §2 are hard limits. On reaching one, commit what is
   finished and stop.
4. After every session the owner reads the cost from the Claude usage page and it is
   recorded in the ledger below. No session starts unless the remaining budget covers its
   phase cap plus 20%.
5. If any phase runs more than 25% over its cap, set `STATUS: HALT` and re-plan before
   any further spending.
6. After Phase 1, stop and review cost per card and quality. If the projected total for the
   pilot exceeds $250, shrink the plan before continuing.

## Ledger

| Date | Session | Phase | Cards | Cost | Remaining |
|---|---|---|---|---|---|
| 2026-10-03 | Phase 1 McKinley county deck (incl. two blocked-network attempts) | 1 | 9 | $2 | $248 |
| 2026-10-03 | Phase 1 re-run, run in the owner's local Claude Code session (not cloud credit): writer 36 fetches, checker 37 | 1 | 25 | $0 cloud | $248 |
| 2026-10-03 | R1 Kern County deck (cloud, Sonnet): writer 38 fetches, checker ~31 | R1 | 30 | $5 | $243 |
| 2026-10-03 | R3 towns (cloud, Sonnet): 16 towns, writer 83 fetches, checker 80 | R3 | 60 | $18 | $225 |
| 2026-10-03 | R4 stretches (cloud, Sonnet): 12 stretches, writer ~50 fetches, checker ~44 | R4 | 21 | $13 | $212 |
| 2026-10-03 | R6 landscape (cloud, Sonnet): 12 units, writer ~58 fetches, checker ~42 | R6 | 43 | $12 | $200 |
| 2026-10-04 | P1 Tehachapi Pass (run in the owner's local Claude Code session, not cloud credit): writer 30 fetches, checker 36 | P1 | 23 | $0 cloud | $200 |
| 2026-10-05 | P2 Caliente to Bakersfield (owner's local Claude Code session, not cloud credit): written 2026-10-04, independent re-check 2026-10-05 (99 sources opened for P2 and P3 together) | P2 | 24 | $0 cloud | $200 |
| 2026-10-05 | P3 West Kern and I-5 (owner's local session, not cloud credit): one card dropped in check (farm acreage from prose) | P3 | 14 | $0 cloud | $200 |
| 2026-10-05 | P4 CA-46 Lost Hills to Shandon (owner's local Claude Code session, not cloud credit): writer ~45 fetches, checker re-opened every source | P4 | 13 | $0 cloud | $200 |
| 2026-10-05 | P5 Paso Robles and Adelaide (owner's local Claude Code session, not cloud credit): writer 29 fetches, checker re-opened every source | P5 | 20 | $0 cloud | $200 |
| 2026-10-05 | P6 San Luis Obispo county deck (owner's local Claude Code session, not cloud credit): writer 28 fetches, checker re-opened every source | P6 | 15 | $0 cloud | $200 |
| 2026-10-05 | P7 road stretches (owner's local Claude Code session, not cloud credit): writer 14 distinct pages, checker re-opened every source; geometry from OSRM | P7 | 13 | $0 cloud | $200 |
