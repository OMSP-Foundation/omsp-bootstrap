---
Artifact-ID: OMSP-MODS-ODS-0500
Title: ODS-500 — Operational Risk Assessment Standard (Draft)
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

# ODS-500 — Operational Risk Assessment Standard (Draft)

> **Status: Draft.** This section is a v0.1 skeleton: the section structure
> and the normative rule framework are defined; content scales in later
> Work Packages, before the first operational risk content is rendered
> (WP-0075 §4 / WP-0084).

## 1. Purpose and Scope

ODS-500 defines how **risk information is presented in rendered
operational documents**: hazard identification, risk evaluation,
mitigation, and residual-risk statements. It is part of the MODS
Specification
([`MODS_SPECIFICATION.md`](MODS_SPECIFICATION.md), `OMSP-MODS-SPEC-0001`)
and inherits its scope boundary — with the authority-overlap rule applied
explicitly:

- Anchored existing foundation (per `OMSP-MODS-SPEC-0001` §4):
  **repository engineering risk artifacts** are governed by
  [`templates/RISK_TEMPLATE.md`](../../templates/RISK_TEMPLATE.md) and the
  existing governance standards. ODS-500 does not redefine that template,
  its lifecycle, or any acceptance authority.
- ODS-500 governs only the **rendered operational presentation** of risk
  content (e.g., the safety-constraints subsection of a scenario section,
  ODS-100-R-04.4, and future operational risk-assessment sections).

Rule identifiers follow the pattern `ODS-500-R-NN` and are stable: a
withdrawn rule number is never reused.

## 2. Hazard Identification Presentation

**ODS-500-R-01 — Hazard statement structure.** Every rendered hazard
statement names, at minimum: the hazard, the affected system or equipment
(by model element reference), and the mechanism or condition under which
the hazard applies. Free-floating hazard prose without these elements is
non-conformant.

**ODS-500-R-02 — Hazard traceability.** Every rendered hazard statement
traces to a model element and to a source reference (for the golden path:
a source-register entry) or to a governed scenario definition — or carries
an explicit `unknown` evidence marker. (Document-level analogue:
ODS-100-R-05.)

**ODS-500-R-03 — Unknown risk is stated, never omitted.** Where hazard
identification for a rendered slice is incomplete or unestablished, the
document states this explicitly. Silence about unassessed risk is
non-conformant. (Document-level analogue: ODS-100-R-07.)

## 3. Risk Evaluation Presentation

**ODS-500-R-04 — Evaluation method reference.** Any rendered risk rating
(qualitative or quantitative) names the method and inputs it was produced
with. A rating without a method reference is non-conformant. The normative
matrix dimensions and scales are **Reserved** (Section 5).

**ODS-500-R-05 — Ratings carry evidence class.** A rendered risk rating is
presented with the authority class of its inputs, never as an unqualified
fact. (Document-level analogue: ODS-100-R-06.)

## 4. Mitigation and Residual Risk

**ODS-500-R-06 — Mitigation traceability.** Every rendered mitigation
traces to the procedure (ODS-300 constructs), equipment role, or
constraint that implements it. An untraceable mitigation claim is
non-conformant.

**ODS-500-R-07 — Residual-risk acceptance is a human authority.** A
rendered document never states, implies, or generates residual-risk
**acceptance**. Where an acceptance exists, the document references the
identified human decision record; where none exists, the residual risk is
rendered as open. This rule restates, for rendered content, the human
authority boundary of `OMSP-MODS-SPEC-0001` §7.

## 5. Reserved Subtopics (not drafted in v0.1)

The following ODS-500 subtopics are **Reserved**. They carry no normative
content in v0.1 and are drafted in later Work Packages (see
`OMSP-MODS-SPEC-0001` §4):

### 5.1 Normative risk matrix dimensions and scales — Reserved

### 5.2 Scoring and aggregation method — Reserved

### 5.3 Operational risk-register composition and its document placement — Reserved

### 5.4 Presentation of risk trends across document revisions — Reserved

## 6. Conformance Notes

- Conformance to ODS-500 is **advisory (non-gating) in v0.1**: the
  renderer conformance checklist
  ([`MODS_RENDERER_CONFORMANCE_CHECKLIST.md`](MODS_RENDERER_CONFORMANCE_CHECKLIST.md),
  `OMSP-MODS-CONFORMANCE-0001`) contains items for ODS-100 and ODS-300
  only; **only ODS-100/300 gate rendering conformance**. This draft adds
  no checklist items.
- Adding ODS-500 checklist items later is a human decision, taken after
  the first rendered risk content exercises these rules.
- No ODS-500 rule carries any certification, compliance, or
  operational-authority claim, and nothing rendered under it constitutes a
  risk acceptance; the safety and authority boundary of
  `OMSP-MODS-SPEC-0001` §7 applies unchanged.
