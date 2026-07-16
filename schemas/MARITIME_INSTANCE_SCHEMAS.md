---
Artifact-ID: OMSP-SCHEMA-MARITIME-0001
Title: Maritime Instance Schemas
Version: 0.2.0
Status: Draft
Owner: toss-cengiz
Baseline: Sprint-7
Classification: Public
Related-Issue: WP-0078 / #199
Depends-On:
  - OMSP-ONTOLOGY-MARITIME-0001
Traceability:
  - ISSUE-199
  - ISSUE-201
  - ISSUE-203
  - OMSP-PLANNING-GOLDEN-PATH-0001
  - OMSP-PLANNING-REBASELINE-0001
  - OMSP-REFERENCE-EQUIPMENT-0001
  - OMSP-REFERENCE-SCENARIO-0001
  - OMSP-REFERENCE-SOURCE-0001
---

# Maritime Instance Schemas

## 1. Purpose

This artifact is the companion documentation for the maritime instance
JSON Schemas delivered by WP-0078. The schemas make real vessel data
mechanically validatable: every value-bearing field must either carry a
complete provenance block or an explicit `unknown` marker — the binding
provenance rules of `OMSP-PLANNING-GOLDEN-PATH-0001` §4.3 become a
schema contract instead of a review convention.

The schema files are the normative machine-readable contract; this
document records their conceptual grounding, mapping to the maritime
ontology, and boundaries. Where they disagree, the schema files govern
and this document must be corrected.

## 2. Schema Set

| Schema file | Instance type | Ontology concept |
| --- | --- | --- |
| `schemas/provenance.schema.json` | shared `$defs` (no instance type) | grounds `OMSP-CONCEPT-SOURCE-RECORD` references |
| `schemas/vessel-instance.schema.json` | Vessel | `OMSP-CONCEPT-VESSEL` |
| `schemas/system-instance.schema.json` | Vessel System | `OMSP-CONCEPT-VESSEL-SYSTEM` |
| `schemas/equipment-instance.schema.json` | Equipment Role | `OMSP-CONCEPT-EQUIPMENT-ROLE` |
| `schemas/interface-instance.schema.json` | Interface | `OMSP-CONCEPT-INTERFACE` |
| `schemas/connection-instance.schema.json` | Connection | `OMSP-CONCEPT-CONNECTION` |
| `schemas/scenario-instance.schema.json` | Operational Scenario | `OMSP-CONCEPT-OPERATIONAL-SCENARIO` |

Every instance carries a required `concept` constant naming its
ontology identity; the validator dispatches instances to schemas by
this field. Nested structures resolve to further maritime concepts:
`ports[]` items to `OMSP-CONCEPT-PORT`, `measurement_points[]` items to
`OMSP-CONCEPT-MEASUREMENT-POINT`, and `implements:
OMSP-CONCEPT-PROTECTION` to the Protection capability.

## 3. Property-to-Relation Mapping

Schema properties encode the maritime and core relations of
`OMSP-ONTOLOGY-MARITIME-0001` §3 (relations are not redefined here):

| Schema property | Relation | Domain → Range |
| --- | --- | --- |
| `system.belongs_to`, `equipment.belongs_to`, `connection.belongs_to` | `belongs-to` (core) | member → parent |
| `equipment.depends_on[]` | `depends-on` (core) | Equipment Role → Equipment Role |
| `equipment.implements[]`, `connection.implements` | `implements` (core) | role → Protection / connection → Interface |
| `connection.source_port`, `connection.target_port` | `connects-to` | Port → Port |
| `equipment.protects[]` | `protects` | Equipment Role → Entity |
| `measurement_points[].measures` | `measures` | Measurement Point → Entity |
| `provenance.source_id` | `sourced-from` | Entity → Source Record |
| `scenario.related_equipment[]`, `scenario.affected_systems[]` | `uses` / `traces-to` (core) | Scenario → model elements |

## 4. Provenance Contract (binding)

Defined once in `schemas/provenance.schema.json` and referenced by all
value-bearing fields (`provenanced-value`):

