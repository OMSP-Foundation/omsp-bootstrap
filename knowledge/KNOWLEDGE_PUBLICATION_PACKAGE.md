---
Artifact-ID: OMSP-KNOWLEDGE-PUBLICATION-0001
Title: OMSP Knowledge Publication Package
Version: 1.0.0
Status: Review
Owner: OMSP Engineering Council
Baseline: Sprint-3
Classification: Public
Related-Issue: WP-0035 / #69
Depends-On:
  - OMSP-KNOWLEDGE-REGISTRY-0001
  - OMSP-KNOWLEDGE-AI-PROCESSING-0001
  - OMSP-PUBLICATION-WORKFLOW-0001
---

# OMSP Knowledge Publication Package

## 1. Purpose

This artifact defines the governed structure and publication rules for packaging OMSP knowledge artifacts for downstream consumption. A knowledge publication package is a reproducible, traceable and versioned collection assembled only from governed sources.

## 2. Publication Principles

A publication package must:

- preserve the identity, version and lifecycle status of every included artifact;
- distinguish draft or review material from approved baseline or release content;
- record the exact source revision used to assemble the package;
- include dependency and provenance information;
- be reproducible from its manifest;
- never create new governance authority by packaging content;
- require accountable human approval before being represented as approved or released.

## 3. Package Classes

| Class | Meaning | Authority |
| --- | --- | --- |
| Preview | Non-authoritative package for review or testing | No baseline or release authority |
| Baseline Candidate | Proposed package assembled for baseline review | Requires human baseline approval |
| Baseline | Approved snapshot of governed knowledge | Human-approved baseline authority |
| Release Candidate | Proposed externally consumable package | Requires release review |
| Release | Approved and versioned publication | Human-approved release authority |
| Deprecated | Published package retained for compatibility but discouraged | Replacement should be identified |
| Retired | Package no longer supported for normal use | Historical access only |

Automation may assemble Preview, Baseline Candidate and Release Candidate packages. It may not promote them to Baseline or Release.

## 4. Package Manifest

Each package must contain a manifest with these required fields:

```yaml
package_id: OMSP-PACKAGE-<NAME>-<VERSION>
title: Human-readable package title
package_version: MAJOR.MINOR.PATCH
package_class: preview | baseline-candidate | baseline | release-candidate | release | deprecated | retired
created_at: ISO-8601 timestamp
created_by: accountable actor or automation identity
source_repository: owner/repository
source_ref: branch, tag or immutable commit SHA
source_commit: full commit SHA
baseline: baseline identifier or null
release: release identifier or null
approval_evidence: human approval reference or null
artifacts: []
dependencies: []
validation: []
```

## 5. Artifact Entries

Every included artifact entry must record:

```yaml
artifact_id: OMSP-<DOMAIN>-<TYPE>-<NUMBER>
version: MAJOR.MINOR.PATCH
status: Proposed | Draft | Review | Active | Superseded | Deprecated | Retired
path: repository-relative path
content_digest: sha256:<digest>
registry_record: registry reference
provenance: source commit or immutable source reference
included_as: normative | informative | example | compatibility
```

Artifact identity must be taken from the governed source and must not be generated or rewritten by the packaging process.

## 6. Inclusion Rules

### 6.1 Approved Packages

A Baseline or Release package may include normative artifacts only when:

- the artifact has stable identity and valid metadata;
- the artifact is `Active`, `Superseded`, `Deprecated` or `Retired` according to package purpose;
- its source revision is immutable and recorded;
- required dependencies are present or explicitly declared external;
- its approval and baseline context are traceable;
- package validation has completed successfully;
- accountable human approval evidence exists.

Draft, Proposed and Review artifacts must not be represented as approved normative content.

### 6.2 Preview Packages

Preview packages may include Draft or Review artifacts when:

- the package class is clearly `preview`;
- each non-active artifact retains its source lifecycle status;
- consumer guidance states that the package is non-authoritative;
- no baseline or release claim is made.

