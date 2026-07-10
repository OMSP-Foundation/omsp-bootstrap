---
Artifact-ID: OMSP-REFERENCE-EQUIPMENT-0001
Title: Equipment and Interface Model
Version: 1.0.0
Status: Review
Owner: OMSP Engineering Council
Approvers:
  - Accountable Maintainer
Created: 2026-07-10
Last-Updated: 2026-07-10
Sprint: Sprint-4
Work-Package: WP-0041
Traceability:
  - ISSUE-75
  - OMSP-PLAN-SPRINT-0004
  - OMSP-REFERENCE-VESSEL-0001
  - OMSP-REFERENCE-CONFIG-0001
  - OMSP-ONTOLOGY-CORE-0001
---

# Equipment and Interface Model

## 1. Objective

This artifact defines a governed, vendor-neutral model for vessel equipment, subsystems and interfaces. It extends the Vessel Reference Model without asserting that any example item is installed on a particular vessel.

The model supports design-family references, option packages, verified vessel configurations, maintenance traceability, operational scenarios and digital-twin observations while preserving provenance and human authority.

## 2. Modeling Layers

Equipment information is separated into four layers:

1. **Equipment class** — reusable functional class such as propulsion engine, battery, bilge pump or multifunction display.
2. **Equipment design** — manufacturer/model family or design definition, when sourced.
3. **Configuration item** — an equipment role selected for a versioned vessel configuration.
4. **Installed equipment instance** — a uniquely identified physical item with vessel-specific evidence.

A class or configuration item must never be represented as an installed instance. Manufacturer/model, serial number, firmware, calibration and installation location remain unknown until supported by evidence.

## 3. Stable Identity Rules

| Entity | Stable identity pattern |
| --- | --- |
| EquipmentClass | `equipment-class:<domain>:<slug>` |
| EquipmentDesign | `equipment-design:<namespace>:<model-slug>` |
| ConfigurationItem | `equipment:<configuration-id>:<local-id>` |
| InstalledEquipment | `equipment:<vessel-instance-id>:<local-id>` |
| Port | `port:<equipment-id>:<local-id>` |
| Interface | `interface:<source-port-id>:<target-port-id>:<type>` |
| MaintenanceTask | `maintenance-task:<equipment-class-or-design-id>:<slug>` |
| DocumentReference | `document:<authority>:<identifier>:<version>` |

Identifiers remain stable across display-name, repository-path and ownership changes.

## 4. Equipment Taxonomy

Equipment classes may be grouped by primary function:

- structural and hull fittings;
- rigging, sail handling and deck machinery;
- propulsion and maneuvering;
- steering and control;
- electrical generation, conversion, storage and distribution;
- navigation, communications and positioning;
- fuel, lubrication, cooling and exhaust;
- freshwater, wastewater, bilge and drainage;
- heating, ventilation and environmental control;
- domestic and accommodation systems;
- fire detection and suppression;
- lifesaving, emergency and security;
- anchoring, mooring and towing;
- monitoring, instrumentation, gateways and networks;
- tools, spares, documentation and maintenance support.

An equipment class records its intended function, ontology mapping, applicable systems, expected interfaces, capabilities, constraints, safety relevance and evidence requirements.

## 5. Equipment Record Contract

Every equipment record should include:

- stable identifier and entity layer;
- equipment class and optional design identifier;
- parent system, subsystem and configuration applicability;
- quantity and role;
- lifecycle and verification state;
- source authority, confidence and provenance;
- manufacturer, model, serial number and firmware only when evidenced;
- installation location and containment relationship;
- replaceable-unit and maintenance-boundary status;
- ports and typed interfaces;
- capabilities, constraints and operating assumptions;
- related documents, procedures, maintenance tasks and evidence;
- safety relevance, failure implications and unresolved unknowns.

Missing fields are represented explicitly as `unknown`, not omitted in a way that implies absence.

## 6. Interface Families

