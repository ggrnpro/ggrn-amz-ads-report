# What changed in Amazon Ads (2025 to 2026)

This file tells the analyzer what is current in Amazon Ads as of mid-2026, so it does not flag old assumptions (siloed consoles, keyword-only discovery, same-day ROAS) as problems or miss new reports and levers. Read it before judging account structure, naming, creative, bidding, or report coverage. When a name or spec is load-bearing for a recommendation, verify against the live Amazon page, because Amazon renames and re-specs often (two renames already landed in 2026: "Rufus" became "Alexa for Shopping" on May 13, 2026, and Sponsored Display is merging into a unified "Display" / DSP path).

Source anchor: most changes below were announced at Amazon Ads unBoxed 2025 (Nov 11-12, 2025, Nashville).

## The big structural shift

Amazon moved from siloed consoles plus keyword matching to a single AI-driven, full-funnel platform plus persona and answer-based discovery. Four practical consequences for the analyzer:

1. One console, one report set. Sponsored Ads and Amazon DSP now share a unified Campaign Manager and a single reporting hub (15 months daily, 6 years monthly). Do not assume separate exports.
2. Creative is no longer a budget gate. Creative Agent generates image, video, audio, and Streaming-TV ads from an ASIN or URL for free. Flag quality and usage, not absence.
3. Discovery is partly conversational. Keyword and search-term reports are now one input. Alexa for Shopping (formerly Rufus) reads the listing as a source document, so PDP "answer-readiness" matters.
4. Metrics moved to long-term. Look for long-term sales ROAS and new-to-brand (NTB), not just same-day or one-time-sale ROAS.

## What changed and why you should check it

