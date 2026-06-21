#!/usr/bin/env python3
"""
build_report.py: inject an analysis JSON into the HTML report template.

The template (assets/report-template.html) renders entirely from a single
`REPORT_DATA` object delimited by:
    /* === REPORT_DATA_START === */ ... /* === REPORT_DATA_END === */

This script swaps that placeholder object for your real analysis and writes a
finished, self-contained HTML file (no external requests, so it is safe to email).

Usage
-----
    python build_report.py --data report-data.json --out AMAZON-ADS-REPORT.html
    # template path is auto-detected (../assets/report-template.html); override with --template

The JSON must match the shape documented in references/report-data-schema.md.
Run with --validate to check the JSON shape without writing output.
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

START = "/* === REPORT_DATA_START ==="
END = "/* === REPORT_DATA_END === */"

REQUIRED_TOP = ["meta", "health"]
KNOWN_TOP = {
    "meta", "health", "confidence", "how_to_read", "how_to_read_lede",
    "categories", "kpis", "findings", "quick_wins", "harvest", "asin_table",
    "funnel", "ad_types", "action_plan", "data_provided", "data_missing",
    "glossary",
}
VALID_STATUS = {"good", "warning", "bad", "info"}
VALID_SEVERITY = {"critical", "high", "medium", "low"}


def find_template(explicit: str | None) -> Path:
    if explicit:
        return Path(explicit)
    here = Path(__file__).resolve().parent
    for cand in (here.parent / "assets" / "report-template.html",
                 here / "report-template.html"):
        if cand.exists():
            return cand
    raise SystemExit("Template not found. Pass --template <path>.")


def validate(data: dict) -> list[str]:
    """Return a list of human-readable warnings (empty == clean)."""
    warns: list[str] = []
    for k in REQUIRED_TOP:
        if k not in data:
            warns.append(f"missing required top-level key: '{k}'")
    for k in data:
        if k not in KNOWN_TOP:
            warns.append(f"unknown top-level key '{k}' (will be ignored by template)")

    h = data.get("health", {})
    if isinstance(h, dict):
        s = h.get("score")
        if not isinstance(s, (int, float)) or not (0 <= s <= 100):
            warns.append("health.score should be a number from 0 to 100")
        if h.get("grade") not in (None, "A", "B", "C", "D", "F"):
            warns.append("health.grade should be one of A/B/C/D/F")

    for i, k in enumerate(data.get("kpis", []) or []):
        if k.get("status") not in VALID_STATUS:
            warns.append(f"kpis[{i}].status '{k.get('status')}' not in {sorted(VALID_STATUS)}")
    for i, f in enumerate(data.get("findings", []) or []):
        if f.get("severity") not in VALID_SEVERITY:
            warns.append(f"findings[{i}].severity '{f.get('severity')}' not in {sorted(VALID_SEVERITY)}")

    cf = data.get("confidence")
    if isinstance(cf, dict):
        cs = cf.get("score")
        if not isinstance(cs, (int, float)) or not (0 <= cs <= 100):
            warns.append("confidence.score should be a number from 0 to 100")

    cats = data.get("categories", []) or []
    if cats:
        total_w = sum((c.get("weight") or 0) for c in cats)
        if abs(total_w - 100) > 0.5:
            warns.append(f"category weights sum to {total_w}, not 100")
    return warns


def build(template_path: Path, data: dict) -> str:
    html = template_path.read_text(encoding="utf-8")
    s = html.find(START)
    e = html.find(END)
    if s == -1 or e == -1 or e < s:
        raise SystemExit("Could not locate REPORT_DATA markers in template.")
    # keep the START comment line, replace the JS object + sample comment body
    head = html[:s] + START + " injected by build_report.py */\n"
    payload = "const REPORT_DATA = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
    tail = html[e:]
    return head + payload + tail


def main() -> int:
    ap = argparse.ArgumentParser(description="Inject analysis JSON into the Amazon Ads HTML report template.")
    ap.add_argument("--data", required=True, help="Path to the analysis JSON file.")
    ap.add_argument("--out", default="AMAZON-ADS-REPORT.html", help="Output HTML path.")
    ap.add_argument("--template", help="Override template path.")
    ap.add_argument("--validate", action="store_true", help="Only validate the JSON; do not write output.")
    a = ap.parse_args()

    try:
        data = json.loads(Path(a.data).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as ex:
        print(f"ERROR reading/parsing --data: {ex}", file=sys.stderr)
        return 2

    warns = validate(data)
    for w in warns:
        print(f"  warn: {w}", file=sys.stderr)

    if a.validate:
        print("VALID (with warnings above)" if warns else "VALID", file=sys.stderr)
        return 0

    out = Path(a.out)
    out.write_text(build(find_template(a.template), data), encoding="utf-8")
    print(f"Wrote {out}  ({out.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
