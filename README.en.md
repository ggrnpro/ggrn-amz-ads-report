![Amazon Ads Analyzer: from raw Amazon reports to a 0 to 100 HTML health report](assets/banner.png)

# Amazon Ads Analyzer (ggrn-amz-ads-report)

[Русская версия](README.md).

Turn your Amazon advertising reports into one clean HTML health report. You
upload what you have (exported reports, or even a screenshot), and you get back a
single self-contained HTML page that scores the account out of 100, compares your
metrics to 2026 benchmarks, lists the issues in priority order, and hands you a
search-term harvest and negatives plan you can act on the same day.

It is built as a Claude skill (an `Agent Skill`, the `SKILL.md` format). It runs
locally, reads only the data you give it, and never logs into Amazon or changes
your campaigns. The report it produces makes no external network requests, so you
can email it to a client without anything phoning home.

**See a live demo report:** [open the rendered example](https://htmlpreview.github.io/?https://github.com/ggrnpro/ggrn-amz-ads-report/blob/main/examples/demo-report.html)
(or the raw file: [`examples/demo-report.html`](examples/demo-report.html)). It is a
single-product launch with anonymized sample data. A
[Russian version of the same report](https://htmlpreview.github.io/?https://github.com/ggrnpro/ggrn-amz-ads-report/blob/main/examples/demo-report.ru.html) is also available.

## What you get

- A 0-100 health score with a letter grade and a plain-language summary.
- A data-confidence score that tells you how much to trust the result, plus the
  exact files to add to raise it.
- KPI cards (ACOS, TACOS, ROAS, CTR, CVR, CPC, spend, sales) colored against the
  benchmark, not just printed.
- Prioritized findings, each with a quantified impact and a concrete action.
- Quick wins you can do in under fifteen minutes.
- A search-term harvest plan: which terms to promote to exact match, which to add
  as negatives, straight from your Search Term report.
- An ACOS-by-ASIN profitability table that marks the unprofitable SKUs.
- A funnel diagnosis that separates an ad problem from a listing problem, so you
  do not waste money raising bids on a listing that does not convert.
- A prioritized action plan with owners and timing.

The whole thing is one HTML file. Open it in any browser, print it to PDF, or
send it on.

## Who it is for

- Amazon sellers and brand owners who want a straight answer on whether their ads
  are working, without learning a new dashboard.
- Agencies and freelancers who want a fast, repeatable client-ready report.
- Anyone new to Amazon PPC who does not yet know which report to pull. The skill
  walks you through the exports step by step.

## How it works

1. You give it your data. Best is a Sponsored Products Search Term report plus
   Campaign and Targeting reports. A single Campaign Manager screenshot works too.
2. It computes every metric from the raw numbers, derives your break-even and
   target ACOS from your margin, and scores nine categories.
3. It writes `report-data.json` (the analysis) and builds
   `AMAZON-ADS-REPORT.html` (the deliverable).
4. It tells you the score, the single biggest lever, and which file to add next
   for a more accurate read.

It does not connect to Amazon, place bids, or post anything. Creating and editing
campaigns stays in your hands.

## What to upload

You do not need everything. Upload what you have and add more later. The report
states its own confidence and tells you which missing file would help most.

Most useful, in order:

1. Sponsored Products Search Term report (last 60 to 90 days). The single most
   important file.
2. Campaign, Advertised Product, Targeting, and Placement reports.
3. The Bulk Operations file (your whole account structure in one sheet).
4. Sponsored Brands and Sponsored Display reports, if you run them.
5. Business Reports and, if you are brand-registered, Brand Analytics Search Query
   Performance. These show whether a weak result is an ad problem or a listing
   problem.

Bonus inputs that sharpen the report (optional):

- A keyword export from Helium 10 (Cerebro, Magnet), Jungle Scout (Keyword
  Scout), or Data Dive, with search volume and competition.
- A product cost sheet (COGS, fees, sell price) so the target ACOS is exact
  instead of a category default.
- A competitor or listing screenshot, and your current inventory status.

The full click-by-click export guide, including where each report lives in the
Amazon Ads console and Seller Central, is in
[`references/data-collection-guide.md`](references/data-collection-guide.md).

## Install

One command, through the [skills.sh](https://skills.sh) installer. It detects your
agent and drops the skill in the right place:

```bash
npx skills add ggrnpro/ggrn-amz-ads-report
```

That covers Claude Code, Codex, Cursor, Windsurf, Gemini CLI, Goose, GitHub Copilot,
and the other agents skills.sh supports. To update later:

```bash
npx skills update
```

Then start your agent and say "analyze my Amazon ads" with your reports attached,
or call the skill by name.


### Manual install

If you would rather not use the installer, this is a plain Agent Skill: the folder
holding `SKILL.md` is the skill. Clone it into your tool's skills directory, for
example Claude Code:

```bash
git clone https://github.com/ggrnpro/ggrn-amz-ads-report.git ~/.claude/skills/amazon-ads-analyzer
```

```powershell
git clone https://github.com/ggrnpro/ggrn-amz-ads-report.git "$env:USERPROFILE\.claude\skills\amazon-ads-analyzer"
```

Other agents use their own skills folders (Codex `~/.codex/skills/`, Cursor
`~/.cursor/skills/`, Windsurf `~/.windsurf/skills/`, Gemini `~/.gemini/skills/`,
Goose `~/.config/goose/skills/`). Claude Desktop and claude.ai take the folder as
an uploaded skill.

## Requirements

- Python 3.10 or newer, for `scripts/build_report.py` (it ships with no
  third-party dependencies).
- For reading `.xlsx` exports, the analyzer uses a spreadsheet reader if one is
  available. CSV exports need nothing extra.

## Generate a report by hand

If you have the analysis JSON already, you can build the HTML directly:

```bash
python scripts/build_report.py --data report-data.json --out AMAZON-ADS-REPORT.html
# check the JSON shape first:
python scripts/build_report.py --data report-data.json --validate
```

See [`examples/demo-report-data.json`](examples/demo-report-data.json) and the
HTML it produces, [`examples/demo-report.html`](examples/demo-report.html). The
data shape is documented in
[`references/report-data-schema.md`](references/report-data-schema.md).

## What is inside

```
ggrn-amz-ads-report/
  SKILL.md                       the skill: workflow and rules
  assets/report-template.html    the HTML report template (renders from JSON)
  scripts/build_report.py        injects analysis JSON into the template
  references/
    data-collection-guide.md     what to upload, where, and how (newbie-first)
    metrics-glossary.md          every metric, formula, and how to read it
    benchmarks.md                2026 category and ad-type benchmarks
    analysis-playbook.md         the checks, scoring rubric, and practitioner rules
    whats-new-2026.md            current Amazon Ads features and renames
    report-data-schema.md        the JSON contract for the report
  examples/                      a demo report you can open
```

## Privacy

Everything runs on your machine through your agent tool. Your account data is not
uploaded anywhere by this skill. The HTML report is fully self-contained and
makes no network requests, so opening or sharing it does not leak data.

## Notes and limits

This is an analysis aid, not financial advice. Benchmarks are directional
averages from third-party datasets; your margin and stage decide the right
targets. The skill is not affiliated with, endorsed by, or sponsored by Amazon.
Amazon, Amazon Ads, and related marks belong to Amazon.com, Inc.

## License

MIT. See [LICENSE](LICENSE).

Built by Oleg Gagarin. Site: [ggrn.pro](https://ggrn.pro).
