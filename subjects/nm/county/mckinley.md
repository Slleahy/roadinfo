# McKinley County, New Mexico (FIPS 35031): research notes

Phase 1 calibration batch, re-run (local session, 2026-10-02). 25 county cards, none checked yet.

## Cards
- Rewritten in the new voice (same ids): namesake, population (income merged in), chaco, church-rock-spill, church-rock-aftermath, westerns, navajo-homeland.
- Dropped: navajo-government-01 (about the internal structure of the Navajo Nation government, not the county); income-01 (merged into population-01).
- New: land-ownership, checkerboard, climate, county-government, elevation, continental-divide, railroad-route66, uranium-boom, uranium-church-rock-crownpoint, coal-field, coal-fires, coal-strike-1933, gallup-riot-1935, ceremonial, code-talkers, fort-wingate, zuni-reservation, language.
- "checked" removed from every card; all 25 need the §9 check.
- Unsourced pronunciations from the first run (Chaco, Puerco, Chinle, Shiprock, Navajo, Diné Bikéyah, Diné Bizaad) were removed. Kept only Diné (IPA from Wiktionary) and Shiwi'ma (IPA from Wikipedia, Zuni language).

## Fetch tally
36 of 40 page fetches used (failures counted): Wikipedia county page x2, Intermountain Histories, EPA Church Rock PDF (aborted), Science History Institute, Newberry Atlas, McLemore 2013 PDF, Wikipedia Uranium mining in NM, Navajo Times (404), UNM New Mexico Quarterly (403), Wikipedia Paddy Martinez, Census Reporter C16001, NARA Prologue, Wikipedia Fort Wingate, Visit Gallup Fort Wingate, ashiwi.org, zunitourism.com (certificate error), Wikipedia Zuni Indian Reservation, New Mexico Magazine, KUNM, gallupintertribalceremonial.com (domain now a gambling site), hmdb (403), Visit Gallup Ceremonial, NMBGMR OFR 530, EMNRD coal fire nomination, dinelanduse.org, NRC PDF (403), Wikipedia I-40 in NM, CLUI, Wikipedia Continental Divide NM, El Palacio, Encyclopedia.com, Gallup Film Office, NPS El Rancho, Wikipedia Zuni language, Wiktionary diné. About 20 web searches.
Two PDFs (McLemore 2013, OFR 530) and the EMNRD form fields were read locally with pypdf, from the copy WebFetch saved.

## Sources used
- Newberry Library, Atlas of Historical County Boundaries, NM county chronologies (act passed 23 Feb 1899, took effect 1 Jan 1901; N.M. Terr. Laws 1899, 33d assy., ch. 19)
- New Mexico Association of Counties; Wikipedia McKinley County
- Church Rock: Wikipedia; Intermountain Histories (BYU); Science History Institute, "On Poisoned Ground"
- Uranium: McLemore et al. 2013, NMGS Guidebook 64 (NMBGMR); Wikipedia Uranium mining in NM; Wikipedia Paddy Martinez
- Coal: NMBGMR Open-file Report 530 (2010); NM EMNRD AML coal fire nomination (2025); El Palacio "Strike and Struggle" (2025); Encyclopedia.com "Gallup Coal Strike"
- Code Talkers / Fort Wingate: National Archives Prologue blog (2022); Wikipedia Fort Wingate; Visit Gallup
- Zuni: New Mexico Magazine "Zuni Staying Power"; Wikipedia Zuni Indian Reservation; Wikipedia Zuni language
- Ceremonial: KUNM (2022); Visit Gallup event page
- Road: Wikipedia I-40 in NM; CLUI Land Use Database; Wikipedia Continental Divide NM
- Film: City of Gallup Film Office; NPS El Rancho Hotel page
- Land: Diné Nihi Kéyah Project; Navajo Nation History page; NPS Chaco history page
- Facts file (facts/nm/35031.json): ACS B01003, B01002, B19013, B25077; Census Reporter C16001 (fetched this session); TIGER land area; PAD-US 4.1; NOAA normals; Census of Governments 2022; USGS EPQS

