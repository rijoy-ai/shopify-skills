#!/usr/bin/env python3
"""
批量评论 → 痛点标签粗分类工具。

设计目标：
- 单一职责：只做“文本归一化 + 关键词/规则匹配 + 结构化输出”
- 可扩展：关键词映射从 JSON 加载（默认同目录 keywords_zh.json）
- 可审计：可导出逐条评论的标签结果，方便人工复核与合并同类项
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator, Mapping, Sequence


DEFAULT_KEYWORDS_PATH = Path(__file__).with_name("keywords_zh.json")


def normalize_text(text: str) -> str:
    text = (text or "").strip()
    text = re.sub(r"\s+", " ", text)
    return text


def load_keyword_map(path: Path | None) -> dict[str, list[str]]:
    p = (path or DEFAULT_KEYWORDS_PATH).resolve()
    with p.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("关键词映射必须是 JSON object：{label: [keywords...]}")
    keyword_map: dict[str, list[str]] = {}
    for label, keywords in data.items():
        if not isinstance(label, str) or not isinstance(keywords, list):
            raise ValueError("关键词映射格式错误：label 必须是字符串，keywords 必须是数组")
        keyword_map[label] = [str(k).strip() for k in keywords if str(k).strip()]
    return keyword_map


def iter_reviews_from_path(path: Path, text_column: str | None) -> Iterator[str]:
    path = path.resolve()
    if not path.exists():
        raise FileNotFoundError(f"文件不存在: {path}")

    if path.suffix.lower() == ".csv":
        with path.open(encoding="utf-8", errors="replace", newline="") as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames:
                return
            col = text_column or reader.fieldnames[0]
            if col not in reader.fieldnames:
                raise ValueError(f"CSV 找不到列：{col}。可用列：{reader.fieldnames}")
            for row in reader:
                t = normalize_text(row.get(col, ""))
                if t:
                    yield t
    else:
        with path.open(encoding="utf-8", errors="replace") as f:
            for line in f:
                t = normalize_text(line)
                if t:
                    yield t


def iter_reviews_from_stdin() -> Iterator[str]:
    for line in sys.stdin:
        t = normalize_text(line)
        if t:
            yield t


def classify_review(review: str, keyword_map: Mapping[str, Sequence[str]]) -> list[str]:
    """
    返回该评论命中的标签列表（可多标签）。
    这里只做关键词包含匹配；更复杂的语义归类应交给人工/模型层。
    """
    text = normalize_text(review)
    if not text:
        return []
    labels: list[str] = []
    for label, keywords in keyword_map.items():
        if any(kw and kw in text for kw in keywords):
            labels.append(label)
    return labels


@dataclass(frozen=True)
class AggregatedLabel:
    label: str
    count: int
    examples: list[str]


def aggregate_labels(
    reviews: Iterable[str],
    keyword_map: Mapping[str, Sequence[str]],
    *,
    min_mentions: int = 1,
    max_examples_per_label: int = 5,
) -> dict[str, AggregatedLabel]:
    label_counts: Counter[str] = Counter()
    label_examples: dict[str, list[str]] = defaultdict(list)

    for review in reviews:
        labels = set(classify_review(review, keyword_map))
        for label in labels:
            label_counts[label] += 1
            if len(label_examples[label]) < max_examples_per_label:
                snippet = normalize_text(review)[:120]
                if snippet and snippet not in label_examples[label]:
                    label_examples[label].append(snippet)

    result: dict[str, AggregatedLabel] = {}
    for label, count in label_counts.most_common():
        if count >= min_mentions:
            result[label] = AggregatedLabel(label=label, count=count, examples=label_examples[label])
    return result


def tag_each_review(
    reviews: Iterable[str],
    keyword_map: Mapping[str, Sequence[str]],
) -> Iterator[dict]:
    for review in reviews:
        labels = classify_review(review, keyword_map)
        yield {"review": review, "labels": labels}


def format_table(aggregated: Mapping[str, AggregatedLabel], *, example_cols: int = 2) -> str:
    lines = ["痛点标签\t提及次数\t示例摘要", "-\t-\t-"]
    for label, info in aggregated.items():
        ex = info.examples[:example_cols]
        ex_str = " | ".join(ex) if ex else "-"
        lines.append(f"{label}\t{info.count}\t{ex_str}")
    return "\n".join(lines)


def write_csv_aggregate(path: Path, aggregated: Mapping[str, AggregatedLabel]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["label", "count", "examples"])
        for label, info in aggregated.items():
            w.writerow([label, info.count, " | ".join(info.examples)])


def write_csv_tagged(path: Path, tagged: Iterable[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["review", "labels"])
        for item in tagged:
            w.writerow([item.get("review", ""), ",".join(item.get("labels", []))])


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="从评论文件（CSV/TXT）中做痛点粗分类，输出统计与示例。")
    p.add_argument(
        "input",
        nargs="?",
        type=Path,
        default=None,
        help="评论文件路径（.csv 或 .txt）；不填则从 stdin 按行读",
    )
    p.add_argument("-c", "--column", type=str, default=None, help="CSV 中评论文本所在列名（仅 CSV 需要）")
    p.add_argument(
        "-k",
        "--keywords",
        type=Path,
        default=None,
        help="关键词映射 JSON 路径（默认使用同目录 keywords_zh.json）",
    )
    p.add_argument(
        "-f",
        "--format",
        choices=["table", "json", "csv"],
        default="table",
        help="输出格式：table/json/csv（csv 需配合 --output）",
    )
    p.add_argument(
        "-m",
        "--min-mentions",
        type=int,
        default=1,
        help="至少出现次数才输出该痛点（默认 1）",
    )
    p.add_argument(
        "--per-review",
        action="store_true",
        help="输出逐条评论的标签结果（而非聚合统计）",
    )
    p.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="输出文件路径（建议用于 json/csv；不填则打印到 stdout）",
    )
    return p.parse_args()


def main() -> int:
    args = parse_args()

    try:
        keyword_map = load_keyword_map(args.keywords)
    except Exception as e:
        print(f"错误：关键词映射加载失败：{e}", file=sys.stderr)
        return 2

    try:
        if args.input is None:
            reviews = list(iter_reviews_from_stdin())
        else:
            reviews = list(iter_reviews_from_path(args.input, args.column))
    except Exception as e:
        print(f"错误：读取评论失败：{e}", file=sys.stderr)
        return 2

    if args.per_review:
        tagged = list(tag_each_review(reviews, keyword_map))
        if args.format == "table":
            preview = tagged[:10]
            text = json.dumps({"preview_top10": preview, "total": len(tagged)}, ensure_ascii=False, indent=2)
            if args.output:
                args.output.write_text(text, encoding="utf-8")
            else:
                print(text)
            return 0

        if args.format == "json":
            text = json.dumps(tagged, ensure_ascii=False, indent=2)
            if args.output:
                args.output.write_text(text, encoding="utf-8")
            else:
                print(text)
            return 0

        if not args.output:
            print("错误：--format csv 且 --per-review 时必须提供 --output", file=sys.stderr)
            return 2
        write_csv_tagged(args.output, tagged)
        return 0

    aggregated = aggregate_labels(reviews, keyword_map, min_mentions=args.min_mentions)

    if args.format == "table":
        text = format_table(aggregated)
        if args.output:
            args.output.write_text(text, encoding="utf-8")
        else:
            print(text)
        return 0

    if args.format == "json":
        payload = {
            "total_reviews": len(reviews),
            "labels": [
                {"label": v.label, "count": v.count, "examples": v.examples}
                for v in aggregated.values()
            ],
        }
        text = json.dumps(payload, ensure_ascii=False, indent=2)
        if args.output:
            args.output.write_text(text, encoding="utf-8")
        else:
            print(text)
        return 0

    if not args.output:
        print("错误：--format csv 时必须提供 --output", file=sys.stderr)
        return 2
    write_csv_aggregate(args.output, aggregated)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

