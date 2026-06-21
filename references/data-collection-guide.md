# Data collection guide: what to upload, where to get it, how

This file tells you what to give the analyzer, where each file lives in Amazon, and exactly how to pull it. Read it before you upload anything. It is written for people who have never exported an Amazon ad report. Start with the tier list, grab what you can, and upload more later to sharpen the report. The more you provide, the higher the confidence score on your health report.

A few facts that shape everything below:
- Console reports export as XLSX or CSV with plain-English column names like "Customer Search Term", "Spend", and "Total Advertising Cost of Sales (ACoS)".
- Attribution window gotcha: Sponsored Products seller reports use a 7-day window; vendor reports plus all Sponsored Brands and Sponsored Display reports use a 14-day window. The analyzer needs to know which one it is reading, so always include the column headers and date range.

## (A) What to upload: minimum, better, best

| Tier | Upload this | What you get back |
|---|---|---|
| **Minimum** | One Sponsored Products **Search Term** report (last 30 days) | Wasted-spend and negative-keyword findings, top converting terms to promote. A basic report. |
| **Better** | Search Term + **Targeting** + **Campaign** + **Advertised Product** reports (all SP, 30 days), or the **Bulk Operations** file | Bid guidance per target, per-ASIN profit read, account scorecard, structural issues. A solid report. |
| **Best** | The "Better" set, plus **Sponsored Brands** and **Sponsored Display** reports, **Business Reports** (Detail Page Sales and Traffic by Child Item), **Search Query Performance** if brand-registered, and the bonus inputs in section (E): COGS/price sheet, keyword-tool exports, inventory status | Full ad-vs-listing diagnosis, exact break-even ACOS, share-of-voice and keyword-gap analysis. Highest confidence. |

You do not need all of it. Upload what you have. The report states its own confidence level and tells you which missing file would raise it most.

## (B) Amazon Ads console reports

### Where the reports live

Log in at advertising.amazon.com. In the left sidebar, the path is **Measurement and Reporting > Sponsored ads reports**. That is the newer label. The older label is **Reports > Advertising reports**, and sellers can also reach the same builder from **Seller Central > Reports > Advertising Reports**. All three land in the same place. The button you click to start is "Create report" (sometimes still shown as "New report").

### The universal "how to generate any report" flow

1. Log in to the Amazon Ads console (advertising.amazon.com).
2. Left sidebar: **Measurement and Reporting > Sponsored ads reports**.
3. Pick **Report category** (the ad product): Sponsored Products, Sponsored Brands, Sponsored Display, or Amazon Attribution.
4. Pick **Report type** from the dropdown (Search term, Targeting, and so on).
5. Configure **Country**, **Time unit** ("Summary" gives one total row per item; "Daily" gives one row per day), and **Report period** (the date range).
6. Name the report, then click **Create report**. It processes in the background, usually a few minutes.
7. When the status shows "Completed", click **Download** to get the XLSX or CSV.

### Report inventory

**Sponsored Products (13 report types)**

