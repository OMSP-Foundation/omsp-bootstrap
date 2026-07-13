---
Artifact-ID: OMSP-GOV-AUTHORITY-MAP-0001
Title: Canonical Authority Map
Version: 1.1.0
Status: Active
Owner: OMSP Engineering Council
Review-Cycle: Each baseline
Traceability:
  - WP-0057
  - ISSUE-91
  - WP-0072
  - ISSUE-166
---

# Canonical Authority Map

## Purpose

This map identifies the sole authoritative artifact for each governed standard or policy domain, and records the governed removal of retired legacy paths.

Authority is determined first by stable Artifact ID, then by the canonical repository path. Compatibility stubs have no independent normative authority.

## Authority Registry

| Authority domain | Canonical Artifact ID | Canonical path | Removed legacy paths | Disposition |
| --- | --- | --- | --- | --- |
| Engineering artifact lifecycle, identity and governance | `OMSP-STD-ARTIFACT-0001` | `governance/ENGINEERING_ARTIFACT_STANDARD.md` | `foundation/ENGINEERING_ARTIFACT_STANDARD.md` | Stub removed in WP-0072 (#166); removal review was overdue since Sprint-4 |
| Metadata and traceability | `OMSP-STD-METADATA-TRACEABILITY-0001` | `governance/METADATA_AND_TRACEABILITY_STANDARD.md` | `foundation/METADATA_STANDARD.md`; `foundation/TRACEABILITY_STANDARD.md` | Stubs removed in WP-0072 (#166) |
| Decision and review governance | `OMSP-GOV-DECISION-REVIEW-0001` | `governance/DECISION_AND_REVIEW_POLICY.md` | `governance/DECISION_POLICY.md`; `governance/REVIEW_POLICY.md` | Stubs removed in WP-0072 (#166) |
| Engineering lifecycle policies (branching, sprint, Work Package, baseline, definition of done, pull request, release, contribution) | `OMSP-GOV-PLAYBOOK-0001` | `governance/ENGINEERING_PLAYBOOK.md` §5–§11 | `governance/BRANCHING_STRATEGY.md`; `governance/SPRINT_POLICY.md`; `governance/WORK_PACKAGE_LIFECYCLE.md`; `governance/BASELINE_MANAGEMENT.md`; `governance/DEFINITION_OF_DONE.md`; `governance/PULL_REQUEST_POLICY.md`; `governance/RELEASE_POLICY.md`; `governance/CONTRIBUTION_WORKFLOW.md` | Thin duplicates merged into the Playbook and removed in WP-0072 (#166) |
| Platform engine definitions | `OMSP-ARCH-PLATFORM-0001` | `architecture/PLATFORM_ARCHITECTURE.md` (with the engine artifacts in `architecture/`) | `platform/ENGINEERING_KERNEL.md`; `platform/KNOWLEDGE_ENGINE.md`; `platform/PUBLICATION_ENGINE.md`; `platform/TRACEABILITY_ENGINE.md` | Bootstrap stubs and the `platform/` directory removed in WP-0072 (#166) |

Relocation record: `foundation/AI_GOVERNANCE.md` moved to
`governance/AI_GOVERNANCE.md` (`OMSP-GOV-AI-GOVERNANCE-0001`, Draft) in
WP-0072; consolidation is WP-0073 (#167). With this, the `foundation/`
directory was retired.

## Precedence Rules

1. A canonical Artifact ID is the primary authority identifier.
2. The canonical path in this registry is the repository location for the authoritative content.
3. A compatibility stub with `Status: Superseded` cannot define, amend or override normative requirements.
4. New artifacts and references must use the canonical Artifact ID and canonical path.
5. A path move does not change authority when the canonical Artifact ID is preserved and this map is updated through governance review.
6. Two artifacts may not both claim `Status: Active` for the same authority domain.

## Migration Rules

- Existing inbound references should be migrated when touched.
- New references to removed legacy paths are prohibited; reference the canonical path (and section, where given) instead.
- Legacy stubs were removed in WP-0072 (#166) after repository-wide reference migration and an accountable governance decision (2026-07-13); removed paths remain recorded here and in `canonical-authorities.json` (`removed_legacy_paths`) for provenance.
- Any future compatibility stub must carry `Status: Superseded`, `Superseded-By`, and `Canonical-Path` metadata, and may be removed only through the same governed process.

## Validation Contract

Repository validation must fail when:

- more than one active Artifact ID is registered for one authority domain;
- a canonical path is missing;
- a registered legacy stub exists without `Superseded-By` and `Canonical-Path` metadata;
- this map and the machine-readable authority registry diverge.

## Human Approval Boundary

Automation may detect conflicts and produce evidence. It cannot approve authority changes. Any change to canonical authority requires accountable human governance review.
