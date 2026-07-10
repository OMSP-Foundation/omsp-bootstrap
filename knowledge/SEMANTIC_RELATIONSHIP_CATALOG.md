---
Artifact-ID: OMSP-KNOWLEDGE-RELATIONSHIP-0001
Title: OMSP Semantic Relationship Catalog
Version: 1.0.0
Status: Review
Owner: OMSP Engineering Council
Baseline: Sprint-3
Classification: Public
Related-Issue: WP-0032 / #66
Depends-On:
  - OMSP-ONTOLOGY-CORE-0001
  - OMSP-KNOWLEDGE-GRAPH-0001
  - OMSP-STD-METADATA-TRACEABILITY-0001
---

# OMSP Semantic Relationship Catalog

## 1. Purpose

This catalog defines the governed semantic relationship vocabulary used across OMSP artifacts, ontology records, knowledge graph representations and future validators. It narrows relationship meaning, direction, source and target constraints so that the same relation is not overloaded across incompatible contexts.

## 2. Relationship Record Contract

Each semantic relationship record contains:

```yaml
relation_id: OMSP-RELATION-<NAME>
label: kebab-case-label
direction: source-to-target
source_types: [allowed ontology concepts]
target_types: [allowed ontology concepts]
cardinality: source-cardinality -> target-cardinality
inverse: relation-id | none
transitive: true | false | controlled
symmetric: true | false
lifecycle: proposed | active | deprecated | retired
```

A relationship instance must also identify its source, target, provenance evidence and lifecycle state.

## 3. Core Relationship Vocabulary

| Relation ID | Label | Allowed source | Allowed target | Cardinality guidance | Inverse | Transitive | Meaning |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `OMSP-RELATION-DEFINES` | defines | Artifact | Entity | many-to-many | none | false | Source provides a normative or descriptive definition of target. |
| `OMSP-RELATION-GOVERNS` | governs | Artifact | Entity | many-to-many | none | controlled | Source establishes authority, policy or control over target. |
| `OMSP-RELATION-IMPLEMENTS` | implements | Entity | Entity | many-to-many | none | false | Source realizes all or part of target. |
| `OMSP-RELATION-DEPENDS-ON` | depends-on | Entity | Entity | many-to-many | none | controlled | Source requires target for validity, execution or interpretation. |
| `OMSP-RELATION-TRACES-TO` | traces-to | Entity | Entity | many-to-many | none | false | General traceability relation used only when no narrower relation applies. |
| `OMSP-RELATION-VALIDATES` | validates | Evidence | Entity | many-to-many | none | false | Source provides validation evidence for target. |
| `OMSP-RELATION-VERIFIES` | verifies | Evidence | Requirement | many-to-many | none | false | Source demonstrates conformance to target requirement. |
| `OMSP-RELATION-CONSTRAINS` | constrains | Constraint | Entity | many-to-many | none | controlled | Source limits allowable properties, states or behavior of target. |
| `OMSP-RELATION-BELONGS-TO` | belongs-to | Entity | Entity | many-to-one by default | `OMSP-RELATION-CONTAINS` | false | Source is a member or part of target context. |
| `OMSP-RELATION-CONTAINS` | contains | Entity | Entity | one-to-many by default | `OMSP-RELATION-BELONGS-TO` | false | Source contains or groups target. |
| `OMSP-RELATION-USES` | uses | Entity | Entity | many-to-many | none | false | Source consumes or employs target. |
| `OMSP-RELATION-PRODUCES` | produces | Entity | Entity | one-to-many by default | `OMSP-RELATION-PRODUCED-BY` | false | Source creates or emits target. |
| `OMSP-RELATION-PRODUCED-BY` | produced-by | Entity | Entity | many-to-one by default | `OMSP-RELATION-PRODUCES` | false | Source was created or emitted by target. |
| `OMSP-RELATION-SUPERSEDES` | supersedes | Artifact | Artifact | many-to-one constrained | `OMSP-RELATION-SUPERSEDED-BY` | false | Source replaces target as current authority. |
| `OMSP-RELATION-SUPERSEDED-BY` | superseded-by | Artifact | Artifact | one-to-many constrained | `OMSP-RELATION-SUPERSEDES` | false | Source has been replaced by target. |
| `OMSP-RELATION-SUPPORTS` | supports | Evidence | Claim | many-to-many | none | false | Source contributes evidence for target claim. |
| `OMSP-RELATION-APPROVES` | approves | Actor | Artifact | many-to-many | `OMSP-RELATION-APPROVED-BY` | false | Accountable human actor or authorized human body approves target. |
| `OMSP-RELATION-APPROVED-BY` | approved-by | Artifact | Actor | many-to-many | `OMSP-RELATION-APPROVES` | false | Source records approval by target accountable actor or body. |
| `OMSP-RELATION-REVIEWS` | reviews | Actor | Artifact | many-to-many | `OMSP-RELATION-REVIEWED-BY` | false | Source evaluates target without necessarily approving it. |
| `OMSP-RELATION-REVIEWED-BY` | reviewed-by | Artifact | Actor | many-to-many | `OMSP-RELATION-REVIEWS` | false | Source has review evidence from target. |
| `OMSP-RELATION-BASELINES` | baselines | Baseline | Artifact | one-to-many | `OMSP-RELATION-IN-BASELINE` | false | Source governed baseline includes target artifact state. |
| `OMSP-RELATION-IN-BASELINE` | in-baseline | Artifact | Baseline | many-to-one or many-to-many | `OMSP-RELATION-BASELINES` | false | Source artifact version is included in target baseline. |
| `OMSP-RELATION-RELEASES` | releases | Release | Artifact | one-to-many | `OMSP-RELATION-IN-RELEASE` | false | Source release publishes target artifact state. |
| `OMSP-RELATION-IN-RELEASE` | in-release | Artifact | Release | many-to-one or many-to-many | `OMSP-RELATION-RELEASES` | false | Source artifact version is included in target release. |

