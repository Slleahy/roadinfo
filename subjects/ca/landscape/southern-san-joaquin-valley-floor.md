# Southern San Joaquin Valley floor (landscape unit): research notes

Phase P3, writer session 2026-10-04. 4 cards written (cap 30). Before the §9 check.

## Where it plays
`near` is 35.40056, -119.46944 (the Buttonwillow coordinates, the only cited point near the middle
of the driveable part of the unit), radius 45,000 m. That covers the Bakersfield-to-Interstate-5
run, the freeway north to Lost Hills and the first few miles of Highway 46 west. The San Joaquin
Valley article's own coordinates, 36.62889, -120.185, are ninety miles north of this route and are
useless as a play point.

## Cards
- `tulare-lake` — the closed basin, the five rivers, the biggest freshwater lake west of the
  Mississippi, dry by 1899, back over 114,000 acres in 2023. `elsewhere` at 36.05, -119.78806.
- `sinking` — subsidence since about 1920, 5,200 square miles down more than a foot by 1970, up to
  28 feet in places, two feet a year in 2015 and 2016, and the canals losing capacity.
- `san-joaquin-desert` — the valley floor's dry uplands have a desert of their own; more than five
  million acres farmed; what grows here.
- `endangered-animals` — the kit fox, the leopard lizard and the kangaroo rats, and the single
  recovery plan covering 34 species.

## Fetch tally
16 of 25. Successful: Wikipedia San Joaquin Valley; Wikipedia Tulare Lake (twice); Wikipedia
Central Valley land subsidence; the Endangered Species Recovery Program's copy of the federal
recovery plan executive summary; `cdfa.ca.gov/Statistics`; the U.S. Geological Survey's
land-subsidence page for the San Joaquin Valley; Wikipedia Kern County, California (twice).
Failed or useless: `en.wikipedia.org/wiki/San_Joaquin_Desert` (404 — the article does not exist);
the Kern County crop report PDF (two attempts, connection reset; a third via curl downloaded
16 MB that could not be read, see below); the USDA county profile PDF (image-only);
`ca.water.usgs.gov` (301, followed); `thepacker.com` (403); the University of California carrot
publication (PDF, unreadable).

## The numbers problem on this subject
**No PDF reader is available in this environment.** There is no `pdftotext`, no `poppler`, and no
Python PDF module, and the Read tool's PDF rendering needs `pdftoppm`. Three official tables were
reachable and unusable for exactly that reason:

1. **The Kern County crop report** (`kernag.com/dept/news/2025/2024_Kern_County_Crop_Report.pdf`,
   and the 2023 edition at the matching 2024 path). This is the right source under §6 for what is
   grown here and what it is worth, and it would carry the "number one agricultural county in the
   nation" claim. It is the single biggest gap in this deck.
2. **The 2022 Census of Agriculture county profile** for Kern (`cp06029.pdf`) — an image-only PDF.
3. **The University of California carrot production publication.**

Installing poppler, or adding a PDF-to-text step to the research tooling, would unlock all three
and is worth doing before phase P4.

## What was dropped for want of a second source
- **"Kern County grows about 80 percent of the carrots in the United States."** This is in the
  Wikipedia Kern County article and is repeated widely in the trade press, where it traces to a
  single University of California, Davis estimate rather than a federal statistic. It is a
  superlative, so §5 drops it. It is also the best single fact about this farmland for a listener
  staring at a flat green field, so it is worth going back for: the Kern crop report plus a
  University of California publication would carry it.
- **Air quality.** The valley has some of the worst particulate pollution in the country, 17
  micrograms per cubic metre of PM2.5 on the Wikipedia article. One source, and a comparative claim.
  The Environmental Protection Agency's own design-value tables would make this a strong card.
- **Kern County's agricultural total.** The Wikipedia article's figure is $6.8 billion for 2013,
  too old to say out loud. The California Department of Food and Agriculture's statistics page
  gives only state totals ($64.7 billion in cash receipts for 2025) and the top ten commodities,
  not counties.

## Sources found
- U.S. Geological Survey, land subsidence in the San Joaquin Valley — subsidence beginning around
  1920; by 1970 more than a foot across about half the valley, some 5,200 square miles, and as much
  as 28 feet; renewed subsidence in the droughts of 1976–77, 1986–92, 2007–09 and 2012–15; reduced
  freeboard and flow capacity on the Delta-Mendota Canal, the California Aqueduct and other canals,
  needing expensive repairs.
- Wikipedia Central Valley land subsidence — up to 28 feet since the 1920s (the second source for
  that figure); as fast as two feet a year between May 2015 and September 2016; a 2019 study finding
  up to 20% loss of aqueduct carrying capacity.
- Wikipedia San Joaquin Valley — the southern valley as an endorheic basin centred on Tulare Lake
  fed by the Tule, Kings, Kaweah, White and Kern Rivers; more than 5 million acres farmed as of
  2022; grapes, cotton, almonds, pistachios, citrus and vegetables; the valley beginning to form
  about 66 million years ago; Lake Corcoran about 700,000 years ago.
- Wikipedia Tulare Lake — largest freshwater lake west of the Mississippi, 81 miles long, 690 square
  miles, 6.5 million acre-feet; dry by 1899; the Wowol, Chunut and Tachi Yokuts; over 114,000 acres
  back in 2023; coordinates 36.05, -119.78806.
- Recovery Plan for Upland Species of the San Joaquin Valley (1998) — 34 species covered; five
  endangered animals, the giant, Fresno and Tipton kangaroo rats, the blunt-nosed leopard lizard
  and the San Joaquin kit fox; remaining natural communities generally less than 5 percent of
  historical values and highly fragmented.
- Fish and Wildlife Service, Kern refuge — "the historic valley uplands in the San Joaquin Desert",
  which is where the desert card's first line comes from.
- Wikipedia Kern County — 71% of California's oil production and 78% of its active wells; more than
  three quarters of all onshore California oil. Not used in a card this session; it belongs to the
  Kern county deck, which already exists.

## Leads not followed
- **The geology card.** The valley began to form about 66 million years ago, and Lake Corcoran
  filled it about 700,000 years ago. One source, nothing surprising, an easy fifth card.
- **Buena Vista Lake and Kern Lake**, the southern valley's other drained lakes, on the route and
  with no card anywhere in the deck.
- **The Yokuts of the lake country** — the Wowol, Chunut and Tachi. §8 applies. Their own published
  sources should come first, and the Tachi Yokut Tribe has a website.
- The Lake Corcoran clay, the layer that makes the subsidence possible, would tie the geology card
  and the sinking card together.

## Checker, 2026-10-05
`san-joaquin-desert` dropped: its farmland figure (more than five million acres, 2022) came from
Wikipedia prose, not the Census of Agriculture table (§6), and the one sentence left could not stand
alone. Worth rebuilding once the crop report or the agriculture census profile can be read.
