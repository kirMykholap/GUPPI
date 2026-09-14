---
type: rule
kind: Leaf
purpose: Prevents a heredoc from carrying a backslash escape or writing a file through the Bash tool
status: built
enforcement: hook
implementation_ref: [guppi/bashguard.py, tests/test_bashguard.py, .claude/settings.json]
parent: "[[rule-harness]]"
estimates: ["[[estimate-bash-guard]]"]
origin: raw/2026-09-14/1029/ledger.md#case-127
sprint: migration
created: 2026-09-14
tags: [hooks, harness]
---

## Purpose

Prevents a heredoc from carrying a backslash escape or writing a file through the Bash
tool. On this Windows machine the tool's shell layer interprets backslash escapes inside a
heredoc body before the interpreter reads it, whatever the quoting of the marker; three
sessions (H, L, M) broke edit scripts that way with the lesson live, and a heredoc that
writes a file fails on quotes in its body. A lesson the agent has to remember is not a
rule; a `PreToolUse` hook cannot be skipped.

## How it works

`uv run guppi bashguard` on `PreToolUse` of `Bash`. It reads `tool_input.command`, finds
every heredoc (`<<` or `<<-`, the marker quoted or not) and its body up to the closing
line. A body with a backslash, or a marker line that redirects into a file (`>` or `>>`
not to `/dev/null`, `tee`), exits 2 with the reason on stderr — `bashguard: heredoc
refused — <a backslash in its body | it writes <path>>. Write the script with the Write
tool into the scratchpad and run it by path; change a file with Edit.` — which blocks
the call; one line `bashguard: <reason>` goes to `vault/raw/<date>/event_log.md` before
that (case 91). A `<<<` here-string, a heredoc without a backslash whose output goes to a
pipe or the screen, a command without a heredoc, any other tool, or a payload the hook
cannot read: exit 0, the last with one line on stderr. The hook never raises (case 127).

## Estimates

- [[estimate-bash-guard]]

## Parent

- [[rule-harness]]

## Implementation

- `guppi/bashguard.py`
- `tests/test_bashguard.py`
- `.claude/settings.json`

## History

- 2026-09-14 deferred, placeholder · [[decision-case-120]]
- 2026-09-14 defer by decision-case-120 superseded · [[decision-case-127]]
- 2026-09-14 created over placeholder · [[decision-case-127]]
- 2026-09-14 estimate estimate-bash-guard added · [[decision-case-127]]
- 2026-09-14 status: draft → built · cascade
