---
Artifact-ID: OMSP-MODS-ODS-0200
Title: ODS-200 — Operational Document Graphic Standards (Draft)
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

# ODS-200 — Operational Document Graphic Standards (Draft)

> **Status: Draft.** This section is a v0.1 skeleton: the section structure
> and the normative rule framework are defined; content scales in later
> Work Packages. Findings from the first rendered golden-path output
> instance (Sprint 9, WP-0087) feed back into this document
> (WP-0075 §4 / WP-0084).

## 1. Purpose and Scope

ODS-200 defines the **visual presentation** rules of rendered operational
documents: warning-level presentation, typography roles, and color usage.
It is part of the MODS Specification
([`MODS_SPECIFICATION.md`](MODS_SPECIFICATION.md), `OMSP-MODS-SPEC-0001`)
and inherits its scope boundary: ODS-200 governs rendered operational
content only, never repository engineering artifacts.

Anchored existing foundation (per `OMSP-MODS-SPEC-0001` §4): the rendering
and publication pipeline is governed by
[`architecture/PUBLICATION_WORKFLOW.md`](../../architecture/PUBLICATION_WORKFLOW.md).
ODS-200 states presentation rules that renderers in that pipeline apply; it
does not redefine the pipeline, its phases, or its authority boundaries.

Scope demarcation inside MODS:

- The **text** of the advisory banner and of document components is
  governed by ODS-100; ODS-200 governs only their visual treatment.
- Diagram **content and derivation** rules are governed by ODS-400 and the
  Marine Diagram System
  ([`MDS-MARINE-DIAGRAM-SYSTEM.md`](MDS-MARINE-DIAGRAM-SYSTEM.md));
  ODS-200 governs the graphic treatment applied to diagrams when rendered.

Rule identifiers follow the pattern `ODS-200-R-NN` and are stable: a
withdrawn rule number is never reused.

## 2. Warning-Level Presentation

MODS documents use three warning levels. Their **semantics are defined by
this standard** (design lineage: aviation-style manuals; no external
standard is asserted or cited normatively):

| Level | Semantics in MODS documents |
| --- | --- |
| **WARNING** | Information whose disregard involves risk to people |
| **CAUTION** | Information whose disregard involves risk of damage to equipment or systems |
| **NOTE** | Operationally relevant information without a damage or injury dimension |

**ODS-200-R-01 — Fixed level set.** Rendered operational documents use
exactly these three levels with these names. A renderer neither invents
additional levels nor renames these.

**ODS-200-R-02 — Placement before the qualified content.** A warning-level
callout is rendered immediately **before** the step, section, or content
it qualifies — never after it, and never detached from it.

**ODS-200-R-03 — Level label is text, never color or icon alone.** Every
callout renders its level name (`WARNING` / `CAUTION` / `NOTE`) as visible
text. Color, icons, or other graphic treatment may supplement the label
but may never replace it: no warning-level meaning is carried by color or
iconography alone.

**ODS-200-R-04 — Visual distinction, palette reserved.** Callouts are
visually distinct from body text (in v0.1: at minimum a typographically
distinct label, e.g., bold uppercase). A normative color and icon
treatment per level is **Reserved** (Section 5); until it is drafted,
renderers apply typographic distinction only.

## 3. Typography Roles

**ODS-200-R-05 — Consistent text roles.** Every rendered operational
document distinguishes, consistently across the whole document, at least
these text roles: document title, section heading, body text, procedure
step text (ODS-300 constructs), warning-level label, and evidence/metadata
text. The same role always receives the same treatment within one
document. Concrete typeface, size, and spacing values are **Reserved**
(Section 5).

**ODS-200-R-06 — Advisory banner prominence.** The advisory banner
(text fixed by ODS-100-R-02) is rendered as the first content element,
visually distinct from body text, and never reduced below body-text
legibility. Its fixed wording is an ODS-100 concern; its prominence is
governed here.

## 4. Color Usage

**ODS-200-R-07 — Meaning is never color-alone.** No meaning in a rendered
operational document — warning level, state, identity, or emphasis — is
carried by color alone. Every color-supported meaning also has a textual
or structural carrier. This rule protects color-vision-deficient readers
and monochrome print output.

**ODS-200-R-08 — Warning colors are reserved.** Any color treatment
assigned to warning levels (once the Reserved palette is drafted) is
reserved for that purpose and is not reused for decoration, series
identity, or other document elements.

## 5. Reserved Subtopics (not drafted in v0.1)

The following ODS-200 subtopics are **Reserved**. They carry no normative
content in v0.1 and are drafted in later Work Packages (see
`OMSP-MODS-SPEC-0001` §4):

### 5.1 Normative color palette and its accessibility validation — Reserved

### 5.2 Iconography and symbol treatment for callouts — Reserved

### 5.3 Page layout and pagination (with ODS-100 §5.5) — Reserved

### 5.4 Typeface, size, and spacing values per text role — Reserved

### 5.5 Print/PDF and dark-mode output treatment — Reserved

## 6. Conformance Notes

- Conformance to ODS-200 is **advisory (non-gating) in v0.1**: the
  renderer conformance checklist
  ([`MODS_RENDERER_CONFORMANCE_CHECKLIST.md`](MODS_RENDERER_CONFORMANCE_CHECKLIST.md),
  `OMSP-MODS-CONFORMANCE-0001`) contains items for ODS-100 and ODS-300
  only; **only ODS-100/300 gate rendering conformance**. This draft adds
  no checklist items.
- Adding ODS-200 checklist items later is a human decision, taken after
  the first rendered instances exercise these rules.
- No ODS-200 rule carries any certification, compliance, or
  operational-authority claim; the safety and authority boundary of
  `OMSP-MODS-SPEC-0001` §7 applies unchanged.
