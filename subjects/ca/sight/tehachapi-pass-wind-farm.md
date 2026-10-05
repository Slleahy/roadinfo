# Tehachapi Pass Wind Farm (sight): research notes

Phase P1, writer session 2026-10-04. 3 cards written, the sight cap. Before the §9 check.

## Cards
- half-the-states-wind, generations-of-turbines, the-wire-not-the-wind.
- `near` is 35.102222, -118.282778, radius 18,000 m, from the Wikipedia article's coordinates. The
  radius is deliberately wide: the turbines are visible for miles along State Route 58 and the
  Alta plant extends west towards Monolith.
- Avoided repeat: the existing landscape card `ca-landscape-tehachapi-mountains-pass-wind-01`
  already carries the venturi effect, the early-1980s start, James Dehlsen and Zond, the Storm
  Master failure and the switch to Danish machines. None of that is repeated here.

## Fetch tally
4 of 5 used: Wikipedia Tehachapi Pass Wind Farm; Wikipedia Tehachapi Pass; Wikipedia Alta Wind
Energy Center; California Wind Energy Association fast facts.

## Sources found
- `https://www.calwea.org/fast-facts` — the one real table source for wind numbers found this
  session: "Wind energy projects totaling over 6,171 megawatts (MW) of capacity are operating in
  California today", "Kern County (Tehachapi - Antelope Valley) 3,254", and 2024 generation of
  15,761 GWh, 7.3% of in-state generation. The page says the data is "compiled by CalWEA primarily
  from the U.S. Wind Turbine Database V8.3 (March 25, 2026)" with a California Energy Commission
  figure of 6,194 MW as of Q4 2024. Recorded in the card's source `table` field.
- `https://en.wikipedia.org/wiki/Alta_Wind_Energy_Center` — commissioned 2010, 1,550 MW, 600
  turbines, Terra-Gen Power.
- `https://en.wikipedia.org/wiki/Tehachapi_Pass_Wind_Farm` — multiple generations of turbines up to
  3 MW; the Tehachapi Renewable Transmission Project, 4.5 GW, 2008 to 2016, allowing 10 GW.

## Deliberately left out
- **"Largest wind farm in the United States."** Wikipedia says Alta held that title as of 2022, but
  §5 wants two independent sources for a superlative and only one was found. Dropped. A second
  source (an Energy Information Administration table, say) would make it a strong card.
- **3,400 turbines and 3,200 acres** for the older Tehachapi Pass farm. Prose on Wikipedia with
  differing dates, and the R6 checker already declined these figures once. Still declined.
- The USGS U.S. Wind Turbine Database API at `eersc.usgs.gov/api/uswtdb/v1/turbines` returned
  nothing for two query shapes from this machine. It is the right source for an exact turbine count
  in Kern County and is worth one attempt from a different network.

## Open questions
- `asOf` on the Kern County capacity card is set to 2026, the database vintage, while the sentence
  about generation states 2024 explicitly. A checker may want these split into two cards.
- The pass's own elevation is given two ways by Wikipedia: 3,771 feet at the narrows and 4,031 feet
  at the actual high point just east of town. No card uses either; a named high point wants a USGS
  figure under §6.

## Checking pass, 2026-10-04
- **The Alta sentence came out.** It claimed Alta was "the newest of them" and sat "on the western
  side" of the pass. Neither is in the Alta article: it gives coordinates of 35.02111, -118.32056,
  describes the project as running west from State Route 14 at Mojave along Oak Creek Road, and the
  Tehachapi Pass article says the pass is still being repowered, so nothing there is "newest".
  Replaced with two facts the Tehachapi Pass article does carry: development started in the early
  1980s under James Dehlsen and Zond Corporation, and about 3,400 turbines stand there now. The
  Alta citation was removed from the card.
- **The "first large-scale wind farm in the U.S." claim was deliberately left out.** Both the
  Tehachapi Pass and Alta Wikipedia articles say it, but they are not independent of each other, so
  it does not clear the two-source bar for a "first". Worth a card if an Energy Department or CEC
  page says it.
- **Alta's 1,550 MW is a nameplate figure** that includes units beyond what is built, which is the
  other reason it is now out of the deck.
- CalWEA checked out word for word: 6,171 MW operating statewide, 3,254 MW in the
  "Kern County (Tehachapi - Antelope Valley)" row, and "In 2024, California wind projects generated
  15,761 gigawatt-hours (GWh) of electricity – 7.3% of all power generated within California", from
  the U.S. Wind Turbine Database V8.3 of 25 March 2026. The card's sentence was reworded from "Wind
  projects in Kern County" to "here and out in the Antelope Valley", because that is what the row
  actually covers and the Antelope Valley is mostly in Los Angeles County.
- The wind farm's `near` point (35.102222, -118.282778) is Tehachapi Pass's own coordinate, and it
  appears in the Tehachapi Pass Wind Farm infobox too. Correct.
