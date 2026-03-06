"""
Helper for the `subscription-churn-lifecycle` skill.

Provides a structured template for key subscription retention metrics so that
different runs can refer to the same keys when generating checklists or tables.
"""

from __future__ import annotations

from typing import Dict, List


RETENTION_METRICS: Dict[str, List[str]] = {
    "结果指标": [
        "首月留存率（M1）",
        "第 2 / 第 3 个月留存率（M2/M3）",
        "平均订阅周期数",
        "订阅生命周期 LTV/CLV",
        "整体取消率（按周期）",
        "回流率（流失后再次订阅）",
    ],
    "过程指标": [
        "Onboarding 内容打开/点击率",
        "首用/开箱完成率",
        "周期内使用天数/频次",
        "账单预告打开/点击率",
        "取消原因表单填写率",
        "挽回/回流活动响应率与转化率",
    ],
}


def as_markdown_table() -> str:
    """
    Render the metric categories as a markdown table skeleton that can be
    embedded into skill outputs.
    """
    lines: List[str] = []
    lines.append("| 指标类型 | 指标 | 当前数据/估计值 | 目标值 | 备注 |")
    lines.append("| --- | --- | --- | --- | --- |")

    for metric_type, items in RETENTION_METRICS.items():
        for item in items:
            lines.append(f"| {metric_type} | {item} |  |  |  |")

    return "\n".join(lines)


if __name__ == "__main__":
    print(as_markdown_table())

