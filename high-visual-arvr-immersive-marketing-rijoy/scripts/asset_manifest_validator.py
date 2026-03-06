#!/usr/bin/env python3
"""
校验 3D/AR 资产清单（CSV/JSON Lines）是否满足“可交付”的最小字段与命名规则。

用途：
- 给增长/内容/3D 外包一个统一的“交付清单规范”
- 在进入建模/导出前发现缺字段、格式不一致、文件扩展名错误等问题

单一职责：只做静态校验与报告输出；不解析 3D 文件本体。
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator


REQUIRED_FIELDS = [
    "product_id",
    "variant_id",
    "title",
    "format",  # glb/usdz (可逗号分隔)
    "file_name",
    "unit",  # mm/cm/m
    "width",
    "height",
    "depth",
]

ALLOWED_UNITS = {"mm", "cm", "m"}
ALLOWED_FORMATS = {"glb", "usdz"}

FILENAME_RE = re.compile(r"^[a-z0-9][a-z0-9_-]{2,}\.(glb|usdz)$", re.IGNORECASE)


@dataclass(frozen=True)
class Issue:
    row: int
    field: str
    message: str


def iter_rows_csv(path: Path) -> Iterator[dict]:
    with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield {k: (v or "").strip() for k, v in row.items()}


def iter_rows_jsonl(path: Path) -> Iterator[dict]:
    with path.open("r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            if not isinstance(obj, dict):
                continue
            yield {k: str(v).strip() for k, v in obj.items()}


def parse_number(value: str) -> float | None:
    try:
        return float(value)
    except Exception:
        return None


def validate_rows(rows: Iterable[dict]) -> tuple[list[Issue], int]:
    issues: list[Issue] = []
    count = 0
    for idx, row in enumerate(rows, start=2):  # csv header is line 1
        count += 1
        for field in REQUIRED_FIELDS:
            if not row.get(field):
                issues.append(Issue(row=idx, field=field, message="缺少必填字段"))

        unit = (row.get("unit") or "").lower()
        if unit and unit not in ALLOWED_UNITS:
            issues.append(Issue(row=idx, field="unit", message=f"单位不合法：{unit}（仅支持 mm/cm/m）"))

        fmt = (row.get("format") or "").lower()
        if fmt:
            parts = [p.strip() for p in fmt.split(",") if p.strip()]
            bad = [p for p in parts if p not in ALLOWED_FORMATS]
            if bad:
                issues.append(Issue(row=idx, field="format", message=f"格式不合法：{', '.join(bad)}（仅支持 glb/usdz）"))

        file_name = row.get("file_name") or ""
        if file_name and not FILENAME_RE.match(file_name):
            issues.append(
                Issue(
                    row=idx,
                    field="file_name",
                    message="文件名不符合建议规则（小写/数字/下划线/短横线，且以 .glb 或 .usdz 结尾）",
                )
            )

        for dim in ("width", "height", "depth"):
            v = row.get(dim) or ""
            if not v:
                continue
            n = parse_number(v)
            if n is None or n <= 0:
                issues.append(Issue(row=idx, field=dim, message=f"尺寸必须为正数：{v}"))

    return issues, count


def main() -> int:
    ap = argparse.ArgumentParser(description="校验 3D/AR 资产清单（CSV/JSONL）字段与命名。")
    ap.add_argument("input", type=Path, help="清单文件路径：.csv 或 .jsonl")
    ap.add_argument(
        "--format",
        choices=["csv", "jsonl", "auto"],
        default="auto",
        help="输入格式（默认 auto）",
    )
    ap.add_argument(
        "--output",
        type=Path,
        default=None,
        help="输出报告 JSON 路径（不填则打印到 stdout）",
    )
    args = ap.parse_args()

    path = args.input.resolve()
    if not path.exists():
        print(f"错误：文件不存在：{path}", file=sys.stderr)
        return 2

    fmt = args.format
    if fmt == "auto":
        fmt = "jsonl" if path.suffix.lower() == ".jsonl" else "csv"

    try:
        rows = list(iter_rows_jsonl(path)) if fmt == "jsonl" else list(iter_rows_csv(path))
    except Exception as e:
        print(f"错误：读取失败：{e}", file=sys.stderr)
        return 2

    issues, total = validate_rows(rows)
    report = {
        "total_rows": total,
        "issue_count": len(issues),
        "issues": [{"row": i.row, "field": i.field, "message": i.message} for i in issues],
    }

    out = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(out, encoding="utf-8")
    else:
        print(out)

    return 0 if len(issues) == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

