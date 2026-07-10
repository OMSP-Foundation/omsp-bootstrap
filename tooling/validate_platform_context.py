#!/usr/bin/env python3
"""Validate the OMSP platform context artifact and registry."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "architecture" / "PLATFORM_CONTEXT.md"
REGISTRY = ROOT / "architecture" / "platform-context.json"
EXPECTED_ENGINES = {
    "engineering-kernel",
    "knowledge-engine",
    "traceability-engine",
    "publication-engine",
}
REQUIRED_SECTIONS = (
    "## 3. System Context",
    "## 4. External Actors",
    "## 5. OMSP Platform Boundary",
    "## 6. Repository Boundary View",
    "## 7. Engine Interaction View",
    "## 8. Trust and Authority Boundaries",
)


def main() -> int:
    errors: list[str] = []

    if not DOC.is_file():
        errors.append("missing architecture/PLATFORM_CONTEXT.md")
    if not REGISTRY.is_file():
        errors.append("missing architecture/platform-context.json")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    text = DOC.read_text(encoding="utf-8")
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))

    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"missing required section: {section}")

    if "```mermaid" not in text:
        errors.append("platform context does not contain Mermaid source")

    engines = set(data.get("engines", []))
    if engines != EXPECTED_ENGINES:
        errors.append(f"engine registry mismatch: {sorted(engines)}")

    rules = data.get("authority_rules", {})
    if rules.get("human_approval_required") is not True:
        errors.append("human approval boundary must be required")
    if rules.get("automation_can_approve") is not False:
        errors.append("automation must not be allowed to approve")
    if rules.get("artifact_identity_basis") != "Artifact-ID":
        errors.append("artifact identity basis must be Artifact-ID")

    for engine in EXPECTED_ENGINES:
        label = engine.replace("-", " ").title()
        if label not in text:
            errors.append(f"context document does not name engine: {label}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Platform context validation failed with {len(errors)} error(s).")
        return 1

    print("Platform context validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
