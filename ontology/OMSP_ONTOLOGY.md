---
Artifact-ID: OMSP-ONTOLOGY-CORE-0001
Title: OMSP Formal Ontology
Version: 1.0.0
Status: Active
Owner: OMSP Foundation Governance
Baseline: Sprint-2
Classification: Public
Related-Issue: WP-0023 / #49
Depends-On:
  - OMSP-CANON-ONTOLOGY-OVERVIEW-0001
  - OMSP-CANON-TERMINOLOGY-0001
  - OMSP-STD-ARTIFACT-0001
  - OMSP-STD-METADATA-TRACEABILITY-0001
---

# OMSP Formal Ontology

## 1. Purpose

This artifact defines the formal, technology-neutral conceptual ontology for OMSP. It establishes stable concept identifiers, relation identifiers, meanings, domains, ranges and governance rules for downstream architecture, models, registries, traceability and automation.

## 2. Scope and Format Decision

Sprint-2 adopts a two-layer ontology format:

1. this Markdown artifact is the human-readable normative definition;
2. `ontology/omsp-ontology.json` is the machine-readable registry.

OWL, RDF and SHACL serializations are deferred until a downstream implementation requires semantic-web interoperability. That deferral avoids selecting an implementation technology before the concept and relation contracts stabilize.

## 3. Identity Rules

- Concept IDs use `OMSP-CONCEPT-<NAME>`.
- Relation IDs use `OMSP-RELATION-<NAME>`.
- IDs are stable and must not be reused for a different meaning.
- Labels may evolve without changing identity when meaning remains compatible.
- Material semantic changes require a new version, issue-backed review and migration notes.
- Deprecated concepts and relations remain addressable until governed retirement.

## 4. Concept Taxonomy

| Concept ID | Preferred label | Definition | Parent concept |
| --- | --- | --- | --- |
| `OMSP-CONCEPT-ENTITY` | Entity | Anything with distinct identity in the OMSP knowledge domain. | — |
| `OMSP-CONCEPT-ACTOR` | Actor | A person, organization, role, system or agent that acts or holds responsibility. | Entity |
| `OMSP-CONCEPT-OPERATION` | Operation | A coordinated maritime activity with intent, context, actors, constraints and outcomes. | Entity |
| `OMSP-CONCEPT-CAPABILITY` | Capability | An ability required or provided by an actor, system, process or organization. | Entity |
| `OMSP-CONCEPT-SYSTEM` | System | A technical, organizational, operational or socio-technical entity. | Entity |
| `OMSP-CONCEPT-ARTIFACT` | Artifact | A durable representation of knowledge, decision, model, process, baseline, release or evidence. | Entity |
| `OMSP-CONCEPT-DECISION` | Decision | A recorded choice affecting scope, architecture, governance, baseline, release, operation or implementation. | Artifact |
| `OMSP-CONCEPT-EVIDENCE` | Evidence | A traceable record supporting a claim, validation, review, approval, baseline or release. | Artifact |
| `OMSP-CONCEPT-CONSTRAINT` | Constraint | A rule, limitation, requirement, policy, environmental condition, standard or governance boundary. | Entity |
| `OMSP-CONCEPT-REQUIREMENT` | Requirement | A governed statement of a necessary capability, behavior, quality or constraint. | Constraint |
| `OMSP-CONCEPT-MODEL` | Model | A structured representation of entities, relations, behavior, state or constraints. | Artifact |
| `OMSP-CONCEPT-BASELINE` | Baseline | A governed and approved snapshot of artifact or repository state. | Artifact |
| `OMSP-CONCEPT-RELEASE` | Release | A versioned publication of an approved repository state or artifact set. | Artifact |
| `OMSP-CONCEPT-WORK-PACKAGE` | Work Package | A scoped unit of issue-backed work with deliverables and acceptance criteria. | Entity |
| `OMSP-CONCEPT-CLAIM` | Claim | A statement whose acceptance depends on evidence or accountable judgment. | Entity |

## 5. Relation Taxonomy

| Relation ID | Label | Domain | Range | Meaning |
| --- | --- | --- | --- | --- |
| `OMSP-RELATION-DEFINES` | defines | Artifact | Entity | The source provides the normative or descriptive definition of the target. |
| `OMSP-RELATION-GOVERNS` | governs | Artifact | Entity | The source establishes authority, rules or control over the target. |
| `OMSP-RELATION-IMPLEMENTS` | implements | Entity | Entity | The source realizes all or part of the target. |
| `OMSP-RELATION-DEPENDS-ON` | depends-on | Entity | Entity | The source requires the target for validity, execution or interpretation. |
| `OMSP-RELATION-TRACES-TO` | traces-to | Entity | Entity | The source has a general traceability connection to the target. |
| `OMSP-RELATION-VALIDATES` | validates | Evidence | Entity | The source provides validation evidence for the target. |
| `OMSP-RELATION-VERIFIES` | verifies | Evidence | Requirement | The source demonstrates conformance to the target requirement. |
| `OMSP-RELATION-CONSTRAINS` | constrains | Constraint | Entity | The source limits allowable properties or behavior of the target. |
| `OMSP-RELATION-BELONGS-TO` | belongs-to | Entity | Entity | The source is a member or part of the target context. |
| `OMSP-RELATION-USES` | uses | Entity | Entity | The source consumes or employs the target. |
| `OMSP-RELATION-PRODUCES` | produces | Entity | Entity | The source creates or emits the target. |
| `OMSP-RELATION-SUPERSEDES` | supersedes | Artifact | Artifact | The source replaces the target as the current authority. |
| `OMSP-RELATION-SUPPORTS` | supports | Evidence | Claim | The source contributes evidence for the target claim. |
| `OMSP-RELATION-APPROVES` | approves | Actor | Artifact | The accountable actor records approval of the target. |

## 6. Relation Semantics

- Relations are directed from source to target.
- `depends-on` is not assumed transitive unless a validator or downstream model explicitly declares transitive closure.
- `supersedes` is asymmetric and must not form cycles.
- `approves` may only identify accountable human actors or authorized human governance bodies.
- AI systems may `produces` proposals or evidence summaries, but may not be the source of `approves`.
- General `traces-to` should not replace a more precise relation when one exists.

## 7. Canon Mapping

The detailed term-to-concept mapping is maintained in `ontology/CANON_ONTOLOGY_MAPPING.md`. Canon terminology remains the authoritative language layer; this ontology supplies stable semantic identities and relation contracts.

## 8. Evolution Governance

A proposed ontology change must include:

- the affected concept or relation IDs;
- compatibility classification: additive, compatible refinement, deprecation or breaking;
- impacted artifacts and downstream consumers;
- migration guidance for breaking or deprecated semantics;
- issue, branch, PR, review and approval evidence.

Automation may validate structure, identifiers and relation constraints. It cannot approve semantic authority or ontology release state.

## 9. Traceability Chain

Material ontology use should support this chain:

```text
Canon term → Ontology concept/relation → Model or architecture artifact → Requirement/decision → Evidence → Baseline/release
```

## 10. Boundaries

This artifact does not define a complete maritime domain ontology, runtime data model, database schema, reasoning engine or certified operational instruction set. Domain extensions must build on these identifiers through separate governed artifacts.
