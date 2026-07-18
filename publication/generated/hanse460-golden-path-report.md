# Hanse 460 Golden-Path Operational Report

> **ADVISORY MATERIAL — NOT A CERTIFIED PROCEDURE.** This document is
> advisory knowledge material generated from a governed model. It is not a
> certified procedure and does not replace manufacturer documentation,
> approved vessel procedures, or the judgment of the responsible human. It
> carries no seaworthiness, compliance, or navigation-safety claim, and it
> does not authorize navigation, maintenance, or emergency action. Every
> safety-relevant conclusion requires human judgment. Where this document
> conflicts with manufacturer documentation or the responsible human's
> judgment, the latter prevail.

## Generation provenance

- Source model: `OMSP-REFERENCE-HANSE460-ELECTRICAL-0001` version `0.4.0` (`reference/hanse460`)
- Source register: `reference/HANSE_460_SOURCE_REGISTER.md`
- Generator: `tooling/generate_report.py` version `0.1.0`
- Generation source reference: input content digest `sha256:38b92a449c21988732a5b43a94526dfff27cf6231feae4e74267f7a6c84af114` (deterministic digest over the model files and register — commit-equivalent per ODS-100-R-10)
- Conformance claim: ODS-100 v0.1.0 (Draft), ODS-300 v0.1.0 (Draft)
- Derived artifact: generated from the YAML model, never edited by hand (ODS-100-R-08/R-09); corrections belong in the source model.

## System overview

Energy chain of the modeled slice (shore power → charger → battery bank → DC distribution → consumers, with the inverter branch and the alternator charge path). Every modeled element of the slice is listed; key values carry their authority class or an explicit `unknown` (ODS-100-R-03).

### Shore power inlet

- Model element: `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:shore-power-inlet` (`equipment-shore-power-inlet.yaml`)
- Role: Shore power inlet and AC supply path of the golden-path slice: accepts the 230 V shore supply and feeds the battery charger. AC distribution beyond the shore-inlet-to-charger (and inverter output role) path is out of scope per golden path section 5.2.
- Protection: `unknown` — no protective device resolves to this element in the model

| Key value | Value | Authority class | Source |
| --- | --- | --- | --- |
| `quantity` | `unknown` — Number of shore-power inlets is not stated by any captured source. | `unknown` | — |
| `connector-standard` | `unknown` — Shore-connector standard is not stated by any captured source; the owner's manual describes only a "compatible shore-connecting line" without a connector standard. | `unknown` | — |
| `inlet-protection-rating` | shore inlet marked 230 V / 32 A; protected by a combined RCD/breaker "FI/LS 32A" (2F1) in the breaker box, with a 32 A galvanic isolator in the shore-1 feed; the owner's manual states the shore connection is fuse-protected with a GFCI device | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` |
| `nominal-supply-voltage` | 230 | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` |
| `provisioned-circuits` | shore 1 feed (standard drawing path, inlet 230 V / 32 A, breaker box 2F1 FI/LS 32 A, 32 A isolator); shore 2 option path (inlet 230 V / 32 A, breaker box 2F2 FI/LS 32 A, 32 A isolator); AC generator option path (2G1 generator 8000i/10000i with converter, breaker box 2F3 LS 32 A); breaker boxes located "technic room aft prt" | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` |

### Battery charger

- Model element: `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:battery-charger` (`equipment-battery-charger.yaml`)
- Role: Shore-powered battery charger of the golden-path slice: converts the 230 V shore supply into DC charging power for the service battery bank.
- Protection: `unknown` — no protective device resolves to this element in the model

| Key value | Value | Authority class | Source |
| --- | --- | --- | --- |
| `quantity` | `unknown` — Number of chargers is not stated by any captured source. | `unknown` | — |
| `charge-profile` | IUoUo, automatic, 3-step+ (12 V models: charge voltage bulk 14.4 V, absorption 14.25 V, float 13.25 V; adjustable; battery type settings Flooded (default), GEL, AGM, Lithium-ion (MLI), constant voltage) | `sourced-manufacturer` | `source:manufacturer:owner-held:mastervolt-chargemaster-plus-manual-10000016594-03:2026-07-16` |
| `input-voltage-range` | nominal input 120/240 V, 50/60 Hz | `sourced-manufacturer` | `source:manufacturer:owner-held:mastervolt-chargemaster-plus-manual-10000016594-03:2026-07-16` |
| `rated-charge-current` | 35 | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` |
| `standard-and-option-charger-ratings` | 35A charger standard (1xAGM); 50A charger option (2xAGM); 75A charger option (6xLi-Ion) | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` |

### Alternator charging source

- Model element: `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:alternator-charging` (`equipment-alternator-charging.yaml`)
- Role: Engine-driven charging source of the golden-path slice, modeled as a charging-source role only per golden path section 5.1. The engine start battery and engine starting circuit are out of scope per section 5.2. Presence and rating are transcribed from the owner-held series circuit diagram (WP-0093); engine-side vendor data awaits capture of the propulsion document set (source register section 4.4).
- Protection: `unknown` — no protective device resolves to this element in the model

| Key value | Value | Authority class | Source |
| --- | --- | --- | --- |
| `quantity` | 1 | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` |
| `charge-path-topology` | alternator output to the engine busbar; service-bank charging via the 70 mm2 charge wire between engine and service busbars through charge relay engine (20F1, 125 A) and the battery combiner (10K1) - path marked "not applicable with Li-Ion batterys"; with the Li-Ion option, charging runs instead through Mac Plus 12/12-50 DC-DC chargers and Charge Mate Pro (sheets 20, 21) | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` |
| `rated-output-current` | 125 | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` |
| `regulation-type` | `unknown` — Alternator regulation is not stated by the circuit diagram; engine/alternator vendor data awaits capture of the propulsion document set (source register section 4.4). | `unknown` | — |

### Service (house) battery bank

- Model element: `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:service-battery-bank` (`equipment-service-battery-bank.yaml`)
- Role: Service (house) energy-storage role of the golden-path slice: stores DC energy and supplies the main DC distribution. The captured source describes the whole-vessel standard battery set without allocating capacities to service versus other functions; bank-level values are therefore explicit unknowns.
- Protection: `unknown` — no protective device resolves to this element in the model

| Key value | Value | Authority class | Source |
| --- | --- | --- | --- |
| `quantity` | `unknown` — The battery count depends on the fitted variant (1 or 2 AGM, or 6 Li-Ion per the series circuit diagram, see service-bank-capacity); the installed as-built bank composition is not confirmed (issue #260), so no single count is asserted. | `unknown` | — |
| `bank-topology` | single service bank on the service busbar; all bank variants connect through common positive/negative battery links with the negative path through a 500 A shunt; battery temperature sensors (drawing symbols "MASTERVOLT battery temperature sensor" for charger, inverter and shunt) at the bank; drawing note: "All positive and negative battery wires must have the same length and must not be shortened! With shunt!" | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` |
| `chemistry` | AGM | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` |
| `critical-voltage-threshold` | `unknown` — Battery-chemistry- and manufacturer-specific; never asserted from general knowledge (golden path section 8); vendor manual pending capture (source register section 4.4). | `unknown` | — |
| `nominal-voltage` | `unknown` — Battery-level nominal voltage is not separately stated; the 12 V system-level claim is recorded on the system instance only. | `unknown` | — |
| `service-bank-capacity` | standard: 1x AGM 160 Ah (11G1); option XH1001: 2x AGM 160 Ah (11G1 + 11G2); option XH1005: 6x Li-Ion 105 Ah (11G3-11G8) | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` |
| `vessel-battery-set-composition` | 1x 90 Ah + 1x 160 Ah AGM (whole-vessel standard battery set) | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` |

### Main DC distribution

- Model element: `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:dc-main-distribution` (`equipment-dc-main-distribution.yaml`)
- Role: Main DC distribution panel/bus of the golden-path slice: distributes service-bank DC power to the modeled consumer set. Consumer branch ports are modeling structure; the physical circuit layout is unknown.
- Protection: DC main protection

| Key value | Value | Authority class | Source |
| --- | --- | --- | --- |
| `quantity` | `unknown` — The source states "main panels" without count or per-panel scope; the number of DC distribution panels is not established. | `unknown` | — |
| `bus-topology` | service busbar fed by the service battery bank; fused main paths off the busbar: service main 250 A with main switch (10F7/10S1), dc distribution aft 300 A with main switch (10F9/10S2), powerboard permanent 100 A (10F5), charge relay service 125 A (10F4), solar charger 80 A (10F6); the powerboard carries fuse boards X8/X9/X12 for high-power and relay-switched consumers; the DC panel carries the switched consumer circuits (interior lighting, refrigeration, navigation electronics, pumps, navigation lights, maneuvering, bathing platform) on SIMARINE SPU 303 units (parts 1-3) with a SIMARINE SCP 220 H monitoring unit (part 4) | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` |
| `dc-panel-unit-identity` | DC panel parts 1-3: SIMARINE SPU 303; DC panel part 4: SIMARINE SCP 220 H (tank/battery monitoring inputs) | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` |
| `main-panels-fitted` | True | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` |

### DC main protection

- Model element: `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:protection-dc-main` (`equipment-protection-dc-main.yaml`)
- Role: Protection role of the golden-path slice (golden path section 5.1 "protection-*": fuses, breakers, main battery switches) covering the modeled DC path from the service battery bank into the main DC distribution. Device inventory and ratings are transcribed from the owner-held series documents (WP-0093). Nothing in this model is an instruction to operate or bypass protection devices.
- Protection: `unknown` — no protective device resolves to this element in the model

