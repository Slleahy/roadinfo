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
| 1 | Calibration: McKinley County, county deck only | $15 | **open** | |
| 2 | McKinley County: towns, sights, road stretches | $55 | not started | |
| 3 | Cibola County: all levels | $55 | not started | |
| 4 | Landscape decks along the corridor (shared statewide) | $40 | not started | |
| 5 | New Mexico region deck | $35 | not started | |
| — | Reserve for fixes and re-checks | $50 | held | |
| | **Total** | **$250** | | **$0** |

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
| | | | | | $250 |
