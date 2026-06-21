# Analysis playbook and scoring rubric

This file is the analysis engine of the amazon-ads-analyzer skill. Read it when you need to turn a seller's raw Amazon Ads exports into findings, a health score, and a ranked fix list. It has two halves: the agency-grade audit pipeline plus scoring rubric, and a set of practitioner heuristics from r/PPC and the FBA seller forums that explain the "why" behind each threshold in plain terms. All metrics are current as of 2026. Every number here varies by margin, price, and niche, so derive thresholds from the seller's own economics wherever possible and state your assumptions out loud.

## Inputs to ask for or detect

Minimum: a Search Term report (SP) and a Targeting report (SP). Better: add Advertised Product, Placement, Campaign, and Budget reports, plus the product's cost/margin and sell price. For brand work, add Sponsored Brands Keyword, Search term, and Attributed Purchases (NTB). For Sponsored Display, add the SD Campaign report (and read click-based orders, not view-through totals).

2026 console path: Measurement and Reporting > Sponsored ads reports > [Report category: SP / SB / SD / Attribution] > [Report type]. Sponsored Products now exposes 13 report types including Search term, Targeting, Advertised product, Campaign, Placement, Purchased product, Budget, Search Term Impression Share, Audience, Performance Over Time, Gross and Invalid Traffic, Video, and the new Prompts report (performance inside Rufus AI shopping suggestions). When ingesting uploads, verify report names against this 2026 set. Prompts (Rufus) and Search Term Impression Share are newer, so a non-expert may not have them. Treat any Rufus/Prompts analysis as emerging and lightly documented.

## The 9-step audit pipeline

Run these in order. Each step names the report it reads and the decision it produces.

1. Account structure review. Confirm that auto campaigns are used only for discovery and harvesting (not as the whole account), that manual campaigns control bids at the keyword or ASIN level, that high-volume SKUs are isolated into dedicated campaigns, that branded terms are isolated from non-branded and competitor terms, that portfolios group budgets sensibly, and that the SP to SB to SD mix is reasonable (SP is the foundation). The two most common findings are over-reliance on auto and branded blended with generic.

2. Search-term harvest plan. From the Search Term report (last 14 to 30 days), harvest any term with 3 or more orders at ACOS below target by promoting it to exact match in a manual campaign. This is "graduation." Sequence the matching negation carefully (see step 3 and the negation rules below).

3. Wasted-spend and negation analysis. Negate any term with 10 or more clicks and 0 orders as a quick first pass. Then refine with the ratio rule: the real pause threshold is 2 to 3 times the product's average clicks-per-sale. A 10% CVR product converts about every 10 clicks, so the escalation point is roughly 30 to 35 clicks with 0 sales. High-AOV products tolerate far more pre-sale spend (budget tolerance is roughly target ACOS times price). Use 10 clicks / 0 orders as a warning, and escalate to fail only at about 3 times expected clicks-per-sale or when spend on the term exceeds the target CPA.

4. ACOS and TACOS versus margin-derived target. Break-even ACOS equals the pre-ad profit margin percent. Target ACOS equals break-even minus the desired profit. TACOS equals ad spend divided by total revenue (including organic). A rough max-TACOS guardrail is net margin percent times an efficiency factor (about 30 to 60%). Compute ACOS by campaign and by ASIN (Advertised Product report). Flag SKUs or campaigns above break-even as unprofitable (fail), and those between target and break-even as watch (warning).

5. Placement and bid optimization. From the Placement report, compare Top of Search, Product Pages (Rest of Detail), and Rest of Search. If Top of Search has higher CTR and CVR, apply a positive Top-of-Search modifier (Amazon allows up to +900%), sized to measured lift. Flag all-zero modifiers (lift left on the table) and blanket max modifiers with no CVR justification. From the Targeting report, cut bids 20% on targets running 50%+ above target ACOS and raise bids 15% on targets running 30%+ below target ACOS. Review monthly and measure incremental lift before scaling multipliers, since they inflate cost.

6. Funnel diagnosis (the core "ad problem vs listing problem" logic). This is the central diagnostic of the whole skill. Branch on the two ad metrics:
   - Low CTR (below the roughly 0.3 to 0.6% SP benchmark) points to the ad and discovery layer: main image, title, price shown, or keyword relevance.
   - Healthy CTR but low CVR points to the listing and offer layer: price (too high or too low), listing quality, reviews and ratings, availability or Buy Box, or relevance. PPC cannot fix a listing problem. Surface it to the seller as a listing action, not a bid change.

