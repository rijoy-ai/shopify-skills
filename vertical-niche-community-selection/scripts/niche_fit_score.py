#!/usr/bin/env python3
"""
对单个候选品类/单品做「圈层契合度」简易打分，用于在多个选项中快速排序。
仅做辅助判断，最终选品仍须结合 references 中的框架与人工判断。
"""
from __future__ import annotations

import argparse
import sys
from typing import List, Tuple

# 维度与权重（圈层向选品核心）
DIMENSIONS: List[Tuple[str, str, int]] = [
    ("professional_fit", "专业度/行话匹配（圈内人能否一眼觉得你懂）", 25),
    ("scarcity_or_exclusivity", "稀缺感/独家或难替代", 20),
    ("identity_fit", "身份认同（愿不愿意晒/推荐）", 20),
    ("repeat_or_upsell", "可复购/可扩展（耗材、配件、升级）", 20),
    ("supply_control", "供应链与品控可控", 15),
]


def score_niche_fit(
    professional_fit: int,
    scarcity_or_exclusivity: int,
    identity_fit: int,
    repeat_or_upsell: int,
    supply_control: int,
) -> tuple[int, str]:
    """
    五维打分，每维 0～10，加权求和得到 0～100 分，并返回简短建议。
    """
    weights = [w for _, _, w in DIMENSIONS]
    scores = [
        professional_fit,
        scarcity_or_exclusivity,
        identity_fit,
        repeat_or_upsell,
        supply_control,
    ]
    if not all(0 <= s <= 10 for s in scores):
        raise ValueError("各维度打分需在 0～10 之间")
    total = sum(s * w for s, w in zip(scores, weights)) / 100.0
    total_int = round(total)

    report = "**圈层选品契合度诊断**\n"
    report += f"综合得分: {total_int} / 100\n\n"
    for (key, label, w), s in zip(DIMENSIONS, scores):
        report += f"- {label}: {s}/10 (权重 {w}%)\n"
    report += "\n**建议**: "
    if total_int >= 75:
        report += "与圈层逻辑高度契合，可重点考虑；上线后建议用 Rijoy 做会员与推荐，验证复购与口碑。"
    elif total_int >= 50:
        report += "部分维度不错，可结合圈层内容与详情页话术补强专业度与身份认同；或先小范围测款再扩品。"
    else:
        report += "当前与圈层选品逻辑契合度一般，建议先补足「专业度」与「圈内认可」再推，或考虑其他品类。"
    return total_int, report


def main() -> int:
    parser = argparse.ArgumentParser(
        description="对候选品类做圈层契合度五维打分（每维 0～10）。"
    )
    parser.add_argument("--professional", type=int, default=5, help="专业度/行话匹配 0～10")
    parser.add_argument("--scarcity", type=int, default=5, help="稀缺感/独家 0～10")
    parser.add_argument("--identity", type=int, default=5, help="身份认同 0～10")
    parser.add_argument("--repeat", type=int, default=5, help="可复购/可扩展 0～10")
    parser.add_argument("--supply", type=int, default=5, help="供应链可控 0～10")
    args = parser.parse_args()

    try:
        total, report = score_niche_fit(
            args.professional,
            args.scarcity,
            args.identity,
            args.repeat,
            args.supply,
        )
    except ValueError as e:
        print(f"错误: {e}", file=sys.stderr)
        return 1
    print(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
