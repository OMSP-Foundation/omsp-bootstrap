# OMSP Foundation Release Notes — v0.5.2

**Release date:** 2026-07-13
**Classification:** Process-automation patch (Production Baseline Candidate lineage)
**Approval status:** Published by the Automated Release Pipeline under the standing human authorization of ADR-0002; recorded human release decision: direct instruction (Cengiz, 2026-07-13)
**Authorized scope:** Controlled pre-production and pilot evaluation (unchanged from v0.5.1)

## Overview

`v0.5.2` is a patch release on the `v0.5.1` clean baseline. It delivers the
process automation and agent architecture that Sprint-7+ execution relies
on: the test-gated merge flow with the `omsp-tester` agent, the automated
release pipeline with standing human authorization (ADR-0002), the
`omsp-domain-engineer` agent for Horizon 2+ domain content, the formal
Sprint-6 closure record, and CI hygiene fixes.

This release contains no new maritime domain content and does not change
the authorized-use scope. It is not an authorized production release and
grants no production deployment, unrestricted external publication,
autonomous operational authority, certification or automatic residual-risk
acceptance.

## Notable Outcomes

- test-gated merge flow delegated by the human (#212): `omsp-tester` issues
  evidence-based verdicts (`gate:tester-approved` / `gate:test-failed`),
  `omsp-cto` reviews TDD compliance (`gate:cto-approved`), and
  `approval-gate-merge.yml` merges automatically on green CI; issue status
  transitions are driven by `pr-testing-status.yml` (#215);
- ADR-0002 automated release pipeline: closing a SemVer release milestone
  (or a recorded human instruction via manual dispatch) triggers the
  mechanical CTO verification gate — full validator family, quality gate,
  changelog/release-notes version alignment — and publishes the pre-release
  automatically on GO, or opens a blocking issue on NO-GO
  (`governance/ADR-0002-AUTOMATED-RELEASE-PIPELINE.md`, WP-0090, #214);
- `omsp-domain-engineer` agent added as the program's domain-content author
  for Horizon 2+ (maritime ontology, MODS-layer content, Hanse 460 VDM
  content, diagram sources, scenarios), with
  `governance/AI_GOVERNANCE.md` aligned to the five-agent architecture
  (#218, #219);
- Sprint-6 formally closed per Engineering Playbook §9.3–§9.4: roadmap
  closure record (7/7 Work Packages delivered, `v0.5.1` published, milestone
  closed) and working-agreement status alignment (#222, #223);
- CI hygiene: three broken workflow stubs without a `jobs` key removed
  (#216, #217).

## Verification Evidence

Collected on the final `v0.5.2` state of `develop`; the publishing pipeline
run appends its own machine-produced verification record to the GitHub
Release:

- `omsp_validate.py` on all governed paths (including canon, docs,
  templates): **0 findings**;
- quality gate: **6/6 checks passed**;
- all seven `validate_*.py` domain validators pass;
- `CHANGELOG.md` and `RELEASE_NOTES.md` aligned to `v0.5.2`.

## Compatibility and Usage

Tooling continues to target Python 3.12 in CI with standard-library
dependencies only. Governed Markdown metadata, JSON profiles and registries
remain the primary interfaces. Consumers must preserve artifact identity,
lifecycle status, provenance and approval evidence; removed legacy paths are
recorded in `governance/canonical-authorities.json` under
`removed_legacy_paths` and must not be referenced.

## Approval Boundary

The accountable approval for `v0.5.2` permits controlled pre-production and
pilot evaluation only. The following remain separately governed decisions:

- production deployment;
- unrestricted external publication;
- residual-risk acceptance;
- operational use against a physical vessel;
- certification, regulatory acceptance or seaworthiness claims;
- autonomous or safety-critical control authority.

Automation and AI assistance may produce evidence and recommendations but
cannot originate these decisions (`governance/AI_GOVERNANCE.md`). The
automated release pipeline operates strictly within the pre-release class
under ADR-0002; declaring a production release remains a direct human act.

## Known Limitations

Unchanged from `v0.5.1`. Deferred capabilities carry recorded re-entry
triggers (`planning/WP-0075-DOMAIN-BACKLOG-REBASELINE.md` §8):

- production environment approval and deployment controls;
- signed provenance, attestations and cryptographically signed audit
  evidence;
- remote telemetry, alert delivery, paging and long-term evidence storage;
- vulnerability-database intelligence and repository-history secret
  scanning;
- performance, capacity, availability and endurance qualification;
- external backup infrastructure and disaster-recovery validation.

Persistent risks `RR-001` through `RR-005` remain open; reassessment is
scheduled against design-partner pilot evidence (Sprint-12, epic #176).
Maritime domain content (ontology concepts, vessel YAML models, scenarios,
rendered outputs) is defined but not yet implemented — that is the Sprint
7–9 scope.

## Sprint-7 Direction

Sprint-7 (epic #171, milestone v0.6.0) builds the maritime domain model
foundation:

- maritime core ontology v0.1 (WP-0077 / #198);
- vessel and equipment YAML schemas with mandatory provenance blocks
  (WP-0078 / #199);
- MODS Specification v0.1 skeleton with ODS-100/300 in Draft — the
  spec-first gate for all rendered content (WP-0079 / #200);
- domain validation rules and a compliant sample model package — the
  sprint's visible outcome (WP-0080 / #201).

Planned Sprint-7 work is not part of the delivered `v0.5.2` baseline until
implemented, reviewed and approved.

## Governed References

- GitHub Releases — release notes, baseline approval and readiness records per tag
- GitHub Projects, Issues and Milestones — sprint, Work Package and release tracking
- `governance/ADR-0002-AUTOMATED-RELEASE-PIPELINE.md`
- `planning/WP-0074-GOLDEN-PATH-DEFINITION.md`
- `planning/WP-0075-DOMAIN-BACKLOG-REBASELINE.md`
- `governance/CANONICAL_AUTHORITY_MAP.md`
- `governance/AI_GOVERNANCE.md`
