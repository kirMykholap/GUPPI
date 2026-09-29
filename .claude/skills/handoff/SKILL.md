---
name: handoff
description: Write the handoff note from memory and hand the session to the librarian.
---


Tree: !`git status --porcelain`

If Tree above is not empty, stop and say "commit first". Otherwise write `vault/raw/<date>/<hi HHMM>/handoff.md` — the session's folder, one document, no `---` (case 73) — headed `# Handoff — <date>, <slice or topic>`. It is the report of Retro, written by the agent for the librarian and the next session (case 531.5), in these sections, in this order:
- `## Notes from memory`: where the person hesitated, what stayed unclear, which decisions carried caveats.
- `## Direct instructions to the librarian`: what to check first, what may duplicate what.
- `## What actually got done`: the ids of the Cases ratified, by the Tail, a Case that a `{supersedes:case N}` line names not counted; the code files and tests changed; the result of `make test` and `make style`; the readings and lessons written, by their ledger line numbers.
- `## Debt`: each box of the Spec that is debt, and each red test reverted into a patch, with the path of the patch; under them two lines: the count of the boxes that wait for the librarian, and the slugs of the `read` lines whose slug this session creates or updates.
- `## Observations`: what was noticed in Work Mode and Retro — a bug, a contract that turned out imprecise, a red before the work, an expected red with its check and the page or file it waits for.
- `## For the next session`: what needs a decision, which Retro does not take.
- `## Ask the person`: one line per reading that only the person can take — the Estimate by slug, the mark `needs the person`, and the question the person answers.
A fact stands in one section only: a Case, a box, a reading, a lesson or an observation named in one section is not named in another (cases 468.2, 531.5). The file names no commit, no number of an item and no end of an item. Write it from memory; do not re-read the artifacts. Short or empty sections are normal.

Then dispatch the `librarian-guppi` agent with one line: `Materialize <date> from vault/raw/<date>/<hi HHMM>/handoff.md.`, the path of the file you just wrote. Wait for its report and show it to the person unchanged. Do not commit after this, and write no `LEDGER` block.
