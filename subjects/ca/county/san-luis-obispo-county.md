# San Luis Obispo County, California (FIPS 06079): research notes

Phase P6 (Ridgecrest to Paso Robles corridor), writer session 2026-10-05. 15 county cards written, before the §9 check. Focus: the county's north end along CA-46 (see corridors/ridgecrest-paso.json), plus county-wide cards. These cards are the county-level fallback west of Kern.

## Cards
- County-wide (facts file numbers): population (2024 ACS, TIGER land area), county-government (2022 Census of Governments, plus District 1 covering Cholame, Shandon, Paso Robles, Lake Nacimiento and "Adelaide"), climate (Paso Robles airport normals from the facts file plus SLO County Regional Airport July high from NOAA monthly normals), land-ownership (PAD-US 2024).
- County-wide (history and economy): formation (1850, original 27 counties, the name), crops (2024 crop statistics), wartime-growth (Camp San Luis Obispo, Camp Roberts, veterans, Cal Poly).
- North end, with `near`: mission-san-miguel (Mission San Miguel Arcángel, 40 km radius), camp-roberts (40 km radius).
- People: salinan (tribe's own site plus Wikipedia), northern-chumash (yak titʸu titʸu yak tiłhini Northern Chumash Tribe's own site plus Wikipedia). No ceremonies or sacred-site details; Painted Rock's seasonal closure is noted on the Carrizo card.
- Elsewhere cards (open on the county, `{distance}` plus `elsewhere`): valley-of-the-bears (Mission San Luis Obispo), hearst-castle (opened from Highway 46 running to the coast), carrizo-plain, diablo-canyon (brief).
- All cards carry `pronunciations` for "San Luis Obispo" only, from the Wikipedia county article's lead: `{{IPAc-en|s|æ|n|_|ˌ|l|uː|ɪ|s|_|oʊ|ˈ|b|ɪ|s|p|oʊ}}` and `{{respell|san-lu-is-o-bis-po}}` (wikitext, rev 1378174865). The card value copies both verbatim: "san-lu-is-o-bis-po (IPA: sæn ˌluːɪs oʊˈbɪspoʊ)". No stress-marked respelling was invented.

## Fetch tally
28 of 40 page fetches used (failed and wasted fetches counted):
1-9. Wikipedia via API: San Luis Obispo County (rev 1378174865); Mission San Luis Obispo de Tolosa (1367607125); Mission San Miguel Arcángel (1367607146); Camp Roberts (disambiguation page, wasted); Hearst Castle (1371505759); Carrizo Plain (1376570656); Salinan (1374717392); California State Route 46 (1374511198); Diablo Canyon Power Plant (1378430788).
10. Wikipedia Camp Roberts, California (1377260646).
11. slocounty.ca.gov About the County.
12. yttnorthernchumashtribe.com home page.
13. salinantribe.com home page.
14. counties.org county profile (no usable text).
15. Wikipedia San Luis Obispo, California (1378598760).
16-17. accessgenealogy.com (Cloudflare block, plus a header check).
18. newadvent.org (wrong article, wasted).
19. factcards.califa.org Pedro Fages.
20. BLM Carrizo Plain National Monument page.
21. militarymuseum.org/CampRoberts.html (empty, wasted).
22. militarymuseum.org/campbob.html (California State Military Museum, Camp Roberts).
23. parks.ca.gov Hearst San Simeon State Historical Monument.
24. California Senate Energy committee background paper on Diablo Canyon (PDF, read locally).
25. NPS article on Mission San Miguel Arcàngel.
26. slocounty.ca.gov 2024 crop statistics news release.
27. NOAA NCEI monthly normals, USW00093206 (SLO County Regional Airport).
28. Wikipedia county article wikitext (for the pronunciation template).
About 10 web searches, not counted.

