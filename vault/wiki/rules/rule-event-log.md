---
type: rule
kind: Leaf
purpose: Prevents the ledger from being written into a session nothing recorded
status: draft
enforcement: hook
implementation_ref: [guppi/event.py, guppi/gate.py, guppi/cli.py, tests/test_gate.py, tests/test_event.py, .claude/settings.json]
parent: "[[rule-session-start]]"
estimates: ["[[estimate-event-log-records]]"]
origin: raw/2026-09-09/ledger.md#case-9
sprint: migration
created: 2026-09-09
tags: [session, hooks, harness]
---

## Purpose

Prevents the ledger from being written into a session nothing recorded. The event log is
the noisy record of a session — starts, tool calls, agent dispatches, commits, test runs —
written by hooks rather than by instructions, so it still fills when the agent deviates or
crashes. It is gitignored: debugging material, not traceability. Its governance jobs: to carry the `hi` mark that tells the ledger hook a working session is open, and to name the session's plan file by its `tool Write:` and `tool Edit:` lines for `guppi gate` (case 122).

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
one more decision to maintain. The `hi` line is written by `guppi event prompt` on `UserPromptSubmit`: when the prompt, trimmed, is `/hi` or starts with `/hi `, and no `hi` of this session's stamp follows its first `session-start` in the logs the ledger hook walks, the log gains `- HH:MM:SS <stamp> hi`, the stamp from the payload's `session_id`; a second `/hi` of the same session and any other prompt write nothing (case 111.1); a `/hi` whose `permission_mode` is not `plan`, missing or empty included, writes no line, prints nothing on stdout and exits 2 with the reason on stderr, and Claude Code blocks the prompt (case 445.6). Having written the line, the hook prints `hi: HH:MM:SS <stamp> → raw/<date>/<HHMM>/` on stdout, which Claude Code adds to the context; when a `hi` of this session already exists it prints `hi: already recorded at HH:MM:SS → raw/<date>/<HHMM>/`; on any other prompt it is silent. The `/hi` skill takes the time of the session's folder from that line (case 125). The marks `prespec`, `retro` and `handoff` are written by `guppi gate` — on `PreToolUse Skill` for the agent's call, on `UserPromptSubmit` for the person's typed command (case 169.1) — when it lets the call through, one line `- HH:MM:SS <stamp> <mark>` with the stamp from the payload's `session_id`; a refused call leaves no mark. Until case 136.1 the three skills wrote them through a `!` substitution where `CLAUDE_SESSION_ID` is empty, so every mark read `--------` (case 136.1).

The hook never fails the session on an error: any error goes to stderr and the exit code is 0; its one exit 2 is the refusal of a `/hi` outside plan mode (case 445.6).

**A limit lifted.** Until case 111 the `hi` line carried `--------` and the ledger hook looked for a `hi` after the last `session-start` of its own session, so two sessions open at once could not be told apart; on 2026-09-14 a session restored by `resume` in the same second took the `hi` of the session that typed it. With the stamp on the `hi` line a `hi` of one session never belongs to another (case 111.1).

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-9
- 2026-09-10 status: draft → built · cascade
- 2026-09-14 updated: the hi line is written by guppi event prompt on UserPromptSubmit with the session's stamp, once per session; the known limit is lifted (case 111.1) · [[decision-case-111.1]]
- 2026-09-14 status: built → draft · cascade
- 2026-09-14 updated: the prompt hook prints the hi it wrote, or the one already recorded, with the session's folder, into the context (case 125) · [[decision-case-125]]
- 2026-09-14 updated: the event log's second governance job, the plan path for guppi gate, named (case 132) · [[decision-case-132]]
- 2026-09-14 status: draft → built · cascade
- 2026-09-14 updated: the marks pretask, retro, handoff written by guppi gate with the session's stamp; the skills' Recorded lines dropped (case 136.1) · [[decision-case-136.1]]
- 2026-09-15 updated: the marks name the second entry of the gate, the typed command on UserPromptSubmit (case 169.1) · [[decision-case-169.1]]
- 2026-09-27 updated: no hi line outside plan mode; the refusal exits 2 (case 445.6) · [[decision-case-445.6]]
- 2026-09-27 status: built → draft · cascade
