# OMSP Foundation

> **Open Maritime Systems Platform**  
> A knowledge-first, model-driven engineering foundation for maritime operations.

OMSP Foundation is the starting point for building an open, traceable and architecture-driven systems engineering platform for maritime operational knowledge.

---

## Project Status

| Item | Status |
| --- | --- |
| Repository | Foundation Repository |
| Current Release | `v0.1.0-foundation-sprint-1` |
| Current Sprint | Sprint-1 Completed / Sprint-2 Planned |
| Development Branch | `develop` |
| Work Package Flow | Issue → Branch → Commit → Draft PR → Review → Merge |

---

## What is OMSP?

OMSP, the **Open Maritime Systems Platform**, is an open, model-based and knowledge-first engineering platform for maritime operations.

It is designed to connect requirements, architecture, domain knowledge, validation evidence, documentation and implementation into a coherent engineering lifecycle. OMSP is not only a software project; it is an engineering knowledge system intended to make maritime operational systems more understandable, traceable, reusable and governable.

---

## Why OMSP?

Maritime operations involve complex interactions between vessels, crews, procedures, equipment, regulations, safety constraints, maintenance activities and operational environments. These elements are often documented separately, making it difficult to reason about the whole system.

OMSP addresses this by establishing a foundation where:

- knowledge is treated as a first-class engineering asset;
- models are created before implementation details;
- decisions are captured and reviewed;
- requirements, architecture and evidence remain traceable;
- documentation is structured for both humans and automation;
- AI-assisted engineering can operate on governed artifacts.

---

## Vision

To become an open, model-based, knowledge-first systems engineering platform for maritime operations.

## Mission

To provide an open engineering foundation that enables interoperable, traceable and reusable maritime operational knowledge.

---

## Core Engineering Principles

OMSP follows a small set of stable engineering principles:

1. **Knowledge First** — domain knowledge is captured, structured and maintained as an engineering asset.
2. **Models Before Code** — implementation follows explicit models, standards and decisions.
3. **Architecture Driven** — system structure and responsibility boundaries are made explicit.
4. **Traceability by Design** — requirements, artifacts, decisions and validation evidence are connected.
5. **Evidence Based Engineering** — important claims should be supported by reviewable evidence.
6. **Automation by Default** — repeatable engineering checks should become automated quality gates.
7. **Open Standards** — the platform should prefer open formats, clear interfaces and portable knowledge.
8. **AI Assisted Engineering** — AI may assist with drafting, analysis and validation, but governance remains human-led.

---

## Repository Overview

This repository contains the initial OMSP foundation artifacts. It defines the governance, standards, schemas, templates, canonical language, platform concepts, validation approach and reference structure required for future OMSP repositories.

| Area | Purpose |
| --- | --- |
| `.github/` | GitHub workflows, templates and repository automation |
| `governance/` | Engineering governance, review, release and decision policies |
| `foundation/` | Core engineering standards for artifacts, metadata and traceability |
| `schemas/` | Machine-readable schema foundations |
| `templates/` | Reusable engineering artifact templates |
| `canon/` | Vision, mission, principles, terminology and ontology overview |
| `platform/` | Initial platform component definitions |
| `validation/` | Quality gates, verification and validation foundations |
| `release/` | Baseline, release readiness, release notes and approval records |
| `reference/` | Reference examples and future domain-specific material |
| `tooling/` | Scripts, validators and generators |
| `docs/` | Repository-level documentation and navigation |
| `roadmap/` | Sprint and program roadmap artifacts |

---

## Documentation Center

Start here:

| Document | Purpose |
| --- | --- |
| `docs/GETTING_STARTED.md` | First steps for readers, contributors and maintainers |
| `docs/REPOSITORY_OVERVIEW.md` | Repository intent, scope and structure |
| `docs/ARCHITECTURE_OVERVIEW.md` | Foundation architecture and main building blocks |
| `docs/NAVIGATION.md` | Documentation map and recommended reading paths |
| `PROJECT_STRUCTURE.md` | Directory-by-directory repository structure |
| `roadmap/OMSP_ROADMAP.md` | OMSP roadmap and sprint evolution |
| `governance/ENGINEERING_PLAYBOOK.md` | Official engineering workflow and lifecycle |
| `release/RELEASE_NOTES_SPRINT_1.md` | Sprint-1 foundation release notes |
| `release/SPRINT_1_BASELINE_MANIFEST.md` | Sprint-1 baseline manifest |

