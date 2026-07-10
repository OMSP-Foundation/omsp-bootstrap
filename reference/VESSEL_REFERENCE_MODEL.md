---
Artifact-ID: OMSP-REFERENCE-VESSEL-0001
Title: Vessel Reference Model
Version: 1.0.0
Status: Review
Owner: OMSP Engineering Council
Approvers:
  - Accountable Maintainer
Created: 2026-07-10
Last-Updated: 2026-07-10
Sprint: Sprint-4
Work-Package: WP-0039
Traceability:
  - ISSUE-73
  - OMSP-PLAN-SPRINT-0004
  - OMSP-ONTOLOGY-CORE-0001
  - OMSP-KNOWLEDGE-GRAPH-0001
  - OMSP-KNOWLEDGE-REGISTRY-0001
---

# Vessel Reference Model

## 1. Objective

This artifact defines a vendor-neutral and extensible reference model for representing a maritime vessel as a governed system-of-systems. It provides stable identity, decomposition, configuration, interface and traceability rules for downstream vessel-specific configurations, equipment models, scenarios and digital-twin observations.

The model is descriptive. It does not represent an as-built vessel unless supported by verified evidence, and it does not authorize operation, control, maintenance or safety decisions.

## 2. Modeling Boundary

The reference model distinguishes four layers:

1. **Vessel type** — reusable class-level description such as sailing yacht, motor vessel or workboat.
2. **Vessel design** — design or model family description independent of an individual hull.
3. **Vessel configuration** — versioned arrangement of systems, equipment and interfaces.
4. **Vessel instance** — uniquely identified physical vessel with evidence-backed configuration claims.

A reference configuration must never be presented as a verified vessel instance. Unknown, assumed, sourced, verified, observed and derived information must remain distinguishable.

## 3. Core Entity Model

| Entity | Purpose | Stable identity rule |
| --- | --- | --- |
| VesselType | Classifies broad vessel purpose and operating form | `vessel-type:<slug>` |
| VesselDesign | Represents a reusable design or model family | `vessel-design:<namespace>:<slug>` |
| VesselInstance | Represents one physical vessel | `vessel:<authority>:<identifier>` |
| Configuration | Versioned system and equipment arrangement | `configuration:<vessel-or-design-id>:<version>` |
| System | Major functional or structural grouping | `system:<parent-id>:<slug>` |
| Subsystem | Decomposed child of a system | `subsystem:<parent-id>:<slug>` |
| Equipment | Replaceable or maintainable physical/virtual item | `equipment:<parent-id>:<local-id>` |
| Interface | Typed connection or dependency between entities | `interface:<source-id>:<target-id>:<type>` |
| Compartment | Spatial or containment boundary | `compartment:<parent-id>:<slug>` |
| Capability | Governed statement of supported function | `capability:<parent-id>:<slug>` |
| Constraint | Limit, dependency or operating boundary | `constraint:<parent-id>:<slug>` |

Identifiers must be stable across file moves and display-name changes. Manufacturer serial numbers, hull identifiers or registration numbers may be recorded as external identifiers but must include issuing authority and provenance.

## 4. Reference System Decomposition

The following top-level decomposition is recommended and may be extended:

- hull, structure and watertight integrity;
- deck, rig and sail systems;
- propulsion and maneuvering;
- steering and control;
- electrical generation, storage and distribution;
- navigation and communications;
- machinery, fuel, lubrication and exhaust;
- freshwater, wastewater and bilge;
- heating, ventilation and environmental control;
- accommodation and domestic systems;
- fire detection and suppression;
- lifesaving, emergency and security systems;
- anchoring, mooring and towing;
- monitoring, instrumentation and vessel networks;
- documentation, procedures and maintenance support.

The decomposition is functional and structural, not regulatory certification. A downstream model may add or omit systems only with rationale and traceability.

## 5. Entity Record Contract

Every modeled entity should record:

- stable identifier and entity type;
- display name and optional aliases;
- parent or containment relationship;
- lifecycle state;
- configuration applicability;
- source and provenance references;
- authority classification: reference, sourced, verified, observed or derived;
- confidence and known limitations;
- safety relevance and critical assumptions;
- related artifacts, requirements, procedures and evidence;
- interfaces, dependencies, capabilities and constraints.

Missing information must be represented explicitly rather than inferred as absent or false.

## 6. Configuration Rules

A configuration is an immutable versioned snapshot. A change creates a new configuration version and records:

- predecessor configuration;
- additions, removals and replacements;
- changed interfaces or dependencies;
- source evidence and effective date;
- approval or review evidence when promoted to governed status;
- unresolved conflicts and unknowns.

Reference, proposed, verified-as-designed and verified-as-built configurations are separate authority classes. Promotion between them requires evidence and accountable human review.

## 7. Interface Model

Interfaces must be typed. Recommended interface families are:

- physical attachment or containment;
- electrical power supply and return;
- fluid transfer;
- mechanical drive or force transmission;
- data, network or signal exchange;
- human interaction;
- spatial access;
- functional dependency;
- safety or protection dependency.

Each interface records directionality, endpoints, media or protocol where known, nominal constraints, failure implications, provenance and confidence. An interface definition is not proof that a physical connection exists on a particular vessel.

## 8. Capability and Constraint Model

Capabilities describe what an entity is intended or evidenced to support. Constraints describe limits or conditions. Both must distinguish:

- design intent;
- sourced manufacturer claim;
- verified configuration evidence;
- observed behavior;
- derived assessment.

Safety-critical capabilities and constraints require explicit source evidence and human review. AI-generated or inferred statements remain proposed and cannot become verified facts automatically.

## 9. Traceability

Vessel entities should be traceable to governed ontology concepts, source documents, requirements, procedures, maintenance records, validation evidence and configuration changes. Relations should use controlled semantics such as `contains`, `depends-on`, `interfaces-with`, `supports`, `constrained-by`, `documented-by`, `validated-by` and `derived-from`.

A model record must preserve whether a relation is asserted, sourced, inferred or observed. Inferred relations cannot overwrite authoritative asserted relations.

## 10. Safety and Authority Boundary

This model does not:

- certify seaworthiness, regulatory compliance or class status;
- replace manufacturer documentation or approved operating procedures;
- authorize operation, navigation, maintenance or emergency action;
- verify a vessel-specific fact without evidence;
- connect to or control vessel systems;
- grant AI or automation approval authority.

Safety-relevant assumptions, conflicts and unknowns must be visible to reviewers and downstream consumers.

## 11. Validation Rules

A conforming vessel model should satisfy the following checks:

- all entities have unique stable identifiers;
- entity types and parent relationships are valid;
- no containment cycles exist;
- configuration versions are immutable and linked to predecessors;
- external identifiers include authority and provenance;
- every interface has valid typed endpoints;
- source authority and confidence are explicit;
- safety-relevant assumptions and unknowns are recorded;
- reference and verified information are not conflated;
- lifecycle promotion requires accountable human evidence.

## 12. Downstream Use

WP-0040 may instantiate this model for a Hanse 460 reference configuration. WP-0041 may extend equipment and interface detail. WP-0042 and WP-0043 may reference the stable identifiers for scenarios, states and observations. Any downstream extension must preserve identity, provenance, configuration versioning and authority distinctions.

## 13. Known Limitations

This artifact does not select a production database, exchange standard, digital-twin runtime, sensor protocol or certification framework. The accompanying JSON is illustrative and is not an approved vessel configuration.