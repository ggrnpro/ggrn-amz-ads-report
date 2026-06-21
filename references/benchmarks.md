# Amazon Ads benchmarks (2026)

This file holds the 2026 benchmark numbers the skill uses to judge an uploaded account. Read it when you need a comparison band for CTR, CVR, ACOS, or CPC by ad type or product category, or when you set goal-based target ranges. Treat every number here as a sanity band, not a verdict. The decisive test for ACOS is always the seller's own break-even, covered in the last section.

All figures come from the two source JSONs (Trellis, Autron, Ad Badger). Where a category number is not in those sources, the table says so rather than guessing.

## By ad type (Sponsored Products / Brands / Display)

Source: Trellis 2026, with CPC cross-checked against Autron and goTrellis ranges.

| Ad type | CTR | CVR | ACOS | CPC |
|---|---|---|---|---|
| Sponsored Products | 0.3 to 0.6% | 10 to 15% | 20 to 35% | $0.75 to $2.50 (up to $3.50+ in competitive categories) |
| Sponsored Brands | 0.2 to 0.4% | 8 to 12% | 25 to 40% | not separately published in sources; runs at or above SP CPC |
| Sponsored Display | 0.1 to 0.3% | 5 to 10% | 30 to 50% | not separately published in sources; varies (CPC or vCPM) |

Reading notes:
- Sponsored Brands and Sponsored Display run lower CTR and CVR and higher ACOS than Sponsored Products. That is expected, not a problem on its own. SP is the foundation; SB and SD carry more upper-funnel and brand work.
- For Sponsored Display, judge click-based orders, not view-through (VCPM) totals. View-through attribution inflates results.

## Category conversion rate (CVR)

Source: Trellis 2026 category CVR examples. Only the four categories below appear in the sources. For any category not listed here, there is no source figure, so fall back to the account-wide CVR band (about 10 to 15% for optimized listings) and flag that no category-specific benchmark was available.

| Category | CVR |
|---|---|
| Beauty | 12 to 15% |
| Health / Household | 11 to 14% |
| Home / Kitchen | 10 to 13% |
| Apparel | 8 to 11% |
| Other categories (Electronics, Toys, Grocery, Pet, etc.) | not in sources; use account-wide 10 to 15% and note the gap |

Note: a CVR below roughly 8% in most categories points to a listing problem (price, images, reviews, ratings, availability, Buy Box) when CTR is healthy. CVR is a listing and offer metric, not a bidding metric.

## Account-wide 2026 averages

These are blended, cross-category baselines. Use them when the seller has no category data, and always caveat that category, price, and lifecycle stage drive large variance.

| Metric | Ad Badger (Feb to Mar 2026) | Autron 2026 |
|---|---|---|
| ACOS | ~29.6% (range 25 to 36%; Jan 2026 peak 32.5%) | 32.48% |
| CPC | ~$1.22 | $1.18 |
| CTR | ~0.58% | 0.59% |
| CVR | ~11.1% | 11.55% |

A practical "healthy" default frame when category data is missing: ACOS at or under break-even, CTR at least 0.4% (SP), CVR at least 10%, CPC within the max-profitable-CPC ceiling (CVR x price x target ACOS), ROAS roughly 2.5x to 5.0x.

## Goal-based target ranges

The right ACOS target depends on the goal for that campaign or SKU, not on the average. Two broad postures:

| Posture | When to use it | ACOS stance | TACOS stance | What to optimize for |
|---|---|---|---|---|
| Launch / aggressive | New product, ranking push, market-share grab, competitive defense | Allowed to run at or above break-even, sometimes well above, on purpose | Rising TACOS is acceptable during launch or expansion | Rank, impression share on money terms, New-to-Brand (NTB) share on SB/SD, branded-search lift. Do not judge on click-ROAS alone. |
| Profit / defend | Mature SKU, steady-state, margin protection | Target ACOS set below break-even, a few points under contribution margin | Stable or falling TACOS at steady or rising total sales (the flywheel working) | Efficiency: ACOS under target, low wasted spend, tight negatives, harvested converters |

Supporting math (same in both postures, only the target moves):
- Break-even ACOS = pre-ad profit margin %.
- Target ACOS = break-even ACOS minus the profit margin you want to keep. Example (Perpetua): 25% pre-ad margin minus 10% desired post-ad profit = 15% target ACOS.
- Max profitable CPC = CVR x selling price x target ACOS.
- Mature-brand TACOS often lands around 8 to 15%, but there is no universal benchmark; the trend matters more than the level.

## How to use these numbers (read this before flagging anything)

ACOS is judged against the seller's break-even ACOS, not against the averages on this page. Break-even ACOS equals the seller's pre-ad profit margin. An ACOS that is "high" versus the 30% account average can still be profitable if the seller's margin is 55%, and an ACOS that looks "low" can be a loss if the margin is thin. Collect the seller's margin first; without it you cannot say whether any ACOS is good. Flag a campaign or SKU above break-even as unprofitable, and one between target and break-even as a watch item.

All third-party benchmark numbers here are indicative, not authoritative. Amazon does not publish official "healthy" numbers for ACOS, CTR, CVR, or CPC. Every band on this page comes from agency and tool datasets (Trellis, Autron, Ad Badger) whose samples differ, so the figures vary between sources and from year to year. Use them to decide what to investigate, never as an automatic pass or fail. The seller's margin and goal override the averages every time.

## Sources

- Amazon Ads Benchmarks by Category and Ad Type (2026 Update), Trellis: https://gotrellis.com/resources/blog/amazon-advertising-benchmarks/
- Amazon Advertising Benchmarks 2026, Autron: https://autron.ai/blog/amazon-advertising-benchmarks-2026
- Amazon PPC Benchmarks by Category (2026), Autron: https://autron.ai/benchmark/amazon-ppc-benchmarks-by-category-2026
- Amazon Advertising Benchmarks 2026: Stats Every Seller Needs, Ad Badger: https://www.adbadger.com/blog/amazon-advertising-stats/
- Amazon ACoS: Calculate Your Target Based on Margins, SupplyKick: https://www.supplykick.com/blog/advertising-on-amazon-what-is-acos
- Amazon ACoS: What Is Advertising Cost of Sale and How to Improve It, Perpetua: https://perpetua.io/blog-amazon-advertising-cost-of-sale-acos/
- Break-Even ACoS Formula for Amazon PPC, Ad Badger: https://www.adbadger.com/blog/amazon-ppc-education/break-even-amazon-acos/
- Amazon Total ACoS (TACoS): Introduction to a Key Ad Metric, Perpetua: https://perpetua.io/blog-amazon-tacos/
