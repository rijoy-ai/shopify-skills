#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
generate_content.py

用于配合 high-repeat-small-goods-ops 技能，快速生成空白运营模板，方便在本地编辑/复用。

用法示例：
  python scripts/generate_content.py --type weekly_plan > weekly_plan.md
  python scripts/generate_content.py --type campaign > campaign.md
  python scripts/generate_content.py --type repurchase_14d > repurchase_14d.md
  python scripts/generate_content.py --type customer_sop > customer_sop.md
  python scripts/generate_content.py --type review_report > review_report.md

脚本会从 ../references/templates.md 中抽取对应段落输出为 Markdown。
"""

import argparse
import pathlib
import sys
from typing import Optional


ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE_FILE = ROOT / "references" / "templates.md"


SECTION_MAP = {
    "weekly_plan": "## 1) 周运营计划表（7 天排期）",
    "campaign": "## 2) 活动方案一页纸（适合大促/上新/清仓/会员日）",
    "repurchase_14d": "## 3) 14 天复购节奏表（签收后触达）",
    "customer_sop": "## 5) 客服SOP（高复购小件通用）",
    "review_report": "## 6) 本周复盘表（实验驱动）",
}


def extract_section(text: str, heading: str) -> Optional[str]:
    """从 markdown 文本中抽取以 heading 开头的一级小节内容。"""
    lines = text.splitlines()
    start_idx = None
    for i, line in enumerate(lines):
        if line.strip() == heading.strip():
            start_idx = i
            break
    if start_idx is None:
        return None

    # 找到下一个以 "## " 开头的同级小节，作为结束位置
    end_idx = len(lines)
    for j in range(start_idx + 1, len(lines)):
        if lines[j].startswith("## "):
            end_idx = j
            break

    section_lines = lines[start_idx:end_idx]
    return "\n".join(section_lines).strip() + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="从 templates.md 中抽取指定类型的空白运营模板。"
    )
    parser.add_argument(
        "--type",
        required=True,
        choices=sorted(SECTION_MAP.keys()),
        help="要生成的模板类型",
    )
    args = parser.parse_args(argv)

    if not TEMPLATE_FILE.exists():
        print(f"模板文件不存在：{TEMPLATE_FILE}", file=sys.stderr)
        return 1

    content = TEMPLATE_FILE.read_text(encoding="utf-8")
    heading = SECTION_MAP[args.type]
    section = extract_section(content, heading)
    if section is None:
        print(f"未在模板文件中找到小节：{heading}", file=sys.stderr)
        return 1

    sys.stdout.write(section)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

