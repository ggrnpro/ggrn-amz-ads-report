# Amazon Ads metrics glossary and interpretation

This file defines every metric an analyst reads off Amazon ad reports: the formula, the healthy and warning bands, and how to read it in context. Read it when you need to turn raw ad-report numbers into a verdict, when a number looks off and you need to know what drives it, or when a seller asks "is this good?" and you need the right answer instead of a guess. The numbers, formulas, report names, and menu paths here are current as of 2026.

Lead rule: do the profit math first. Almost no metric is "good" or "bad" on its own. Most are judged against the seller's profit margin (break-even ACOS) and the category benchmark. Before you judge any ACOS or ROAS, get the seller's margin. Everything keys off it.

## 1. The profit math you must establish first

- Pre-ad profit per unit = Selling Price minus COGS minus Amazon referral and FBA/FFN fees minus all other per-unit costs (everything except ad spend).
- Break-even ACOS = pre-ad profit margin % = (pre-ad profit per unit ÷ Selling Price) × 100.
  - Worked example (Ad Badger): $20 price minus $3 Amazon fees minus $6 COGS = $11 profit, so break-even ACOS = $11 ÷ $20 = 55%. At 55% ACOS you make $0. Below 55% you profit. Above 55% you lose money.
- Target ACOS = break-even ACOS minus the profit margin you want to keep. Example (Perpetua): 25% pre-ad margin minus 10% desired post-ad profit = 15% target ACOS.
- Precise note on a common confusion: "target ACOS = contribution margin" describes the break-even ceiling. That is, break-even ACOS equals your contribution margin %, and spending right up to it leaves zero profit. To actually keep profit, set target ACOS below contribution margin. It is NOT `target ACOS = (1 minus margin)`. That expression equals the cost ratio and is wrong for ad-spend tolerance. Always use: break-even ACOS = margin %; target ACOS = margin % minus desired profit %.
- Max profitable CPC = CVR × Selling Price × Target ACOS. Use this to tell a seller how high they can safely bid.

Plain-language version for a non-expert seller: "You can spend up to [your margin %] of a sale on ads before you lose money. Aim a few points under that to stay profitable."

## 2. ACOS, ROAS, and TACOS

Amazon's official definitions:

- ACOS = (Ad Spend ÷ Ad Revenue) × 100. Efficiency of ad spend against ad-attributed sales only. Amazon: "There isn't a definitive number for a good Amazon ACOS." It depends on margin, goals, and category. Read it relative to break-even ACOS, never as an absolute. Low ACOS can mean under-investing (leaving rank and sales on the table). High ACOS means either inefficiency or a deliberate launch or defense play. Always ask "vs what target?"
- ROAS = Ad Revenue ÷ Ad Spend. Amazon states ROAS "is the inverse of ACOS." Therefore ACOS = 1 ÷ ROAS and ROAS = 1 ÷ ACOS. (ACOS 25% = ROAS 4.0; ACOS 50% = ROAS 2.0; ACOS 20% = ROAS 5.0.) They are the same data shown two ways. Use ACOS to compare against margin, ROAS to compare against other channels.
- TACOS = (Ad Spend ÷ Total Sales) × 100, where total sales = ad-attributed plus organic. Not in ad reports natively. Combine ad spend (ad console) with total sales (Seller Central Business Reports). TACOS trend is the single best brand-health signal: falling TACOS at steady or rising total sales means ads are seeding organic rank (the flywheel is working). Rising TACOS at flat total sales means growing ad-dependence and weakening organic (warning). Rising TACOS is acceptable during launches or expansion. Mature brands often run roughly 8 to 15%, but there is no universal benchmark; it varies by category, price, and stage.

## 3. Master metrics table

