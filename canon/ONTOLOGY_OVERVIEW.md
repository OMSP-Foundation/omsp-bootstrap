---
Artifact-ID: OMSP-CANON-ONTOLOGY-OVERVIEW-0001
Title: OMSP Ontology Overview
Version: 1.0.0
Status: Active
Owner: OMSP Foundation Governance
Baseline: Sprint-1
Classification: Public
Related-Issue: WP-0016 / #38
---

# OMSP Ontology Overview

## 1. Purpose

This overview introduces the OMSP conceptual model and provides the starting point for future ontology, architecture, and model-based engineering artifacts.

It does not define a full formal ontology. It defines the foundation concepts and relation families that downstream artifacts may refine.

## 2. Ontology Intent

The OMSP ontology exists to make maritime operational knowledge explicit, structured, traceable, and reusable.

It should help downstream repositories answer:

- what concepts exist;
- how concepts relate;
- which artifacts define or govern each concept;
- what evidence supports a model or decision;
- how operational knowledge maps to architecture and implementation.

## 3. Foundational Concept Families

### 3.1 Actor

A person, organization, role, system, or agent that performs actions or holds responsibility.

### 3.2 Operation

A coordinated maritime activity with intent, scope, context, actors, constraints, and outcomes.

### 3.3 Capability

An ability required or provided by an actor, system, process, or organization.

### 3.4 System

A technical, organizational, operational, or socio-technical entity that participates in maritime operations.

### 3.5 Artifact

A durable representation of knowledge, decision, model, process, baseline, release, or evidence.

### 3.6 Decision

A recorded choice that affects scope, architecture, governance, baseline, release, operation, or implementation.

### 3.7 Evidence

A traceable record that supports a claim, validation, review, approval, baseline, or release.

### 3.8 Constraint

A rule, limitation, policy, requirement, environmental condition, standard, or governance boundary.

### 3.9 Relation

A typed connection between concepts, artifacts, work items, evidence, decisions, or operational entities.

## 4. Foundational Relation Families

OMSP relation families include:

| Relation Family | Meaning |
| --- | --- |
| `defines` | An artifact defines a concept, rule, or model. |
| `governs` | A governance artifact controls another artifact, process, or decision. |
| `implements` | A work item or artifact implements a concept, standard, or decision. |
| `depends-on` | One concept, artifact, or work item depends on another. |
| `traces-to` | A general traceability link between source and target. |
| `validates` | Evidence supports or confirms a target. |
| `constrains` | A rule or condition limits possible behavior. |
| `belongs-to` | An entity is part of a larger context or grouping. |
| `uses` | An actor, system, or operation uses another entity. |
| `produces` | An actor, system, operation, or process produces an artifact or outcome. |

## 5. Canon to Ontology Mapping

Canon artifacts provide the language layer for ontology work:

| Canon Artifact | Ontology Role |
| --- | --- |
| Vision | Defines long-term intent. |
| Mission | Defines operational purpose. |
| Philosophy | Defines interpretive stance. |
| Principles | Defines normative constraints. |
| Terminology | Defines canonical terms. |
| Ontology Overview | Defines initial concept and relation families. |

## 6. Governance and Traceability

Ontology artifacts are governed engineering artifacts and must follow metadata, traceability, ownership, and review standards.

Future ontology extensions should trace to:

```text
Canon → Terminology → Ontology Concept → Model Artifact → Decision / Evidence → Downstream Use
```

## 7. Downstream Use

Downstream repositories may use this overview to:

- define domain models;
- create architecture views;
- classify artifacts;
- structure traceability matrices;
- align terminology;
- identify missing concepts or relations;
- prepare future formal ontology work.

## 8. Boundaries

This overview does not yet define:

- a formal OWL/RDF ontology;
- complete maritime domain taxonomy;
- operational procedure models;
- implementation schemas;
- data exchange standards.

Those should be introduced through future Work Packages when needed.

## 9. Maintenance

This Ontology Overview is maintained through issue-backed Work Packages and reviewed pull requests. Material changes require governance review and version metadata update.
