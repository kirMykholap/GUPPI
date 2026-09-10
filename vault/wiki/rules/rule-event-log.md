---
type: rule
kind: Leaf
purpose: Prevents the ledger from being written into a session nothing recorded
status: built
enforcement: hook
implementation_ref: [guppi/event.py, guppi/cli.py, .claude/settings.json]
parent: rule-session-start
estimates: [estimate-event-log-records]
origin: raw/2026-09-09/ledger.md#case-9
sprint: migration
created: 2026-09-09
tags: [session, hooks, harness]
---

## Purpose

Prevents the ledger from being written into a session nothing recorded. The event log is
the noisy record of a session — starts, tool calls, agent dispatches, commits, test runs —
written by hooks rather than by instructions, so it still fills when the agent deviates or
crashes. It is gitignored: debugging material, not traceability. Its one governance job is
to carry the `hi` mark that tells the ledger hook a working session is open.

## How it works

`uv run guppi event <name> [--session ID] [detail ...]` appends one line to
`vault/raw/<today>/event_log.md`, creating the folder and the file:

```
- 15:02:11 a1b2c3d4 session-start startup
- 15:02:40 -------- hi
- 15:03:05 a1b2c3d4 tool Bash: git status --short
- 15:04:12 a1b2c3d4 tool Agent: Explore
```

`- HH:MM:SS <first 8 of session_id, or -------- when unknown> <event> <detail>`. The
payload comes from stdin when a hook is the caller: `session_id`, `tool_name` and the most
telling field of `tool_input` (`command` cut to 80 characters on one line, `subagent_type`,
`skill`, `file_path`). Registered on `SessionStart` (`session-start`) and on `PostToolUse`
with no matcher (`tool`) — every tool, because this is a debugging record and a filter is
one more decision to maintain. `/hi` writes its own `hi` line through a `!` substitution,
with the session id when `CLAUDE_SESSION_ID` reaches a substitution and `--------` when it
does not.

The hook never fails the session: any error goes to stderr and the exit code is 0.

**Known limit.** With `--------` on the `hi` line, two sessions open at once in one
repository cannot be told apart by the ledger hook, which looks for a `hi` after the last
`session-start` of its own session. Sequential sessions are fine.

## Estimates

- [[estimate-event-log-records]]

## Parent

- [[rule-session-start]]

## Implementation

- `guppi/event.py`
- `guppi/cli.py`
- `.claude/settings.json`

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-9
- 2026-09-10 status: draft → built · cascade
