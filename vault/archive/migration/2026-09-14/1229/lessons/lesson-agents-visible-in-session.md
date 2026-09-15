---
type: lesson
kind: knowledge
root_cause: the agent list is re-read during a session, at least after a file appears under .claude/agents/; this contradicts lesson-agents-loaded-at-session-start of session D, where three dispatches in the rendering session failed — the difference between the two sessions is not measured
status: archived
source: session E 2026-09-10, the Agent tool listing librarian-guppi at 10:52 after guppi render at 10:40 (raw/2026-09-10/ledger.md#L80)
insight: "[[insight-harness-agent-visibility]]"
origin: raw/2026-09-10/ledger.md#L80
sprint: migration
created: 2026-09-10
tags: [harness, hooks]
---

## Trigger

session E rendered .claude/agents/librarian-guppi.md by `guppi render` at about 10:40; the Agent tool listed `librarian-guppi` as available in the same session, at 10:52, before any restart

## Root cause

the agent list is re-read during a session, at least after a file appears under .claude/agents/; this contradicts lesson-agents-loaded-at-session-start of session D, where three dispatches in the rendering session failed — the difference between the two sessions is not measured

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#L80
- 2026-09-10 updated: clustered by librarian: agent visibility, with lesson-agents-loaded-at-session-start · raw/2026-09-10/ledger.md#L80
- 2026-09-11 estimates removed: a lesson has no Estimate · [[decision-case-53.1]]
- 2026-09-14 insight section derived
- 2026-09-14 updated: source filled (case 113) · [[decision-case-113]]
- 2026-09-14 archived · insight actioned
- 2026-09-14 archived · cleanup
