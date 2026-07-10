#!/usr/bin/env python3
"""Validate OMSP platform engine architecture registry."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "architecture" / "platform-engines.json"
REQUIRED_SECTIONS = ("## Purpose", "## Responsibilities", "## Inputs", "## Outputs", "## Boundaries", "## Contracts", "## Governance")


def main() -> int:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    engines = data.get("engines", [])
    errors: list[str] = []

    if len(engines) != 4:
        errors.append(f"expected 4 engines, found {len(engines)}")

    ids: set[str] = set()
    artifact_ids: set[str] = set()
    paths: set[str] = set()

    for engine in engines:
        for field in ("id", "artifact_id", "path", "inputs", "outputs"):
            if not engine.get(field):
                errors.append(f"engine entry lacks {field}: {engine}")

        if engine.get("id") in ids:
            errors.append(f"duplicate engine id: {engine['id']}")
        ids.add(engine.get("id", ""))

        if engine.get("artifact_id") in artifact_ids:
            errors.append(f"duplicate Artifact ID: {engine['artifact_id']}")
        artifact_ids.add(engine.get("artifact_id", ""))

        if engine.get("path") in paths:
            errors.append(f"duplicate engine path: {engine['path']}")
        paths.add(engine.get("path", ""))

        path = ROOT / engine.get("path", "")
        if not path.is_file():
            errors.append(f"missing engine artifact: {engine.get('path')}")
            continue

        text = path.read_text(encoding="utf-8")
        if engine.get("artifact_id") not in text:
            errors.append(f"Artifact ID mismatch in {engine.get('path')}")
        for section in REQUIRED_SECTIONS:
            if section not in text:
                errors.append(f"{engine.get('path')} lacks section {section}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Platform engine architecture validation passed for 4 engines.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
