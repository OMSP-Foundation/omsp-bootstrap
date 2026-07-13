---
Artifact-ID: OMSP-GOV-ADR-0002
Title: ADR-0002 Automated Release Pipeline with Standing Human Authorization
Version: 1.0.0
Status: Active
Owner: OMSP Foundation Governance
Baseline: Sprint-6
Classification: Public
Related-Issue: WP-0090 / #213
---

# ADR-0002: Automated Release Pipeline with Standing Human Authorization

## Status

Accepted by accountable human decision (Cengiz, 2026-07-13, recorded release
instruction: "release adımlarını otomatik yapmamız gerekecek … Bu genel
kural olmalı"), delivered through WP-0090.

## Context

Through v0.5.1, release publication required a manual sequence after the
last Work Package merged: reconcile the drafted notes, publish the GitHub
Release, close the milestone, record approval. With release gates now
mechanical and measurable (`planning/WP-0075-DOMAIN-BACKLOG-REBASELINE.md`
§7) and the readiness evidence produced by the normal Work Package flow,
the manual tail duplicates checks that automation performs identically.

Options considered:

- **(A) Keep fully manual publication** — safest on paper, but the human
  steps are mechanical transcription; they add latency, not judgment.
- **(B) Fully autonomous release** (automation decides when to release) —
  rejected: it removes the human release decision entirely, conflicting
  with the accountability principle.
- **(C) Standing authorization with a human trigger** — the act of
  **closing a release milestone** is the recorded human release decision;
  everything after (final verification, notes assembly, publication)
  executes automatically, and only if every mechanical gate passes.

## Decision

Adopt **(C)**. The general rule:

```text
All milestone work closed
  → human closes the milestone            (the recorded release decision)
    → PM stage: release package assembled  (notes, changelog, evidence)
      → CTO stage: final verification run  (full mechanical gate suite)
        → GO  → release published automatically (pre-release class)
        → NO-GO → publication blocked; a blocking issue is opened
```

Binding conditions:

1. **Human trigger.** Closing a release milestone whose title carries a
   SemVer version is the accountable human release decision. No release is
   published without it.
2. **CTO verification gate (mechanical).** The pipeline must run and pass:
   governed-metadata validation on the full scope, the quality gate,
   canonical-authority validation, and the full `validate_*.py` family —
   plus version alignment of `CHANGELOG.md` and `RELEASE_NOTES.md`.
   Any failure is NO-GO: nothing is published and a blocking issue is
   opened with the run evidence.
3. **Pre-release class only.** Automation may publish releases classified
   as pre-release (the current baseline-candidate lineage). Declaring a
   production release, certification-relevant status, or any change to the
   authorized-use scope remains a direct human act.
4. **Advisory agent roles.** The `omsp-pm` agent prepares release packages
   during the closing Work Package; the `omsp-cto` agent's GO/NO-GO
   assessment is realized mechanically by the verification gate in CI. In
   interactive sessions the agents may run the same sequence, under the
   same conditions.
5. **Revocation.** This standing authorization is revoked by a single PR
   superseding this ADR (or disabling the workflow); revocation requires
   no notice period.

## Consequences

Positive: zero-latency releases once work is done; the release record
always contains machine-produced verification evidence; the human decision
is preserved but reduced to its real content (deciding that the milestone
is done).

Accepted costs and risks: a mistakenly closed milestone publishes a
pre-release — mitigated by the gate suite, the pre-release-only class, and
the ability to delete/yank a release and reopen the milestone; gate
coverage must grow with the product (each new validator family should be
added to the pipeline).

## Alternatives Considered

- (A) Fully manual — rejected as mechanical toil without added judgment.
- (B) Fully autonomous — rejected as removing the human release decision.
