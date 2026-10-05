# Bakersfield (town): research notes

Phase P2, writer session 2026-10-04. 6 cards written, before the §9 check. Town cap is 8.

The Bakersfield Sound is held in a separate deck, `subjects/ca/sight/bakersfield-sound.md`, and the
biography cards in `subjects/ca/person/bakersfield-people.md`, so three decks do not tell the same
story in the same place. The town cards point at them with `followOn`.

## Where it is relative to the drive
`near` is 35.373333, -119.018889 (the Wikipedia infobox coordinates) with a radius of **15,000 m**,
not the usual 8,000. State Route 58 runs through the south side of the city and then west toward
Interstate 5, so an 8,000 m radius centred on downtown would drop the cards for most of the drive
through town. Bakersfield had 403,455 people at the 2020 census; the wider radius is proportionate.

## Cards
- bakers-field, fire-of-1889, 1952-aftershock, dry-river, kern-river-oil, okie-camp.
- fire-of-1889 and 1952-aftershock are a deliberate pair: the town rebuilt in brick after the fire,
  and the 1952 aftershock took the brick buildings down. fire-of-1889 carries a `followOn` to it.
- kern-river-oil uses `elsewhere` for the Kern River Oil Field (35.4564, -118.9834) and okie-camp
  uses `elsewhere` for Weedpatch Camp (35.223056, -118.905278). Both say `{distance}`.
- The county deck already has `ca-kern-county-kern-river-oil-01` on the 1899 discovery at 70 feet.
  The town card deliberately avoids repeating the discovery and is about the scale and the steam.

## Fetch tally
**12 of 12 used — the limit was reached and the subject was closed.**
1. Wikipedia *Bakersfield, California* (rev 1376434309)
2. Wikipedia *Bakersfield, California* again, for the History, Kern River, Dust Bowl and
   Bakersfield Sound passages verbatim
3. Wikipedia *1952 Kern County earthquake*, for the Bakersfield passages
4. Wikipedia *List of people from Bakersfield, California*
5. Wikipedia *Great Bakersfield Fire of 1889* (rev 1360496566)
6. Wikipedia *Kern River Oil Field* (rev 1357295056)
7. Wikipedia *Arvin Federal Government Camp* (rev 1372308346)
8. National Park Service, *Weedpatch Camp*
9. Census Reporter, Bakersfield city profile
10. Wikipedia *Kern River* (rev 1375917296)
11. `bakersfield.com` "A (brief) history of Bakersfield" — HTTP 429, wasted
12. `britannica.com/place/Bakersfield` — HTTP 403, wasted

Two of twelve went to throttled or blocked pages, which is why the deck has no non-Wikipedia source
for the fire, the quake or the river. Budget for that next time.

## Sources found
- **Wikipedia Bakersfield** — Thomas Baker, "a lawyer and former colonel in the militia of Ohio",
  moving to the banks of the Kern River in 1863; "what became known as Baker's Field, which became a
  stopover for travelers"; 600 people by 1870 and "becoming the principal town in Kern County"; the
  Kern River's alluvial plain, the vast wetlands and seasonal lakes, the diversions into canals, and
  "Diverting the river's flow has left 30 miles (48 km) of the riverbed that runs through Bakersfield
  dry"; the Bakersfield Sound "commercially dominated the industry for over a decade"; census counts
  801 (1880), 2,626 (1890), 56,848 (1960), 174,820 (1990), 347,483 (2010), 403,455 (2020).
- **Office of Historic Preservation, CHL No. 382, Colonel Thomas Baker Memorial**, at city hall:
  "In 1863 Colonel Baker ... came here to found 'Bakers Field.' His motto was, 'Time will justify a
  man who means to do right.'" Fetched under the Caliente budget. This is the one non-Wikipedia
  source in the deck and it is what makes the founding card worth hearing.
- **Wikipedia Great Bakersfield Fire of 1889** — 7 July 1889; burned three hours; 196 buildings, one
  man killed, 1,500 homeless; began at a stove in a residence near 20th Street and Chester Avenue;
  "There was not enough water pressure in the line to deliver water to the fire"; rebuilt "larger
  and grander", mostly in brick.
- **Wikipedia 1952 Kern County earthquake** — in the main shock, "windows were broken and dislodged
  plaster littered residential and commercial districts, and the county jail was damaged"; the
  strongest aftershock, on 22 August, was magnitude 5.8; "Damage was especially heavy to brick
  buildings in Bakersfield, and although only a few buildings collapsed outright, 90 of 264
  buildings that the shock damaged needed to be brought down completely"; repercussions in the
  downtown unreinforced masonry "well into the 1990s".
- **Wikipedia Kern River Oil Field** — north-northeast of Bakersfield at 35.4564, -118.9834; close to
  2 billion barrels by the end of 2006, 9,183 active wells, Chevron the principal operator; steam
  flooding revived the field in the 1960s and made recoverable "much of the oil once considered
  unfeasible to recover". The production figures are the article's citation of California Department
  of Conservation data.
