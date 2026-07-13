---
Artifact-ID: OMSP-ONTOLOGY-MARITIME-0001
Title: Maritime Core Ontology
Version: 0.1.0
Status: Draft
Owner: toss-cengiz
Baseline: Sprint-7
Classification: Public
Related-Issue: WP-0077 / #198
Depends-On:
  - OMSP-ONTOLOGY-CORE-0001
Traceability:
  - ISSUE-198
  - OMSP-PLANNING-GOLDEN-PATH-0001
  - OMSP-PLANNING-REBASELINE-0001
  - OMSP-REFERENCE-EQUIPMENT-0001
  - OMSP-REFERENCE-SCENARIO-0001
---

# Maritime Core Ontology

## 1. Purpose and Relationship to the Core Ontology

This artifact defines the first maritime domain extension of the OMSP formal
ontology (`OMSP-ONTOLOGY-CORE-0001`). It introduces stable concept and
relation identifiers for describing a vessel as a system of systems: its
functional systems, equipment roles, ports, interfaces, connections,
protection, measurement points, operational scenarios and provenance records.

The extension is strictly **additive**:

- it **extends** the core ontology and **does not modify** any existing core
  concept, relation, domain, range or constraint;
- every maritime concept declares a parent in the core taxonomy
  (`OMSP-ONTOLOGY-CORE-0001` §4), so core reasoning and validation rules
  apply unchanged;
- core relations (`belongs-to`, `depends-on`, `uses`, `implements`,
  `traces-to`, …) are reused as defined in `OMSP-ONTOLOGY-CORE-0001` §5 and
  are **not** redefined here;
- identity rules follow `OMSP-ONTOLOGY-CORE-0001` §3 (`OMSP-CONCEPT-<NAME>`,
  `OMSP-RELATION-<NAME>`; identities are never reused for a different
  meaning).

Machine-readable entries live in `ontology/omsp-ontology.json`. Maritime
entries carry the marker field `"layer": "maritime"`; entries without a
`layer` field belong to the core layer and remain normatively defined by
`OMSP-ONTOLOGY-CORE-0001`.

**Domain-neutrality rule (binding for this layer):** every definition in this
artifact must apply, word for word, to any vessel system slice — for example
a freshwater or bilge system as well as an energy system. No concept or
relation in this layer may encode an equipment type, a vessel model, a
physical quantity kind or a transported-medium kind. Such specifics are
instances and attributes of downstream models, not ontology identities.

## 2. Concept Taxonomy

| Concept ID | Preferred label | Definition | Parent concept |
| --- | --- | --- | --- |
| `OMSP-CONCEPT-VESSEL` | Vessel | A waterborne craft represented as a governed system of systems, with stable identity maintained across type, design, configuration and instance layers. | System |
| `OMSP-CONCEPT-VESSEL-SYSTEM` | Vessel System | A functionally bounded grouping of equipment roles, ports and connections aboard a vessel, serving one coherent purpose within the vessel decomposition. | System |
| `OMSP-CONCEPT-EQUIPMENT-ROLE` | Equipment Role | An identified functional position within a vessel system that equipment is intended to fill in a versioned configuration, independent of any physical item. | Entity |
| `OMSP-CONCEPT-PORT` | Port | A declared point on an equipment role or vessel system through which a medium, signal or service enters or leaves. | Entity |
| `OMSP-CONCEPT-INTERFACE` | Interface | A typed contract describing how ports may interact, including interface family, media or signal kind, direction and declared limits where evidenced. | Entity |
| `OMSP-CONCEPT-CONNECTION` | Connection | A realized link between two ports in a specific configuration, carrying the media or service described by an interface. | Entity |
| `OMSP-CONCEPT-PROTECTION` | Protection | The ability to limit, interrupt or isolate conditions that could harm people, equipment, connections or the media they carry. | Capability |
| `OMSP-CONCEPT-MEASUREMENT-POINT` | Measurement Point | An identified physical or logical point at which a quantity or state of a system element is observed and recorded as evidence. | Entity |
| `OMSP-CONCEPT-OPERATIONAL-SCENARIO` | Operational Scenario | A structured, bounded representation of actors, context, preconditions, triggers, steps, decisions, hazards, outcomes and human-authority boundaries for a maritime activity. | Model |
| `OMSP-CONCEPT-SOURCE-RECORD` | Source Record | A traceable provenance record identifying the origin, authority class, retrieval context and applicability of asserted facts. | Evidence |

### 2.1 Definition sources

Each definition is grounded in an existing governed OMSP artifact; no
external standard is claimed:

