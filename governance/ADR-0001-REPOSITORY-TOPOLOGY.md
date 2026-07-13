---
Artifact-ID: OMSP-GOV-ADR-0001
Title: ADR-0001 Repository Topology for the MODS Product Stack — Monorepo
Version: 1.0.0
Status: Active
Owner: OMSP Foundation Governance
Baseline: Sprint-6
Classification: Public
Related-Issue: WP-0070 / #165
---

# ADR-0001: Repository Topology for the MODS Product Stack — Monorepo

## Status

Accepted by accountable human decision (Cengiz, 2026-07-13), recorded through
WP-0070. Re-evaluation is trigger-based (see Consequences).

## Context

OMSP will produce the layered MODS product stack: MODS Specification (with
the ODS-100…600 series) → Marine Diagram System → Core Operations Manual →
Vessel Definition Modules → Scenario Library → QRH.

Options considered:

- **(A) Monorepo** — continue in `omsp-bootstrap`, enforcing layer separation
  with directories, Artifact-ID classes, and validator rules.
- **(B) Multirepo** — one repository per stack layer.
- **(C) Hybrid** — foundation repository plus separate product repositories.

Decision criteria:

- single-contributor reality (one maintainer, one review authority);
- traceability tooling is path-based (`tooling/omsp_validate.py`,
  `schemas/traceability.schema.yaml`) and works within one tree;
- ~26 CI workflows are maintained in one place;
- cross-layer traceability density: the QRH → Emergency Procedure → Scenario
  → Core Operations chain would cross repository boundaries in (B)/(C),
  multiplying link-check and CI cost;
- the repository generator (WP-0049, `tooling/omsp_generate_repo.py`) already
  exists as the sanctioned downstream-derivation mechanism;
- `canon/VISION.md` §3 anticipates downstream repositories — eventually, not
  necessarily now.

## Decision

Remain a **monorepo** until v1.0 stabilization. MODS layer separation is
enforced by directory structure, Artifact-ID classes, and validator rules —
not by repository boundaries.

Downstream or second-vessel repositories are opened only when one of these
triggers occurs:

- **T1** — external contributor acceptance (community readiness block);
- **T2** — a second Vessel Definition Module needs an independent release
  cadence;
- **T3** — the MODS Specification gains consumers outside OMSP.

Derivation, when triggered, must go through the repository generator; manual
repository copies are prohibited.

## Consequences

Positive:

- one CI/validator pipeline; atomic cross-layer pull requests;
- low operating burden for a single contributor;
- traceability chains remain intact within one tree.

Negative / accepted risks:

- the repository grows (Markdown volume is low; risk limited);
- no per-layer access separation (not a real constraint with one contributor);
- a future split carries migration cost — bounded by stable Artifact-IDs and
  the generator.

This ADR is re-evaluated when any of T1–T3 occurs and is superseded by a new
ADR if the decision changes.
