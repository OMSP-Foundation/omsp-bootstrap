# OMSP Foundation

> **Open Maritime Systems Platform**  
> A knowledge-first, model-driven engineering foundation for maritime operations.

OMSP Foundation provides the governed standards, models, tooling and evidence needed to build traceable maritime engineering systems. This repository is the foundation baseline for the wider OMSP ecosystem.

---

## Project Status

| Item | Status |
| --- | --- |
| Repository | Foundation Repository |
| Current Governed Baseline | `v0.5.2` (process-automation patch on the `v0.5.1` clean baseline) |
| Baseline Classification | Clean Baseline — Production Baseline Candidate lineage |
| Authorized Use | Controlled pre-production and pilot evaluation |
| Production Deployment | Not authorized |
| Completed Sprint | Sprint-6 |
| Current Planning Horizon | Sprint-7 — Maritime Domain Model Foundation (v0.6.0, epic #171) |
| Development Branch | `develop` |
| Work Package Flow | Issue → Branch → Commit → Draft PR → Review → Merge |

`v0.5.2` is a process-automation patch on the `v0.5.1` clean baseline, in the approved-with-conditions candidate lineage. It is not a production release and does not authorize production deployment, unrestricted external publication, autonomous operational authority or automatic residual-risk acceptance.

---

## What OMSP Provides

OMSP connects governed engineering knowledge, architecture, models, validation evidence, automation and publication into one traceable lifecycle. The current baseline includes:

- governance, decision, review, metadata and traceability standards;
- formal ontology and semantic relationship foundations;
- platform engine architecture and context models;
- artifact registry, knowledge graph and AI-readable processing contracts;
- vessel, equipment, operational scenario and digital-twin reference models;
- deterministic validator and repository-generator tooling;
- governed preview, baseline and release publication workflows;
- integrated CI/CD quality gates and security baseline checks;
- structured operational observability and audit evidence;
- an end-to-end platform integration demonstrator;
- incident, recovery and release-readiness evidence.

OMSP remains a governed engineering foundation. Physical-vessel applicability, production runtime deployment, certification, regulatory acceptance, seaworthiness and operational control require separate evidence and accountable approval.

---

## Core Engineering Principles

1. **Knowledge First** — domain knowledge is maintained as an engineering asset.
2. **Models Before Code** — implementation follows explicit models and decisions.
3. **Architecture Driven** — responsibilities and system boundaries are visible.
4. **Traceability by Design** — artifacts, decisions and evidence remain linked.
5. **Evidence-Based Engineering** — material claims require reviewable evidence.
6. **Automation by Default** — repeatable checks become deterministic quality gates.
7. **Open Standards** — formats and interfaces should remain portable and inspectable.
8. **Human-Led Governance** — AI and automation may assist but cannot originate approval authority.

---

## Repository Areas

| Area | Purpose |
| --- | --- |
| `.github/` | Workflows, templates and repository automation |
| `governance/` | Canonical governance, decision, review and engineering standards |
| `canon/` | Vision, mission, principles, terminology, methodology and ontology overview |
| `ontology/` | Formal ontology and evolution policy |
| `architecture/` | Platform, engine, context, traceability and publication architecture |
| `knowledge/` | Knowledge graph, registry, AI-processing and publication contracts |
| `reference/` | Vessel, equipment, scenario and digital-twin reference models |
| `validation/` | Verification, validation, quality-gate and checklist foundations |
| `schemas/` | Machine-readable schemas and contracts |
| `templates/` | Reusable governed artifact templates |
| `tooling/` | Validators, generators, publication and evidence tooling |
| `security/` | Security and software supply-chain baseline |
| `operations/` | Observability, audit, incident and recovery models |
| `demonstrator/` | End-to-end integration demonstrator documentation |
| `planning/` | Sprint execution plans |
| `roadmap/` | Program roadmap and horizon status |
| `docs/` | Repository guidance and navigation |

---

## Start Here

| Document | Purpose |
| --- | --- |
| `docs/GETTING_STARTED.md` | First steps for readers and contributors |
| `docs/REPOSITORY_OVERVIEW.md` | Repository purpose and structure |
| `docs/ARCHITECTURE_OVERVIEW.md` | Architecture summary |
| `docs/NAVIGATION.md` | Recommended reading paths |
| `governance/ENGINEERING_PLAYBOOK.md` | Governed engineering workflow |
| `governance/CANONICAL_AUTHORITY_MAP.md` | Canonical standard authority map |
| `planning/WP-0075-DOMAIN-BACKLOG-REBASELINE.md` | Sprint 7–14 product-led backlog and release gates |
| `planning/WP-0074-GOLDEN-PATH-DEFINITION.md` | Canonical first golden path (Hanse 460 electrical) |
| `RELEASE_NOTES.md` | Governed `v0.5.2` release notes |
| GitHub Releases & Projects | Release records, baseline approvals, issue and milestone tracking |
| `roadmap/OMSP_ROADMAP.md` | Roadmap and sprint evolution |

---

## Engineering Workflow

```text
Backlog → Issue → Feature Branch → Implementation → Commit(s)
        → Draft Pull Request → Validation → Human Review → Merge to develop
        → Issue Closure → Baseline / Release Decision
```

Normal work is not committed directly to `develop` or `main`. Feature branches use Work Package identifiers, for example:

```text
feature/wp-0058-v050-root-release-docs
feature/wp-0059-persistent-risk-reassessment
feature/wp-0060-sprint-6-controlled-pilot-plan
```

Automation may validate, report and recommend. It cannot approve a pull request, accept risk, authorize publication, approve a baseline or authorize deployment.

---

## Sprint Roadmap

| Sprint | Status | Goal |
| --- | --- | --- |
| Sprint-0 | Completed | Bootstrap repository and initial foundation |
| Sprint-1 | Completed | Governance and engineering foundation |
| Sprint-2 | Completed | Ontology, platform architecture and automation design |
| Sprint-3 | Completed | Knowledge platform foundations |
| Sprint-4 | Completed | Vessel and digital-twin reference foundation |
| Sprint-5 | Completed | Executable tooling and production-readiness candidate |
| Sprint-6 | Completed | Post-audit product reorientation and v0.5.1 clean baseline |
| Sprint-7 | Planning | Maritime domain model foundation (ontology, schemas, MODS Spec v0.1) |

---

## Release Status

The current governed baseline is:

```text
v0.5.2
```

It is approved for controlled pre-production and pilot evaluation only. Persistent risks `RR-001` through `RR-005` and the following production gaps remain open (each with a recorded re-entry trigger in `planning/WP-0075-DOMAIN-BACKLOG-REBASELINE.md` §8):

- production environment approval;
- signed provenance and attestations;
- remote telemetry, alerting and long-term evidence storage;
- vulnerability intelligence and history-level secret scanning;
- performance and capacity qualification;
- external backup and disaster-recovery validation.

See `RELEASE_NOTES.md`, `CHANGELOG.md` and the corresponding GitHub Release and Project records for the authoritative scope and limitations. Release, baseline and milestone tracking is managed on GitHub (Releases, Issues, Milestones and Projects), not in a repository folder.

---

## Contributing

Contributions must preserve traceability, reviewability and accountable authority:

- reference a GitHub issue and Work Package;
- use a focused feature branch;
- include relevant tests and validation evidence;
- update affected documentation and traceability records;
- open a pull request against `develop`;
- keep human approval boundaries explicit.

See `.github/CONTRIBUTING.md` and `governance/ENGINEERING_PLAYBOOK.md`.

---

## License

This repository is licensed under the terms defined in `LICENSE`.