| Report | Key contents | Console retention | Priority |
|---|---|---|---|
| Search term | Customer search term, keyword, match type, impressions, clicks, CPC, CTR, spend, 7-Day Orders/Sales, ACoS, ROAS. A `*` in the search-term column means a product-page placement with no typed query. | about 65 days | Essential |
| Targeting | One row per keyword or product target: target text, match type, impressions, clicks, spend, CPC, CTR, 7-Day Orders/Sales, conversion rate, ACoS, ROAS. | about 65 to 95 days | Essential |
| Advertised product | Per ASIN/SKU you advertise: impressions, clicks, spend, sales/orders/units by 1/7/14/30-day, Same-SKU vs Other-SKU sales, ACoS, ROAS. | 95 days | Essential |
| Campaign | Campaign name, status, budget, bidding strategy, impressions, clicks, spend, orders/sales/units. | 95 days | Important |
| Placement | Split by Top of Search, Product Pages, Rest of Search. | 95 days | Important |
| Purchased product | Advertised ASIN vs the ASIN actually bought, Same-SKU vs Other-SKU (halo). Sellers only. | 95 days | Important |
| Budget | Budget use plus time-in-budget (% of day in budget). Console only, not in the API. | console only | Situational |
| Search Term Impression Share (SIS) | The Search term report plus two columns: Search Term Impression Share (% of that term's impressions you won) and Search Term Impression Rank (1 = top share). Console only. | console only | Situational |
| Audience | Performance by audience segment. | n/a | Situational |
| Performance Over Time | Daily or weekly account totals. Console only. | console only | Situational |
| Gross and Invalid Traffic | Gross vs invalid impressions and clicks, invalid click-through rate. | 365 days | Situational |
| Prompts (new 2025-26) | Performance when products appear in Rufus AI shopping prompts (Prompt Ad Extension). New and account-dependent. | n/a | Growing |
| Video | SP video-ad performance. | n/a | Situational |

**Sponsored Brands (9 report types)**

Keyword, Search term, Campaign, Keyword Placement, Campaign Placement, Search Term Impression Share, Category Benchmark (your metrics vs category percentiles), Attributed Purchases (new-to-brand vs repeat), Gross and Invalid Traffic.
- SB uses "Keyword" where SP uses "Targeting".
- The SB Purchased Product report uniquely carries new-to-brand sales and purchases (14-day) plus product name and category, and can pull up to 731 days of history.

**Sponsored Display (7 report types)**

Campaign, Targeting, Advertised product, Purchased product, Matched target, Gross and Invalid Traffic, Pricing transparency.
- VCPM caution: the SD Campaign report mixes click-based and view-through metrics. Read click-based orders separately, since view-through attribution inflates results.

### Click-by-click: the 4 reports that matter most

**1) Search Term report (Sponsored Products): the #1 report**
1. Go to advertising.amazon.com and sign in.
2. Left menu: **Measurement and Reporting > Sponsored ads reports**.
3. **Report category**: Sponsored Products.
4. **Report type**: Search term.
5. **Time unit**: Summary. **Report period**: last 30 days (you can go up to about 60).
6. Name it (for example "SP Search Term 30d"), then click **Create report**.
7. Wait for "Completed" in the list, then click **Download** (CSV or XLSX).
8. What to look at: Customer Search Term, Clicks, 7 Day Total Orders, Spend, ACoS. Terms with many clicks and 0 orders are negation candidates; terms with 3 or more orders at low ACoS are promotion candidates.

**2) Targeting report (Sponsored Products)**
1. Steps 1 and 2 as above.
2. **Report category**: Sponsored Products.
3. **Report type**: Targeting.
4. **Time unit**: Summary. **Report period**: 30 days. Click **Create report**.
5. Download. Use it to raise bids on targets below your ACoS goal and lower bids on targets well above it.

**3) Advertised Product report (Sponsored Products)**
1. Steps 1 and 2 as above.
2. **Report category**: Sponsored Products.
3. **Report type**: Advertised product.
4. Summary, 30 days, then **Create report** and **Download**.
5. Each row is one of your ASINs/SKUs. Find ASINs that lose money (high spend, low 7 Day Total Sales) and your winners.

**4) Campaign report (Sponsored Products): the account scorecard**
1. Steps 1 and 2 as above.
2. **Report category**: Sponsored Products.
3. **Report type**: Campaign.
4. Summary, 30 days, then **Create report** and **Download**.
5. Top-line health per campaign: Spend, Sales, ACoS, plus budget and bidding-strategy columns that flag budget-capped campaigns.

To get the same reports for Sponsored Brands or Sponsored Display, change the **Report category** in step 3 (for example SB > Keyword or Search term; SD > Campaign or Targeting).

## (C) The Bulk Operations file (Bulksheets)

This is not a performance report. It is an Excel (.xlsx) workbook for creating and editing campaigns, ad groups, keywords, product ads, negatives, bids, and budgets in bulk. For the analyzer it is the single richest export, because one download contains every campaign, ad group, keyword, and bid, plus optional search-term and zero-impression data.

**Where to find it**
- Vendors: console left menu, **Sponsored ads > Bulk operations**.
- Sellers: Seller Central, **All campaigns > Bulk operations**.

**Custom download options (max 60 days of data):** include terminated campaigns, items with zero impressions (good for finding keywords to negate), placement data, brand assets (SB only), Sponsored Products input guidance, and Sponsored Products search-term data.

**Structure:** the first three columns are always Product (for example Sponsored Products), Entity (Campaign, Ad group, Keyword), and Operation (Create, Update, Archive). Rows follow a parent-to-child order: Campaign, then Ad group, then Ad (ASIN/SKU), then Keyword.

