---
Artifact-ID: OMSP-CANON-TERMINOLOGY-0001
Title: OMSP Terminology
Version: 1.0.0
Status: Active
Owner: OMSP Foundation Governance
Baseline: Sprint-1
Classification: Public
Related-Issue: WP-0016 / #38
---

# OMSP Terminology

## 1. Purpose

This document defines common OMSP vocabulary so canon, governance, engineering, architecture, and downstream repository artifacts use consistent language.

Terms defined here should be referenced by downstream artifacts when ambiguity would affect scope, authority, traceability, architecture, or review.

## 2. Core Terms

### 2.1 OMSP

The Open Maritime Systems Platform: an open, model-based, knowledge-first systems engineering foundation for maritime operations.

### 2.2 Canon

The durable identity and language layer of OMSP. Canon artifacts define vision, mission, philosophy, principles, terminology, and ontology concepts.

### 2.3 Governance

The authority, responsibility, decision, review, baseline, and release model used to control OMSP work.

### 2.4 Engineering Artifact

A durable repository object that records a decision, standard, model, process, baseline, release, architecture, or reusable engineering knowledge.

### 2.5 Work Package

A scoped unit of work represented by an issue, with objective, deliverables, acceptance criteria, branch, and target branch.

### 2.6 Baseline

A controlled snapshot of repository state, governance state, artifact state, or program state approved according to governance rules.

### 2.7 Release

A versioned publication or communication of a repository state, artifact set, or deliverable set.

### 2.8 Traceability

The ability to follow intent, work, evidence, review, decision, and outcome across issues, artifacts, commits, PRs, baselines, and releases.

### 2.9 Ontology

A structured conceptual model that defines entity types, relations, meanings, and boundaries in the OMSP knowledge domain.

### 2.10 Maritime Operational Knowledge

The concepts, procedures, roles, constraints, systems, interactions, risks, and decisions that describe maritime operations.

### 2.11 Model-Based Engineering

An engineering approach where structured models and explicit relations guide design, analysis, implementation, validation, and governance.

### 2.12 Downstream Artifact

Any artifact that references or depends on canon, governance, engineering standards, or architecture foundations.

### 2.13 Human Accountability

The principle that final authority for approval, governance, baseline, release, and material decisions remains with accountable human roles or bodies.

### 2.14 AI Assistance

Use of AI to draft, summarize, compare, detect inconsistencies, prepare validation, or support review without replacing human accountability.

## 3. Naming Rules

OMSP terminology should:

- prefer explicit names over abbreviations;
- avoid multiple names for the same concept;
- define acronyms before use;
- preserve canonical capitalization for artifact names;
- use stable terms in governed artifacts.

## 4. Term Lifecycle

Terms may be:

- **Proposed**: suggested but not yet canonical;
- **Active**: approved for use;
- **Deprecated**: discouraged for new work;
- **Retired**: no longer used.

Material terminology changes should be traceable to an issue and reviewed PR.

## 5. Downstream Use

Downstream artifacts should reference this terminology when defining:

- artifact metadata;
- architecture concepts;
- governance responsibilities;
- traceability relations;
- baseline or release language;
- domain ontology concepts.

## 6. Related Canon Artifacts

- [Vision](./VISION.md) defines the long-term intent behind canonical terms.
- [Mission](./MISSION.md) defines the program purpose that terminology supports.
- [Philosophy](./PHILOSOPHY.md) explains why stable language matters to OMSP.
- [Principles](./PRINCIPLES.md) define rules that depend on consistent terminology.
- [Ontology Overview](./ONTOLOGY_OVERVIEW.md) turns terminology into concept and relation families.
- [Canon Index](./CANON_INDEX.md) provides the recommended reading order for downstream references.

## 7. Maintenance

This Terminology is maintained through issue-backed Work Packages and reviewed pull requests. Material changes require governance review and version metadata update.