---

## Getting Started

For readers new to OMSP:

1. Read this README to understand the purpose of the repository.
2. Open `docs/GETTING_STARTED.md` for the recommended first steps.
3. Review `governance/ENGINEERING_PLAYBOOK.md` to understand how work is managed.
4. Review `foundation/` to understand artifact, metadata and traceability standards.
5. Use `templates/` when creating new governed engineering artifacts.

For contributors:

1. Pick or create an issue.
2. Create a feature branch using the Work Package identifier.
3. Make focused commits.
4. Open a Draft Pull Request against `develop`.
5. Complete review and merge only after acceptance criteria are satisfied.

---

## Engineering Workflow

OMSP uses a governed Work Package workflow:

```text
Backlog
  ↓
Issue
  ↓
Feature Branch
  ↓
Implementation
  ↓
Commit(s)
  ↓
Draft Pull Request
  ↓
Architecture Review
  ↓
Ready for Review
  ↓
Approval
  ↓
Merge → develop
  ↓
Issue Closed
  ↓
Baseline Update
```

Normal work is not committed directly to `develop` or `main`.

---

## Branch and Commit Conventions

Feature branches use the Work Package identifier:

```text
feature/wp-0011-repository-modernization
feature/wp-0012-engineering-playbook-v1
feature/wp-0019-github-quality-gates
```

Commit messages follow Conventional Commits:

```text
docs(readme): modernize repository landing page
docs(repository): add documentation center
ci(validation): add markdown validation workflow
chore(release): prepare v0.2.0-foundation
```

---

## Sprint Roadmap

| Sprint | Status | Goal |
| --- | --- | --- |
| Sprint-0 | Completed | Bootstrap foundation and repository skeleton |
| Sprint-1 | Completed | Production-quality Foundation Repository |
| Sprint-2 | Planned | Engineering models and structured artifacts |
| Sprint-3 | Planned | Knowledge platform foundations |
| Sprint-4 | Planned | Digital twin foundation |
| Sprint-5 | Planned | Production platform readiness |

---

## OMSP Ecosystem

This repository is the foundation for a broader OMSP ecosystem.

Planned repository families include:

```text
OMSP Foundation
├── omsp-bootstrap
├── omsp-core
├── omsp-ontology
├── omsp-models
├── omsp-validation
├── omsp-reference
├── omsp-tools
└── omsp-docs
```

The purpose of `omsp-bootstrap` is to define the engineering baseline from which those repositories can grow.

---

## Governance

OMSP governance is led by the **OMSP Engineering Council**. Governance artifacts define how decisions are made, reviewed and released.

Key governance documents:

- `governance/ENGINEERING_PLAYBOOK.md`
- `governance/GOVERNANCE_MODEL.md`
- `governance/ENGINEERING_COUNCIL.md`
- `governance/DECISION_POLICY.md`
- `governance/REVIEW_POLICY.md`
- `governance/RELEASE_POLICY.md`

---

## Contributing

OMSP contributions should preserve traceability, reviewability and engineering quality.

Minimum contribution expectations:

- create or reference an issue;
- use a Work Package branch;
- keep changes focused;
- update documentation when behavior, structure or governance changes;
- open a Pull Request against `develop`;
- include acceptance criteria and related issue links.

See `.github/CONTRIBUTING.md` and `governance/ENGINEERING_PLAYBOOK.md` for the formal workflow.

---

## Releases

Current release candidate baseline:

```text
v0.1.0-foundation-sprint-1
```

This release closes Sprint-1 and captures the first production-quality OMSP foundation baseline.

Sprint-2 is planned to introduce engineering models and structured artifact systems.

---

## License

This repository is licensed under the terms defined in `LICENSE`.

---

## Acknowledgements

OMSP is built as an open engineering effort for maritime operations, systems thinking, model-based engineering and knowledge-first product development.
