# Pilot Readiness Assessment and Approval

## Purpose

This document defines the governed assessment and accountable human approval record required before an immutable OMSP revision may enter a controlled pilot.

## Scope

The assessment consolidates evidence produced by WP-0061 through WP-0067 and determines whether the candidate revision is ready for a controlled, non-production pilot. It does not authorize production deployment, unrestricted external access, physical-vessel control, certification, or autonomous operation.

## Immutable Assessment Identity

Every assessment shall bind to:

- source repository and immutable commit SHA;
- artifact identifier and cryptographic digest;
- provenance statement and signer identity;
- controlled-pilot environment identifier and revision;
- configuration and policy revision;
- demonstrator execution identifier;
- evidence manifest digest;
- assessment timestamp and expiry timestamp.

Any change to a bound item invalidates the approval and requires reassessment.

## Mandatory Evidence Domains

The assessor shall review evidence for:

1. controlled pilot environment and access-control baseline;
2. signed provenance and tamper-evident audit evidence;
3. remote telemetry, alerting, paging and evidence retention;
4. vulnerability intelligence and full-history secret scanning;
5. performance, availability and capacity qualification;
6. external backup and disaster-recovery validation;
7. controlled pilot integration demonstrator.

A missing, stale, unverifiable or internally inconsistent evidence domain shall produce a `BLOCKED` disposition.

## Gate Outcomes

Each gate shall be recorded as one of:

- `PASS` — evidence satisfies the declared requirement;
- `PASS_WITH_LIMITATIONS` — requirement is substantially met, with explicit non-blocking limitations;
- `FAIL` — evidence demonstrates that the requirement is not met;
- `BLOCKED` — evidence is absent, stale, unverifiable or execution could not be completed.

Critical mandatory gates may not be overridden by automation.

## Risk Register

The assessment shall explicitly record the status of RR-001 through RR-005, including:

- current severity;
- evidence reviewed;
- mitigation status;
- residual exposure;
- accountable owner;
- expiry or reassessment date;
- whether human risk acceptance is requested.

Documentation alone does not close a risk. Closure requires concrete implementation evidence, validation and accountable human approval.

## Decision Model

Allowed final dispositions are:

- `APPROVED_FOR_CONTROLLED_PILOT`;
- `APPROVED_WITH_CONDITIONS`;
- `NOT_APPROVED`;
- `BLOCKED`.

`APPROVED_FOR_CONTROLLED_PILOT` requires all mandatory gates to pass, no unresolved blocking condition, complete evidence integrity, and all required human approvals.

`APPROVED_WITH_CONDITIONS` is permitted only when limitations are explicitly bounded, time-limited, non-critical and accepted by authorized humans. It may not be used to bypass missing provenance, missing environment approval, exposed secrets, failed critical security gates, telemetry loss, failed recovery validation or abort-control failures.

## Human Approval and Separation of Duties

At minimum, the record shall include:

- technical assessor;
- security approver;
- operations or reliability approver;
- accountable pilot owner;
- risk owner for each accepted residual risk.

The same person shall not be the sole author, sole assessor and sole approver of the same evidence package. Conflicts of interest shall be declared.

Automation may assemble evidence and recommend a disposition. Automation may not approve pilot activation, accept residual risk, waive mandatory gates or sign on behalf of a human approver.

## Approval Record

Each human approval shall contain:

- approver name and accountable role;
- identity reference;
- decision;
- scope and conditions;
- acknowledged residual risks;
- timestamp;
- expiry;
- cryptographic or platform-verifiable approval reference.

The approval shall be bound to the immutable assessment identity and evidence manifest digest.

## Expiry, Revocation and Reassessment

Approval shall expire automatically when:

- the declared expiry date is reached;
- source, artifact, environment or configuration changes;
- a signing key is revoked or compromised;
- a new critical vulnerability or exposed secret is identified;
- telemetry, alerting or audit evidence becomes unavailable;
- recovery objectives are no longer met;
- a material incident occurs;
- a mandatory control fails;
- an approver revokes consent.

After expiry or revocation, pilot activity shall pause until reassessment and renewed human approval.

## Evidence Retention

The final assessment package shall retain:

- evidence manifest;
- gate-by-gate findings;
- unresolved limitations;
- risk decisions;
- approver records;
- timestamps and identities;
- final disposition;
- revision and artifact bindings;
- revocation and expiry information.

The package shall be tamper-evident and stored outside the primary pilot failure domain when feasible.

## Governance Boundary

A successful assessment authorizes only the declared controlled-pilot scope for the declared immutable revision and validity period. It does not establish a production SLA, certify safety, authorize autonomous or physical control, or grant production authority.

## Current Status

This document defines the assessment and approval contract only. It does not record an actual pilot approval and does not claim that RR-001 through RR-005 are closed.