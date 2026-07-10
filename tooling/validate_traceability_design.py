#!/usr/bin/env python3
"""Validate the Sprint-2 traceability automation design artifacts."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DESIGN = ROOT / "architecture" / "TRACEABILITY_AUTOMATION_DESIGN.md"
RULES = ROOT / "validation" / "traceability-rules.json"
SCHEMA = ROOT / "schemas" / "traceability-report.schema.json"
RULE_RE = re.compile(r"^TRACE-[A-Z]+-[0-9]{3}$")


def main() -> int:
    errors: list[str] = []
    for path in (DESIGN, RULES, SCHEMA):
        if not path.is_file():
            errors.append(f"missing required artifact: {path.relative_to(ROOT)}")

    if errors:
        print("\n".join(f"ERROR: {item}" for item in errors))
        return 1

    design = DESIGN.read_text(encoding="utf-8")
    for heading in (
        "## Metadata Validation",
        "## Artifact ID Validation",
        "## Relation Validation",
        "## Pull Request Evidence",
        "## Baseline and Release Reports",
        "## Human Accountability Boundary",
    ):
        if heading not in design:
            errors.append(f"design lacks section: {heading}")

    registry = json.loads(RULES.read_text(encoding="utf-8"))
    rules = registry.get("rules", [])
    ids = [rule.get("id", "") for rule in rules]
    if len(ids) != len(set(ids)):
        errors.append("duplicate rule ID")
    for rule_id in ids:
        if not RULE_RE.fullmatch(rule_id):
            errors.append(f"invalid rule ID: {rule_id}")

    categories = {rule.get("category") for rule in rules}
    required = {"metadata", "identity", "relation", "pull-request", "baseline", "release"}
    missing = sorted(required - categories)
    if missing:
        errors.append(f"missing rule categories: {', '.join(missing)}")

    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    required_fields = set(schema.get("required", []))
    if not {"tool", "repository", "summary", "findings"}.issubset(required_fields):
        errors.append("report schema lacks required top-level fields")

    if errors:
        print("\n".join(f"ERROR: {item}" for item in errors))
        return 1

    print(f"Traceability automation design validation passed for {len(rules)} rules.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
