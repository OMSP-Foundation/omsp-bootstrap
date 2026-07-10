# Digital Twin State and Observation Model Package

This package implements WP-0043 and establishes the governed boundary between configuration facts, runtime observations, time-bounded state assertions, current-state projections, historical state and derived values.

## Artifacts

- `DIGITAL_TWIN_STATE_AND_OBSERVATION_MODEL.md` — normative conceptual and governance model.
- `digital-twin-state-observation.examples.json` — illustrative machine-readable records.
- `DIGITAL_TWIN_STATE_OBSERVATION_VALIDATION_CHECKLIST.md` — acceptance and review checklist.

## Dependencies

The package uses stable vessel, system, equipment, interface and scenario identities defined by:

- `OMSP-REFERENCE-VESSEL-0001`;
- `OMSP-REFERENCE-CONFIG-0001`;
- `OMSP-REFERENCE-EQUIPMENT-0001`;
- `OMSP-REFERENCE-SCENARIO-0001`.

## Core Boundary

Runtime data does not become configuration truth merely because it is recent, repeated or machine-generated. Observations are immutable evidence records. Current state is a reproducible projection evaluated at a declared time. Derived values preserve their complete input and method provenance.

## Example Scope

The JSON examples use Hanse 460 design-family identifiers to demonstrate:

- timestamp and source metadata;
- simulated and human-reported observations;
- missing data representation;
- unresolved conflicting observations;
- state assertion generation;
- derived-value provenance;
- a conflict-preserving current-state view.

They are not live telemetry, installed-equipment evidence, approved procedures or claims about a physical vessel.

## Downstream Use

WP-0044 may use this package to construct a bounded validation demonstrator. Downstream implementations must preserve append-only evidence, authority separation, data-quality visibility and accountable human review.

## Exclusions

This package does not define a production database, event bus, time-series platform, sensor protocol, cybersecurity control, visualization layer or command-and-control integration.