| Key value | Value | Authority class | Source |
| --- | --- | --- | --- |
| `quantity` | `unknown` — The series device inventory is recorded in the device-inventory attribute; the as-built device count depends on fitted options and is not confirmed for any built vessel (issue #260). | `unknown` | — |
| `device-inventory` | service-side devices per the series circuit diagram, sheet 10: main switch service (10S1), main switch dc distribution aft (10S2), strip fuses 10F1-10F9 (charger supply, mac+ 1/2, charge mate pro, charge relay service, powerboard permanent, solar charger, service main, battery combiner control, dc distribution aft), 500 A latching relay with MPC battery-protection controller, battery combiner (10K1, not applicable with Li-Ion batteries); downstream branch protection on the powerboard (strip/blade fuse boards X8/X9/X12) and DC panel power unit (blade fuses F1-F31) | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` |
| `ratings` | main service batteries (main switch) 250 A; dc distribution aft 300 A; service batteries permanent+ 100 A; charge relay service (charger wire service-engine battery) 125 A; mac plus 100 A; charge mate pro relay 40 A; solar charger 80 A; charger supply 40 A standard / 63 A (2xAGM) / 80 A (Li-Ion); inverter/charger combination 250 A; battery combiner control fuse 3 A | `sourced-manufacturer` | `source:manufacturer:owner-held:owners-manual-460-en-v11:2026-07-16` |

### Service-battery measurement

- Model element: `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:measurement-service-battery` (`equipment-measurement-service-battery.yaml`)
- Role: Voltage/current measurement role of the golden-path slice (golden path section 5.1 "measurement-*": battery monitor / panel meters) observing the service battery bank. Measurement points are modeled as points, not as a live data pipeline (golden path section 5.2). The series measurement arrangement is transcribed from the owner-held circuit diagram (WP-0093); the installed display variant remains unconfirmed as-built.
- Protection: `unknown` — no protective device resolves to this element in the model

| Key value | Value | Authority class | Source |
| --- | --- | --- | --- |
| `quantity` | `unknown` — Instrument inventory (battery monitor, panel meters) is not stated by any captured source. | `unknown` | — |
| `calibration-state` | `unknown` — Measurement authority and calibration state are explicit unknowns per golden path section 8 preconditions. | `unknown` | — |
| `display-location` | `unknown` — The as-built display variant and its location are not confirmed (Simarine PICO vs. PICOone, source register section 4.4; issue #260). | `unknown` | — |
| `instrument-type` | 500 A DC shunt in the service-bank negative path ("shunt 500A installed"), Masterbus-connected, with a battery temperature sensor; battery voltage/shunt inputs terminate on the SIMARINE SCP 220 H unit (DC panel part 4, input "battery service") with an information display | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` |

### Inverter (DC to AC)

- Model element: `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:inverter` (`equipment-inverter.yaml`)
- Role: DC-to-AC inverter role of the golden-path slice (golden path section 5.1). Per the captured US-market standard specification the inverter is NOT standard equipment: it is available only as factory option XH2201 (inverter/charger, only with battery upgrade XH1001 or XH1005). The role is kept in the model because section 5.1 mandates it; its presence in any built configuration is an explicit unknown.
- Protection: `unknown` — no protective device resolves to this element in the model

| Key value | Value | Authority class | Source |
| --- | --- | --- | --- |
| `quantity` | `unknown` — Not standard equipment (factory option XH2201); installed as-built configuration unknown (source register section 3.3 applicability note for named option equipment). | `unknown` | — |
| `option-xh2201-rating` | 12 V / 2600 W - 100 A, incl. AC panel | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` |
| `standard-fitment` | not standard equipment; factory option XH2201 (inverter/charger, incl. AC panel), only with XH1001 or XH1005 | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` |
| `transfer-behavior` | `unknown` — Transfer behavior is not established by any captured source; vendor manual pending capture (source register section 4.4). | `unknown` | — |

### DC consumer — navigation lights

- Model element: `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:dc-consumer-navigation-lights` (`equipment-dc-consumer-navigation-lights.yaml`)
- Role: Navigation-lights consumer role of the golden-path slice, fed from the main DC distribution. Member of the source-fixed dc-consumer set (LED navigation lights per the captured standard specification).
- Protection: `unknown` — no protective device resolves to this element in the model

| Key value | Value | Authority class | Source |
| --- | --- | --- | --- |
| `quantity` | `unknown` — The source states LED navigation lights without count or inventory; the light inventory is not established. | `unknown` | — |
| `circuit-inventory` | four switched navigation-light circuit groups on DC panel part 2: navi lts 1/2 (fuse F23, 5 A), tricolor lts (F22, 5 A), steaming lts (F21, 5 A), anchor lts (F20, 5 A); light functions per the owner's manual: side, stern, masthead and anchor lights in fixed positions | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` |
| `lamp-technology` | LED | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` |
| `power-draw` | `unknown` — Electrical power draw is not transcribed: per-light consumption figures exist only in the Aqua Signal vendor manuals, and the installed light series/positions are not confirmed as-built (issue #260). | `unknown` | — |
| `supply-voltage` | `unknown` — Not separately stated for the navigation lights; the 12 V system-level claim is recorded on the system instance only. | `unknown` | — |

### DC consumer — electric bilge pump

- Model element: `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:dc-consumer-bilge-pump` (`equipment-dc-consumer-bilge-pump.yaml`)
- Role: Electric bilge-pump consumer role of the golden-path slice, fed from the main DC distribution. Member of the source-fixed dc-consumer set. The captured specification lists "electric and manual bilge pump"; the manual pump is not an electrical consumer and is not modeled here.
- Protection: `unknown` — no protective device resolves to this element in the model

| Key value | Value | Authority class | Source |
| --- | --- | --- | --- |
| `quantity` | 1 | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` |
| `control-arrangement` | automatic (float switch) or manual operation via the bilge-pump panel (auto/manual switch with red/green LEDs, drawing location "pantry stb"); bilge-alarm buzzer in the cockpit (added at drawing rev. 03, "bp alarm added") | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` |
| `drive` | electric | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` |
| `rated-flow` | 69 | `sourced-manufacturer` | `source:manufacturer:owner-held:owners-manual-460-en-v11:2026-07-16` |
| `supply-voltage` | `unknown` — Not separately stated for the bilge pump; the 12 V system-level claim is recorded on the system instance only. | `unknown` | — |

### DC consumer — electric freshwater pump

- Model element: `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:dc-consumer-freshwater-pump` (`equipment-dc-consumer-freshwater-pump.yaml`)
- Role: Electric freshwater-pump consumer role of the golden-path slice, fed from the main DC distribution. Member of the source-fixed dc-consumer set. Only the pump's electrical-consumer role is modeled here; the freshwater system itself is a non-electrical system and out of scope per golden path section 5.2.
- Protection: `unknown` — no protective device resolves to this element in the model

| Key value | Value | Authority class | Source |
| --- | --- | --- | --- |
| `quantity` | 1 | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` |
| `drive` | electric | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` |
| `rated-flow` | `unknown` — Pump rating is not stated by any captured source. | `unknown` | — |
| `supply-voltage` | `unknown` — Not separately stated for the freshwater pump; the 12 V system-level claim is recorded on the system instance only. | `unknown` | — |

### DC consumer — refrigeration

- Model element: `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:dc-consumer-refrigeration` (`equipment-dc-consumer-refrigeration.yaml`)
- Role: Refrigeration consumer role of the golden-path slice, fed from the main DC distribution. Member of the source-fixed dc-consumer set (standard 12 V fridge per the captured specification).
- Protection: `unknown` — no protective device resolves to this element in the model

| Key value | Value | Authority class | Source |
| --- | --- | --- | --- |
| `quantity` | 1 | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` |
| `gross-volume` | 135 | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` |
| `power-draw` | `unknown` — Electrical power draw is not stated by any captured source. | `unknown` | — |
| `supply-voltage` | 12 | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` |

## Scenario — Document-stated maintenance obligations due on the electrical slice (reference review scenario)

- Scenario ID: `scenario:hanse:460:maintenance-due:0.1.0`
- Class: `maintenance`
- Accountable authority: Skipper (human). The skipper holds command authority for every decision in this scenario, including whether and when any document-stated test or servicing is performed and by whom; the owner's manual assigns installation, alterations and maintenance of the electrical system to a competent marine electrical technician. Software and monitoring equipment may observe, record, warn and recommend only; no command authority is assigned to software (OMSP-REFERENCE-SCENARIO-0001 section 5).
- Objective: Answer, from the modeled electrical slice with full provenance, the question "which maintenance is due on this boat's electrical slice?": which periodic maintenance, inspection and test obligations the captured documents state for the modeled equipment roles, which of them are due — or cannot be shown not-due — and in which conservative order a human reviews them. This is a reference review order for the design-family configuration; it never provides the maintenance instructions themselves and is never an approved vessel procedure.

### Trigger — maintenance-due

- Description: Calendar or record review, or an observation, indicates that a document-stated maintenance obligation on the modeled electrical slice has elapsed or cannot be shown satisfied. The captured item-specific intervals are recorded in the causes below (unused batteries: full charge at least once a month; electrical installation: examination at least once a year; electrical system: inspection at least biennially; GFCI function test: "regularly", no interval stated). No captured document defines a consolidated maintenance schedule for the vessel, and no captured document defines a maintenance log, so the due-state usually rests on incomplete records and is treated conservatively.
- Source: inferred
- Timestamp handling: Recorded at review time by the reviewing human. This reference scenario defines the recording rule, not a real event.
- Confidence: low
- Threshold: `unknown` — No single consolidated maintenance-due threshold exists: the captured documents state item-specific intervals (recorded per cause with their extraction locations), the GFCI test interval is stated only as "regularly", and any battery-model-specific maintenance intervals are blocked pending as-built confirmation of the installed battery model (issue #260; e.g. the Lifos document document:lifos:lifos-105-battery-instructions-8546:undated applies only if the Lifos 105 is confirmed installed). (authority: `unknown`, source: —)

### Affected systems — maintenance-due

- `system:vessel-design:hanse:460:electrical`

### Likely causes — maintenance-due

**Cause: `battery-charge-upkeep-interval-elapsed`**

- Cause ID: `cause:hanse:460:maintenance-due:battery-charge-upkeep-interval-elapsed`
- Description: Battery charge-upkeep obligation elapsed: the owner's manual states the AGM / lithium batteries "require low maintenance and should be well charged at all times", to be checked regularly, and that batteries not used for a long time "should be fully charged at least once a month"; more than a month without a recorded full charge while the bank is unused makes this item due.
- Implicates:
  - `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:service-battery-bank`
  - `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:measurement-service-battery`
- Evidence requirement: Owner's manual document:hanseyachts:owners-manual-460-en:v11, Chapter 2 section 1.5.1, "Maintenance" block, printed page 64 (PDF page 74), plus the last-full-charge record (step 2) and the present charge-state observation at the shunt display (step 3). Battery-model-specific charge criteria are blocked pending as-built confirmation (issue #260).

**Cause: `installation-examination-interval-elapsed`**

- Cause ID: `cause:hanse:460:maintenance-due:installation-examination-interval-elapsed`
- Description: Annual installation-examination obligation elapsed: the charger family manual requires no specific maintenance of the charger itself but requires examining the electrical installation "on a regular basis, at least once a year", with defects such as loose connections or damaged wiring to be corrected immediately; more than a year without a recorded examination makes this item due.
- Implicates:
  - `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:battery-charger`
  - `connection:configuration:vessel-design:hanse:460:reference-0.1.0:shore-power-feed`
  - `connection:configuration:vessel-design:hanse:460:reference-0.1.0:charger-dc-output`
- Evidence requirement: Family manual document:mastervolt:chargemaster-plus-manual-10000016594:03, section 5.6 "Maintenance" (PDF page 24), plus the last-examination record (step 2) and the visual condition observation of the charger installation (step 5). The installed charger model is unconfirmed as-built (issue #260); the examination itself belongs to a qualified person, not to this scenario.

**Cause: `gfci-function-test-interval-unknown`**

- Cause ID: `cause:hanse:460:maintenance-due:gfci-function-test-interval-unknown`
- Description: GFCI function-test obligation not shown satisfied: the owner's manual states the shore power is protected with a GFCI device and that "this functionality of the switch must be tested regularly by pressing the release button or with the help of an electric tester" — without stating an interval; with no stated interval and no test record, the item cannot be shown not-due and is treated conservatively as due.
- Implicates:
  - `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:shore-power-inlet`
  - `connection:configuration:vessel-design:hanse:460:reference-0.1.0:shore-power-feed`
- Evidence requirement: Owner's manual document:hanseyachts:owners-manual-460-en:v11, Chapter 2 section 1.5.2 "Shore connection", printed page 66 (PDF page 76), plus the last-test record (step 2) — explicit unknown marker: the test interval is unsourced ("regularly"). Whether and when the test is performed is a skipper decision following the owner's manual (step 6), never an instruction of this scenario.

**Cause: `system-inspection-interval-elapsed`**

- Cause ID: `cause:hanse:460:maintenance-due:system-inspection-interval-elapsed`
- Description: Biennial system-inspection obligation elapsed: the owner's manual requires that the electrical system be inspected "at least biennially" and that installation, alterations and maintenance be performed by a competent marine electrical technician; more than two years without a recorded inspection makes this item due.
- Implicates:
  - `system:vessel-design:hanse:460:electrical`
- Evidence requirement: Owner's manual document:hanseyachts:owners-manual-460-en:v11, Chapter 1 section 1.2.5 "Electrical system", printed page 6 (PDF page 16), plus the last-inspection record (step 2). The inspection itself is professional work outside this scenario.

**Cause: `maintenance-record-gap`**

- Cause ID: `cause:hanse:460:maintenance-due:maintenance-record-gap`
- Description: Record gap: no evidence of last completion exists or can be located for one or more document-stated items. No captured document defines a maintenance log or record format for the vessel, so a missing record is a plausible origin of the due-state and is never interpreted as "not due".
- Implicates:
  - `system:vessel-design:hanse:460:electrical`
- Evidence requirement: Outcome of the record review (step 2) — explicit unknown marker: the existence, format and completeness of the vessel's maintenance records are unsourced; the conservative treatment (missing record = due) follows OMSP-REFERENCE-SCENARIO-0001 section 4.

**Cause: `condition-finding`**

- Cause ID: `cause:hanse:460:maintenance-due:condition-finding`
- Description: Condition finding: an observed condition indicates maintenance need regardless of calendar — battery poles not clean or not protected against corrosion (the owner's manual requires the poles clean and protected with pole grease), or defects of the installation such as loose connections or damaged wiring (which the charger family manual requires to be corrected immediately).
- Implicates:
  - `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:service-battery-bank`
  - `connection:configuration:vessel-design:hanse:460:reference-0.1.0:battery-main-feed`
  - `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:battery-charger`
- Evidence requirement: Visual condition observations (steps 4 and 5) recorded against the owner's manual document:hanseyachts:owners-manual-460-en:v11 (Chapter 2 section 1.5.1, printed page 64) and the family manual document:mastervolt:chargemaster-plus-manual-10000016594:03 (section 5.6, PDF page 24). Observation only: any correction is routed to the accountable human / qualified service.

### Inspection sequence — maintenance-due

Reference inspection order, not an approved vessel procedure. Steps follow ODS-300 procedure language; every step field the model does not establish is rendered as an explicit unknown.

#### Step 1 — `scenario-step:scenario:hanse:460:maintenance-due:0.1.0:1` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human)
- Action: Assemble the document-stated maintenance items applicable to the modeled slice and record each with its source location: battery charge upkeep (equipment role service-battery-bank; owner's manual document:hanseyachts:owners-manual-460-en:v11 Chapter 2 section 1.5.1 "Maintenance", printed page 64, PDF page 74), installation examination (equipment role battery-charger; family manual document:mastervolt:chargemaster-plus-manual-10000016594:03 section 5.6, PDF page 24), GFCI function test (equipment role shore-power-inlet; owner's manual Chapter 2 section 1.5.2, printed page 66) and the biennial system inspection (system-level; owner's manual Chapter 1 section 1.2.5, printed page 6). Record explicitly that battery-model-specific items are blocked pending as-built confirmation (issue #260).
- Entry criteria: Trigger condition present; preconditions reviewed by the skipper.
- Completion criteria: Item list with source locations and blocked items recorded.
- Expected observation: Four document-stated items on the modeled slice; any further items belong to documents outside the captured set and are recorded as out of scope.
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: If an item cannot be tied to a captured source location, it is not asserted: record it as unsourced and route to the conservative human-review branch.

#### Step 2 — `scenario-step:scenario:hanse:460:maintenance-due:0.1.0:2` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human)
- Action: Establish last-completion evidence for each item from the vessel's records (equipment roles service-battery-bank, battery-charger, shore-power-inlet) — explicit unknown marker: no captured document defines a maintenance log or record format, so the existence and completeness of such records are unsourced and the search method is left to the skipper. A missing record never becomes "not due" (OMSP-REFERENCE-SCENARIO-0001 section 4).
- Entry criteria: Step 1 completed and recorded.
- Completion criteria: For each item: last-completion date recorded, or recorded statement that no record exists.
- Expected observation: Item-by-item due assessment against the document-stated intervals; items without record or interval (GFCI test) remain conservatively due.
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: Conflicting records are never resolved by this scenario: route to the conservative human-review branch.

#### Step 3 — `scenario-step:scenario:hanse:460:maintenance-due:0.1.0:3` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human); monitoring display, informed source only
- Action: Observe the present charge state of the service bank at the shunt display (equipment roles measurement-service-battery and service-battery-bank; series measurement arrangement per the series circuit diagram document:hanseyachts:h20b-7215-100-010:03 sheets 10 and 19) against the owner's-manual requirement that the batteries be well charged at all times (Chapter 2 section 1.5.1, printed page 64). The installed display variant and its calibration state are explicit unknowns (issue #260); a charge-state conclusion from a single uncorroborated reading belongs to the human.
- Entry criteria: Step 2 completed.
- Completion criteria: Charge-state observation, time and measurement source recorded.
- Expected observation: A well-charged bank (weakens the charge-upkeep cause) or a low state of charge (supports it and may route to the critical-voltage scenario).
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: If the reading indicates a critically low bank, continue under scenario:hanse:460:service-battery-critical-voltage:0.1.0 and record the handover.

#### Step 4 — `scenario-step:scenario:hanse:460:maintenance-due:0.1.0:4` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human)
- Action: Visually observe the battery poles and terminal area of the service bank without touching conductors (equipment role service-battery-bank; the connected battery links carry high currents — battery-main-feed): clean poles, corrosion protection with pole grease per the owner's manual document:hanseyachts:owners-manual-460-en:v11 Chapter 2 section 1.5.1, printed page 64 (PDF page 74). Observation only: any cleaning or greasing is maintenance execution following the owner's manual, outside this scenario.
- Entry criteria: Step 3 completed.
- Completion criteria: Pole/terminal condition recorded; anomalies noted explicitly.
- Expected observation: Clean, protected poles (weakens the condition-finding cause) or corrosion/contamination (supports it; routes to human disposition).
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: Any sign of damage, heat, smell or electrolyte hazard means: do not touch, stop the sequence, route to the conservative human-review branch / qualified service.

#### Step 5 — `scenario-step:scenario:hanse:460:maintenance-due:0.1.0:5` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human)
- Action: Visually observe the accessible charger installation for the defect classes the family manual names — loose connections, damaged wiring — without opening the charger enclosure or any switchboard (equipment role battery-charger, charger located "sitting corner prt fwd" per the series circuit diagram document:hanseyachts:h20b-7215-100-010:03 sheet 10; defect classes per the family manual document:mastervolt:chargemaster-plus-manual-10000016594:03 section 5.6, PDF page 24). Observation only: the manual's requirement that defects "must be corrected immediately" is discharged by routing the finding to the accountable human and qualified service, never by in-scenario intervention.
- Entry criteria: Step 4 completed.
- Completion criteria: Visible installation condition recorded; findings noted explicitly.
- Expected observation: No visible defect (weakens the condition-finding cause) or a visible defect (supports it and makes the correction an immediate human/service action).
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: Any visible defect or hazard sign (heat, smell, smoke, discolored insulation) means: stop the sequence and route to the conservative human-review branch / qualified service without delay.

#### Step 6 — `scenario-step:scenario:hanse:460:maintenance-due:0.1.0:6` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human), sole decision authority
- Action: Decide the disposition of the GFCI function test (equipment role shore-power-inlet): whether and when the owner's-manual test ("pressing the release button or with the help of an electric tester", document:hanseyachts:owners-manual-460-en:v11 Chapter 2 section 1.5.2, printed page 66, PDF page 76) is performed, considering that the test de-energizes the shore-supplied AC system. Performing the test follows the owner's manual and the skipper's timing decision; this scenario only records the decision and, if performed, the result.
- Entry criteria: Step 2 completed; GFCI item conservatively due.
- Completion criteria: Decision (perform now / defer with rationale) recorded; test result recorded if performed.
- Expected observation: A recorded, dated disposition that replaces the unsourced "regularly" interval with an accountable human decision.
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: A failed or ambiguous test result means: leave the shore supply de-energized as found and route to qualified service; this scenario never instructs re-energizing.

#### Step 7 — `scenario-step:scenario:hanse:460:maintenance-due:0.1.0:7` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human), with competent marine electrical technician / qualified service consulted
- Action: Record the disposition of every item: due / not due / cannot be shown not-due, and for each due item the intended execution path — the owner's manual assigns installation, alterations and maintenance to a competent marine electrical technician (document:hanseyachts:owners-manual-460-en:v11 Chapter 1 section 1.2.5, printed page 6) and OEM instructions govern the work itself (the manual requires observing the operating instructions of all OEM manuals). Scheduling and execution are human decisions outside this scenario (equipment roles service-battery-bank, battery-charger, shore-power-inlet).
- Entry criteria: Steps 1-6 completed.
- Completion criteria: Item-by-item disposition and execution path recorded.
- Expected observation: A complete disposition list in which no due item is silently dropped and no execution is claimed by this scenario.
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: If a due item cannot be assigned an execution path, it remains recorded as open and routes to the conservative human-review branch; it is never closed by assumption.

#### Step 8 — `scenario-step:scenario:hanse:460:maintenance-due:0.1.0:8` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human)
- Action: Close the scenario: record the outcome class (expected / degraded-but-controlled / aborted / unacceptable / unknown per OMSP-REFERENCE-SCENARIO-0001 section 9), the evidence gathered at each step, and every value that remained unknown (equipment roles service-battery-bank, battery-charger and shore-power-inlet as the reviewed elements; recording rule defined by this scenario, no captured document prescribes a log format — explicit unknown marker).
- Entry criteria: Sequence ended by completed disposition, by skipper decision, or by a stop/abort condition.
- Completion criteria: Outcome, evidence list and open unknowns recorded.
- Expected observation: A closed record whose every claim carries its source or an explicit unknown, consistent with the provenance rules of the model package.
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: If the closing record would contain a claim without source or unknown marking, the record is incomplete: route to the conservative human-review branch instead of closing.

### Decision point — continuation decision — maintenance-due

First-class decision construct (ODS-300-R-07/R-08) derived from the scenario's modeled stop/abort conditions and mandatory conservative human-review branch:

- Available branches:
  - Continue the inspection sequence (no stop/abort condition met).
  - Stop/abort: Abort immediately on any sign of electrical hazard (heat, smell, smoke, discolored insulation, damaged battery casing) during any observation; do not continue and route to qualified service.
  - Stop/abort: Stop at any visible installation defect: the family manual requires immediate correction, which is a human/service action; the review sequence does not continue past an uncorrected hazard-relevant defect.
  - Stop/abort: Stop if maintenance records conflict and the conflict cannot be resolved by observation; do not proceed on unresolved conflict.
  - Stop/abort: Stop at any step whose required evidence is blocked by an as-built unknown (installed battery model, charger model, display variant — issue #260); never substitute a guessed value.
  - Stop/abort: Hand over to scenario:hanse:460:service-battery-critical-voltage:0.1.0 when its trigger condition is observed; the handover is recorded.
  - Conservative human review (mandatory default for unknown or conflicting evidence, below).
- Decision authority: Skipper (human). The skipper holds command authority for every decision in this scenario, including whether and when any document-stated test or servicing is performed and by whom; the owner's manual assigns installation, alterations and maintenance of the electrical system to a competent marine electrical technician. Software and monitoring equipment may observe, record, warn and recommend only; no command authority is assigned to software (OMSP-REFERENCE-SCENARIO-0001 section 5).
- Required evidence: the entry/completion criteria and expected observations of the executed steps (rendered above); unknown markers remain unknown.
- Time sensitivity: `unknown` — not modeled by the source scenario (explicit unknown per ODS-300-R-09).
- Fallback behaviour (conservative human-review branch): Unknown or conflicting evidence at any step — missing records, unstated intervals, blocked battery-model-specific items — routes to the accountable human skipper for conservative review (consulting a competent marine electrical technician or the suppliers of the cited OEM documents as the skipper decides); the scenario never resolves such a conflict automatically, and values blocked pending as-built confirmation (installed battery model, charger model, display variant — issue #260) remain unknowns until closed through the source register, never through in-scenario assumption.

### Safety constraints — maintenance-due

- This scenario never provides maintenance instructions for live use (OMSP-REFERENCE-SCENARIO-0001 section 14): it reviews which document-stated obligations are due; execution follows the cited source documents, the competent marine electrical technician requirement of the owner's manual, and the skipper's decision.
- Electrical hazard: the service bank and its links carry high currents (500 A shunt path, 150 mm2 battery links per the series circuit diagram); all observations are contact-free, no step authorizes work on live conductors, battery terminals, opened switchboards or the charger enclosure.
- The GFCI function test de-energizes the shore-supplied AC system; whether and when it is performed is a skipper decision in full operational context, following the owner's manual only.
- No instruction to bypass, defeat or force any protection device exists in this scenario, and none may be derived from it.
- Battery-model-specific maintenance (including any lithium-battery instruction of the Lifos document set) is blocked pending as-built confirmation of the installed battery model (issue #260); the owner's manual itself requires observing the manufacturer's instructions for the fitted batteries.
- Conservative stop: at any ambiguity, conflicting evidence or suspected hazard, the sequence stops and the situation routes to the accountable human; proceeding on unresolved conflict is prohibited.
- Advisory boundary: this scenario is reference material derived from a design-family model; it is not an approved procedure, carries no seaworthiness or navigation-safety claim, and approved vessel instructions and the skipper's judgment always prevail (OMSP-REFERENCE-SCENARIO-0001 section 14).

### Unacceptable outcomes and stop/abort conditions — maintenance-due

- Unacceptable outcome: Any maintenance execution performed from this scenario's text instead of the cited source documents and qualified persons.
- Unacceptable outcome: A missing record or an unstated interval silently treated as "not due" or "satisfied".
- Unacceptable outcome: Battery-model-specific maintenance applied while the installed battery model is unconfirmed as-built.
- Unacceptable outcome: A visible installation defect (loose connection, damaged wiring) recorded but not routed to the accountable human and qualified service.
- Unacceptable outcome: Any protection device bypassed, defeated or re-energized without understanding its state.
- Unacceptable outcome: Software or this scenario acting as command authority for any decision.
- Stop/abort condition: Abort immediately on any sign of electrical hazard (heat, smell, smoke, discolored insulation, damaged battery casing) during any observation; do not continue and route to qualified service.
- Stop/abort condition: Stop at any visible installation defect: the family manual requires immediate correction, which is a human/service action; the review sequence does not continue past an uncorrected hazard-relevant defect.
- Stop/abort condition: Stop if maintenance records conflict and the conflict cannot be resolved by observation; do not proceed on unresolved conflict.
- Stop/abort condition: Stop at any step whose required evidence is blocked by an as-built unknown (installed battery model, charger model, display variant — issue #260); never substitute a guessed value.
- Stop/abort condition: Hand over to scenario:hanse:460:service-battery-critical-voltage:0.1.0 when its trigger condition is observed; the handover is recorded.

### Related equipment — maintenance-due

- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:service-battery-bank`
- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:battery-charger`
- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:shore-power-inlet`
- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:measurement-service-battery`

### Source documents — maintenance-due

- `document:hanseyachts:h20b-7215-100-010:03`
- `document:hanseyachts:owners-manual-460-en:v11`
- `document:mastervolt:chargemaster-plus-manual-10000016594:03`
- `document:lifos:lifos-105-battery-instructions-8546:undated`

### Assumptions — maintenance-due

- The standard reference configuration applies; fitted options and their maintenance items (generator, thrusters, HVAC and other §4.4 pending-capture document sets) are outside this slice and not assumed present.
- Affected-set derivation rule (document-derived, not graph-derived): related_equipment is exactly the set of equipment roles for which a captured register document states a periodic maintenance, inspection or test requirement, plus measurement roles whose measurement_points measure such a role; the biennial system-level inspection is carried by affected_systems. Rule and citations: README.md section 9.
- The four maintenance items reflect the captured document set of register v0.3.0 only; documents pending capture (§4.4 inventory) may add items and do not narrow the recorded ones.

### Declared unknowns — maintenance-due

- No consolidated maintenance schedule, maintenance log or record format is defined by any captured document; last-completion evidence for every item is unsourced until vessel records are reviewed.
- The GFCI function-test interval is stated only as "regularly"; no captured document quantifies it.
- Installed battery model, charger model and display variant are unconfirmed as-built (issue #260); every battery-model-specific maintenance item (including the Lifos instructions) is blocked until confirmation.
- The calibration state of the service-battery measurement role is unknown; charge-state observations are single-source unless the skipper adds an independent reading.

### Exclusions — maintenance-due

- The execution of any maintenance, test or repair, and any instruction for it: this scenario is a review/disposition reference only; execution follows the cited documents and qualified persons.
- Maintenance items of equipment outside the golden-path electrical slice (engine/propulsion set, generator, navigation electronics, windlass, pumps' vendor-specific service items and all §4.4 pending-capture sets).
- Inverter role and AC consumers (option XH2201; no realized connection instance in the standard reference configuration) and the alternator's engine-side service items (propulsion document set pending capture).
- Seasonal/winter storage procedures (the owner's manual winter note is recorded as context; the storage activity itself is outside this review scenario).

## Scenario — Service-battery voltage critically low (reference inspection scenario)

- Scenario ID: `scenario:hanse:460:service-battery-critical-voltage:0.1.0`
- Class: `degraded`
- Accountable authority: Skipper (human). The skipper holds command authority for every decision in this scenario, including load shedding and any protection or charging state change. Software and monitoring equipment (measurement role, panel displays) may observe, record, warn and recommend only; no command authority is assigned to software (OMSP-REFERENCE-SCENARIO-0001 section 5).
- Objective: Answer, from the modeled electrical slice with full provenance, the golden-path question "service-battery voltage is critical — what does that mean on this boat?": which systems and equipment roles are affected, which causes are plausible and what evidence each requires, and in which conservative order a human can inspect them. This is a reference inspection order for the design-family configuration, never an approved vessel procedure.

### Trigger — service-battery-critical-voltage

- Description: Observed or reported service-battery voltage at or below a critical threshold, at the service-battery measurement role (series arrangement: 500 A shunt in the bank negative path with the battery voltage/shunt inputs terminating on the SIMARINE SCP 220 H unit, input "battery service", with an information display — series circuit diagram sheets 10 and 19). The numeric threshold is deliberately not asserted: it is battery-chemistry- and manufacturer-specific, no captured register document states a critical-low value for the reference AGM set, the installed battery model is unconfirmed as-built, and the display variant-specific alarm values are blocked pending as-built confirmation (issue #260). Confidence of a real trigger event starts at medium at best, because the calibration state of the measurement role is an explicit unknown; an independent cross-check (inspection step 2) is required before treating the reading as confirmed.
- Source: observed
- Timestamp handling: Recorded at observation time by the observing human or from the monitoring display log. This reference scenario defines the recording rule, not a real event.
- Confidence: medium
- Threshold: `unknown` — Critical-low voltage threshold for the service bank: no captured source register document states it; never asserted from general knowledge (golden path section 8). Closure path: as-built confirmation of the installed battery model, then transcription from the confirmed manufacturer document (issue #260; source register section 4.4). Display variant-specific alarm values are likewise blocked (issue #260). (authority: `unknown`, source: —)

### Affected systems — service-battery-critical-voltage

- `system:vessel-design:hanse:460:electrical`

### Likely causes — service-battery-critical-voltage

**Cause: `charge-path-shore-failure`**

- Cause ID: `cause:hanse:460:service-battery-critical-voltage:charge-path-shore-failure`
- Description: Shore charging path not delivering: shore supply absent or disconnected, inlet protection open, or battery charger not producing DC output. Derived charge path: shore-power-inlet -> (shore-power-feed) -> battery-charger -> (charger-dc-output) -> service-battery-bank.
- Implicates:
  - `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:shore-power-inlet`
  - `connection:configuration:vessel-design:hanse:460:reference-0.1.0:shore-power-feed`
  - `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:battery-charger`
  - `connection:configuration:vessel-design:hanse:460:reference-0.1.0:charger-dc-output`
- Evidence requirement: Observation of shore-supply presence and charger operating state (inspection step 4), and of charging current at the shunt display while the shore path should be active. Charger status indications are family-common values from the ChargeMaster Plus manual; the installed charger model is unconfirmed as-built (issue #260).

**Cause: `charge-path-alternator-failure`**

- Cause ID: `cause:hanse:460:service-battery-critical-voltage:charge-path-alternator-failure`
- Description: Engine-driven charging path not delivering while under way: alternator, charge-relay/battery-combiner path or charge wire not charging the service bank. Derived charge path: alternator-charging -> (alternator-charge-feed) -> service-battery-bank; the realized path depends on the fitted battery variant (series circuit diagram sheets 10, 20, 21).
- Implicates:
  - `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:alternator-charging`
  - `connection:configuration:vessel-design:hanse:460:reference-0.1.0:alternator-charge-feed`
- Evidence requirement: Charging-current observation at the shunt display with the engine running (inspection step 5, engine start is a skipper decision). Alternator regulation data is an explicit unknown pending the propulsion document set (source register section 4.4).

**Cause: `excessive-consumer-load`**

- Cause ID: `cause:hanse:460:service-battery-critical-voltage:excessive-consumer-load`
- Description: Genuine deep discharge from consumer load exceeding charging input over time, through the main DC distribution to the derived consumer set (refrigeration, navigation lights, bilge pump, freshwater pump).
- Implicates:
  - `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:dc-main-distribution`
  - `connection:configuration:vessel-design:hanse:460:reference-0.1.0:battery-main-feed`
  - `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:dc-consumer-refrigeration`
  - `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:dc-consumer-navigation-lights`
  - `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:dc-consumer-bilge-pump`
  - `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:dc-consumer-freshwater-pump`
- Evidence requirement: Present discharge current at the 500 A shunt reading compared against which consumers are switched on (inspection step 3). Expected per-consumer draw is largely unsourced in the model (explicit unknowns), so this comparison is qualitative and its conclusion belongs to the human.

**Cause: `protection-open`**

- Cause ID: `cause:hanse:460:service-battery-critical-voltage:protection-open`
- Description: A protection device in the charge or supply path is open (main switch, strip fuse, latching relay / battery-protection controller per the series device inventory), isolating a charge source or misrepresenting the bank state at the panel.
- Implicates:
  - `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:protection-dc-main`
  - `connection:configuration:vessel-design:hanse:460:reference-0.1.0:battery-main-feed`
- Evidence requirement: Visual state observation of main switches and fuse positions per the owner's manual fuse overview (inspection step 6). Observation only: this scenario contains no instruction to operate, reset or bypass any protection device.

**Cause: `battery-degradation`**

- Cause ID: `cause:hanse:460:service-battery-critical-voltage:battery-degradation`
- Description: Battery ageing or cell damage: the bank reaches the critical voltage under normal load because its usable capacity is degraded.
- Implicates:
  - `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:service-battery-bank`
- Evidence requirement: Manufacturer acceptance criteria for the installed battery model — currently blocked: the installed model is unconfirmed as-built and no manufacturer battery value is transcribed (issue #260). Until sourced, degradation cannot be confirmed or excluded from the model; assessment routes to the conservative human-review branch (inspection step 8).

**Cause: `measurement-error`**

- Cause ID: `cause:hanse:460:service-battery-critical-voltage:measurement-error`
- Description: Measurement error: the displayed voltage is wrong (shunt wiring, display fault, configuration or calibration), and the bank is not actually at a critical level.
- Implicates:
  - `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:measurement-service-battery`
- Evidence requirement: An independent second voltage reading compared against the panel value (inspection step 2). The calibration state of the measurement role is an explicit unknown; a single uncorroborated reading is never treated as confirmed.

### Inspection sequence — service-battery-critical-voltage

Reference inspection order, not an approved vessel procedure. Steps follow ODS-300 procedure language; every step field the model does not establish is rendered as an explicit unknown.

#### Step 1 — `scenario-step:scenario:hanse:460:service-battery-critical-voltage:0.1.0:1` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human), responsible; monitoring display, informed source only
- Action: Observe and record the service-battery voltage and its instrument: equipment role measurement-service-battery (500 A shunt / SCP 220 H chain, series circuit diagram document:hanseyachts:h20b-7215-100-010:03 sheets 10 and 19). Record which display produced the value; the installed display variant is an explicit unknown (issue #260).
- Entry criteria: Trigger condition observed or reported; preconditions reviewed by the skipper.
- Completion criteria: Voltage value, time and measurement source recorded.
- Expected observation: A voltage reading at or below the (unsourced, explicitly unknown) critical threshold; the reading itself is the evidence under test, not yet a confirmed bank state.
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: If no reading can be obtained, or the display state is anomalous, stop and route to the conservative human-review branch.

#### Step 2 — `scenario-step:scenario:hanse:460:service-battery-critical-voltage:0.1.0:2` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human)
- Action: Cross-check the reading against an independent second source before acting on it (cause: measurement-error; equipment role measurement-service-battery). No captured register document defines a cross-check procedure or a second installed voltage source — explicit unknown marker: the method and instrument for the independent reading are unsourced and left to the skipper.
- Entry criteria: Step 1 completed and recorded.
- Completion criteria: Second reading recorded, or recorded decision that no independent source is available.
- Expected observation: Agreement of the two readings (supports a genuine low-voltage state) or disagreement (supports measurement error).
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: Conflicting readings are never resolved by this scenario: route to the conservative human-review branch and treat the bank state as unconfirmed.

#### Step 3 — `scenario-step:scenario:hanse:460:service-battery-critical-voltage:0.1.0:3` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human)
- Action: Observe the present service-bank current at the shunt display and note which consumers are switched on at the main DC distribution (equipment roles measurement-service-battery and dc-main-distribution; switched consumer circuits per the series circuit diagram document:hanseyachts:h20b-7215-100-010:03 sheets 10 and 16-19 and the owner's manual document:hanseyachts:owners-manual-460-en:v11 chapter 2 section 1.5.1, printed pages 61-63).
- Entry criteria: Step 2 completed; bank state provisionally treated as genuine.
- Completion criteria: Discharge/charge current and active consumer set recorded.
- Expected observation: Either a discharge current consistent with the active consumer set (supports excessive-consumer-load or charge-path causes) or a charging current (weakens both).
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: A current reading inconsistent with the switch states (e.g. large discharge with all consumers off) is ambiguous evidence: stop and route to the conservative human-review branch.

#### Step 4 — `scenario-step:scenario:hanse:460:service-battery-critical-voltage:0.1.0:4` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human)
- Action: If on shore power: observe the shore charging path — shore supply present at the inlet and charger operating state (equipment roles shore-power-inlet and battery-charger; shore/charger arrangement per the series circuit diagram document:hanseyachts:h20b-7215-100-010:03 sheet 10; charger status indications per the family manual document:mastervolt:chargemaster-plus-manual-10000016594:03 — family-common values only, installed model unconfirmed as-built, issue #260).
- Entry criteria: Step 3 completed; vessel is, or is expected to be, on the shore charging path.
- Completion criteria: Shore-supply presence and charger state recorded (observation only; no reset or reconfiguration is instructed here).
- Expected observation: Charger delivering charge current (weakens the shore-path cause) or visibly not delivering (supports it).
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: Any charger fault indication or hazard sign (heat, smell, smoke) means: do not intervene, stop the sequence, route to the conservative human-review branch / shore service.

#### Step 5 — `scenario-step:scenario:hanse:460:service-battery-critical-voltage:0.1.0:5` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human)
- Action: If under way or shore power unavailable: decide whether to run the engine, and if running, observe whether the service bank receives charging current at the shunt display (equipment role alternator-charging; engine charge path per the series circuit diagram document:hanseyachts:h20b-7215-100-010:03 sheets 10, 20 and 21; the realized path depends on the fitted battery variant). Starting the engine is a navigation/safety decision of the skipper, not an instruction of this scenario.
- Entry criteria: Step 3 completed; skipper has decided engine operation is safe and appropriate.
- Completion criteria: Charging-current observation with engine running recorded, or recorded skipper decision not to run the engine.
- Expected observation: Charging current into the bank with engine running (weakens the alternator-path cause) or none (supports it).
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: No charging current with engine running is charge-path evidence, not an instruction to intervene: record and continue; any ambiguity routes to the conservative human-review branch.

#### Step 6 — `scenario-step:scenario:hanse:460:service-battery-critical-voltage:0.1.0:6` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human)
- Action: Visually inspect the state of the service-side protection devices: main battery switches and fuse positions (equipment role protection-dc-main; device inventory per the series circuit diagram document:hanseyachts:h20b-7215-100-010:03 sheet 10; locations and fuse overview per the owner's manual document:hanseyachts:owners-manual-460-en:v11, printed pages 57-59 and 64). Observation only: this scenario never instructs operating, resetting or bypassing a protection device.
- Entry criteria: Steps 4/5 (as applicable) completed without resolving the cause.
- Completion criteria: Switch and visible fuse states recorded; anomalies noted explicitly.
- Expected observation: All expected devices closed/intact (weakens the protection-open cause) or an open/tripped device found (supports it).
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: An open protection device is a finding for human judgment: the decision whether and how to restore it belongs to the skipper or qualified service, outside this scenario; if the reason for the open device is unknown, treat re-energizing as unsafe and route to the conservative human-review branch.

#### Step 7 — `scenario-step:scenario:hanse:460:service-battery-critical-voltage:0.1.0:7` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human), sole decision authority
- Action: Decide load prioritization (load shedding) while the bank state remains critical. This decision is reserved to the human skipper and must weigh navigation safety and bilge capability: the derived consumer set includes the navigation lights and the electric bilge pump (69 l/min per the owner's manual document:hanseyachts:owners-manual-460-en:v11 chapter 2 section 1.2.5, printed page 52; equipment roles dc-main-distribution, dc-consumer-bilge-pump, dc-consumer-navigation-lights, dc-consumer-refrigeration, dc-consumer-freshwater-pump).
- Entry criteria: Steps 1-3 completed; bank state treated as genuinely critical.
- Completion criteria: Skipper's load decision and its rationale recorded, including the effect on navigation-light and bilge-pump availability.
- Expected observation: Reduced discharge current after the human decision, observed at the shunt display.
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: If reducing load does not change the observed discharge current, the evidence is inconsistent: stop and route to the conservative human-review branch.

#### Step 8 — `scenario-step:scenario:hanse:460:service-battery-critical-voltage:0.1.0:8` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human), with shore support / qualified service consulted
- Action: Defer the battery-condition assessment (cause: battery-degradation; equipment role service-battery-bank) to the accountable human with the confirmed manufacturer documentation — explicit unknown marker: this step cannot be completed from the captured document set because the installed battery model is unconfirmed as-built and no manufacturer battery criteria are transcribed (issue #260).
- Entry criteria: Charge paths and protection state inspected (steps 4-6) without identifying a cause.
- Completion criteria: Recorded human disposition: degradation suspected/not suspected, and what as-built confirmation is still required.
- Expected observation: No model-backed observation is defined; any conclusion here is human judgment, explicitly marked as resting on unsourced data.
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: This step is itself the conservative branch for battery condition: unknown data never becomes an assumed-good state (OMSP-REFERENCE-SCENARIO-0001 section 4).

#### Step 9 — `scenario-step:scenario:hanse:460:service-battery-critical-voltage:0.1.0:9` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human)
- Action: Close the scenario: record the outcome class (expected / degraded-but-controlled / aborted / unacceptable / unknown per OMSP-REFERENCE-SCENARIO-0001 section 9), the evidence gathered at each step, and every value that remained unknown (equipment roles service-battery-bank and measurement-service-battery as the observed elements; recording rule defined by this scenario, no captured document prescribes a log format — explicit unknown marker).
- Entry criteria: Sequence ended by cause identification, by skipper decision, or by a stop/abort condition.
- Completion criteria: Outcome, evidence list and open unknowns recorded.
- Expected observation: A closed record whose every claim carries its source or an explicit unknown, consistent with the provenance rules of the model package.
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: If the closing record would contain a claim without source or unknown marking, the record is incomplete: route to the conservative human-review branch instead of closing.

### Decision point — continuation decision — service-battery-critical-voltage

First-class decision construct (ODS-300-R-07/R-08) derived from the scenario's modeled stop/abort conditions and mandatory conservative human-review branch:

- Available branches:
  - Continue the inspection sequence (no stop/abort condition met).
  - Stop/abort: Stop if the panel reading and an independent reading conflict and the conflict cannot be resolved by observation; do not proceed on unresolved conflict.
  - Stop/abort: Abort immediately on any sign of electrical hazard (heat, smell, smoke, discolored insulation) or suspected hazard to people; do not continue inspection.
  - Stop/abort: Stop if voltage continues to fall although an inspected charging path appears active — the evidence is inconsistent and the situation exceeds this reference scenario.
  - Stop/abort: Stop at any step whose required evidence is blocked by an as-built unknown (issue #260); never substitute a guessed value.
  - Conservative human review (mandatory default for unknown or conflicting evidence, below).
- Decision authority: Skipper (human). The skipper holds command authority for every decision in this scenario, including load shedding and any protection or charging state change. Software and monitoring equipment (measurement role, panel displays) may observe, record, warn and recommend only; no command authority is assigned to software (OMSP-REFERENCE-SCENARIO-0001 section 5).
- Required evidence: the entry/completion criteria and expected observations of the executed steps (rendered above); unknown markers remain unknown.
- Time sensitivity: `unknown` — not modeled by the source scenario (explicit unknown per ODS-300-R-09).
- Fallback behaviour (conservative human-review branch): Unknown or conflicting evidence at any step routes to the accountable human skipper for conservative review (consulting qualified service or shore support as the skipper decides); the scenario never resolves such a conflict automatically, and values blocked pending as-built confirmation (critical threshold, installed battery model, display variant and calibration state — issue #260) remain unknowns until closed through the source register, never through in-scenario assumption.

### Safety constraints — service-battery-critical-voltage

- Electrical hazard: the service bank and its links carry high currents (500 A shunt path, 150 mm2 battery links per the series circuit diagram); inspection is observation-only, and no step authorizes working on live conductors or battery terminals.
- Load-shedding decisions that affect navigation capability (navigation lights) or bilge capability (electric bilge pump, 69 l/min) are reserved to the human skipper in full navigation context; software and this scenario may only present the derived consumer set and observations.
- No instruction to bypass, defeat or force any protection device exists in this scenario, and none may be derived from it; protection state changes are human decisions outside this scenario's authority.
- Conservative stop: at any ambiguity, conflicting evidence or suspected hazard (heat, smell, smoke, anomalous display), the sequence stops and the situation routes to the accountable human; proceeding on unresolved conflict is prohibited.
- Advisory boundary: this scenario is reference material derived from a design-family model; it is not an approved procedure, carries no seaworthiness or navigation-safety claim, and approved vessel instructions and the skipper's judgment always prevail (OMSP-REFERENCE-SCENARIO-0001 section 14).

### Unacceptable outcomes and stop/abort conditions — service-battery-critical-voltage

- Unacceptable outcome: Loss of bilge-pumping or navigation-light capability caused by load shedding without a recorded human decision.
- Unacceptable outcome: Continued discharge until essential consumers become unavailable without a recorded human decision.
- Unacceptable outcome: Any protection device bypassed, defeated or re-energized without understanding why it opened.
- Unacceptable outcome: An unknown value (threshold, battery model, calibration state) silently treated as a known or safe value.
- Unacceptable outcome: Software or this scenario acting as command authority for any decision.
- Stop/abort condition: Stop if the panel reading and an independent reading conflict and the conflict cannot be resolved by observation; do not proceed on unresolved conflict.
- Stop/abort condition: Abort immediately on any sign of electrical hazard (heat, smell, smoke, discolored insulation) or suspected hazard to people; do not continue inspection.
- Stop/abort condition: Stop if voltage continues to fall although an inspected charging path appears active — the evidence is inconsistent and the situation exceeds this reference scenario.
- Stop/abort condition: Stop at any step whose required evidence is blocked by an as-built unknown (issue #260); never substitute a guessed value.

### Related equipment — service-battery-critical-voltage

- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:service-battery-bank`
- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:dc-main-distribution`
- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:dc-consumer-refrigeration`
- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:dc-consumer-navigation-lights`
- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:dc-consumer-bilge-pump`
- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:dc-consumer-freshwater-pump`
- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:battery-charger`
- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:shore-power-inlet`
- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:alternator-charging`
- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:protection-dc-main`
- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:measurement-service-battery`

### Source documents — service-battery-critical-voltage

- `document:hanseyachts:h20b-7215-100-010:03`
- `document:hanseyachts:owners-manual-460-en:v11`
- `document:mastervolt:chargemaster-plus-manual-10000016594:03`
- `document:hanseyachts:hanse-460-specification-pricelist-us:2021-11-12`

### Assumptions — service-battery-critical-voltage

- The standard reference configuration applies (AGM standard battery set); fitted options (XH1001, XH1005, XH2201) may change charge paths and are not assumed present.
- Affected-set derivation rule (graph-derived, not hand-listed): related_equipment and the connections cited in causes[] are the equipment reachable from service-battery-bank via connection instances downstream (supply direction) and upstream (charge paths), plus the protection role protecting a derived element and the measurement role measuring a derived element; reproducible command in README.md section 9.

### Declared unknowns — service-battery-critical-voltage

- Critical-low voltage threshold of the service bank (trigger threshold): no captured document states it; closure requires as-built battery-model confirmation (issue #260).
- Installed battery model, charger model and display variant are unconfirmed as-built (issue #260); all family-level citations are marked as such.
- Calibration state and measurement authority of the service-battery measurement role are unknown.
- Per-consumer expected current draw is largely unsourced; the step-3 load comparison is qualitative.

### Exclusions — service-battery-critical-voltage

- Inverter role and AC consumers: the standard reference configuration realizes no inverter connection instance (option XH2201; README section 4), so the graph derivation excludes the inverter; AC-side consumers are outside the golden-path slice (golden path section 5.2).
- Engine start battery and engine starting circuit (golden path section 5.2).
- Any repair, reset or reconfiguration procedure: this scenario is inspection/observation reference only.

## Scenario — Shore-power supply loss on the shore connection (reference inspection scenario)

- Scenario ID: `scenario:hanse:460:shore-power-loss:0.1.0`
- Class: `degraded`
- Accountable authority: Skipper (human). The skipper holds command authority for every decision in this scenario, including any reconnection, protection state change, load prioritization and the decision to use an alternative charging path. Software and monitoring equipment (charger status display, measurement role, panel displays) may observe, record, warn and recommend only; no command authority is assigned to software (OMSP-REFERENCE-SCENARIO-0001 section 5).
- Objective: Answer, from the modeled electrical slice with full provenance, the question "shore power is lost — what does that mean on this boat?": which systems and equipment roles are affected through the derived shore-power-inlet -> charger -> service-bank -> DC-consumer chain, which causes are plausible and what evidence each requires, and in which conservative order a human can inspect them. This is a reference inspection order for the design-family configuration, never an approved vessel procedure.

### Trigger — shore-power-loss

- Description: Observed loss of the 230 V shore supply while the vessel is on the shore connection: the battery charger stops delivering ("No output voltage and/or current — No AC input" per the family manual troubleshooting table; alarm "AC error — AC input (mains) out of range" and error-menu LED indication per the status display), and/or the service-battery measurement role (500 A shunt / SCP 220 H chain, series circuit diagram sheets 10 and 19) shows discharge while the shore charging path should be active. A single indication is not treated as a confirmed supply loss: the installed charger model and display variant are unconfirmed as-built (issue #260), so independent confirmation at the inlet and breaker box (inspection step 2) is required.
- Source: observed
- Timestamp handling: Recorded at observation time by the observing human or from the monitoring display log. This reference scenario defines the recording rule, not a real event.
- Confidence: medium
- Threshold: Charger AC-error condition "AC input (mains) out of range"; the family manual's troubleshooting table treats AC input voltage below 75 V AC as too low. No vessel-specific alarm threshold is captured. (authority: `sourced-manufacturer`, source: `source:manufacturer:owner-held:mastervolt-chargemaster-plus-manual-10000016594-03:2026-07-16`)

### Affected systems — shore-power-loss

- `system:vessel-design:hanse:460:electrical`

### Likely causes — shore-power-loss

**Cause: `charge-path-shore-failure`**

- Cause ID: `cause:hanse:460:service-battery-critical-voltage:charge-path-shore-failure`
- Description: Shore charging path not delivering: shore supply absent or disconnected, inlet protection open, or battery charger not producing DC output. Derived charge path: shore-power-inlet -> (shore-power-feed) -> battery-charger -> (charger-dc-output) -> service-battery-bank.
- Implicates:
  - `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:shore-power-inlet`
  - `connection:configuration:vessel-design:hanse:460:reference-0.1.0:shore-power-feed`
  - `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:battery-charger`
  - `connection:configuration:vessel-design:hanse:460:reference-0.1.0:charger-dc-output`
- Evidence requirement: Family-level shared taxonomy entry, minted by scenario:hanse:460:service-battery-critical-voltage:0.1.0 and reused here by identity (same cause id and description). In this scenario it is the condition under inspection; the scenario-specific causes below decompose it into path segments, and its evidence is the union of the segment observations (inspection steps 1-5).

**Cause: `shore-side-supply-failure`**

- Cause ID: `cause:hanse:460:shore-power-loss:shore-side-supply-failure`
- Description: Supply failure on the shore side of the connection: the marina pedestal or shore-side protection no longer delivers, so no supply reaches the vessel inlet although the vessel-side path is intact. The shore-side installation is outside the model boundary; aboard it is observable only as absence of supply at the inlet with intact vessel-side devices.
- Implicates:
  - `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:shore-power-inlet`
  - `connection:configuration:vessel-design:hanse:460:reference-0.1.0:shore-power-feed`
- Evidence requirement: Observation at the inlet and breaker box (step 2) showing intact vessel-side devices, plus shore-side observation (step 3). No captured register document describes the shore-side installation — explicit unknown marker: shore-pedestal evidence is unsourced and its assessment belongs to the human and the marina operator.

**Cause: `shore-cable-disconnected-or-damaged`**

- Cause ID: `cause:hanse:460:shore-power-loss:shore-cable-disconnected-or-damaged`
- Description: The shore-connecting cable is physically disconnected, unevenly plugged or damaged: the owner's manual requires the cap opening angle of the shore power cable to be at least 180 degrees to prevent tilting or uneven plugging, requires a compatible shore-connecting line, and warns that the cable and connectors must have no contact with the water.
- Implicates:
  - `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:shore-power-inlet`
  - `connection:configuration:vessel-design:hanse:460:reference-0.1.0:shore-power-feed`
- Evidence requirement: Visual observation of the cable seating, cap and connectors at both ends (step 3; owner's manual document:hanseyachts:owners-manual-460-en:v11 Chapter 2 section 1.5.2 "Shore connection", printed page 66, PDF page 76). Any re-plugging follows the owner's-manual order and is a skipper action outside this scenario's authority.

**Cause: `inlet-protection-open`**

- Cause ID: `cause:hanse:460:shore-power-loss:inlet-protection-open`
- Description: The shore-feed protection is open: the combined RCD/breaker "FI/LS 32A" (2F1) of the shore 1 feed in the breaker box has tripped or been switched off — including a legitimate GFCI trip, since the owner's manual states the shore power is protected with a GFCI device "switching off the system immediately at a malfunction".
- Implicates:
  - `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:shore-power-inlet`
  - `connection:configuration:vessel-design:hanse:460:reference-0.1.0:shore-power-feed`
- Evidence requirement: Visual position observation of the 2F1 FI/LS device in the breaker box ("technic room aft prt", series circuit diagram document:hanseyachts:h20b-7215-100-010:03 sheet 2; GFCI statement per owner's manual document:hanseyachts:owners-manual-460-en:v11 Chapter 2 section 1.5.2, printed page 66). Observation only: an open protection device is a finding for human judgment, and re-energizing after an unexplained trip is treated as unsafe.

**Cause: `isolation-device-fault`**

- Cause ID: `cause:hanse:460:shore-power-loss:isolation-device-fault`
- Description: The galvanic-isolation device in the shore feed interrupts or degrades the supply: the series drawing places a 32 A galvanic isolator in the shore 1 feed and the owner's manual device list names a galvanic isolator; the owner-held delivery set holds manuals for both a Victron 7000 W isolation transformer and a WhisperPower WP-GI galvanic isolation transformer, and which isolation device (if either transformer) is installed is not confirmed as-built (issue #260).
- Implicates:
  - `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:shore-power-inlet`
  - `connection:configuration:vessel-design:hanse:460:reference-0.1.0:shore-power-feed`
- Evidence requirement: Indication observation per the applicable vendor manual (document:victron:isolation-transformer-7000w-manual:03 or document:whisperpower:wp-gi-3600-manual:undated) — blocked pending as-built confirmation of the installed unit (issue #260); until confirmed, assessment routes to the conservative human-review branch. Bypassing or defeating galvanic isolation is prohibited and no evidence step may require it.

**Cause: `charger-ac-stage-failure`**

- Cause ID: `cause:hanse:460:shore-power-loss:charger-ac-stage-failure`
- Description: The battery charger itself does not accept or process the available AC supply: device fault, charger switched off, or AC input out of the accepted range at the charger, while shore supply is present upstream.
- Implicates:
  - `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:battery-charger`
  - `connection:configuration:vessel-design:hanse:460:reference-0.1.0:shore-power-feed`
- Evidence requirement: Charger status observation (step 1): status-display LED states and error menu (Battery 2 error LED = "AC error — check AC voltage/frequency") per the family manual document:mastervolt:chargemaster-plus-manual-10000016594:03, section 5.3 Status display (PDF pages 22-23) and chapter 6 troubleshooting (PDF page 26); auto-resume observation after supply restoration (step 5, section 5.2, PDF page 22). Family-common indications only; the installed charger model is unconfirmed as-built (issue #260). The charger enclosure is never opened; any repair belongs to qualified service.

### Inspection sequence — shore-power-loss

Reference inspection order, not an approved vessel procedure. Steps follow ODS-300 procedure language; every step field the model does not establish is rendered as an explicit unknown.

#### Step 1 — `scenario-step:scenario:hanse:460:shore-power-loss:0.1.0:1` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human), responsible; charger status display and monitoring display, informed sources only
- Action: Observe and record the charger state and the service-bank state: charger status-display LED states and any error-menu indication (equipment role battery-charger; family manual document:mastervolt:chargemaster-plus-manual-10000016594:03, section 5.3 Status display, PDF pages 22-23) and the charge/discharge current and voltage at the shunt display (equipment role measurement-service-battery, series circuit diagram document:hanseyachts:h20b-7215-100-010:03 sheets 10 and 19). Record which instruments produced the values; the installed charger model and display variant are explicit unknowns (issue #260).
- Entry criteria: Trigger condition observed or reported; preconditions reviewed by the skipper.
- Completion criteria: Charger indication, shunt reading, time and measurement sources recorded.
- Expected observation: Charger not delivering (off, stand-by or AC-error indication) and/or discharge current at the shunt while on the shore connection; the indications are the evidence under test, not yet a confirmed supply loss.
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: If indications conflict (e.g. charger shows charging while the shunt shows discharge), stop and route to the conservative human-review branch; do not proceed on unresolved conflict.

#### Step 2 — `scenario-step:scenario:hanse:460:shore-power-loss:0.1.0:2` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human)
- Action: Confirm the loss at the vessel-side supply path by observation only: state of the shore-feed protection "FI/LS 32A" (2F1) in the breaker box ("technic room aft prt") and the inlet connection (equipment role shore-power-inlet; series circuit diagram document:hanseyachts:h20b-7215-100-010:03 sheet 2). No switchboard is opened and no live AC work is performed: the owner's manual document:hanseyachts:owners-manual-460-en:v11 (Chapter 1 section 1.2.5, printed page 6, PDF page 16) prohibits work on a live alternating-current system and warns of electric shock at switchboards.
- Entry criteria: Step 1 completed and recorded.
- Completion criteria: 2F1 position and inlet connection state recorded; anomalies noted explicitly.
- Expected observation: Either an open/tripped 2F1 (supports inlet-protection-open) or an intact vessel-side path (shifts evidence toward the shore side, the cable or the charger).
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: An open protection device is a finding for human judgment: re-energizing after an unexplained trip is treated as unsafe; route to the conservative human-review branch / qualified service.

#### Step 3 — `scenario-step:scenario:hanse:460:shore-power-loss:0.1.0:3` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human)
- Action: Observe the shore-connecting cable and the shore side: cable seating and cap at the vessel inlet, connector condition at both ends, water contact, and the shore pedestal state (equipment role shore-power-inlet; owner's manual document:hanseyachts:owners-manual-460-en:v11 Chapter 2 section 1.5.2 "Shore connection", printed page 66, PDF page 76). The shore-side installation is outside the model boundary — explicit unknown marker: no captured document describes it. Any unplugging or re-plugging is a skipper action following the owner's-manual order (switch the shore connection switch off first; connect aboard first, separate ashore first), not an instruction of this scenario.
- Entry criteria: Step 2 completed; vessel-side protection state recorded.
- Completion criteria: Cable, connector and shore-side observations recorded, including any decision to involve the marina operator.
- Expected observation: Either a visible cable/connector fault or shore-side outage (supports the respective cause) or an intact connection (shifts evidence toward the isolation device or the charger).
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: Wet, damaged or heat-marked connectors mean: do not reconnect; stop and route to the conservative human-review branch / qualified service.

#### Step 4 — `scenario-step:scenario:hanse:460:shore-power-loss:0.1.0:4` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human)
- Action: Observe the galvanic-isolation device in the shore feed for available indications (equipment role shore-power-inlet; isolator per series circuit diagram document:hanseyachts:h20b-7215-100-010:03 sheet 2 and owner's manual device list item 34, printed page 60, PDF page 70). Which isolation device is installed is unconfirmed as-built (issue #260) — explicit unknown marker: the applicable vendor indication set (document:victron:isolation-transformer-7000w-manual:03 or document:whisperpower:wp-gi-3600-manual:undated) cannot be selected until the installed unit is confirmed. Observation only; galvanic isolation is never bypassed or defeated.
- Entry criteria: Steps 2-3 completed without identifying the cause.
- Completion criteria: Available isolation-device observations recorded, or recorded statement that no indication is accessible/selectable.
- Expected observation: No model-backed observation is defined while the installed unit is unconfirmed; any conclusion here is human judgment resting on explicitly unsourced device identity.
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: This step routes to the conservative human-review branch whenever the device identity or indication meaning is unknown; unknown data never becomes an assumed-good state (OMSP-REFERENCE-SCENARIO-0001 section 4).

#### Step 5 — `scenario-step:scenario:hanse:460:shore-power-loss:0.1.0:5` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human)
- Action: If the supply is restored (shore side or protection closed by a justified human decision): observe whether the charger resumes charging — the family manual states the charger automatically resumes operation after a temporary AC disconnection (equipment roles battery-charger and measurement-service-battery; family manual document:mastervolt:chargemaster-plus-manual-10000016594:03, section 5.2, PDF page 22) — and confirm charging current at the shunt display.
- Entry criteria: Supply restoration observed or decided by the skipper; steps 1-4 recorded.
- Completion criteria: Post-restoration charger state and shunt charging current recorded, or recorded decision that restoration is not possible.
- Expected observation: Charger returns to a charging stage (bulk/absorption/float LED states) and the shunt shows charging current (closes the scenario as resolved) or it does not (supports charger-ac-stage-failure; qualified service).
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: Any charger fault indication or hazard sign (heat, smell, smoke) means: do not intervene, stop the sequence, route to the conservative human-review branch / qualified service.

#### Step 6 — `scenario-step:scenario:hanse:460:shore-power-loss:0.1.0:6` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human), sole decision authority
- Action: While shore power remains lost, assess the consequence on the derived downstream chain: the service bank is the sole source for the DC consumers (equipment roles service-battery-bank, dc-main-distribution and the derived consumer set including the navigation lights and the electric bilge pump, 69 l/min per the owner's manual document:hanseyachts:owners-manual-460-en:v11 Chapter 2 section 1.2.5, printed page 52). Decide load prioritization and whether to use an alternative charging path (engine-driven charging per scenario:hanse:460:service-battery-critical-voltage:0.1.0 step 5); both are navigation/safety decisions reserved to the skipper, not instructions of this scenario.
- Entry criteria: Steps 1-4 completed; supply restoration not achieved or not yet decided.
- Completion criteria: Skipper's load and alternative-charging decisions and their rationale recorded, including the effect on navigation-light and bilge-pump availability.
- Expected observation: Discharge current at the shunt display consistent with the decided consumer set.
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: If the observed discharge is inconsistent with the decided consumer set, the evidence is inconsistent: stop and route to the conservative human-review branch.

#### Step 7 — `scenario-step:scenario:hanse:460:shore-power-loss:0.1.0:7` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human)
- Action: Monitor the service-bank voltage while the loss persists (equipment roles service-battery-bank and measurement-service-battery). If the voltage approaches a critical level, continue under scenario:hanse:460:service-battery-critical-voltage:0.1.0 — whose critical-low threshold is itself an explicit unknown pending as-built battery-model confirmation (issue #260).
- Entry criteria: Step 6 completed; shore supply still lost.
- Completion criteria: Monitoring rule recorded (which display, which interval — the interval is a skipper decision; no captured document prescribes one — explicit unknown marker) and any handover to the critical-voltage scenario recorded.
- Expected observation: Bank voltage stable or declining; a declining trend routes toward the critical-voltage scenario.
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: Trigger conditions of the critical-voltage scenario observed: hand over to that scenario and record the handover.

#### Step 8 — `scenario-step:scenario:hanse:460:shore-power-loss:0.1.0:8` **[HUMAN CONFIRMATION REQUIRED]**

- Responsible actor: Skipper (human)
- Action: Close the scenario: record the outcome class (expected / degraded-but-controlled / aborted / unacceptable / unknown per OMSP-REFERENCE-SCENARIO-0001 section 9), the evidence gathered at each step, and every value that remained unknown (equipment roles shore-power-inlet and battery-charger as the primary observed elements; recording rule defined by this scenario, no captured document prescribes a log format — explicit unknown marker).
- Entry criteria: Sequence ended by cause identification, by supply restoration, by handover to the critical-voltage scenario, by skipper decision, or by a stop/abort condition.
- Completion criteria: Outcome, evidence list and open unknowns recorded.
- Expected observation: A closed record whose every claim carries its source or an explicit unknown, consistent with the provenance rules of the model package.
- Hazards and safeguards: no step-specific hazard field is modeled (explicit statement per ODS-300-R-06); the scenario-level safety constraints above apply to every step
- Escalation: If the closing record would contain a claim without source or unknown marking, the record is incomplete: route to the conservative human-review branch instead of closing.

### Decision point — continuation decision — shore-power-loss

First-class decision construct (ODS-300-R-07/R-08) derived from the scenario's modeled stop/abort conditions and mandatory conservative human-review branch:

- Available branches:
  - Continue the inspection sequence (no stop/abort condition met).
  - Stop/abort: Abort immediately on any sign of electrical hazard (heat, smell, smoke, discolored insulation, wet connectors) at the inlet, breaker box, isolation device or charger; do not continue inspection and do not reconnect.
  - Stop/abort: Stop if the shore-feed protection (2F1) has tripped and the reason is unknown; re-energizing is treated as unsafe and the situation routes to qualified service.
  - Stop/abort: Stop if charger and shunt indications conflict and the conflict cannot be resolved by observation; do not proceed on unresolved conflict.
  - Stop/abort: Stop at any step whose required evidence is blocked by an as-built unknown (installed charger model, isolation-device identity — issue #260); never substitute a guessed value.
  - Stop/abort: Hand over to scenario:hanse:460:service-battery-critical-voltage:0.1.0 when its trigger condition is observed; the handover is recorded.
  - Conservative human review (mandatory default for unknown or conflicting evidence, below).
- Decision authority: Skipper (human). The skipper holds command authority for every decision in this scenario, including any reconnection, protection state change, load prioritization and the decision to use an alternative charging path. Software and monitoring equipment (charger status display, measurement role, panel displays) may observe, record, warn and recommend only; no command authority is assigned to software (OMSP-REFERENCE-SCENARIO-0001 section 5).
- Required evidence: the entry/completion criteria and expected observations of the executed steps (rendered above); unknown markers remain unknown.
- Time sensitivity: `unknown` — not modeled by the source scenario (explicit unknown per ODS-300-R-09).
- Fallback behaviour (conservative human-review branch): Unknown or conflicting evidence at any step routes to the accountable human skipper for conservative review (consulting the marina operator, qualified service or shore support as the skipper decides); the scenario never resolves such a conflict automatically, and values blocked pending as-built confirmation (installed charger model, isolation-device identity, display variant — issue #260) remain unknowns until closed through the source register, never through in-scenario assumption.

### Safety constraints — shore-power-loss

- 230 V AC hazard: no step of this scenario authorizes work on a live alternating-current system, opening switchboards or the charger enclosure, or contact with shore-cable conductors; the owner's manual warns of fire, explosion and electric-shock risk (Chapter 1 section 1.2.5, printed page 6) and inspection here is observation-only.
- Swimming hazard: the owner's manual warns that swimming near a boat operating on an AC electrical system can lead to severe shock and death; no swimming while the AC system is in use.
- Shore-cable handling follows the owner's-manual order only (switch the shore connection switch off first before plugging or unplugging; connect aboard first; separate ashore first; no water contact of cable and connectors); this scenario never instructs the handling itself.
- No instruction to bypass, defeat or force any protection or galvanic-isolation device (FI/LS 2F1, galvanic isolator, isolation transformer) exists in this scenario, and none may be derived from it; protection state changes are human decisions outside this scenario's authority.
- Load and alternative-charging decisions that affect navigation capability (navigation lights) or bilge capability (electric bilge pump, 69 l/min) are reserved to the human skipper in full navigation context.
- Conservative stop: at any ambiguity, conflicting evidence or suspected hazard (heat, smell, smoke, wet or damaged connectors, anomalous display), the sequence stops and the situation routes to the accountable human; proceeding on unresolved conflict is prohibited.
- Advisory boundary: this scenario is reference material derived from a design-family model; it is not an approved procedure, carries no seaworthiness or navigation-safety claim, and approved vessel instructions and the skipper's judgment always prevail (OMSP-REFERENCE-SCENARIO-0001 section 14).

### Unacceptable outcomes and stop/abort conditions — shore-power-loss

- Unacceptable outcome: Any work on a live AC system, any opened switchboard or charger enclosure, or any shore-cable handling outside the owner's-manual order.
- Unacceptable outcome: Any protection or galvanic-isolation device bypassed, defeated or re-energized without understanding why it opened.
- Unacceptable outcome: Swimming near the vessel while the AC system is energized.
- Unacceptable outcome: Continued discharge until essential consumers (navigation lights, bilge pump) become unavailable without a recorded human decision.
- Unacceptable outcome: An unknown value (installed charger model, isolation-device identity, display variant) silently treated as a known or safe value.
- Unacceptable outcome: Software or this scenario acting as command authority for any decision.
- Stop/abort condition: Abort immediately on any sign of electrical hazard (heat, smell, smoke, discolored insulation, wet connectors) at the inlet, breaker box, isolation device or charger; do not continue inspection and do not reconnect.
- Stop/abort condition: Stop if the shore-feed protection (2F1) has tripped and the reason is unknown; re-energizing is treated as unsafe and the situation routes to qualified service.
- Stop/abort condition: Stop if charger and shunt indications conflict and the conflict cannot be resolved by observation; do not proceed on unresolved conflict.
- Stop/abort condition: Stop at any step whose required evidence is blocked by an as-built unknown (installed charger model, isolation-device identity — issue #260); never substitute a guessed value.
- Stop/abort condition: Hand over to scenario:hanse:460:service-battery-critical-voltage:0.1.0 when its trigger condition is observed; the handover is recorded.

### Related equipment — shore-power-loss

- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:shore-power-inlet`
- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:battery-charger`
- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:service-battery-bank`
- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:dc-main-distribution`
- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:dc-consumer-refrigeration`
- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:dc-consumer-navigation-lights`
- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:dc-consumer-bilge-pump`
- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:dc-consumer-freshwater-pump`
- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:protection-dc-main`
- `equipment:configuration:vessel-design:hanse:460:reference-0.1.0:measurement-service-battery`

### Source documents — shore-power-loss

- `document:hanseyachts:h20b-7215-100-010:03`
- `document:hanseyachts:owners-manual-460-en:v11`
- `document:mastervolt:chargemaster-plus-manual-10000016594:03`
- `document:victron:isolation-transformer-7000w-manual:03`
- `document:whisperpower:wp-gi-3600-manual:undated`

### Assumptions — shore-power-loss

- The standard reference configuration applies: the shore 1 feed is the standard drawing path; shore 2 and AC-generator paths are provisioned options (series circuit diagram sheet 2) and are not assumed present.
- Affected-set derivation rule (graph-derived, not hand-listed): related_equipment and the connections cited in causes[] are the equipment reachable from shore-power-inlet via connection instances in supply direction, plus the protection role protecting a derived element and the measurement role measuring a derived element; reproducible command in README.md section 9 (seed shore-power-inlet: 10 equipment, 7 connections).
- Shared cause taxonomy: the family-level entry cause:hanse:460:service-battery-critical-voltage:charge-path-shore-failure is reused by identity from the WP-0085 scenario (identical id, description and implicates; scenario-local evidence_requirement); the scenario-specific causes refine it without re-describing it (README.md section 9, shared-taxonomy note).

### Declared unknowns — shore-power-loss

- Installed charger model within the documented family, installed display variant and the installed galvanic-isolation device identity (galvanic isolator alone vs. Victron or WhisperPower isolation transformer) are unconfirmed as-built (issue #260); all family-level citations are marked as such.
- The shore-side installation (pedestal, shore-side protection, connecting-power limitation) is outside the model boundary and described by no captured document.
- Shore-connector standard and inlet position on deck are not stated by any captured source (equipment-shore-power-inlet unknowns).
- No captured document prescribes a monitoring interval or log format for the loss condition; the recording rule is defined by this scenario.

### Exclusions — shore-power-loss

- Shore 2 and AC-generator option paths (provisioned option paths of the series drawing, not realized in the standard reference configuration) and all shore-side infrastructure beyond the inlet.
- Inverter role and AC consumers: the standard reference configuration realizes no inverter connection instance (option XH2201; README section 4), so the graph derivation excludes the inverter; AC-side consumers are outside the golden-path slice (golden path section 5.2).
- Alternator role and engine charging path: mechanically excluded by the seed derivation (unaffected by a shore-supply loss); engine-driven charging enters only as a skipper decision in step 6, handled by the critical-voltage scenario.
- Any repair, reset or reconfiguration procedure: this scenario is inspection/observation reference only.

## Evidence appendix

Authority class and source for every rendered claim (ODS-100-R-06). Source IDs and `document:` identities resolve in the source register `reference/HANSE_460_SOURCE_REGISTER.md`.

### Sourced claims

| Model element | Field | Authority class | Source | Confidence |
| --- | --- | --- | --- | --- |
| `connection-alternator-charge-feed.yaml` | `conductor-specification` | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` | high |
| `connection-battery-main-feed.yaml` | `conductor-specification` | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` | high |
| `connection-charger-dc-output.yaml` | `conductor-specification` | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` | high |
| `connection-dc-feed-bilge-pump.yaml` | `conductor-specification` | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` | high |
| `connection-dc-feed-freshwater-pump.yaml` | `conductor-specification` | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` | high |
| `connection-dc-feed-navigation-lights.yaml` | `conductor-specification` | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` | high |
| `connection-dc-feed-refrigeration.yaml` | `conductor-specification` | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` | high |
| `connection-shore-power-feed.yaml` | `conductor-specification` | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` | high |
| `equipment-alternator-charging.yaml` | `quantity` | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` | medium |
| `equipment-alternator-charging.yaml` | `charge-path-topology` | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` | medium |
| `equipment-alternator-charging.yaml` | `rated-output-current` | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` | high |
| `equipment-battery-charger.yaml` | `charge-profile` | `sourced-manufacturer` | `source:manufacturer:owner-held:mastervolt-chargemaster-plus-manual-10000016594-03:2026-07-16` | high |
| `equipment-battery-charger.yaml` | `input-voltage-range` | `sourced-manufacturer` | `source:manufacturer:owner-held:mastervolt-chargemaster-plus-manual-10000016594-03:2026-07-16` | high |
| `equipment-battery-charger.yaml` | `rated-charge-current` | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` | medium |
| `equipment-battery-charger.yaml` | `standard-and-option-charger-ratings` | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` | high |
| `equipment-dc-consumer-bilge-pump.yaml` | `quantity` | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` | medium |
| `equipment-dc-consumer-bilge-pump.yaml` | `control-arrangement` | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` | high |
| `equipment-dc-consumer-bilge-pump.yaml` | `drive` | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` | medium |
| `equipment-dc-consumer-bilge-pump.yaml` | `rated-flow` | `sourced-manufacturer` | `source:manufacturer:owner-held:owners-manual-460-en-v11:2026-07-16` | high |
| `equipment-dc-consumer-freshwater-pump.yaml` | `quantity` | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` | medium |
| `equipment-dc-consumer-freshwater-pump.yaml` | `drive` | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` | medium |
| `equipment-dc-consumer-navigation-lights.yaml` | `circuit-inventory` | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` | high |
| `equipment-dc-consumer-navigation-lights.yaml` | `lamp-technology` | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` | medium |
| `equipment-dc-consumer-refrigeration.yaml` | `quantity` | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` | medium |
| `equipment-dc-consumer-refrigeration.yaml` | `gross-volume` | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` | medium |
| `equipment-dc-consumer-refrigeration.yaml` | `supply-voltage` | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` | medium |
| `equipment-dc-main-distribution.yaml` | `bus-topology` | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` | medium |
| `equipment-dc-main-distribution.yaml` | `dc-panel-unit-identity` | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` | high |
| `equipment-dc-main-distribution.yaml` | `main-panels-fitted` | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` | medium |
| `equipment-inverter.yaml` | `option-xh2201-rating` | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` | medium |
| `equipment-inverter.yaml` | `standard-fitment` | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` | medium |
| `equipment-measurement-service-battery.yaml` | `instrument-type` | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` | high |
| `equipment-protection-dc-main.yaml` | `device-inventory` | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` | high |
| `equipment-protection-dc-main.yaml` | `ratings` | `sourced-manufacturer` | `source:manufacturer:owner-held:owners-manual-460-en-v11:2026-07-16` | high |
| `equipment-service-battery-bank.yaml` | `bank-topology` | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` | high |
| `equipment-service-battery-bank.yaml` | `chemistry` | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` | medium |
| `equipment-service-battery-bank.yaml` | `service-bank-capacity` | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` | high |
| `equipment-service-battery-bank.yaml` | `vessel-battery-set-composition` | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` | medium |
| `equipment-shore-power-inlet.yaml` | `inlet-protection-rating` | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` | high |
| `equipment-shore-power-inlet.yaml` | `nominal-supply-voltage` | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` | medium |
| `equipment-shore-power-inlet.yaml` | `provisioned-circuits` | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` | medium |
| `scenario-shore-power-loss.yaml` | `trigger.threshold` | `sourced-manufacturer` | `source:manufacturer:owner-held:mastervolt-chargemaster-plus-manual-10000016594-03:2026-07-16` | high |
| `system-electrical.yaml` | `nominal-ac-voltage` | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` | medium |
| `system-electrical.yaml` | `nominal-dc-voltage` | `sourced-secondary` | `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15` | medium |
| `system-electrical.yaml` | `system-architecture` | `sourced-manufacturer` | `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16` | medium |

### Unknowns (listed, not hidden)

The model publishes **67** explicit `status: unknown` occurrences. Every one is listed below (ODS-100-R-07); an unknown is an accepted document state, not a rendering failure.

| Model file | Field path |
| --- | --- |
| `equipment-alternator-charging.yaml` | `attributes.regulation-type` |
| `equipment-alternator-charging.yaml` | `manufacturer` |
| `equipment-alternator-charging.yaml` | `model` |
| `equipment-alternator-charging.yaml` | `serial_number` |
| `equipment-battery-charger.yaml` | `quantity` |
| `equipment-battery-charger.yaml` | `manufacturer` |
| `equipment-battery-charger.yaml` | `model` |
| `equipment-battery-charger.yaml` | `serial_number` |
| `equipment-dc-consumer-bilge-pump.yaml` | `attributes.supply-voltage` |
| `equipment-dc-consumer-bilge-pump.yaml` | `manufacturer` |
| `equipment-dc-consumer-bilge-pump.yaml` | `model` |
| `equipment-dc-consumer-bilge-pump.yaml` | `serial_number` |
| `equipment-dc-consumer-freshwater-pump.yaml` | `attributes.rated-flow` |
| `equipment-dc-consumer-freshwater-pump.yaml` | `attributes.supply-voltage` |
| `equipment-dc-consumer-freshwater-pump.yaml` | `installation_location` |
| `equipment-dc-consumer-freshwater-pump.yaml` | `manufacturer` |
| `equipment-dc-consumer-freshwater-pump.yaml` | `model` |
| `equipment-dc-consumer-freshwater-pump.yaml` | `serial_number` |
| `equipment-dc-consumer-navigation-lights.yaml` | `quantity` |
| `equipment-dc-consumer-navigation-lights.yaml` | `attributes.supply-voltage` |
| `equipment-dc-consumer-navigation-lights.yaml` | `attributes.power-draw` |
| `equipment-dc-consumer-navigation-lights.yaml` | `installation_location` |
| `equipment-dc-consumer-navigation-lights.yaml` | `manufacturer` |
| `equipment-dc-consumer-navigation-lights.yaml` | `model` |
| `equipment-dc-consumer-navigation-lights.yaml` | `serial_number` |
| `equipment-dc-consumer-refrigeration.yaml` | `attributes.power-draw` |
| `equipment-dc-consumer-refrigeration.yaml` | `manufacturer` |
| `equipment-dc-consumer-refrigeration.yaml` | `model` |
| `equipment-dc-consumer-refrigeration.yaml` | `serial_number` |
| `equipment-dc-main-distribution.yaml` | `quantity` |
| `equipment-dc-main-distribution.yaml` | `manufacturer` |
| `equipment-dc-main-distribution.yaml` | `model` |
| `equipment-dc-main-distribution.yaml` | `serial_number` |
| `equipment-inverter.yaml` | `quantity` |
| `equipment-inverter.yaml` | `attributes.transfer-behavior` |
| `equipment-inverter.yaml` | `installation_location` |
| `equipment-inverter.yaml` | `manufacturer` |
| `equipment-inverter.yaml` | `model` |
| `equipment-inverter.yaml` | `serial_number` |
| `equipment-measurement-service-battery.yaml` | `quantity` |
| `equipment-measurement-service-battery.yaml` | `attributes.display-location` |
| `equipment-measurement-service-battery.yaml` | `attributes.calibration-state` |
| `equipment-measurement-service-battery.yaml` | `installation_location` |
| `equipment-measurement-service-battery.yaml` | `manufacturer` |
| `equipment-measurement-service-battery.yaml` | `model` |
| `equipment-measurement-service-battery.yaml` | `serial_number` |
| `equipment-protection-dc-main.yaml` | `quantity` |
| `equipment-protection-dc-main.yaml` | `manufacturer` |
| `equipment-protection-dc-main.yaml` | `model` |
| `equipment-protection-dc-main.yaml` | `serial_number` |
| `equipment-service-battery-bank.yaml` | `quantity` |
| `equipment-service-battery-bank.yaml` | `attributes.nominal-voltage` |
| `equipment-service-battery-bank.yaml` | `attributes.critical-voltage-threshold` |
| `equipment-service-battery-bank.yaml` | `manufacturer` |
| `equipment-service-battery-bank.yaml` | `model` |
| `equipment-service-battery-bank.yaml` | `serial_number` |
| `equipment-shore-power-inlet.yaml` | `quantity` |
| `equipment-shore-power-inlet.yaml` | `attributes.connector-standard` |
| `equipment-shore-power-inlet.yaml` | `installation_location` |
| `equipment-shore-power-inlet.yaml` | `manufacturer` |
| `equipment-shore-power-inlet.yaml` | `model` |
| `equipment-shore-power-inlet.yaml` | `serial_number` |
| `interface-alternator-charge-feed.yaml` | `media` |
| `interface-charger-dc-output.yaml` | `nominal_limits.max-charge-current` |
| `interface-inverter-dc-feed.yaml` | `nominal_limits.max-continuous-load` |
| `scenario-maintenance-due.yaml` | `trigger.threshold` |
| `scenario-service-battery-critical-voltage.yaml` | `trigger.threshold` |
