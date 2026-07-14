---
Artifact-ID: OMSP-GOV-AI-GOVERNANCE-0001
Title: AI Governance
Version: 1.3.0
Status: Active
Owner: OMSP Foundation Governance
Baseline: Sprint-6
Classification: Public
Related-Issue: WP-0073 / #167, #218, #221, #235
Traceability:
  - OMSP-CANON-PRINCIPLES-0001
  - OMSP-CANON-PHILOSOPHY-0001
  - OMSP-GOV-PLAYBOOK-0001
  - OMSP-VAL-VALIDATION-0001
---

# AI Governance

## 1. Purpose and Canonical Authority

This artifact is the **single canonical entry point** for how AI may assist
OMSP engineering without replacing human authority, approval, or
accountability. Context-specific AI rules elsewhere in the repository are
applications of this artifact, not competing authorities:

| Context | Application artifact |
| --- | --- |
| Engineering lifecycle | `governance/ENGINEERING_PLAYBOOK.md` §15 |
| Validation work | `validation/VALIDATION_FRAMEWORK.md` §11 |
| Digital-twin work | `reference/DIGITAL_TWIN_AI_ASSISTANCE_BOUNDARIES.md` |
| Every pull request | `.github/PULL_REQUEST_TEMPLATE.md` — AI Assistance Boundary section |
| Agent definitions | `.claude/agents/` (omsp-cto, omsp-pm, omsp-domain-engineer, omsp-tester, omsp-auditor, omsp-web-steward) |

If an application artifact appears to conflict with this artifact, this
artifact prevails and the conflict must be raised as an issue.

## 2. Principle Basis

Grounded in canon: AI assistance is human-governed
(`canon/PRINCIPLES.md` §2.10, `canon/PHILOSOPHY.md` §5). Automation reduces
repetitive work; accountability remains with named humans. In OMSP the
accountable human authority is the repository owner (Cengiz, `toss-cengiz`)
unless governance explicitly names another role.

## 3. Permitted AI Assistance Roles

AI may, under the conditions in §6:

- draft artifacts, issues, branches, PR content, and documentation;
- analyze diffs, repositories, and evidence; identify inconsistencies;
- propose plans, requirements, risk analyses, and validation notes;
- run and summarize deterministic validators and quality gates;
- prepare review checklists, comparisons, and impact analyses;
- prepare approval packages and recommendations for human decision;
- generate clearly-labeled simulated test data;
- execute mechanical repository operations explicitly instructed and
  reviewable through normal workflow (commits on work branches, opening PRs,
  issue metadata edits recorded with audit comments);
- open and schedule issues autonomously in the project-manager role
  (omsp-pm): side findings and newly discovered needs may be captured as
  issues and placed into the current sprint or the backlog by severity,
  each issue recording its delegation source (#221; Cengiz, 2026-07-13
  session instruction);
- execute the delegated merge act in the project-manager role (omsp-pm)
  on the test-gated path only — after both gate labels and green CI —
  under the conditions and override rights of §5 item 1.

## 4. Prohibited Roles (Non-Delegable Authority)

AI must not, regardless of instruction source:

- approve governance, architecture, baseline, release, or validation
  authority — "approved", "ready", "authorized" are human-only declarations;
- merge to protected branches, publish releases, or accept residual risk;
- invent, fabricate, or conceal evidence; claim validation not performed;
- silently expand scope or modify authoritative records;
- issue vessel-control, navigation, emergency, or maintenance commands;
- declare seaworthiness, certification, regulatory compliance, or any
  external authority's position;
- override an accountable human decision or an approved procedure.

The ontology encodes this boundary: the `approves` relation may only
originate from accountable human actors (`ontology/OMSP_ONTOLOGY.md` §6).

## 5. Mandatory Human Approval Gates

The following always require explicit, recorded human approval:

1. merge of any pull request into `develop` or `main` — with one governed
   delegation: under `governance/ENGINEERING_PLAYBOOK.md` §5.8–5.9 (recorded
   in issue #212 and extended in issue #221; source: Cengiz, 2026-07-13
   session instruction), a pull request into `develop` carrying both
   `gate:tester-approved` and `gate:cto-approved` with all CI checks green
   is merged by `omsp-pm` as a delegated mechanical act recorded on the PR;
   the owner retains override at any time by removing a gate label, closing
   the pull request, or revoking the delegation; every other merge path
   remains a direct human act;
