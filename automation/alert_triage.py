#!/usr/bin/env python3
"""Summarize Wazuh JSONL alerts into a CSV triage sheet."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


def nested_get(data: dict[str, Any], *keys: str, default: Any = "") -> Any:
    current: Any = data
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current


def severity_from_level(level: int) -> str:
    if level >= 12:
        return "critical"
    if level >= 10:
        return "high"
    if level >= 7:
        return "medium"
    return "low"


def normalize_mitre(value: Any) -> str:
    if isinstance(value, list):
        return ",".join(str(item) for item in value)
    if value in (None, ""):
        return ""
    return str(value)


def parse_alert(alert: dict[str, Any]) -> dict[str, Any]:
    raw_level = nested_get(alert, "rule", "level", default=0)
    try:
        level = int(raw_level)
    except (TypeError, ValueError):
        level = 0

    mitre_ids = nested_get(alert, "rule", "mitre", "id", default=[])

    return {
        "timestamp": alert.get("timestamp", ""),
        "agent": nested_get(alert, "agent", "name"),
        "rule_id": nested_get(alert, "rule", "id"),
        "level": level,
        "severity": severity_from_level(level),
        "description": nested_get(alert, "rule", "description"),
        "mitre": normalize_mitre(mitre_ids),
    }


def load_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON on line {line_number}: {exc}") from exc
            if not isinstance(item, dict):
                raise ValueError(f"Line {line_number} is not a JSON object")
            yield item


def write_csv(rows: list[dict[str, Any]], output: Path) -> None:
    fieldnames = [
        "timestamp",
        "agent",
        "rule_id",
        "level",
        "severity",
        "description",
        "mitre",
    ]
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def print_summary(rows: list[dict[str, Any]]) -> None:
    print(f"Alerts triaged: {len(rows)}")
    if not rows:
        return

    severity_counts = Counter(row["severity"] for row in rows)
    rule_counts = Counter(str(row["rule_id"]) for row in rows)

    print("Severity:")
    for severity in ("critical", "high", "medium", "low"):
        if severity_counts[severity]:
            print(f"  {severity:8} {severity_counts[severity]}")

    print("Top rules:")
    for rule_id, count in rule_counts.most_common(5):
        print(f"  {rule_id:8} {count}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Triage Wazuh JSONL alerts")
    parser.add_argument("input", type=Path, help="JSONL alert file")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("triage.csv"),
        help="CSV output path (default: triage.csv)",
    )
    parser.add_argument(
        "--min-level",
        type=int,
        default=0,
        help="Only include alerts at or above this Wazuh level",
    )
    args = parser.parse_args()

    parsed = [parse_alert(alert) for alert in load_jsonl(args.input)]
    rows = [row for row in parsed if row["level"] >= args.min_level]

    write_csv(rows, args.output)
    print_summary(rows)
    print(f"CSV written to: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
