# Changelog

All notable changes to the OMSP Foundation repository are recorded here. Governed release scope and approval boundaries are defined by the corresponding GitHub Release records and project milestones.

## [0.5.1] - 2026-07-13

Clean baseline and product reorientation (Sprint-6, Work Packages WP-0070…WP-0076). GitHub Release publication is a separate accountable human decision.

### Added

- canonical engineering-methodology inventory (`canon/ENGINEERING_METHODOLOGY.md`, WP-0069);
- `omsp-cto` top-layer advisory agent: aviation-derived operational-documentation expertise, spec-first MODS product stack (MODS Specification / ODS-100…600, Marine Diagram System, Core Operations Manual, Vessel Definition Modules, Scenario Library, QRH), docs-as-code chain ownership, task-to-skill map;
- audit reconciliation disposition table with 16 evidence-backed findings (`planning/WP-0070-AUDIT-DISPOSITION.md`);
- ADR-0001 repository topology: monorepo with trigger-based re-evaluation (`governance/ADR-0001-REPOSITORY-TOPOLOGY.md`);
- filled governed artifact templates: requirement, risk, validation record, ADR, Work Package (WP-0071);
- canonical AI governance artifact with human approval gates and provenance rules (`governance/AI_GOVERNANCE.md`, WP-0073);
- Hanse 460 golden-path product definition — users, provenance rules, model boundary, validator evidence contract, output specification, five-minute demo storyboard (`planning/WP-0074-GOLDEN-PATH-DEFINITION.md`);
- Sprint 7–14 product-led backlog with epic exit criteria, WP-0077…WP-0089 breakdown, capacity policy, deferred-governance triggers and measurable release gates (`planning/WP-0075-DOMAIN-BACKLOG-REBASELINE.md`).

### Changed

- issue #145 (Post-Audit Product Reorientation) declared the official roadmap; the controlled-pilot-readiness Sprint-6 plan superseded;
- open Sprint-6 work renumbered WP-0070…WP-0076 (resolving the WP-0061…0066 collision); WP-0060–0068 retired and reserved;
- roadmap updated: Sprint-5 completed, Sprint-6 reorientation, Sprint-7…14+ MODS-fused blocks;
- lifecycle mini-policies consolidated into the Engineering Playbook as the single authority; canonical authority registry extended to five domains with removed-legacy-path provenance;
- root documentation, navigation and structure documents aligned to the clean baseline.

### Removed

- 25 stub/duplicate files removed with governed authority record (WP-0072): overdue superseded `foundation/` stubs, `platform/` bootstrap duplicates, eight thin governance mini-policies, and orphan placeholders; `foundation/` and `platform/` directories retired (Markdown stub ratio reduced from ~29.7% to ~17.2%; remaining short files are intentional fixtures or phase-deferred).

### Known Limitations

- carried over from `v0.5.0`: production deployment not authorized; provenance signing, remote telemetry, vulnerability intelligence, performance qualification, and external disaster-recovery remain deferred — now each with a recorded re-entry trigger;
- persistent risks `RR-001`…`RR-005` remain open; reassessment is scheduled against design-partner pilot evidence (Sprint-12);
- maritime domain content (ontology concepts, vessel YAML models, scenarios) is defined but not yet implemented — Sprint 7–9 scope.

## [0.5.0] - 2026-07-10

### Added

- deterministic governed-artifact validator with machine-readable findings;
- reproducible repository generator with dry-run and overwrite protection;
- governed preview, baseline and release publication channels with integrity manifests;
- security and software supply-chain baseline, workflow inventory, secret-pattern checks and SBOM evidence;
- integrated CI/CD quality gate with retained component evidence;
- structured operational audit events, health records and privacy-aware redaction;
- end-to-end platform integration demonstrator;
- operations, incident-response and recovery runbook with exercised recovery drill;
- production-readiness assessment, residual-risk register and accountable approval records.

### Changed

- advanced the governed baseline from documentation and reference-model foundations to executable standard-library tooling;
- completed Sprint-5 and opened Sprint-6 controlled pilot-readiness planning;
- classified the current baseline as a Production Baseline Candidate approved for controlled pre-production and pilot evaluation;
- retained human authority for review, risk acceptance, baseline, publication, release and deployment decisions.

### Known Limitations

- production deployment is not authorized;
- production environment approvals are not implemented;
- provenance and audit evidence are not cryptographically signed;
- remote telemetry, paging and long-term evidence storage are not integrated;
- vulnerability intelligence and repository-history secret scanning remain deferred;
- performance, capacity and availability qualification remain incomplete;
- external backup and disaster-recovery infrastructure remain deferred;
- persistent risks `RR-001` through `RR-005` require reassessment before a production-release decision.

## [0.4.0] - 2026-07-10

### Added

- generic vessel reference model;
- Hanse 460 design-family reference configuration;
- equipment and interface model;
- operational scenario model;
- digital-twin state and observation model;
- digital-twin validation demonstrator;
- digital-twin governance and safety boundaries.

### Scope

Documentation-level digital-twin foundation only. No physical-vessel configuration, live telemetry, vessel control, certification or operational authorization was granted.

## [0.3.0] - 2026-07-10

### Added

- knowledge graph conceptual model;
- semantic relationship catalog;
- artifact registry and knowledge index;
- AI-readable artifact processing contract;
- knowledge publication package;
- knowledge-platform validation scenarios and baseline-readiness package.

## [0.2.0] - 2026-07-10

### Added

- formal ontology artifact and canon mapping;
- dedicated architecture artifacts for the four OMSP platform engines;
- platform context model;
- traceability automation design;
- publication workflow design;
- validation checklist linting design;
- canonical authority map and duplicate-authority validation.

## [0.1.0] - 2026-07-09

### Added

- governance foundation and engineering council model;
- engineering artifact, metadata and traceability standards;
- canon foundation;
- platform architecture;
- validation and quality-gate foundations;
- GitHub workflow and contribution controls;
- first governed baseline and release-readiness package.

## [0.1.0-alpha]

- Initial repository bootstrap.
