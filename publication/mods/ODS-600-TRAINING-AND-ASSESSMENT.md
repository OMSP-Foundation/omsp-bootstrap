---
Artifact-ID: OMSP-MODS-ODS-0600
Title: ODS-600 — Operational Training and Assessment Standard (Draft)
Version: 0.1.0
Status: Draft
Owner: toss-cengiz
Baseline: Sprint-8
Classification: Public
Related-Issue: WP-0084 / #205
Traceability:
  - ISSUE-205
  - EPIC-172
  - ISSUE-200
  - OMSP-MODS-SPEC-0001
  - OMSP-MODS-ODS-0100
  - OMSP-PLANNING-REBASELINE-0001
---

# ODS-600 — Operational Training and Assessment Standard (Draft)

> **Status: Draft.** This section is a v0.1 skeleton: the section structure
> and the normative rule framework are defined; content scales in later
> Work Packages, before the first training or assessment content is
> rendered (WP-0075 §4 / WP-0084).

## 1. Purpose and Scope

ODS-600 defines the structure of **training and assessment content**
derived from rendered operational documentation: competency objectives,
curriculum structure, and assessment criteria. It is part of the MODS
Specification
([`MODS_SPECIFICATION.md`](MODS_SPECIFICATION.md), `OMSP-MODS-SPEC-0001`)
and inherits its scope boundary: ODS-600 governs rendered operational
content only, never repository engineering artifacts.

Anchored existing foundation (per `OMSP-MODS-SPEC-0001` §4): the evidence
categories and verification/validation discipline that assessment
evidence must follow are defined by
[`validation/VALIDATION_FRAMEWORK.md`](../../validation/VALIDATION_FRAMEWORK.md).
ODS-600 adds no new evidence category and no new validation authority; it
states how training content presents objectives and evidence within those
categories.

Rule identifiers follow the pattern `ODS-600-R-NN` and are stable: a
withdrawn rule number is never reused.

## 2. Competency Objectives

**ODS-600-R-01 — Objectives derive from upper layers.** Every competency
objective traces to procedure, scenario, or system content of the upper
MODS stack layers (`OMSP-MODS-SPEC-0001` §3). Training content carries no
independent operational content: an objective with no upper-layer source
is non-conformant. (Stack analogue: the QRH derivation rule,
`OMSP-MODS-SPEC-0001` §3 rule 5.)

**ODS-600-R-02 — Objectives are observable.** Every competency objective
is formulated as an observable, assessable behavior or demonstration —
not as familiarity or awareness prose that cannot be assessed.

## 3. Curriculum Structure

**ODS-600-R-03 — Curriculum units reference their sources.** Every
curriculum unit references the rendered document sections (and thereby
the governed model content) it teaches, with the same traceability
discipline as the source documents themselves. Detailed curriculum
formats are **Reserved** (Section 5).

## 4. Assessment Criteria

**ODS-600-R-04 — Criteria map to objectives with evidence.** Every
assessment criterion maps to a competency objective (R-01) and names the
evidence that satisfies it, using the evidence categories of the anchored
validation framework. A criterion without an evidence definition is
non-conformant.

**ODS-600-R-05 — Assessment confers no authority.** No training or
assessment outcome rendered under this standard constitutes a
qualification, license, certification, or operational authorization of
any kind. Assessment records are advisory evidence only; any qualification
decision is a human authority outside MODS. This rule restates, for
training content, the boundary of `OMSP-MODS-SPEC-0001` §7.

## 5. Reserved Subtopics (not drafted in v0.1)

The following ODS-600 subtopics are **Reserved**. They carry no normative
content in v0.1 and are drafted in later Work Packages (see
`OMSP-MODS-SPEC-0001` §4):

### 5.1 Curriculum unit format and sequencing rules — Reserved

### 5.2 Assessment instruments and scoring — Reserved

### 5.3 Training-record structure and retention — Reserved

### 5.4 Scenario-based drill and simulation content rules — Reserved

## 6. Conformance Notes

- Conformance to ODS-600 is **advisory (non-gating) in v0.1**: the
  renderer conformance checklist
  ([`MODS_RENDERER_CONFORMANCE_CHECKLIST.md`](MODS_RENDERER_CONFORMANCE_CHECKLIST.md),
  `OMSP-MODS-CONFORMANCE-0001`) contains items for ODS-100 and ODS-300
  only; **only ODS-100/300 gate rendering conformance**. This draft adds
  no checklist items.
- Adding ODS-600 checklist items later is a human decision, taken after
  the first training content exercises these rules.
- No ODS-600 rule carries any certification, qualification, or
  operational-authority claim; the safety and authority boundary of
  `OMSP-MODS-SPEC-0001` §7 applies unchanged.
