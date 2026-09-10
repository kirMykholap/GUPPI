---
type: lesson
kind: knowledge
root_cause: the agent list is re-read during a session, at least after a file appears under .claude/agents/; this contradicts lesson-agents-loaded-at-session-start of session D, where three dispatches in the rendering session failed — the difference between the two sessions is not measured
status: clustered
estimates: [estimate-agents-visible-in-session]
insight: insight-harness-agent-visibility
origin: raw/2026-09-10/ledger.md#L80
sprint: migration
created: 2026-09-10
tags: [harness, hooks]
---

## Trigger

session E rendered .claude/agents/librarian-guppi.md by `guppi render` at about 10:40; the Agent tool listed `librarian-guppi` as available in the same session, at 10:52, before any restart

## Root cause

the agent list is re-read during a session, at least after a file appears under .claude/agents/; this contradicts lesson-agents-loaded-at-session-start of session D, where three dispatches in the rendering session failed — the difference between the two sessions is not measured

## Estimates

- [[estimate-agents-visible-in-session]]

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#L80
- 2026-09-10 updated: clustered by librarian: agent visibility, with lesson-agents-loaded-at-session-start · raw/2026-09-10/ledger.md#L80
