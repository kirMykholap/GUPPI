---
type: estimate
kind: QA
status: passed
target: "[[rule-handoff]]"
purpose: Whether handoff.md, the report of Retro, says each thing once in the section of its kind — a Case, box, reading, lesson or observation named again only with what the second section adds, the readings that wait listed in Debt alone and not counted as debt — with no commit, no number and no end, and keeps the three old section names
method: one reading by hand of .claude/skills/handoff/SKILL.md as rendered, or, at the Retro of the session that changes it, of the new Render of rule-handoff in the Spec, against the Criterion, recorded in the estimate line
checked: 2026-10-12
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
The agent calls `/handoff` on `PreToolUse Skill` after the reply that ends Retro, or the person types `/handoff` on `UserPromptSubmit`, on a clean tree, and the agent runs `.claude/skills/handoff/SKILL.md` as rendered from `rule-handoff` and writes `raw/<date>/<hi HHMM>/handoff.md`.

Then:
`raw/<date>/<hi HHMM>/handoff.md` is the report of Retro: under `# Handoff — <date>, <slice or topic>` it holds, in order, `## Notes from memory`, `## Direct instructions to the librarian`, `## What actually got done`, `## Debt`, `## Observations`, `## For the next session` and `## Ask the person`.
**＋** `## Notes from memory` holds only where the person hesitated, what stayed unclear and which decisions carried caveats. `## Direct instructions to the librarian` holds only what to check first and what may duplicate what, and lists no reading that waits.
**＋** `## What actually got done` holds the ids of the Cases ratified, the code files and tests changed, the result of `uv run --project .guppi guppi test` and `uv run --project .guppi guppi style`, and the readings and lessons written, by their ledger line numbers.
**＋** `## Debt` holds each box of the Spec that is debt and each red test reverted into a patch, with the path of the patch. Under them stands a line with the count of the boxes that wait for the librarian. Then comes one line per Estimate whose reading cannot be taken yet, except one that `## Ask the person` holds: its slug and the moment its reading waits for. These lines stand in the section and are not debt.
**＋** An Estimate this session creates or updates has no such line in `## Debt`: the Retro of `rule-retro` read it or set it `failed`, unless the person's answer is its reading. An Estimate of the live sprint page `entity-sprint-<id>` whose work is not done, which that Retro left `pending`, has its line, its moment the Retro of the session that finishes its work or the close of the sprint. An Estimate whose `method` waits for an event that has not come, which that Retro left `pending`, has its line, its moment that event.
**＋** `## Observations` holds what was noticed in Work Mode and Retro, a red before the work and an expected red among them; `## For the next session` holds what needs a decision.
**＋** `## Ask the person` holds one line per reading that only the person can take: the Estimate by slug, the mark `needs the person` and the question the person answers.
**－** No statement stands twice: a Case, box, reading, lesson or observation that one section names stands in another section only with what that section's kind adds about it, such as a caveat or what to check first, and no section says again what another section says of it. The file holds no commit, no number of an item and no end of an item.
**－** The section names `## Notes from memory`, `## Direct instructions to the librarian` and `## What actually got done` stay, so `rule-brief` reads `## What actually got done` as before.

## Result

2026-10-12, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
