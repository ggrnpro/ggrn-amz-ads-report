---
name: amazon-ads-analyzer
description: "Analyze Amazon advertising performance from exported reports or screenshots and produce a structured, self-contained HTML health report with a 0-100 score, a data-confidence score, benchmark comparison, prioritized findings, a search-term harvest and negatives plan, and an action plan. Use whenever the user wants to analyze, audit, review, or check Amazon Ads, Amazon PPC, Sponsored Products, Sponsored Brands, Sponsored Display, Sponsored TV, or Amazon DSP performance, understand their ACOS, TACOS, ROAS, or wasted spend, interpret an Amazon Advertising or Brand Analytics export, figure out why their Amazon ads are unprofitable, or asks 'how are my Amazon ads doing'. Also trigger when the user uploads an Amazon Search Term report, Campaign report, Targeting report, Bulk file, Business Report, Search Query Performance or Brand Analytics file, or a Helium 10 / Jungle Scout keyword export, or pastes Amazon ad metrics. Works for Amazon Seller Central and Vendor Central advertisers, brand-registered or not. Triggers in Russian too: 'проанализируй рекламу на Amazon', 'аудит рекламы Amazon', 'отчёт по рекламе Amazon', 'ACOS', 'почему реклама на Амазоне убыточна'."
license: MIT
metadata:
  version: 1.1.0
  author: Oleg Gagarin (https://ggrn.pro)
  domain: amazon-advertising
---

# Amazon Ads Analyzer

Turn a pile of Amazon advertising exports (and screenshots) into one clean,
self-contained HTML health report a seller or agency can read in two minutes and
act on the same day. The report carries a 0-100 health score, a data-confidence
score that tells the user how much to trust the result, KPI-versus-benchmark
cards, prioritized findings, a search-term harvest and negatives plan, an
ACOS-by-ASIN profitability table, a funnel diagnosis (is the problem the ad or
the listing?), and a prioritized action plan.

This is an analysis and strategy tool. It reads data the user provides. It does
not log into Amazon, change bids, or post anything. All work is local, and the
HTML report makes no external requests, so it is safe to email to a client.

A non-expert can use it. Most users do not know which of Amazon's dozen reports
to pull or where they live. The first job of this skill is to guide the upload
(see `references/data-collection-guide.md`), then work with whatever the user
actually provides, even a single screenshot, and clearly mark what extra data
would sharpen the result.

## When to run

Trigger on any request to analyze, audit, review, or check Amazon ads, to
understand ACOS, TACOS, ROAS, or wasted spend, to interpret an Amazon
Advertising or Brand Analytics export, or whenever the user attaches an Amazon
ad report or pastes Amazon ad metrics. If they only say "look at my Amazon ads"
with no file, start at step 1 and help them export the right reports.

## Workflow

Run these steps in order. The guiding idea: look at the real data before you
diagnose, derive targets from the seller's own margin (never a blanket "30% ACOS
is fine"), and read every metric inside the funnel rather than alone. Skipping
the intake and context step is the most common way an Amazon ad analysis goes
wrong.

### 1. Intake: get the data and the context

Ask for whatever the user has. Accept any combination. Exports are best, but
screenshots or pasted numbers work. If they are unsure what to pull, walk them
through `references/data-collection-guide.md`. It has click-by-click export
steps and explains where each report lives. The highest-value inputs:

1. Sponsored Products Search Term report (last 60 to 90 days). This is the
   single most important file. It drives harvesting and wasted-spend analysis.
2. Campaign, Advertised Product, Targeting, and Placement reports.
3. The Bulk Operations file, which holds the full account structure and bids in
   one sheet.
4. Sponsored Brands and Sponsored Display reports if those are running.
5. Business Reports (ASIN sessions and conversion rate) and, if brand-registered,
   Brand Analytics Search Query Performance. These tell you whether a weak result
   is an ad problem or a listing problem.

Bonus inputs that raise the confidence score (offer them, do not require them):

- A keyword export from Helium 10 (Cerebro, Magnet), Jungle Scout (Keyword
  Scout), Data Dive, or a similar tool, showing search volume, competition, and
  organic or sponsored rank. This lets the harvest and keyword priorities be
  data-backed rather than guessed.
- A product cost sheet (COGS, Amazon fees, sell price) so target ACOS is exact
  instead of a category default.
- A competitor or listing screenshot, and current inventory status.

Always capture the context too (ask if it is missing). It changes every
threshold:

- Marketplace (US, UK, DE, and so on), Seller vs Vendor, Brand Registered or not.
- Product category, which loads the right benchmark row.
- Goal: aggressive launch or rank, versus profit or defend.
- Contribution margin, or enough to estimate it (price, COGS, FBA fee, referral
  fee). Without margin you cannot set a correct target ACOS. If the user does not
  know it, say so in the report and use the category default, flagged as an
  assumption.

### 2. Parse what was provided

Read each file. Amazon exports are `.xlsx` or `.csv`. For `.xlsx` use the `xlsx`
skill or a quick pandas read. Normalize column names, because Amazon varies them
across report versions and marketplaces, and watch the attribution window:
Sponsored Products seller exports use 7-day columns, while Vendor, Sponsored
Brands, and Sponsored Display exports use 14-day. Identify, per row, the
dimension (campaign, ad group, search term, target, ASIN, or placement) and the
core columns (Impressions, Clicks, Spend, Sales, Orders, Units, plus any
new-to-brand columns). From screenshots, transcribe the visible numbers. Do not
invent values you cannot see. Record exactly what you received, because it
becomes the report's data-coverage and confidence sections.

### 3. Compute the metrics

Derive every KPI from the raw data. Do not trust a single summary tile. See
`references/metrics-glossary.md` for every formula and how to read it. At a
minimum, compute account-level and per-campaign and per-ASIN ACOS, ROAS, CTR,
CVR, CPC, and CPM, and, if total (organic plus ad) sales are available, TACOS and
its trend. Compute break-even ACOS from margin and the target ACOS for the stated
goal. These are the lines every other number is judged against.

### 4. Evaluate the checks

Work through the playbook in `references/analysis-playbook.md`. It defines, per
category, exactly what to look for and the pass, warning, and fail thresholds,
and it carries the weighted scoring rubric. Only score categories you have data
for. Renormalize the weights across the categories you can actually evaluate, and
list the rest under "not assessed".

Run the funnel diagnosis here too. It is what makes the report feel expert.
Compare CTR and CVR to the category benchmark to separate an ad or targeting
problem from a listing or conversion problem. Low CTR points to the main image,
title, price, or relevance. Healthy CTR but low CVR points to the listing, price,
reviews, or Buy Box. A high wasted-spend share points to negatives and relevance.

### 5. Score the account

Apply the weighted algorithm in `references/analysis-playbook.md` (pass earns
full points, warning half, fail zero, weighted by severity and category). Produce
the 0-100 score and a letter grade (A is 90 to 100, B is 75 to 89, C is 60 to 74,
D is 40 to 59, F is below 40).

### 6. Score the data confidence

Separately from the health score, judge how much to trust the analysis given what
was supplied, and express it as a 0-100 confidence score (High 75+, Medium 50 to
74, Low below 50). Base it on coverage of the high-value inputs and whether margin
was supplied or assumed. Then list the specific inputs that would raise it most,
each with a rough lift and a one-line reason. This is the `confidence` block in
the report. A small, honest data set should produce a strong health analysis with
a low confidence score, not a falsely certain one.

### 7. Assemble the report data

Build a single JSON object matching `references/report-data-schema.md` (the same
shape the HTML template renders). Populate `meta`, `health`, `confidence`,
`categories`, `kpis` (with a `status` of good, warning, or bad versus benchmark),
`findings` (severity, impact, action), `quick_wins`, `harvest` (promote and
negate rows from the Search Term report), `asin_table`, `funnel`, `ad_types`,
`action_plan`, `data_provided`, and `data_missing`. Write it to
`report-data.json` in the working directory. Every finding needs a concrete
action and, where possible, a dollar impact. A finding with no action is noise.

Write the report prose like a human, not a bot. The summary, findings, and
funnel notes are read by a person, so keep them plain and direct. No em dashes,
no emoji, straight quotes, plain verbs, and no filler. Short sentences beat long
ones. See `references/report-data-schema.md` for the small style checklist.

### 8. Generate the HTML report

Run the bundled script (it is deterministic, so do not hand-edit the template):

```bash
python scripts/build_report.py --data report-data.json --out AMAZON-ADS-REPORT.html
```

It injects your JSON into `assets/report-template.html` and writes a finished,
offline-safe HTML file. Use `--validate` first to check the JSON shape. If Python
is unavailable, copy `assets/report-template.html` and replace the object between
the `REPORT_DATA_START` and `REPORT_DATA_END` markers with your JSON.

### 9. Present

Tell the user the path to `AMAZON-ADS-REPORT.html`. Give a three or four sentence
spoken summary (score, the one biggest lever, the top quick win, and the
confidence level). List what extra data would raise confidence. Offer the obvious
next step, for example "want the negative-keyword list as a ready-to-upload bulk
file?".

## Reference files

Load these as needed. Do not read them all up front.

- `references/data-collection-guide.md`: what to upload, where every report lives,
  click-by-click export steps, and the bonus third-party inputs that raise
  confidence. Read at step 1, especially for non-expert users.
- `references/metrics-glossary.md`: every metric with its definition, formula,
  healthy and warning bands, and how to read it. Read at step 3.
- `references/benchmarks.md`: category and ad-type benchmarks and goal-based target
  ranges. Read at steps 3 and 4.
- `references/analysis-playbook.md`: the checks, thresholds, funnel logic, scoring
  rubric, and practitioner heuristics. Read at steps 4 and 5.
- `references/whats-new-2026.md`: current Amazon Ads formats and features so the
  analysis reflects 2026, not 2022. Skim when relevant.
- `references/report-data-schema.md`: the exact JSON shape and the report-copy
  style checklist for steps 6 and 7.

## Output contract

- `AMAZON-ADS-REPORT.html`: the deliverable, self-contained and ready to print or
  email.
- `report-data.json`: the structured analysis behind it, reusable and diff-able.

## Guardrails

- Derive targets from margin, not habit. "30% ACOS" means nothing without the
  seller's contribution margin. State assumptions when margin is unknown.
- Read metrics in the funnel, never alone. A 50% ACOS on a brand-defense campaign
  and on a cold prospecting campaign mean opposite things.
- Do not judge too early. Flag keywords or campaigns with too few clicks
  (roughly 2 divided by the conversion rate, and at least one week of data) as
  "insufficient data", not as winners or losers.
- Separate ad problems from listing problems before recommending bid changes.
  More budget cannot fix a listing that does not convert.
- Never fabricate numbers. Analyze only what was provided, and mark gaps openly
  through the confidence score.
- This is analysis guidance, not financial advice. Benchmarks are directional.
