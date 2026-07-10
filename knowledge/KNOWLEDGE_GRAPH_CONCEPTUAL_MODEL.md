---
Artifact-ID: OMSP-KNOWLEDGE-GRAPH-0001
Title: OMSP Knowledge Graph Conceptual Model
Version: 0.1.0
Status: Review
Owner: OMSP Engineering Council
Baseline: Sprint-3
Classification: Public
Related-Issue: WP-0031 / #65
Depends-On:
  - OMSP-ONTOLOGY-CORE-0001
  - OMSP-STD-METADATA-TRACEABILITY-0001
  - OMSP-PLAN-SPRINT-0003
---

# OMSP Knowledge Graph Conceptual Model

## 1. Purpose

This artifact defines the technology-neutral conceptual model for representing governed OMSP knowledge as a graph. It establishes node categories, edge semantics, identity and versioning rules, lifecycle-state handling, provenance requirements, governance boundaries and example graph fragments.

The model supports future registries, validators, publication packages, AI-readable processing and cross-repository knowledge services without selecting a graph database or semantic-web technology prematurely.

## 2. Design Principles

The OMSP knowledge graph must:

1. preserve stable ontology and Artifact-ID identities;
2. represent typed, directed relations rather than unstructured links;
3. distinguish semantic identity from artifact version and lifecycle state;
4. preserve source provenance for every material node and edge;
5. keep draft, review, active, baseline and release contexts distinguishable;
6. make human approval authority explicit and non-delegable to automation;
7. support machine validation without treating machine output as governance approval;
8. remain portable across storage and serialization technologies.

## 3. Graph Building Blocks

| Record type | Purpose | Examples |
| --- | --- | --- |
| Concept node | Represents an ontology-defined concept identity | Artifact, Requirement, Evidence, Decision |
| Instance node | Represents an identified occurrence of a concept | A specific standard, issue, baseline or release |
| Relation edge | Represents a typed directed relation | depends-on, validates, supersedes, approves |
| Context record | Captures provenance, lifecycle, baseline and publication context | source file, commit, review, release package |

Context records may be implemented as nodes, edge attributes or external records, but their information must remain queryable and traceable.

## 4. Node Model

### 4.1 Concept Nodes

A concept node represents a stable identity from `OMSP-ONTOLOGY-CORE-0001`.

Required properties:

| Property | Rule |
| --- | --- |
| `node_id` | Stable ontology concept ID such as `OMSP-CONCEPT-ARTIFACT` |
| `node_type` | `concept` |
| `label` | Current preferred human-readable label |
| `ontology_version` | Version of the ontology registry used |
| `status` | Ontology lifecycle status |
| `source` | Governed ontology artifact reference |

Concept nodes are definitions. They are not project artifacts, approvals or runtime observations.

### 4.2 Instance Nodes

An instance node represents a specific governed object.

| Property | Rule |
| --- | --- |
| `node_id` | Stable entity reference or Artifact-ID |
| `node_type` | Ontology concept ID classifying the instance |
| `version` | Version when the source object is versioned |
| `lifecycle_state` | Proposed, Draft, Review, Active, Superseded, Deprecated or Retired |
| `source_ref` | File, issue, PR, commit, baseline, release or cross-repository reference |
| `owner` | Accountable role or governance body when applicable |
| `created_at` | Source-derived timestamp when available |
| `updated_at` | Source-derived timestamp when available |

Optional properties may include title, classification, repository, branch, hash, effective date and publication status.

### 4.3 Graph Identity

Graph identity must use the narrowest stable identifier available:

1. governed Artifact-ID;
2. ontology concept or relation ID;
3. prefixed traceability reference such as `issue:#65`, `pr:#102` or `commit:<sha>`;
4. cross-repository reference using the metadata standard form;
5. a governed domain identifier defined by a future extension.

File paths, labels and titles are locators or display data. They must not replace stable identity when an Artifact-ID exists.

## 5. Relation Model

Relations are directed from source to target and use ontology relation IDs as their semantic authority.

| Property | Rule |
| --- | --- |
| `edge_id` | Unique relation occurrence identifier |
| `relation_id` | Stable ontology relation ID |
| `source_node` | Existing graph node identity |
| `target_node` | Existing graph node identity |
| `status` | proposed, active, superseded or deprecated |
| `evidence_ref` | Source artifact, PR, review, commit or validation record |
| `asserted_by` | Human role, governed process or automation identity |
| `assertion_time` | Timestamp when available |

### 5.1 Relation Semantics

- A relation occurrence must conform to ontology domain and range rules.
- General `OMSP-RELATION-TRACES-TO` must not replace a more precise relation when one exists.
- `OMSP-RELATION-SUPERSEDES` must be acyclic.
- `OMSP-RELATION-APPROVES` may originate only from an accountable human actor or authorized human governance body.
- Automation may assert proposed relations and validation findings, but proposed assertions must remain distinguishable from reviewed active assertions.
- Relation evidence must be retained when an edge changes state or is superseded.

## 6. Artifact-to-Graph Mapping

| Artifact element | Graph representation |
| --- | --- |
| `Artifact-ID` | Primary instance node identity |
| `Title` | Display label |
| `Version` | Version property or version node |
| `Status` | Lifecycle-state property |
| `Owner` | Ownership relation or owner property |
| `Baseline` | Membership relation to baseline context |
| `Related-Issue` | Traceability relation to issue node |
| `Depends-On` | Typed dependency edges |
| `Supersedes` | Typed supersession edge |
| `Approver` / review evidence | Human approval actor and evidence relation |
| Source file path | Provenance locator |
| Commit and PR | Implementation and review provenance nodes |

