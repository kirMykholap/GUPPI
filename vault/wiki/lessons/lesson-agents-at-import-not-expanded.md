---
type: lesson
kind: knowledge
root_cause: an `@path` in an agent definition is passed to the subagent as literal text, unlike the imports of CLAUDE.md and the `@` lines of a skill; the agent must Read the file itself, one extra tool call per dispatch, and the index text lands in its context, not the caller's
status: new
source: session E 2026-09-10, the ask-guppi dispatch of the estimate-ask-finds reading (raw/2026-09-10/ledger.md#L3)
origin: raw/2026-09-10/ledger.md#L3
sprint: migration
created: 2026-09-10
tags: [harness, session]
---

## Trigger

the estimate-ask-finds reading, the agent was asked whether its `@vault/wiki/rules-index.md` line arrived expanded

## Root cause

an `@path` in an agent definition is passed to the subagent as literal text, unlike the imports of CLAUDE.md and the `@` lines of a skill; the agent must Read the file itself, one extra tool call per dispatch, and the index text lands in its context, not the caller's

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#L3
- 2026-09-11 estimates removed: a lesson has no Estimate · [[decision-case-53.1]]
- 2026-09-14 updated: tags and source filled (case 113) · [[decision-case-113]]
