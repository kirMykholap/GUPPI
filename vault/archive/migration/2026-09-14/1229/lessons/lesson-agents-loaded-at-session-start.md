---
type: lesson
kind: error
root_cause: Claude Code reads agent definitions at session start and skills on demand; a rendered agent is usable only from the next session, so an Estimate on a new agent cannot be read in the session that creates it
status: archived
insight: "[[insight-harness-agent-visibility]]"
origin: raw/2026-09-09/ledger.md#L90
sprint: migration
created: 2026-09-09
tags: [harness, render, session]
---

## Trigger

session D rendered .claude/agents/ask-guppi.md and dispatched it three times in the same session; every call failed with "Agent type 'ask-guppi' not found", while the skill .claude/skills/pre-task/SKILL.md rendered minutes earlier was invocable at once

## Root cause

Claude Code reads agent definitions at session start and skills on demand; a rendered agent is usable only from the next session, so an Estimate on a new agent cannot be read in the session that creates it

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#L90
- 2026-09-10 updated: clustered by librarian: agent visibility, with lesson-agents-visible-in-session · raw/2026-09-10/ledger.md#L80
- 2026-09-11 estimates removed: a lesson has no Estimate · [[decision-case-53.1]]
- 2026-09-14 insight section derived
- 2026-09-14 updated: tags filled (case 113) · [[decision-case-113]]
- 2026-09-14 archived · insight actioned
- 2026-09-14 archived · cleanup
