---
type: estimate
kind: QA
status: passed
target: "[[rule-bash-guard]]"
purpose: A heredoc with a backslash, a file write or an interpreter it feeds is refused before it runs, with a message that sends the agent to Write and Edit and says the refusal is no finding
method: uv run pytest tests/test_bashguard.py; the live reading is the first refusal of a session, its message read on stderr
checked: 2026-10-13
origin: raw/2026-09-14/1029/ledger.md#case-127
sprint: migration
created: 2026-09-14
tags: [hooks, harness]
---

## Criterion

When:
The agent calls `Bash`, and `uv run guppi bashguard` on `PreToolUse` reads `tool_input.command` of the payload and finds every heredoc (`<<` or `<<-`, the marker quoted or not) and its body up to the closing line.

Then:
A heredoc whose body holds a backslash, whose marker line writes a file (`>` or `>>` not to `/dev/null`, `tee`), or whose marker line runs an interpreter (`python`, `python3`, `py`, `uv run python`, `node`, `perl` or `ruby`) as one of its commands exits 2 with the reason on stderr: `bashguard: heredoc refused — <a backslash in its body | it writes <path> | it feeds <interpreter>>. Write a whole file with the Write tool and change a file with Edit, never through Bash; only a script goes into the scratchpad, written with the Write tool and run by path. The refusal is this guard working as designed, not an event of the session: do not report it at Retro.`
**＋** Before the refusal one line `- HH:MM:SS <stamp> bashguard refused: <reason>` goes to `raw/<date>/event_log.md`.
**＋** A `<<<` here-string, a heredoc with no backslash, no file write and no interpreter on its marker line, a command without a heredoc, another tool — exit 0.
**＋** A payload the hook cannot read — exit 0 with one line on stderr.
**－** An interpreter that runs a script by path, or takes it by `-c` or `-e`, is no reason to refuse.
**－** The hook never raises.

## Result

2026-10-13, Retro of session 1426, `uv run pytest tests/test_bashguard.py`: 20 passed; live: a Bash call `python - <<'EOF'` was refused on stderr with "bashguard: heredoc refused — it feeds python. Write a whole file with the Write tool …", and the event log holds `17:21:36 6f2e6cde bashguard refused: it feeds python`

## History

- 2026-09-14 created · [[decision-case-127]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1029/ledger.md#L35
- 2026-09-14 status: passed → passed · raw/2026-09-14/1229/ledger.md#L3
- 2026-09-24 updated: the Criterion replaced whole — the message says the refusal is by design; recut to the shape of case 193 (case 384) · [[decision-case-384]]
- 2026-09-24 status: pending → passed · raw/2026-09-23/1859/ledger.md#L28
- 2026-09-30 updated: the Criterion replaced whole — the refusal text sends a whole file to Write and only a script to the scratchpad (case 530.2) · [[decision-case-530.2]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/0248/ledger.md#L35
- 2026-10-13 updated: the Criterion replaced whole — a heredoc fed into an interpreter is refused (case 796.1) · [[decision-case-796.1]]
- 2026-10-13 status: pending → passed · raw/2026-10-13/1426/ledger.md#L25
