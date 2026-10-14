---
type: rule
kind: Leaf
purpose: Prevents the session's memory from being lost between the commit and the librarian
status: built
enforcement: render
governs: .claude/skills/handoff/SKILL.md
render_mode: full
parent: "[[rule-end-of-work]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [session, workflow, harness, render]
core: true
---

## Purpose

Prevents the session's memory from being lost between the commit and the
librarian. The handoff note is the report of Retro: it carries what no artifact holds — where the person hesitated and what the librarian should check first — and what got done, the debt, the observations, what the next session decides and what only the person can answer, one section each.
It is written from memory, because re-reading the artifacts would spend the
context advantage that is the note's only reason to exist.

## Render

<!-- rule-handoff -->
---
name: handoff
description: Write the handoff note from memory and hand the session to the librarian.
---


Tree: !`git status --porcelain`

If Tree above is not empty, stop and say "commit first". Otherwise write `vault/raw/<date>/<hi HHMM>/handoff.md` — the session's folder, one document, no `---` — headed `# Handoff — <date>, <slice or topic>`. It is the report of Retro, written by the agent for the librarian and the next session, in these sections, in this order:
- `## Notes from memory`: where the person hesitated, what stayed unclear, which decisions carried caveats.
- `## Direct instructions to the librarian`: what to check first, what may duplicate what; no reading that waits, which `## Debt` lists.
- `## What actually got done`: the ids of the Cases ratified, by the Tail, a Case that a `{supersedes:case N}` line names, and each of its sub-cases, not counted; the code files and tests changed; the result of `make test` and `make style`; the readings and lessons written, by their ledger line numbers.
- `## Debt`: each box of the Spec that is debt, and each red test reverted into a patch, with the path of the patch; under them a line with the count of the boxes that wait for the librarian, then one line per Estimate whose reading cannot be taken yet, except one that `## Ask the person` holds: its slug and the moment its reading waits for; an Estimate this session creates or updates has no such line, since Retro read it or set it `failed`, but for an Estimate of the live sprint page whose work is not done, which Retro left `pending`: its line names the Retro of the session that finishes its work or the close of the sprint, and for an Estimate whose `method` waits for an event that has not come, which Retro left `pending`: its line names that event; these lines stand in the section and are not debt.
- `## Observations`: what was noticed in Work Mode and Retro — a bug, a contract that turned out imprecise, a red before the work, an expected red with its check and the page or file it waits for.
- `## For the next session`: what needs a decision, which Retro does not take.
- `## Ask the person`: one line per reading that only the person can take — the Estimate by slug, the mark `needs the person`, and the question the person answers.
A thing is said once: a Case, a box, a reading, a lesson or an observation that one section names stands in another section only with what that section's kind adds about it — a caveat in `## Notes from memory`, what to check first in `## Direct instructions to the librarian` — and no section says again what another section says of it. The file names no commit, no number of an item and no end of an item. Write it from memory; do not re-read the artifacts. Short or empty sections are normal.

Then, in a session whose `work.md` holds `## Conserved Spec` — one that `/box` runs, as you wrote it in this turn — dispatch nothing: go back to the step of `/box` that follows `/handoff`, which merges the branch and dispatches the librarian. In any other session, dispatch the `librarian-guppi` agent with one line: `Materialize <date> from vault/raw/<date>/<hi HHMM>/handoff.md.`, the path of the file you just wrote. Wait for its report and show it to the person unchanged. Do not commit after this, and write no `LEDGER` block.
<!-- /rule-handoff -->

## History

- 2026-10-14 shipped with GUPPI
