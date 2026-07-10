# Digital Twin Validation Demonstrator — Known Limitations

- Artifact ID: `OMSP-REFERENCE-TWIN-DEMO-LIMITS-0001`
- Version: `0.1.0`
- Status: `review`

## Scope limitations

The demonstrator validates documentation-level interoperability only.

It does not provide:

- a production digital-twin platform;
- a live telemetry connection;
- a physical vessel model;
- an as-built equipment inventory;
- an approved navigation or emergency procedure;
- a certified risk assessment;
- a control system or command path;
- a cybersecurity implementation;
- a database, event bus, time-series store, or API contract;
- deterministic real-time guarantees;
- calibration evidence;
- fleet-scale identity management;
- data-retention or privacy controls;
- operator training or competence evidence.

## Data limitations

All demonstrator observations are simulated or human-reported. Values are illustrative and must not be interpreted as measurements from a real Hanse 460.

The Hanse 460 configuration remains a design-family reference. Unknown manufacturer, option-package, equipment, interface, installation, and vessel-instance facts remain unknown.

## Method limitations

The current-state projection and `navigation-data-readiness` method are documentation examples. They are not validated algorithms for operational decision-making.

No numerical threshold in the demonstrator is approved for navigation, safety, maintenance, or certification use.

## Human authority limitation

The demonstrator can only surface evidence and advisory states. It cannot authorize, execute, or verify operational action.

## Reproducibility limitation

Reproduction means applying the declared documentation rules to the included static manifest. It does not demonstrate runtime determinism across software implementations.

## Promotion boundary

No demonstrator result may be promoted to:

- verified configuration;
- verified as-built state;
- approved procedure;
- operational authorization;
- seaworthiness evidence;
- certification evidence;
- autonomous-control authority.

Such promotion requires separate governed evidence and accountable human approval.