- **Known value** — object with `value` (scalar; the literals `unknown`
  and `<to-be-sourced>` are schema-invalid here, per decision D3 of the
  issue #199 record), optional free-string `unit`, and a required
  `provenance` object whose five sub-fields are all mandatory:
  `source_id` (pattern `^source:...`), `authority_class` (the five
  evidence-bearing classes of `OMSP-PLANNING-GOLDEN-PATH-0001` §4.1;
  `unknown` is not an authority class of a known value), `confidence`
  (`high | medium | low`, decision D2), `retrieval_date` (ISO date) and
  `applicability`.
- **Unknown marker** — `{status: unknown}` with an optional `note`.
  Unknowns are first-class and always expressible; hiding an unknown
  behind an unsourced value is mechanically impossible.
- **Conflicting claims** (v0.2.0, WP-0082) — `{claims: [...]}` with an
  optional `note`: an array of **at least two** complete known-values
  (each with its own five-field provenance block) representing
  conflicting source values for a single attribute side by side, per
  the conflict discipline of `OMSP-REFERENCE-SOURCE-0001` §6 and
  `OMSP-PLANNING-GOLDEN-PATH-0001` §4.3 rule 3. The schema cannot and
  does not select a winning claim; conflict resolution is an
  accountable human decision.
- **Bare scalars are rejected** on value-bearing fields
  (`type: object` + `oneOf`; the three branches are mutually
  exclusive).

Structural fields (identifiers, `concept`, layer/class enums,
`belongs_to`/parent references, port endpoints, interface family,
`accountable_authority`, `schema_version`) can never be `unknown`
(decision D4): an instance without a resolvable identity skeleton is
not capturable data.

## 5. Domain Neutrality

The schemas encode no equipment type, vessel model, physical-quantity
kind or transported-medium kind, per the binding neutrality rule of
`OMSP-ONTOLOGY-MARITIME-0001` §1. The only governed enums are: the
authority classes, the confidence scale, the nine interface families
(`OMSP-REFERENCE-EQUIPMENT-0001` §6) and the five scenario classes
(`OMSP-REFERENCE-SCENARIO-0001` §2). Value-bearing content — media,
units, quantities, manufacturer facts — is free-form instance data
under the provenance contract. The non-electrical fixture
(`tests/schemas/positive/equipment-freshwater-pump.yaml`) is the
standing smoke test for this rule.

## 6. Validation and CI

- Validator: `tooling/validate_instance_schemas.py` — (1) checks every
  `schemas/*.schema.json` against the Draft 2020-12 meta-schema,
  (2) self-tests the contracts (`tests/schemas/positive/*` must pass,
  `tests/schemas/negative/*` must be rejected), (3) validates instance
  YAML paths passed as arguments, (4) ontology conformance (WP-0080,
  rule `OMSP-ISCHEMA-005`): every `OMSP-CONCEPT-*` reference in the
  schema files and in argument instances must resolve to
  `ontology/omsp-ontology.json`, independently of the schema `concept`
  const dispatch. Output is a JSON findings report consistent with
  `tooling/omsp_validate.py`; any finding exits non-zero.
- CI gate: `.github/workflows/instance-schemas.yml`, with dependencies
  pinned per `governance/ADR-0004-PYTHON-VALIDATION-DEPENDENCIES.md`.
- Sample package: `examples/maritime-sample/` (WP-0080) instantiates
  every schema type; its README documents the single validation
  command chain (not repeated here).
- Fixtures are permanent and fictional; see `tests/schemas/README.md`
  (decision D6). Referential integrity across instances and resolution
  of `source_id` against the source register are WP-0083 scope, not
  schema scope.

## 7. Versioning

Each instance carries a required `schema_version` (SemVer). The current
contract version is `0.2.0`; breaking changes to any schema require a
version change of this artifact and a migration note per the change
rules of `governance/ENGINEERING_PLAYBOOK.md`.

Change record:

- **0.2.0 (WP-0082 / #203)** — additive minor change: new
  `conflicting-claims` branch (`claims[]` of known-values, `minItems: 2`)
  in the `provenanced-value` `oneOf` of `provenance.schema.json`,
  implementing the #171 criterion-6 decision (CTO gap-1). **Backward
  compatible:** every instance valid under `0.1.0` remains valid
  unchanged (no existing field or branch was modified); no migration is
  required. Instances that use the `claims[]` construct must declare
  `schema_version` `0.2.0` or later. Fixtures: positive
  `equipment-conflicting-claims.yaml`, negative N12.
- **0.1.x** — initial WP-0078 contract (`0.1.0`) and its documentation
  corrections.

## 8. Safety and Authority Boundary

- Schema validation is **advisory verification only**. A passing
  instance proves structural and provenance-contract conformance — it
  does not certify seaworthiness, electrical or equipment compliance,
  installation, fitness, or safe operation, and it does not make the
  described data true.
- Scenario instances validated by these schemas are reference material
  under `OMSP-REFERENCE-SCENARIO-0001` §14: never approved procedures,
  never operational instructions, never a substitute for manufacturer
  documentation or the accountable human's judgment.
- The schemas grant no authority to AI or automation: authority-class
  promotion, conflict resolution and every approval remain accountable
  human decisions (`reference/DIGITAL_TWIN_GOVERNANCE_AND_SAFETY_BOUNDARIES.md`).
