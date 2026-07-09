---
Artifact-ID: OMSP-STD-ARTIFACT-0001
Title: OMSP Engineering Artifact Standard
Version: 1.0.0
Status: Active
Owner: OMSP Engineering Council
Baseline: Sprint-1
Classification: Public
Related-Issue: WP-0014 / #36
---

# OMSP Engineering Artifact Standard

## 1. Purpose

This standard defines the lifecycle, identity, metadata, ownership, review, and status model for governed OMSP engineering artifacts.

It ensures that documents, models, standards, policies, charters, decision records, baselines, and release artifacts can be consistently identified, reviewed, versioned, maintained, and reused across OMSP repositories.

## 2. Scope

This standard applies to governed engineering artifacts in OMSP Foundation repositories, including:

- governance documents;
- engineering standards;
- architecture documents;
- lifecycle models;
- decision records;
- baseline notes;
- release notes;
- repository procedures;
- templates;
- long-lived technical documentation.

This standard does not apply to temporary notes, scratch files, generated build output, or implementation source files unless a repository-specific rule explicitly classifies them as governed artifacts.

## 3. Artifact Definition

An OMSP engineering artifact is a durable repository object that records a decision, standard, model, process, baseline, release, architecture, or other reusable engineering knowledge.

A governed artifact must be:

- discoverable in the repository;
- owned by an accountable role or body;
- identifiable by a stable Artifact ID;
- versioned when materially changed;
- reviewable through normal engineering workflow;
- traceable to issue, PR, baseline, or release context where applicable.

## 4. Artifact Lifecycle Model

Governed artifacts follow this lifecycle:

```text
Proposed
  ↓
Draft
  ↓
Review
  ↓
Active
  ↓
Superseded / Deprecated / Retired
```

### 4.1 Proposed

The artifact need has been identified, but the artifact may not exist yet. Proposed artifacts should be tracked through an issue or Work Package.

### 4.2 Draft

The artifact exists but is not authoritative. Draft artifacts may be incomplete and must not be used as final governance authority unless explicitly stated.

### 4.3 Review

The artifact is ready for structured review. Review must check completeness, consistency, ownership, metadata, and impact on existing governance or engineering artifacts.

### 4.4 Active

The artifact is approved for use and may be referenced as authoritative within its scope.

### 4.5 Superseded

The artifact has been replaced by a newer artifact or version. It is preserved for history but should not be used for new work.

### 4.6 Deprecated

The artifact remains available but is no longer recommended for new work. A replacement path should be identified where practical.

### 4.7 Retired

The artifact is no longer in use and has no active replacement requirement. Retired artifacts should be clearly marked and retained only where useful for traceability.

## 5. Artifact Status Model

The `Status` metadata field must use one of the following values:

| Status | Meaning | May be authoritative? |
| --- | --- | --- |
| Proposed | Need identified; artifact may not exist or may be planned. | No |
| Draft | Artifact exists but is incomplete or unapproved. | No |
| Review | Artifact is ready for formal review. | No |
| Active | Artifact is approved for current use. | Yes |
| Superseded | Artifact has been replaced by a newer artifact or version. | No for new work |
| Deprecated | Artifact is discouraged for new work but retained temporarily. | Limited |
| Retired | Artifact is no longer used. | No |

Status changes require review when the artifact is governed.

## 6. Required Metadata

Every governed artifact must begin with YAML front matter unless a repository-specific format makes that impossible.

Required metadata fields:

```yaml
---
Artifact-ID: OMSP-<DOMAIN>-<TYPE>-<NUMBER>
Title: Human-readable artifact title
Version: MAJOR.MINOR.PATCH
Status: Draft | Review | Active | Superseded | Deprecated | Retired
Owner: Accountable role or body
Baseline: Sprint, baseline, or release context
Classification: Public | Internal | Restricted
Related-Issue: Work Package or issue reference
---
```

### 6.1 Artifact-ID

A stable identifier that does not change when the file is renamed.

### 6.2 Title

A human-readable title that matches the artifact purpose.

### 6.3 Version

Semantic artifact version in `MAJOR.MINOR.PATCH` form.

### 6.4 Status

Current lifecycle status from the approved status model.

### 6.5 Owner

The accountable human role, council, program function, or governance body.

### 6.6 Baseline

The baseline, sprint, or release context where the artifact became authoritative or was last materially updated.

### 6.7 Classification

Visibility and handling classification. Allowed values are:

- `Public`
- `Internal`
- `Restricted`

### 6.8 Related-Issue

The issue, Work Package, or change request that created or materially updated the artifact.

## 7. Optional Metadata

Artifacts may include optional metadata when useful:

```yaml
Supersedes: OMSP-<DOMAIN>-<TYPE>-<NUMBER>
Superseded-By: OMSP-<DOMAIN>-<TYPE>-<NUMBER>
Reviewers: Role or team list
Approver: Human approver or governance body
Effective-Date: YYYY-MM-DD
Review-Cadence: Quarterly | Semiannual | Annual | On-change
Repository-Scope: Single-repo | Multi-repo | Foundation-wide
Tags: [governance, architecture, standard]
```

