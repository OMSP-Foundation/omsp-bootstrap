---
Artifact-ID: OMSP-CANON-PHILOSOPHY-0001
Title: OMSP Philosophy
Version: 1.0.0
Status: Active
Owner: OMSP Foundation Governance
Baseline: Sprint-1
Classification: Public
Related-Issue: WP-0016 / #38
---

# OMSP Philosophy

## 1. Core Philosophy

OMSP is guided by three foundational ideas:

```text
Knowledge First • Models Before Code • Traceability by Design
```

These ideas define how OMSP approaches maritime systems engineering, governance, documentation, architecture, implementation, and AI-assisted work.

## 2. Knowledge First

OMSP treats operational knowledge as a primary engineering asset.

Knowledge should be:

- explicit rather than implicit;
- structured rather than scattered;
- reusable rather than one-off;
- governed rather than informal;
- traceable rather than disconnected.

Documents, models, standards, and decisions are not secondary outputs; they are durable engineering artifacts.

## 3. Models Before Code

OMSP favors model-based understanding before implementation.

Before code or automation is treated as authoritative, the underlying concepts, terms, responsibilities, interfaces, and decisions should be modeled or documented at the appropriate level.

This does not block implementation; it makes implementation explainable, reviewable, and reusable.

## 4. Traceability by Design

OMSP work should be traceable from intent to evidence.

Material work should preserve a path across:

```text
Vision → Mission → Principles → Issue → Artifact → Decision → PR → Review → Baseline/Release
```

Traceability is not an after-the-fact reporting task. It is part of how OMSP controls quality and accountability.

## 5. Human-Governed Automation

Automation and AI may support drafting, checking, summarizing, comparing, and validation preparation.

They must not replace accountable human ownership, review, approval, baseline authority, or release authority.

## 6. Open Foundation Thinking

OMSP favors open foundations that downstream repositories can reference and extend.

This requires shared terminology, stable artifact identity, clear governance, and documented exceptions where local repositories need specialization.

## 7. Practical Interpretation

When trade-offs arise, OMSP should prefer:

- explicit models over hidden assumptions;
- reviewed artifacts over informal agreement;
- reusable standards over local shortcuts;
- traceable decisions over undocumented changes;
- human accountability over automation convenience.

## 8. Related Canon Artifacts

- [Vision](./VISION.md) defines the long-term direction interpreted by this Philosophy.
- [Mission](./MISSION.md) defines the program purpose shaped by this Philosophy.
- [Principles](./PRINCIPLES.md) convert this Philosophy into operating rules.
- [Terminology](./TERMINOLOGY.md) defines the shared language used to express the Philosophy.
- [Ontology Overview](./ONTOLOGY_OVERVIEW.md) introduces the model layer implied by `Models Before Code`.
- [Canon Index](./CANON_INDEX.md) provides the recommended reading order for downstream references.

## 9. Maintenance

This Philosophy is maintained through issue-backed Work Packages and reviewed pull requests. Material changes require governance review and version metadata update.