2. baseline declaration and release publication — with one governed
   delegation: under `governance/ADR-0002-AUTOMATED-RELEASE-PIPELINE.md`,
   the human act of closing a release milestone is the recorded release
   decision, after which the automated pipeline verifies and publishes
   the **pre-release-class** release without further approval, provided
   every mechanical gate passes; production-release declarations and any
   change to authorized-use scope remain direct human acts;
3. canonical authority changes (`governance/CANONICAL_AUTHORITY_MAP.md`);
4. artifact status promotion to `Active` for normative artifacts;
5. deletion or retirement of governed artifacts and directories;
6. residual-risk acceptance and safety-relevant dispositions;
7. issue closure that asserts acceptance criteria are met;
8. anything the PR template's AI Assistance Boundary section covers.

Approval must be attributable: a merge, an issue comment, or a recorded
instruction from the accountable human. AI restating an approval is not an
approval.

## 6. Provenance, Attribution, and Generated-Artifact Status

- AI-assisted commits carry an attribution trailer
  (`Co-Authored-By: Claude ...`); the human author remains responsible.
- Every PR declares AI involvement in the AI Assistance Boundary section.
- Material AI-assisted output must remain reviewable, preserve links to
  source evidence, state assumptions and uncertainty, and label simulated
  or generated content.
- AI-drafted normative artifacts enter as `Draft` or `Review`; promotion to
  `Active` is a human gate (§5.4). Where merge review itself is the
  promotion decision, the PR must say so explicitly.
- Evidence used for acceptance must be reproducible (commands, validator
  output) — never a bare AI assertion.

## 7. Data, Model, and Dependency Boundaries

- No credentials, personal data beyond public repository identity, or
  non-public third-party content may be introduced into governed artifacts.
- Copyrighted manufacturer documentation is referenced by source register
  entry (`reference/HANSE_460_SOURCE_REGISTER.md`), not reproduced.
- Outputs must not depend on a specific AI vendor or model to remain
  usable: governed artifacts stand alone as plain text (open-format rule).
- Technical claims about external standards or equipment must cite a
  verifiable source; unverified values are marked as unsourced.

## 8. Error Responsibility and Escalation

- AI output is advisory; acting on it is a human decision, and
  responsibility for merged content rests with the human approver.
- Discovered AI-introduced errors are corrected through normal issue-backed
  workflow — never silent rewrites of history.
- AI-assisted output must be rejected or marked `indeterminate` when
  evidence cannot be resolved, uncertainty is hidden, authority is
  ambiguous, or output could be mistaken for an operational instruction
  (`reference/DIGITAL_TWIN_AI_ASSISTANCE_BOUNDARIES.md` failure rules).

## 9. Runtime Boundary

This artifact governs engineering assistance only. Any use of AI in an
operational or runtime context (onboard advice, monitoring, alerting)
requires a separate, explicit approval package covering model identity,
test evidence, failure behavior, human override, and operating envelope.
No current artifact grants that approval.

## 10. Maintenance

Maintained through issue-backed Work Packages and reviewed pull requests.
Material changes require governance review and version metadata update.
This version consolidates the placeholder relocated in WP-0072 and closes
the AI-governance gap recorded in the WP-0070 audit disposition (F7).
Version 1.2.0 (#218) records the test-gated merge delegation of issue #212
in §5, and completes the agent list in §1 with `omsp-tester` and the new
`omsp-domain-engineer`. Version 1.3.0 (WP-0091, #235) registers
`omsp-web-steward`, the advisory keeper of the public standards website
(`governance/ADR-0003-PUBLIC-STANDARDS-WEBSITE.md`); it holds no gate or
publication authority. Version 1.3.0 also records the process-delegation
extensions of issue #221 (source: Cengiz, 2026-07-13 session instruction):
autonomous issue opening and the test-gated merge act by `omsp-pm` (§3, §5.1),
the pre-implementation checklist rule, and the lightweight CTO gate — the two
changes landed independently on the same day and share this version.
