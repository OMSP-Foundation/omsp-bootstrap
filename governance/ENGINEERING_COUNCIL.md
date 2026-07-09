---
Artifact-ID: OMSP-GOV-ENGINEERING-COUNCIL-0001
Title: OMSP Engineering Council Charter
Version: 1.0.0
Status: Active
Owner: OMSP Engineering Council
Baseline: Sprint-1
Classification: Public
Related-Issue: WP-0013 / #35
---

# OMSP Engineering Council Charter

## 1. Purpose

The OMSP Engineering Council is the accountable technical governance body for OMSP Foundation repositories. It owns engineering lifecycle standards, architecture review, baseline readiness review, and technical decision consistency.

## 2. Responsibilities

The Engineering Council is responsible for:

- maintaining the Engineering Playbook;
- reviewing architecture-impacting changes;
- defining engineering lifecycle rules;
- reviewing baseline readiness;
- reviewing release readiness where technical integrity is involved;
- ensuring Work Package traceability;
- identifying governance gaps and follow-up issues;
- approving technical exceptions within its delegated authority.

## 3. Authority

The Engineering Council may approve or reject engineering governance changes, architecture review outcomes, baseline readiness recommendations, and technical process exceptions.

It may not override the Constitution, approve Foundation-level governance changes, or approve releases outside delegated authority.

## 4. Membership

Membership is determined by OMSP Foundation Governance or Program Ownership according to current operating needs.

Members should represent enough technical and governance understanding to evaluate:

- architecture impact;
- engineering workflow impact;
- repository safety;
- baseline readiness;
- documentation consistency;
- delivery risk.

## 5. Decision Method

Council decisions should be documented through one or more of:

- pull request review;
- issue comment;
- decision record;
- baseline note;
- release note.

Material decisions must identify the decision class, rationale, affected artifacts, and follow-up work.

## 6. Architecture Review

Architecture review is required when a Work Package materially affects:

- system structure;
- repository structure;
- lifecycle governance;
- interface contracts;
- baseline or release behavior;
- security, reliability, or operational posture.

Architecture review must confirm consistency with current governance artifacts and identify any required documentation updates.

## 7. Baseline Readiness Review

Before a baseline is approved, the Engineering Council must review:

- merged Work Packages;
- unresolved technical risks;
- governance artifact consistency;
- validation evidence;
- release or baseline notes;
- whether known gaps are documented.

The Council may recommend baseline approval, request changes, or defer the baseline.

## 8. Review Outcomes

Review outcomes may be:

- **Approved**: work is acceptable as submitted.
- **Approved with Follow-up**: work may proceed, but follow-up issues are required.
- **Changes Requested**: work must be updated before approval.
- **Deferred**: decision is postponed due to missing information or unresolved dependency.
- **Rejected**: work conflicts with governance or technical direction.

## 9. AI Assistance

AI may assist the Council by drafting review notes, identifying inconsistencies, summarizing diffs, and preparing decision records. AI may not cast approval votes or replace accountable human review.

## 10. Maintenance

This charter is maintained by the Engineering Council through issue-backed Work Packages and reviewed pull requests.