## Open issues
- Church Rock (task 2): governor's refusal now has a second source (Intermountain Histories, BYU), but it says the governor was asked "to declare a state of emergency," while Wikipedia says "request disaster assistance." The card names both. "Warnings only in English" was REMOVED. The Science History Institute shows a warning sign in English, Spanish, and Diné, which contradicts it. The card now says the signs were in all three languages. The EPA-hosted NM health and environmental assessment PDF (semspub.epa.gov/work/06/1000720.pdf) failed to load; it may settle the volume figures and how the warnings were given.
- Spill and aftermath cards are no longer tagged `tragedy`: §7 defines it as loss of life, and no deaths are cited. Reviewer may prefer to keep the tag.
- Fort Wingate card: the years 1860 (Fort Fauntleroy at Bear Springs) and 1868 (Fort Wingate moved there) came from the Wikipedia fetch summary, outside the quoted text. Checker should confirm against the article's timeline.
- Zuni: the Pueblo of Zuni's own site (ashiwi.org) has no history or visitor text on its home page, and zunitourism.com failed with a certificate error. The Zuni card rests on New Mexico Magazine and Wikipedia. Prefer Zuni Tourism's "Rules of Etiquette" page when it can be reached.
- Halona:wa Idiwan'a and A:shiwi have no sourced pronunciation. A speech engine may misread the colons.
- gallupintertribalceremonial.com now serves a gambling site; do not cite it.
- Population, income, and language numbers come through Census Reporter, not census.gov.

## Dropped for lack of a second source, or disputed
- Navajo as the language most spoken at home (Wikipedia, 2000 census; "one of three counties where it is neither English nor Spanish"). No Census page naming Navajo was found: ACS C16001 lumps it into "other and unspecified languages." The language card says only that about half speak a language other than English, and that Spanish accounts for about 3,000 of them.
- Fort Wingate supplied 100 tons of Composition B to the Manhattan Project for Trinity (Wikipedia and Visit Gallup, likely not independent; the figure may be mixed up with the 100-ton TNT test).
- Church Rock as the largest release of radioactivity in US history (only "one of the largest," from Wikipedia).
- I-40's highest point in New Mexico at the Divide (Wikipedia gave Sedillo Ridge as a "highest point" east of Albuquerque; not resolved).
- Zuni language split "some 8,000 years ago"; 70 percent of Zuni households relying on art income (prose statistics, single source).
- Haystack Mountain's county: no source places it in McKinley County (one Wikipedia page says "Grants County," which is wrong). The card says only "near Grants."

## Leads not used
- Mount Taylor / Tsoodził: mostly Cibola; no source tying it to McKinley County was fetched. IPA [tsʰòːtsɪ̀ɬ] is on Wikipedia, Mount Taylor (not fetched).
- Gamerco as the Gallup American Coal Company's company town (Facebook/Visit Gallup only); Chihuahuita evictions (El Palacio, has detail).
- Ambrosia Lake subdistrict (more than 211 million lbs U3O8, McLemore Table 1): its county was not confirmed.
- Code Talkers' Gallup "Departure, May 4, 1942" marker (hmdb, 403); Gallup Navajo Code Talkers exhibit.
- Crownpoint: Eastern Navajo Agency headquarters, founded 1909-1910 by Samuel Stacher (Navajo Times, town level, Phase 2).
- Zuni Mountains and Bluewater Lake; Red Rock Park; Navajo-Gallup Water Supply Project (county scale, EMNRD gives 300 miles and 250,000 people).
- Election history: use MIT data, not Wikipedia prose.
- NRC page on the United Nuclear Corporation mill (nrc.gov info-finder) as an extra Church Rock source.

## Checker report (2026-10-03)

Checker pass per playbook §9. Every cited non-facts URL was opened (raw wikitext for Wikipedia, page text or PDF text otherwise) and each quote searched for. Facts-file figures were compared with facts/nm/35031.json, not refetched, except C16001, which is not in the facts file and was fetched from the Census Reporter API (ACS 2020-2024: 66,359 aged 5+; English only 33,918; Spanish 3,011; other and unspecified 28,340). All 25 cards kept; 0 deleted; 1 sentence removed; 12 sentences edited; quotes corrected on 14 cards. All cards validate against schema/card.schema.json.

Writer's flagged items:
- Fort Wingate 1860 and 1868: confirmed in the article's timeline ("1860: Fort Fauntleroy was established at Bear Springs (Ojo del Oso)"; "1868: Fort Wingate was moved back to the former site of Fort Lyon at Ojo del Oso"). Now quoted.
- Governor's refusal: the two sources differ. Wikipedia: asked the governor "to request that the president declare the site a federal disaster area"; Intermountain Histories: "to declare a state of emergency". The sentence now names both requests, and both are quoted.
- Warning-sign languages: the source is one AP photo caption of one sign ("A sign along the Rio Puerco warns residents in English, Spanish, and Diné"). Sentence narrowed from "signs went up" to one sign.
- Founding dates: confirmed verbatim in the Newberry atlas ("Act passed 23 February 1899; took effect 1 January 1901"). Note: on March 18, 1901 the county also gained land from Bernalillo, San Juan, and Valencia; the card does not need to say so.
- Language numbers: 48.9 percent non-English and 3,011 Spanish confirmed. The Zuni speaker count of about 9,500 is a prose figure, not from a table (§2.4, §6), so it was dropped.

