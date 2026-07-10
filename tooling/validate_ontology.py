#!/usr/bin/env python3
"""Validate the OMSP machine-readable ontology registry."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "ontology" / "omsp-ontology.json"


def main() -> int:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    errors: list[str] = []

    concepts = data.get("concepts", [])
    relations = data.get("relations", [])
    concept_ids = [item.get("id") for item in concepts]
    relation_ids = [item.get("id") for item in relations]
    concept_set = set(concept_ids)

    if len(concept_ids) != len(concept_set):
        errors.append("duplicate concept ID")
    if len(relation_ids) != len(set(relation_ids)):
        errors.append("duplicate relation ID")

    for concept in concepts:
        cid = concept.get("id", "")
        if not cid.startswith("OMSP-CONCEPT-"):
            errors.append(f"invalid concept ID: {cid}")
        parent = concept.get("parent")
        if parent and parent not in concept_set:
            errors.append(f"unknown parent {parent} for {cid}")

    for relation in relations:
        rid = relation.get("id", "")
        if not rid.startswith("OMSP-RELATION-"):
            errors.append(f"invalid relation ID: {rid}")
        for field in ("domain", "range"):
            target = relation.get(field)
            if target not in concept_set:
                errors.append(f"unknown {field} {target} for {rid}")

    if "OMSP-RELATION-APPROVES" in relation_ids:
        relation = next(r for r in relations if r["id"] == "OMSP-RELATION-APPROVES")
        if relation.get("human_authority_required") is not True:
            errors.append("approves relation must require human authority")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Ontology validation passed: {len(concepts)} concepts, {len(relations)} relations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
