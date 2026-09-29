---
type: rule
kind: Leaf
purpose: Prevents the session's memory from being lost between the commit and the librarian
status: draft
enforcement: render
governs: .claude/skills/handoff/SKILL.md
render_mode: full
parent: "[[rule-end-of-work]]"
estimates: ["[[estimate-handoff-dispatches]]", "[[estimate-handoff-holds-each-fact-once]]"]
origin: raw/2026-09-10/ledger.md#case-38.3
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness, render]
---

## Purpose

Prevents the session's memory from being lost between the commit and the
librarian. The handoff note is the report of Retro: it carries what no artifact holds — where the person hesitated and what the librarian should check first — and what got done, the debt, the observations, what the next session decides and what only the person can answer, one section each (case 531.5).
It is written from memory, because re-reading the artifacts would spend the
context advantage that is the note's only reason to exist.

## Render

<!-- rule-handoff -->
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
<!-- /rule-handoff -->

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.3
- 2026-09-10 estimate estimate-handoff-dispatches added · raw/2026-09-10/ledger.md#case-38.3
- 2026-09-10 status: draft → built · cascade
- 2026-09-12 updated: the handoff is one document in the session's folder; the librarian is dispatched with its path (case 73.7) · [[decision-case-73.7]]
- 2026-09-12 status: built → draft · cascade
- 2026-09-14 updated: the Recorded line dropped; guppi gate writes the stamped handoff mark (case 136.1) · [[decision-case-136.1]]
- 2026-09-14 status: draft → built · cascade
- 2026-09-27 updated: the handoff holds each fact once — What actually got done carries the Retro close, a note for the handoff stands as the end of its item, the notes and the instructions hold only their own facts (case 468.2) · [[decision-case-468.2]]
- 2026-09-27 estimate estimate-handoff-holds-each-fact-once added · [[decision-case-468.2]]
- 2026-09-27 status: built → draft · cascade
- 2026-09-29 updated: the dispatch names handoff.md by its path, as case 73.7 meant and the librarian's frame reads (case 499.2) · [[decision-case-499.2]]
- 2026-09-30 updated: handoff.md is the report of Retro: Debt, Observations, For the next session and Ask the person added; no number, no end and no commit; the three old section names kept; the Purpose no longer counts three things (case 531.5) · [[decision-case-531.5]]
