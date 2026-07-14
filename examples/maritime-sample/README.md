---
Artifact-ID: OMSP-EXAMPLE-MARITIME-SAMPLE-0001
Title: Maritime Sample Model Package
Version: 0.1.0
Status: Draft
Owner: toss-cengiz
Baseline: Sprint-7
Classification: Public
Related-Issue: WP-0080 / #201
Depends-On:
  - OMSP-ONTOLOGY-MARITIME-0001
  - OMSP-SCHEMA-MARITIME-0001
Traceability:
  - ISSUE-201
  - OMSP-PLANNING-REBASELINE-0001
---

# Maritime Sample Model Package

## 1. Purpose

This package is the representative sample maritime model of WP-0080 —
the Sprint-7 visible outcome (`OMSP-PLANNING-REBASELINE-0001` §3.1,
exit criteria 3 and 5). It proves, **before any real data entry**, that
the WP-0077 ontology and WP-0078 instance schemas validate end-to-end:
every schema type is instantiated, every value-bearing field satisfies
the provenance contract, and one non-electrical placeholder slice
(freshwater) passes the **same** pipeline with no special-case code —
the domain-neutrality proof.

The package validates against the merged, governed schema and ontology
files (`schemas/`, `ontology/omsp-ontology.json`). It contains **no
copy** of any schema or ontology content (single-source rule).

## 2. Fictionality declaration (binding for this package)

- **All data in this package is fictional.** The
  `vessel-design:fixture:example-yacht` namespace, all
  `source:fixture:*` and `document:fixture:*` identifiers, and every
  numeric value and unit (`fixture-metre`, `fixture-volt`, …) are
  artificial placeholders created only to exercise the validators.
- No file represents a real vessel, manufacturer, model or technical
  value. In particular the package contains **no Hanse 460 data**; real
  sourced data is WP-0082 scope.
- `source:fixture:*` identifiers exist in **no source register**
  (including `reference/HANSE_460_SOURCE_REGISTER.md`) and carry **no
  evidence value**; source-register resolution is WP-0083 scope.
- Nothing in this package is an operational instruction, an approved
  procedure, or a seaworthiness, safety or certification claim.
  Validation results prove structural and provenance-contract
  conformance only (see `schemas/MARITIME_INSTANCE_SCHEMAS.md` §8).

## 3. Package contents (type → file mapping)

| Instance type (schema) | Ontology concept | File |
| --- | --- | --- |
| Vessel (`vessel-instance.schema.json`) | `OMSP-CONCEPT-VESSEL` | `vessel.yaml` |
| Vessel System (`system-instance.schema.json`) | `OMSP-CONCEPT-VESSEL-SYSTEM` | `system-electrical.yaml`, `system-freshwater.yaml` |
| Equipment Role (`equipment-instance.schema.json`) | `OMSP-CONCEPT-EQUIPMENT-ROLE` | `equipment-battery-bank.yaml`, `equipment-dc-distribution-panel.yaml`, `equipment-freshwater-tank.yaml`, `equipment-freshwater-pressure-pump.yaml` |
| Interface (`interface-instance.schema.json`) | `OMSP-CONCEPT-INTERFACE` | `interface-electrical-feed.yaml`, `interface-freshwater-suction.yaml` |
| Connection (`connection-instance.schema.json`) | `OMSP-CONCEPT-CONNECTION` | `connection-electrical-feed.yaml`, `connection-freshwater-suction.yaml` |
| Operational Scenario (`scenario-instance.schema.json`) | `OMSP-CONCEPT-OPERATIONAL-SCENARIO` | `scenario-freshwater-delivery-degraded.yaml` |

All files describe one coherent fictional boat: a vessel design with an
electrical slice (battery bank → DC distribution panel) and a
non-electrical freshwater slice (tank → pressure pump), cross-linked by
file-to-file ID references (e.g. the pump role `depends_on` the panel
role; the degraded-delivery scenario implicates roles from both
slices). Nested `ports[]` and `measurement_points[]` entries resolve to
`OMSP-CONCEPT-PORT` and `OMSP-CONCEPT-MEASUREMENT-POINT`.

## 4. Validation — the one documented command chain

Prerequisite (once per environment, pinned per
`governance/ADR-0004-PYTHON-VALIDATION-DEPENDENCIES.md`):
`pip install jsonschema==4.26.0 PyYAML==6.0.3`.

Run from the repository root:

```bash
python3 tooling/validate_ontology.py
python3 tooling/validate_instance_schemas.py examples/maritime-sample
```

Expected result — both commands exit `0`:

1. `validate_ontology.py` prints
   `Ontology validation passed: 25 concepts, 19 relations.`
2. `validate_instance_schemas.py` prints a JSON report with
   `"findings": 0` and `"errors": 0`; the summary shows the 12 package
   instances validated (`instances_validated`), the schema self-test
   fixtures (positives accepted, negatives rejected) and the
   ontology-conformance check (`OMSP-ISCHEMA-005`): every
   `OMSP-CONCEPT-*` reference in the schemas and in this package
   resolves to `ontology/omsp-ontology.json`.

The same chain runs in CI (`.github/workflows/instance-schemas.yml`).
Deliberately failing inputs live in `tests/schemas/negative/` (N1–N11,
see `tests/schemas/README.md`); this package intentionally contains
none.
