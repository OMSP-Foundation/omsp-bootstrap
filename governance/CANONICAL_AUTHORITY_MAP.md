---
Artifact-ID: OMSP-GOV-AUTHORITY-MAP-0001
Version: 1.0.0
Status: Active
Owner: OMSP Engineering Council
Review-Cycle: Each baseline
Traceability:
  - WP-0057
  - ISSUE-91
---

# Canonical Authority Map

## Purpose

This map identifies the sole authoritative artifact for each governed standard or policy domain where legacy Sprint-0 placeholders still exist.

Authority is determined first by stable Artifact ID, then by the canonical repository path. Compatibility stubs have no independent normative authority.

## Authority Registry

| Authority domain | Canonical Artifact ID | Canonical path | Legacy compatibility paths | Disposition |
| --- | --- | --- | --- | --- |
| Engineering artifact lifecycle, identity and governance | `OMSP-STD-ARTIFACT-0001` | `governance/ENGINEERING_ARTIFACT_STANDARD.md` | `foundation/ENGINEERING_ARTIFACT_STANDARD.md` | Superseded stub; removal review Sprint-4 |
| Metadata and traceability | `OMSP-STD-METADATA-TRACEABILITY-0001` | `governance/METADATA_AND_TRACEABILITY_STANDARD.md` | `foundation/METADATA_STANDARD.md`; `foundation/TRACEABILITY_STANDARD.md` | Superseded stubs; removal review Sprint-4 |
| Decision and review governance | `OMSP-GOV-DECISION-REVIEW-0001` | `governance/DECISION_AND_REVIEW_POLICY.md` | `governance/DECISION_POLICY.md`; `governance/REVIEW_POLICY.md` | Superseded stubs; removal review Sprint-4 |

## Precedence Rules

1. A canonical Artifact ID is the primary authority identifier.
2. The canonical path in this registry is the repository location for the authoritative content.
3. A compatibility stub with `Status: Superseded` cannot define, amend or override normative requirements.
4. New artifacts and references must use the canonical Artifact ID and canonical path.
5. A path move does not change authority when the canonical Artifact ID is preserved and this map is updated through governance review.
6. Two artifacts may not both claim `Status: Active` for the same authority domain.

## Migration Rules

- Existing inbound references should be migrated when touched.
- New references to compatibility paths are prohibited.
- Compatibility stubs remain only to preserve old links and provenance.
- Removal requires repository-wide link validation and an accountable governance decision.

## Validation Contract

Repository validation must fail when:

- more than one active Artifact ID is registered for one authority domain;
- a compatibility entry is not marked `Superseded`;
- a canonical path is missing;
- a legacy stub lacks `Superseded-By` and `Canonical-Path` metadata;
- this map and the machine-readable authority registry diverge.

## Human Approval Boundary

Automation may detect conflicts and produce evidence. It cannot approve authority changes. Any change to canonical authority requires accountable human governance review.
