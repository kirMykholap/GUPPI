---
type: estimate
kind: QA
status: passed
target: "[[rule-handoff]]"
purpose: Whether handoff.md, the report of Retro, says each thing once in the section of its kind — a Case, box, reading, lesson or observation named again only with what the second section adds, the readings that wait listed in Debt alone and not counted as debt — with no commit, no number and no end, and keeps the three old section names
method: one reading by hand of .claude/skills/handoff/SKILL.md as rendered, or, at the Retro of the session that changes it, of the new Render of rule-handoff in the Spec, against the Criterion, recorded in the estimate line
checked: 2026-10-05
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
**＋** `## Debt` holds each box of the Spec that is debt and each red test reverted into a patch, with the path of the patch. Under them stands a line with the count of the boxes that wait for the librarian. Then comes one line per Estimate whose reading cannot be taken yet, except one that `## Ask the person` holds: its slug and the moment its reading waits for. These lines stand in the section and are not debt.
**＋** An Estimate this session creates or updates has no such line in `## Debt`: the Retro of `rule-retro` read it or set it `failed`, unless the person's answer is its reading.
**＋** `## Observations` holds what was noticed in Work Mode and Retro, a red before the work and an expected red among them; `## For the next session` holds what needs a decision.
**＋** `## Ask the person` holds one line per reading that only the person can take: the Estimate by slug, the mark `needs the person` and the question the person answers.
**－** No statement stands twice: a Case, box, reading, lesson or observation that one section names stands in another section only with what that section's kind adds about it, such as a caveat or what to check first, and no section says again what another section says of it. The file holds no commit, no number of an item and no end of an item.
**－** The section names `## Notes from memory`, `## Direct instructions to the librarian` and `## What actually got done` stay, so `rule-brief` reads `## What actually got done` as before.

## Result

2026-10-05, at the /hi of session 2103, by hand, .claude/skills/handoff/SKILL.md as rendered against the Criterion: the heading and the seven sections in the order of the Criterion, each with the content the Criterion gives it; Direct instructions lists no reading that waits; Debt holds the debt boxes and the patches with their paths, the count of the waiting boxes, then one line per Estimate not yet readable but those of Ask, said not to be debt, none for an Estimate the session creates or updates; Ask holds the slug, `needs the person` and the question; a thing said once, no commit, no item number, no end; the three old section names kept; a dirty tree stops it with "commit first"

## History

- 2026-09-27 created · [[decision-case-468.2]]
- 2026-09-30 updated: the Criterion replaced whole — handoff.md is the report of Retro, one section for each kind of fact, no numbers and no ends (case 531.5) · [[decision-case-531.5]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-03 status: pending → failed · raw/2026-10-03/1341/ledger.md#L2
- 2026-10-03 deferred · [[decision-case-618]]
- 2026-10-04 deferred · [[decision-case-621]]
- 2026-10-04 updated: the Criterion replaced whole — one statement once, a second section naming a thing only with what its kind adds; the readings that wait in Debt alone, each with its moment, not debt; read on a handoff the rendered skill wrote (case 624) · [[decision-case-624]]
- 2026-10-04 status: pending → failed · raw/2026-10-04/2041/ledger.md#L7
- 2026-10-05 status: failed → passed · raw/2026-10-04/2245/ledger.md#L2
- 2026-10-05 updated: the Criterion replaced whole — Debt lists no Estimate the session creates or updates as a reading that waits (case 670.3) · [[decision-case-670.3]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/2103/ledger.md#L3
