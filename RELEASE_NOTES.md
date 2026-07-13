# OMSP Foundation Release Notes — v0.5.0

**Release date:** 2026-07-10  
**Classification:** Production Baseline Candidate  
**Approval status:** Approved with conditions  
**Authorized scope:** Controlled pre-production and pilot evaluation

## Overview

`v0.5.0` closes Sprint-5 and establishes the first OMSP baseline that combines governed engineering foundations with executable validation, generation, publication, security, observability and recovery tooling.

This baseline is suitable for controlled pre-production and pilot evaluation. It is not an authorized production release and does not grant production deployment, unrestricted external publication, autonomous operational authority, certification or automatic residual-risk acceptance.

## Notable Outcomes

- deterministic governed-artifact validation with stable findings and machine-readable reports;
- reproducible repository generation with dry-run and overwrite protections;
- preview, baseline and release publication channels with manifests and checksums;
- software supply-chain evidence covering workflow permissions, action references, secret patterns and SBOM output;
- a unified CI/CD quality gate preserving component evidence and human approval boundaries;
- structured JSONL audit events, correlation identifiers, health evidence and sensitive-data redaction;
- an end-to-end integration demonstrator linking generation, validation, publication preview, security and audit evidence;
- incident classification, escalation, rollback, restore and recovery guidance;
- an exercised recovery drill and production-readiness assessment;
- accountable human approval records and an explicit residual-risk register.

## Compatibility and Usage

The Sprint-5 executable tooling targets Python 3.12 in CI and uses Python standard-library dependencies only. Governed Markdown metadata, JSON profiles, manifests and evidence records remain the primary interfaces.

Consumers must preserve artifact identity, lifecycle status, provenance and approval evidence. Preview output must not be represented as an approved baseline or release.

## Approval Boundary

The accountable approval for `v0.5.0` permits controlled pre-production and pilot evaluation only.

The following remain separately governed decisions:

- production deployment;
- unrestricted external publication;
- residual-risk acceptance;
- operational use against a physical vessel;
- certification, regulatory acceptance or seaworthiness claims;
- autonomous or safety-critical control authority.

Automation and AI assistance may produce evidence and recommendations but cannot originate these decisions.

## Known Limitations

The following capabilities remain deferred or incomplete:

- production environment approval and deployment controls;
- signed provenance, attestations and cryptographically signed audit evidence;
- remote telemetry, alert delivery, paging and long-term evidence storage;
- vulnerability-database intelligence and repository-history secret scanning;
- performance, capacity, availability and endurance qualification;
- external backup infrastructure and disaster-recovery validation;
- production rollback targets and environment-specific operational procedures.

Persistent risks `RR-001` through `RR-005` must be reassessed through the Sprint-6 governed risk plan before any production-release decision.

## Sprint-6 Direction

Sprint-6 focuses on controlled pilot readiness. Planned work includes:

- root release-document alignment and repository-status reconciliation;
- persistent-risk reassessment with owners, triggers and evidence requirements;
- controlled pilot scope, environment and entry/exit criteria;
- stronger provenance, security, telemetry, performance and recovery evidence;
- a reproducible pilot validation package;
- accountable human approval before pilot activation.

Planned Sprint-6 work is not part of the delivered `v0.5.0` baseline until implemented, reviewed and approved.

## Governed References

- GitHub Releases — release notes, baseline approval and readiness records per tag
- GitHub Projects, Issues and Milestones — sprint, Work Package and release tracking
- `operations/OPERATIONS_INCIDENT_RECOVERY_RUNBOOK.md`
- `security/SECURITY_SUPPLY_CHAIN_BASELINE.md`
- `demonstrator/PLATFORM_INTEGRATION_DEMONSTRATOR.md`
