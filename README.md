# roadinfo

An open, sourced database of spoken road-trip narration for the United States: what a
knowledgeable passenger would tell you about the land, towns, roads, and history you are
driving through. Built for the Road Savant iOS/CarPlay app, published openly so anyone can
use, check, and improve it.

## What's in it

Short spoken items called **cards**, each 2 to 5 sentences, written to be heard rather than
read. Every card is anchored to a place on the map and carries silent citations for every
sentence, so any fact can be traced to its source.

Cards come in six levels, from most local to most general. A narrator plays the most local
good card available and falls back to wider levels, so a drive is never left in silence.

| Level | Covers | Anchored to |
|---|---|---|
| `sight` | Landmarks, historic sites, peaks, odd roadside things | A point, with a reach |
| `stretch` | A stretch of road, per direction; historic trails like Route 66 | A road segment |
| `town` | A city, town, or community | A Census place |
| `county` | County history, government, economy, facts | A county (FIPS code) |
| `landscape` | Geology, ecoregion, watershed, climate | A landscape unit |
| `region` | State and regional history and themes | A state or region |

## Status

Pilot: **I-40 in New Mexico, Arizona state line to Acoma** (McKinley and Cibola counties).
See [`corridors/i40-nm-west.json`](corridors/i40-nm-west.json).

## How it's made

Cards are researched and written by an AI agent following [`PLAYBOOK.md`](PLAYBOOK.md):
it starts from Wikipedia, follows promising links, searches local and official sources,
takes numbers only from official data tables, and scores each card for relevance and
interest. A separate checking pass confirms every sentence against its cited source and
drops anything it cannot confirm.

## License

The narrative text is adapted in part from Wikipedia and is licensed under
[CC BY-SA 4.0](LICENSE). Each card lists its sources. Facts from U.S. government data
tables are public domain; see each card's citations for origins.

Corrections are welcome as issues or pull requests. Please cite a source.
