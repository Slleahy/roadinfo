# McKinley County, New Mexico (FIPS 35031): research notes

Phase 1 calibration batch. 9 cards written (target was up to 40); all 9 passed the §9 check.

## Method and limits
- The fetch budget (about 15 per county) was spent: ~15 attempts, 7 successful pages.
- The first sessions ran with Wikipedia and most official hosts blocked by the egress proxy; the network was opened later.
- Checker (separate subagent) made 6 further fetches, one per distinct cited URL.

## Sources used
- Wikipedia, McKinley County, New Mexico (read 2026-10-03; revision id not captured)
- Wikipedia, Church Rock uranium mill spill
- New Mexico Association of Counties, McKinley County page (nmcounties.org)
- Census Reporter API (republishes ACS 2024 5-year, tables B01003 and B19013)
- National Park Service, Chaco Culture NHP history page
- Navajo Nation, History page (navajo-nsn.gov)

## Open issues
- RESOLVED LEAD (owner, 2026-10-03): created February 23, 1899, by the New Mexico Territorial Legislature; county government organized January 1, 1901. Still needs a citation: 1899 territorial session laws, NM State Records Center and Archives, or the county's own history page. Use both dates in the namesake card once cited.
- Creation date conflict: Wikipedia and nmcounties.org say 1901; a search-result snippet said 23 February 1899. Cards avoid the date. Needs an official source (NM State Records Center, session laws).
- Church Rock cards rest on one source (Wikipedia), confidence 3. Governor's refusal and English-only warnings are the claims that would need a second source under the two-source rule. Wikipedia gave about 93 million gallons; the card says "more than 90 million".
- Population and income come via Census Reporter, not census.gov directly (census.gov and api.census.gov were not usable: 403 / API key required).
- Chaco: McKinley County containing part of the park is Wikipedia-only.

## Not sourced (no table or second source obtained)
- NOAA 1991-2020 climate normals (NCEI service returned 400; only a secondary site was seen via search: Gallup airport about 10.7 in precipitation, 33.8 in snow. Not used).
- Census of Governments county spending and employees.
- Elevation (USGS), PAD-US land ownership, MIT election results.
- Geology and landscape at county scale; Mount Taylor / Tsoodził; Zuni Pueblo and Zuni reservation in the county.

## Leads not used
- Language: Navajo most spoken at home; one of very few US counties where neither English nor Spanish leads (Wikipedia only; needs ACS table plus second source).
- Gallup railroad origin (1881), El Rancho Hotel, Route 66 (town/sight level, Phase 2).
- Ambrosia Lake uranium district (Wikipedia page URL returned 404; find correct page).
- Navajo Code Talkers, Fort Wingate, Wingate boarding schools, Gallup-McKinley County Schools.
- Church Rock second sources: newmexicohistory.org (DNS failed), EPA (404 on guessed URL), ippnw PDF, Beyond Nuclear.
- Election history: Democratic since 1932 (Wikipedia prose; use MIT data).
