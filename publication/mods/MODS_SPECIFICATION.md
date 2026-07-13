---
Artifact-ID: OMSP-MODS-SPEC-0001
Title: MODS Specification v0.1 — Maritime Operations Documentation Standard
Version: 0.1.0
Status: Draft
Owner: toss-cengiz
Baseline: Sprint-7
Classification: Public
Related-Issue: WP-0079 / #200
Traceability:
  - ISSUE-200
  - OMSP-PLANNING-GOLDEN-PATH-0001
  - OMSP-REFERENCE-SCENARIO-0001
  - OMSP-PLANNING-REBASELINE-0001
---

# MODS Specification v0.1 — Maritime Operations Documentation Standard

> **Status: Draft.** This specification is subject to revision by the first
> conformance test: the first golden-path output instance produced in
> Sprint 9 (WP-0087) is the first conformance test of these sections, and
> its findings feed back into this document (WP-0075 §4 / WP-0079).

## 1. Purpose and Scope

**MODS (Maritime Operations Documentation Standard)** is the OMSP standard
for maritime **operational documentation content**: the human-readable
manuals, procedures, scenario renderings, and quick-reference material
derived from governed OMSP models. This project does not produce a single
boat book; it produces its own operational documentation standard, and every
book is an instance of that standard.

Scope boundary (binding):

- MODS governs **operational documentation content only** — its structure,
  language, evidence presentation, and conformance.
- The authority over repository engineering artifacts (canon, governance,
  planning, reference models, schemas, validation) remains with the existing
  standards recorded in
  [`governance/CANONICAL_AUTHORITY_MAP.md`](../../governance/CANONICAL_AUTHORITY_MAP.md).
  **Authority overlap is prohibited:** where a MODS/ODS rule would overlap an
  existing repository standard, the MODS/ODS rule is narrowed and refers to
  the existing standard instead. MODS never redefines repository artifact
  lifecycle, metadata, or approval authority.

Methodology anchor: spec-first ordering is a binding rule of the domain
re-baseline
([`planning/WP-0075-DOMAIN-BACKLOG-REBASELINE.md`](../../planning/WP-0075-DOMAIN-BACKLOG-REBASELINE.md)
§2.2) and of the golden-path definition
([`planning/WP-0074-GOLDEN-PATH-DEFINITION.md`](../../planning/WP-0074-GOLDEN-PATH-DEFINITION.md)
§7.2): standards precede content, and content becomes the first conformance
test of the standard.

## 2. Three-Layer Architecture and Vessel-Agnosticism

MODS content is organized in three mandatory layers:

| Layer | Content | Lives in |
| --- | --- | --- |
| 1. ODS standard | Vessel-agnostic rules for structure, language, diagrams, risk, training | `publication/mods/` ODS artifacts |
| 2. Schema / template | Machine-readable and reusable carriers of the ODS rules | `schemas/`, `templates/` (delivered with the owning ODS series) |
| 3. Vessel instance | Vessel-specific rendered content | Instance artifacts (first: Hanse 460 golden-path output) |

Rules:

1. **Vessel-agnosticism (primary intent).** The ODS layer states rules
   independent of vessel type; vessel-specific content lives only in the
   instance layer. If an ODS rule embeds a Hanse 460-specific assumption,
   that is a design defect: the rule is generalized and the specific content
   moves to an instance example.
2. **Hanse 460 is the first reference implementation**, not a privileged
   case. Deriving a second vessel type (Horizon 3) is the validity proof of
   the ODS layer.
3. Each ODS series artifact is a governed artifact with its own
   Artifact-ID (`OMSP-MODS-ODS-<series>`), its own WP/issue/PR flow, and —
   when its rules require machine-readable carriers — accompanying
   `schemas/` and `templates/` counterparts.

## 3. Binding Stack Order (Spec-First Product Architecture)

The MODS product stack and its **mandatory development order** are:

1. **MODS Specification** (this artifact and its ODS sections) — rules,
   terminology, structure, coding/numbering, revision and quality.
2. **Marine Diagram System (MDS)** — vector component library and visual
   language; the concrete implementation of ODS-200/ODS-400 rules.
3. **Core Operations Manual** — vessel-agnostic common operational content.
4. **Vessel Definition Module (VDM)** — model-specific deltas extending or
   overriding Core; the first VDM is Hanse 460.
5. **Scenario Library** — validated operational scenarios, traceable to
   [`reference/OPERATIONAL_SCENARIO_MODEL.md`](../../reference/OPERATIONAL_SCENARIO_MODEL.md).
6. **Quick Reference Handbook (QRH)** — short field checklists derived from
   upper layers; carries no independent content.

Stack rules (binding):

1. **Order is binding.** Content for layer N may not be produced unless
   layer N−1 exists as a governed artifact in at least Draft/Review status.
   Source of the rule:
   [`planning/WP-0074-GOLDEN-PATH-DEFINITION.md`](../../planning/WP-0074-GOLDEN-PATH-DEFINITION.md)
   §7.2 and
   [`planning/WP-0075-DOMAIN-BACKLOG-REBASELINE.md`](../../planning/WP-0075-DOMAIN-BACKLOG-REBASELINE.md)
   §2.2. Work that breaks the order is reported, not executed.
2. **Standard before content.** Before the first instance of a document type
   is written, the relevant ODS section must be at least Draft. The first
   instance is the first conformance test of that section.
3. **Delta architecture.** A VDM carries only differences from Core; copying
   Core content into a VDM is prohibited (single-source rule). A new vessel
   model means only a new VDM; if MODS, MDS, and Core remain unchanged, the
   architecture is working.
