---
Artifact-ID: OMSP-REFERENCE-CONFIG-0001
Title: Hanse 460 Reference Configuration
Version: 0.1.0
Status: Review
Owner: OMSP Engineering Council
Approvers:
  - Accountable Maintainer
Created: 2026-07-10
Last-Updated: 2026-07-10
Sprint: Sprint-4
Work-Package: WP-0040
Traceability:
  - ISSUE-74
  - OMSP-PLAN-SPRINT-0004
  - OMSP-REFERENCE-VESSEL-0001
---

# Hanse 460 Reference Configuration

## 1. Objective

This artifact instantiates the vendor-neutral Vessel Reference Model for the Hanse 460 design family. It creates a governed reference configuration that can support equipment modeling, operational scenarios and digital-twin demonstrations without claiming to represent a specific physical vessel.

The configuration is intentionally conservative. Values are included only when their source and authority class are recorded. Missing or inaccessible manufacturer evidence is represented as unknown rather than inferred.

## 2. Configuration Identity

| Field | Value |
| --- | --- |
| Configuration ID | `configuration:vessel-design:hanse:460:reference-0.1.0` |
| Vessel design ID | `vessel-design:hanse:460` |
| Vessel type ID | `vessel-type:sailing-yacht` |
| Configuration class | Reference |
| Applicability | Hanse 460 design family; no individual hull applicability |
| Verification state | Not verified as-designed or as-built |
| Predecessor | None |

This configuration must not be used as evidence for a particular hull, installed equipment set, regulatory status or operational readiness.

## 3. Source and Authority Classification

The following authority classes are used:

- **reference** — OMSP modeling structure or placeholder;
- **sourced-secondary** — value transcribed from a named secondary source;
- **sourced-manufacturer** — value transcribed from accessible manufacturer-controlled documentation;
- **verified-design** — value verified against controlled design evidence;
- **verified-as-built** — value verified on a physical vessel;
- **unknown** — value not established by current evidence.

No field in version `0.1.0` is classified as `verified-design` or `verified-as-built`.

## 4. Design-Family Characteristics

| Property | Value | Unit | Authority | Confidence | Source note |
| --- | ---: | --- | --- | --- | --- |
| Model designation | Hanse 460 | — | sourced-secondary | medium | Hanse brand/model summaries |
| Model introduction year | 2021 | year | sourced-secondary | medium | Secondary model-history summary |
| Length overall | 14.60 | m | sourced-secondary | medium | Secondary technical summary |
| Beam | 4.79 | m | sourced-secondary | medium | Secondary technical summary |
| Standard displacement | 12.6 | t | sourced-secondary | medium | Stated for standard version |
| Standard draft | 2.25 | m | sourced-secondary | medium | Standard/alternative distinction preserved |
| Alternative draft | 1.75 | m | sourced-secondary | medium | Alternative keel/draft option; exact option identity unverified |
| Air draft | 21.90 | m | sourced-secondary | medium | Secondary technical summary |
| Standard sail area | 106.0 | m² | sourced-secondary | medium | Aggregate standard-version value |
| Naval architecture | unknown | — | unknown | none | Manufacturer-controlled design attribution not captured in this version |
| Certification category | unknown | — | unknown | none | No controlled certification evidence included |

The source URL and retrieval context are recorded in the accompanying JSON. Secondary-source values are not promoted to manufacturer-authoritative or verified status.

## 5. Reference System Decomposition

The following top-level entities instantiate the generic model:

| System ID | Display name | Configuration treatment |
| --- | --- | --- |
| `system:vessel-design:hanse:460:hull-structure` | Hull, structure and watertight integrity | Present as reference system; construction details unknown |
| `system:vessel-design:hanse:460:deck-rig-sails` | Deck, rig and sail systems | Present; aggregate sail-area claim sourced; component inventory unknown |
| `system:vessel-design:hanse:460:propulsion-maneuvering` | Propulsion and maneuvering | Present; engine, gearbox, propeller and thruster details unknown |
| `system:vessel-design:hanse:460:steering-control` | Steering and control | Present; architecture and installed components unknown |
| `system:vessel-design:hanse:460:electrical` | Electrical generation, storage and distribution | Present; voltage domains, sources and capacities unknown |
| `system:vessel-design:hanse:460:navigation-comms` | Navigation and communications | Present; vendor and equipment inventory unknown |
| `system:vessel-design:hanse:460:machinery-fuel-exhaust` | Machinery, fuel and exhaust | Present; capacities and component identities unknown |
| `system:vessel-design:hanse:460:water-waste-bilge` | Freshwater, wastewater and bilge | Present; tank and pump details unknown |
| `system:vessel-design:hanse:460:environmental-control` | Heating, ventilation and environmental control | Present; option applicability unknown |
| `system:vessel-design:hanse:460:accommodation-domestic` | Accommodation and domestic systems | Present; layout variant not selected |
| `system:vessel-design:hanse:460:fire-safety` | Fire detection and suppression | Present; equipment and compliance evidence unknown |
| `system:vessel-design:hanse:460:lifesaving-emergency-security` | Lifesaving, emergency and security | Present; equipment inventory unknown |
| `system:vessel-design:hanse:460:anchoring-mooring` | Anchoring and mooring | Present; equipment identity and load ratings unknown |
| `system:vessel-design:hanse:460:monitoring-networks` | Monitoring, instrumentation and vessel networks | Present; protocols and topology unknown |
| `system:vessel-design:hanse:460:documentation-maintenance` | Documentation, procedures and maintenance support | Present; controlled document set not yet captured |

