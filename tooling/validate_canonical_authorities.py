#!/usr/bin/env python3
"""Validate OMSP canonical authority registry and compatibility stubs."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "governance" / "canonical-authorities.json"
REQUIRED_STUB_FIELDS = ("Status: Superseded", "Superseded-By:", "Canonical-Path:")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def main() -> int:
    errors = 0
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    authorities = data.get("authorities", [])

    domains: set[str] = set()
    artifact_ids: set[str] = set()

    for authority in authorities:
        domain = authority["domain"]
        artifact_id = authority["canonical_artifact_id"]
        canonical_path = ROOT / authority["canonical_path"]

        if domain in domains:
            fail(f"duplicate authority domain: {domain}")
            errors += 1
        domains.add(domain)

        if artifact_id in artifact_ids:
            fail(f"duplicate canonical Artifact ID: {artifact_id}")
            errors += 1
        artifact_ids.add(artifact_id)

        if authority.get("status") != "Active":
            fail(f"canonical authority is not Active: {domain}")
            errors += 1

        if not canonical_path.is_file():
            fail(f"missing canonical path: {authority['canonical_path']}")
            errors += 1

        for legacy in authority.get("legacy_paths", []):
            legacy_path = ROOT / legacy
            if not legacy_path.is_file():
                fail(f"missing compatibility stub: {legacy}")
                errors += 1
                continue
            text = legacy_path.read_text(encoding="utf-8")
            for field in REQUIRED_STUB_FIELDS:
                if field not in text:
                    fail(f"{legacy} lacks required marker: {field}")
                    errors += 1
            if artifact_id not in text:
                fail(f"{legacy} does not reference canonical Artifact ID {artifact_id}")
                errors += 1

    if errors:
        print(f"Canonical authority validation failed with {errors} error(s).")
        return 1

    print(f"Canonical authority validation passed for {len(authorities)} domains.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
