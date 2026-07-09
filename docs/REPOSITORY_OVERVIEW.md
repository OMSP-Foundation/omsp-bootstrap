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
- platform architecture foundations;
- validation and verification foundations;
- reference material;
- release and baseline management.

## Out of Scope

This repository does not yet implement the full runtime platform. Runtime components, domain models, ontology services and production tooling will be developed in later OMSP repositories and sprints.

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
| Standards | `foundation/` |
| Schemas | `schemas/` |
| Templates | `templates/` |
| Canonical language | `canon/` |
| Platform concepts | `platform/` |
| Validation | `validation/` |
| Reference examples | `reference/` |
| Tooling | `tooling/` |
| Repository documentation | `docs/` |
| Roadmap | `roadmap/` |

## Lifecycle

The repository evolves through governed Work Packages. Every meaningful change should be traceable to an issue, branch, commit and pull request.

## Baseline Status

Sprint-0 established the first bootstrap baseline:

```text
v0.1.0-bootstrap
```

Sprint-1 converts this bootstrap baseline into a production-quality Foundation Repository.