| Change (when) | What it is | What to now check that you didn't before |
|---|---|---|
| Unified Campaign Manager (Nov 2025) | Sponsored Ads console and Amazon DSP merged into one platform; centralized reporting, standardized metrics, AI search, format-based buying. Amazon cites 67% faster launches. | Expect SP/SB/SD/DSP/Streaming-TV in one export. Confirm which platform an upload came from; do not treat DSP and sponsored as separate worlds. |
| Creative Agent (Nov 2025) | Agentic AI builds full ads (multi-scene video, images, voiceover, music, end cards, Streaming TV spots) from an ASIN or URL in hours, free, via Creative Studio. | Stop auto-flagging "no video" as a budget issue. Check whether AI creative is used and is on-brand and differentiated (new failure mode: generic AI creative). |
| Ads Agent (Nov 2025) | AI drafts audience strategies and keywords from natural language; queries AMC conversationally. Amazon Ads MCP Server for partner agents. | Targeting may be AI-suggested, not hand-built. Validate that accepted audiences and keywords actually fit the product. |
| Full-funnel Campaigns (Nov 2025) | One campaign type spanning SP, SB, display, and Streaming TV; auto-rebalances budget, audience, and tactics; optimizes NTB and long-term sales. | Per-format ACOS can mislead inside a Full-funnel campaign (cross-subsidized by design). Identify these before judging any one format. |
| Sponsored Prompts and "Prompts" report (Nov 2025, beta) | Sponsored products surface inside Alexa-for-Shopping conversations; auto-enrolled, algorithmic placement (no prompt targeting yet). New Prompts report (Ads console, Reporting, Sponsored Products, Prompts). | New report to look for. Surface top prompt-impression ASINs and the natural-language questions driving them; map to PDP gaps. Judge on impressions (CTR and CVR are still low). |
| Rufus renamed Alexa for Shopping (May 13, 2026) | Rufus brand retired; tech folded into Alexa for Shopping (about 300M active customers, about $12B incremental annualized sales, per Amazon Q4 2025). COSMO handles retrieval and ranking. | Use 2026 naming. Treat keyword reports as partial. Recommend PDPs written for constraints, "best-for and not-ideal-for," and lifestyle scenarios so the AI can confidently recommend. |
| Sponsored Products video (Nov 2025, US, sellers and vendors) | Interactive: upload 1-5 feature videos per product; shopper sees up to 3 thumbnails by relevance, can skip to a feature, then clicks to PDP. Plus 9% CTR; 8x CTR for the 20% who watch more than 5 seconds. Bid adjustments boost placement. | Distinct from SB video. If the seller runs SP and has video, recommend enabling on existing campaigns (low effort). Check for multiple feature clips and the bid-adjustment lever. |
| SB reserve share of voice (Nov 2025) | Pre-purchase a top-of-search placement for branded keywords at a fixed upfront price (not auction). | For brand defense, launches, and Prime Day, check whether the seller locks top-of-search via reserve SOV instead of fighting the auction. |
| SB collections (Nov 2025) | Display multiple related catalog products in one shopper-friendly SB unit. | New SB creative option for catalog cross-sell; check whether it is used for multi-ASIN brands. |
| SB vertical video (9:16) | SB video supports vertical 9:16 and horizontal 16:9 (duration commonly 6-45s); vertical fits mobile, UGC, and creator authenticity. | If only running 16:9, recommend testing 9:16 for mobile and UGC. |
| Performance+ and Brand+ upgrades (Nov 2025) | DSP automated types: better AI targeting, mid-funnel consideration tactics, in-workflow creative optimization, and retargeting of SP-engaged users. | SP and DSP audiences now overlap. Check for retargeting double-counting between SP and DSP. |
| SP rule-based bidding (doc updated Dec 2025) | Set a ROAS guardrail; Amazon auto-moves base bids (down to minus 100%) to hit it (not guaranteed). Eligibility: 10+ days live, 10+ conversions in last 30 days, and a minimum daily budget (US/UK/EU 10 local currency; IN 300; JP 600; MX 50; BR 20). Guardrail evaluated on prior 21 days; auto-disables if 20-day ROAS drops below 30% of the 20-40 day ROAS, reverting to prior bidding. Scheduled bid rules also exist. | If bids move with no manual edits, suspect rule-based or AI bidding. Check a reverted campaign for an auto-disabled guardrail. Verify eligibility thresholds before recommending it. |
| Brand Analytics SQP, ASIN-level view | Search Query Performance now has an ASIN-level table (in addition to brand-level). Path: Seller Central, Brand Analytics, Search Analysis, Search Query Performance; toggle brand or ASIN. Shows impressions, clicks, cart-adds, purchases per search term, plus your share. | Brand-Registry-gated. Pull ASIN-level SQP to separate high impression share with low purchase share (a listing, price, or conversion problem) from low impression share (an ads or ranking problem). Distinct from the ad search-term report. |
| AMC: 25-month lookback, Prime Video signals, Ad Agent Skills (Nov 2025) | Lookback extended from 13 to 25 months (full year-over-year). Prime Video viewership signals in open beta. Conversational "Ad Agent Skills for AMC": clean-room queries with no SQL; no-code audience templates. | AMC is now usable by non-experts. Recommend it for cross-channel audiences, incrementality, and YoY. If they run Streaming TV, AMC can tie viewership to conversion. |
| Unified reporting and long-term ROAS (Nov 2025) | SP, DSP, and streaming in one dashboard; 15 months daily, 6 years monthly; emphasis on long-term sales ROAS; Authenticated Graph reaches about 90% of US households (deterministic). | Do not evaluate on same-day ROAS alone. Look for long-term ROAS and NTB. The 6-year monthly history enables seasonality benchmarking. |
| Sponsored TV becomes self-service Streaming TV | Self-service streaming-TV for brands of all sizes selling on Amazon (US, then UK and others); now a first-class API product, inside unified Campaign Manager and Full-funnel. Prime Video reach 315M+ global, 130M+ US monthly (Sept 2024 to Aug 2025). "Complete TV" is the DSP cross-publisher buying layer with upfront delivery guarantees. | CTV is no longer enterprise or DSP only. Small sellers can run self-service Sponsored TV, and Creative Agent makes the spot free. Flag as newly accessible upper-funnel. |
| Sponsored Display and DSP simplification | DSP simplified audience targeting (up to 10 include groups plus 1 exclude group per campaign). SD is converging into the unified "Display" path; on- and off-Amazon reach; Amazon-generated or custom creative. Self-service DSP minimum commonly cited around $35,000 (managed-service around $50,000). | Treat SD as converging with DSP; new campaigns may use the Display path. Do not recommend DSP to a tiny seller (about $35K floor). Emphasize off-Amazon reach and audience targeting. |

