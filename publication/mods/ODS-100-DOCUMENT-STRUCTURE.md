---
Artifact-ID: OMSP-MODS-ODS-0100
Title: ODS-100 — Operational Document Structure Standard (Draft)
Version: 0.1.0
Status: Draft
Owner: toss-cengiz
Baseline: Sprint-7
Classification: Public
Related-Issue: WP-0079 / #200
Traceability:
  - ISSUE-200
  - OMSP-MODS-SPEC-0001
  - OMSP-PLANNING-GOLDEN-PATH-0001
  - OMSP-REFERENCE-SCENARIO-0001
  - OMSP-PLANNING-REBASELINE-0001
---

# ODS-100 — Operational Document Structure Standard (Draft)

> **Status: Draft.** This section is subject to revision by the first
> conformance test: the first golden-path output instance produced in
> Sprint 9 (WP-0087) is the first conformance test of these rules, and its
> findings feed back into this document (WP-0075 §4 / WP-0079).

## 1. Purpose and Scope

ODS-100 defines the mandatory structure of **rendered operational
documents** produced from governed OMSP models. It is part of the MODS
Specification
([`MODS_SPECIFICATION.md`](MODS_SPECIFICATION.md), `OMSP-MODS-SPEC-0001`)
and inherits its scope boundary: ODS-100 governs rendered operational
content only, never repository engineering artifacts.

v0.1 normatively covers the structure required for the first golden-path
output — the Hanse 460 service-battery scenario document defined in
[`planning/WP-0074-GOLDEN-PATH-DEFINITION.md`](../../planning/WP-0074-GOLDEN-PATH-DEFINITION.md)
§7.1. All other document-structure topics are Reserved (Section 5).

Rule identifiers follow the pattern `ODS-100-R-NN` and are stable: a
withdrawn rule number is never reused.

## 2. Mandatory Document Components

**ODS-100-R-01 — Four mandatory components.** Every rendered operational
document contains all four of the following components. None may be omitted
or merged away:

1. **System overview** — the modeled system chain (for the golden path: the
   energy chain shore power → charger → battery bank → DC distribution →
   consumers, with the inverter branch).
2. **Scenario section** — one section per rendered operational scenario.
3. **Evidence appendix** — the evidence record for every rendered claim.
4. **Advisory banner** — the fixed advisory text of ODS-100-R-02.

Source: golden-path output specification, WP-0074 §7.1 items (1)–(4).

**ODS-100-R-02 — Advisory banner, fixed text.** Every rendered operational
document begins with the following banner text. The text is **normative and
fixed word-for-word**: renderers reproduce it verbatim, without
modification, abbreviation, or paraphrase. Changing this text is a version
change of ODS-100, never a renderer or instance decision.

> **ADVISORY MATERIAL — NOT A CERTIFIED PROCEDURE.** This document is
> advisory knowledge material generated from a governed model. It is not a
> certified procedure and does not replace manufacturer documentation,
> approved vessel procedures, or the judgment of the responsible human. It
> carries no seaworthiness, compliance, or navigation-safety claim, and it
> does not authorize navigation, maintenance, or emergency action. Every
> safety-relevant conclusion requires human judgment. Where this document
> conflicts with manufacturer documentation or the responsible human's
> judgment, the latter prevail.

Derivation: WP-0074 §7.1(4) and §12, and the disclaimer and presentation
rules of
[`reference/DIGITAL_TWIN_GOVERNANCE_AND_SAFETY_BOUNDARIES.md`](../../reference/DIGITAL_TWIN_GOVERNANCE_AND_SAFETY_BOUNDARIES.md)
(§5, §11).

**ODS-100-R-03 — System overview content.** The system overview presents
every modeled element of the documented slice with, at minimum: its role,
its key values — each value carrying its authority class or an explicit
`unknown` — and its protection (protective devices in its path, or an
explicit `unknown`). No element of the modeled slice is silently omitted.

**ODS-100-R-04 — Scenario section content.** Each scenario section
contains, at minimum, all six of the following subsections:

1. affected systems;
2. likely causes;
3. inspection sequence (written in ODS-300 procedure language);
4. safety constraints;
5. related equipment;
6. source documents.

**ODS-100-R-05 — Scenario line-item traceability.** Every line item in a
scenario section is traceable to a model element and to a source-register
entry (for the golden path:
[`reference/HANSE_460_SOURCE_REGISTER.md`](../../reference/HANSE_460_SOURCE_REGISTER.md))
or carries an explicit `unknown` evidence marker.

## 3. Evidence Presentation

**ODS-100-R-06 — Evidence appendix.** The evidence appendix records, for
**every** claim rendered in the document, the claim's authority class and
its source reference. A rendered claim without an evidence-appendix entry is
non-conformant.

**ODS-100-R-07 — Unknowns are listed, never hidden.** Values or claims whose
evidence state is `unknown` or `<to-be-sourced>` are rendered visibly as
such, in place and in the evidence appendix. Omitting, hiding, or
paraphrasing away an unknown is non-conformant. An unknown is an accepted
document state, not a rendering failure.

## 4. Derived-Artifact Rules

**ODS-100-R-08 — Rendered documents are derived artifacts.** Every rendered
operational document declares its source model reference and its generation
provenance. No content may exist only in the rendered document: every
statement derives from the source model (single-source rule, WP-0074 §7.2).

**ODS-100-R-09 — No manual editing.** Rendered documents are never edited
by hand. Corrections are made in the source model (or the renderer) and the
document is regenerated. A hand-edited rendered document is non-conformant
and its content is void as evidence.

**ODS-100-R-10 — Rendered-document metadata minimum.** Every rendered
operational document carries at least the following metadata, visibly or in
a machine-readable header:

1. source model identity and **model version** from which it was generated;
2. generator identity and version (tool or pipeline reference);
3. generation source reference (repository commit or equivalent);
4. the MODS/ODS specification version the document claims conformance to.

## 5. Reserved Subtopics (not drafted in v0.1)

The following ODS-100 subtopics are **Reserved**. They carry no normative
content in v0.1 and are drafted in later Work Packages (see
`OMSP-MODS-SPEC-0001` §4):

### 5.1 Document taxonomy — Reserved

### 5.2 Sectioning and numbering scheme — Reserved

### 5.3 Published-document versioning and revision marking — Reserved

### 5.4 Multi-scenario and multi-system document composition — Reserved

### 5.5 Page layout and pagination (with ODS-200) — Reserved

## 6. Conformance

Conformance to ODS-100 is checked with
[`MODS_RENDERER_CONFORMANCE_CHECKLIST.md`](MODS_RENDERER_CONFORMANCE_CHECKLIST.md)
(`OMSP-MODS-CONFORMANCE-0001`). The first conformance test is the Sprint-9
golden-path output instance (WP-0087).
