# Digital Twin Authority Matrix

- Artifact ID: `OMSP-REFERENCE-TWIN-AUTHORITY-0001`
- Version: `0.1.0`
- Status: `review`

## Authority matrix

| Artifact or output | May be created by | Required review | May approve | Operational meaning |
|---|---|---|---|---|
| Reference configuration | Author or model contributor | Model review | Reference maintainer | Design-family reference only |
| Declared configuration | Accountable owner delegate | Evidence review | Configuration authority | Owner declaration, not independently verified |
| Verified configuration | Authorized inspector/reviewer | Independent evidence review | Configuration authority | Verified within evidence scope |
| Observation | Sensor, human reporter, importer, simulator | Source/quality validation | Not applicable | Time-bound report, not configuration proof |
| State assertion | Declared projection process | Policy and provenance review | Model authority | Time-bounded interpretation |
| Derived advisory value | Declared method or AI-assisted process | Method and input review | Accountable human for use | Advisory only |
| Scenario artifact | Scenario author | Operational and safety review | Scenario authority | Modelled workflow, not approved procedure |
| Approved procedure | Competent external/internal authority | Controlled approval process | Designated procedure authority | Only authority defined by that process |
| AI-generated draft | AI-assisted process | Human review required | Authorized human | No authority before review |
| Runtime control output | Approved implementation only | Safety, system and operational assurance | Competent operational authority | Outside Sprint-4 reference scope |

## Separation rules

1. Observation authority does not equal configuration authority.
2. Multiple consistent observations may support a configuration review but cannot perform approval.
3. State projections expire according to their declared freshness policy.
4. Derived confidence does not raise authority level.
5. Repository merge indicates project acceptance, not operational authorization.
6. Simulated records must remain visibly simulated.
7. Human reports must remain distinguishable from machine observations.

## RACI-style accountability

| Activity | Author | Independent reviewer | Configuration authority | Accountable operator | AI/tooling |
|---|---|---|---|---|---|
| Draft model artifact | R | C | I | I | Aids only |
| Validate identifiers/provenance | R | A | C | I | Aids only |
| Approve configuration claim | C | C | A/R | I | Prohibited |
| Accept advisory for operational consideration | I | C | I | A/R | Prohibited |
| Resolve safety-critical conflict | C | C | C | A/R | Flag only |
| Approve model change | R | A | C when affected | I | Prohibited |
| Authorize runtime use | C | C | C | Competent authority | Prohibited |

Legend: `R` responsible, `A` accountable, `C` consulted, `I` informed.

## Mandatory presentation labels

Every consumer-facing representation must display, as applicable:

- authority class;
- approval status;
- source type;
- timestamp and freshness;
- quality and conflict status;
- simulation or AI-assistance marker;
- applicable configuration/version;
- required human action.
