# Sprint 4 Baseline and Release Readiness

- Artifact ID: `OMSP-REFERENCE-SPRINT4-BASELINE-0001`
- Version: `0.1.0`
- Status: `review`
- Baseline type: documentation-level digital twin foundation
- Proposed release version: `0.4.0`

## 1. Purpose

This package closes Sprint 4 by defining a governed documentation baseline for OMSP digital-twin foundations.

It records what is complete, what remains deferred, which dependencies have been satisfied, and which approval and safety boundaries apply.

## 2. Baseline scope

The baseline includes:

- Sprint 4 scope and execution plan;
- vessel reference model;
- Hanse 460 reference configuration;
- equipment and interface model;
- operational scenario model;
- digital-twin state and observation model;
- validation demonstrator;
- governance and safety boundaries;
- release-readiness evidence.

## 3. Work-package evidence

| Work package | Issue | Evidence status | Baseline disposition |
|---|---:|---|---|
| WP-0038 Sprint Scope & Execution Plan | #72 | merged | accepted |
| WP-0039 Vessel Reference Model | #73 | merged | accepted |
| WP-0040 Hanse 460 Reference Configuration | #74 | merged | accepted |
| WP-0041 Equipment & Interface Model | #75 | merged | accepted |
| WP-0042 Operational Scenario Model | #76 | merged | accepted |
| WP-0043 Digital Twin State & Observation Model | #77 | merged | accepted |
| WP-0044 Digital Twin Validation Demonstrator | #78 | merged | accepted |
| WP-0045 Digital Twin Governance & Safety Boundaries | #79 | merged | accepted |
| WP-0046 Baseline & Release Readiness | #80 | pending review | release gate |

## 4. Readiness conclusion

The Sprint 4 documentation baseline is ready for human review and repository merge when:

1. all WP-0046 artifacts are reviewed;
2. no unresolved model-interoperability defect remains;
3. governance and safety boundaries are explicitly acknowledged;
4. a named human approver records approval or rejection;
5. the release scope remains documentation-only.

## 5. Release classification

Proposed classification:

`foundation-documentation-baseline`

This classification does not authorize:

- live telemetry ingestion;
- production runtime deployment;
- vessel control;
- autonomous navigation;
- approved operating procedures;
- certification or class approval;
- vessel-specific as-built claims;
- seaworthiness or legal-compliance claims.

## 6. Baseline integrity rules

- Every artifact retains a stable identifier and version.
- Every illustrative value remains visibly illustrative.
- Observations remain separate from verified configuration.
- Derived values retain provenance and remain advisory.
- Human authority remains explicit.
- Repository merge does not create operational authority.
- Deferred work remains visible rather than being represented as complete.

## 7. Proposed next baseline

Future runtime, vessel-instance, telemetry, security, certification, and operational work must be placed in later governed baselines with separate approval evidence.