## Caveats the checker should know
- Wikipedia quotes were taken from the API plain-text extract of the stated revision; the NOAA SLO station name is not in the API response (the station ID is USW00093206, and the Wikipedia county article gives the same 78.0 F July figure for SLO County Regional Airport).
- Facts-file sources use synthetic quotes in the Kern style ("B01003 Total population, San Luis Obispo County: 281,555"); values are copied from facts/ca/06079.json.
- Carrizo monument date: BLM says created January 17, 2001; Wikipedia says Clinton proclaimed it January 12, 2001. The card says only "in 2001".
- Valley of the bears: two Wikipedia articles (mission and city) plus a schools fact card ("one story tells that Fages organized a grizzly bear hunt"). The fact card frames it as a story and garbles who was starving; the card relies mainly on the city article for "dried bear meat ... sent north". The 1769 naming is reported as "llano de los osos" (mission article) and "Cañada de Los Osos" (city article); the card says only that soldiers named a valley for bears. Confidence 4.
- Formation: "obispo is Spanish for bishop" rests on the two articles glossing "obispo de Tolosa" as "bishop of Toulouse". No source found that says the county was named *for* the mission, so the card says it *shares* the name.
- Diablo Canyon card tagged `voting` for the protest/political-controversy line.
- Camp Roberts tagged `tragedy` for Corporal Roberts's death.
- Salinan card: the tribe's site and Wikipedia disagree on the language (Hokan group vs language isolate, and spoken "until the 1950s" vs still spoken); the card leaves language out. "We are still here" is quoted from the tribe's site.
- County-government card spells the place "Adelaida" as on other cards; the county page writes "Adelaide".

## Dropped or not used
- Carrizo Plain "largest single native grassland remaining in California": Wikipedia only; BLM says only "a remnant remains". Dropped (two-source rule).
- Mission San Luis Obispo "only L-shaped mission church in California": Wikipedia only. Dropped.
- Camp Roberts "one of only a few military posts named for an enlisted man", "largest parade ground": Military Museum only. Dropped.
- Hearst Castle visitor numbers: Wikipedia says about 750,000 a year, the county page says over one million. Dropped.
- Diablo Canyon "nearly two thousand arrests in two weeks in 1981": Wikipedia only. Dropped.
- 1850 county population of 336 and first sheriff Henry J. Dalley (Sheriff's historical report PDF, seen only in search snippets, not fetched).
- Cabernet Sauvignon acreage second only to Napa (2025): Wikipedia prose, no table fetched.
- Caliente Mountain, 5,106 feet, highest point in the county: Wikipedia prose only, no USGS figure fetched.
- Morro Rock (Lesa'mo' to the Salinan Tribe; tribe says "we, the Salinan Tribe, belong to Morro Rock"): not used, close to sacred-site territory; possible coast card later with care.
- 1844 grants to Indigenous residents of San Miguel (Las Gallinas, El Nacimiento, La Estrella) later rejected by U.S. courts: good lead for a north-county card (Wikipedia county article only).
- Japanese American removal in 1942, Port San Luis oil, railroad dates (Paso Robles railroad card already covers 1886).

## Facts-file notes
- Used: population, median age, median household income, median home value, land area, county spending, full-time employees, property tax, Paso Robles July high, January low, snowfall (0.0), PAD-US shares and largest units.
- Not used: annual precipitation (12.15 in, already on the Santa Lucia rain-shadow card), annual mean temperature, sales tax, part-time employees, payroll.

## Checker pass (2026-10-05)
- 15 cards checked, 15 kept, 0 sentences removed. All quotes confirmed verbatim against the stated Wikipedia revisions and live pages (two stray spaces before commas fixed in the Camp Roberts and county-government quotes).
- NOAA: SLO airport July normal 78.0 F confirmed (USW00093206, SAN LUIS OBISPO AP). Paso Robles July high and January low re-sourced to the monthly normals URL; the annual/seasonal URL in the facts file does not carry those two values.
- Crops: figures confirmed in the 2024 Annual Crop Report Top 10 table (total $1,015,871,000; wine grapes down 40% across all varietals); report added as a source.
- Valley of the bears: both Wikipedia passages on the hunt are marked citation needed. Re-framed as a story ("the story goes", "is said to"), the mule-load detail dropped, and the California State Military Museum Fages page added (1st land expedition, 1769; hunting bears for meat at San Luis Obispo, 1772).
- County government: District 1 sentence cut to Cholame, Shandon and Paso Robles (the county page lists communities, not the highway, and spells Adelaida "Adelaide").
- Mission San Miguel: "never retouched" now has a second source (Wikipedia nickname "The Unretouched Mission").