7. Budget pacing, caps, and dayparting. Use the Budget report's time-in-budget. Flag campaigns going out-of-budget before the day ends (constrained winners to fund) and overfunded underperformers. Dayparting applies an hourly or weekly multiplier on the base bid to concentrate spend in profitable hours; start modest (10 to 20%). Treat dayparting as a refinement, not a fail, and see the practitioner note below on when it is worth the effort.

8. Branded vs non-branded plus NTB. Split spend into branded and non-branded buckets and report each ACOS separately; blending hides true acquisition cost. New-to-Brand (NTB) measures orders and sales from customers who have not bought from the brand in the prior 12 months. NTB is not available for Sponsored Products; read it from Sponsored Brands (Attributed Purchases) and SD/DSP. High branded share with low NTB% suggests low-incrementality spend (paying for demand you would win organically). Rising NTB% on SB/SD is healthy new-customer acquisition.

9. SB / SD / DSP specifics. SB carries NTB, Category benchmark, and Brand Store traffic; video SB usually outperforms static. SD VCPM caveat: evaluate click-based orders, not view-through totals, because view-through attribution inflates results and can mask organic cannibalization. DSP and Sponsored TV are CPM and upper-funnel; judge them on reach, NTB lift, and branded-search lift, not click ACOS.

## Funnel diagnosis quick reference

| Symptom | Layer | Likely cause | Action owner |
|---|---|---|---|
| Low CTR (< ~0.3% SP) | Ad / discovery | Main image, title, price shown, keyword relevance | PPC + creative |
| Healthy CTR, low CVR (< ~5%) | Listing / offer | Price, listing quality, reviews, Buy Box, stock | Seller (listing fix, not bids) |
| Healthy CTR and CVR, high ACOS | Economics | Bid too high vs margin, wrong target ACOS | PPC (bid / target) |
| Low impressions | Auction / budget | Bid too low, budget capped, low relevance | PPC (bid / budget) |

## 2026 benchmarks by ad type

Use these as sanity ranges. Judge ACOS against the SKU's own margin first, then against these bands.

| Ad type | CTR | CVR | ACOS | CPC |
|---|---|---|---|---|
| Sponsored Products | 0.3 to 0.6% | 10 to 15% | 20 to 35% | $0.75 to $2.50 |
| Sponsored Brands | 0.2 to 0.4% | 8 to 12% | 25 to 40% | about SP or higher |
| Sponsored Display | 0.1 to 0.3% | 5 to 10% | 30 to 50% | variable |

Aggregate 2026 baselines: average ACOS 32.48%, average CPC $1.18, average CTR 0.59%, average CVR 11.55%. Category CVR examples: Beauty 12 to 15%, Health/Household 11 to 14%, Home/Kitchen 10 to 13%, Apparel 8 to 11%. CVR below about 8% in most categories points to a listing problem; CTR below about 0.3% points to an ad or creative problem.

## Scoring categories and weights

The health score is a weighted 0 to 100. Weights are a defensible synthesis aligned to the benchmarks above (no agency publishes a numeric rubric publicly), so tune them against real reports.

| # | Category | Weight |
|---|---|---|
| 1 | Profitability (ACOS vs target, TACOS, unprofitable-SKU share) | 22 |
| 2 | Wasted spend / negation discipline | 18 |
| 3 | Search-term harvesting and match-type structure | 14 |
| 4 | Account/campaign structure (auto vs manual, ASIN coverage, branded isolation) | 12 |
| 5 | Funnel health (CTR and CVR vs benchmark) | 12 |
| 6 | Bid and placement optimization | 8 |
| 7 | Budget pacing / caps / dayparting | 6 |
| 8 | Branded vs non-branded split and NTB | 5 |
| 9 | SB/SD/DSP setup and VCPM hygiene | 3 |

## Checks table

