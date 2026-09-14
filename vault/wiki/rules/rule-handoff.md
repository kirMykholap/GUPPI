---
type: rule
kind: Leaf
purpose: Prevents the session's memory from being lost between the commit and the librarian
status: built
enforcement: render
governs: .claude/skills/handoff/SKILL.md
render_mode: full
parent: rule-end-of-work
estimates: [estimate-handoff-dispatches]
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
unclear, which decisions carried caveats), `## Direct instructions to the
librarian` (what to check first, what may duplicate what), `## What actually got
done` (which Cases closed, where the code landed, what is not done). Write it from
memory; do not re-read the artifacts. Short or empty sections are normal.

Then dispatch the `librarian-guppi` agent with one line: `Materialize <date>.` Wait
for its report and show it to the person unchanged. Do not commit after this.
<!-- /rule-handoff -->

## Estimates

- [[estimate-handoff-dispatches]]

## Parent

- [[rule-end-of-work]]

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.3
- 2026-09-10 estimate estimate-handoff-dispatches added · raw/2026-09-10/ledger.md#case-38.3
- 2026-09-10 status: draft → built · cascade
- 2026-09-12 updated: the handoff is one document in the session's folder; the librarian is dispatched with its path (case 73.7) · [[decision-case-73.7]]
- 2026-09-12 status: built → draft · cascade
- 2026-09-14 updated: the Recorded line dropped; guppi gate writes the stamped handoff mark (case 136.1) · [[decision-case-136.1]]
- 2026-09-14 status: draft → built · cascade
