---
Artifact-ID: OMSP-STD-METADATA-TRACEABILITY-0001
Title: OMSP Metadata and Traceability Standard
Version: 1.0.0
Status: Active
Owner: OMSP Engineering Council
Baseline: Sprint-1
Classification: Public
Related-Issue: WP-0015 / #37
---

# OMSP Metadata and Traceability Standard

## 1. Purpose

This standard defines the required metadata schema and traceability relation model for governed OMSP artifacts.

It ensures that every governed artifact can be consistently identified, owned, reviewed, versioned, and traced through issues, branches, commits, pull requests, baselines, and releases.

## 2. Scope

This standard applies to governed artifacts across OMSP Foundation repositories, including:

- governance documents;
- engineering standards;
- architecture documents;
- decision records;
- baseline notes;
- release notes;
- repository procedures;
- templates;
- long-lived technical documentation.

It complements the Engineering Artifact Standard by defining the machine-checkable metadata and traceability model in more detail.

## 3. Goals

The metadata and traceability model must support:

- stable artifact identity;
- explicit ownership;
- lifecycle and review visibility;
- relation mapping between artifacts and work items;
- machine-checkable validation;
- cross-repository reuse;
- baseline and release auditability.

## 4. Required Metadata Schema

Every governed Markdown artifact must begin with YAML front matter containing the required fields below.

```yaml
---
Artifact-ID: OMSP-<DOMAIN>-<TYPE>-<NUMBER>
Title: Human-readable title
Version: MAJOR.MINOR.PATCH
Status: Proposed | Draft | Review | Active | Superseded | Deprecated | Retired
Owner: Accountable role, council, program function, or governance body
Baseline: Sprint, baseline, release, or governing context
Classification: Public | Internal | Restricted
Related-Issue: WP-XXXX / #NN
---
```

### 4.1 Field Requirements

| Field | Required | Type | Machine-check rule |
| --- | --- | --- | --- |
| `Artifact-ID` | Yes | String | Must match `^OMSP-[A-Z0-9]+-[A-Z0-9-]+-[0-9]{4}$` |
| `Title` | Yes | String | Must be non-empty |
| `Version` | Yes | SemVer string | Must match `^[0-9]+\.[0-9]+\.[0-9]+$` |
| `Status` | Yes | Enum | Must be an allowed lifecycle status |
| `Owner` | Yes | String | Must be non-empty and name a role/body |
| `Baseline` | Yes | String | Must be non-empty |
| `Classification` | Yes | Enum | Must be `Public`, `Internal`, or `Restricted` |
| `Related-Issue` | Yes | String | Must reference issue, Work Package, or change request |

## 5. Optional Metadata Schema

Optional fields may be added when useful.

```yaml
Supersedes: OMSP-<DOMAIN>-<TYPE>-<NUMBER>
Superseded-By: OMSP-<DOMAIN>-<TYPE>-<NUMBER>
Depends-On: [OMSP-<DOMAIN>-<TYPE>-<NUMBER>]
Related-Artifacts: [OMSP-<DOMAIN>-<TYPE>-<NUMBER>]
Reviewers: [role-or-team]
Approver: human approver or governance body
Effective-Date: YYYY-MM-DD
Review-Cadence: Quarterly | Semiannual | Annual | On-change
Repository-Scope: Single-repo | Multi-repo | Foundation-wide
Tags: [governance, standard]
Traceability: URI or path to traceability matrix
```

### 5.1 Optional Field Rules

| Field | Type | Machine-check rule |
| --- | --- | --- |
| `Supersedes` | Artifact ID | Must match Artifact-ID pattern |
| `Superseded-By` | Artifact ID | Must match Artifact-ID pattern |
| `Depends-On` | List of Artifact IDs | Each entry must match Artifact-ID pattern |
| `Related-Artifacts` | List of Artifact IDs | Each entry must match Artifact-ID pattern |
| `Reviewers` | List | Must be non-empty when present |
| `Approver` | String | Must not be AI-only for Active artifacts |
| `Effective-Date` | Date | Must match `YYYY-MM-DD` |
| `Review-Cadence` | Enum | Must be one of allowed cadence values |
| `Repository-Scope` | Enum | Must be one of allowed scope values |
| `Tags` | List | Values should be lowercase kebab-case |
| `Traceability` | String | Should point to an artifact, file, or section |

## 6. Metadata Status Rules

The `Status` field controls artifact authority.

| Status | Meaning | Required review state |
| --- | --- | --- |
| Proposed | Need is identified; artifact may not exist yet. | Issue or backlog reference |
| Draft | Artifact exists but is not authoritative. | Author self-check |
| Review | Artifact is ready for structured review. | Reviewer evaluation pending |
| Active | Artifact is approved for current use. | Required review complete |
| Superseded | Artifact replaced by a newer artifact or version. | Replacement linked |
| Deprecated | Artifact retained but discouraged for new work. | Deprecation rationale documented |
| Retired | Artifact is no longer used. | Retirement rationale documented |

A governed artifact must not move to `Active` without human review.

## 7. Traceability Relation Model

OMSP uses typed traceability relations so dependencies and evidence can be checked consistently.

Relation records should use this shape:

```yaml
source: OMSP-<DOMAIN>-<TYPE>-<NUMBER> | issue:#NN | pr:#NN | commit:<sha> | branch:<name> | file:<path>
relation: satisfies | implements | updates | supersedes | depends-on | reviews | approves | validates | releases | baselines | documents | traces-to
target: OMSP-<DOMAIN>-<TYPE>-<NUMBER> | issue:#NN | pr:#NN | commit:<sha> | branch:<name> | file:<path> | baseline:<id> | release:<id>
evidence: URL, path, PR number, review ID, or commit SHA
status: proposed | active | superseded | deprecated
```

