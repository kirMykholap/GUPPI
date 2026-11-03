---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-sprint-open]]"
purpose: Whether /sprint-open has the opening Case word the goal of the sprint from the person's answer to the open question alone, with no question on the goal and nothing taken from the vault or from the description of the project in CLAUDE.md
method: "by hand at Retro: the new Render of rule-skill-sprint-open in the Spec, raw/<date>/<hi HHMM>/spec.md, read against the Criterion, recorded in the estimate line"
checked: 2026-11-03
origin: raw/2026-10-31/0128/ledger.md#case-952
sprint: plugin
created: 2026-10-31
tags: [sprint, workflow, harness]
---

## Criterion

When:
The main agent starts `/sprint-open` of `.claude/skills/sprint-open/SKILL.md`, rendered from `rule-skill-sprint-open`, on `PreToolUse Skill`, or the person types `/sprint-open` on `UserPromptSubmit`, and the main agent dispatches `case-guppi` for the opening Case with the person's answer on what to build in the sprint.

Then:
The prompt of the call asks that the opening Case word the goal of the sprint in one sentence, the `purpose` and the `## Purpose` of the new sprint page, from the person's answer alone.
**＋** The opening Case puts no question on the goal to the person, who corrects it at the showing of the Case.
**－** No word of the goal comes from the vault or from the description of the project that `CLAUDE.md` holds.

## Result

2026-11-03, by hand at Retro of session 0316: the new step 2 of the Render of rule-skill-sprint-open in vault/raw/2026-11-03/0316/spec.md (Case 1018.1) has the prompt ask that the opening Case word the goal in one sentence from the person's answer alone, put it to the person in no question of its rounds, and take no word of it from the vault or from the description of CLAUDE.md

## History

- 2026-10-31 created · [[decision-case-952]]
- 2026-10-31 status: pending → passed · raw/2026-10-31/0128/ledger.md#L14
- 2026-11-03 updated: the Criterion replaced whole — the goal is worded from the person's answer, with no goal question and nothing from the description; the reading takes the new Render in the Spec at Retro · [[decision-case-1018.2]]
- 2026-11-03 status: pending → passed · raw/2026-11-03/0316/ledger.md#L31
