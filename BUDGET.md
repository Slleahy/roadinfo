STATUS: GO

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
| R1 | Kern County deck (county level, eastern Kern focus) | $10 | **open** | |
| R2 | San Bernardino and Los Angeles county decks | $10 | not started | |
| R3 | Towns along the three drives | $25 | not started | |
| R4 | Road stretches, both directions | $20 | not started | |
| R5 | Sights | $40 | not started | |
| R6 | Landscape units | $25 | not started | |
| R7 | California and Mojave region deck | $20 | not started | |
| | **Total** | **$250** | | **$2** |

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