## 6. Major Equipment Inventory Template

Equipment records use `equipment:<parent-id>:<local-id>` and remain placeholders until supported by evidence.

| Equipment family | Required minimum fields | Current state |
| --- | --- | --- |
| Main propulsion engine | manufacturer, model, rating, serial applicability, source | unknown |
| Gearbox / saildrive | manufacturer, model, ratio, source | unknown |
| Propeller | type, dimensions, material, source | unknown |
| Steering gear | type, components, redundancy, source | unknown |
| Batteries | chemistry, nominal voltage, capacity, quantity, source | unknown |
| Charging sources | alternator, shore charger, renewable sources, ratings | unknown |
| Shore power | nominal supply, inlet, protection, distribution | unknown |
| Navigation electronics | function, manufacturer, model, network interface | unknown |
| Communications | VHF/AIS/satellite applicability and interfaces | unknown |
| Pumps and tanks | service, capacity, location, interface | unknown |
| Fire and lifesaving equipment | type, location, approval evidence, expiry state | unknown |

An unknown record means “not established in this reference configuration”; it does not mean the item is absent from the design or a vessel.

## 7. Variants and Applicability

The Hanse 460 design family may have configuration choices and production changes. Version `0.1.0` does not select or assert:

- keel or draft variant beyond recording sourced alternative draft values;
- interior cabin or accommodation layout;
- propulsion package;
- rig, sail or deck-equipment package;
- electrical or energy package;
- navigation-electronics package;
- comfort, climate or domestic-system options;
- production year, hull number or market-specific package.

Variant-specific facts require a variant identifier, effective context, source evidence and conflict handling. A value from one option package must not be generalized to the design family.

## 8. Provenance and Conflict Rules

Each factual claim must include source identifier, source owner, source class, retrieval date, applicable model/variant context and confidence. Where sources conflict:

1. both claims remain visible;
2. neither claim is silently selected;
3. authority and applicability differences are recorded;
4. a reviewer documents the resolution or deferral;
5. safety-relevant conflicts block promotion to verified status.

Manufacturer-controlled evidence may supersede a secondary reference only after applicability and version context are confirmed. A later source is not automatically more authoritative.

## 9. Mapping to the Vessel Reference Model

| Generic entity | Hanse 460 instantiation |
| --- | --- |
| VesselType | `vessel-type:sailing-yacht` |
| VesselDesign | `vessel-design:hanse:460` |
| Configuration | `configuration:vessel-design:hanse:460:reference-0.1.0` |
| VesselInstance | None |
| System | System identifiers in Section 5 |
| Equipment | Template only; no equipment facts asserted |
| Interface | Deferred to WP-0041 except for generic placeholder relationships |
| Capability | No safety- or performance-critical capability asserted |
| Constraint | Draft and dimensional claims remain sourced-secondary constraints |

## 10. Downstream Use

WP-0041 may populate equipment and interface structures while preserving unknowns and variant applicability. WP-0042 may reference stable system identifiers in operational scenarios. WP-0043 and WP-0044 may use the configuration as a reference topology but must not present it as live, verified or vessel-specific state.

## 11. Safety and Authority Boundary

This configuration does not certify seaworthiness, compliance, stability, performance, equipment suitability or operational readiness. It does not replace manufacturer documentation, approved manuals, surveys, inspections or vessel-specific records. It does not authorize navigation, maintenance, emergency action or automated control.

AI assistance may extract, compare and propose data, but cannot promote a claim to verified status or resolve a safety-relevant conflict without accountable human review.

## 12. Validation Checklist

A conforming update must confirm that:

- the design family is not represented as a physical vessel;
- every non-unknown value has provenance and authority classification;
- secondary claims are not labeled manufacturer-authoritative;
- variant applicability is explicit;
- unknown values remain visible;
- stable identifiers conform to `OMSP-REFERENCE-VESSEL-0001`;
- no safety or certification claim is inferred;
- no configuration promotion occurs without human evidence.

## 13. Known Limitations

The manufacturer product page and controlled brochure were not captured as repository evidence for this version. The current dimensional values therefore remain secondary-source claims. Equipment, interfaces, layout variants, tank capacities, propulsion, electrical architecture, network protocols and safety equipment are intentionally deferred or unknown.