---
type: estimate
kind: QA
status: passed
target: "[[rule-skill-sprint-open]]"
purpose: Whether /sprint-open has the opening Case ask the goal of the sprint in every project and at every sprint by a question of the grill-me shape whose options are goals taken only from the description of the project in CLAUDE.md and one option in the person's own words, which it recommends, and offer no goal made up from the vault
method: "by hand: the Render of rule-skill-sprint-open in .claude/skills/sprint-open/SKILL.md read against the Criterion"
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [sprint, workflow, harness]
core: true
---

## Criterion

When:
The main agent starts `/sprint-open` of `.claude/skills/sprint-open/SKILL.md`, rendered from `rule-skill-sprint-open`, on `PreToolUse Skill`, or the person types `/sprint-open` on `UserPromptSubmit`, and the main agent dispatches `case-guppi` for the opening Case.

Then:
The prompt of the call asks that the opening Case ask the goal of the sprint, in every project and at every sprint, by a question of the shape that `.claude/skills/grill-me/SKILL.md` sets.
**＋** Each option of that question but one is a goal taken from the description of the project that `CLAUDE.md` holds between its project-description markers, as `rule-claude-md` sets them.
**＋** One option is the goal in the person's own words, and the recommended answer of the question is that option.
**＋** Where `CLAUDE.md` holds no description of the project, the option in the person's own words is the only option.
**－** No option of that question is a goal made up from the vault.

## Result

2026-10-31, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
