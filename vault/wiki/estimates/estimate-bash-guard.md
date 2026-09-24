---
type: estimate
kind: QA
status: passed
target: "[[rule-bash-guard]]"
purpose: A heredoc with a backslash or a file write is refused before it runs, with a message that sends the agent to Write and says the refusal is no finding
method: uv run pytest tests/test_bashguard.py; the live reading is the first refusal of a session, its message read on stderr
checked: 2026-09-24
origin: raw/2026-09-14/1029/ledger.md#case-127
sprint: migration
created: 2026-09-14
tags: [hooks, harness]
---

## Criterion

When:
The agent calls `Bash`, and `uv run guppi bashguard` on `PreToolUse` reads `tool_input.command` of the payload and finds every heredoc (`<<` or `<<-`, the marker quoted or not) and its body up to the closing line.

Then:
A body with a backslash, or a marker line that writes a file (`>` or `>>` not to `/dev/null`, `tee`), exits 2 with the reason on stderr: `bashguard: heredoc refused — <a backslash in its body | it writes <path>>. Write the script with the Write tool into the scratchpad and run it by path; change a file with Edit. The refusal is this guard working as designed, not an event of the session: do not report it at Retro.`
**＋** Before the refusal one line `- HH:MM:SS <stamp> bashguard refused: <reason>` goes to `raw/<date>/event_log.md`.
**＋** A `<<<` here-string, a heredoc with no backslash and no file write, a command without a heredoc, another tool — exit 0.
**＋** A payload the hook cannot read — exit 0 with one line on stderr.
**－** The hook never raises.

## Result

2026-09-24, uv run pytest tests/test_bashguard.py: 15 passed, the refusal test checks the new sentence; live in session 1859: two heredoc refusals after the change carried on stderr "The refusal is this guard working as designed, not an event of the session: do not report it at Retro."

## History

- 2026-09-14 created · [[decision-case-127]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1029/ledger.md#L35
- 2026-09-14 status: passed → passed · raw/2026-09-14/1229/ledger.md#L3
- 2026-09-24 updated: the Criterion replaced whole — the message says the refusal is by design; recut to the shape of case 193 (case 384) · [[decision-case-384]]
- 2026-09-24 status: pending → passed · raw/2026-09-23/1859/ledger.md#L28