**Cautions**
- Download a fresh file right before you edit. Stale IDs cause errors.
- If you plan to open it in Excel, save as CSV so Excel does not turn ASINs and SKUs into scientific notation (for example "1.23E+09").
- Never delete the auto-generated ID columns when updating.

## (D) Seller and Vendor Central data

Ad reports tell you what your ads did. They cannot tell you why money was wasted. Pairing ad reports with Seller Central data lets the analyzer split a problem into an **ad problem** (bids, targeting, budgets, placement) versus a **listing or conversion problem** (image, price, reviews, content, Buy Box).

### The one rule that decides what you can access: Brand Registry

- **Brand Analytics** reports (Search Query Performance, Search Catalog Performance, Amazon Search Terms, Market Basket, Customer Loyalty, Demographics) require a **Brand Representative** role on a brand enrolled in **Amazon Brand Registry**. You must be internal to the brand and responsible for selling it.
- **Business Reports** require no Brand Registry. Every seller has them. This is your universal fallback.
- If you are brand-registered but still cannot see Brand Analytics, the cause is usually a permissions toggle, not eligibility. The Primary Account Administrator must grant "Amazon Brand Analytics" in **Settings > User Permissions > Global User Permissions**.
- Not brand-registered? You lose Brand Analytics. Diagnose conversion using Business Reports plus your own ad-console reports. To gain access later, enroll the brand in Brand Registry, then enable benefits at Brand Registry > Manage selling benefits (brandregistry.amazon.com/brg/selling-benefits).

Vendor Central note: vendors (1P) do not use Seller Central Business Reports. The equivalent is Amazon Retail Analytics / Vendor Central Analytics (Sales, Traffic, Search Terms). Brand Analytics SQP is available to brand-registered vendors too. The menu paths below are the Seller Central (3P) paths.

### Quick reference table

| Data source | Where (2026 path) | Brand Registry? | Export | What it proves |
|---|---|---|---|---|
| Search Query Performance (SQP) | Brands > Brand Analytics > Search Query Performance | Yes | Generate Download, CSV (Simple) | Full search funnel plus your share of impressions/clicks/cart-adds/purchases per query. The #1 ad-vs-listing tool. |
| Search Catalog Performance | Brands > Brand Analytics > Search Catalog Performance | Yes | Generate Download, CSV | Same funnel as SQP but per product across all searches: which ASINs leak, and where. |
| Amazon Search Terms report (formerly "Top Search Terms") | Brands > Brand Analytics > Amazon Search Terms | Yes | Generate Download, CSV | Highest-volume queries and which ASINs win them: keyword opportunity and competitive gaps. |
| Market Basket Analysis | Brands > Brand Analytics > Market Basket Analysis | Yes | Generate Download, CSV | Products bought with yours: bundle ideas and Sponsored Display / product-targeting seed ASINs. |
| Repeat Purchase Behavior / Customer Loyalty Analytics | Brands > Brand Analytics > Repeat Purchase Behavior (also in Customer Loyalty Analytics) | Yes | Generate Download, CSV | Repeat rate. High repeat rate justifies a higher allowable ACOS (lifetime value). |
| Demographics | Brands > Brand Analytics > Demographics | Yes | Generate Download, CSV | Age, income, gender, and so on: sanity-checks DSP / Sponsored Display targeting. |
| Business Reports: Detail Page Sales and Traffic by Child Item | Menu > Reports > Business Reports > By ASIN | No | Download, CSV | Sessions, Page Views, Unit Session % (conversion rate), Featured Offer (Buy Box) %. Core conversion and Buy Box diagnosis. |

Caution: the **Item Comparison and Alternate Purchase Behavior** dashboard was removed by Amazon on June 30, 2022. It is not live. The closest replacements are Market Basket Analysis (bought-together) and the SQP Query Detail view (top 10 competing ASINs for a query). Older blog posts that still list it are out of date.

### Search Query Performance (SQP): the big one

Each row is one search query, with marketplace totals and your brand's share at every stage: Search Query Volume, then Impressions, then Clicks, then Cart Adds, then Purchases. Each stage reports a count, a brand count, and a brand share %. It includes organic and Sponsored Products traffic from the search results page (it excludes widget traffic like "Top Rated" and "New Arrivals").

