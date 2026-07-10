# Digital Twin Validation Traceability

- Artifact ID: `OMSP-REFERENCE-TWIN-DEMO-TRACE-0001`
- Version: `0.1.0`
- Status: `review`

## Purpose

This matrix records how the WP-0044 demonstrator links the Sprint-4 reference artifacts into one reviewable evidence chain.

## Traceability matrix

| Demonstrator concern | Source artifact | Referenced identifier | Evidence in demonstrator | Expected result |
|---|---|---|---|---|
| Vessel applicability | `hanse-460-reference-configuration.json` | `configuration:vessel-design:hanse:460:reference-0.1.0` | manifest `references.configuration_id` | design-family reference only |
| Vessel design | `hanse-460-reference-configuration.json` | `vessel-design:hanse:460` | manifest `references.vessel_design_id` | no vessel instance asserted |
| Navigation system | Hanse 460 configuration | `system:vessel-design:hanse:460:navigation-comms` | all observation targets | system role resolves |
| Monitoring system | Hanse 460 configuration | `system:vessel-design:hanse:460:monitoring-networks` | manifest system references | system role resolves |
| Equipment role semantics | `equipment-interface-model.example.json` | illustrative equipment/port/interface roles | demonstrator narrative and targets | no installed-equipment claim |
| Scenario | `operational-scenario-model.examples.json` | `scenario:hanse-460:navigation-data-degradation:illustrative-0.1.0` | manifest `references.scenario_id` | degraded scenario resolves |
| Human authority | scenario model | `actor:accountable-human-operator` | run authority and human report | human command remains explicit |
| Immutable observations | `digital-twin-state-observation.examples.json` | observation identity pattern | manifest `observations[]` | observations remain evidence records |
| Freshness handling | state/observation model | freshness metadata | stale position observation | stale data excluded from current state |
| Conflict handling | state/observation model | conflict-set semantics | two speed observations | conflict preserved and visible |
| Missing-data handling | state/observation model | missing reason codes | missing wind observation | no fabricated default |
| Human report handling | state/observation model | human-reported authority | display inconsistency report | separate from sensor observation |
| Current-state projection | state/observation model | projection policy | `current-state-policy:wp-0044:0.1.0` | reproducible time-scoped view |
| Derived provenance | state/observation model | derived-value contract | readiness derived value | inputs and method version visible |
| Scenario decision boundary | scenario model | advisory-only software role | derived readiness outcome | no autonomous action |

## Evidence chain

```text
Hanse 460 design-family reference configuration
  -> navigation and monitoring system identifiers
  -> illustrative equipment and interface roles
  -> navigation-data degradation scenario
  -> immutable simulated and human-reported observations
  -> quality, freshness, missing and conflict evaluation
  -> reproducible current-state projection
  -> provenance-complete advisory derived value
  -> accountable human disposition
```

## Review assertions

A reviewer shall confirm that:

1. every stable identifier resolves to the intended model layer;
2. applicability remains design-family reference scope;
3. equipment roles are not presented as physical installations;
4. observations are not presented as configuration facts;
5. current state is produced only through a declared policy;
6. stale, missing and conflicting evidence remains visible;
7. derived values retain method and input provenance;
8. human authority remains explicit;
9. no vessel-control output is produced.

## Evidence status values

Each traceability item may be recorded as:

- `pass`: reference and expected behavior are demonstrated;
- `fail`: reference is unresolved or behavior violates the model;
- `indeterminate`: evidence is insufficient to decide;
- `not-applicable`: item is outside the declared demonstrator scope.

`Indeterminate` must not be silently converted to `pass`.