| Check | How to evaluate | Pass | Warning | Fail | Severity |
|---|---|---|---|---|---|
| Wasted-spend terms | Search Term report: terms with clicks but 0 orders | < 5% of spend on zero-sale terms | 5 to 15%; terms at 10+ clicks / 0 orders exist | > 15% of spend wasted, or terms past 3x clicks-per-sale still live | High |
| Negative keyword discipline | Presence of negatives; recurring irrelevant terms | Negatives applied, few new offenders weekly | Sparse negatives | No negatives anywhere | High |
| Harvest execution | Converters (3+ orders, sub-target ACOS) promoted to exact | Converters graduated, negated in source after migration | Some converters un-promoted | Auto carries all sales, no manual exacts | Med |
| ACOS vs target (campaign) | ACOS vs target (break-even minus profit) | At or below target | Between target and break-even | Above break-even | High |
| Unprofitable SKUs | Per-ASIN ACOS vs that SKU's break-even | 0 SKUs above break-even | 1 to 2 marginal SKUs | Multiple SKUs bleeding | High |
| TACOS trend | Ad spend / total revenue over time | Flat or down with sales growth | Rising slowly | Rising while sales flat | Med |
| Auto vs manual balance | Share of spend / structure in auto | Auto = harvest only | Auto > 50% of spend | Account is one auto campaign | Med |
| Branded isolation | Branded terms in own campaigns | Fully separated | Partially mixed | Branded blended with generic | Med |
| ASIN coverage | Active SKUs with ads vs catalog | Key SKUs covered and isolated | Gaps on some movers | Top sellers unadvertised | Med |
| CTR (ad problem) | CTR vs 0.3 to 0.6% SP benchmark | At or above benchmark | 0.15 to 0.3% | Below 0.15% (image / title / price / relevance) | High |
| CVR (listing problem) | CVR (given healthy CTR) vs category | At or above category benchmark | 5 to 8% | Below 5% with healthy CTR (listing / price / reviews / stock) | High |
| Placement modifiers | Placement report ToS vs others vs modifiers in use | Data-backed modifiers set | All 0% modifiers | Blanket max modifier, no lift data | Low |
| Bid responsiveness | Targeting report: high-ACOS targets at high bids | Bids tied to target ACOS | Some stale high bids | Overspending targets untouched | Med |
| Budget caps | Budget report time-in-budget | Winners not capped | Some out-of-budget hours | Top campaigns capped, weak ones overspend | Med |
| Dayparting | Hourly ACOS variance vs flat delivery | Applied where data warrants | Opportunity unused | n/a (refinement only) | Low |
| NTB / acquisition | SB/SD NTB%; branded share | Healthy NTB on SB/SD | Low NTB, high branded share | All spend branded, near-zero NTB | Low |
| SD VCPM hygiene | SD Campaign: click-based vs total orders | Judged on click-based orders | Mixed reporting | ACOS claimed on view-through | Low |

## Reporting rules (avoid the classic audit mistakes)

Always tie ACOS to margin, never to a generic number. Output a short ranked fix list rather than 50 simultaneous changes, because too many overlapping changes break attribution. Explicitly flag likely non-incremental branded spend. Label listing-side issues as seller actions that PPC cannot fix. Re-run on a cadence, since audit insights decay quickly. The crude thresholds here (10 clicks / 0 orders, 3 orders to harvest) come from published agency workflows; other agencies use slightly different counts (7 to 15 clicks, or a spend-based trigger like more than 1x target CPA), so treat exact numbers as defaults, not universal law.

## Practitioner heuristics and common mistakes

These are community rules of thumb, upvote-weighted from r/PPC, r/FulfillmentByAmazon, r/AmazonFBA, and r/AmazonSeller. They are not Amazon-published numbers and they shift with margin, price, and niche. Use them to flag and explain, always paired with the reasoning so a non-expert understands the "why." When in doubt, state the assumption (for example, "assuming a 10% conversion rate").

### Use the CVR-based click rule, not a flat number

The single most common beginner mistake is killing a keyword after 3 to 6 clicks. The community rule:

> Clicks-to-judge is about 2 divided by conversion rate.
> - 20% CVR means about 10 clicks before a zero-sale keyword means anything
> - 10% CVR means about 20 clicks (10% is the common Amazon default to assume)
> - 5% CVR means about 40 clicks

Why: at a 10% CVR, 1 in 10 clicks converts, so pausing at 11 clicks with 0 sales is premature. By about 20 clicks you have had roughly a 90% chance at a sale, and only then is zero sales a real signal. This reconciles with the agency rule in step 3: the agency "10 clicks / 0 orders" line is just the 20% CVR case of the same formula, and the agency "30 to 35 clicks" escalation is the 10% CVR case. Use 2 divided by CVR as the single underlying rule, and treat any flat click count as a special case of it. Below threshold means insufficient data, not a problem.

