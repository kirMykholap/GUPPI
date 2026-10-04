---
type: estimate
kind: QA
status: failed
target: "[[rule-handoff]]"
purpose: Whether handoff.md, the report of Retro, says each thing once in the section of its kind — a Case, box, reading, lesson or observation named again only with what the second section adds, the readings that wait listed in Debt alone and not counted as debt — with no commit, no number and no end, and keeps the three old section names
method: one reading by hand, at the /hi of a later session, of a handoff.md written by .claude/skills/handoff/SKILL.md as rendered from rule-handoff after case 624, against the close of its Retro, recorded in the estimate line
checked: 2026-10-04
origin: raw/2026-09-27/2050/ledger.md#case-468.2
sprint: migration
created: 2026-09-27
tags: [session, workflow, harness]
---

## Criterion

When:
The agent calls `/handoff` on `PreToolUse Skill` after the reply that ends Retro, or the person types `/handoff` on `UserPromptSubmit`, on a clean tree, and the agent runs `.claude/skills/handoff/SKILL.md` as rendered from `rule-handoff` and writes `raw/<date>/<hi HHMM>/handoff.md`.

Then:
`raw/<date>/<hi HHMM>/handoff.md` is the report of Retro: under `# Handoff — <date>, <slice or topic>` it holds, in order, `## Notes from memory`, `## Direct instructions to the librarian`, `## What actually got done`, `## Debt`, `## Observations`, `## For the next session` and `## Ask the person`.
**＋** `## Notes from memory` holds only where the person hesitated, what stayed unclear and which decisions carried caveats. `## Direct instructions to the librarian` holds only what to check first and what may duplicate what, and lists no reading that waits.
**＋** `## What actually got done` holds the ids of the Cases ratified, the code files and tests changed, the result of `make test` and `make style`, and the readings and lessons written, by their ledger line numbers.
**＋** `## Debt` holds each box of the Spec that is debt and each red test reverted into a patch, with the path of the patch. Under them stands a line with the count of the boxes that wait for the librarian. Then comes one line per Estimate whose reading cannot be taken yet, each one this session creates or updates among them, except one that `## Ask the person` holds: its slug and the moment its reading waits for. These lines stand in the section and are not debt.
**＋** `## Observations` holds what was noticed in Work Mode and Retro, a red before the work and an expected red among them; `## For the next session` holds what needs a decision.
**＋** `## Ask the person` holds one line per reading that only the person can take: the Estimate by slug, the mark `needs the person` and the question the person answers.
**－** No statement stands twice: a Case, box, reading, lesson or observation that one section names stands in another section only with what that section's kind adds about it, such as a caveat or what to check first, and no section says again what another section says of it. The file holds no commit, no number of an item and no end of an item.
**－** The section names `## Notes from memory`, `## Direct instructions to the librarian` and `## What actually got done` stay, so `rule-brief` reads `## What actually got done` as before.

## Result

2026-10-04, at the /hi of session 2041, by hand: vault/raw/2026-10-04/1934/handoff.md against the close of its Retro, raw/2026-10-04/1934/ledger.md, 5 lines, the last at 20:30:44: the heading and the seven sections stand in order and each holds its kind; What actually got done names the 4 readings and the lesson by L1-L5 as the ledger holds them; Debt says no box is debt and counts 84 boxes that wait; the readings that wait stand in Debt alone; but Debt gives them as 30 Estimates in two lines grouped by moment, not one line per Estimate

## History

- 2026-09-27 created · [[decision-case-468.2]]
- 2026-09-30 updated: the Criterion replaced whole — handoff.md is the report of Retro, one section for each kind of fact, no numbers and no ends (case 531.5) · [[decision-case-531.5]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-03 status: pending → failed · raw/2026-10-03/1341/ledger.md#L2
- 2026-10-03 deferred · [[decision-case-618]]
- 2026-10-04 deferred · [[decision-case-621]]
- 2026-10-04 updated: the Criterion replaced whole — one statement once, a second section naming a thing only with what its kind adds; the readings that wait in Debt alone, each with its moment, not debt; read on a handoff the rendered skill wrote (case 624) · [[decision-case-624]]
- 2026-10-04 status: pending → failed · raw/2026-10-04/2041/ledger.md#L7
