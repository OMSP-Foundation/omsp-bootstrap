---
Artifact-ID: OMSP-REFERENCE-HANSE460-ELECTRICAL-0001
Title: Hanse 460 Electrical-Slice Reference Model
Version: 0.2.0
Status: Draft
Owner: toss-cengiz
Baseline: Sprint-9
Classification: Public
Related-Issue: WP-0093 / #258 (value transcription; model created by WP-0082 / #203)
Depends-On:
  - OMSP-SCHEMA-MARITIME-0001
  - OMSP-REFERENCE-SOURCE-0001
Traceability:
  - ISSUE-203
  - ISSUE-205
  - ISSUE-258
  - EPIC-172
  - OMSP-PLANNING-GOLDEN-PATH-0001
  - OMSP-PLANNING-REBASELINE-0001
  - OMSP-REFERENCE-CONFIG-0001
  - OMSP-REFERENCE-EQUIPMENT-0001
---

# Hanse 460 Electrical-Slice Reference Model

## 1. Purpose and scope

This package is the WP-0082 electrical-slice YAML model of the Hanse 460
reference configuration — the first provenance-carrying structured model
of the reference vessel. It instantiates **every** golden-path §5.1 role
(`planning/WP-0074-GOLDEN-PATH-DEFINITION.md`), with typed interfaces,
connections, protection and measurement roles, under the identity
skeleton of `OMSP-REFERENCE-CONFIG-0001`:

- Configuration: `configuration:vessel-design:hanse:460:reference-0.1.0`
- System: `system:vessel-design:hanse:460:electrical`
- Equipment identity: `equipment:<configuration-id>:<local-id>`
  (`OMSP-REFERENCE-EQUIPMENT-0001` §3)

The model boundary is exactly golden path §5.1; the §5.2 exclusion list
applies unchanged and is not repeated here (single-source rule). No item
outside §5.1 was added; register-listed factory options outside the
slice are deliberately **not** modeled. Interface instances use only the
families permitted by golden path §5.1 (this slice: `electrical-power`).

## 2. Provenance and evidence base

Every value in this model is either sourced or an explicit
`{status: unknown}` marker (`OMSP-PLANNING-GOLDEN-PATH-0001` §4.3, made
mechanical by `OMSP-SCHEMA-MARITIME-0001`). All sourced values resolve
to register entries of `reference/HANSE_460_SOURCE_REGISTER.md`
**v0.3.0**:

- `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15`
  (class `sourced-secondary`, confidence `medium`) — the WP-0082
  baseline evidence; its values are retained unchanged;
- `source:manufacturer:owner-held:h20b-7215-100-010-03:2026-07-16`
  (series circuit diagram H20B-7215-100-010 rev. 03, 54 sheets),