Views: **Brand view** (one row per query across your catalog, max 1,000 queries), **ASIN view** (one row per query for a single product, best for ad-level diagnosis), and **Query Detail view** (the top 10 competing ASINs vs yours for a chosen query).

How to export:
1. Seller Central > **Brands** tab > **Brand Analytics**.
2. Open **Search Query Performance**.
3. Choose Brand or ASIN view and a reporting range (Weekly, Monthly, or Quarterly).
4. Click **Generate Download**, choose **Simple** (CSV), and download.
5. Data is generally available within about 72 hours of a period closing.

The ad-vs-listing diagnostic logic:

| Pattern in SQP | Reading | Action type |
|---|---|---|
| Low impression share on a high-volume query | You barely show up | Ad problem or opportunity: bid up, add the keyword |
| High impression share, low click share | Seen but not clicked | Listing: main image, title, price, rating, badge |
| High click share, low cart-add or purchase share | Clicks do not convert | Listing/conversion: detail page, price, reviews, content |
| You win purchase share at low click share | Efficient converter | Scale ad spend on this query |

Critical caveat: Amazon states that SQP metrics do not match advertising-console metrics and should not be reconciled against them. SQP is search-stage, marketplace-level share, attributed differently than ad clicks and sales. Use it directionally, not to tie out spend.

### Search Catalog Performance: the ASIN-level twin of SQP

Same funnel (impressions, clicks, cart adds, purchases), but organized by product across all searches, plus Amazon's Choice badge impact (monthly range only). Use SQP to find the bad keyword; use Search Catalog Performance to find the bad ASIN. An ASIN that converts poorly across the board points to listing, price, or reviews, not a single bad bid. Path: Brands > Brand Analytics > Search Catalog Performance, set range, Generate Download, CSV.

### Other Brand Analytics dashboards (supporting context)

- **Amazon Search Terms report** (the renamed "Top Search Terms"): top queries by volume plus the top-3 clicked ASINs and their click/conversion share. Keyword discovery and competitive benchmarking.
- **Market Basket Analysis**: products most often bought with yours, which seed Sponsored Display and product-targeting ideas.
- **Repeat Purchase Behavior / Customer Loyalty Analytics**: orders vs unique customers and repeat rate. A high repeat rate means higher lifetime value, so you can justify a higher allowable ACOS and lean into retargeting and Subscribe & Save.
- **Demographics**: age, income, gender, and so on, which sanity-check DSP and Sponsored Display audience choices.

All export the same way: Brands > Brand Analytics > [dashboard] > Generate Download > CSV.

### Business Reports: Detail Page Sales and Traffic (works for every seller)

Path: Seller Central > **Menu > Reports > Business Reports** > left rail > By ASIN > **Detail Page Sales and Traffic by Child Item** (also "by Parent Item"). Set the date range, then **Download** (CSV). The by-Child-Item version is the most useful for ads, because ads run at the child-ASIN level.

Key fields:

| Field | Definition | Why it matters for ads |
|---|---|---|
| Sessions | Unique visits to the product page in a 24-hour window (any seller in the Buy Box) | Denominator for conversion |
| Page Views | Total views (a session can have several) | Traffic depth |
| Unit Session Percentage | Units ordered ÷ Sessions = the ASIN conversion rate | The listing-vs-ad number. Low % = the listing is not converting traffic, so fixing bids will not help |
| Featured Offer (Buy Box) Percentage | % of page views where your offer held the Buy Box | If under about 95 to 100%, ads may send traffic to a page where you do not even win the sale: a Buy Box / pricing problem, not an ad problem. A drop here precedes a drop in sales |
| Ordered Product Sales / Units Ordered / Total Order Items | Sales and units per ASIN/SKU | The revenue side of TACOS |
| B2B variants (UnitSessionPercentageB2B, BuyBoxPercentageB2B) | Same metrics for Amazon Business buyers | Measure the B2B channel separately |
| Mobile App vs Browser sessions/page views | Traffic source split | Mobile-heavy traffic means optimize the mobile listing and main image |

Diagnostic flow: if ads drive clicks but ACOS is bad, check Unit Session % (low = listing/conversion problem) and Buy Box % (low = pricing/Buy Box problem) before touching bids. Only when both are healthy is the issue genuinely in the ad account (targeting, bids, search-term harvesting, negatives).

