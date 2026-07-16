---
Artifact-ID: OMSP-MODS-ODS-0400
Title: ODS-400 — Operational Diagram Rules Standard (Draft)
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
  - OMSP-PLANNING-GOLDEN-PATH-0001
  - OMSP-PLANNING-REBASELINE-0001
---

# ODS-400 — Operational Diagram Rules Standard (Draft)

> **Status: Draft.** This section is a v0.1 skeleton: the section structure
> and the normative rule framework are defined; content scales in later
> Work Packages. Its first applied exercise is the golden-path
> energy-chain diagram view produced with this Work Package (WP-0084);
> findings from rendered instances (Sprint 9, WP-0087) feed back into this
> document (WP-0075 §4 / WP-0084).

## 1. Purpose and Scope

ODS-400 defines the rules for **diagrams in rendered operational
documents**: how diagrams derive from governed models, how their elements
are identified, and how their machine-readable sources are kept. It is
part of the MODS Specification
([`MODS_SPECIFICATION.md`](MODS_SPECIFICATION.md), `OMSP-MODS-SPEC-0001`)
and inherits its scope boundary: ODS-400 governs rendered operational
content only, never repository engineering artifacts.

Anchored existing foundation (per `OMSP-MODS-SPEC-0001` §4): the concept
contracts that diagram elements must trace to are defined by
[`ontology/OMSP_ONTOLOGY.md`](../../ontology/OMSP_ONTOLOGY.md) and the
machine-readable instance contracts under `schemas/`
([`schemas/MARITIME_INSTANCE_SCHEMAS.md`](../../schemas/MARITIME_INSTANCE_SCHEMAS.md)).
ODS-400 adds no new concept and no new schema; it states how instances of
those contracts are rendered as diagrams.

Division of labor: ODS-400 states the **vessel-agnostic rules**; the
concrete notation set, view classes, and source-file convention are the
**Marine Diagram System (MDS)**
([`MDS-MARINE-DIAGRAM-SYSTEM.md`](MDS-MARINE-DIAGRAM-SYSTEM.md),
`OMSP-MODS-MDS-0001`), which is the implementation of ODS-200/ODS-400
rules per `OMSP-MODS-SPEC-0001` §3. Graphic treatment (color, typography)
of diagrams is an ODS-200 concern.

Rule identifiers follow the pattern `ODS-400-R-NN` and are stable: a
withdrawn rule number is never reused.

## 2. Model Derivation Rules

**ODS-400-R-01 — Diagrams are derived views.** Every diagram in a rendered
operational document is a derived view of governed model instances. No
diagram element may exist only in the diagram: an element with no model
counterpart (and no declared external-boundary status, R-02) is
non-conformant. (Document-level analogue: ODS-100-R-08.)

**ODS-400-R-02 — Node identity.** Every diagram node traces to exactly one
model element identifier (equipment, system, or other governed instance),
or is explicitly declared an **external boundary** — an element outside
the modeled slice, visually distinguished per MDS notation. Undeclared,
untraceable nodes are non-conformant.

**ODS-400-R-03 — Edge identity.** Every diagram edge traces to exactly
one of: a connection instance, an interface instance, a declared model
relation (e.g., `protects`, `measures`), or a declared external-boundary
edge (R-02). An interface that has no realized connection (e.g., an
option path) is visually distinguished from a realized connection per MDS
notation; rendering it as realized is non-conformant.

**ODS-400-R-04 — Direction fidelity.** Edge direction renders the model's
declared direction (source port → target port). A renderer never invents,
reverses, or omits direction.

**ODS-400-R-05 — Unknowns rendered explicitly.** Structural unknowns of
the modeled slice (e.g., unknown presence or quantity of an element) are
rendered visibly as unknown, never hidden and never rendered as
established fact. (Document-level analogue: ODS-100-R-07.)

**ODS-400-R-06 — Identifier mapping table.** Every diagram is accompanied
by a mapping table that resolves each diagram label to the full model
element identifier and its source file, including the port endpoints of
every rendered edge. Diagram labels may abbreviate; the mapping table may
not.

## 3. View Classes

**ODS-400-R-07 — Declared view class.** Every diagram declares its view
class. The v0.1 view classes are defined by MDS
(`OMSP-MODS-MDS-0001` §2): the **energy-chain view** and the
**interface view**. A diagram of an undefined view class is
non-conformant; introducing a new view class is an MDS revision, not an
instance decision.

## 4. Machine-Readable Sources

**ODS-400-R-08 — Text-based source in the repository.** Every diagram has
a text-based, machine-readable source kept in the repository, located and
formatted per the MDS source convention (`OMSP-MODS-MDS-0001` §4). A
diagram whose only form is a binary image is non-conformant.

**ODS-400-R-09 — Rendered images are derived.** Any rendered image (SVG,
PNG, PDF embedding) is derived from the text source and is regenerable
from it. Rendered images are never hand-edited; corrections are made in
the model or in the diagram source and the image is regenerated.
(Document-level analogue: ODS-100-R-09.)

## 5. Reserved Subtopics (not drafted in v0.1)

The following ODS-400 subtopics are **Reserved**. They carry no normative
content in v0.1 and are drafted in later Work Packages (see
`OMSP-MODS-SPEC-0001` §4):

### 5.1 Symbol library beyond the MDS v0.1 notation set — Reserved

### 5.2 Multi-system and composite diagram views — Reserved

### 5.3 Spatial/geometric arrangement diagrams (compartments, routing) — Reserved

### 5.4 Interface families beyond `electrical-power` — Reserved

### 5.5 Automated generation of diagram sources from model instances — Reserved

## 6. Conformance Notes

- Conformance to ODS-400 is **advisory (non-gating) in v0.1**: the
  renderer conformance checklist
  ([`MODS_RENDERER_CONFORMANCE_CHECKLIST.md`](MODS_RENDERER_CONFORMANCE_CHECKLIST.md),
  `OMSP-MODS-CONFORMANCE-0001`) contains items for ODS-100 and ODS-300
  only; **only ODS-100/300 gate rendering conformance**. This draft adds
  no checklist items.
- The first applied exercise of these rules is the golden-path
  energy-chain diagram view
  ([`reference/hanse460/diagrams/ENERGY-CHAIN-VIEW.md`](../../reference/hanse460/diagrams/ENERGY-CHAIN-VIEW.md));
  its findings feed back into this draft. Adding ODS-400 checklist items
  later is a human decision.
- No ODS-400 rule carries any certification, compliance, or
  operational-authority claim; the safety and authority boundary of
  `OMSP-MODS-SPEC-0001` §7 applies unchanged.
