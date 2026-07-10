---
Artifact-ID: OMSP-PROVENANCE-BASELINE-0001
Title: Signed Provenance and Immutable Audit Evidence Baseline
Version: 0.1.0
Status: Draft
Owner: OMSP Engineering Council
Created: 2026-07-10
Last-Updated: 2026-07-10
Sprint: Sprint-6
Work-Package: WP-0062
Traceability:
  - ISSUE-150
  - WP-0061
  - RR-002
---

# Signed Provenance and Immutable Audit Evidence Baseline

## Purpose

This baseline defines the minimum provenance, attestation, signing-key governance and tamper-evident audit controls required for controlled OMSP pilot releases.

It establishes a verification contract. It does not claim that a production signing service, hardware security module or external immutable archive has already been provisioned.

## Authority Boundary

Automation may generate digests, provenance statements, signatures, verification findings and audit records. Automation cannot approve a release, accept residual risk, authorize pilot activation or grant production authority.

## Required Provenance Chain

Every pilot candidate must link:

1. immutable source revision;
2. workflow identity and run identifier;
3. declared build inputs and tool versions;
4. generated artifacts and SHA-256 digests;
5. validation and security evidence;
6. signed provenance statement;
7. accountable human approval record.

A missing or unverifiable element blocks pilot release publication.

## Provenance Statement

The canonical machine-readable statement must contain:

- schema and statement version;
- repository and immutable commit SHA;
- branch or tag context;
- workflow, run and job identifiers;
- builder identity;
- build timestamp in UTC;
- declared inputs and dependency evidence;
- artifact names, media types, sizes and SHA-256 digests;
- validation evidence references;
- signing key identifier and signature algorithm;
- verification status;
- approval-record reference.

Mutable branch names, issue numbers and human-readable labels are supporting metadata only and cannot replace immutable identifiers.

## Signing Requirements

- pilot release provenance must be digitally signed;
- signing keys must be distinct from ordinary contributor credentials;
- private keys must not be stored in the repository, workflow logs or release artifacts;
- signing must occur only after required quality, security and environment checks succeed;
- signature verification must occur before publication and before pilot deployment;
- verification failure must fail closed;
- unsigned artifacts must be classified as preview-only and cannot enter the pilot environment.

## Key Governance

| Control | Requirement |
|---|---|
| Ownership | A named accountable key owner and backup owner are recorded. |
| Storage | Private signing material is held in an approved protected secret or signing service. |
| Access | Least privilege, MFA and auditable authorization are required. |
| Rotation | Keys are rotated on schedule and after suspected compromise. |
| Revocation | Revocation status is published and checked during verification. |
| Recovery | Loss or compromise initiates incident handling and re-signing analysis. |
| Separation | Build execution, signing authorization and release approval are separated where practicable. |

## Audit Evidence Model

Material events must be recorded as append-only or tamper-evident entries, including:

- build start and completion;
- validator and quality-gate outcomes;
- signing request and completion;
- signature verification;
- artifact publication;
- pilot deployment approval, execution, pause, rollback and revocation;
- privileged and break-glass access;
- key creation, rotation, suspension and revocation;
- human approval and risk disposition.

Each record must include UTC timestamp, event type, actor or workload identity, immutable subject reference, outcome, correlation identifier and previous-record digest or equivalent integrity control.

## Tamper-Evidence and Retention

The pilot baseline requires one of the following verified patterns:

- append-only storage with retention lock;
- write-once object retention;
- cryptographically chained event records anchored to an independently retained checkpoint;
- an equivalent control approved by the Engineering Council.

A normal mutable repository file or transient workflow log alone is insufficient.

Retention duration, access roles, export procedure and deletion authority must be declared before pilot activation.

## Verification Gates

Pilot publication and deployment must be blocked when:

- provenance is absent, malformed or references a mutable revision;
- an artifact digest does not match;
- the signature is missing, invalid, expired or revoked;
- the signer is not authorized for the declared environment;
- required audit evidence cannot be written or verified;
- a key compromise investigation is open;
- human approval is missing or does not match the immutable revision.

## Compromise and Rotation Procedure

On suspected signing-key compromise:

1. suspend affected signing operations;
2. revoke or disable the key;
3. identify all artifacts and statements signed by the key;
4. preserve incident and audit evidence;
5. determine the trust window and affected revisions;
6. rotate to a new approved key;
7. rebuild, revalidate and re-sign affected pilot artifacts where required;
8. obtain a new accountable approval decision.

Automation cannot silently replace a compromised signature or approval.

## Validation Evidence

Completion evidence must include:

- one valid signed provenance example;
- successful independent verification;
- modified-artifact verification failure;
- unauthorized-signer rejection;
- revoked-key rejection;
- simulated key rotation and compromise response;
- audit-chain integrity verification;
- evidence-retention location and access review.

## RR-002 Disposition

RR-002 remains open until a concrete signing mechanism and tamper-evident retention target are provisioned, exercised and approved. This document alone does not close RR-002.

## Production Boundary

Compliance with this pilot baseline does not prove production-grade key custody, regulatory provenance compliance, long-term archive durability or production release authorization. Those claims require separate evidence and approval.
