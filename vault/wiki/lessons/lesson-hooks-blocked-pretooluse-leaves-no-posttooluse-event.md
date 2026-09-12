---
type: lesson
kind: knowledge
root_cause: Claude Code fires PostToolUse only for a tool that ran; a tool blocked by a PreToolUse hook has no PostToolUse, so a refusal is visible only on stderr unless the blocking hook writes its own event line
status: new
source: live probe 2026-09-12 session J, uv run guppi guard on an Edit of .claude/skills/hi/SKILL.md; raw/2026-09-12/event_log.md
origin: raw/2026-09-12/ledger.md#L156
sprint: migration
created: 2026-09-12
tags: [hooks, harness]
---

## Trigger

the guard refused the Edit with exit 2 and the rule named, and the event log gained no line for the call, though guppi event tool logs every PostToolUse

## Root cause

Claude Code fires PostToolUse only for a tool that ran; a tool blocked by a PreToolUse hook has no PostToolUse, so a refusal is visible only on stderr unless the blocking hook writes its own event line

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#L156