- `source:manufacturer:owner-held:owners-manual-460-en-v11:2026-07-16`
  (Owner's Manual EN V11, May 2024), and
- `source:manufacturer:owner-held:mastervolt-chargemaster-plus-manual-10000016594-03:2026-07-16`
  (ChargeMaster Plus family manual; family-common values only) —
  the WP-0093 / #258 value transcription at class
  `sourced-manufacturer`, per the register §4.5 closure paths.

Document references resolve through register §7; no inaccessible
source (register §4.3) is cited. Every WP-0093 provenance block names
its `document:` identity and extraction location (sheet or page) in the
`applicability` field. No electrical value was entered from memory;
everything the captured documents do not support — including every
group blocked by the as-built confirmation preconditions of issue #258
(service-battery model/cells, MultiPlus inverter values, isolation
transformer, hull identity, Simarine Pico variant/shunt configuration,
Aqua Signal installed series/positions; follow-up issue #260) — remains
an explicit unknown. No authority-class promotion was performed
(`verified-*` is absent from the package).

## 3. Role-to-file mapping (golden path §5.1 — 100% coverage)

| §5.1 role | Local ID in this model | File |
| --- | --- | --- |
| `shore-power-inlet` | `shore-power-inlet` | `equipment-shore-power-inlet.yaml` |
| `service-battery-bank` | `service-battery-bank` | `equipment-service-battery-bank.yaml` |
| `battery-charger` | `battery-charger` | `equipment-battery-charger.yaml` |
| `alternator-charging` | `alternator-charging` | `equipment-alternator-charging.yaml` |
| `inverter` | `inverter` | `equipment-inverter.yaml` |
| `dc-main-distribution` | `dc-main-distribution` | `equipment-dc-main-distribution.yaml` |
| `dc-consumer-*` | `dc-consumer-refrigeration` | `equipment-dc-consumer-refrigeration.yaml` |
| `dc-consumer-*` | `dc-consumer-navigation-lights` | `equipment-dc-consumer-navigation-lights.yaml` |
| `dc-consumer-*` | `dc-consumer-bilge-pump` | `equipment-dc-consumer-bilge-pump.yaml` |
| `dc-consumer-*` | `dc-consumer-freshwater-pump` | `equipment-dc-consumer-freshwater-pump.yaml` |
| `protection-*` | `protection-dc-main` | `equipment-protection-dc-main.yaml` |
| `measurement-*` | `measurement-service-battery` | `equipment-measurement-service-battery.yaml` |

**Consumer set (fixed with sources).** Golden path §5.1 left the
`dc-consumer-*` set as a candidate list to be "fixed at implementation
with sources". The captured register v0.2.0 claims (§3.3) support
exactly four standard DC consumers: the 12 V galley fridge (approx.
135 l), LED navigation lights, the electric bilge pump and the electric
freshwater pump. The candidate items "navigation instruments" and
"cabin lighting" are **not** in the set: the register supports
navigation instruments only as optional vendor equipment (option
package, as-built unknown) and contains no cabin-lighting claim.

**Protection and measurement roles.** Since WP-0093, both roles carry
transcribed series data: the protection role records the sheet-10
device inventory and the fuse-rating list corroborated by the owner's
manual "Overview fuses" page, and the measurement role records the
500 A shunt / SCP 220 H arrangement of the series drawing. The
installed display variant (Simarine PICO vs. PICOone), shunt
configuration and all as-built device identities remain explicit
unknowns (issue #260).

## 4. Other model files

| File | Content |
| --- | --- |
| `system-electrical.yaml` | The electrical system instance (12 V / 230 V system-level claims) |
| `interface-shore-power-feed.yaml` + `connection-shore-power-feed.yaml` | Shore inlet → battery charger (AC) |
| `interface-charger-dc-output.yaml` + `connection-charger-dc-output.yaml` | Charger → service bank |
| `interface-alternator-charge-feed.yaml` + `connection-alternator-charge-feed.yaml` | Alternator role → service bank |
| `interface-battery-main-feed.yaml` + `connection-battery-main-feed.yaml` | Service bank → main DC distribution |
| `interface-dc-feed-refrigeration.yaml` + `connection-dc-feed-refrigeration.yaml` | Distribution → refrigeration |
| `interface-dc-feed-navigation-lights.yaml` + `connection-dc-feed-navigation-lights.yaml` | Distribution → navigation lights |
| `interface-dc-feed-bilge-pump.yaml` + `connection-dc-feed-bilge-pump.yaml` | Distribution → electric bilge pump |
| `interface-dc-feed-freshwater-pump.yaml` + `connection-dc-feed-freshwater-pump.yaml` | Distribution → electric freshwater pump |
| `interface-inverter-dc-feed.yaml` (no connection — see below) | Service bank → inverter (option path) |

**Inverter representation decision.** The captured specification lists
the inverter only as factory option XH2201 (inverter/charger, only with
battery upgrade XH1001 or XH1005); it is not standard equipment. The
§5.1-mandated role is therefore modeled with its presence explicitly
unknown (`quantity: unknown`), the option rating transcribed verbatim
as an option-scoped attribute, and the battery-to-inverter **interface**
kept as the typed contract of the option path — but **no connection
instance** exists, because a connection is a realized link of the
configuration and the standard reference configuration contains no
inverter. AC-side consumers of the option package are out of scope per
golden path §5.2.

## 5. Published unknowns count per file

Generated with (run from the repository root):

```bash
cd reference/hanse460 && for f in *.yaml; do echo "$f: $(grep -c 'status: unknown' $f)"; done
```

| File | Unknowns |
| --- | --- |
| `connection-alternator-charge-feed.yaml` | 0 |
| `connection-battery-main-feed.yaml` | 0 |
| `connection-charger-dc-output.yaml` | 0 |
| `connection-dc-feed-bilge-pump.yaml` | 0 |
| `connection-dc-feed-freshwater-pump.yaml` | 0 |
| `connection-dc-feed-navigation-lights.yaml` | 0 |
| `connection-dc-feed-refrigeration.yaml` | 0 |
| `connection-shore-power-feed.yaml` | 0 |
| `equipment-alternator-charging.yaml` | 4 |
| `equipment-battery-charger.yaml` | 4 |
| `equipment-dc-consumer-bilge-pump.yaml` | 4 |
| `equipment-dc-consumer-freshwater-pump.yaml` | 6 |
| `equipment-dc-consumer-navigation-lights.yaml` | 7 |
| `equipment-dc-consumer-refrigeration.yaml` | 4 |
| `equipment-dc-main-distribution.yaml` | 4 |
| `equipment-inverter.yaml` | 6 |
| `equipment-measurement-service-battery.yaml` | 7 |
| `equipment-protection-dc-main.yaml` | 4 |
| `equipment-service-battery-bank.yaml` | 6 |
| `equipment-shore-power-inlet.yaml` | 6 |
| `interface-alternator-charge-feed.yaml` | 1 |
| `interface-battery-main-feed.yaml` | 0 |
| `interface-charger-dc-output.yaml` | 1 |
| `interface-dc-feed-bilge-pump.yaml` | 0 |
| `interface-dc-feed-freshwater-pump.yaml` | 0 |
| `interface-dc-feed-navigation-lights.yaml` | 0 |
| `interface-dc-feed-refrigeration.yaml` | 0 |
| `interface-inverter-dc-feed.yaml` | 1 |
| `interface-shore-power-feed.yaml` | 0 |
| `system-electrical.yaml` | 0 |
| **Total** | **65** |

WP-0093 / #258 transcribed the owner-held document set captured by
register v0.3.0 into the model: **34 of the 99** WP-0082 unknowns were
closed at class `sourced-manufacturer` (41 new sourced values in total,
including 7 new attributes such as bank topology, protection inventory
and circuit inventory). Per unknown group:

- **Closed (34):** system architecture (1); service-bank capacity and
  location (2); charger profile, input range and location (3);
  DC-distribution topology and location (2); protection inventory,
  ratings and locations (3); measurement instrument type (1);
  alternator presence, rating and location (3); shore-inlet protection
  rating (1); bilge-pump flow rating and location (2); all eight
  connection conductor specifications (8); eight interface limits/media
  (8).
- **Blocked, deliberately still unknown (per issue #258 preconditions,
  follow-up #260):** service-battery model/manufacturer/bank
  composition (Lifos 105 vs. Go); every MultiPlus/inverter value
  (`equipment-inverter.yaml` unchanged, 6 unknowns); isolation
  transformer values; hull identity (all applicability statements stay
  design-family); Simarine Pico variant/shunt configuration and display
  location; Aqua Signal installed light series/positions/power draw.
- **Otherwise open:** values no captured document states (e.g.
  freshwater-pump rating, connector standard, calibration state,
  regulation type, serial numbers).

The remaining unknown count is the honest state of the evidence:
unknowns are first-class data, never hidden (golden path §10.2
assumption 1), and closing the blocked groups requires the accountable
maintainer's as-built confirmations (register §4.4/§5, issue #260).

## 6. Conflicting-claims record

Schema contract v0.2.0 (`OMSP-SCHEMA-MARITIME-0001` §4/§7) provides the
`claims[]` construct for representing conflicting source values side by
side. **The WP-0093 transcription produced no electrical conflict**:
every owner-held value that overlaps an existing `sourced-secondary`
claim corroborates it (charger 35 A standard rating, 12 V/230 V system
claims, AGM standard battery set — see register §3.4 for the
register-level assessment), so no existing value was removed or
converted, and the register §3.4 conflicts (fuel tank, sail areas) are
outside this electrical slice. This model therefore still contains no
`claims[]` instance; the construct is exercised by the permanent schema
fixtures (`tests/schemas/positive/equipment-conflicting-claims.yaml`,
negative N12). When future captures produce conflicting electrical
claims — e.g. resolving the inverter-identity discrepancy noted in
issue #260 (circuit diagram sheet 3 names a Mastervolt Combi Master
12/3000 option; the archived vendor manual is a Victron MultiPlus
Compact 120 V edition) — they must be modeled side by side with this
construct, never silently resolved (register §6).

## 7. Validation

From the repository root (dependencies pinned per
`governance/ADR-0004-PYTHON-VALIDATION-DEPENDENCIES.md`):

```bash
python3 tooling/validate_ontology.py
python3 tooling/validate_instance_schemas.py reference/hanse460
python3 tooling/validate_model_integrity.py reference/hanse460 \
  --register reference/HANSE_460_SOURCE_REGISTER.md
```

All commands must exit `0` with `"findings": 0`. The same chain runs
in CI (`.github/workflows/instance-schemas.yml`). The third command
(WP-0083 / #204, `tooling/validate_model_integrity.py`) mechanically
checks referential integrity across instances and register resolution:
interface/connection endpoints resolve to package ports
(`OMSP-INTEGRITY-001`), scenario references resolve to package
equipment/connections (`OMSP-INTEGRITY-002`; this package has no
scenario instances yet, so the class runs over zero instances),
`document:` references resolve through the register §7 mapping and cite
no inaccessible source (`OMSP-INTEGRITY-003`), and every non-`unknown`
value carries complete five-field provenance whose `source_id` resolves
to a register §2.2 entry (`OMSP-INTEGRITY-004`).

## 8. Derived diagram views (WP-0084 addition, v0.1.1)

Structural diagram views derived from this model package live in
[`diagrams/`](diagrams/), per the Marine Diagram System source convention
(`publication/mods/MDS-MARINE-DIAGRAM-SYSTEM.md`, `OMSP-MODS-MDS-0001`,
MDS-R-10). Views are derived artifacts: they add no model content, and
corrections are made in the model instances, never in a view.

| View | Artifact |
| --- | --- |
| Energy-chain view (golden path §7.1) | [`diagrams/ENERGY-CHAIN-VIEW.md`](diagrams/ENERGY-CHAIN-VIEW.md) (`OMSP-REFERENCE-HANSE460-DIAGRAM-0001`) |

## 9. Safety and authority boundary

This model is advisory reference data for a design-family configuration
(`OMSP-REFERENCE-CONFIG-0001` §2): it represents no specific hull, makes
no `verified-design` or `verified-as-built` claim, and carries no
certification, compliance, seaworthiness or operational-fitness meaning.
Nothing in it is an operational instruction; every safety-relevant
conclusion requires accountable human judgment
(`reference/DIGITAL_TWIN_GOVERNANCE_AND_SAFETY_BOUNDARIES.md`).