## (E) Bonus inputs that raise report confidence (third-party tools and your own numbers)

None of these come from Amazon, and none are required. Each one removes a guess from the analysis and lifts the confidence score. Upload as CSV/XLSX exports or clear screenshots.

| Bonus input | Where it comes from | What it unlocks | Confidence lift |
|---|---|---|---|
| **Reverse-ASIN keyword export** | Helium 10 Cerebro, Jungle Scout Keyword Scout, Data Dive | Search volume, competition, and your organic + sponsored rank per keyword. Separates "low volume" terms from "we rank poorly" terms and finds keywords you should be bidding on but are not. | High |
| **Keyword research export** | Helium 10 Magnet, Jungle Scout Keyword Scout | A broader keyword universe with search volume and competition for gap analysis against your Search Term report. | Medium to high |
| **Sales analytics export** | Jungle Scout Sales Analytics, Helium 10 | Confirms revenue, units, and profit trends to validate TACOS and reconcile ad sales against total sales. | Medium |
| **Product cost / COGS and sell-price sheet** | Your own spreadsheet | The exact break-even ACOS per product (break-even ACOS = gross margin before ad spend, as a % of sale price). Without it the analyzer must guess a target ACOS; with it, every "too high / too low ACOS" call becomes exact. | Very high |
| **Competitor / listing screenshot** | Amazon search results and detail pages | Visual context for click-share and conversion findings: main image, price, badge, review count vs competitors. Turns "low click share" into a concrete fix. | Medium |
| **Inventory status** | Seller Central inventory, or a screenshot | Flags items low or out of stock so the analyzer does not tell you to scale spend on something about to run dry, and explains sudden impression or sales drops. | Medium |

How this ties to the confidence score: the health report grades itself on input coverage. Ad reports alone give a directional report. Adding the COGS/price sheet makes the ACOS math exact rather than assumed, which is the single biggest jump. Adding keyword-tool exports and Business Reports / SQP lets the analyzer prove ad-vs-listing causes instead of inferring them. Each extra file converts an assumption into a fact, and the report tells the user which one to add next.

## (F) If you can only screenshot Campaign Manager

The Campaign Manager dashboard (advertising.amazon.com/campaign-manager/all-campaigns) shows a thin, customizable metric set: Impressions, Clicks, CTR, Spend, CPC, Orders, Sales, ACoS, ROAS, plus viewable impressions for SD vCPM. Seller SP rows use 7-day attribution; vendor/SB/SD use 14-day. A screenshot omits per-keyword and per-search-term detail, so prefer a downloaded report whenever you can. If a screenshot is all you have:

1. Set the **date range** (top-right) first, and make sure it is visible in the screenshot.
2. Use the **column customizer** to add Orders, Sales, ACoS, and ROAS if they are missing.
3. Capture the **full table including the headers**, so the analyzer can tell which attribution window the numbers use.
4. If you can, download a Campaign report instead. It carries far more detail than a screenshot.

## (G) A note on AMC and Amazon Marketing Stream

Two advanced systems exist, and you will probably not have either as a non-expert. Know they exist; both are usually out of scope here.

- **Amazon Marketing Cloud (AMC)**: a privacy-safe cloud "clean room" where advertisers run SQL over event-level Amazon Ads signals to answer cross-channel questions (path-to-purchase, new-to-brand, ad-assist, audience overlap). Since October 15, 2024, Amazon DSP is no longer a hard prerequisite, so DSP advertisers and Amazon Ads Partner Network partners (including those serving sponsored-ads-only clients) can register. In practice access runs through an agency, so most single sellers will not have it.
- **Amazon Marketing Stream**: a push-based system that delivers hourly Amazon Ads campaign metrics and change events in near real-time to your own AWS destination (Amazon SQS) via the Ads API. It powers dayparting and intraday bid automation. It is an API/AWS developer feature, not a Seller Central export, so it is tool and agency territory.

## A note on attribution windows and date ranges

When the analyzer reads your files, it must know which attribution window each column uses, because SP seller exports use 7-day windows while SB, SD, and vendor exports use 14-day windows. Always keep the original column headers and include the report's date range. Console custom date ranges can exceed API limits, so old data is sometimes reachable only through the console, and console vs API totals can differ by up to about 5% due to traffic-validation and refresh timing.

## Sources

