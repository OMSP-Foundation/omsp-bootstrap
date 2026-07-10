---
Artifact-ID: OMSP-VALIDATION-TOOLCHAIN-0001
Title: Validator Toolchain MVP
Version: 0.1.0
Status: Review
Owner: OMSP Engineering Council
Approvers:
  - Accountable Maintainer
Created: 2026-07-10
Last-Updated: 2026-07-10
Sprint: Sprint-5
Work-Package: WP-0048
Traceability:
  - ISSUE-82
---

# Validator Toolchain MVP

## Purpose

The MVP provides a deterministic, dependency-free Python validator for governed Markdown and JSON artifacts. It checks required front-matter metadata, Artifact ID syntax, JSON parseability and prohibited automation-authority claims. It emits a stable machine-readable JSON report.

## Local Execution

```bash
python tooling/omsp_validate.py governance planning roadmap architecture knowledge reference release schemas validation
python tooling/omsp_validate.py planning/SPRINT_5_EXECUTION_PLAN.md --output report.json
python -m unittest tests/test_omsp_validator.py
```

Exit codes are `0` for no blocking findings, `1` for error or gate findings and `2` for invalid invocation or unsafe target paths.

## Determinism

Files and findings are sorted before report generation. The report excludes timestamps and environment-dependent random values. Equivalent repository content and tool version therefore produce equivalent findings and summary values. The repository path field may differ between execution environments and is not an integrity digest.

## Rule Set

- `OMSP-META-001`: required metadata is missing;
- `OMSP-ID-001`: Artifact ID syntax is invalid;
- `OMSP-JSON-001`: JSON cannot be parsed;
- `OMSP-AUTH-001`: text claims approval authority for AI, CI or validation automation.

## Fixtures and Tests

The positive fixture must return no findings. The negative fixture must return both metadata and identity findings. Unit tests also verify deterministic discovery ordering.

## CI Integration

`.github/workflows/omsp-validator.yml` runs unit tests, validates governed repository directories and uploads the JSON report even when validation fails. Workflow permissions are read-only.

## Authority Boundary

A successful validation report confirms only that implemented deterministic rules passed. It does not approve artifact meaning, evidence adequacy, safety, security, baseline status, release status or production readiness. Those decisions remain with accountable human reviewers.

## Known Limitations

The MVP does not yet provide full YAML parsing, schema evaluation, cross-file relation resolution, duplicate Artifact ID detection, checklist semantic evaluation, cryptographic integrity evidence or incremental validation. These are explicit follow-up areas for later Sprint-5 work.
