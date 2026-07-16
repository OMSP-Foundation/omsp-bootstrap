---
Artifact-ID: OMSP-MODS-MDS-0001
Title: Marine Diagram System (MDS) v0.1 (Draft)
Version: 0.1.0
Status: Draft
Owner: toss-cengiz
Baseline: Sprint-8
Classification: Public
Related-Issue: WP-0084 / #205
Depends-On:
  - OMSP-MODS-ODS-0200
  - OMSP-MODS-ODS-0400
Traceability:
  - ISSUE-205
  - EPIC-172
  - ISSUE-200
  - OMSP-MODS-SPEC-0001
  - OMSP-PLANNING-GOLDEN-PATH-0001
  - OMSP-PLANNING-REBASELINE-0001
---

# Marine Diagram System (MDS) v0.1 (Draft)

> **Status: Draft.** MDS v0.1 defines the minimal notation set and source
> convention needed by the golden path. Its first applied instance is the
> Hanse 460 energy-chain diagram view (Section 5); findings from applied
> instances feed back into this document (WP-0075 §4 / WP-0084).

## 1. Purpose and Position in the Stack

The **Marine Diagram System (MDS)** is the concrete visual language of
MODS diagrams: the notation set, the view classes, and the
machine-readable source convention. In the binding MODS stack
([`MODS_SPECIFICATION.md`](MODS_SPECIFICATION.md) §3,
`OMSP-MODS-SPEC-0001`), MDS is stack layer 2 — the implementation of the
ODS-200/ODS-400 rules:

- [`ODS-400-DIAGRAM-RULES.md`](ODS-400-DIAGRAM-RULES.md)
  (`OMSP-MODS-ODS-0400`) states the vessel-agnostic diagram rules; MDS
  realizes them as a concrete notation.
- [`ODS-200-GRAPHIC-STANDARDS.md`](ODS-200-GRAPHIC-STANDARDS.md)
  (`OMSP-MODS-ODS-0200`) governs graphic treatment; MDS v0.1 is
  deliberately monochrome-default and carries no meaning by color alone
  (ODS-200-R-07).

Placement decision: MDS is a **separate governed artifact**, not a
section of ODS-400, because the MODS stack (§3) names MDS as its own
layer and because ODS-400 rules are vessel- and notation-agnostic while
MDS binds them to a concrete notation and format that will grow
(component library, further view classes) on its own revision cadence.

Rule identifiers follow the pattern `MDS-R-NN` and are stable: a
withdrawn rule number is never reused.

## 2. View Classes (v0.1)

MDS v0.1 defines exactly two view classes (per ODS-400-R-07). Every MDS
diagram declares which class it renders.

### 2.1 Energy-chain view

- **Purpose:** one system slice's energy flow — sources → storage →
  distribution → consumers — as a node-link diagram.
- **Content rule:** the view renders **every** equipment role of the
  modeled slice, including protection and measurement roles (as
  annotation nodes, MDS-R-06), and every connection and declared
  interface between them. Omitting a modeled slice element is
  non-conformant (ODS-400-R-01/R-02).
- **Value rule:** the energy-chain view renders **structure only**:
  element identity, flow direction, realized/unrealized status, and
  explicit structural unknowns (presence, quantity). It renders no
  attribute values (capacities, ratings, limits); attribute values and
  their provenance belong to interface views and document tables.
- **Reading direction:** energy flows from sources on the left/top to
  consumers on the right/bottom.

### 2.2 Interface view

- **Purpose:** the typed contract of **one** interface (and its realizing
  connection, if any) in detail.
- **Content rule:** the view renders the two endpoint equipment roles,
  the interface edge with its port endpoints, and an accompanying fact
  table with, at minimum: interface family, direction, media, and nominal
  limits — every value carrying its authority class or an explicit
  `unknown` (ODS-100-R-03 analogue, ODS-400-R-05).

## 3. Notation Set (v0.1)

**MDS-R-01 — Source format.** The v0.1 machine-readable diagram source
format is a **Mermaid `flowchart`** definition. Other text-based formats
(e.g., PlantUML) are Reserved (Section 6).

**MDS-R-02 — Equipment node.** A modeled equipment role is a rectangular
node. Its label carries the human-readable name and the model **local
ID** on a second line. The full model ID resolves through the mapping
table (MDS-R-08).

**MDS-R-03 — External boundary node.** An element outside the modeled
slice (e.g., the shore supply) is a stadium-shaped node labeled with the
suffix `(external)` (ODS-400-R-02). An external boundary connects to the
modeled slice only with a **dotted, labeled** edge into an existing model
port, and that edge is labeled as not being a modeled connection.

**MDS-R-04 — Realized connection edge.** A connection instance is a
**solid arrow** pointing from the connection's `source_port` equipment to
its `target_port` equipment (ODS-400-R-04), labeled with the connection
local ID. The mapping table records the full connection ID and both port
endpoints (ODS-400-R-06).

**MDS-R-05 — Interface-only edge (unrealized path).** An interface with
no realizing connection instance (e.g., a factory-option path) is a
**dotted arrow** labeled with the interface local ID and the suffix
`(interface only)` (ODS-400-R-03).

