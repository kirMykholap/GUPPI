---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-sprint-open]]"
purpose: Whether /sprint-open has the opening Case word the goal of the sprint from the person's answer to the open question alone, with no question on the goal and nothing taken from the vault or from the description of the project in CLAUDE.md
method: "by hand at Retro: the new Render of rule-skill-sprint-open in the Spec, raw/<date>/<hi HHMM>/spec.md, read against the Criterion, recorded in the estimate line"
checked: 2026-11-03
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [sprint, workflow, harness]
core: true
---

## Criterion

When:
The main agent starts `/sprint-open` of `.claude/skills/sprint-open/SKILL.md`, rendered from `rule-skill-sprint-open`, on `PreToolUse Skill`, or the person types `/sprint-open` on `UserPromptSubmit`, and the main agent dispatches `case-guppi` for the opening Case with the person's answer on what to build in the sprint.

Then:
The prompt of the call asks that the opening Case word the goal of the sprint in one sentence, the `purpose` and the `## Purpose` of the new sprint page, from the person's answer alone.
**＋** The opening Case puts no question on the goal to the person, who corrects it at the showing of the Case.
**－** No word of the goal comes from the vault or from the description of the project that `CLAUDE.md` holds.

## Result

2026-11-03, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