| Concept ID | Grounding artifact and section |
| --- | --- |
| `OMSP-CONCEPT-VESSEL` | `OMSP-REFERENCE-VESSEL-0001` §1–§3 (vessel as governed system-of-systems; type/design/configuration/instance layers) |
| `OMSP-CONCEPT-VESSEL-SYSTEM` | `OMSP-REFERENCE-VESSEL-0001` §3–§4 (system as major functional grouping within the decomposition) |
| `OMSP-CONCEPT-EQUIPMENT-ROLE` | `OMSP-REFERENCE-EQUIPMENT-0001` §2 (configuration item: "an equipment role selected for a versioned vessel configuration"), §3, §10 |
| `OMSP-CONCEPT-PORT` | `OMSP-REFERENCE-EQUIPMENT-0001` §3, §6 (typed ports as interface endpoints) |
| `OMSP-CONCEPT-INTERFACE` | `OMSP-REFERENCE-EQUIPMENT-0001` §6 (interface families; recorded media, direction, limits) |
| `OMSP-CONCEPT-CONNECTION` | `OMSP-REFERENCE-EQUIPMENT-0001` §6 ("interfaces are represented through typed ports and connections") |
| `OMSP-CONCEPT-PROTECTION` | `OMSP-REFERENCE-EQUIPMENT-0001` §6 (safety-protection interface family), §7 (capability model); core Capability definition |
| `OMSP-CONCEPT-MEASUREMENT-POINT` | `OMSP-PLANNING-GOLDEN-PATH-0001` §5.1–§5.2 (measurement roles "modeled as points, not as a live data pipeline") |
| `OMSP-CONCEPT-OPERATIONAL-SCENARIO` | `OMSP-REFERENCE-SCENARIO-0001` §1, §4 (scenario record contract) |
| `OMSP-CONCEPT-SOURCE-RECORD` | `OMSP-REFERENCE-SOURCE-0001` §1–§2 (source register record contract); `OMSP-PLANNING-GOLDEN-PATH-0001` §4 |

### 2.2 Classification decisions

Two parent assignments required an explicit decision; the rationale is
recorded here per `ontology/CHANGE_POLICY.md`:

1. **Equipment Role is an Entity, not a Capability.** An equipment role is an
   identifiable configuration element (`OMSP-REFERENCE-EQUIPMENT-0001` §2,
   layer 3) that carries ports, connections, provenance and lifecycle state.
   It is a *bearer* of capabilities, not an ability itself;
   `OMSP-REFERENCE-EQUIPMENT-0001` §7 deliberately keeps capability records
   separate from equipment records. Classifying the role under Capability
   would conflate the function slot with the function it provides.
