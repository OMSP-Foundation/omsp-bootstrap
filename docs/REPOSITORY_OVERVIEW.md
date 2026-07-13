# Repository Overview

## Purpose

`omsp-bootstrap` is the foundation repository for the Open Maritime Systems Platform. Its purpose is to define the baseline engineering system used to create, govern, validate and evolve OMSP artifacts.

This repository is not only a code container. It is an engineering knowledge base that establishes how OMSP work is structured, reviewed and released.

## Scope

The repository covers:

- engineering governance;
- Work Package lifecycle;
- repository standards;
- artifact standards;
- metadata and traceability standards;
- canonical terminology;
- ontology meta-model and canon-ontology mapping;
- platform architecture foundations and engine designs;
- knowledge platform concepts (artifact registry, knowledge graph, AI-readable processing contract);
- validation and verification foundations;
- publication pipeline and repository generator MVPs;
- operations and assurance baselines (security, provenance, recovery, observability, performance, risk);
- controlled pilot environment and integration demonstrators;
- reference material;
- sprint planning and execution records;
- release and baseline management.

## Out of Scope

This repository does not yet implement the full runtime platform. Runtime components, maritime-specific domain models and production ontology services will be developed in later OMSP repositories and sprints. The ontology content in this repository is a generic meta-model, not yet a maritime domain ontology.

## Primary Audiences

The repository is intended for:

- OMSP maintainers;
- maritime systems engineers;
- architects;
- contributors;
- AI-assisted engineering agents;
- future OMSP repository owners.

## Repository Role in the OMSP Ecosystem

`omsp-bootstrap` provides the foundation for future repositories such as:

- `omsp-core`;
- `omsp-ontology`;
- `omsp-models`;
- `omsp-validation`;
- `omsp-reference`;
- `omsp-tools`;
- `omsp-docs`.

## Information Architecture

The repository is organized around stable engineering concerns:

| Concern | Directory |
| --- | --- |
| Governance | `governance/` |
| Standards | `governance/` |
| Schemas | `schemas/` |
| Templates | `templates/` |
| Canonical language | `canon/` |
| Ontology meta-model | `ontology/` |
| Platform concepts | `architecture/` |
| Architecture designs | `architecture/` |
| Knowledge platform | `knowledge/` |
| Validation | `validation/` |
| Tests | `tests/` |
| CI integration | `ci/` |
| Publication pipeline | `publication/` |
| Repository generator | `generator/` |
| Demonstrators | `demonstrator/` |
| Pilot environment | `pilot/` |
| Security | `security/` |
| Provenance | `provenance/` |
| Recovery | `recovery/` |
| Observability | `observability/` |
| Operations | `operations/` |
| Performance | `performance/` |
| Risk management | `risk/` |
| Reference examples | `reference/` |
| Examples | `examples/` |
| Tooling | `tooling/` |
| Repository documentation | `docs/` |
| Documentation assets | `assets/` |
| Roadmap | `roadmap/` |
| Sprint planning | `planning/` |
| Release and baselines | GitHub Releases, Milestones and Projects |

## Lifecycle

The repository evolves through governed Work Packages. Every meaningful change should be traceable to an issue, branch, commit and pull request.

## Baseline Status

The current approved baseline is:

```text
v0.5.0
```

`v0.5.0` is a Production Baseline Candidate, approved with conditions for controlled pre-production and pilot evaluation (see the `v0.5.0` GitHub Release record; the historical baseline approval record is preserved in git history). It does not authorize production deployment.

Baseline history:

- Sprint-0 established the first bootstrap baseline (`v0.1.0-bootstrap`).
- Sprint-1 converted the bootstrap baseline into a production-quality Foundation Repository.
- Sprint-2 advanced the repository into structured, machine-checkable engineering models and platform architecture designs (`v0.2.0`).
- Sprint-3 established the knowledge platform concepts (`v0.3.0`).
- Sprint-4 established the first governed digital-twin foundation baseline for vessel references (`v0.4.0`).
- Sprint-5 added the validator, repository generator, publication channels, security baseline and integrated quality gate, approved as `v0.5.0`.
- Sprint-6 work on the controlled pilot environment and pilot readiness is in progress on `develop`, ahead of the next baseline.