### Wait out the attribution lag before acting

Always wait at least 1 week, ideally 2, before killing a keyword or campaign, because Amazon attributes purchases up to about 7 to 14 days after the click. Recent days understate conversions. Never judge on fewer than 7 days of data. Flag any user reacting to less than a week of data. Use 30-day windows to find rising-star winners and shorter 7 or 14-day windows for recent trend.

### Spend-based pause as an alternative to the click rule

A cross-platform version expressed in spend: when spend on a single keyword exceeds about 5 times your target or break-even cost-per-acquisition with 0 orders, it is a pause candidate (a lighter 2 to 3 times CPA version also circulates). This is the same idea as the agency "spend > target CPA" escalation, just at a higher multiple. Before pausing, check the search-term report. The wasted spend may be one bad query inside a broad keyword that you can negate instead of killing the whole keyword.

### Clicks but no sales is usually a listing problem

If clicks are healthy (CTR is fine) but orders are zero across many terms, the listing is failing to convert: price, main image, reviews, A+ content. "31 clicks no sale equals something wrong with your listing." Fix the listing before thrashing bids. For a main keyword, practitioners drop the bid to about $0.20 and fix the listing rather than pausing. This is the forum-level expression of the funnel diagnosis in step 6.

### TACOS is the north star, break-even ACOS is the guardrail

Optimizing raw ACOS to the floor while ignoring the whole picture is the most-mocked beginner behavior. A consultant boasting a 100% target ACOS got dunked (26 upvotes): "Not all ACOS are equal, the most important factor is conversion rate, actively targeting 100% as a default is shameful." The discipline:
- Break-even ACOS equals margin divided by price. It is the guardrail line, not the target.
- Go above break-even deliberately for launch and ranking; stay below it for profit campaigns.
- Judge the business on TACOS (total ad spend divided by total revenue). "If increasing ACOS decreases TACOS, go for it."
- For consumables and subscriptions, target break-even ACOS and make profit on LTV and repeat purchases. LTV and TACOS matter more than ACOS.

Make TACOS the headline metric with break-even ACOS as the guardrail. High ACOS is acceptable only if TACOS is trending down and organic rank is rising. Flag a single ranking campaign judged on its ACOS in isolation.

### Classify every campaign by goal: launch, profit, or defensive

Push spend toward break-even ACOS during launch, because sales velocity drives BSR, which drives organic rank, which compounds into free organic sales and badges ("Amazon's Choice", "1K+ bought"). The nuance: if you already rank #1 organically and dominate the niche, break-even PPC on those terms just burns margin. Switch to defensive PPC (block competitors, defend branded terms) and test adjacent or higher-volume keywords instead. Classify each campaign:
- Launch / ranking: tolerate high ACOS, watch TACOS and organic rank.
- Profit: keep under break-even.
- Defensive: branded plus competitor-ASIN defense.

Flag spending at break-even on keywords the seller already owns organically.

### Harvesting cadence and the discovery-to-exact pipeline

The loop experienced sellers run:
1. Discovery layer: auto plus broad campaigns to surface what real shoppers type.
2. Weekly (or biweekly) Search-Term report review.
3. Graduate converting search terms into exact-match (often single-keyword) manual campaigns.
4. Negate clearly irrelevant high-spend zero-sale terms.

"Every week auto gets cleaner and manual gets stronger; after 6 to 8 weeks it compounds." Caveat: harvested keywords often underperform their source campaign for the first 1 to 2 weeks, so do not panic-kill a freshly graduated keyword. An account with auto only, no negatives, and no graduation is structurally incomplete.

### Over-negation kills accounts quietly

