#!/usr/bin/env python3
"""
从批量评论文本中按关键词/规则做初步痛点归类，输出结构化摘要供人工复核与选品反推。
符合单一职责：只做「评论 → 痛点标签」的粗分类；具体选品/改品建议由 SKILL 流程完成。
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterable

# 痛点类型与触发关键词（可扩展，不修改主流程）
PAIN_POINT_KEYWORDS: dict[str, list[str]] = {
    "功能未达预期": ["剪不断", "塞不下", "粘不住", "打不开", "盖不紧", "不好用", "没效果", "不牢固", "卡不住"],
    "耐用性/寿命": ["锈", "断", "裂", "松了", "脱胶", "用几次", "用没多久", "坏了", "不耐用", "质量差"],
    "尺寸/适配": ["太小", "太大", "放不下", "塞不进去", "不合适", "对不上", "尺寸", "型号不对"],
    "使用体验": ["难清洗", "不好拿", "占地方", "麻烦", "费劲", "不方便", "复杂", "难用"],
    "安全/气味": ["味大", "刺鼻", "异味", "刮手", "不稳", "容易倒", "锋利", "割手"],
    "与描述不符": ["和图片", "和描述", "和说的", "没有说的", "没写清楚", "夸大", "不一样"],
}


def _normalize(text: str) -> str:
    """简单清洗：去空白、标点，便于匹配。"""
    text = (text or "").strip()
    text = re.sub(r"\s+", " ", text)
    return text


def _classify_one(review: str) -> list[str]:
    """单条评论打上匹配的痛点标签（可多条）。"""
    normalized = _normalize(review)
    if not normalized:
        return []
    labels: list[str] = []
    for label, keywords in PAIN_POINT_KEYWORDS.items():
        if any(kw in normalized for kw in keywords):
            labels.append(label)
    return labels


def _read_reviews_from_path(path: Path, text_column: str | None) -> Iterable[str]:
    """从文件读取评论文本：支持 .csv（指定列名）或 .txt（每行一条）。"""
    path = path.resolve()
    if not path.exists():
        raise FileNotFoundError(f"文件不存在: {path}")

    if path.suffix.lower() == ".csv":
        with path.open(encoding="utf-8", errors="replace") as f:
            reader = csv.DictReader(f)
            col = text_column or (reader.fieldnames[0] if reader.fieldnames else None)
            if not col:
                raise ValueError("CSV 需指定评论文本列名，例如 --column 评论")
            for row in reader:
                t = row.get(col, "").strip()
                if t:
                    yield t
    else:
        with path.open(encoding="utf-8", errors="replace") as f:
            for line in f:
                line = line.strip()
                if line:
                    yield line


def extract_pain_points(
    reviews: Iterable[str],
    min_mentions: int = 1,
) -> dict[str, dict]:
    """
    对评论迭代器做痛点归类，返回按痛点标签聚合的统计与示例。
    :param reviews: 评论文本迭代器
    :param min_mentions: 至少出现多少次才纳入输出（默认 1）
    :return: { 痛点标签: { "count": N, "examples": [ ... ] } }
    """
    label_count: dict[str, int] = defaultdict(int)
    label_examples: dict[str, list[str]] = defaultdict(list)
    max_examples_per_label = 5

    for review in reviews:
        labels = _classify_one(review)
        for label in set(labels):
            label_count[label] += 1
            if len(label_examples[label]) < max_examples_per_label:
                # 保留原文前 80 字作示例
                snippet = (_normalize(review))[:80]
                if snippet not in label_examples[label]:
                    label_examples[label].append(snippet)

    result: dict[str, dict] = {}
    for label in sorted(label_count.keys(), key=lambda k: -label_count[k]):
        if label_count[label] >= min_mentions:
            result[label] = {
                "count": label_count[label],
                "examples": label_examples[label],
            }
    return result


def _output_table(data: dict[str, dict]) -> str:
    """格式化为可读表格文本。"""
    lines = ["痛点标签\t提及次数\t示例摘要", "-\t-\t-"]
    for label, info in data.items():
        ex = info["examples"][:2]
        ex_str = " | ".join(ex) if ex else "-"
        lines.append(f"{label}\t{info['count']}\t{ex_str}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="从评论文件（CSV/TXT）中做痛点粗分类，输出统计与示例。"
    )
    parser.add_argument(
        "input",
        nargs="?",
        type=Path,
        default=None,
        help="评论文件路径（.csv 或 .txt）；不填则从 stdin 按行读",
    )
    parser.add_argument(
        "-c", "--column",
        type=str,
        default=None,
        help="CSV 中评论文本所在列名（仅 CSV 需要）",
    )
    parser.add_argument(
        "-f", "--format",
        choices=["json", "table"],
        default="table",
        help="输出格式：table 为可读表格，json 为机器可读",
    )
    parser.add_argument(
        "-m", "--min-mentions",
        type=int,
        default=1,
        help="至少出现次数才输出该痛点（默认 1）",
    )
    args = parser.parse_args()

    if args.input is not None:
        reviews = _read_reviews_from_path(args.input, args.column)
    else:
        reviews = (_normalize(line) for line in sys.stdin if _normalize(line))

    try:
        data = extract_pain_points(reviews, min_mentions=args.min_mentions)
    except Exception as e:
        print(f"错误: {e}", file=sys.stderr)
        return 1

    if args.format == "json":
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print(_output_table(data))
    return 0


if __name__ == "__main__":
    sys.exit(main())
