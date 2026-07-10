---
Artifact-ID: OMSP-SECURITY-SUPPLY-CHAIN-0001
Title: Security and Software Supply-Chain Baseline
Version: 0.1.0
Status: Review
Owner: OMSP Engineering Council
Approvers:
  - Accountable Maintainer
Created: 2026-07-10
Last-Updated: 2026-07-10
Sprint: Sprint-5
Work-Package: WP-0051
Traceability:
  - ISSUE-85
---

# Security and Software Supply-Chain Baseline

## Purpose

This baseline defines the minimum security and software supply-chain controls for the Sprint-5 OMSP toolchain. It creates reviewable evidence; it does not certify the repository or authorize production deployment.

## Control Baseline

- workflows must declare explicit least-privilege permissions;
- write permissions require documented purpose and accountable review;
- third-party actions must include a version and should migrate from tags to immutable commit SHAs;
- secrets, private keys and credentials must not be committed or emitted into reports;
- tool dependencies and external actions must be inventoried;
- security reports, SBOM records and exceptions must remain traceable to a source revision;
- critical findings block release unless an accountable human records an approved disposition;
- generated evidence must not contain approval, release or risk-acceptance authority.

## Implemented Evidence

`tooling/omsp_security_baseline.py` produces a deterministic JSON report containing workflow digests, external action references, permission findings and potential committed-secret findings. The CI workflow also emits a minimal SBOM record. Sprint-5 Python tooling currently declares no third-party runtime packages and uses the Python standard library.

## Severity and Enforcement

- missing action versions and detected secret material are blocking errors;
- missing explicit workflow permissions, tag-pinned actions and write permissions are migration or review warnings;
- warnings must be resolved or explicitly dispositioned before WP-0056 can claim production readiness;
- a passing scan means only that implemented rules found no blocking condition.

## Current Migration Risks

Existing workflows commonly use major-version action tags such as `@v4` and `@v5`. These are inventoried as warnings rather than silently accepted as immutable provenance. Migration to reviewed commit SHAs is required before a strong supply-chain integrity claim can be made.

Some legacy workflows may lack explicit permissions. The scanner records these as migration warnings so the baseline can be introduced without hiding inherited debt. New Sprint-5 workflows use explicit `contents: read` permissions.

## Exception Process

An exception must record the finding, affected workflow or dependency, reason, compensating controls, owner, expiry or review point, and accountable approval reference. Automation may verify that an exception record exists but cannot approve it or accept residual risk.

## Incident and Revocation

A suspected credential exposure, compromised action, malicious dependency or provenance failure requires stopping affected publication/release activity, rotating exposed credentials, preserving evidence, identifying affected revisions and packages, and issuing a corrective package or rollback decision through accountable governance.

## Authority Boundary

Security automation may discover, classify and report risks. It cannot declare the system secure, approve exceptions, accept residual risk, authorize release or approve production readiness. Those decisions remain with named accountable humans.

## Known Limitations

The MVP does not perform vulnerability-database lookup, malware analysis, signed provenance verification, secret-history scanning, dependency license analysis or remote action source verification. These limitations must remain visible in release-readiness evidence.
