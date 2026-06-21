# Report data schema

The HTML report renders entirely from one JSON object (`report-data.json`).
`scripts/build_report.py` injects it into `assets/report-template.html` between
the `REPORT_DATA_START` and `REPORT_DATA_END` markers. Any section you omit is
hidden automatically, so provide only what the data supports. Never invent rows
to fill a section.

Status and severity vocabularies (the template keys colors off these, so use them
exactly):

- KPI `status`: `good`, `warning`, `bad`, `info`
- finding `severity`: `critical`, `high`, `medium`, `low`
- ASIN `verdict`: `good`, `warn`, `bad`
- health `grade`: `A`, `B`, `C`, `D`, `F`

## Top-level shape

```jsonc
{
  "meta": {                       // REQUIRED
    "lang": "en",                 // "en" (default) or "ru". Switches the report's fixed UI strings
                                  // (titles, help lines, table headers, legends). Write the data
                                  // strings (summary, findings, hints, glossary) in that language too.
    "brand": "Acme Supplements",
    "marketplace": "Amazon.com (US)",
    "account_type": "Seller, Brand Registered",   // or "Vendor", "Seller (not brand-registered)"
    "category": "Health & Household, Supplements",
    "date_range": "2026-03-23 to 2026-06-21 (90 days)",
    "generated": "2026-06-21",
    "analyst_note": "Margin not supplied; target ACOS uses the category default (28%). Confirm."
  },

  "health": {                     // REQUIRED
    "score": 71,                  // 0-100
    "grade": "C",                 // A/B/C/D/F
    "summary": "2 to 4 sentences: state of the account, the single biggest lever, the headline number."
  },

  "confidence": {                 // how much to trust the analysis given the data supplied
    "score": 62,                  // 0-100 data-completeness/accuracy
    "level": "Medium",            // High (75+), Medium (50 to 74), Low (below 50)
    "basis": "One line on what the score rests on (inputs present, assumptions made).",
    "boosters": [                 // what to add to raise accuracy, biggest lift first
      { "item": "Brand Analytics, Search Query Performance", "adds": "+15%",
        "why": "What this unlocks in the analysis." }
    ]
  },

  "how_to_read_lede": "One plain sentence framing the report for a beginner.",
  "how_to_read": [               // a short numbered intro card. Keep it 3 to 4 items, plain language.
    "Start at the top. The score and summary tell you where you stand.",
    "The <b>Action plan</b> near the bottom is your ordered to-do list."
  ],

  "categories": [                 // category scores; weights should sum to about 100 across those assessed
    { "name": "Search-Term Harvesting & Negatives", "weight": 25, "score": 55 }
  ],

  "kpis": [                       // metric cards vs benchmark
    { "label": "ACOS", "value": "31%", "benchmark": "break-even 35%, target 28% or lower",
      "status": "warning", "hint": "Optional one-liner shown under the card.",
      // Optional gauge: bar = where you are (0-100 position), mark = the target line (0-100),
      // good = which side of the line is healthy ("left" for lower-is-better like ACOS/CPC,
      // "right" for higher-is-better like ROAS/CTR/CVR), mark_label = the line's name on the legend.
      "bar": 62, "mark": 70, "good": "left", "mark_label": "break-even" }
  ],

  "findings": [
    { "id": "H-01", "severity": "critical", "area": "Wasted spend", "eta_days": 1,
      "title": "Short, specific headline with the number in it",
      "impact": "Quantified consequence (recoverable $, % of spend, SKUs affected)",
      "action": "The concrete fix to make" }
  ],

  "quick_wins": [                 // strings: high-impact, under 15 min each, include the $ where known
    "Add 41 zero-order high-spend terms as negatives (about 10 min, recovers about $1,300/mo)"
  ],

  "harvest": {                    // straight from the Search Term report
    "promote": [ { "term": "magnesium glycinate 400mg", "campaign": "SP-Auto-Supps",
                   "clicks": 212, "orders": 31, "acos": "19%", "action": "To Manual Exact" } ],
    "negate":  [ { "term": "magnesium oil spray", "campaign": "SP-Auto-Supps",
                   "spend": "$214", "clicks": 191, "orders": 0, "reason": "0 orders / 191 clicks" } ]
  },

  "asin_table": [
    { "asin": "B0ASIN0001", "title": "Magnesium Glycinate 120ct",
      "spend": "$9,420", "sales": "$41,300", "acos": "22.8%", "tacos": "7.1%",
      "target_acos": "28%", "verdict": "good" }   // good | warn | bad
  ],

  "funnel": {
    "diagnosis": "Plain language: is this an ad problem or a listing problem, and why.",
    // stages drive the centered funnel chart. Order them top (widest) to bottom.
    // Widths use a log scale so even a tiny bottom stage stays a readable band, and
    // the step % between stages is computed for you. value is a raw number.
    "stages": [ { "label": "Impressions (wk)", "value": 14356 }, { "label": "Clicks", "value": 72 },
                { "label": "Cart adds", "value": 21 }, { "label": "Purchases", "value": 4 } ],
    "rows": [ { "metric": "CTR", "value": "0.38%", "benchmark": "about 0.40%",
                "read": "On benchmark, image and relevance are fine." } ]
  },

  "ad_types": [
    { "type": "Sponsored Products", "score": 72, "notes": ["83% of spend", "Harvest cadence is the gap"] },
    { "type": "Sponsored TV / DSP", "score": null, "notes": ["Not running. Consider once spend is above $15k/mo"] }
  ],

  "action_plan": [
    { "priority": 1, "action": "Negative sweep + harvest", "owner": "PPC",
      "eta": "This week", "impact": "Recover about $1,300/mo, ACOS down about 4pp" }
  ],

  "glossary": [                   // plain-English definitions for the terms used. Helps non-experts.
    { "term": "ACOS", "plain": "Ad spend divided by ad sales. Compare it to your margin, not the average." }
  ],

  "data_provided": ["SP Search Term Report (90d)", "SP Campaign Report (90d)"],
  "data_missing":  ["Placement Report", "Brand Analytics, Search Query Performance"]
}
```