### 7.1 Relation Types

| Relation | Meaning | Typical source → target |
| --- | --- | --- |
| `satisfies` | Work satisfies an acceptance criterion or issue. | PR → issue |
| `implements` | Change implements an artifact, decision, or requirement. | commit/PR → artifact |
| `updates` | Change modifies an existing artifact. | PR → artifact |
| `supersedes` | Artifact replaces another artifact. | artifact → artifact |
| `depends-on` | Artifact or work requires another artifact or work item. | artifact/issue → artifact/issue |
| `reviews` | Review evaluates a work item or artifact. | review → PR/artifact |
| `approves` | Human authority approves a decision, baseline, or release. | approver/review → baseline/release |
| `validates` | Evidence validates a requirement or artifact. | check/test/review → artifact/PR |
| `releases` | Release includes or publishes a change. | release → PR/artifact |
| `baselines` | Baseline includes an artifact or change. | baseline → artifact/PR |
| `documents` | Artifact documents a decision, process, or model. | artifact → decision/model |
| `traces-to` | General traceability link where no narrower relation applies. | any → any |

### 7.2 Entity Reference Format

Machine-checkable relation references should use these prefixes:

| Prefix | Example |
| --- | --- |
| `issue:` | `issue:#37` |
| `pr:` | `pr:#46` |
| `commit:` | `commit:2ad9cc5` |
| `branch:` | `branch:feature/wp-0015-metadata-traceability-v1` |
| `file:` | `file:governance/METADATA_AND_TRACEABILITY_STANDARD.md` |
| `baseline:` | `baseline:Sprint-1` |
| `release:` | `release:v0.1.0-bootstrap` |
| Artifact ID | `OMSP-STD-METADATA-TRACEABILITY-0001` |

## 8. Required Traceability Chain

Material work must preserve this minimum chain:

```text
Issue → Branch → Commit → Pull Request → Review → Merge → Baseline/Release when applicable
```

For governed artifacts, the artifact must also trace to:

```text
Artifact → Owner → Review → Baseline/Release context
```

## 9. Example Traceability Matrix

| Source | Relation | Target | Evidence | Status |
| --- | --- | --- | --- | --- |
| `branch:feature/wp-0015-metadata-traceability-v1` | `implements` | `issue:#37` | GitHub branch | active |
| `file:governance/METADATA_AND_TRACEABILITY_STANDARD.md` | `documents` | `issue:#37` | PR description | active |
| `OMSP-STD-METADATA-TRACEABILITY-0001` | `depends-on` | `OMSP-STD-ARTIFACT-0001` | Engineering Artifact Standard | active |
| `pr:#<TBD>` | `satisfies` | `issue:#37` | PR acceptance checklist | proposed |
| `review:#<TBD>` | `reviews` | `pr:#<TBD>` | GitHub review | proposed |
| `baseline:Sprint-1` | `baselines` | `OMSP-STD-METADATA-TRACEABILITY-0001` | Sprint-1 baseline notes | proposed |

## 10. Machine-Checkable Validation Rules

A repository validator should be able to check:

- required metadata fields exist;
- `Artifact-ID` matches the required pattern;
- `Version` is SemVer-compatible;
- `Status` is an allowed value;
- `Classification` is an allowed value;
- required issue references exist in `Related-Issue`;
- relation records use allowed relation names;
- relation entity references use known prefixes or valid Artifact IDs;
- Active artifacts do not name AI as the sole approver;
- superseded artifacts identify a replacement where practical.

## 11. Ownership and Review Traceability

Ownership must be traceable from metadata and review records.

For Active artifacts:

- `Owner` must name a role or body accountable for maintenance.
- PR review must show that the artifact was reviewed before activation.
- Baseline or release context must be recorded in `Baseline`.
- Follow-up risks must be captured as issues or traceability records.

## 12. Cross-Repository Traceability

For cross-repository relations, entity references should include repository context when needed.

Recommended form:

```text
repo:<owner>/<repo>#issue:<number>
repo:<owner>/<repo>#pr:<number>
repo:<owner>/<repo>#file:<path>
```

Example:

```text
repo:OMSP-Foundation/omsp-bootstrap#issue:37
repo:OMSP-Foundation/omsp-bootstrap#file:governance/METADATA_AND_TRACEABILITY_STANDARD.md
```

## 13. AI Assisted Metadata and Traceability

AI may assist by:

- proposing metadata;
- generating traceability matrices;
- detecting missing links;
- checking schema consistency;
- summarizing relation evidence.

AI must not:

- approve traceability evidence;
- invent issue, PR, commit, baseline, or release references;
- mark artifacts Active without human review;
- override ownership or approval authority.

## 14. Compliance Checklist

Before merging a material artifact change, confirm:

- [ ] Required metadata fields are present.
- [ ] Artifact ID follows the pattern.
- [ ] Status is valid.
- [ ] Owner is clear.
- [ ] Related issue or Work Package is referenced.
- [ ] Traceability chain is preserved.
- [ ] Required relation records are machine-checkable where used.
- [ ] Review and approval authority are human-accountable.
- [ ] Baseline or release impact is documented if applicable.

## 15. Maintenance

This standard is maintained by the OMSP Engineering Council.

Material changes require:

- issue-backed Work Package;
- feature branch;
- pull request into the appropriate target branch;
- review for schema and traceability consistency;
- version metadata update;
- baseline update when applicable.
