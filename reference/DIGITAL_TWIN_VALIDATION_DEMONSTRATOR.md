# Digital Twin Validation Demonstrator

- Artifact ID: `OMSP-REFERENCE-TWIN-DEMO-0001`
- Version: `0.1.0`
- Status: `review`
- Scope: documentation-level interoperability validation
- Vessel applicability: Hanse 460 design family reference only

## 1. Purpose

This demonstrator validates that the Sprint-4 vessel configuration, equipment/interface, operational scenario, and state/observation models can be linked into one reviewable evidence chain.

It does not represent a production runtime, a physical vessel, an installed equipment inventory, an approved operating procedure, or authority to control a vessel.

## 2. Demonstrator use case

### Use case

Navigation data degradation during an illustrative Hanse 460 design-family voyage-planning review.

### Goal

Show that:

1. a scenario can reference a vessel configuration and system roles;
2. observations can reference those roles without becoming configuration facts;
3. conflicting and stale observations remain visible;
4. a current-state projection can be reproduced from immutable inputs;
5. a derived advisory value can retain full provenance;
6. human command authority remains explicit.

## 3. Referenced artifacts

| Layer | Artifact |
|---|---|
| Vessel configuration | `reference/hanse-460-reference-configuration.json` |
| Equipment/interface model | `reference/equipment-interface-model.example.json` |
| Scenario model | `reference/operational-scenario-model.examples.json` |
| State/observation model | `reference/digital-twin-state-observation.examples.json` |

## 4. Stable identifiers used

- Configuration: `configuration:vessel-design:hanse:460:reference-0.1.0`
- Vessel design: `vessel-design:hanse:460`
- Navigation system: `system:vessel-design:hanse:460:navigation-comms`
- Monitoring network: `system:vessel-design:hanse:460:monitoring-networks`
- Scenario: `scenario:hanse-460:navigation-data-degradation:illustrative-0.1.0`
- Demonstrator run: `demonstrator-run:wp-0044:nav-data-degradation:001`

Identifiers referring to equipment roles are illustrative design-family roles and are not assertions of installed devices.

## 5. Initial conditions

- The configuration authority remains `reference` or lower.
- No vessel instance is assigned.
- No installed sensor is asserted.
- All input observations are simulated or human-reported.
- The accountable human operator retains command authority.
- Software output is advisory only.

## 6. Evidence sequence

### Step 1 — Scenario activation

The scenario is activated for review when an illustrative navigation-data source becomes unavailable or inconsistent.

Expected traceability:

`scenario -> vessel configuration -> navigation system role -> observation targets`

### Step 2 — Observation intake

The evidence package contains:

- a simulated fresh heading observation;
- a stale simulated position observation;
- two conflicting simulated speed observations;
- one human report stating that a display appears inconsistent;
- one explicitly missing observation with a reason code.

Each observation retains:

- event time;
- receipt time;
- processing time;
- source identity and source class;
- authority class;
- quality and freshness state;
- target entity/property;
- immutable observation identity.

### Step 3 — Current-state projection

The projection policy:

1. excludes observations beyond freshness limits;
2. does not silently choose between unresolved conflicts;
3. preserves missing values as missing;
4. surfaces human reports separately from machine observations;
5. records the projection time and policy version.

Expected result:

- heading may be represented as current when fresh and valid;
- position remains stale and is not promoted into the current state;
- speed remains conflicted;
- the human report remains visible as a report;
- missing data remains explicit.

### Step 4 — Derived advisory value

An illustrative `navigation-data-readiness` value is derived from the projected state.

The result must identify:

- every input observation or state assertion;
- method identifier and version;
- assumptions;
- execution time;
- result quality;
- unresolved conflicts and missing inputs.

The derived value must not be represented as a verified vessel fact or an operational command.

### Step 5 — Scenario decision boundary

The demonstrator may produce an advisory state such as `degraded-data-review-required`.

Only the accountable human operator may:

- accept or reject the advisory;
- decide whether to continue, pause, or abort an activity;
- apply an approved procedure;
- resolve a conflict based on external evidence.

## 7. State transitions

| From | Trigger | To | Authority |
|---|---|---|---|
| `not-evaluated` | scenario review starts | `evaluating` | demonstrator process |
| `evaluating` | stale/conflicting inputs detected | `degraded-data-review-required` | advisory only |
| `degraded-data-review-required` | accountable human records disposition | `human-disposition-recorded` | human authority |
| any | evidence invalid or incomplete | `indeterminate` | model rule |

No state transition in this demonstrator controls equipment or changes vessel configuration.

## 8. Reproducibility procedure

A reviewer can reproduce the evidence chain by:

1. loading the manifest in `digital-twin-validation-demonstrator.example.json`;
2. resolving all referenced stable identifiers;
3. ordering observations by event time while preserving receipt and processing times;
4. applying projection policy `current-state-policy:wp-0044:0.1.0`;
5. checking stale, missing, and conflict rules;
6. evaluating derived method `method:navigation-data-readiness:0.1.0`;
7. comparing the result with the expected assertions in the manifest;
8. recording pass, fail, or indeterminate for every validation item.

## 9. Pass criteria

The demonstrator passes when:

- every reference resolves to the intended artifact layer;
- observations remain distinct from configuration facts;
- stale, missing, and conflicting data remain visible;
- current-state output is reproducible from the declared policy;
- derived values expose complete provenance;
- human authority is explicit;
- no production or vessel-control capability is claimed.

## 10. Failure criteria

The demonstrator fails when:

- an observation is promoted to verified configuration without governed evidence;
- an unresolved conflict is silently discarded;
- stale data silently populates current state;
- missing values are replaced with fabricated defaults;
- derived outputs omit inputs or method versions;
- software is represented as command authority;
- any illustrative role is presented as installed equipment evidence.

## 11. Safety boundary

This artifact is not:

- a navigation procedure;
- an emergency checklist;
- a seaworthiness assessment;
- a certification record;
- a vessel-specific configuration record;
- a live digital-twin runtime;
- an autonomous control function.
