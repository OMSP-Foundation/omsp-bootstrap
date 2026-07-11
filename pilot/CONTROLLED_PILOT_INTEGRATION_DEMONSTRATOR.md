# Controlled Pilot Integration Demonstrator

## Status

Design and validation contract only. This document does not authorize production deployment, external operational control, certification, physical-vessel operation or autonomous action.

## Purpose

Define a repeatable controlled-pilot demonstrator that proves the OMSP release, deployment, observability, security, recovery and governance controls operate together against one immutable revision and one bounded pilot environment.

## Entry Gates

The demonstrator must not start unless the accountable pilot approver records all of the following:

- approved controlled-pilot environment and resource inventory;
- immutable source revision and exact artifact digest;
- verified signed provenance and accepted signer identity;
- current vulnerability and repository-history secret-scan evidence;
- active remote telemetry, alert routing and evidence retention;
- declared workload, performance thresholds and abort conditions;
- available rollback, access revocation and external recovery procedures;
- named operator, observer, security reviewer and approver;
- explicit statement that production authority remains absent.

An unmet or unverifiable mandatory gate results in `BLOCKED`.

## Demonstrator Boundary

The demonstrator is limited to synthetic, public or explicitly approved non-production data. It must not:

- connect to production control systems;
- command physical equipment or vessels;
- expose unrestricted public ingress;
- use long-lived shared credentials;
- treat automation output as risk acceptance;
- extrapolate pilot results into production readiness.

## Required Scenario Sequence

### D-01 Release Identity and Provenance

1. Select an immutable source revision.
2. Build the candidate artifact.
3. verify artifact digest, provenance signature and signer trust.
4. Reject a deliberately modified artifact.

Expected result: only the verified artifact may proceed.

### D-02 Governed Deployment

1. Confirm accountable human approval is bound to the revision and artifact digest.
2. Deploy using least-privilege pilot identity.
3. Record deployment identity, environment, timestamp and configuration revision.
4. Verify production targets remain inaccessible.

Expected result: deployment is auditable and restricted to the approved pilot environment.

### D-03 End-to-End Functional Flow

1. Submit bounded synthetic inputs through the documented pilot interface.
2. Confirm deterministic processing and expected outputs.
3. Confirm correlation identifiers cross logs, metrics, traces and audit records.
4. Verify no prohibited side effect or authority escalation occurs.

Expected result: the bounded integration path completes with traceable evidence.

### D-04 Telemetry and Alert Delivery

1. Confirm remote export of health, security, deployment and governance signals.
2. Inject a controlled critical condition.
3. Confirm paging, acknowledgement and escalation.
4. Interrupt export and verify buffering plus pilot pause behavior.

Expected result: alert delivery and telemetry-loss controls operate as declared.

### D-05 Security Gate

1. Run dependency, source, artifact, configuration and full-history secret scans.
2. Demonstrate that a seeded critical finding blocks continuation.
3. Demonstrate that a seeded secret triggers revocation/rotation workflow.
4. Retain scanner versions, intelligence freshness and raw reports.

Expected result: security gates fail closed and exceptions require accountable human approval.

### D-06 Performance and Degradation

1. Run baseline and declared step-load profiles.
2. Capture latency, throughput, error, saturation and queue metrics.
3. Inject a dependency degradation condition.
4. Confirm warning, pause or abort thresholds trigger without retroactive relaxation.

Expected result: operating limits and degraded behavior are evidenced, not inferred.

### D-07 Rollback and Access Revocation

1. Trigger the approved rollback path.
2. Confirm prior known-good revision restoration.
3. Revoke the deployment and privileged identities.
4. Confirm revoked identities can no longer act.

Expected result: rollback and revocation complete within declared objectives with full audit evidence.

### D-08 Backup Restore and Recovery

1. Select an isolated backup by immutable identifier.
2. Restore into an approved recovery target outside the primary failure domain.
3. Verify manifest and application-level integrity.
4. Reject a corrupted backup and deny unauthorized restore/delete attempts.

Expected result: recovery evidence includes measured RPO/RTO and integrity results.

### D-09 Pilot Abort

1. Trigger a declared abort condition.
2. Confirm new work is stopped.
3. Preserve evidence and operator communication.
4. Require human authorization before any restart.

Expected result: automation cannot silently continue or self-authorize restart.

## Evidence Package

The retained package must include:

- demonstrator ID and timestamps;
- immutable source revision;
- artifact digest and signed provenance reference;
- environment and configuration revision;
- identities and roles involved;
- approval record;
- security scan results and intelligence freshness;
- raw and summarized telemetry;
- alert delivery and acknowledgement evidence;
- workload definitions and performance results;
- rollback, revocation and recovery results;
- all failures, retries, pauses and aborts;
- known limitations and unresolved risks;
- independent reviewer disposition.

Evidence must be stored in a tamper-evident or append-only location outside the primary pilot failure domain.

## Outcomes

Allowed dispositions are:

- `PASS`: all mandatory scenarios and evidence requirements succeeded;
- `PASS_WITH_LIMITATIONS`: mandatory scenarios succeeded but documented non-blocking limitations remain;
- `FAIL`: one or more mandatory scenarios failed;
- `BLOCKED`: entry gates or required evidence were unavailable.

Only an accountable human may approve the final disposition. A passing demonstrator does not itself authorize pilot activation or production deployment.

## Risk Treatment

The demonstrator consolidates evidence relevant to RR-001 through RR-005. It may support reassessment but cannot close a risk solely through documentation or simulated results. Closure requires a concrete implementation, representative execution and accountable human acceptance.