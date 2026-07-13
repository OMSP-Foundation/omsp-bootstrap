---
Artifact-ID: OMSP-MODS-CONFORMANCE-0001
Title: MODS Renderer Conformance Checklist v0.1
Version: 0.1.0
Status: Draft
Owner: toss-cengiz
Baseline: Sprint-7
Classification: Public
Related-Issue: WP-0079 / #200
Traceability:
  - ISSUE-200
  - OMSP-MODS-SPEC-0001
  - OMSP-MODS-ODS-0100
  - OMSP-MODS-ODS-0300
  - OMSP-PLANNING-GOLDEN-PATH-0001
  - OMSP-REFERENCE-SCENARIO-0001
  - OMSP-PLANNING-REBASELINE-0001
---

# MODS Renderer Conformance Checklist v0.1

## 1. Purpose and Execution Rules

This checklist is the operational definition of **MODS-conformant** for
rendered operational documents and their renderers
([`MODS_SPECIFICATION.md`](MODS_SPECIFICATION.md) §6). It is executed
against one rendered document instance at a time.

Execution rules:

1. Every checklist item traces to a normative rule ID (`ODS-100-R-NN` /
   `ODS-300-R-NN`). An item without a rule ID is invalid and may not be
   added.
2. Each executed item records its evidence per the item's evidence type:
   - **output inspection** — cited excerpt or section reference of the
     rendered document;
   - **diff** — a comparison command output (e.g., against the fixed
     banner text or a regenerated document);
   - **command** — a command invocation and its output.
3. In v0.1 the checklist is run **manually** by a human reviewer. A
   machine-readable `ods-lint` implementation is recorded future work (see
   Section 4); it is not part of this Work Package and is not implemented
   here.
4. A passing run is verification evidence only. It confers no approval,
   baseline, release, or operational authority; acceptance of a conformance
   claim is a human decision.

Result recording: item ID, PASS/FAIL, evidence, reviewer, date, document
instance reference (source model version + generation commit,
ODS-100-R-10).

## 2. Document Structure (ODS-100)

| Item | Check statement | Traces to | Evidence type |
| --- | --- | --- | --- |
| CC-01 | The rendered document contains all four mandatory components: system overview, scenario section, evidence appendix, advisory banner. | ODS-100-R-01 | output inspection |
| CC-02 | The document begins with the advisory banner, and the banner text matches the ODS-100 fixed text **verbatim** (word-for-word, no modification). | ODS-100-R-02 | diff (rendered banner vs. ODS-100 §2 fixed text) |
| CC-03 | The system overview presents every modeled element of the documented slice with role, key values, and protection; no slice element is missing. | ODS-100-R-03 | output inspection (overview vs. model element list) |
| CC-04 | Every key value in the system overview carries an authority class or an explicit `unknown`. | ODS-100-R-03 | output inspection |
| CC-05 | Each scenario section contains all six subsections: affected systems, likely causes, inspection sequence, safety constraints, related equipment, source documents. | ODS-100-R-04 | output inspection |
| CC-06 | Every scenario line item is traceable to a model element and a source-register entry, or carries an explicit `unknown` evidence marker. | ODS-100-R-05 | output inspection (sampled line items traced to model + register) |
| CC-07 | The evidence appendix records authority class and source reference for every rendered claim; no rendered claim lacks an appendix entry. | ODS-100-R-06 | output inspection (sampled claims cross-checked against appendix) |
| CC-08 | All `unknown` / `<to-be-sourced>` values are rendered visibly in place and listed in the evidence appendix; none are omitted or paraphrased away. | ODS-100-R-07 | diff (model unknown count vs. rendered unknown count) |
| CC-09 | The document declares its source model reference and generation provenance, and contains no content absent from the source model. | ODS-100-R-08 | output inspection + command (regeneration from the declared source) |
| CC-10 | The rendered document is byte-identical to a regeneration from its declared source; no manual edits are present. | ODS-100-R-09 | command (regenerate + diff) |
| CC-11 | The document carries the metadata minimum: source model identity and version, generator identity and version, generation source reference, and the MODS/ODS version it claims conformance to. | ODS-100-R-10 | output inspection |

## 3. Procedure Language (ODS-300)

| Item | Check statement | Traces to | Evidence type |
| --- | --- | --- | --- |
| CC-12 | Every action/observation step is written in the imperative mood. | ODS-300-R-01 | output inspection |
| CC-13 | Every step contains exactly one action or one observation; no compound instructions. | ODS-300-R-02 | output inspection |
| CC-14 | Every step renders its sequence number, stable step ID, and responsible-actor label. | ODS-300-R-03 | output inspection |
| CC-15 | Every step renders entry criterion, completion criterion, and expected observation; unestablished criteria appear as explicit unknowns, not blanks. | ODS-300-R-04 | output inspection |
| CC-16 | Every human-confirmation-mandatory step carries the explicit `[HUMAN CONFIRMATION REQUIRED]` marker. | ODS-300-R-05 | output inspection (markers vs. source scenario confirmation flags) |
| CC-17 | Every step renders hazards/safeguards and an escalation block; steps with no identified hazard state so explicitly. | ODS-300-R-06 | output inspection |
| CC-18 | Every decision point is rendered as a first-class construct with all five fields: branches, decision authority, required evidence, time sensitivity, fallback behavior. | ODS-300-R-07 | output inspection |
| CC-19 | Every decision point includes the conservative human-review branch for unknown or conflicting evidence. | ODS-300-R-08 | output inspection |
| CC-20 | No `unknown` / `<to-be-sourced>` step value is hidden, dropped, or replaced with a guessed value. | ODS-300-R-09 | diff (source scenario unknowns vs. rendered steps) |
| CC-21 | Every step references at least one equipment role and at least one source reference, or carries an explicit `unknown` evidence marker. | ODS-300-R-10 | output inspection (sampled steps traced to model + register) |
| CC-22 | No source scenario step or decision field (`OMSP-REFERENCE-SCENARIO-0001` §7) has been dropped by the renderer; the ODS-300 §2 mapping is fully expressed. | ODS-300-R-01…R-10 (mapping table, ODS-300 §2) | diff (source scenario fields vs. rendered fields) |

## 4. Future Work (recorded, not implemented)

A machine-readable `ods-lint` check that automates items of this checklist
is planned future tooling (see `OMSP-MODS-SPEC-0001` and the skill roadmap
in program planning). Until it exists, manual execution with recorded
evidence is the only conformance path. This note creates no Work Package
and implements nothing.
