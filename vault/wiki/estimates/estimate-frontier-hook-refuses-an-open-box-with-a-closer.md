---
type: estimate
kind: QA
status: passed
target: "[[rule-frontier-hook]]"
purpose: Whether an Edit, Write or MultiEdit of the frontier.md of a session folder that would leave a line with the box [ ] beside a closer is refused before it runs, with a reason that names the item and its closer, and every other call passes
method: uv run --project .guppi guppi test, which runs .guppi/tests/test_frontierguard.py
origin: raw/2026-11-02/2155/ledger.md#case-1012
sprint: plugin
created: 2026-11-02
tags: [hooks, harness, session]
---

## Criterion

When:
The agent calls `Edit`, `Write` or `MultiEdit` on a file `vault/raw/<date>/<HHMM>/frontier.md`, and the `PreToolUse` hook `uv run --project .guppi guppi frontierguard` of `.guppi/guppi/frontierguard.py` reads the payload.
**＋** Or `.guppi/tests/test_frontierguard.py` runs the hook over a made-up payload and a made-up `frontier.md`.

Then:
The hook works out the whole text the call would leave: the `content` of a `Write`, or the file with each `old_string` replaced by its `new_string` in order, once or at each match with `replace_all`, by the one function that `builder_write` of `.guppi/guppi/ratified.py` uses too.
**＋** When a box line of that text, under any heading, keeps the box `[ ]` while its last segment after ` · ` is a closer by `CLOSERS` of `.guppi/guppi/prespec.py`, the hook exits 2, and the call does not run.
**＋** The reason on stderr names each such item and its closer, and says that the box and the closer are written in one edit of the whole line, `[x]` for an item ended and `[-]` for an item put off.
**＋** Before the refusal one line goes to the day's `event_log.md`, since a blocked call has no `PostToolUse`.
**－** A text whose open lines carry no closer, a file other than such a `frontier.md`, and another tool exit 0.
**－** An old string missing or found more than once without `replace_all`, a file to edit that does not exist, and a payload the hook cannot read exit 0, the last with one line on stderr; the hook never raises.
**－** The check of the Frontier in `.guppi/guppi/prespec.py` stays as it is.

## Result

2026-11-03, uv run --project .guppi guppi test: 1921 passed, 6 skipped, 1 deselected; .guppi/tests/test_frontierguard.py 13 tests passed: an Edit that appends · case 7 to an open line exits 2 with "C2 (· case 7)" in the reason, the same Edit with the box [x] passes, a Write and a MultiEdit that leave such a line are refused, a replace_all edit is judged on every match, an open line with no closer, a frontier.md outside a session folder, another file and another tool pass, a missing old string, a missing file, an old string found twice and an unreadable payload pass, and a refusal writes one line to the event log

## History

- 2026-11-03 created · [[decision-case-1012]]
- 2026-11-03 status: pending → passed · raw/2026-11-02/2155/ledger.md#L19