## 7. Dependency Rules

Dependencies are classified as:

- `embedded`: included within the package;
- `external-required`: required but resolved outside the package;
- `external-optional`: optional consumer dependency;
- `governance`: controlling standard, policy or approval artifact;
- `historical`: retained for traceability or migration.

Each dependency must record its identifier, version or revision, relation type and resolution location. Missing required dependencies invalidate approved package publication.

## 8. Reproducibility

A package is reproducible when another authorized process can:

1. retrieve the recorded source repository and immutable source commit;
2. resolve the exact artifact set from the manifest;
3. verify each content digest;
4. resolve embedded and external dependencies;
5. run the declared validation set;
6. produce an equivalent manifest and content set.

Build timestamps, archive ordering or transport metadata may differ without changing package equivalence. Artifact content, identity, versions and dependency resolution must match.

## 9. Consumer Guidance

Every package must include consumer guidance stating:

- intended audience and use;
- package class and authority level;
- baseline and release status;
- included artifact categories;
- excluded or deferred content;
- dependency resolution instructions;
- compatibility and migration notes;
- known limitations;
- where to report defects or request changes.

Consumers must not infer operational certification, regulatory approval or safety authority from package publication.

## 10. Publication Workflow

```text
Governed source artifacts
  -> registry resolution
  -> dependency closure
  -> package manifest generation
  -> content digest generation
  -> structural and semantic validation
  -> Preview or Candidate package
  -> accountable human review
  -> Baseline or Release approval
  -> immutable publication reference
```

Failure at any validation or approval step must stop approved publication. A failed candidate may remain available as a clearly marked diagnostic artifact.

## 11. Validation Requirements

A future validator should check:

- required manifest fields exist;
- package and artifact versions are valid;
- source commit is immutable and resolvable;
- Artifact IDs are unique within the package;
- artifact metadata matches registry records;
- lifecycle states are preserved;
- all required dependencies resolve;
- content digests match;
- baseline and release claims have human approval evidence;
- preview content is not presented as approved;
- deprecated or retired packages identify status and replacement guidance where available.

## 12. Deprecation and Retirement

A package may be deprecated when a replacement exists or continued use is discouraged. Deprecation records must include:

- reason;
- effective date;
- replacement package when applicable;
- compatibility implications;
- migration guidance;
- accountable decision reference.

Retirement removes normal support but must preserve historical identity, provenance and audit access. Package identifiers must never be reused.

## 13. AI-Assisted Packaging

AI-assisted tools may:

- propose package composition;
- detect missing dependencies;
- generate draft manifests;
- summarize consumer guidance;
- identify lifecycle or provenance conflicts;
- propose compatibility notes.

AI-assisted tools must not:

- promote a package to Baseline or Release;
- invent approval evidence, source revisions or digests;
- change source lifecycle status during packaging;
- omit known conflicts or uncertainty;
- represent generated summaries as normative source content.

## 14. Example Manifest

```yaml
package_id: OMSP-PACKAGE-KNOWLEDGE-0.3.0
package_version: 0.3.0
package_class: release-candidate
source_repository: OMSP-Foundation/omsp-bootstrap
source_ref: develop
source_commit: <full-commit-sha>
baseline: Sprint-3-candidate
release: v0.3.0-foundation-sprint-3-rc1
approval_evidence: null
artifacts:
  - artifact_id: OMSP-KNOWLEDGE-GRAPH-0001
    version: 1.0.0
    status: Active
    path: knowledge/KNOWLEDGE_GRAPH_CONCEPTUAL_MODEL.md
    content_digest: sha256:<digest>
    included_as: normative
validation:
  - metadata-valid
  - dependency-closure-valid
  - lifecycle-authority-valid
```

This example is illustrative and does not constitute an approved package or release.

## 15. Boundaries

This artifact defines the package contract, not a production publishing service, archive format, package registry, website, API, signing infrastructure or deployment pipeline. Those implementations require separate governed Work Packages.