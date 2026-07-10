#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    ROOT / "architecture/PUBLICATION_WORKFLOW.md",
    ROOT / "schemas/publication-package.schema.json",
    ROOT / "validation/PUBLICATION_READINESS_CHECKLIST.md",
]


def main() -> int:
    errors: list[str] = []
    for path in REQUIRED:
        if not path.is_file():
            errors.append(f"missing required artifact: {path.relative_to(ROOT)}")
    if (ROOT / "schemas/publication-package.schema.json").is_file():
        schema = json.loads((ROOT / "schemas/publication-package.schema.json").read_text())
        required = set(schema.get("required", []))
        for field in {"package_id", "version", "channel", "source_commit", "artifacts", "integrity"}:
            if field not in required:
                errors.append(f"schema missing required field: {field}")
    workflow = (ROOT / "architecture/PUBLICATION_WORKFLOW.md").read_text() if REQUIRED[0].is_file() else ""
    for phrase in ["Preview", "Baseline", "Release", "Human Authority Boundary", "Publication Evidence"]:
        if phrase not in workflow:
            errors.append(f"workflow missing section or concept: {phrase}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Publication workflow design validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
