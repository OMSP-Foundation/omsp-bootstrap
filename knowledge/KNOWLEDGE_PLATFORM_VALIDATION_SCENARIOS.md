---
Artifact-ID: OMSP-KNOWLEDGE-VALIDATION-0001
Title: OMSP Knowledge Platform Validation Scenarios
Version: 1.0.0
Status: Review
Owner: OMSP Engineering Council
Baseline: Sprint-3
Classification: Public
Related-Issue: WP-0036 / #70
Depends-On:
  - OMSP-ONTOLOGY-CORE-0001
  - OMSP-KNOWLEDGE-GRAPH-0001
  - OMSP-KNOWLEDGE-RELATIONSHIP-0001
  - OMSP-KNOWLEDGE-REGISTRY-0001
  - OMSP-KNOWLEDGE-AI-PROCESSING-0001
  - OMSP-KNOWLEDGE-PUBLICATION-0001
---

# OMSP Knowledge Platform Validation Scenarios

## 1. Purpose

This artifact defines end-to-end validation scenarios for the governed OMSP knowledge workflow. It covers ontology identity, graph representation, semantic relationships, artifact registry behavior, AI-assisted processing and publication packaging while preserving accountable human authority.

## 2. Validation Principles

All scenarios must preserve:

- stable Artifact IDs and ontology identifiers;
- explicit lifecycle state and version information;
- complete provenance and traceability evidence;
- distinction between asserted and inferred relationships;
- distinction between proposals, reviews, approvals, baselines and releases;
- accountable human control of approval, baseline, release and risk acceptance.

A scenario passes only when both structural correctness and governance boundaries are satisfied.

## 3. Evidence Record

Each validation execution should record:

```yaml
scenario-id: KPV-XXX
execution-id: unique execution reference
executed-at: ISO-8601 timestamp
executor: human, workflow or tool identity
inputs:
  - artifact or package references
checks:
  - check identifier and result
result: pass | fail | blocked
findings:
  - severity, message and evidence reference
provenance:
  repository: owner/repository
  ref: branch, tag or commit
  commit: immutable commit SHA
review-status: proposed | reviewed | approved
reviewer: accountable human or governance body when reviewed
```

Automation may produce a proposed evidence record. It may not mark that record approved without accountable human review.

## 4. Positive Scenarios

### KPV-001 — Governed Artifact Discovery

**Objective:** Verify that a governed artifact can be discovered uniquely through the registry.

**Input:** A repository containing an artifact with valid metadata and a matching registry entry.

**Checks:**

1. Artifact ID matches the metadata standard.
2. Artifact ID is unique within the registry scope.
3. Repository path and immutable source revision are present.
4. Owner, version, status and classification are indexed.
5. Registry lifecycle state matches the source artifact.

**Expected result:** One authoritative registry record is returned with complete provenance.

### KPV-002 — Knowledge Graph Projection

**Objective:** Verify that a governed artifact projects into the graph without changing its identity.

**Checks:**

1. Artifact node retains the source Artifact ID.
2. Concept types reference governed ontology identifiers.
3. Relationship edges use cataloged relation IDs.
4. Edge direction matches the relationship catalog.
5. Asserted and inferred edges are distinguishable.

**Expected result:** Graph nodes and edges are traceable to source artifacts and relation definitions.

### KPV-003 — Dependency Traversal

**Objective:** Verify reproducible traversal of artifact dependencies.

**Checks:**

1. Every `depends-on` edge resolves to an existing target.
2. No dependency cycle violates an explicit catalog rule.
3. Historical or superseded dependencies remain distinguishable.
4. Missing optional dependencies are reported without being fabricated.

**Expected result:** The dependency chain is complete, typed and evidence-backed.

### KPV-004 — AI-Assisted Analysis Proposal

**Objective:** Verify that AI-assisted processing produces a bounded proposal.

**Checks:**

1. Input artifacts include identity, version, lifecycle state and provenance.
2. Output records assumptions, uncertainty and source references.
3. Proposed changes do not overwrite source artifacts.
4. Output lifecycle state is `proposed`.
5. No approval, baseline, release or merge authority is asserted.

**Expected result:** A reviewable proposal is produced with no governance promotion.

### KPV-005 — Reproducible Publication Package

**Objective:** Verify that a publication package can be reproduced from governed sources.

**Checks:**

1. Manifest identifies package class and version.
2. Every included artifact records Artifact ID, version, status, path and content digest.
3. Dependency closure is complete or explicitly documented.
4. Package source ref resolves to an immutable commit.
5. Consumer guidance identifies normative and non-normative content.

**Expected result:** Package contents and provenance are reproducible from the manifest.

