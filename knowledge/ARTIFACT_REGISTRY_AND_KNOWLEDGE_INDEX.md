---
Artifact-ID: OMSP-KNOWLEDGE-REGISTRY-0001
Title: OMSP Artifact Registry and Knowledge Index
Version: 1.0.0
Status: Review
Owner: OMSP Engineering Council
Baseline: Sprint-3
Classification: Public
Related-Issue: WP-0033 / #67
Depends-On:
  - OMSP-STD-METADATA-TRACEABILITY-0001
  - OMSP-ONTOLOGY-CORE-0001
  - OMSP-KNOWLEDGE-GRAPH-0001
  - OMSP-KNOWLEDGE-RELATIONSHIP-0001
---

# OMSP Artifact Registry and Knowledge Index

## 1. Purpose

This artifact defines the authoritative registry and discovery index for governed OMSP artifacts. It establishes the minimum record schema, identity rules, lifecycle handling, ownership and provenance links, indexing behavior, and example dataset structure required for future machine-readable registries and knowledge services.

## 2. Authority Model

The registry is an index of governed sources; it is not itself the authority for artifact content.

- The governed artifact remains authoritative for its content and lifecycle metadata.
- The registry mirrors selected metadata for discovery, validation and traceability.
- Registry records must identify the source file and repository ref from which they were derived.
- A registry entry must never silently promote a Draft or Review artifact to Active.
- Human approval records remain the authority for activation, baseline and release decisions.

## 3. Registry Record Schema

Each registry record must contain:

| Field | Required | Description |
| --- | --- | --- |
| `artifact_id` | Yes | Stable OMSP Artifact-ID |
| `title` | Yes | Human-readable title |
| `version` | Yes | Artifact semantic version |
| `status` | Yes | Proposed, Draft, Review, Active, Superseded, Deprecated or Retired |
| `owner` | Yes | Accountable role or governance body |
| `classification` | Yes | Public, Internal or Restricted |
| `baseline` | Yes | Governing sprint, baseline or release context |
| `repository` | Yes | Repository full name |
| `path` | Yes | Canonical repository path |
| `source_ref` | Yes | Branch, commit, tag or baseline ref used to index the record |
| `related_issue` | Yes | Work Package or issue reference |
| `artifact_type` | Yes | Ontology-aligned artifact concept or controlled type |
| `updated_at` | Yes | Last governed source update date |
| `indexed_at` | Yes | Registry indexing timestamp |
| `content_digest` | Recommended | Digest of indexed source content |
| `depends_on` | Optional | Artifact-ID list |
| `related_artifacts` | Optional | Artifact-ID list |
| `supersedes` | Optional | Artifact-ID replaced by this record |
| `superseded_by` | Optional | Replacement Artifact-ID |
| `provenance` | Yes | Source and derivation evidence list |
| `approval_evidence` | Conditional | Required for Active, baseline or release authority claims |

## 4. Identity and Uniqueness Rules

- `artifact_id` is the global logical identity of a governed artifact.
- `artifact_id` plus `version` identifies a governed artifact version.
- `repository` plus `path` identifies the indexed source location.
- The same `artifact_id` must not represent different meanings.
- Duplicate records for the same `artifact_id` and `version` are invalid unless one is explicitly a historical snapshot with distinct provenance.
- File renames preserve artifact identity when semantic meaning remains compatible.
- Breaking semantic changes require a new major version or new Artifact-ID according to the governing standard.

## 5. Artifact Type Mapping

`artifact_type` should map to an ontology concept where practical, including:

- `OMSP-CONCEPT-ARTIFACT`
- `OMSP-CONCEPT-DECISION`
- `OMSP-CONCEPT-EVIDENCE`
- `OMSP-CONCEPT-MODEL`
- `OMSP-CONCEPT-BASELINE`
- `OMSP-CONCEPT-RELEASE`

More specific controlled subtypes may be introduced through governed extensions, but they must preserve a traceable mapping to the ontology.

## 6. Lifecycle Handling

The registry must preserve source lifecycle state exactly.