| Metric | Formula | Healthy (2026 defaults) | Warning | What it tells you |
|---|---|---|---|---|
| ACOS | (Ad Spend ÷ Ad Sales) × 100 | Below break-even ACOS (acct avg ~30%) | At or above break-even margin | Ad efficiency vs margin. High = inefficient or deliberate launch/defense; low = efficient but possibly under-investing. |
| ROAS | Ad Sales ÷ Ad Spend | At or above 1 ÷ break-even ACOS (acct avg ~2.5 to 5x) | Below break-even multiple | Same as ACOS, inverted. Dollars returned per $1 spent. |
| TACOS | (Ad Spend ÷ Total Sales) × 100 | Stable or falling; mature brands often ~8 to 15% | Rising with flat total sales | Ad-dependence and organic health (the flywheel). Trend matters more than level. |
| Break-even ACOS | Pre-ad profit ÷ Price × 100 | = your margin % | n/a (it is the ceiling) | The max ACOS before you lose money. Collect this first. |
| Target ACOS | Break-even ACOS minus desired profit % | Set below break-even | Set at or above break-even | The ACOS you bid toward to hit a profit goal. |
| Spend / Cost | Sum of click costs | Within budget and at or under target | Pacing over budget with poor ROAS | Raw input dollars. |
| Ad Sales | Sum of attributed order revenue (7-day SP/SB window) | Growing | Falling at flat spend | Ad-attributed revenue only, a subset of total sales. |
| Orders | Attributed orders | n/a | n/a | Count of ad-driven orders. |
| Units | Units in attributed orders | Units at or above Orders | n/a | Multi-unit baskets lift AOV. |
| Impressions | Times ad displayed | Enough to gather clicks | Very low = bid/budget/relevance issue | Top-of-funnel volume; everything else depends on it. |
| Clicks | Ad engagements | n/a | n/a | Traffic delivered to the listing. |
| CTR | Clicks ÷ Impressions | SP ~0.4 to 0.6%; acct avg ~0.58% | Well below category | Creative, relevance, and placement appeal. High CTR with low CVR = listing problem. |
| CPC | Spend ÷ Clicks | At or under max-profitable-CPC; acct avg ~$1.22 | Rising at flat CVR | Auction competition cost. Judge vs CVR × price × target ACOS. |
| CPM | (Spend ÷ Impressions) × 1,000 | Category-dependent | High CPM, weak reach or NTB | Reach cost (SD vCPM, Sponsored TV, DSP). |
| CVR (conversion rate) | Orders ÷ Clicks | 10 to 15% optimized; acct avg ~11% | Below category with healthy CTR | Listing, price, and review health. The lever that links CPC to ACOS. |
| CPA | Spend ÷ Orders (= CPC ÷ CVR) | Below pre-ad profit per order | Rising | Absolute dollars to buy one order. |
| NTB Orders / Purchases | First orders from new buyers (12-mo lookback) | High for SB/SD/STV growth goals | Near 0 (cannibalizing) | Customer acquisition. SB/SD/STV only, NOT Sponsored Products. |
| % Orders NTB | NTB orders ÷ total orders | High (often 50 to 80%+ for SB) | Low | Share of orders that are genuinely new customers. |
| NTB Sales / % Sales NTB | NTB sales ÷ total sales | High for awareness goals | Low | Revenue from new customers. |
| NTB ROAS (derived) | NTB Sales ÷ Spend | At or above target for acquisition | Low | Efficiency of new-customer acquisition. |
| Purchase rate over clicks (NTB) | NTB orders ÷ clicks | n/a | n/a | New-customer conversion efficiency. |
| Detail Page Views (DPV) | Attributed page views | DPV at or above orders (normal) | High DPV, low orders | Consideration. Gap to orders = listing/price issue. |
| DPV Rate (NTB) | NTB DPVs-from-views ÷ Impressions | n/a | n/a | Consideration lift per impression (awareness KPI). |
| Cost per DPV (NTB) | Cost ÷ NTB DPVs-from-views | n/a | Rising | Cost to drive new-customer consideration. |
| Viewable Impressions | Impr. with at least 50% on-screen for 2+ sec | High share of impressions | Low | Whether video/display ads were actually seen. |
| VTR (view-through rate) | Completed views ÷ measured impressions | Higher | Low | Video completion strength. |
| vCTR | Clicks ÷ Viewable Impressions | At or above CTR | Low | Click rate among ads actually seen. |
| 5-second views / rate | Impr. watched 5+ sec (÷ impr. for rate) | Higher rate | Low | Hook strength of the video opening. |
| VCR (video completion rate) | Video Completes ÷ Video Starts | Higher | Low | Message retention; low = weak creative. |
| Quartiles (25/50/75%) | Impr. reaching each quartile | Gentle drop-off | Steep early drop | Where viewers abandon the video. |
| Branded Searches | Branded-keyword searches attributed to ad | Rising | Flat | Awareness lift (especially Sponsored TV). |
| Search Term Impression Share | Your SP impr. ÷ all SP impr. for that term | High on converting terms | Low on money keywords | Paid share-of-voice. Low = outbid; raise bid/budget if profitable. |
| Search Term Impression Rank | Your rank in SP impr. for that term (1 = most) | Low number (1 to 3) on key terms | High number | Where you stand vs competitors for a term. |
| Top-of-Search IS | Impr. won in top-of-search slot ÷ available | High on best terms | Low | Hold on the premium, highest-CVR placement. |
| SQP Impression/Click/Cart/Purchase Share | Your catalog ÷ market total at each funnel stage | Share held or rising down funnel | Share leaks at a stage | (Brand Analytics, organic plus paid) where you lose the funnel battle. |