4. **Scenario validation.** Scenario Library entries require real validation
   evidence per
   [`validation/VALIDATION_FRAMEWORK.md`](../../validation/VALIDATION_FRAMEWORK.md)
   categories; an unvalidated scenario stays in Draft and may not enter the
   QRH.
5. **QRH derivation.** Every QRH item traces to its source
   abnormal/emergency procedure with a `traces-to` relation; a sourceless
   QRH item is not accepted.
6. **Long-term publication discipline.** Every new section, diagram, and
   procedure passes a conformance check against this architecture;
   non-conformance produces a correction proposal, not silent acceptance.

## 4. ODS Series Map

The ODS (Operations Documentation Standard) series are the sections of this
specification. Artifact-ID convention: `OMSP-MODS-ODS-<series number>`
(e.g., ODS-100 → `OMSP-MODS-ODS-0100`).

| Series | Scope | Anchored existing foundation | v0.1 status |
| --- | --- | --- | --- |
| **ODS-100** Document structure | Document taxonomy, sectioning, numbering, rendered-document metadata, versioning | [`governance/ENGINEERING_ARTIFACT_STANDARD.md`](../../governance/ENGINEERING_ARTIFACT_STANDARD.md), [`governance/METADATA_AND_TRACEABILITY_STANDARD.md`](../../governance/METADATA_AND_TRACEABILITY_STANDARD.md) | **Draft** — [`ODS-100-DOCUMENT-STRUCTURE.md`](ODS-100-DOCUMENT-STRUCTURE.md) |
| **ODS-200** Graphic standards | Typography, color/icon language, warning levels (Warning/Caution/Note), page layout | [`architecture/PUBLICATION_WORKFLOW.md`](../../architecture/PUBLICATION_WORKFLOW.md) | Reserved — Sprint-8 / WP-0084 (#205) |
| **ODS-300** Procedure language | Imperative step language, step granularity, challenge–response checklist language, role assignments, condition blocks | [`reference/OPERATIONAL_SCENARIO_MODEL.md`](../../reference/OPERATIONAL_SCENARIO_MODEL.md) §7 | **Draft** — [`ODS-300-PROCEDURE-LANGUAGE.md`](ODS-300-PROCEDURE-LANGUAGE.md) |
| **ODS-400** Diagram rules | System schematics, flow diagrams, symbol library, machine-readable diagram sources | [`ontology/OMSP_ONTOLOGY.md`](../../ontology/OMSP_ONTOLOGY.md), `schemas/` | Reserved — Sprint-8 / WP-0084 (#205) |
| **ODS-500** Risk assessment standard | Hazard identification, risk matrix, mitigation, residual-risk acceptance | [`templates/RISK_TEMPLATE.md`](../../templates/RISK_TEMPLATE.md) | Reserved — Sprint-8 / WP-0084 (#205) |
| **ODS-600** Training and assessment standard | Competency objectives, curriculum structure, assessment criteria | [`validation/VALIDATION_FRAMEWORK.md`](../../validation/VALIDATION_FRAMEWORK.md) | Reserved — Sprint-8 / WP-0084 (#205) |

Reserved series carry **no normative content** in v0.1; only this map entry
exists. Drafting them ahead of WP-0084 would break WP scoping, not the stack
order.

Extensibility: the series grows in blocks of 100 (e.g., ODS-700+ for new
needs); opening a new block requires governance review.

## 5. Versioning

- MODS Specification and each ODS series artifact are versioned with
  **Semantic Versioning** in their governed `Version` metadata, per
  [`governance/ENGINEERING_PLAYBOOK.md`](../../governance/ENGINEERING_PLAYBOOK.md).
- MODS versions are **independent** of ontology (`ontology/`) and schema
  (`schemas/`) versions. A MODS revision does not imply an ontology or
  schema revision, and vice versa; cross-references between them name the
  version they were written against.
- A change that alters the meaning of a normative rule (rule semantics,
  mandatory component set, fixed text) is at least a **minor** version
  change; removing or breaking a rule is a **major** change.

## 6. Conformance Model

A rendered operational document or a renderer is **MODS-conformant** when it
demonstrably passes every applicable item of the
[`MODS_RENDERER_CONFORMANCE_CHECKLIST.md`](MODS_RENDERER_CONFORMANCE_CHECKLIST.md)
(`OMSP-MODS-CONFORMANCE-0001`), with recorded evidence per item.

- Conformance is claimed per document instance and per checklist version;
  there is no blanket conformance claim.
- In v0.1 the checklist is executed **manually** by a human reviewer;
  passing it is verification evidence only and confers no approval,
  baseline, or release authority.
- The first conformance test is the Sprint-9 golden-path output instance
  (WP-0087); its findings revise this specification.

## 7. Safety and Authority Boundary

- No MODS output carries any certification, seaworthiness, compliance, or
  operational-authority claim. Every MODS output is **advisory** and is
  governed by
  [`reference/DIGITAL_TWIN_GOVERNANCE_AND_SAFETY_BOUNDARIES.md`](../../reference/DIGITAL_TWIN_GOVERNANCE_AND_SAFETY_BOUNDARIES.md).
- MODS documents never replace manufacturer documentation, approved vessel
  procedures, or the judgment of the responsible human.
- The mandatory advisory banner and its fixed text are defined in ODS-100.
- Adoption, promotion beyond Draft, and any conformance acceptance are
  human decisions; this specification proposes, it does not approve.
