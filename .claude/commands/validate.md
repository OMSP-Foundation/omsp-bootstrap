---
description: Run OMSP validators and quality gate, then summarize findings
---

Run the OMSP validation suite from the repository root and report results.

Steps:
1. By default validate the CI-governed scope (matches
   `.github/workflows/omsp-validator.yml`):
   `python3 tooling/omsp_validate.py governance planning roadmap architecture knowledge reference release schemas validation`
   and capture the JSON output.
2. If `$ARGUMENTS` names specific paths, validate only those:
   `python3 tooling/omsp_validate.py $ARGUMENTS`.
   (Avoid `.` for routine checks — it also scans non-governed config like `.claude/`
   and root docs, producing false `OMSP-META-001` positives.)
3. Optionally run the full gate `python3 tooling/omsp_quality_gate.py` when the
   change touches governed paths (governance, planning, roadmap, architecture,
   knowledge, reference, release, schemas, validation, generator, publication,
   security, ci, operations, demonstrator).
4. Run unit tests: `python3 -m unittest discover -s tests -p "test_*.py"`.

Report:
- Total files scanned, findings count, error count.
- Each finding as `rule_id · severity · path · message` (group by file).
- Call out `OMSP-META-001` (missing metadata), `OMSP-ID-001` (bad Artifact-ID),
  and `OMSP-AUTH-001` (authority-claim gate) explicitly.
- End with a clear PASS / FAIL verdict.

Do NOT edit files or claim approval. This command is advisory reporting only —
a passing result never authorizes merge, baseline, or release.
