---
type: estimate
kind: QA
status: passed
target: "[[rule-bash-guard]]"
purpose: A heredoc with a backslash, a file write or an interpreter it feeds is refused before it runs, with a message that sends the agent to Write and Edit and says the refusal is no finding
method: uv run --project .guppi pytest .guppi/tests/test_bashguard.py; the live reading is the first refusal of a session, its message read on stderr
checked: 2026-10-13
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness]
core: true
---

## Criterion

When:
The agent calls `Bash`, and `uv run --project .guppi guppi bashguard` on `PreToolUse` reads `tool_input.command` of the payload and finds every heredoc (`<<` or `<<-`, the marker quoted or not) and its body up to the closing line.

Then:
A heredoc whose body holds a backslash, whose marker line writes a file (`>` or `>>` not to `/dev/null`, `tee`), or whose marker line runs an interpreter (`python`, `python3`, `py`, `uv run python`, `node`, `perl` or `ruby`) as one of its commands exits 2 with the reason on stderr: `bashguard: heredoc refused — <a backslash in its body | it writes <path> | it feeds <interpreter>>. Write a whole file with the Write tool and change a file with Edit, never through Bash; only a script goes into the scratchpad, written with the Write tool and run by path. The refusal is this guard working as designed, not an event of the session: do not report it at Retro.`
**＋** Before the refusal one line `- HH:MM:SS <stamp> bashguard refused: <reason>` goes to `raw/<date>/event_log.md`.
**＋** A `<<<` here-string, a heredoc with no backslash, no file write and no interpreter on its marker line, a command without a heredoc, another tool — exit 0.
**＋** A payload the hook cannot read — exit 0 with one line on stderr.
**－** An interpreter that runs a script by path, or takes it by `-c` or `-e`, is no reason to refuse.
**－** The hook never raises.

## Result

2026-10-13, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