Over-negation is a recognized and rising failure mode:
- Do not blanket-negate every zero-sale term over a time window. "This kills campaigns quietly. Low-volume search terms often rotate," so a zero-sale snapshot of a low-volume term is unreliable.
- Only negate clearly irrelevant intent. Somewhat-relevant terms often still convert at acceptable ACOS.
- Negative exact match is broader than it looks (an expensive trap). Amazon treats singular and plural as matches and ignores stop-words (in, of, for, by, the, with). Negating "box for candy" (0 sales) also blocks "boxes of candy," "box of candy," "box candy," "box with candy," and so on, one of which may be a top seller. Always check for a profitable close variant before adding a negative exact.
- Do not negate a winner you are also retargeting until the new exact campaign is actually winning impressions, or you starve it. Sequence: graduate, confirm the exact campaign gets traffic, then negate in the source. This is the careful sequencing referenced in pipeline steps 2 and 3.
- Mind assisted conversions. A generic or upper-funnel term may get the early click while branded or exact gets the last-click sale. On Amazon's last-click console this is hard to see, so be lenient with zero-last-click generic terms and reserve hard negation for irrelevant terms.

### Single-keyword / single-intent structure wins on Amazon

The "house of cards" post (129 upvotes) is the canonical argument. Multi-keyword, mixed-match campaigns break because:
1. Placement bid modifiers apply to the whole campaign, so you cannot boost Top-of-Search for one keyword without boosting all of them.
2. Keywords convert differently per placement, so blended ACOS is unreadable (a "20% ACOS campaign" can be 5% branded plus 50% generic).
3. Impression suppression: Amazon's ML funnels budget to whichever keyword gains traction first (usually the broad, high-volume one), starving good keywords.
4. Campaign-level negatives can block profitable terms belonging to other keywords in the same campaign.

Rules: single-keyword campaigns for roughly 1,000+ monthly-search-volume, hyper-relevant, or branded keywords; let auto and broad discovery pick up the long tail. Never mix match types in one campaign. One ASIN per campaign for clean data. Cross-platform dissent: in Google Ads, SKAGs are considered dead (replaced by single-theme or single-intent ad groups), but on Amazon the single-keyword approach persists specifically for placement control. Caution: this multiplies campaign count and can blow up spend, so gate it by search volume and watch budgets. Flag mixed match types in one campaign, many keywords per ad group, and multiple parent ASINs per campaign.

### Reading the Placement report and bid multipliers

- The base bid wins the underlying auction; the Top-of-Search modifier signals how much more you will pay for that spot. A low base bid plus a big TOS modifier loses the auction. One seller's TOS-to-Product-Page impression ratio collapsed from 1:3 to 1:25 after doing exactly that.
- Stacking order: the placement adjustment applies first, then Dynamic "Down Only" can reduce from there.
- TOS is not always most profitable. Rest-of-search or Product-pages sometimes convert better or cheaper. Read CVR and ACOS per placement and set modifiers toward whatever converts.
- Because modifiers are campaign-wide, meaningful placement optimization basically requires single-keyword or single-intent campaigns (ties to the structure section above).

Flag a gutted base bid faking TOS via a modifier.

### Down Only as the default bidding strategy

- Dynamic Bids, Down Only is the practitioner default for steady-state and profit campaigns (it lowers bids when a click is unlikely to convert), layered with a TOS placement modifier.
- Up and Down can raise bids up to +100% on top placements. Use it for launch and ranking, but it is a spend risk on mature campaigns ("Amazon may decide you'll convert when you don't").
- Fixed is used for deliberate ranking pushes.

Flag Up and Down running on mature profit campaigns as a likely overspend.

### Dayparting is mostly overrated for small accounts

Majority view: "Dayparting is overrated, it can save a little spend but it's not worth the effort." And: "don't bother with hourly-parting under about $1k/day ad spend." Turning ads fully off overnight can hurt next-day ramp and momentum. A minority use spend-versus-sales heatmaps to trim low-converting hours, but that is usually tool-vendor framing. For most users, do not recommend dayparting; suggest pulling the hourly report to sanity-check, and only consider it above about $1k/day. This refines pipeline step 7.

### Budget headroom: do not cap your winners

"Keep budget $100 to $200 above average daily spend so a search-volume spike doesn't make you run out and miss sales." The deeper rule: if every search term runs below your max or break-even ACOS, everything is profitable, so you should want to spend more. Only cap to throttle unprofitable spend. Budget exhaustion on a profitable campaign equals lost impressions, which is a real mistake. Flag campaigns hitting their daily cap early; for profitable ones, recommend raising the cap to average daily spend plus $100 to $200 rather than capping.

### The newbie-mistake cluster

