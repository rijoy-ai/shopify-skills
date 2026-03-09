#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
generate_flow_spec.py

配合 fitness-plan-flows skill，生成空白流规格模板，便于本地填写与复用。

用法示例：
  python scripts/generate_flow_spec.py > flow_spec.md
  python scripts/generate_flow_spec.py --flow "购后入门计划" >> my_flows.md
"""

import argparse
import sys

FLOW_SPEC_TEMPLATE = """## 训练计划配套流总览 (Flow map)
- （各流名称、目标、与「计划」的关系：交付/促复购/拉新）

## 流规格 (Flow specs)

### Flow: {flow_name}
- Goal:
- Trigger:
- Exit rules:
- Segments（若分层）:
- Timeline (T+ 或自然日):
- 计划类型与内容要点（如：入门 7 天计划 / 4 周进阶 / 周计划）:
- Messages (Email/SMS/其他):
  - Subject / Hook:
  - Body 结构（含计划 CTA、链接/附件说明）:
  - CTA:
- KPIs:
- 实现映射（Klaviyo/Shopify Email/其他）:

## 计划内容清单（本套流涉及的计划）
- 计划 1：名称、适用产品、时长、交付节点
- 计划 2：…
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="生成空白流规格模板")
    parser.add_argument(
        "--flow",
        default="<名称>",
        help="当前 Flow 名称占位，默认 <名称>",
    )
    args = parser.parse_args()
    out = FLOW_SPEC_TEMPLATE.format(flow_name=args.flow)
    sys.stdout.write(out)


if __name__ == "__main__":
    main()