Notes on the raw inputs: Ad Sales in ad reports is ad-attributed only, a subset of total sales. Never confuse it with Business-Report total sales. Units above Orders signals multi-unit baskets (good for AOV). Low impressions point to a bid, budget, or relevance problem upstream of everything else.

## 4. How the metrics relate (cheat sheet)

- ACOS is approximately CPC ÷ (CVR × Price). So ACOS rises if CPC goes up, CVR goes down, or price goes down. To cut ACOS: lower CPC (bids and negatives), or raise CVR (listing, price, reviews). Doubling CVR roughly halves ACOS at constant CPC.
- CTR is an ads problem; CVR is a listing problem. High CTR with low CVR means fix the listing, not the bids. Low CTR means fix keywords, creative, or placement.
- ACOS = 1 ÷ ROAS exactly. Never report them as if they disagree.
- ACOS judges profit; TACOS judges brand health; NTB judges growth. Awareness, SB, SD, and Sponsored TV campaigns should be judged on NTB %, DPV, branded searches, and VCR, not on click-ROAS alone.
- NTB is unavailable for Sponsored Products (SB, SD, and Sponsored TV only). A 12-month lookback defines "new."
- SQP and ad-console numbers will not match. SQP (Brand Analytics) includes organic; ad reports are ad-attributed only.
- Max profitable CPC = CVR × Price × Target ACOS. If your CPC is below this on a converting term, you can profitably bid up for rank. If above, trim bids or raise CVR.

## 5. New-to-Brand metrics in detail

NTB metrics measure purchases, sales, and detail page views from first-time customers of your brand. A customer is NTB if they have not purchased from your brand within the 12-month lookback window. The full set: Purchases (NTB orders); % of purchases NTB; Sales (NTB); % of sales NTB; Units sold (NTB); % of units NTB; Purchase rate over clicks (NTB orders ÷ clicks); DPV (NTB), DPV from views/clicks (NTB), DPV rate (NTB) = NTB DPVs-from-views ÷ impressions; Cost per DPV (NTB). NTB ROAS (NTB sales ÷ spend) is derived, not a named Amazon line item.

NTB is available only for Sponsored Brands, Sponsored Display, and Sponsored TV. New-to-brand data is not available for Sponsored Products.

How to read it: high % of orders NTB (for example above 50 to 80% for SB) means ads are bringing genuinely new customers, which is good for growth and awareness goals. Low NTB % means you are paying to convert people who would likely buy anyway. NTB is the main justification for accepting a higher ACOS on brand and awareness campaigns.

## 6. Video and awareness metrics in detail

These judge upper-funnel video creative quality, not sales.

- Viewable impression: at least 50% of the ad on-screen for 2 continuous seconds while playing.
- VTR (view-through rate) = completed views ÷ measured impressions.
- vCTR = clicks ÷ viewable impressions.
- 5-second views = impressions watched at least 5 seconds; 5-second view rate = % of impressions watched at least 5 seconds. This measures hook strength.
- Video first quartile / midpoint / third quartile = impressions reaching 25% / 50% / 75%.
- Video Start; Video Complete = played to the end. VCR (video completion rate) = video completes ÷ video starts. This measures message retention.
- Unmutes = impressions where the shopper unmuted.

Reading guide: rising 5-second view rate and VCR means the creative holds attention. Low VCR with decent impressions means the opening seconds fail. For SB Video, judge alongside NTB and CTR. For Sponsored TV, judge on reach, VCR, branded searches, and NTB, with no click-ROAS expectation.

Detail Page Views (DPV) is a consideration metric between click and purchase. DPVs above orders is normal. A high DPV count with low orders means shoppers reach the listing but do not buy (a listing, price, or review issue). DPV and branded searches are the right KPIs for awareness campaigns whose payoff is downstream.

## 7. Share-of-voice and Brand Analytics metrics

- Search Term Impression Share (Sponsored Products): account-wide impression share for each search term vs other advertisers. Example: 20% impression share for a term means you won 20% of all SP ad impressions for that term. Low impression share plus a high rank number on your money keywords means competitors are outbidding you; raise bids or budget if those terms are profitable.
- Search Term Impression Rank: a rank of 3 means you received the third most SP ad impressions for that term.
- Top-of-Search Impression Share: how often you hold the premium top-of-search placement, the highest-CVR slot.
- Search Query Performance (SQP) share funnel (Brand Analytics): per query you get Search Query Volume, Impressions, Clicks, Add to Carts, Purchases, plus your brand's Impression Share, Click Share, Cart Add Share, and Purchase Share (your catalog ÷ market total at each funnel stage). SQP covers both organic and paid, so it will never reconcile with ad-console figures. If Impression Share is high but Purchase Share drops off, you are visible but losing the conversion battle (price, reviews, offer). If Impression Share itself is low, it is a visibility problem (SEO plus ad coverage).

