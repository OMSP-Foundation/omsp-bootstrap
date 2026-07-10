# Digital Twin AI-Assistance Boundaries

- Artifact ID: `OMSP-REFERENCE-TWIN-AI-BOUNDARY-0001`
- Version: `0.1.0`
- Status: `review`

## Purpose

This artifact defines permitted, restricted, and prohibited AI-assisted activities for OMSP digital-twin work.

## Permitted assistance

AI may:

- draft documentation and schemas;
- suggest mappings between existing identifiers;
- summarize traceable evidence;
- classify records using declared taxonomies;
- flag missing, stale, inconsistent, or conflicting data;
- propose candidate explanations or validation cases;
- generate simulated test data that is clearly labeled;
- assist reviewers with checklists and impact analysis.

## Conditions for permitted use

Every material AI-assisted output must:

- remain reviewable by a human;
- preserve links to source evidence;
- state assumptions and uncertainty;
- identify simulated or generated content;
- avoid silent modification of authoritative records;
- be reproducible where used as validation evidence;
- remain within the declared model and operating scope.

## Restricted assistance

The following require explicit human review before use:

- candidate configuration extraction from documents or images;
- conflict-resolution recommendations;
- anomaly severity classification;
- scenario decision recommendations;
- derived safety or readiness indicators;
- transformation of natural-language procedures into structured steps;
- generated code for runtime ingestion, alerting, or control-adjacent systems.

Restricted outputs remain advisory and must expose their provenance.

## Prohibited activities

AI must not:

- approve or certify configuration facts;
- fabricate or conceal evidence;
- silently resolve conflicting safety-relevant data;
- issue vessel-control, navigation, emergency, or maintenance commands;
- override accountable human decisions or approved procedures;
- claim manufacturer, class, regulatory, flag-state, or insurer authority;
- declare seaworthiness, compliance, or risk acceptance;
- auto-promote observations or inferences into approved configuration;
- suppress uncertainty because a confidence score is high;
- operate outside an explicitly approved runtime envelope.

## Human review requirements

The reviewer must verify:

- source resolution;
- factual and semantic correctness;
- authority classification;
- completeness of limitations;
- visibility of uncertainty and conflicts;
- impact on dependent artifacts;
- absence of unintended operational instruction language.

## Failure and escalation

AI-assisted output must be rejected, quarantined, or marked `indeterminate` when:

- evidence cannot be resolved;
- the generated statement exceeds the source scope;
- authority or approval status is ambiguous;
- safety-critical uncertainty is hidden;
- output could reasonably be mistaken for an instruction;
- reproducibility or audit evidence is missing.

## Runtime boundary

Use of AI in a future runtime requires separate approval covering model identity, version, test evidence, cybersecurity, latency, failure behavior, monitoring, fallback, human override, and operating envelope. Sprint-4 artifacts do not grant this approval.