- **National Park Service, Weedpatch Camp** — "Arvin Farm Labor Supply Center"; running water for
  showers, bathrooms and laundry rooms and wood platforms for tents; the Joad family's stay in *The
  Grapes of Wrath*; the book dedicated to the camp's administrator Tom Collins; added to the
  National Register on 22 January 1996; **the site is not open to the public**.
- **Wikipedia Arvin Federal Government Camp** — the three surviving buildings (community hall, post
  office, library), 35.223056, -118.905278.
- **Wikipedia Bakersfield sound** — "The town, known mainly for agriculture and oil production, was
  the destination for many Dust Bowl migrants and others from Oklahoma, Texas, Arkansas, and parts
  of the Midwest."

## Conflicts and weak spots
- **Who built Weedpatch and when.** The National Park Service says the Works Progress Administration
  built it in 1935; Wikipedia says the Farm Security Administration in 1936. No card names a builder
  or a construction year. Resolve it from a Farm Security Administration record before adding one.
- **Nearly every card has a single publisher.** Wikipedia carries the fire, the quake, the river and
  the oil field. Confidence is set at 3 for the fire and the river accordingly. The Caltech Southern
  California Earthquake Data Center page already cited in the P1 Tehachapi card covers the main
  shock but not the August aftershock, so it was no help here.
- **No population card was written.** Census Reporter's Bakersfield profile defaulted to ACS 2024
  **1-year** estimates (population 417,461, median household income $82,093, median age 32.8), and
  §6 wants 5-year estimates. The decennial counts in the Wikipedia table would have worked but could
  not be quoted verbatim from the fetch, and with the fetch budget exhausted there was no way to
  confirm them. A population card is the obvious eighth card for this deck; it needs one clean fetch
  of the ACS 5-year table for place GEOID 16000US0603526.
- **Disincorporation was left out.** Bakersfield incorporated in 1873, disincorporated in 1876 over a
  quarrel with the city marshal, ran for 22 years under a citizens' council, and reincorporated on
  11 January 1898. That is the best odd fact in the city's history and it is in no card, because the
  only fetched source is Wikipedia and an unusual claim needs two. Search results point at Gilbert
  P. Gia's "Marshall Alex Mills and Bakersfield's Disincorporation of 1876" and at the Bakersfield
  Californian's own history, which dates the incorporation vote to 1874 rather than 1873. **This is
  the strongest single lead left in Bakersfield.**
- **"Fifth-largest majority-Hispanic city in the United States, with 53% of its population being
  Hispanic in 2020"** is in the Wikipedia article. It is a superlative needing two sources and would
  carry the `demographics` tag. Not used.
- The 1889 fire card says "It seems to have started when…" because the source says accounts vary and
  gives a best-supported view. The householder's name was left out: it adds nothing a listener needs
  and hands the voice a surname nobody can check.

## Leads not followed
- The **disincorporation of 1876** (see above).
- **Gordon's Ferry on the Kern River**, CHL No. 137, on China Loop near Round Mountain Road: a ferry
  run in the 1850s by Major Gordon, and an adobe that was a station on the Butterfield Overland Mail
  route from 1856 to 1860. The inscription is in hand from the Office of Historic Preservation
  listing. Strong sight card, and it is on the Kern River at the edge of town.
- **Garcés Circle** (CHL No. 277) at Chester Avenue and 30th Street, and the point where Francisco
  Garcés crossed the Kern River (CHL No. 278). The county deck already names Garcés in the
  `namesake` card.
- **The Bakersfield Sign**, the neon arch over Sillect Avenue at Buck Owens Boulevard: built 1949
  over Union Avenue and saved, moved and restored with money Buck Owens donated and raised. It has
  its own Wikipedia article. A visible-from-the-freeway sight card, and it ties the town to the
  music deck.
- **Bring Back the Kern.** The dry riverbed is live news: a 2021 lawsuit over the diversions, a fish
  kill counted at 3,033 dead fish over five miles by a CSU Bakersfield biologist, and Fish and Game
  Code 5937. A second card on the river could carry the present-day fight if a newspaper source is
  fetched. Keep it factual and avoid the advocacy framing.
- **Valley fever.** Hans Einstein of Bakersfield was the leading authority on it, and the disease is
  endemic to this soil. That is a real, useful thing for a driver in the valley to hear, handled
  carefully.
- **Carver Mead**, the Caltech pioneer of very-large-scale integrated circuit design, is listed as
  from Bakersfield. Possible person card if the article plainly says he is from here.
- Kern County's share of California oil production: search results range from 65 to 80 percent
  depending on what is being counted. **Do not write a figure without the CalGEM or Department of
  Conservation annual report table.**

## Names a voice may get wrong
Weedpatch, Oildale, Truxtun (not used), Garcés (not used), Havilah (not used), Checotah — which was
deliberately cut from the Merle Haggard card and replaced with "Oklahoma", because the town name
carried no part of the story.
No `pronunciations` field was added to any card.