Optional fields must not conflict with required fields.

## 8. Artifact ID Convention

Artifact IDs must follow this pattern:

```text
OMSP-<DOMAIN>-<TYPE>-<NUMBER>
```

### 8.1 Domain Segment

The domain segment identifies the artifact family.

Recommended domains:

| Domain | Meaning |
| --- | --- |
| `GOV` | Governance artifacts |
| `STD` | Standards |
| `ARCH` | Architecture artifacts |
| `ADR` | Architecture or decision records |
| `BLN` | Baseline artifacts |
| `REL` | Release artifacts |
| `TPL` | Templates |
| `OPS` | Operational procedures |

### 8.2 Type Segment

The type segment identifies the artifact type in short uppercase form.

Examples:

```text
CONSTITUTION
PROGRAM-CHARTER
ENGINEERING-COUNCIL
MODEL
PLAYBOOK
ARTIFACT
DECISION-REVIEW
BASELINE-NOTE
RELEASE-NOTE
```

### 8.3 Number Segment

The number segment must be a zero-padded numeric identifier.

Examples:

```text
OMSP-GOV-CONSTITUTION-0001
OMSP-STD-ARTIFACT-0001
OMSP-ARCH-CONTEXT-0001
OMSP-ADR-DECISION-0001
OMSP-BLN-SPRINT-0001
```

Artifact IDs should not be reused for unrelated artifacts.

## 9. Versioning Rules

Artifacts use semantic versioning.

- Increment `MAJOR` for breaking governance, lifecycle, authority, or compatibility changes.
- Increment `MINOR` for material additions that preserve the existing model.
- Increment `PATCH` for editorial corrections, clarifications, or non-material fixes.

Version changes must be included in the same PR as the material artifact change.

## 10. Ownership Rules

Every governed artifact must have an accountable owner.

Owners are responsible for:

- artifact accuracy;
- lifecycle status;
- review readiness;
- consistency with related artifacts;
- responding to requested changes;
- initiating updates when the artifact becomes stale.

Ownership may be assigned to a role or governance body rather than a named individual.

## 11. Review Rules

Governed artifacts must be reviewed before becoming Active.

Artifact review must check:

- required metadata is present;
- Artifact ID follows convention;
- lifecycle status is correct;
- owner is clear;
- content is complete enough for intended use;
- related artifacts are consistent;
- baseline or release impact is identified;
- AI-generated content, if used, is reviewed by an accountable human.

## 12. Traceability Rules

Material artifact changes must be traceable through:

```text
Issue → Branch → Commit → Pull Request → Review → Merge → Baseline/Release when applicable
```

Artifacts should reference the relevant Work Package or issue in `Related-Issue` metadata.

PR descriptions should list changed governed artifacts and summarize artifact lifecycle or status changes.

## 13. File Naming Rules

Governed artifact filenames should be uppercase with underscores and a `.md` extension when written in Markdown.

Examples:

```text
governance/CONSTITUTION.md
governance/ENGINEERING_PLAYBOOK.md
governance/ENGINEERING_ARTIFACT_STANDARD.md
governance/DECISION_AND_REVIEW_POLICY.md
```

Repository-specific artifacts may use paths such as:

```text
architecture/SYSTEM_CONTEXT.md
decisions/ADR-0001-architecture-boundary.md
releases/RELEASE_NOTES_v0.1.0.md
baselines/SPRINT_1_BASELINE.md
```

## 14. Cross-Repository Use

This standard is intended for all future OMSP repositories.

Repositories may extend the standard with local rules, but must preserve:

- stable Artifact ID;
- required metadata;
- lifecycle status model;
- owner and review rules;
- traceability expectations.

Extensions must not weaken governance requirements without an approved exception.

## 15. AI Assisted Artifact Work

AI may assist by:

- drafting artifact content;
- proposing metadata;
- checking consistency;
- identifying missing sections;
- preparing review checklists;
- summarizing changes.

AI must not:

- approve artifacts;
- assign final authoritative status without human review;
- invent validation evidence;
- silently change artifact ownership;
- override governance or review rules.

## 16. Compliance Checklist

Before a governed artifact becomes Active, confirm:

- [ ] Required metadata is present.
- [ ] Artifact ID follows the convention.
- [ ] Version is valid.
- [ ] Status is valid.
- [ ] Owner is clear.
- [ ] Related issue or Work Package is referenced.
- [ ] Review path is complete.
- [ ] Baseline or release impact is documented if applicable.
- [ ] AI involvement, if any, remains advisory.

## 17. Maintenance

This standard is maintained by the OMSP Engineering Council.

Material updates require:

- issue-backed Work Package;
- feature branch;
- pull request into the appropriate target branch;
- governance or engineering review;
- version metadata update;
- baseline update when applicable.
