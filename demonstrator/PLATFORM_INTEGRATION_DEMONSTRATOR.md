---
Artifact-ID: OMSP-DEMONSTRATOR-PLATFORM-0001
Title: End-to-End Platform Integration Demonstrator
Version: 0.1.0
Status: Review
Owner: OMSP Engineering Council
Approvers:
  - Accountable Maintainer
Created: 2026-07-10
Last-Updated: 2026-07-10
Sprint: Sprint-5
Work-Package: WP-0054
Traceability:
  - ISSUE-88
---

# End-to-End Platform Integration Demonstrator

## Purpose

This demonstrator proves that the Sprint-5 OMSP components can execute as one reproducible evidence chain. It generates a representative repository, validates it, assembles a non-authoritative publication preview, performs security checks and produces correlated audit and health records.

## Reproduction

Run:

```bash
python tooling/omsp_demonstrate.py --source-commit "$(git rev-parse HEAD)"
```

The command recreates `build/demonstrator/` from scratch. Equivalent source inputs and tool versions produce equivalent generated repository content, reports and package checksums. Workflow correlation metadata may differ when a different source commit is supplied.

## Demonstrated Flow

1. `omsp_generate_repo.py` creates the representative repository from `tests/generator/repository-profile.json`.
2. `omsp_validate.py` validates the generated governed artifacts.
3. `omsp_publish.py` assembles the Sprint-5 preview package and checksum manifest.
4. `omsp_security_baseline.py` records workflow, action and secret-scanning evidence.
5. The demonstrator constructs an explainable gate record from component outcomes.
6. `omsp_observability.py` creates structured JSONL audit events and a health record.
7. `demonstrator-manifest.json` links steps, exit codes, outputs and SHA-256 evidence digests.

## Evidence Package

The workflow retains the generated repository, generator report, validation report, publication package, checksums, security report, demonstrator gate, audit events, health record and final demonstrator manifest for 30 days.

## Failure and Recovery Demonstration

Each component preserves command, exit code, bounded stdout/stderr and available evidence. A non-zero component result changes the demonstrator decision to `blocked`. Operators must correct deterministic source failures before rerun. Transient runner failures may be rerun only after classification, while preserving the failed attempt and correlation identifiers.

The negative behavior is covered by unit tests that verify failure propagation. The demonstrator never converts a failed component into a passing decision.

## Human Approval Points

A passing demonstrator does not approve a pull request, baseline, publication, release or deployment. The preview package is non-authoritative. Security warnings require accountable disposition. Production readiness and release authorization remain explicit human decisions.

## Known Production Gaps

- no production deployment target or environment approval;
- no signed provenance or cryptographically signed audit log;
- no remote observability backend, alert delivery or long-term evidence store;
- no vulnerability-database lookup or repository-history secret scan;
- no scalability, load, availability or disaster-recovery validation;
- publication uses a preview channel and does not establish an approved release baseline.

## Authority Boundary

Automation may reproduce the scenario, validate rules, create preview artifacts and produce evidence. It cannot accept risk, approve exceptions, authorize publication, certify production safety or approve release readiness.
