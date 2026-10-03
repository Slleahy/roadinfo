# Kern County, California (FIPS 06029): research notes

Phase R1 (Ridgecrest home drives), writer session 2026-10-03. 30 county cards written, before the §9 check. Focus: eastern Kern County (see corridors/ridgecrest-home.json), with 7 county-wide cards (namesake, formation, population, climate, county government, land ownership, oil).

## Cards
- County-wide: namesake, formation, population, climate, county-government, land-ownership, kern-river-oil.
- China Lake: china-lake-founding, china-lake-size, sidewinder, ridgecrest-earthquakes, ridgecrest-earthquakes-base.
- Water: indian-wells-valley-water, indian-wells-valley-pistachios.
- Walker Pass and the Kern River valley: walker-pass, isabella-dam, isabella-dam-safety, kern-river-preserve.
- El Paso Mountains and Red Rock: red-rock-canyon, red-rock-films, burro-schmidt-tunnel.
- Rand district: randsburg-gold.
- Mojave, Edwards: mojave-spaceport, voyager, mojave-airport-origins, mojave-borax, edwards-yeager, edwards-size.
- Native peoples: tubatulabal, kawaiisu.
- Facts file numbers (facts/ca/06029.json) used in population, climate, county-government, land-ownership, china-lake-size, edwards-size. Not used: snowfall (missing in file), median home value is used; elevation samples (Walker Pass card uses the Wikipedia figure of 5,250 feet instead of the sampled 5,149).

## Fetch tally
38 of 40 page fetches used (failed fetches counted): Wikipedia Kern County; Wikipedia NAWS China Lake; chinalakemuseum.org (404); Wikipedia 2019 Ridgecrest earthquakes; Wikipedia Walker Pass; cnic.navy.mil history (403); Wikipedia Burro Schmidt Tunnel; DesertUSA Burro Schmidt; Ridgecrest IWVGA press release PDF (read locally with pypdf); Inyo County press release PDF (read locally); Wikipedia Red Rock Canyon SP; Wikipedia Randsburg; Wikipedia Isabella Dam; Wikipedia Mojave Air and Space Port; Wikipedia Edwards AFB; Wikipedia Jawbone Siphon (404); Wikipedia Tübatulabal; kern.audubon.org node 4301 (redirect); Wikipedia Kern River Preserve; Wikipedia Kawaiisu; Wikipedia Coso Rock Art District; Wikipedia Mojave; Wikipedia Rosamond; audubon.org California page (no preserve content); Wikipedia El Paso Mountains; Wikipedia Los Angeles Aqueduct; Wikipedia Harmony Borax Works; OHP Rand Mining District; navair.navy.mil Sidewinder (403); stormwater.com Isabella press release; parks.ca.gov Red Rock; encyclopedia.com Tubatulabal; edwards.af.mil history (403); NPS Harmony Borax Works; Wikipedia William B. McLean; kern.audubon.org node 4331 (redirect, not followed); Wikipedia Kern River Oil Field; NARA Unwritten Record (Yeager). About 15 web searches (not counted as fetches).

## Caveats the checker should know
- WebFetch returns a model-written summary, not the raw page. Quotes in the cards are the passages the tool reported in quotation marks, joined with "...". Two sources carry bracketed notes saying the wording came from a fetch summary and should be confirmed on the page: county formation (Kern County, Wikipedia) and five supervisors / four-year terms.
- The IWVGA (Indian Wells Valley Groundwater Authority) press release is a party's statement in a lawsuit. The pistachio card relies on it alone (confidence 3).
- Sidewinder: "1950" (NAWS) and "led the project team from 1945 to 1954" (McLean) both appear in the card; the card keeps both as stated by each source.
- Voyager: the year 1986 is the only date used. The Mojave airport page lists confusing dates for the flight record, so no day or month is given.
- Burro Schmidt: sources disagree on how long it took (38 years vs 33), so the card gives only the start (1906) and finish (1938) years from Wikipedia.
- Tübatulabal band spelling: Encyclopedia.com has "Palegawan"; other sources spell it "Palagewan". Card uses the Encyclopedia.com spelling.
- No tribal government source was found for the Tübatulabal or the Kawaiisu (no official site turned up in searches). Both cards rely on Wikipedia and one other source; no ceremonial or restricted knowledge is described.
- Pronunciations: none added. No source gave one for Kawaiisu, Tübatulabal, Havilah, Inyokern, Muroc, Garcés, or Yeager, and the playbook bars guessing.

## Leads not used (budget or sourcing)
- Coso Rock Art District and Little Petroglyph Canyon: Wikipedia counts disagree (more than 50,000 vs over 100,000 petroglyphs) and no fetched source places the canyon in Kern County (the Navy base spans several counties). Left for the Inyo/landscape layer; tours are run by Maturango Museum in Ridgecrest and need Navy permission.
- Jawbone Siphon and the Los Angeles Aqueduct: Wikipedia Jawbone_Siphon is a 404, and the Aqueduct article has no Kern-specific text. Mojave as aqueduct construction headquarters is mentioned in the mojave-borax card (one source).
- Twenty-mule team composition (eighteen mules and two horses): Wikipedia Harmony Borax Works only; the NPS page did not confirm it. Dropped under the two-source rule.
- Sidewinder "most used and most copied" and "first truly effective" claims: one source each; dropped.
- Isabella Dam "among the highest-risk dams" claim: Wikipedia only (the Corps press release did not say it); dropped.
- Rand silver mine "produced more silver than any mine in California" (Wikipedia only); dropped. Atolia tungsten (1907) and the California Rand Silver Mine at Red Mountain (1919) are in San Bernardino County; left for the R2 San Bernardino deck.
- Mojave Narrows, Tehachapi wind farms, Tehachapi Loop, 1952 Kern County earthquake (7.3, 12 deaths per Wikipedia Kern County): not researched.
- Rosamond: name origin and Willow Springs stagecoach stop are in Wikipedia; the Tropico Gold Mine did not appear in the fetched article. Left for the towns layer.
- California City, Ridgecrest naming, Inyokern, Freeman Junction, Cantil, Onyx, Weldon, Mountain Mesa: town layer (R3).
- Last Chance Canyon / El Paso Mountains: Wikipedia El Paso Mountains has little; Black Mountain 5,244 feet, Last Chance Archaeological District on the National Register.
- Kern River and Lake Isabella boating, Kernville: only touched through Isabella Dam.
- Secondary source suggestions: Maturango Museum (Ridgecrest), Kern County Museum, BLM Ridgecrest Field Office pages, Audubon California Kern River Preserve page (the kern.audubon.org node redirects to a page without preserve text).

## Facts-file notes
- annual_snowfall missing in the facts file; no snowfall claims made.
- Climate figures are from the China Lake NAF station, which is in eastern Kern County; the card says so.

## Checking pass (separate checker agent, 2026-10-03)
- 30 of 30 cards survived; 5 sentences removed across 4 cards (china-lake-size 1, kern-river-oil 1, mojave-spaceport 2, walker-pass 1), about 10 wording edits, quotes rewritten to verbatim page text on 24 cards.
- Removed for failing the two-source or table rule: Navy 85 percent land share, first commercial well, spaceport licence "first", airport elevation, Walker Pass elevation.
- Voyager now says built in Mojave, flown December 1986; spaceport s2 is now The Register (2004); Voyager s2 is the Smithsonian NASM page.
- Checker used about 31 of 40 fetches (its own count could not be fully reconciled); writer used 38.
- Still single-source: pistachio card (party press release), Walker Pass "unaltered" line, Tübatulabal and Kawaiisu (Wikipedia plus one other; no tribal-government source found).
