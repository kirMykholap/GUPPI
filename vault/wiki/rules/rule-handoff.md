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
librarian. The handoff note carries three things no artifact holds: where the
person hesitated, what the librarian should check first, and what actually got done.
It is written from memory, because re-reading the artifacts would spend the
context advantage that is the note's only reason to exist.

## Render

<!-- rule-handoff -->
---
name: handoff
description: Write the handoff note from memory and hand the session to the librarian.
---


Tree: !`git status --porcelain`

If Tree above is not empty, stop and say "commit first". Otherwise write `vault/raw/<date>/<hi HHMM>/handoff.md` — the session's folder, one document, no `---` (case 73) — headed `# Handoff — <date>, <slice or topic>` with
three sections: `## Notes from memory` (where the person hesitated, what stayed
unclear, which decisions carried caveats), `## Direct instructions to the librarian` (what to check first, what may duplicate what), `## What actually got done` (the three parts of the close of the Retro: Ratified and What got done as the person approved them; What is not done names each item of the frontier in a few words with the end it took, since the numbers of the frontier are not in this file, the text of a note for the handoff standing there as the end of its item, and under it the two lines under the frontier — the count of the boxes that wait for the librarian and the slugs of the `read` lines whose slug this session creates or updates). A fact stands in one section only: a Case, a reading, a lesson or an open item named in one section is not named in another (case 468.2). Write it from
memory; do not re-read the artifacts. Short or empty sections are normal.

Then dispatch the `librarian-guppi` agent with one line: `Materialize <date> from vault/raw/<date>/<hi HHMM>/handoff.md.`, the path of the file you just wrote. Wait
for its report and show it to the person unchanged. Do not commit after this.
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