Interfaces are represented through typed ports and connections.

| Family | Examples |
| --- | --- |
| physical | mounting, containment, access, clearance |
| mechanical | shaft, linkage, torque, force transfer |
| electrical-power | DC supply, AC supply, protective earth, return |
| fluid | fuel, freshwater, seawater, coolant, wastewater, hydraulic fluid, air |
| data-signal | NMEA, CAN, Ethernet, serial, discrete signal, analog signal |
| human | control, display, alarm acknowledgement, inspection access |
| procedural | isolation, startup sequence, inspection dependency, permit or checklist |
| functional | capability dependency or service dependency |
| safety-protection | fuse, breaker, interlock, relief, alarm, shutdown dependency |

Every interface records source and target ports, direction, media or protocol where known, nominal limits, isolation or protection, failure implications, provenance and confidence.

## 7. Capability Model

Capabilities describe intended or evidenced functions. Each capability records:

- capability identifier and description;
- supporting equipment and interfaces;
- applicability to design, configuration or vessel instance;
- authority class: reference, sourced, verified, observed or derived;
- preconditions and dependencies;
- nominal constraints and known limitations;
- safety relevance and validation evidence.

Capabilities are descriptive and do not authorize operation.

## 8. Constraint Model

Constraints may include:

- voltage, current, power, pressure, flow, temperature or load limits;
- environmental or installation requirements;
- compatibility and protocol requirements;
- access, service-clearance and isolation requirements;
- operating sequence or human-action dependencies;
- maintenance interval, inspection or calibration requirements;
- prohibited states and unresolved assumptions.

A limit without authoritative evidence remains an assumption or unknown and cannot be treated as a verified operating boundary.

## 9. Maintenance and Document References

Equipment may reference:

- manufacturer manuals and data sheets;
- approved drawings, wiring diagrams and piping diagrams;
- installation, operation and maintenance procedures;
- inspection, test and calibration records;
- maintenance tasks, intervals and evidence;
- replacement, modification and configuration-change records;
- safety notices, service bulletins and defect records.

Document references must preserve authority, title, version, date, applicability and provenance. A document link alone does not prove installation or compliance.

## 10. Configuration and Replacement Rules

A configuration item identifies an intended role. An installed item identifies a physical asset. Replacement creates a new installed-equipment identity when serialised identity or traceability changes.

A configuration update records:

- predecessor and successor equipment identities;
- effective date and vessel/configuration applicability;
- changed interfaces and dependent capabilities;
- source evidence and reviewer;
- maintenance and verification implications;
- unresolved compatibility or safety risks.

Automation may detect missing or inconsistent data but cannot approve a replacement, configuration promotion or safety acceptance.

## 11. Hanse 460 Use

For `configuration:vessel-design:hanse:460:reference-0.1.0`, WP-0041 defines only reusable equipment roles and interface structures. It does not populate unknown manufacturer, model, option package, network topology or vessel-instance facts.

Example records are illustrative and remain `reference` or `proposed`. They must not be interpreted as proof that a Hanse 460 includes the represented equipment.

## 12. Validation Rules

A conforming model should ensure:

- all equipment, port and interface identifiers are unique;
- equipment layers are not conflated;
- parent systems and configuration references exist;
- interface endpoints reference valid ports;
- physical, electrical, fluid, data, human and procedural interfaces remain distinguishable;
- units and directionality are explicit where values exist;
- authority, provenance, confidence and applicability are present;
- unknown manufacturer/model/serial values remain explicit;
- safety-relevant assumptions and failure implications are visible;
- lifecycle or verification promotion requires accountable human evidence.

## 13. Safety and Authority Boundary

This model does not certify installation, compatibility, seaworthiness, regulatory compliance or safe operation. It does not replace manufacturer documentation, vessel inspection or approved procedures. It cannot command equipment or grant AI/automation authority to approve configuration, maintenance, operation, risk or release decisions.
