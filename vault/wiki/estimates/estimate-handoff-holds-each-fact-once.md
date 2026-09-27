---
type: estimate
kind: QA
status: pending
target: "[[rule-handoff]]"
purpose: Whether handoff.md holds each fact once — the Retro close in What actually got done, each open item named once with its end, the notes and the instructions to the librarian only their own facts
method: one reading by hand at the first /handoff after the render, against the close of its Retro, recorded in the estimate line
origin: raw/2026-09-27/2050/ledger.md#case-468.2
sprint: migration
created: 2026-09-27
tags: [session, workflow, harness]
---

## Criterion

When:
The person invokes `/handoff` after the Retro of the session, on a clean tree, and the agent writes `raw/<date>/<hi HHMM>/handoff.md`.

Then:
`## What actually got done` holds the three parts of the close of the Retro of `rule-retro`: Ratified and What got done as the person approved them, and What is not done in the form below.
**＋** What is not done names each item of the frontier in a few words with the end it took, since the numbers of the frontier are not in the file, and the text of a note for the handoff stands there as the end of its item.
**＋** Under What is not done stand the two lines under the frontier: the count of the boxes that wait for the librarian, and the slugs of the `read` lines whose slug this session creates or updates.
**＋** `## Notes from memory` holds only where the person hesitated, what stayed unclear and which decisions carried caveats.
**＋** `## Direct instructions to the librarian` holds only what to check first and what may duplicate what.
**－** No Case, reading, lesson or open item is named in two sections of `handoff.md`.
**－** The three section names stay as they are, so `rule-brief` reads `## What actually got done` as before.

## History

- 2026-09-27 created · [[decision-case-468.2]]
