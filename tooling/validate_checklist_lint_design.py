#!/usr/bin/env python3
"""Validate OMSP checklist linting design artifacts."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULES = ROOT / "validation" / "checklist-lint-rules.json"
SCHEMA = ROOT / "schemas" / "checklist-lint-result.schema.json"
DESIGN = ROOT / "validation" / "CHECKLIST_LINTING_DESIGN.md"


def main() -> int:
    errors: list[str] = []
    rules_data = json.loads(RULES.read_text(encoding="utf-8"))
    schema_data = json.loads(SCHEMA.read_text(encoding="utf-8"))
    design_text = DESIGN.read_text(encoding="utf-8")

    rule_ids: set[str] = set()
    severities = set(rules_data.get("allowed_severities", []))
    for rule in rules_data.get("rules", []):
        rule_id = rule.get("id", "")
        if rule_id in rule_ids:
            errors.append(f"duplicate rule ID: {rule_id}")
        rule_ids.add(rule_id)
        if rule.get("severity") not in severities:
            errors.append(f"invalid severity for {rule_id}")
        if not rule.get("description"):
            errors.append(f"missing description for {rule_id}")

    required_sections = (
        "## 2. Scope",
        "## 4. Outcome Vocabulary",
        "## 5. Lint Rule Families",
        "## 6. Severity and Enforcement",
        "## 8. Human Accountability Boundary",
    )
    for section in required_sections:
        if section not in design_text:
            errors.append(f"missing design section: {section}")

    status_enum = (
        schema_data.get("properties", {})
        .get("status", {})
        .get("enum", [])
    )
    for status in ("pass", "fail", "gate-blocked", "tool-error"):
        if status not in status_enum:
            errors.append(f"missing result status: {status}")

    if "Tooling must not synthesize this value" not in SCHEMA.read_text(encoding="utf-8"):
        errors.append("schema lacks human approval boundary")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Checklist linting design validation passed for {len(rule_ids)} rules.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