2. **Protection is a Capability, not an Entity.** Protection is a provided
   ability — to limit, interrupt or isolate harmful conditions — matching the
   core Capability definition ("an ability required or provided by an actor,
   system, process or organization"). The protective *devices* that realize
   this ability are Equipment Role instances in downstream models, never
   children of this concept. This keeps the concept domain-neutral: the same
   identity covers overcurrent interruption in an energy system and
   overpressure relief in a fluid system without redefinition.

## 3. Relation Taxonomy

| Relation ID | Label | Domain | Range | Meaning |
| --- | --- | --- | --- | --- |
| `OMSP-RELATION-CONNECTS-TO` | connects-to | Port | Port | The source port is joined to the target port through a connection. |
| `OMSP-RELATION-SUPPLIES` | supplies | Equipment Role | Equipment Role | The source provides energy, fluid, data or another transported medium or service that the target consumes, through one or more connections. |
| `OMSP-RELATION-PROTECTS` | protects | Equipment Role | Entity | The source limits, interrupts or isolates conditions that could harm the target or the media it carries. |
| `OMSP-RELATION-MEASURES` | measures | Measurement Point | Entity | The source observes a quantity or state of the target and makes the observation available as evidence. |
| `OMSP-RELATION-SOURCED-FROM` | sourced-from | Entity | Source Record | Asserted facts about the source derive from, and remain traceable to, the target provenance record. |

### 3.1 Relation semantics

- Relations are directed from source to target
  (`OMSP-ONTOLOGY-CORE-0001` §6).
- `supplies` is **medium-neutral by construction**: the kind of medium or
  service (and any flow properties) is an attribute of the connection and
  interface involved, never of the relation. The same relation identity must
  apply unchanged to any transported medium or service.
- `connects-to` records topology only. Direction of flow, media and limits
  belong to the Connection and its Interface contract, not to the relation.
- `protects` has range Entity so that a protective role may guard an
  equipment role, a connection, a port or a whole vessel system.
- `measures` has range Entity so that a measurement point may observe an
  equipment role, a connection or a vessel system state.
- `sourced-from` has domain Entity: any element or asserted fact carrier may
  cite a provenance record. It complements — and does not replace — the
  authority-class rules of `OMSP-PLANNING-GOLDEN-PATH-0001` §4.3.
- Membership and dependency reuse core relations: an equipment role
  `belongs-to` a vessel system, a vessel system `belongs-to` a vessel, a port
  `belongs-to` an equipment role, a measurement point `belongs-to` an
  equipment role or connection; consumers `depends-on` their distribution
  role; an equipment role `implements` Protection when it realizes that
  capability; a connection `implements` its interface contract.

## 4. Core-to-Maritime Concept Mapping

Every maritime identity resolves to a core parent in the registry
(`ontology/omsp-ontology.json`); this table is the Evidence Produced mapping
required by WP-0077.

| Maritime concept ID | Core parent ID | Mapping rationale |
| --- | --- | --- |
| `OMSP-CONCEPT-VESSEL` | `OMSP-CONCEPT-SYSTEM` | A vessel is a socio-technical system of systems. |
| `OMSP-CONCEPT-VESSEL-SYSTEM` | `OMSP-CONCEPT-SYSTEM` | A functional grouping is itself a system within the vessel. |
| `OMSP-CONCEPT-EQUIPMENT-ROLE` | `OMSP-CONCEPT-ENTITY` | An identifiable configuration element; see §2.2 decision 1. |
| `OMSP-CONCEPT-PORT` | `OMSP-CONCEPT-ENTITY` | An identifiable declared interaction point. |
| `OMSP-CONCEPT-INTERFACE` | `OMSP-CONCEPT-ENTITY` | An identifiable typed interaction contract. |
| `OMSP-CONCEPT-CONNECTION` | `OMSP-CONCEPT-ENTITY` | An identifiable realized link between ports. |
| `OMSP-CONCEPT-PROTECTION` | `OMSP-CONCEPT-CAPABILITY` | A provided ability; see §2.2 decision 2. |
| `OMSP-CONCEPT-MEASUREMENT-POINT` | `OMSP-CONCEPT-ENTITY` | An identifiable observation point. |
| `OMSP-CONCEPT-OPERATIONAL-SCENARIO` | `OMSP-CONCEPT-MODEL` | A structured representation of entities, behavior and constraints. |
| `OMSP-CONCEPT-SOURCE-RECORD` | `OMSP-CONCEPT-EVIDENCE` | A traceable record supporting claims and validation. |

## 5. Golden-Path Expressibility Demonstration (non-normative)

> **Non-normative demonstration.** This appendix shows that every role row of
> the golden-path model boundary (`OMSP-PLANNING-GOLDEN-PATH-0001` §5.1) is
> expressible with the concepts and relations above. The vessel- and
> energy-specific terms below (including role identifiers such as
> `service-battery-bank`) are **instance names from the golden-path
> definition**, not ontology identities, and impose no meaning on this
> ontology. Nothing here asserts installed equipment, values or procedures.

Common structure for all rows: each role is an instance of
`OMSP-CONCEPT-EQUIPMENT-ROLE` that `belongs-to` an instance of
`OMSP-CONCEPT-VESSEL-SYSTEM` (the golden-path system identifier), which
`belongs-to` an instance of `OMSP-CONCEPT-VESSEL`; each role exposes
`OMSP-CONCEPT-PORT` instances joined by `OMSP-CONCEPT-CONNECTION` instances
(`connects-to`), each connection `implements` an `OMSP-CONCEPT-INTERFACE`
contract; every asserted fact is `sourced-from` an
`OMSP-CONCEPT-SOURCE-RECORD` or remains explicitly unknown.

| §5.1 role | Expression (concepts + relations) |
| --- | --- |
| `shore-power-inlet` | Equipment Role; `supplies` → `battery-charger`; inlet Ports `connects-to` charger Ports through Connections. |
| `service-battery-bank` | Equipment Role; target of `supplies` from charging roles; `supplies` → `dc-main-distribution` and `inverter`. |
| `battery-charger` | Equipment Role; `depends-on` → `shore-power-inlet`; `supplies` → `service-battery-bank`. |
| `alternator-charging` | Equipment Role (charging-source role only, per §5.1); `supplies` → `service-battery-bank`. |
| `inverter` | Equipment Role; target of `supplies` from `service-battery-bank`; `supplies` → its output-side consumer roles. |
| `dc-main-distribution` | Equipment Role; target of `supplies` from `service-battery-bank`; `supplies` → each `dc-consumer-*`. |
| `dc-consumer-*` | Equipment Role per consumer; target of `supplies` from `dc-main-distribution`; `depends-on` → `dc-main-distribution`. |
| `protection-*` | Equipment Role per protective device; `implements` → Protection; `protects` → the Connection or Equipment Role it guards. |
| `measurement-*` | Equipment Role per measurement provision; hosts Measurement Point instances (`belongs-to` the role); each Measurement Point `measures` → the Equipment Role or Connection it observes. |

The primary scenario (`OMSP-PLANNING-GOLDEN-PATH-0001` §8) is an instance of
`OMSP-CONCEPT-OPERATIONAL-SCENARIO` that `uses` the equipment roles above and
`traces-to` its Source Records, per the record contract of
`OMSP-REFERENCE-SCENARIO-0001` §4 and §10.

**Coverage result:** all nine §5.1 role rows are expressible; no role
required a new concept or relation beyond the closed set of this artifact.

**Neutrality check:** the same combinations express a freshwater or bilge
slice unchanged — a pump role `supplies` a tank or consumer role, a relief or
cutoff role `implements` Protection and `protects` a connection, a level or
flow point `measures` a tank role — with no wording change to any definition
in §2–§3.

## 6. Change Evidence Record

Recorded per `ontology/CHANGE_POLICY.md` (OMSP-ONTOLOGY-CHANGE-POLICY-0001):

- **Issue:** WP-0077 / #198 (Sprint-7, epic #171; specification
  `OMSP-PLANNING-REBASELINE-0001` §4).