The `how_to_read` intro and `glossary` exist to make the report usable by a
total beginner. Always include them, and write every `findings[].action` and
`action_plan[].action` as a concrete do-this step, not an observation. Each
section in the report also shows a fixed plain-language help line under its
title (built into the template), so the data you supply only needs to be
specific and honest, not explanatory.

## Rules

- Numbers are pre-formatted strings (`"31%"`, `"$9,420"`) except where the
  template does math: `health.score`, `confidence.score`,
  `categories[].score/weight` are numbers, `kpis` values are display strings,
  `harvest[].clicks/orders` are numbers, `ad_types[].score` is a number or `null`
  (renders "n/a"), and `action_plan[].priority` is a number (1 is highest, and it
  drives the colored left border).
- Keep `findings[].title` specific and quantified. "Short headline with the number
  in it" beats "Improve negative keywords".
- `kpis[].status` should reflect the benchmark comparison, not the raw value. A
  50% ACOS is `good` for brand-defense and `bad` for prospecting.
- Validate before building:
  `python scripts/build_report.py --data report-data.json --validate`.

## Report-copy style checklist

The report is read by a person, so the prose in `health.summary`,
`findings`, `funnel.diagnosis`, and `quick_wins` should read like a human wrote
it. Before you build:

- No em dashes or en dashes. Use a period, comma, colon, or parentheses.
- No emoji. The template supplies its own plain icons.
- Straight quotes only.
- Plain verbs ("is", "has", "drives"), not "serves as" or "boasts".
- Cut filler ("it is important to note that", "in order to"). Say the thing.
- Vary sentence length. A short sentence lands harder than a third clause.
- Lead with the number and the action. The reader wants the lever, not a preamble.