- One giant auto campaign, no negatives, no harvesting. Fine as a discovery layer, fatal as the whole strategy ("if you ONLY use automatic campaigns you're losing money").
- Running PPC before the listing is ready. Get at least about 5 reviews (ideally 15 to 50) and solid images and price first, or you generate noise and bad data. Counter-view: do not over-wait for 20+ reviews and miss the cold-start visibility boost.
- Impulse changes. Do not react to one bad day with big bid or placement swings; weekly volume, competitor coupons, and seasonality are outside your control. Change one variable at a time and log every bid change to measure impact.
- Mixing match types in one campaign or many keywords per ad group (see the structure section).
- Ignoring organic rank. The entire point of tolerating PPC losses during launch is organic-rank gain. If rank is not tracked, you cannot tell whether aggressive ACOS is paying off.

### Quick-reference thresholds

State these as heuristics and adjust for margin and niche.

| Heuristic | Community rule of thumb |
|---|---|
| Clicks before judging a zero-sale keyword | about 2 / CVR (about 10 at 20%, about 20 at 10%, about 40 at 5%) |
| Minimum data window before acting | at least 1 week, ideally 2 (attribution lag about 7 to 14 days) |
| Spend-based pause | spend > about 5x target CPA, 0 orders, then review search terms before pausing |
| Single-keyword campaign gate | keywords with about 1,000+ monthly searches (plus branded / hyper-relevant) |
| Budget headroom | average daily spend + $100 to $200 on profitable campaigns |
| Reviews before heavy PPC | at least about 5, ideally 15 to 50 |
| North-star metric | TACOS, with break-even ACOS as guardrail (not raw ACOS) |
| Dayparting | skip under about $1k/day ad spend |
| Default bid strategy | Down Only plus TOS modifier (Up and Down or Fixed for launch / ranking) |

## Sources

