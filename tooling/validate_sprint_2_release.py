#!/usr/bin/env python3
"""Validate the Sprint-2 baseline and release-readiness package."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TAG = "v0.2.0-foundation-sprint-2"
FILES = {
    "release/SPRINT_2_BASELINE_MANIFEST.md": [
        "OMSP-REL-SPRINT-2-BASELINE-0001",
        TAG,
        "WP-0022",
        "WP-0057",
        "WP-0028",
        "WP-0029",
    ],
    "release/RELEASE_NOTES_SPRINT_2.md": [
        "OMSP-REL-NOTES-SPRINT-2-0001",
        TAG,
        "Formal Ontology",
        "Platform Architecture",
        "Traceability and Validation",
        "Publication",
    ],
    "release/SPRINT_2_BASELINE_APPROVAL.md": [
        "OMSP-REL-SPRINT-2-APPROVAL-0001",
        TAG,
        "Human Decision",
        "Approved commit SHA",
    ],
    "release/SPRINT_2_RELEASE_READINESS.md": [
        "OMSP-REL-SPRINT-2-READINESS-0001",
        "PR #92",
        "PR #100",
        "Human baseline approval recorded",
    ],
}


def main() -> int:
    errors: list[str] = []
    for relative_path, required_terms in FILES.items():
        path = ROOT / relative_path
        if not path.is_file():
            errors.append(f"missing file: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        for term in required_terms:
            if term not in text:
                errors.append(f"{relative_path} lacks required term: {term}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Sprint-2 release validation failed with {len(errors)} error(s).")
        return 1

    print(f"Sprint-2 release package validation passed for {len(FILES)} artifacts.")
    print("Human approval and tag/release publication remain external accountable actions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