The graph must not infer `Active`, baseline membership or release inclusion solely from file presence. These states require governed source evidence.

## 7. Identity and Versioning Rules

- Artifact-ID and ontology IDs remain stable across compatible revisions.
- Labels and file paths may change without changing identity.
- An identifier must never be reused for a different semantic meaning.
- Deprecated and superseded identities remain resolvable for traceability.

An implementation may represent versions as immutable snapshots of one logical node or as separate version nodes linked to a stable logical identity. In both cases the graph must expose current, prior, baseline-specific and release-specific versions plus supersession and provenance history.

A semantic version value does not imply review, approval, baseline membership or release status. These are separate governed facts.

## 8. Lifecycle and Publication Context

| Context | Meaning |
| --- | --- |
| Draft | Work exists but is not authoritative |
| Review | Work is awaiting structured human review |
| Active | Artifact is approved for current use |
| Baseline | Approved snapshot includes a specific artifact version |
| Release | Published package includes a baseline-approved version |

An artifact may be Active but absent from a particular baseline. A baseline may exist but not yet be published as a release. Draft material must never be returned as approved knowledge without explicit state information.

## 9. Provenance Model

Every material graph assertion must be traceable to evidence.

```text
Graph node or edge
  -> source artifact or engineering record
  -> issue / branch / commit / PR
  -> review evidence
  -> baseline or release context when applicable
```

Required provenance should include source repository and path, Artifact-ID or entity reference, source version or commit hash, asserting actor or process, review status, baseline and release context, and validation evidence where applicable.

Derived facts must identify both their source facts and the rule or process that produced the derivation.

## 10. Governance Boundaries

Only accountable humans or authorized human governance bodies may approve semantic authority, activate governed artifacts, approve ontology changes, approve baseline membership, approve release publication or accept material risk.

Automation and AI may extract candidate nodes and relations, validate constraints, detect missing links, generate proposed graph fragments, summarize provenance and support search and analysis.

Automation and AI must not fabricate provenance, silently promote assertions to active, create human approval edges, decide semantic authority, represent draft knowledge as baseline-approved or override accountable ownership and review decisions.

## 11. Example Graph Fragments

### 11.1 Artifact Dependency

```yaml
nodes:
  - node_id: OMSP-KNOWLEDGE-GRAPH-0001
    node_type: OMSP-CONCEPT-MODEL
    version: 0.1.0
    lifecycle_state: Review
    source_ref: file:knowledge/KNOWLEDGE_GRAPH_CONCEPTUAL_MODEL.md
  - node_id: OMSP-ONTOLOGY-CORE-0001
    node_type: OMSP-CONCEPT-ARTIFACT
    version: 1.0.0
    lifecycle_state: Active
    source_ref: file:ontology/OMSP_ONTOLOGY.md
edges:
  - edge_id: edge:kg-model-depends-on-ontology
    relation_id: OMSP-RELATION-DEPENDS-ON
    source_node: OMSP-KNOWLEDGE-GRAPH-0001
    target_node: OMSP-ONTOLOGY-CORE-0001
    status: active
    evidence_ref: issue:#65
    asserted_by: OMSP Engineering Council
```

### 11.2 Validation Evidence

```yaml
nodes:
  - node_id: evidence:ontology-validation:<commit-sha>
    node_type: OMSP-CONCEPT-EVIDENCE
    lifecycle_state: Active
    source_ref: commit:<commit-sha>
  - node_id: OMSP-ONTOLOGY-CORE-0001
    node_type: OMSP-CONCEPT-ARTIFACT
    lifecycle_state: Active
edges:
  - edge_id: edge:ontology-validation
    relation_id: OMSP-RELATION-VALIDATES
    source_node: evidence:ontology-validation:<commit-sha>
    target_node: OMSP-ONTOLOGY-CORE-0001
    status: active
    evidence_ref: pr:#<number>
    asserted_by: workflow:ontology-validation
```

This edge records evidence; it does not constitute human approval.

### 11.3 Human Approval

```yaml
nodes:
  - node_id: actor:omsp-accountable-maintainer
    node_type: OMSP-CONCEPT-ACTOR
  - node_id: baseline:Sprint-3
    node_type: OMSP-CONCEPT-BASELINE
edges:
  - edge_id: edge:sprint-3-baseline-approval
    relation_id: OMSP-RELATION-APPROVES
    source_node: actor:omsp-accountable-maintainer
    target_node: baseline:Sprint-3
    status: active
    evidence_ref: review:<human-review-id>
    asserted_by: governance-process
```

## 12. Validation Requirements

A future graph validator should check:

- node identifiers use approved formats;
- referenced ontology concepts and relations exist;
- edge domain and range constraints are satisfied;
- lifecycle-state values are valid;
- every material edge has evidence and assertion provenance;
- supersession cycles do not exist;
- draft and review content is distinguishable from active content;
- baseline and release membership references a specific artifact version;
- approval relations originate from human-accountable actors;
- derived facts identify their source and derivation rule.

## 13. Deferred Implementation Decisions

Deferred decisions include graph database selection; RDF, OWL, SHACL, JSON-LD or property-graph serialization; query language and API design; distributed synchronization; production inference; access-control enforcement; ingestion pipelines; and operational digital twin extensions.

## 14. Traceability

This model traces to WP-0031 / issue #65, `OMSP-ONTOLOGY-CORE-0001`, `OMSP-STD-METADATA-TRACEABILITY-0001` and `OMSP-PLAN-SPRINT-0003`.

```text
Issue #65 -> feature branch -> commit -> Draft PR -> human review -> merge to develop
```