- **Affected IDs (all new):** concepts `OMSP-CONCEPT-VESSEL`,
  `OMSP-CONCEPT-VESSEL-SYSTEM`, `OMSP-CONCEPT-EQUIPMENT-ROLE`,
  `OMSP-CONCEPT-PORT`, `OMSP-CONCEPT-INTERFACE`, `OMSP-CONCEPT-CONNECTION`,
  `OMSP-CONCEPT-PROTECTION`, `OMSP-CONCEPT-MEASUREMENT-POINT`,
  `OMSP-CONCEPT-OPERATIONAL-SCENARIO`, `OMSP-CONCEPT-SOURCE-RECORD`;
  relations `OMSP-RELATION-CONNECTS-TO`, `OMSP-RELATION-SUPPLIES`,
  `OMSP-RELATION-PROTECTS`, `OMSP-RELATION-MEASURES`,
  `OMSP-RELATION-SOURCED-FROM`.
- **Compatibility class:** Additive. No core concept, relation, domain,
  range or constraint changed; no identity reused.
- **Impacted artifacts:** `ontology/omsp-ontology.json` (15 additive entries
  with `layer: maritime`), `ontology/OMSP_ONTOLOGY.md` (§10 extension
  pointer; version 1.0.0 → 1.1.0), `ontology/README.md` (artifact listing),
  this artifact (new).
- **Migration guidance:** none required (purely additive; existing consumers
  are unaffected).
- **Validation results:** `python3 tooling/validate_ontology.py` →
  `Ontology validation passed: 25 concepts, 19 relations.` (exit 0);
  governed-metadata validation and quality gate green (see Work Package PR
  evidence).
- **Accountable review:** pending — this artifact enters at `Draft`;
  promotion is a human decision (`OMSP-ONTOLOGY-CHANGE-POLICY-0001`,
  Authority Boundary).

## 7. Boundaries

This artifact does not define:

- a data schema, YAML model format, database structure or reasoning engine
  (schemas remain in `schemas/`; models in downstream Work Packages);
- equipment types or equipment classes — these are Equipment Role and
  equipment-class *instances* in downstream models
  (`OMSP-REFERENCE-EQUIPMENT-0001` §4);
- physical-quantity kinds, media kinds, limits or any vessel-specific fact —
  such values require provenance per `OMSP-PLANNING-GOLDEN-PATH-0001` §4.3;
- protocols, telemetry pipelines or live data semantics;
- alignment with any external standard (no IMO, ISO or class-society claim is
  made in v0.1);
- any certified procedure or operational instruction. Content built on these
  identities remains advisory and subject to the safety boundaries of
  `reference/DIGITAL_TWIN_GOVERNANCE_AND_SAFETY_BOUNDARIES.md`.

Downstream domain extensions must build on these identifiers through separate
governed artifacts, per `OMSP-ONTOLOGY-CORE-0001` §10.
