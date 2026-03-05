"""
Utility script for the `high-ticket-trust-conversion` skill.

Given a list of focus areas, this script generates a simple 2–4 week execution
plan with weekly themes and tasks. It is intentionally lightweight and designed
for manual tweaking by the user.

Usage (example):

    from generate_execution_plan import generate_plan, print_plan

    focus_areas = [
        "补齐信任资产（案例、资质、客户故事）",
        "优化落地页/PDP 的首屏与信任模块",
        "梳理销售/客服首咨与报价话术",
        "搭建 14–30 天线索培育节奏"
    ]

    plan = generate_plan(focus_areas, weeks=4)
    print_plan(plan)
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import List, Dict, Any


@dataclass
class WeeklyTask:
    week: int
    theme: str
    tasks: List[str]


def generate_plan(focus_areas: List[str], weeks: int = 4) -> List[WeeklyTask]:
    """
    Generate a simple weekly execution plan from high-level focus areas.

    - Distributes focus areas roughly across the given number of weeks.
    - For each focus area, creates 2–3 concrete tasks as suggestions.
    """
    if weeks <= 0:
        raise ValueError("weeks must be positive")

    # Basic templates for turning a focus area into concrete tasks.
    def expand_focus_to_tasks(area: str) -> List[str]:
        return [
            f"盘点/整理：{area}",
            f"输出初版方案或文案：{area}",
            f"内部评审并做 1 轮迭代：{area}",
        ]

    weekly_plan: List[WeeklyTask] = []
    for i in range(weeks):
        if focus_areas:
            area_index = min(i, len(focus_areas) - 1)
            theme = focus_areas[area_index]
            tasks = expand_focus_to_tasks(theme)
        else:
            theme = "本周根据实际情况自定义重点"
            tasks = ["明确 1 个本周最重要的信任/转化目标", "拆解 3–5 个可执行动作并安排日程"]

        weekly_plan.append(
            WeeklyTask(
                week=i + 1,
                theme=theme,
                tasks=tasks,
            )
        )

    return weekly_plan


def plan_to_dict(plan: List[WeeklyTask]) -> List[Dict[str, Any]]:
    """Convert a plan to a list of serializable dicts."""
    return [asdict(item) for item in plan]


def print_plan(plan: List[WeeklyTask]) -> None:
    """Pretty-print the plan in a CLI-friendly format."""
    for item in plan:
        print(f"第 {item.week} 周：{item.theme}")
        for idx, task in enumerate(item.tasks, start=1):
            print(f"  {idx}. {task}")
        print()


if __name__ == "__main__":
    default_focus = [
        "补齐信任资产（案例、资质、客户故事）",
        "优化关键页面的首屏与信任模块",
        "优化咨询/销售话术与 SOP",
        "搭建 14–30 天线索培育节奏",
    ]
    plan = generate_plan(default_focus, weeks=4)
    print_plan(plan)