### KPV-006 — Human Approval Evidence

**Objective:** Verify that an approved baseline or release has accountable human evidence.

**Checks:**

1. Approval record identifies an accountable human or authorized governance body.
2. Approval references the exact candidate commit or package digest.
3. Automated validation evidence is linked but not represented as approval.
4. Approved state is consistent across source, registry and package manifest.

**Expected result:** Approval authority and automated evidence remain separate and traceable.

## 5. Negative Scenarios

### KPV-101 — Duplicate Artifact Identity

**Condition:** Two active records use the same Artifact ID for different meanings or source artifacts.

**Expected result:** Validation fails. Neither record may be selected silently as authoritative.

### KPV-102 — Lifecycle State Promotion Without Evidence

**Condition:** A registry or package marks a Draft or Review artifact Active without accountable review evidence.

**Expected result:** Validation fails with a governance-boundary error.

### KPV-103 — Unknown Semantic Relationship

**Condition:** A graph edge uses a relation not present in the governed relationship catalog.

**Expected result:** Validation fails or blocks publication until the relation is governed.

### KPV-104 — Invalid Relationship Domain or Range

**Condition:** A relation is used between source and target types not permitted by its catalog definition.

**Expected result:** Validation fails and reports the relation, source type and target type.

### KPV-105 — Fabricated Provenance

**Condition:** An AI or automation output cites an issue, commit, approval or source that cannot be resolved.

**Expected result:** Validation fails. The unresolved reference is retained as a finding and must not be treated as evidence.

### KPV-106 — AI-Originated Approval

**Condition:** An AI system or automated workflow is recorded as the approver of an artifact, baseline, release or risk acceptance.

**Expected result:** Validation fails with critical severity.

### KPV-107 — Draft Content Presented as Normative

**Condition:** A publication package presents Draft, Proposed or Review content as approved normative content.

**Expected result:** Validation fails and the package must not be promoted to Baseline or Release.

### KPV-108 — Non-Reproducible Package

**Condition:** A package manifest omits immutable source refs, content digests or required dependency records.

**Expected result:** Validation fails reproducibility checks.

### KPV-109 — Inference Presented as Assertion

**Condition:** A derived graph relationship is stored or published as source-asserted evidence.

**Expected result:** Validation fails provenance classification.

### KPV-110 — Superseded Artifact Selected as Current Authority

**Condition:** Discovery returns a superseded artifact as current without explicit historical query intent.

**Expected result:** Validation fails current-authority selection.

## 6. Cross-Artifact Consistency Checks

Validators should check that:

- artifact metadata and registry records agree on ID, version and status;
- graph node identity matches the registry Artifact ID;
- relationship IDs and domain/range rules match the semantic catalog;
- AI processing records cite registry-resolvable sources;
- publication manifests cite immutable source revisions and digests;
- approval records reference the exact candidate being approved;
- supersession links are consistent across artifacts, registry and graph;
- no component silently upgrades authority or lifecycle state.

## 7. Failure Classification

| Severity | Meaning | Typical consequence |
| --- | --- | --- |
| Critical | Human authority, identity or provenance boundary is violated. | Block merge, baseline and release |
| High | Required dependency, lifecycle or reproducibility rule fails. | Block publication and promotion |
| Medium | Structural inconsistency or incomplete evidence exists. | Require correction or explicit deferral |
| Low | Advisory quality or consumer-guidance issue exists. | Record finding and review |

A failed critical or high finding must not be converted into a pass by automation. Deferral requires explicit accountable human rationale.

## 8. Validation Execution Modes

The scenarios may be executed through:

- manual governed review;
- repository validation scripts;
- CI quality gates;
- package validation workflows;
- AI-assisted analysis that produces proposed findings.

Execution technology does not change the acceptance authority. Human reviewers remain accountable for approving semantic changes, baselines, releases and risk acceptance.

## 9. Minimum Sprint-3 Validation Set

Before Sprint-3 baseline readiness, evidence should exist for at least:

- KPV-001 Governed Artifact Discovery;
- KPV-002 Knowledge Graph Projection;
- KPV-004 AI-Assisted Analysis Proposal;
- KPV-005 Reproducible Publication Package;
- KPV-006 Human Approval Evidence;
- KPV-102 Lifecycle State Promotion Without Evidence;
- KPV-105 Fabricated Provenance;
- KPV-106 AI-Originated Approval;
- KPV-107 Draft Content Presented as Normative.

## 10. Boundaries

This artifact defines validation scenarios and evidence expectations. It does not implement a production validator, graph engine, AI runtime, publication service, certification process or regulatory compliance claim.
