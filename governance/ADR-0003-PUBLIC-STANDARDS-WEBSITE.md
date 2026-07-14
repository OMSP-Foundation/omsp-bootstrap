---
Artifact-ID: OMSP-GOV-ADR-0003
Title: ADR-0003 Public Standards Website — Platform, Repository and Content Sync
Version: 1.0.0
Status: Active
Owner: OMSP Foundation Governance
Baseline: Sprint-7 candidate
Classification: Public
Related-Issue: WP-0091 / #235
Traceability:
  - OMSP-GOV-ADR-0001
  - OMSP-PUBLICATION-PIPELINE-0001
---

# ADR-0003: Public Standards Website — Platform, Repository and Content Sync

## Status

Accepted by accountable human decision (Cengiz, 2026-07-14, recorded
instruction: "ADR-0003 kabul ediyorum", logged on issue #235), delivered
through WP-0091. Acceptance is the gate for opening the website repository
(WP-0091 Phase 2); nothing was created or published before that recorded
decision.

## Context

OMSP is positioned as an **open standard**: anyone must be able to read the
MODS Specification, the governed standards, and the supporting documentation,
and learn how to adopt or contribute. Today the only public surface is the
raw GitHub repository, which is optimized for engineering traceability, not
for reading. A public website is required.

Constraints and forces:

- `omsp-bootstrap` is a **monorepo by accepted decision**
  (`governance/ADR-0001-REPOSITORY-TOPOLOGY.md`): governed content lives in
  one tree, and manual repository copies are prohibited. The website must
  therefore be a **derived publication surface**, never a second source of
  truth. This ADR does not supersede ADR-0001; it anticipates its T3 trigger
  (MODS consumers outside OMSP) on the publication side only.
- Governed artifacts are Markdown with YAML front matter carrying
  `Classification` metadata — a machine-checkable publish filter already
  exists.
- The publication pipeline MVP (`publication/PUBLICATION_PIPELINE_MVP.md`,
  `OMSP-PUBLICATION-PIPELINE-0001`) already defines `preview` / `baseline` /
  `release` channels; the website is the first public consumer of that
  channel model.
- Repository tooling is Python (`tooling/omsp_validate.py` and the
  `validate_*.py` family); a single maintainer operates ~24 CI workflows.
  Every additional toolchain is a real maintenance cost.
- The Marine Diagram System produces text-based diagram sources
  (Mermaid/PlantUML); the site must render Mermaid natively.
- Open-format rule (`governance/AI_GOVERNANCE.md` §7): artifacts must remain
  usable as plain text; the website stack must not make content depend on a
  proprietary platform.
- Future needs: Turkish/English audiences (i18n), per-release versioned
  documentation, full-text search.

Decision criteria: Markdown-native rendering (including YAML front matter
tolerance), toolchain alignment with the existing Python tooling, built-in
search, versioned docs, i18n path, Mermaid support, org-owned zero-cost
hosting, and lowest operating burden for a single maintainer.

## Decision

1. **Separate repository.** Open `OMSP-Foundation/omsp-website` as a public
   repository containing only the site: theme/configuration, landing and
   navigation content, sync scripts, and CI. It carries **no governed
   artifacts**; `omsp-bootstrap` remains the single source of truth.
2. **Platform: MkDocs + Material theme**, with `mike` for per-release doc
   versioning. Python-based (aligns with existing tooling), Markdown-native,
   built-in search and Mermaid rendering, mature i18n plugin ecosystem,
   maintained by a single `mkdocs.yml`.
3. **Hosting and CI/CD: GitHub Pages deployed by GitHub Actions** in the
   website repository. Org-owned, no external vendor, custom domain
   attachable later without migration.
4. **Content sync — pull at build time, never copy:**
   - the site build checks out `omsp-bootstrap` read-only and ingests only
     artifacts whose front matter carries `Classification: Public`;
   - **stable** docs are built from the latest release tag (publication
     `release` channel); a clearly-labeled **preview** version is built from
     `develop` (publication `preview` channel), versioned via `mike`;
   - triggers: `repository_dispatch` sent by `omsp-bootstrap` on merge to
     `develop` and on release publication (so even the smallest merged change
     propagates automatically), plus manual `workflow_dispatch` and a weekly
     scheduled rebuild as a safety net. The dispatch secret follows the
     existing cross-repo token pattern (`PROJECT_TOKEN` precedent).
5. **Stewardship.** The `omsp-web-steward` agent
   (`.claude/agents/omsp-web-steward.md`) owns editorial curation and
   sync-health monitoring, advisory-only. Mechanical propagation is CI's
   job; the agent never approves and never publishes.

Re-evaluation triggers (superseding ADR required if the decision changes):

- **W1** — the site needs interactive applications (model viewers, live
  diagram exploration) beyond static rendering → re-evaluate toward Astro.
- **W2** — i18n or branding requirements exceed MkDocs Material's
  capabilities.
- **W3** — ADR-0001 is superseded (repository topology change) — the sync
  source model must be re-decided.

## Consequences

Positive:

- standards become readable by anyone without GitHub literacy; adoption and
  contribution paths get a public front door;
- single source of truth is preserved mechanically (build-time pull +
  `Classification: Public` filter), so the site can never fork the standard;
- one additional `pip`-managed toolchain instead of a new language ecosystem;
- release-versioned docs give consumers a stable citation target per SemVer
  release.

Accepted costs and risks:

- a second repository to operate (CI, secrets, dependency updates) — bounded
  by the site repo carrying no governed content;
- a cross-repo dispatch token to provision and rotate;
- `develop`-based preview publishes pre-release content — mitigated by the
  explicit preview labeling and the `Classification: Public` filter;
- MkDocs Material theming limits are accepted until trigger W1/W2 fires.

## Alternatives Considered

- **Astro Starlight** — excellent modern docs framework; rejected for now
  because it adds a Node toolchain to a Python-tooled, single-maintainer
  program without a current need for its flexibility (revisited under W1/W2).
- **Docusaurus** — versioning and i18n are strong, but React-centric with a
  heavier build and maintenance profile than the need justifies.
- **Hugo** — very fast builds (irrelevant at this volume); weaker
  docs-oriented feature set out of the box; Go templating adds friction.
- **Jekyll / bare GitHub Pages** — minimal setup but weak search,
  versioning, and navigation for a multi-layer standards library.
- **Publishing from a directory inside `omsp-bootstrap`** — avoids a second
  repo but mixes publication CI into the already ~24-workflow monorepo,
  couples site deploys to content CI, and blurs the governed/derived
  boundary the publication pipeline is built on.