## 8. Where to find each metric (current menu paths)

- ACOS, ROAS, Spend, Sales, Orders, CTR, CPC, Impressions, Clicks, CVR: Ad console, Campaign Manager (columns) and Report Center.
- NTB metrics and video/DPV metrics: Ad console reports and columns (SB/SD/Sponsored TV); add NTB and video columns in Campaign Manager.
- Search Term Impression Share and Rank: Ad console, Reports / Report Center, Sponsored Products, Search Term Impression Share report.
- Search Query Performance (SQP) share funnel: Seller Central, Brands, Brand Analytics, Search Query Performance (Brand Registry required).
- TACOS: not native. Compute as Ad Spend (ad console) ÷ Total Sales (Seller Central, Business Reports).

## 9. 2026 default benchmark bands (use only when category data is missing)

Account-wide averages (Ad Badger Feb to Mar 2026; Autron and goTrellis 2026):

- ACOS ~30% (range 25 to 36%; Jan 2026 peak 32.5%)
- CPC ~$1.22 ($0.75 to $3.50+ in competitive categories)
- CTR ~0.58% (SP 0.3 to 0.6%, SB 0.2 to 0.4%, SD 0.1 to 0.3%)
- CVR ~11% (10 to 15% for well-optimized SP listings with strong reviews; SB 8 to 12%, SD 5 to 10%)
- ROAS ~2.5 to 5.0x

Sponsored Brands and Sponsored Display run lower CTR and CVR and higher ACOS than Sponsored Products. A useful default "healthy" frame: ACOS at or under break-even; CTR at or above 0.4% (SP); CVR at or above 10%; CPC within max-profitable-CPC = CVR × price × target ACOS.

Caution: these come from third-party agencies and tools, not from Amazon, and they vary by data sample. Category, price, and lifecycle stage drive large variance. Treat any value far outside these bands as a flag to investigate, not a verdict, and always compare ACOS to the seller's own break-even rather than to the average.

## Sources

- What is advertising cost of sales (ACOS)? Calculation and tips, Amazon Ads. https://advertising.amazon.com/library/guides/acos-advertising-cost-of-sales
- Sponsored ads new-to-brand metrics, Amazon Ads Support Center. https://advertising.amazon.com/help/G5EWB37XK4RS4J4T
- Streaming TV performance metrics, Amazon Ads Support Center. https://advertising.amazon.in/help/GXRPB8WAPEZEU2N5
- What is CPC (cost per click)? How PPC advertising works, Amazon Ads. https://advertising.amazon.com/library/guides/cost-per-click
- Search term impression share report for Sponsored Products, Amazon Ads. https://advertising.amazon.com/resources/whats-new/search-term-impression-report-sponsored-products
- Video view metrics now available for Sponsored Brands video, Amazon Ads. https://advertising.amazon.com/resources/whats-new/sponsored-brands-video-view-metrics
- Amazon Total ACoS (TACoS): Introduction to a Key Ad Metric, Perpetua. https://perpetua.io/blog-amazon-tacos/
- Amazon ACoS: What Is Advertising Cost of Sale and How to Improve It, Perpetua. https://perpetua.io/blog-amazon-advertising-cost-of-sale-acos/
- Amazon Search Query Performance Report, Perpetua. https://perpetua.io/blog-amazon-search-query-performance/
- Break-Even ACoS Formula for Amazon PPC, Ad Badger. https://www.adbadger.com/blog/amazon-ppc-education/break-even-amazon-acos/
- Amazon Advertising Benchmarks 2026: Stats Every Seller Needs, Ad Badger. https://www.adbadger.com/blog/amazon-advertising-stats/
- Amazon Ads Benchmarks by Category and Ad Type (2026 Update), Trellis. https://gotrellis.com/resources/blog/amazon-advertising-benchmarks/
- Amazon PPC Benchmarks by Category (2026), Autron. https://autron.ai/benchmark/amazon-ppc-benchmarks-by-category-2026
- 10 Amazon Sponsored Brands Video Engagement Metrics to Track, Trellis. https://gotrellis.com/resources/blog/10-new-amazon-sponsored-brands-video-engagement-metrics/
