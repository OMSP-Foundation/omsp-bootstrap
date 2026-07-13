# OMSP Foundation Release Notes — v0.5.1

**Release date:** 2026-07-13
**Classification:** Clean Baseline (Production Baseline Candidate lineage)
**Approval status:** Prepared; GitHub Release publication pending accountable human approval
**Authorized scope:** Controlled pre-production and pilot evaluation

## Overview

`v0.5.1` closes Sprint-6 and delivers the post-audit clean baseline: a
reconciled, self-consistent repository reoriented from governance growth to
maritime domain content. Following a full technical audit, the sprint
resolved the Work Package numbering collision, superseded the conflicting
pilot-readiness plan in favor of the official product-reorientation roadmap
(issue #145), rationalized 25 stub and duplicate artifacts, consolidated
lifecycle policy authority into the Engineering Playbook, and established
the product foundations for Sprint 7–9: the canonical engineering
methodology inventory, the spec-first MODS documentation product stack, the
Hanse 460 golden-path definition, and an implementation-ready Sprint 7–14
backlog.

This baseline contains no new maritime domain content yet — it is the
verified, planned starting line for it. It is not an authorized production
release and grants no production deployment, unrestricted external
publication, autonomous operational authority, certification or automatic
residual-risk acceptance.

## Notable Outcomes

- audit reconciliation: 16 findings dispositioned with direct evidence
  (`planning/WP-0070-AUDIT-DISPOSITION.md`); Work Package collision resolved
  (WP-0070…0076 renumbering; WP-0060–0068 retired);
- repository rationalization: `foundation/` and `platform/` directories
  retired, eight thin lifecycle mini-policies merged into the Engineering
  Playbook, canonical authority registry extended to five domains with
  removed-legacy-path provenance; stub ratio reduced from ~29.7% to ~17.2%;
- governed artifact templates (requirement, risk, validation record, ADR,
  Work Package) filled and activated — the spec-first workflow precondition;
- canonical AI governance (`governance/AI_GOVERNANCE.md`): permitted and
  prohibited AI roles, eight mandatory human approval gates, provenance and
  attribution rules, runtime boundary;
- ADR-0001: monorepo topology with trigger-based re-evaluation;
- canonical engineering methodology inventory in canon
  (`canon/ENGINEERING_METHODOLOGY.md`);
- Hanse 460 golden-path product definition: users, provenance-bound inputs,
  electrical-slice model boundary, validator evidence contract, advisory
  output specification, five-minute demo storyboard
  (`planning/WP-0074-GOLDEN-PATH-DEFINITION.md`);
- Sprint 7–14 product-led backlog: epic exit criteria, WP-0077…WP-0089
  breakdown (issues #198–#210), capacity policy, deferred-governance
  triggers, measurable release gates
  (`planning/WP-0075-DOMAIN-BACKLOG-REBASELINE.md`).

## Verification Evidence

Collected on the final Sprint-6 baseline state:

- `omsp_validate.py` on all governed paths (including canon, docs,
  templates): **0 findings**;
- quality gate: **6/6 checks passed**;
- canonical authority validation: **5 domains passed**, no duplicate active
  authority;
- all seven `validate_*.py` domain validators pass;
- Sprint-6 Work Packages WP-0070…WP-0076 delivered through reviewed pull
  requests #192–#197 plus the v0.5.1 readiness package.

## Compatibility and Usage

Tooling continues to target Python 3.12 in CI with standard-library
dependencies only. Governed Markdown metadata, JSON profiles and registries
remain the primary interfaces. Consumers must preserve artifact identity,
lifecycle status, provenance and approval evidence; removed legacy paths are
recorded in `governance/canonical-authorities.json` under
`removed_legacy_paths` and must not be referenced.

## Approval Boundary

The accountable approval for `v0.5.1` permits controlled pre-production and
pilot evaluation only. The following remain separately governed decisions:

- production deployment;
- unrestricted external publication;
- residual-risk acceptance;
- operational use against a physical vessel;
- certification, regulatory acceptance or seaworthiness claims;
- autonomous or safety-critical control authority.

Automation and AI assistance may produce evidence and recommendations but
cannot originate these decisions (`governance/AI_GOVERNANCE.md`).

## Known Limitations

Deferred capabilities carry recorded re-entry triggers
(`planning/WP-0075-DOMAIN-BACKLOG-REBASELINE.md` §8):

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

Planned Sprint-7 work is not part of the delivered `v0.5.1` baseline until
implemented, reviewed and approved.

## Governed References

- GitHub Releases — release notes, baseline approval and readiness records per tag
- GitHub Projects, Issues and Milestones — sprint, Work Package and release tracking
- `planning/WP-0070-AUDIT-DISPOSITION.md`
- `planning/WP-0074-GOLDEN-PATH-DEFINITION.md`
- `planning/WP-0075-DOMAIN-BACKLOG-REBASELINE.md`
- `governance/CANONICAL_AUTHORITY_MAP.md`
- `governance/AI_GOVERNANCE.md`
