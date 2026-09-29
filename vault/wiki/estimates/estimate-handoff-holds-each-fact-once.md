---
type: estimate
kind: QA
status: pending
target: "[[rule-handoff]]"
purpose: Whether handoff.md, the report of Retro, holds each fact once in the section of its kind — What actually got done, Debt, Observations, For the next session, Ask the person — with no commit, no number and no end, and keeps the three old section names
method: one reading by hand at the first /handoff after the render, against the close of its Retro, recorded in the estimate line
origin: raw/2026-09-27/2050/ledger.md#case-468.2
sprint: migration
created: 2026-09-27
tags: [session, workflow, harness]
---

## Criterion

When:
The agent calls `/handoff` on `PreToolUse Skill` after the reply that ends Retro, or the person types `/handoff` on `UserPromptSubmit`, on a clean tree, and the agent writes `raw/<date>/<hi HHMM>/handoff.md`.

Then:
`raw/<date>/<hi HHMM>/handoff.md` is the report of Retro: under `# Handoff — <date>, <slice or topic>` it holds, in order, `## Notes from memory`, `## Direct instructions to the librarian`, `## What actually got done`, `## Debt`, `## Observations`, `## For the next session` and `## Ask the person`.
**＋** `## Notes from memory` holds only where the person hesitated, what stayed unclear and which decisions carried caveats; `## Direct instructions to the librarian` holds only what to check first and what may duplicate what.
**＋** `## What actually got done` holds the ids of the Cases ratified, the code files and tests changed, the result of `make test` and `make style`, and the readings and lessons written, by their ledger line numbers.
**＋** `## Debt` holds each box of the Spec that is debt and each red test reverted into a patch, with the path of the patch, and under them two lines: the count of the boxes that wait for the librarian, and the slugs of the `read` lines whose slug this session creates or updates.
**＋** `## Observations` holds what was noticed in Work Mode and Retro, a red before the work and an expected red among them; `## For the next session` holds what needs a decision.
**＋** `## Ask the person` holds one line per reading that only the person can take: the Estimate by slug, the mark `needs the person` and the question the person answers.
**－** No Case, box, reading, lesson or observation is named in two sections of `handoff.md`, and the file holds no commit, no number of an item and no end of an item.
**－** The section names `## Notes from memory`, `## Direct instructions to the librarian` and `## What actually got done` stay, so `rule-brief` reads `## What actually got done` as before.

## History

- 2026-09-27 created · [[decision-case-468.2]]
- 2026-09-30 updated: the Criterion replaced whole — handoff.md is the report of Retro, one section for each kind of fact, no numbers and no ends (case 531.5) · [[decision-case-531.5]]
