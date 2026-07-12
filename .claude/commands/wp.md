---
description: Start a new WP-XXXX work package with traceability
---

Draft a new OMSP work package (WP-XXXX) from the description in `$ARGUMENTS`.

Steps:
1. Determine the next free WP number: search existing IDs
   (`grep -rho "WP-[0-9]\{4\}" . | sort -u | tail`) and increment.
2. Use the work-package template in `templates/` if present; otherwise create a
   governed Markdown artifact with front-matter:
   ```
   ---
   Artifact-ID: OMSP-WP-NNNN
   Title: <work package title>
   Version: 0.1.0
   Status: Draft
   Owner: toss-cengiz
   ---
   ```
3. Body should cover: objective, scope / out-of-scope, acceptance criteria,
   affected artifacts (traceability links to source requirement/standard IDs),
   validation plan, and residual-risk notes.
4. Maintain the traceability chain — every WP should reference the upstream
   artifact(s) it derives from.
5. Suggest the branch name (`wp-NNNN-<slug>`) and a matching GitHub issue title,
   but do NOT self-approve or auto-open anything the human should confirm.
6. Run `python3 tooling/omsp_validate.py <file>` and report the result.

If the GitHub App lacks org write access, output the WP file and the proposed
issue text for the human to create manually.
