---
Artifact-ID: OMSP-GOV-ADR-0003
Title: ADR-0003 Pinned Python Dependencies for Schema Validation
Version: 0.1.0
Status: Review
Owner: OMSP Foundation Governance
Baseline: Sprint-7
Classification: Public
Related-Issue: WP-0078 / #199
---

# ADR-0003: Pinned Python Dependencies for Schema Validation

## Status

Decision accepted by accountable human decision (Cengiz, 2026-07-14,
recorded as D1 in the issue #199 decision record), delivered through
WP-0078. This artifact enters at `Review`; promotion to `Active` is a
human gate per `governance/METADATA_AND_TRACEABILITY_STANDARD.md` §6.

## Context

Until WP-0078, every OMSP validator (`tooling/omsp_validate.py`,
`tooling/validate_ontology.py`, the `validate_*.py` family) ran on the
Python standard library alone — no third-party dependency existed in any
CI workflow. WP-0078 introduces JSON Schema (Draft 2020-12) instance
schemas in `schemas/` whose CI gate must (test checklist TS-1) verify
each schema against the official meta-schema and validate YAML instances
against the schemas, including cross-file `$ref` resolution.

Options considered:

- **(A) Standard-library subset validator** — hand-write the subset of
  JSON Schema semantics the schemas use. Rejected: it weakens the TS-1
  meta-schema requirement to "whatever the subset implements", silently
  diverges from Draft 2020-12 semantics (`oneOf` short-circuiting,
  `$ref` resolution, `propertyNames`), and turns every future schema
  feature into validator maintenance.
- **(B) Adopt `jsonschema` + `PyYAML` unpinned** — rejected: CI behavior
  would drift with upstream releases; a gate must be reproducible.
- **(C) Adopt `jsonschema` + `PyYAML` with pinned versions** — full
  Draft 2020-12 conformance from the reference Python implementation,
  YAML 1.1 parsing via `yaml.safe_load`, reproducible CI runs, explicit
  human-reviewed upgrades.

## Decision

Adopt **(C)**. Binding rules:

1. Schema-validation tooling (first consumer:
   `tooling/validate_instance_schemas.py`) uses **`jsonschema==4.26.0`**
   and **`PyYAML==6.0.3`** (latest stable on PyPI, verified 2026-07-14).
   Transitive dependencies (`referencing`, `jsonschema-specifications`,
   `attrs`, `rpds-py`) are accepted as resolved by pip for the pinned
   top-level versions.
2. CI workflows that run this tooling install the dependencies with an
   explicit pinned `pip install` step (first consumer:
   `.github/workflows/instance-schemas.yml`). No workflow installs
   unpinned Python packages.
3. Version upgrades are ordinary reviewed changes: a PR updates the pin
   in the workflow(s), this ADR's version list, and must pass the full
   schema self-test (positive fixtures accepted, negative fixtures
   rejected) before merge.
4. Only YAML parsing via `yaml.safe_load` is permitted (no arbitrary
   object construction).
5. Scope: validation tooling only. This ADR authorizes no runtime,
   service, or publication dependency.

## Consequences

Positive: full Draft 2020-12 conformance including meta-schema checks
and cross-file `$ref` resolution; reproducible CI gates; upgrade path is
explicit and human-reviewed.

Accepted costs and risks: the first third-party supply-chain surface in
CI tooling — mitigated by pinning, by `pip`'s use of PyPI over TLS, and
by the deferred security items of
`planning/WP-0075-DOMAIN-BACKLOG-REBASELINE.md` §8 (vulnerability
intelligence re-enters at community opening); local contributors must
install two packages to run the validator (the tool fails with a clear
instruction if they are missing).

## Alternatives Considered

- (A) Standard-library subset — rejected (weakens TS-1, permanent
  maintenance burden).
- (B) Unpinned adoption — rejected (non-reproducible gate).
