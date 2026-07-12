---
description: Scaffold a new governed OMSP artifact with valid metadata
---

Create a new governed artifact that passes `tooling/omsp_validate.py` on the first try.

Input in `$ARGUMENTS` (free-form): intended domain, title, and target directory.
Ask only if domain or title is missing.

Rules:
1. Prefer starting from the matching file in `templates/` if one exists.
2. Emit YAML front-matter with ALL required fields:
   ```
   ---
   Artifact-ID: OMSP-<DOMAIN>-<NAME>-NNNN
   Title: <human title>
   Version: 0.1.0
   Status: Draft
   Owner: <owner or "OMSP Engineering Council">
   ---
   ```
3. `Artifact-ID` must match `^OMSP-[A-Z0-9]+(?:-[A-Z0-9]+)*-[0-9]{4}$`.
   Pick the next free NNNN for that domain — search the repo for existing IDs
   (`grep -r "Artifact-ID: OMSP-<DOMAIN>" .`) and increment.
4. Never reference a `Superseded` compatibility stub. Point at the canonical
   Artifact-ID / `governance/` path instead.
5. Never include automation-approval phrasing (e.g. claiming the AI, validator, or
   CI "approved" something) — such phrases trigger the `OMSP-AUTH-001` gate.
6. After writing, run `python3 tooling/omsp_validate.py <new-file>` and confirm zero
   errors. Report the path and validation result. Leave committing to the human.
