"""
Utility script for the `subscription-churn-lifecycle` skill.

Generates a simple 4–8 week lifecycle execution plan focused on churn prevention
and retention, based on high-level focus areas (e.g., onboarding, usage
education, pre-renewal reminders, win-back).

This is intentionally lightweight: the skill or the user should adjust the
generated plan to fit their actual team capacity and tools.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import List, Dict, Any


@dataclass
class LifecycleWeek:
    week: int
    theme: str
    goals: List[str]
    tasks: List[str]


def generate_lifecycle_plan(
    focus_areas: List[str] | None = None,
    weeks: int = 6,
) -> List[LifecycleWeek]:
    """
    Generate a lifecycle execution plan.

    :param focus_areas: Optional list of high-level focus areas
                        (e.g., ["Onboarding", "预续费提醒", "挽回与回流"]).
                        If omitted, a default sequence will be used.
    :param weeks: Number of weeks to plan for (4–8 is recommended).
    """
    if weeks <= 0:
        raise ValueError("weeks must be positive")

    default_focus = [
        "订阅模型与数据诊断",
        "Onboarding 与首期体验优化",
        "使用场景教育与习惯养成",
        "预续费提醒与价值重申",
        "取消路径与原因收集优化",
        "挽回与回流实验",
    ]

    areas = focus_areas or default_focus

    def default_goals_for_area(area: str) -> List[str]:
        return [
            f"明确本周在「{area}」上的 1–2 个可量化目标",
            f"上线至少 1 个与「{area}」相关的改动或实验",
        ]

    def default_tasks_for_area(area: str) -> List[str]:
        return [
            f"梳理与「{area}」相关的现有触点/文案/配置",
            f"设计并评审 1–2 个改动方案（轻量为先）",
            f"在工具中配置并上线改动，记录观察指标与时间窗口",
        ]

    plan: List[LifecycleWeek] = []

    for i in range(weeks):
        area_index = min(i, len(areas) - 1)
        area = areas[area_index]
        plan.append(
            LifecycleWeek(
                week=i + 1,
                theme=area,
                goals=default_goals_for_area(area),
                tasks=default_tasks_for_area(area),
            )
        )

    return plan


def plan_to_dict(plan: List[LifecycleWeek]) -> List[Dict[str, Any]]:
    """Convert plan to a list of serializable dicts."""
    return [asdict(item) for item in plan]


def print_plan(plan: List[LifecycleWeek]) -> None:
    """Pretty-print the plan in a CLI-friendly format."""
    for item in plan:
        print(f"第 {item.week} 周主题：{item.theme}")
        print("  目标：")
        for g in item.goals:
            print(f"    - {g}")
        print("  关键任务：")
        for t in item.tasks:
            print(f"    - {t}")
        print()


if __name__ == "__main__":
    plan = generate_lifecycle_plan()
    print_plan(plan)

