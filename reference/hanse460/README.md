---
Artifact-ID: OMSP-REFERENCE-HANSE460-ELECTRICAL-0001
Title: Hanse 460 Electrical-Slice Reference Model
Version: 0.1.0
Status: Draft
Owner: toss-cengiz
Baseline: Sprint-8
Classification: Public
Related-Issue: WP-0082 / #203
Depends-On:
  - OMSP-SCHEMA-MARITIME-0001
  - OMSP-REFERENCE-SOURCE-0001
Traceability:
  - ISSUE-203
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
to a single register entry of
`reference/HANSE_460_SOURCE_REGISTER.md` **v0.2.0**:

- `source:secondary:newwaveyachts:hanse-460-spec-pricelist-2021-11-12:2026-07-15`
  (class `sourced-secondary`, confidence `medium`, applicability
  "US-market standard specification valid from 2021.11.12; design family
  only, no hull applicability").

Document references use the register §7 mapping row
`document:hanseyachts:hanse-460-specification-pricelist-us:2021-11-12`;
no inaccessible source (register §4.3) is cited. No electrical value
(voltage threshold, capacity allocation, protection rating, charge
parameter, conductor specification) was entered from memory; everything
the register does not support is an explicit unknown.

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

**Protection and measurement roles.** No captured source states any
protection device, rating, location or monitoring instrument; both
roles are OMSP reference structure (authority class `reference` is
allowed for structure, golden path §4.1) with all values explicitly
unknown. Finer decomposition awaits the owner-held wiring diagrams
(register §4.4).

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
| `connection-alternator-charge-feed.yaml` | 1 |
| `connection-battery-main-feed.yaml` | 1 |
| `connection-charger-dc-output.yaml` | 1 |
| `connection-dc-feed-bilge-pump.yaml` | 1 |
| `connection-dc-feed-freshwater-pump.yaml` | 1 |
| `connection-dc-feed-navigation-lights.yaml` | 1 |
| `connection-dc-feed-refrigeration.yaml` | 1 |
| `connection-shore-power-feed.yaml` | 1 |
| `equipment-alternator-charging.yaml` | 7 |
| `equipment-battery-charger.yaml` | 7 |
| `equipment-dc-consumer-bilge-pump.yaml` | 6 |
| `equipment-dc-consumer-freshwater-pump.yaml` | 6 |
| `equipment-dc-consumer-navigation-lights.yaml` | 7 |
| `equipment-dc-consumer-refrigeration.yaml` | 4 |
| `equipment-dc-main-distribution.yaml` | 6 |
| `equipment-inverter.yaml` | 6 |
| `equipment-measurement-service-battery.yaml` | 8 |
| `equipment-protection-dc-main.yaml` | 7 |
| `equipment-service-battery-bank.yaml` | 8 |
| `equipment-shore-power-inlet.yaml` | 7 |
| `interface-alternator-charge-feed.yaml` | 2 |
| `interface-battery-main-feed.yaml` | 1 |
| `interface-charger-dc-output.yaml` | 2 |
| `interface-dc-feed-bilge-pump.yaml` | 1 |
| `interface-dc-feed-freshwater-pump.yaml` | 1 |
| `interface-dc-feed-navigation-lights.yaml` | 1 |
| `interface-dc-feed-refrigeration.yaml` | 1 |
| `interface-inverter-dc-feed.yaml` | 1 |
| `interface-shore-power-feed.yaml` | 1 |
| `system-electrical.yaml` | 1 |
| **Total** | **99** |

The high unknown count is the intended, honest state of the model: the
owner-held document set — the primary evidence base for this slice — is
pending capture (register §4.4/§8), and unknowns are first-class data,
never hidden (golden path §10.2 assumption 1).

## 6. Conflicting-claims record

Schema contract v0.2.0 (`OMSP-SCHEMA-MARITIME-0001` §4/§7) provides the
`claims[]` construct for representing conflicting source values side by
side. **No conflicting electrical claims exist in source register
v0.2.0**: the register's §3.3 conflict assessment records only the
displacement comparison (consistent) and the sail-area comparison
(differing sail-plan basis, not a numeric contradiction) — neither is
electrical, and the electrical slice draws on a single register entry.
This model therefore contains no `claims[]` instance; the construct is
exercised by the permanent schema fixtures
(`tests/schemas/positive/equipment-conflicting-claims.yaml`, negative
N12). When future captures (register §4.4) produce conflicting
electrical claims, they must be modeled side by side with this
construct, never silently resolved (register §6).

## 7. Validation

From the repository root (dependencies pinned per
`governance/ADR-0004-PYTHON-VALIDATION-DEPENDENCIES.md`):

```bash
python3 tooling/validate_ontology.py
python3 tooling/validate_instance_schemas.py reference/hanse460
```

Both commands must exit `0` with `"findings": 0`. The same chain runs
in CI (`.github/workflows/instance-schemas.yml`). Referential integrity
across instances and mechanical `source_id`/`document:` resolution
against the register are WP-0083 scope.

## 8. Safety and authority boundary

This model is advisory reference data for a design-family configuration
(`OMSP-REFERENCE-CONFIG-0001` §2): it represents no specific hull, makes
no `verified-design` or `verified-as-built` claim, and carries no
certification, compliance, seaworthiness or operational-fitness meaning.
Nothing in it is an operational instruction; every safety-relevant
conclusion requires accountable human judgment
(`reference/DIGITAL_TWIN_GOVERNANCE_AND_SAFETY_BOUNDARIES.md`).
