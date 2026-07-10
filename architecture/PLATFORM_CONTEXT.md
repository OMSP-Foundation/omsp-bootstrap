---
Artifact-ID: OMSP-ARCH-CONTEXT-0001
Title: OMSP Platform Context
Version: 1.0.0
Status: Active
Owner: OMSP Engineering Council
Baseline: Sprint-2
Classification: Public
Related-Issue: WP-0025 / #52
Depends-On:
  - OMSP-ARCH-PLATFORM-0001
  - OMSP-ARCH-ENGINEERING-KERNEL-0001
  - OMSP-ARCH-KNOWLEDGE-ENGINE-0001
  - OMSP-ARCH-TRACEABILITY-ENGINE-0001
  - OMSP-ARCH-PUBLICATION-ENGINE-0001
---

# OMSP Platform Context

## 1. Purpose

This artifact defines the top-level OMSP platform boundary, external actors, repository boundaries and engine interactions. It is a maintainable C4-style context view expressed in Mermaid and governed Markdown.

## 2. Diagram Source Decision

Mermaid is the canonical diagram source for Sprint-2 because it is text-based, reviewable in pull requests and rendered natively by GitHub. Exported images may be produced for publication, but they are derived artifacts and do not replace this source.

## 3. System Context

```mermaid
flowchart LR
    ENG[Engineers and Maintainers]
    GOV[Engineering Council and Reviewers]
    CONS[Downstream Consumers]
    EXT[External Standards and Reference Sources]

    subgraph OMSP[OMSP Platform Boundary]
      EK[Engineering Kernel]
      KE[Knowledge Engine]
      TE[Traceability Engine]
      PE[Publication Engine]
    end

    REPOS[(Governed OMSP Repositories)]
    CI[CI and Repository Automation]
    PUB[(Published Knowledge Packages)]

    ENG -->|creates and changes artifacts| EK
    GOV -->|reviews and approves decisions| EK
    EXT -->|reference inputs with provenance| KE
    EK -->|governed artifacts and models| KE
    EK -->|artifact metadata and change events| TE
    KE -->|semantic structures and indexed knowledge| TE
    TE -->|validation evidence and traceability reports| PE
    EK -->|publication candidates| PE
    KE -->|knowledge package content| PE
    PE -->|versioned governed outputs| PUB
    CONS -->|uses approved publications| PUB

    EK <--> REPOS
    KE <--> REPOS
    TE <--> REPOS
    PE <--> REPOS
    CI -->|executes deterministic checks| TE
    CI -->|builds previews and packages| PE
```

## 4. External Actors

| Actor | Responsibility | Authority Boundary |
| --- | --- | --- |
| Engineers and Maintainers | Create, update and propose governed artifacts and models. | Cannot self-approve material governance, baseline or release decisions unless assigned authority permits it. |
| Engineering Council and Reviewers | Review architecture, governance, baseline and release proposals. | Sole accountable human approval boundary for governed decisions. |
| Downstream Consumers | Use approved knowledge packages, models and references. | Consumption does not change source authority. |
| External Standards and Reference Sources | Supply standards, regulations, manufacturer material and domain references. | Inputs require provenance; external content is not automatically OMSP authority. |
| CI and Repository Automation | Execute deterministic validation, reports and publication builds. | Automation may detect and report; it cannot approve. |

## 5. OMSP Platform Boundary

The platform boundary contains four logical engines:

- **Engineering Kernel** manages governed engineering work and artifact creation.
- **Knowledge Engine** structures, indexes and relates governed knowledge.
- **Traceability Engine** validates identity, metadata, relations and evidence.
- **Publication Engine** assembles eligible governed content into versioned outputs.

The platform boundary does not include accountable human governance authority. Human reviewers interact with the platform but remain external decision authorities.

## 6. Repository Boundary View

```mermaid
flowchart TB
    subgraph Foundation[Foundation Repository]
      GOV[Governance and Standards]
      CANON[Canon and Ontology]
      ARCH[Platform Architecture]
      VAL[Validation Definitions]
    end

    subgraph Downstream[Downstream Repository Families]
      CORE[Core and Tooling]
      MODELS[Models and Digital Twin]
      DOCS[Documentation and Publication]
      REF[Reference Implementations]
    end

    GOV --> CORE
    GOV --> MODELS
    GOV --> DOCS
    GOV --> REF
    CANON --> CORE
    CANON --> MODELS
    ARCH --> CORE
    ARCH --> DOCS
    VAL --> CORE
    VAL --> MODELS
    VAL --> DOCS
    VAL --> REF
```

Foundation artifacts provide authority and contracts. Downstream repositories implement or consume them through stable Artifact IDs and explicit traceability relations.

## 7. Engine Interaction View

```mermaid
sequenceDiagram
    participant H as Human Contributor
    participant EK as Engineering Kernel
    participant KE as Knowledge Engine
    participant TE as Traceability Engine
    participant PE as Publication Engine
    participant R as Human Reviewer

    H->>EK: Propose governed artifact change
    EK->>KE: Submit structured artifact content
    KE->>TE: Provide semantic identities and relations
    EK->>TE: Provide metadata and work-package evidence
    TE-->>H: Validation findings
    H->>EK: Correct or justify findings
    R->>EK: Record accountable review decision
    EK->>PE: Mark approved publication candidate
    TE->>PE: Provide traceability and readiness evidence
    PE-->>R: Produce preview or release candidate
    R->>PE: Record publication/release approval
    PE-->>H: Publish versioned governed package
```

## 8. Trust and Authority Boundaries

1. Repository content is not authoritative solely because it exists on a branch.
2. Draft and review artifacts remain distinguishable from Active, baseline and release artifacts.
3. Engine outputs are proposals, validations, indexes or packages; none confer human approval.
4. External inputs require source, version and provenance metadata.
5. Published outputs must retain links to canonical Artifact IDs and source repository state.

## 9. Change Rules

Material changes to actors, platform boundary, engine responsibilities or trust boundaries require architecture review. Diagram updates must remain consistent with `PLATFORM_ARCHITECTURE.md` and the four engine artifacts.
