"""
Helper for the `high-ticket-trust-conversion` skill.

Provides a structured template for high-ticket trust assets so that different
agents or runs can refer to the same categories and keys when generating
checklists or tables.

Typical usage:

    from trust_assets_template import TRUST_ASSET_CATEGORIES, as_markdown_table

    print(as_markdown_table())
"""

from __future__ import annotations

from typing import Dict, List


TRUST_ASSET_CATEGORIES: Dict[str, List[str]] = {
    "品牌与资质": [
        "品牌历史与故事",
        "资质证书/检测报告",
        "线下门店/工厂/展厅",
        "奖项与媒体报道",
    ],
    "专业与方案能力": [
        "核心团队与背景",
        "服务/施工/教学流程",
        "方法论与标准化体系",
        "典型成功案例与数据结果",
    ],
    "交付与风险控制": [
        "生产/施工/服务节点与质检",
        "延期/事故处理流程",
        "售后服务与质保条款",
        "用户不满意时的兜底方案",
    ],
    "价格与价值逻辑": [
        "定价依据与构成",
        "与低价替代方案的对比",
        "长期使用/持有成本分析",
        "额外增值服务",
    ],
    "社会证明与口碑": [
        "真实评价与回访记录",
        "客户故事与访谈",
        "视频/图片见证素材",
        "复购与转介绍数据",
    ],
}


def as_markdown_table() -> str:
    """
    Render the trust asset categories as a markdown table skeleton that the
    skill can embed in its outputs and then fill with concrete items.
    """
    lines: List[str] = []
    lines.append("| 资产大类 | 要素 | 当前是否具备 | 补充计划（30 天内） | 备注 |")
    lines.append("| --- | --- | --- | --- | --- |")

    for category, items in TRUST_ASSET_CATEGORIES.items():
        for item in items:
            lines.append(f"| {category} | {item} |  |  |  |")

    return "\n".join(lines)


if __name__ == "__main__":
    print(as_markdown_table())