- Report types (Sponsored ads, version 3), Amazon Ads API docs: https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/report-types/overview
- Search term reports, Amazon Ads API docs: https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/report-types/search-term
- Advertised product reports, Amazon Ads API docs: https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/report-types/advertised-product
- Purchased product reports, Amazon Ads API docs: https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/report-types/purchased-product
- Campaign reports, Amazon Ads API docs: https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/report-types/campaign
- Gross and invalid traffic reports, Amazon Ads API docs: https://advertising.amazon.com/API/docs/en-us/guides/reporting/v3/report-types/gross-and-invalid-traffic
- Advertising console vs. API reports, Amazon Ads: https://advertising.amazon.com/API/docs/en-us/guides/reporting/v2/advertising-console
- Get started with bulksheets: Part 1, Amazon Ads: https://advertising.amazon.com/API/docs/en-us/bulksheets/2-0/get-started-with-bulksheets-part1
- Reports, Amazon Ads Support Center: https://advertising.amazon.com/help/GBYSPTSLR337JMLH
- Search Term Impression Share (SIS) report for Sponsored Products, Amazon Ads: https://advertising.amazon.com/help/G7AQQUSFVZPAAXEU
- Amazon Ads Reports: The Complete 2026 Guide, PPC Ninja: https://www.ppcninja.com/blog/performance-over-time-report.html
- Amazon PPC Bulk Operations, PPC Ninja: https://www.ppcninja.com/blog/amazon-ppc-bulk.html
- Master Amazon Advertising Reports: 2025 Complete Guide, My Amazon Guy: https://myamazonguy.com/advertising/amazon-advertising-reports/
- Search Term Impression Share & Brand Category Benchmark Reports, Ad Badger: https://www.adbadger.com/blog/amazon-ppc-education/amazons-new-sponsored-brands-reports-what-they-are-and-how-to-use-them/
- How long does Amazon keep your ad reports?, Intentwise: https://www.intentwise.com/blog/amazon-advertising/explained-how-long-does-amazon-keep-your-ad-reports/
- Search Query Performance dashboard, Amazon Seller Central Help: https://sellercentral.amazon.com/help/hub/reference/external/G8J4CB5ZBF3NX7TP?locale=en-US
- Brand Analytics (hub), Amazon Seller Central Help: https://sellercentral.amazon.com/help/hub/reference/external/GH2Z5B4HMF5ZXCG2?locale=en-US
- Download your Brand Analytics Search dashboard data, Amazon Seller Central Forums: https://sellercentral.amazon.com/seller-forums/discussions/t/844c405b6bf3514f57452580f5db49f2
- Changes to Amazon Brand Analytics dashboards (Item Comparison & Alternate Purchase Behavior discontinued), Amazon Seller Central Forums: https://sellercentral.amazon.com/seller-forums/discussions/t/6c238a7b112fd510e9be4a49d9bc3bc1
- New Brand Analytics search dashboards are now available (Search Catalog Performance), Amazon Seller Central Forums: https://sellercentral.amazon.com/seller-forums/discussions/t/1afe683eb0acb90bb31abdc34950ef74
- Amazon Brand Analytics: Get data to grow your business, Amazon (sell.amazon.com): https://sell.amazon.com/blog/brand-analytics
- Business Reports FAQ, Amazon Seller Central Help: https://sellercentral.amazon.ca/gp/help/external/28761
- Amazon Seller Central Business Report Fields, Gorilla ROI: https://www.gorillaroi.com/amazon-seller-central-reports/business-report
- Analytics Reports (SP-API report type values), Amazon SP-API Developer Docs: https://developer-docs.amazon.com/sp-api/docs/report-type-values-analytics
- Amazon Marketing Cloud: Discover advertising insights, Amazon Ads: https://advertising.amazon.com/solutions/products/amazon-marketing-cloud
- AMC eligibility expanded to sponsored ads advertisers (through partners), Amazon Ads: https://advertising.amazon.com/resources/whats-new/expanding-amc-eligibility-to-advertisers-and-partners
- Amazon Marketing Stream: Measure campaign performance in real time, Amazon Ads: https://advertising.amazon.com/solutions/products/amazon-marketing-stream
- A complete guide to Amazon Marketing Stream, Amazon Ads: https://advertising.amazon.com/library/guides/amazon-marketing-stream