## 4. Directionality Rules

- Every relation is stored from source to target.
- Direction must reflect the catalog definition, not natural-language sentence order.
- Inverse relations may be materialized only when a consumer requires them.
- Validators must not infer an inverse unless the catalog declares one.
- `approves` and `approved-by` are governance-sensitive and must point to accountable human authority evidence.

## 5. Cardinality Rules

Cardinality is guidance unless a downstream schema marks it strict.

- `many-to-many` permits multiple sources and targets.
- `one-to-many by default` means one source commonly produces or contains several targets, but exceptions require explicit modeling rationale.
- `many-to-one constrained` means multiple historical artifacts may be superseded by one replacement, while cycles and self-reference remain forbidden.
- Baseline and release membership is version-specific; validators must not treat all versions of an Artifact-ID as automatically included.

## 6. Inverse Relationship Rules

Declared inverse pairs are semantically equivalent views of the same fact. Implementations should store one canonical direction where practical and derive the inverse for query convenience.

Inverse materialization must:

- preserve the same provenance evidence;
- preserve source and target version references;
- not create a second independent approval or review claim;
- be regenerated when the canonical edge changes.

## 7. Transitivity Guidance

No relationship is universally transitive by default.

Controlled transitivity may be evaluated only under an explicit validator or query profile:

- `depends-on`: transitive closure may support impact analysis but must distinguish direct from inferred dependency;
- `governs`: governance inheritance may be inferred only when the governing artifact explicitly declares scope inheritance;
- `constrains`: inherited constraints require compatible domain and scope;
- `belongs-to` and `contains`: hierarchy traversal must not imply semantic equivalence.

`supersedes`, `approves`, `reviews`, `validates`, `verifies`, `uses`, `produces` and `supports` are not transitive.

## 8. Ambiguity Prevention

Use the narrowest valid relation:

- use `verifies` for evidence against a Requirement;
- use `validates` for broader evidence against an Entity;
- use `supports` for evidence contributing to a Claim;
- use `implements` for realization of a requirement, model or decision;
- use `depends-on` for required dependency;
- use `traces-to` only when no precise relation applies.

Do not use:

- `relates-to`, `associated-with` or other ungoverned generic labels;
- `approves` for automated checks, AI output or merge status;
- `supersedes` for ordinary revisions that retain the same stable artifact identity;
- `validates` as a substitute for accountable acceptance or approval.

## 9. Lifecycle and Version Rules

Relationship records have their own lifecycle state.

- `proposed`: relation has not completed review;
- `active`: relation is accepted for governed use;
- `deprecated`: relation remains readable but should not be created anew;
- `retired`: relation is no longer valid for current records.

A relationship instance must reference immutable or version-resolvable source and target identities when used in a baseline or release.

## 10. Validation Rules

A future validator should check:

1. relation ID exists in this catalog;
2. source and target types satisfy allowed domains and ranges;
3. source and target are not identical where self-reference is forbidden;
4. inverse relation, when materialized, is consistent;
5. forbidden cycles do not exist for `supersedes`;
6. approval edges identify accountable human actors or authorized human bodies;
7. lifecycle state is allowed;
8. provenance evidence is present;
9. inferred edges are marked as inferred and name the inference profile;
10. version-specific baseline and release membership is preserved.

## 11. Validation Examples

### 11.1 Valid dependency

```yaml
source: OMSP-KNOWLEDGE-GRAPH-0001
relation: OMSP-RELATION-DEPENDS-ON
target: OMSP-ONTOLOGY-CORE-0001
provenance: issue:#65
status: active
```

### 11.2 Valid human approval

```yaml
source: actor:OMSP-Engineering-Council
relation: OMSP-RELATION-APPROVES
target: baseline:Sprint-3
provenance: review:<human-review-id>
status: active
```

### 11.3 Invalid automated approval

```yaml
source: system:ci-validator
relation: OMSP-RELATION-APPROVES
target: release:v0.3.0-foundation-sprint-3
```

This is invalid because automation may validate evidence but cannot originate accountable approval authority.

### 11.4 Valid verification

```yaml
source: evidence:validation-record-0042
relation: OMSP-RELATION-VERIFIES
target: requirement:REQ-0042
provenance: file:validation/evidence/validation-record-0042.md
status: active
```

## 12. Governance and Change Control

Changes to this catalog require:

- issue-backed rationale;
- compatibility classification;
- affected relation IDs;
- source and target type impact analysis;
- migration guidance for deprecated or breaking changes;
- feature branch and pull request;
- accountable human review before Active status.

Automation may identify structural violations and propose relationship mappings. It may not approve semantic meaning, governance authority, baseline membership or release acceptance.

## 13. Deferred Implementation Decisions

This catalog does not select RDF, OWL, SHACL, JSON-LD, a property graph database, query language or inference engine. Machine-readable serialization and validator implementation remain downstream governed work.