- Power Digital Marketing, "How to Conduct an Amazon PPC Audit in 2026": https://powerdigitalmarketing.com/blog/amazon-ppc-audit/
- PPC Ninja, "Amazon Ads Reports Guide 2026: Every Report Type Explained": https://www.ppcninja.com/blog/performance-over-time-report.html
- Ad Badger, "How to Optimize Keywords with 0 Sales in Amazon PPC": https://www.adbadger.com/blog/amazon-ppc-education/how-to-optimize-keywords-with-0-sales-in-amazon-ppc/
- Trellis, "Amazon Ads Benchmarks by Category and Ad Type (2026 Update)": https://gotrellis.com/resources/blog/amazon-advertising-benchmarks/
- SupplyKick, "Amazon ACoS: Calculate Your Target Based on Margins": https://www.supplykick.com/blog/advertising-on-amazon-what-is-acos
- PPC Ninja, "Amazon PPC KPIs Explained: ACoS, ROAS, TACoS & More": https://www.ppcninja.com/blog/amazon-ppc-kpis.html
- Amazon Ads Support Center, "Sponsored ads new-to-brand metrics": https://advertising.amazon.com/help/G5EWB37XK4RS4J4T
- Intentwise, "How marketers can use New-To-Brand metrics": https://www.intentwise.com/blog/amazon-advertising/how-marketers-can-use-new-to-brand-metrics/
- Amazon Ads, "Search term report for Sponsored Products": https://advertising.amazon.com/help/G3HEFZYWZF84NPS9
- Perpetua, "Maximizing the Impact of Amazon's Top-of-Search Ad Placements": https://perpetua.io/blog-maximizing-the-impact-of-top-of-search-amazon-ad-placements/
- Clear Ads, "10 Steps on How to Read Amazon Advertising Report": https://clearadsagency.com/amazon-reports/How-to-Read-Amazon-Advertising-Report
- AdLabs, "The Amazon PPC Dayparting Guide": https://adlabs.app/guides/amazon-dayparting-guide/
- Profasee, "Amazon Dayparting: The Complete 2026 Guide": https://profasee.com/blog/amazon-dayparting/
- Autron, "Amazon Advertising Benchmarks 2026": https://autron.ai/blog/amazon-advertising-benchmarks-2026
- Helium 10, "Free Amazon PPC Audit Tool": https://www.helium10.com/tools/free/ppc-audit/
- Junglr, "360 Ads Audit tool": https://junglr.com/360-ads-audit-tool/
- Reddit r/PPC, "Should I kill a keyword that has clicks but no sales... or just wait?": https://www.reddit.com/r/PPC/comments/1jrvvr6/should_i_kill_a_keyword_that_has_clicks_but_no/
- Reddit r/AmazonFBA, "Amazon PPC: How many clicks until you stop the keyword?": https://www.reddit.com/r/AmazonFBA/comments/1js7oao/amazon_ppc_how_many_clicks_until_you_stop_the/
- Reddit r/FulfillmentByAmazon, "How many clicks before evaluating a keyword?": https://www.reddit.com/r/FulfillmentByAmazon/comments/1eme68j/how_many_clicks_before_evaluating_a_keyword/
- Reddit r/FulfillmentByAmazon, "Many Amazon Sellers Mismanage Their PPC with the Wrong Campaign Structure": https://www.reddit.com/r/FulfillmentByAmazon/comments/1bw8y5d/many_amazon_sellers_mismanage_their_ppc_with_the/
- Reddit r/FulfillmentByAmazon, "So many people are focused on ACOS, it hurts my heart": https://www.reddit.com/r/FulfillmentByAmazon/comments/1ag7n77/so_many_people_are_focused_on_acos_it_hurts_my/
- Reddit r/FulfillmentByAmazon, "Why should PPC spend approach break-even ACOS?": https://www.reddit.com/r/FulfillmentByAmazon/comments/1ixedwm/why_should_ppc_spend_approach_breakeven_acos/
- Reddit r/AmazonFBA, "Amazon PPC mistakes you should avoid": https://www.reddit.com/r/AmazonFBA/comments/1jl6ypz/amazon_ppc_mistakes_you_should_avoid_that_iv_seen/
- Reddit r/FulfillmentByAmazon, "Overnegating keywords is why your Amazon PPC keeps losing": https://www.reddit.com/r/FulfillmentByAmazon/comments/1r1cwy6/overnegating_keywords_is_why_your_amazon_ppc/
- Reddit r/FulfillmentByAmazon, "Trying to Understand Adjusting Bids By Placement": https://www.reddit.com/r/FulfillmentByAmazon/comments/1kgriab/trying_to_understand_adjusting_bids_by_placement/
- Reddit r/PPC, "Bid Strategies + Bid Adjustments": https://www.reddit.com/r/PPC/comments/1sc5obr/bid_strategies_bid_adjustments/
- Reddit r/FulfillmentByAmazon, "Should I switch from dynamic PPC campaign to fixed?": https://www.reddit.com/r/FulfillmentByAmazon/comments/n1xvuz/should_i_switch_from_dynamic_ppc_campaign_to_fixed/
- Reddit r/FulfillmentByAmazon, "Amazon PPC tips for beginners and advanced": https://www.reddit.com/r/FulfillmentByAmazon/comments/1joqe85/amazon_ppc_tips_for_beginners_and_advanced_things/
- Reddit r/PPC, "At what point do you add a search term as negative keywords": https://www.reddit.com/r/PPC/comments/1baji7y/at_what_point_do_you_add_a_search_term_as/
- Reddit r/FulfillmentByAmazon, "PPC Day/hourly parting, what's working for me": https://www.reddit.com/r/FulfillmentByAmazon/comments/1ikzm8h/ppc_dayhourly_parting_whats_working_for_me_at_the/
- Reddit r/AmazonFBA, "Do you successfully use Dayparting to turn off ads over night": https://www.reddit.com/r/AmazonFBA/comments/1rxden5/do_you_successfully_use_dayparting_to_turn_off/
- Reddit r/FulfillmentByAmazon, "For those of you only using Automatic Campaigns... you're losing money": https://www.reddit.com/r/FulfillmentByAmazon/comments/ev9bbk/for_those_of_you_that_are_only_using_automatic/
- Reddit r/FulfillmentByAmazon, "Why Am I Not Getting Sales Despite High PPC Impressions?": https://www.reddit.com/r/FulfillmentByAmazon/comments/1hrd68q/why_am_i_not_getting_sales_despite_high_ppc/
- Reddit r/KDP, "The exact process I use every week to harvest keywords from auto": https://www.reddit.com/r/KDP/comments/1u8juzp/the_exact_process_i_use_every_week_to_harvest/
- Reddit r/PPC, "Is Single Keyword Ad Group (SKAG) still a thing?": https://www.reddit.com/r/PPC/comments/1hncq0r/is_single_keyword_ad_group_skag_is_still_a_thing/