Per card:
- ceremonial: kept, 1 edited. S3 "a large Native arts market" to "a Native arts marketplace"; the "country's most complete" wording was not confirmed. Both quotes replaced with verified wording.
- chaco: kept, no edits. Wikipedia quote corrected to the page's "(part)" list wording.
- checkerboard: kept, 1 removed. S3 (210,000 acres of allotments) removed: a land-ownership figure from prose, and about the eastern Navajo region, not the county. Quote trimmed and spelling "swathes" corrected.
- church-rock-aftermath: kept, 3 edited. S1 states both requests (see above). S3 narrowed to one sign; the Wiktionary citation was removed from that sentence (it is kept only for the pronunciation). S4: "just five months" contradicted. Wikipedia says the mill resumed November 2, 1979, after "fewer than four months"; Intermountain says five. Now "within months". Quotes corrected.
- church-rock-spill: kept, no edits. Intermountain quote corrected. Figures differ across sources (93, 94, or 95 million gallons; 1,000 or 1,100 tons). The card's "more than 90 million" and "about a thousand tons" cover all of them.
- climate: kept, no edits. Matches facts file.
- coal-field: kept, no edits. The EMNRD nomination says mining began in the "late 1880s", so it was dropped as a citation for S1 ("early 1880s"); NMBGMR OFR 530 supports it. EMNRD quote corrected.
- coal-fires: kept, no edits. All quotes verified.
- coal-strike-1933: kept, no edits. El Palacio quote was a paraphrase (it does not say "August 30"; the governor declared martial law "in August 1933"). Replaced with verbatim text. Encyclopedia.com quote corrected.
- code-talkers: kept, no edits. All quotes verified.
- continental-divide: kept, no edits. CLUI quote corrected ("Signs in the middle of the interstate mark the Divide at 7,275 feet").
- county-government: kept, no edits. Matches facts file.
- elevation: kept, no edits. 6,224 ft from facts file; 7,275 ft verified on Wikipedia and CLUI.
- fort-wingate: kept, 1 edited. S2 "Soldiers were first posted" to "An army post was set up". The timeline supports the 1860 fort, not that it was the first posting. Quote extended.
- gallup-riot-1935: kept, no edits. Both quotes replaced with verbatim text. Deaths: the sheriff and Velarde died at the scene, and Esquibel died April 12, so "the sheriff and two others died" holds.
- land-ownership: kept, no edits. Matches facts file.
- language: kept, 1 edited. S3 speaker count removed ("It is spoken mostly around Zuni Pueblo"). Wikipedia quote corrected.
- namesake: kept, no edits. All verified.
- navajo-homeland: kept, 1 edited. The Navajo Nation page does not contain "The Navajo people refer to themselves and their homeland as". S3 now says "Diné Bikéyah, or Navajoland, reaches into...". Quote replaced; Wiktionary citation removed from the sentence (kept for pronunciation).
- population: kept, 1 edited. "It is a young county" dropped; no comparison source. Matches facts file.
- railroad-route66: kept, 1 edited. CLUI gives 1880 as the year the railroad chose the pass, not the year it "came through". Sentence reworded.
- uranium-boom: kept, no edits. Superlative (most uranium of any U.S. district, 1951-1980) has two sources: McLemore 2013 and Wikipedia, which cites other works.
- uranium-church-rock-crownpoint: kept, 1 edited. S3: the source says the contamination "is being addressed by" the EPA, not cleanup "handled with" it. "Nearby" was dropped (unsourced). Units confirmed as lbs U3O8 (Table 1).
- westerns: kept, 1 edited. The NPS says both Griffith brothers encouraged moviemakers. Sentence and quote updated.
- zuni-reservation: kept, 1 edited. The magazine has the Middle Place as the place the ancestors searched for, not "their homeland". S1 is now framed as Zuni tradition, with Wikipedia (Zuni language) added for A:shiwi. Quote replaced with verified text (permits, ceremonies).

Concerns:
- The language card's "residents" means people aged 5 and over (the C16001 universe). Language is not a §7 category, but a reviewer may want "demographics".
- The tragedy tag is still off the Church Rock cards; no deaths found in any source.
- New Mexico Magazine blocks curl (403 Akamai). It was read through WebFetch only, as summaries, so its quotes are as reported by that tool.
- Fetch tally: 37 (including one blocked Census Reporter request and two NM Magazine retries).
