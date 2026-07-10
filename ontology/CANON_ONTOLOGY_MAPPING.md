---
Artifact-ID: OMSP-ONTOLOGY-CANON-MAPPING-0001
Title: Canon to Ontology Mapping
Version: 1.0.0
Status: Active
Owner: OMSP Foundation Governance
Baseline: Sprint-2
Related-Issue: WP-0023 / #49
---

# Canon to Ontology Mapping

## Purpose

This mapping connects canonical OMSP terminology to stable ontology concept and relation identifiers. Canon defines preferred language; the ontology defines semantic identity and machine-readable contracts.

## Term Mapping

| Canon term | Canon source | Ontology identity | Mapping note |
| --- | --- | --- | --- |
| OMSP | `OMSP-CANON-TERMINOLOGY-0001` | ontology namespace/context | Program identity, not a class instantiated by default. |
| Canon | `OMSP-CANON-TERMINOLOGY-0001` | `OMSP-CONCEPT-ARTIFACT` | Canon documents are governed artifacts with language authority. |
| Governance | `OMSP-CANON-TERMINOLOGY-0001` | `OMSP-RELATION-GOVERNS` and governance artifacts | Governance is represented through authority-bearing artifacts and relations. |
| Engineering Artifact | `OMSP-CANON-TERMINOLOGY-0001` | `OMSP-CONCEPT-ARTIFACT` | Direct concept mapping. |
| Work Package | `OMSP-CANON-TERMINOLOGY-0001` | `OMSP-CONCEPT-WORK-PACKAGE` | Direct concept mapping. |
| Baseline | `OMSP-CANON-TERMINOLOGY-0001` | `OMSP-CONCEPT-BASELINE` | Specialized Artifact. |
| Release | `OMSP-CANON-TERMINOLOGY-0001` | `OMSP-CONCEPT-RELEASE` | Specialized Artifact. |
| Traceability | `OMSP-CANON-TERMINOLOGY-0001` | typed relation set led by `OMSP-RELATION-TRACES-TO` | Prefer specific relation identities when available. |
| Ontology | `OMSP-CANON-TERMINOLOGY-0001` | `OMSP-ONTOLOGY-CORE-0001` | Governed conceptual model and registry. |
| Maritime Operational Knowledge | `OMSP-CANON-TERMINOLOGY-0001` | domain instances of Actor, Operation, Capability, System and Constraint | Domain scope, not one undifferentiated class. |
| Model-Based Engineering | `OMSP-CANON-TERMINOLOGY-0001` | `OMSP-CONCEPT-MODEL` plus `defines`, `implements`, `validates` and `traces-to` relations | Practice represented by connected artifacts and relations. |
| Downstream Artifact | `OMSP-CANON-TERMINOLOGY-0001` | `OMSP-CONCEPT-ARTIFACT` with `depends-on` or `uses` relation | Contextual role of an Artifact. |
| Human Accountability | `OMSP-CANON-TERMINOLOGY-0001` | `OMSP-CONCEPT-ACTOR` and `OMSP-RELATION-APPROVES` | Approval authority requires a human actor or authorized human body. |
| AI Assistance | `OMSP-CANON-TERMINOLOGY-0001` | Actor/System participating through `produces`, `uses` or `supports` | AI assistance cannot be the authoritative source of `approves`. |

## Overview Concept Mapping

| Overview family | Ontology identity |
| --- | --- |
| Actor | `OMSP-CONCEPT-ACTOR` |
| Operation | `OMSP-CONCEPT-OPERATION` |
| Capability | `OMSP-CONCEPT-CAPABILITY` |
| System | `OMSP-CONCEPT-SYSTEM` |
| Artifact | `OMSP-CONCEPT-ARTIFACT` |
| Decision | `OMSP-CONCEPT-DECISION` |
| Evidence | `OMSP-CONCEPT-EVIDENCE` |
| Constraint | `OMSP-CONCEPT-CONSTRAINT` |
| Relation | the governed `OMSP-RELATION-*` registry |

## Change Rule

A canon term change that alters meaning requires ontology impact analysis. An ontology label change that does not alter meaning must retain its stable ontology ID and update this mapping in the same reviewed change.