**MDS-R-06 — Annotation nodes and relation edges.** Protection and
measurement roles are rendered as annotation nodes (dashed border via a
`classDef`) linked to their target elements with dotted edges labeled by
the model relation name (`protects`, `measures`). v0.1 limitation: where
the relation targets a **connection** (an edge), the relation is recorded
in the mapping table instead of drawn, because the flowchart format
cannot attach an edge to an edge. The mapping table entry is mandatory in
that case.

**MDS-R-07 — Structural unknown marker.** An element whose **presence**
in the configuration is not established by any captured source is
rendered with the textual marker `presence unknown` inside the node label
(ODS-400-R-05). Attribute-level unknowns — including quantity, ratings,
and limits — are **not** rendered in the energy-chain view (structure-only
value rule, Section 2.1); they remain explicit in the model instances and
their published unknown counts. Unknowns are never carried by color,
dimming, or omission.

**MDS-R-08 — Identifier mapping table.** Every MDS diagram is accompanied
(in the same artifact) by a mapping table resolving every node key to its
full model element ID and source file, and every edge label to its full
connection/interface ID with both port endpoints (implements
ODS-400-R-06).

**MDS-R-09 — Monochrome default; color never alone.** MDS v0.1 requires
no color styling. Any color added by a renderer is supplementary and
never the sole carrier of meaning (ODS-200-R-07); realized vs. unrealized
and equipment vs. annotation distinctions are carried by line style and
node shape, never by color alone.

## 4. Machine-Readable Source Convention

**MDS-R-10 — Source location and form.** The canonical source of an MDS
diagram is a fenced `mermaid` code block inside a **governed diagram-view
artifact** (a Markdown file with full governed metadata) located in a
`diagrams/` subdirectory of the model package it renders (first instance:
`reference/hanse460/diagrams/`). One canonical source per diagram; the
same diagram is never maintained in two places (single-source rule,
ODS-400-R-08).

**MDS-R-11 — Diagram-view artifact minimum content.** A diagram-view
artifact contains, at minimum: (1) the declared view class (ODS-400-R-07);
(2) the Mermaid source block; (3) the identifier mapping table
(MDS-R-08); (4) a derivation note naming the model package and version
the view was derived from and how consistency with the model was checked;
(5) the advisory/safety boundary note of its model package. Rendered
images (SVG/PNG), when produced, are derived from this source and are
regenerable (ODS-400-R-09).

**MDS-R-12 — Notation traceability.** Every notation element used in a
diagram must be traceable to an MDS rule. A diagram-view artifact using a
notation element not defined in this document is non-conformant and is
reported as an MDS revision need, not silently accepted.

## 5. Applied Instance (first conformance exercise)

The first applied MDS instance is the golden-path energy-chain view of
the Hanse 460 electrical slice
(`OMSP-PLANNING-GOLDEN-PATH-0001` §7.1 chain: shore power → charger →
battery bank → DC distribution → consumers, with the inverter branch):

- [`reference/hanse460/diagrams/ENERGY-CHAIN-VIEW.md`](../../reference/hanse460/diagrams/ENERGY-CHAIN-VIEW.md)
  (`OMSP-REFERENCE-HANSE460-DIAGRAM-0001`), derived from the WP-0082
  model package
  ([`reference/hanse460/README.md`](../../reference/hanse460/README.md),
  `OMSP-REFERENCE-HANSE460-ELECTRICAL-0001`).

Its notation→rule mapping table demonstrates MDS-R-12. No interface-view
instance exists yet; the first is expected with the Sprint-9 scenario
work, and its findings feed back into Section 2.2.

## 6. Reserved Subtopics (not drafted in v0.1)

The following MDS subtopics are **Reserved**. They carry no normative
content in v0.1 and are drafted in later Work Packages (see
`OMSP-MODS-SPEC-0001` §4):

### 6.1 Vector (SVG) component library and rendered symbol set — Reserved

### 6.2 Color and icon treatment (pending the ODS-200 Reserved palette) — Reserved

### 6.3 Additional view classes (compartment, plumbing, rigging, composite) — Reserved

### 6.4 PlantUML or other source-format profiles — Reserved

### 6.5 Automated source generation and model-consistency checking — Reserved

## 7. Conformance Notes

- MDS conformance is **advisory (non-gating) in v0.1**: the renderer
  conformance checklist
  ([`MODS_RENDERER_CONFORMANCE_CHECKLIST.md`](MODS_RENDERER_CONFORMANCE_CHECKLIST.md),
  `OMSP-MODS-CONFORMANCE-0001`) contains items for ODS-100 and ODS-300
  only; **only ODS-100/300 gate rendering conformance**. This draft adds
  no checklist items and binds no CI gate.
- MDS diagrams are advisory knowledge views of reference models: they
  carry no certification, compliance, seaworthiness, or
  operational-authority meaning, and they are never operational
  instructions. The safety and authority boundary of
  `OMSP-MODS-SPEC-0001` §7 and of the rendered model package applies
  unchanged.
