#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
generate_content.py

Works with the high-repeat-small-goods-ops skill to generate blank ops templates
for local editing and reuse.

Usage examples:
  python scripts/generate_content.py --type weekly_plan > weekly_plan.md
  python scripts/generate_content.py --type campaign > campaign.md
  python scripts/generate_content.py --type repurchase_14d > repurchase_14d.md
  python scripts/generate_content.py --type customer_sop > customer_sop.md
  python scripts/generate_content.py --type review_report > review_report.md

Extracts the matching section from ../references/templates.md and outputs Markdown.
"""

import argparse
import pathlib
import sys
from typing import Optional


ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE_FILE = ROOT / "references" / "templates.md"


SECTION_MAP = {
    "weekly_plan": "## 1) Weekly ops plan (7-day schedule)",
    "campaign": "## 2) One-page campaign brief (promo/new/clearance/member day)",
    "repurchase_14d": "## 3) 14-day repeat rhythm (post-delivery touchpoints)",
    "customer_sop": "## 5) CS SOP (high-repeat small goods, general)",
    "review_report": "## 6) Weekly review table (experiment-driven)",
}


def extract_section(text: str, heading: str) -> Optional[str]:
    """Extract section starting with heading until the next ## section."""
    lines = text.splitlines()
    start_idx = None
    for i, line in enumerate(lines):
        if line.strip() == heading.strip():
            start_idx = i
            break
    if start_idx is None:
        return None

    end_idx = len(lines)
    for j in range(start_idx + 1, len(lines)):
        if lines[j].startswith("## "):
            end_idx = j
            break

    section_lines = lines[start_idx:end_idx]
    return "\n".join(section_lines).strip() + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Extract a blank ops template of the given type from templates.md."
    )
    parser.add_argument(
        "--type",
        required=True,
        choices=sorted(SECTION_MAP.keys()),
        help="Template type to generate",
    )
    args = parser.parse_args(argv)

    if not TEMPLATE_FILE.exists():
        print(f"Template file not found: {TEMPLATE_FILE}", file=sys.stderr)
        return 1

    content = TEMPLATE_FILE.read_text(encoding="utf-8")
    heading = SECTION_MAP[args.type]
    section = extract_section(content, heading)
    if section is None:
        print(f"Section not found in template file: {heading}", file=sys.stderr)
        return 1

    sys.stdout.write(section)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