| Source status | Registry behavior |
| --- | --- |
| Proposed | Discoverable as planned work; not authoritative |
| Draft | Discoverable as work in progress |
| Review | Discoverable as pending review |
| Active | Discoverable as current governed authority after human review evidence |
| Superseded | Retained for traceability and linked to replacement |
| Deprecated | Retained with deprecation rationale |
| Retired | Retained as historical record and excluded from current-authority queries |

Baseline and release are contextual records, not substitutes for artifact lifecycle status. A baseline may include Active artifacts and approved snapshots; a release may publish an approved baseline.

## 7. Discovery and Index Rules

A future indexer should:

1. discover governed files from configured repository scopes;
2. parse required metadata without altering source content;
3. validate Artifact-ID, version, status and classification;
4. resolve source repository, path and ref;
5. compute content digest when supported;
6. collect declared dependencies and relations;
7. attach provenance evidence;
8. reject conflicting identities or malformed records;
9. publish only validated registry records;
10. preserve previous records for audit when versions or states change.

Current-authority queries should prefer:

1. Active records;
2. highest compatible version;
3. approved baseline or release inclusion;
4. non-superseded records;
5. canonical repository/path when duplicate mirrors exist.

## 8. Knowledge Index Views

The same registry dataset may support derived views:

- current authoritative artifacts;
- artifacts by owner;
- artifacts by lifecycle status;
- artifacts by baseline or release;
- dependency and impact views;
- supersession chains;
- artifacts related to an issue, PR or Work Package;
- artifacts missing approval, provenance or dependency links;
- cross-repository artifact discovery.

Derived views must remain traceable to the underlying registry records.

## 9. Ownership and Provenance

Every record must preserve:

- accountable owner;
- source repository and path;
- source ref or commit;
- related issue or Work Package;
- indexing timestamp;
- indexing method or agent;
- approval evidence when authority is claimed.

AI or automation may index, normalize, validate and summarize records. It must not create approval evidence, change lifecycle authority, or infer that an artifact is Active without accountable human evidence.

## 10. Example Registry Record

```yaml
artifact_id: OMSP-KNOWLEDGE-GRAPH-0001
title: OMSP Knowledge Graph Conceptual Model
version: 1.0.0
status: Active
owner: OMSP Engineering Council
classification: Public
baseline: Sprint-3
repository: OMSP-Foundation/omsp-bootstrap
path: knowledge/KNOWLEDGE_GRAPH_CONCEPTUAL_MODEL.md
source_ref: commit:<sha>
related_issue: WP-0031 / #65
artifact_type: OMSP-CONCEPT-MODEL
updated_at: 2026-07-10
indexed_at: 2026-07-10T12:00:00Z
content_digest: sha256:<digest>
depends_on:
  - OMSP-ONTOLOGY-CORE-0001
  - OMSP-STD-METADATA-TRACEABILITY-0001
provenance:
  - source: file:knowledge/KNOWLEDGE_GRAPH_CONCEPTUAL_MODEL.md
    relation: documents
    target: issue:#65
  - source: pr:#<number>
    relation: satisfies
    target: issue:#65
approval_evidence:
  - review:#<human-review-id>
```

## 11. Validator-Oriented Rules

A future registry validator should reject records when:

- required fields are missing;
- Artifact-ID or version format is invalid;
- status or classification is outside the governed enum;
- source repository, path or ref is absent;
- duplicate identity/version records conflict;
- Active status lacks human approval evidence;
- superseded records do not identify a replacement where one exists;
- dependency references use unknown or malformed identifiers;
- provenance claims reference nonexistent evidence;
- an indexing agent is represented as approval authority.

## 12. Example Dataset

A machine-readable example dataset is maintained in `knowledge/artifact-registry.example.json`. It is illustrative and does not constitute an approved baseline or production registry.

## 13. Boundaries

This Work Package does not implement:

- a production registry service;
- repository crawling infrastructure;
- search APIs or user interfaces;
- graph database synchronization;
- automated lifecycle promotion;
- release publication infrastructure;
- regulatory or safety certification claims.

Technology selection and production implementation remain follow-up work.