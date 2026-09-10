---
type: lesson
kind: knowledge
root_cause: an `@path` in an agent definition is passed to the subagent as literal text, unlike the imports of CLAUDE.md and the `@` lines of a skill; the agent must Read the file itself, one extra tool call per dispatch, and the index text lands in its context, not the caller's
status: new
estimates: [estimate-agents-at-import-not-expanded]
origin: raw/2026-09-10/ledger.md#L3
sprint: migration
created: 2026-09-10
---

## Trigger

the estimate-ask-finds reading, the agent was asked whether its `@vault/wiki/rules-index.md` line arrived expanded

## Root cause

an `@path` in an agent definition is passed to the subagent as literal text, unlike the imports of CLAUDE.md and the `@` lines of a skill; the agent must Read the file itself, one extra tool call per dispatch, and the index text lands in its context, not the caller's

## Estimates

- [[estimate-agents-at-import-not-expanded]]

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#L3