## Quick analyzer heuristics (2026)

- Report-name verification: "Search Query Performance" now has brand-level and ASIN-level tables; a new "Prompts" report exists; unified reporting replaces separate SP and DSP exports. If a user's export uses old names, they may be on an older console view.
- Do not penalize missing video creative. It is free via Creative Agent. Penalize unused or generic AI creative instead.
- Keyword data is partial. Pair search-term analysis with PDP answer-readiness for Alexa for Shopping, and check the Prompts report.
- Bid movement is not an error. Rule-based and AI bidding plus Full-funnel auto-optimization move bids and budgets on purpose.
- Use long-term ROAS and NTB where available, not same-day or one-time-sale ROAS.
- CTV is in scope for SMBs now via self-service Sponsored TV.

## Treat as unverified

The following could not be confirmed against an Amazon-official page. Do not state them as fact; verify before relying on them.

- Specific "Complete TV" inventory mix (for example Prime Video plus Netflix plus Paramount+), interactive pause ads or add-to-cart via remote, an official "Display Ads" rename with a fixed menu path, and 2026 CPC benchmarks (for example $1.05-1.65 SP). These come from agency or secondary sources. Amazon's own term is "Complete TV" for the DSP cross-publisher buying experience; the publisher mix should be re-verified.
- The exact Sponsored TV self-service launch date and current market availability. The self-service plus unified-console framing is 2025-2026; confirm the current Amazon product page.
- The self-service Amazon DSP minimum (about $35K) comes from agency blogs, not an Amazon page. Amazon's page states only the managed-service minimum (about $50K), and minimums vary by country and may have changed.
- SB video exact duration and spec limits change often. Pull the live ad-specs page before quoting 6-45s.
- COSMO's exact current role (shopper-facing versus internal ranking) is described variably by agencies.
- Agent persona names such as "Marty" or "Sparky" are not confirmed Amazon products. Sparky is Walmart's assistant. Do not present these as Amazon-official without verification.

## Sources

- unBoxed 2025 keynote recap, Amazon Ads: https://advertising.amazon.com/library/news/unboxed-2025-recap
- Show your products in action with Sponsored Products video, Amazon Ads: https://advertising.amazon.com/resources/whats-new/unboxed-2025-sponsored-products-video
- Sponsored Products rule-based bidding overview, Amazon Ads (Advanced Tools Center / API docs): https://advertising.amazon.com/API/docs/en-us/guides/rules/bidding-rules/overview
- Amazon Ads unBoxed 2025: Full-Funnel, Relevant, and Measurable, Skai: https://skai.io/blog/amazon-unboxed-2025/
- Alexa for Shopping: Optimization Strategies for 2026 (Rufus retired May 13, 2026), Tinuiti: https://tinuiti.com/blog/amazon/alexa-for-shopping/
- Search Query Performance dashboard, Amazon Seller Central: https://sellercentral.amazon.com/help/hub/reference/external/G8J4CB5ZBF3NX7TP
- New ASIN view in Brand Analytics Search Query Performance, Amazon Seller Central Forums: https://sellercentral.amazon.com/seller-forums/discussions/t/5b5759d6f424964254d38fd09bd03bd1
- Create streaming TV and video ad campaigns, Amazon Ads: https://advertising.amazon.com/solutions/products/video-ads
- Amazon Launches Sponsored TV To Bring Smaller Brands Into Streaming, NextTV: https://www.nexttv.com/news/amazon-launches-sponsored-tv-to-bring-smaller-brands-into-streaming
- Amazon DSP debuts simplified audience targeting experience, Amazon Ads: https://advertising.amazon.com/library/news/simplified-audience-targeting
- Amazon DSP: Advertise with a demand-side platform, Amazon Ads: https://advertising.amazon.com/solutions/products/amazon-dsp
- How to get started with Sponsored Brands video ads, Amazon Ads: https://advertising.amazon.com/library/guides/getting-started-with-sponsored-brands-video
- What's new in Amazon advertising for 2026?, Stape: https://stape.io/blog/amazon-advertising
- Amazon unBoxed 2025 Recap: AI Tools, Full-Funnel, Measurement, Flywheel Digital: https://www.flywheeldigital.com/blog/amazon-unboxed-2025-ai-full-funnel-recap
