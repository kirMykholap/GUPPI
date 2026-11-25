---
type: estimate
kind: QA
status: passed
target: "[[rule-event-log]]"
purpose: Whether the event log keeps the whole path of a file that a tool call names, so that plan_path finds a plan file of any length
method: pytest in .guppi/tests/test_event.py with piped JSON payloads against a temp vault; by hand at Retro, a tool line of a Read, Write or Edit in the day's event log written after the change whose path is longer than 80 characters read against the Criterion and written into the estimate line
origin: raw/2026-11-25/0605/ledger.md#case-1045
sprint: plugin
created: 2026-11-25
tags: [session, hooks, harness]
---

## Criterion

When:
The `PostToolUse` hook `uv run --project .guppi guppi event tool` of `.guppi/guppi/event.py` reads through a pipe the payload of a tool call whose `tool_input` holds a `file_path` longer than 80 characters, and `plan_path` of `.guppi/guppi/ledger.py` then reads the event log of the session.

Then:
The `tool` line in `raw/<date>/event_log.md` holds the whole `file_path` on one line.
**＋** `plan_path` names a plan file under `.claude/plans/` whose path is longer than 80 characters.
**＋** A detail taken from `command`, `subagent_type`, `skill`, `pattern` or `description`, and the words of a free event, is still cut to 80 characters on one line.
**－** A line written before the change keeps its cut path, and `plan_path` skips it.

## Result

2026-11-25, Retro of session 0605: uv run --project .guppi pytest .guppi/tests/test_event.py 46 passed, among them test_a_long_file_path_stays_whole_and_plan_path_finds_it and test_a_long_pattern_is_still_cut_at_eighty_characters, the Bash test of 80 characters standing; line 606 of vault/raw/2026-11-25/event_log.md, written at 07:53:27 after the change, holds the tool Read line of C:\Users\kir\.claude\plans\frolicking-crafting-backus-of-16ad52b9-2613-43c4-8115-f092d2d530c2.md whole, 106 characters

## History

- 2026-11-25 created · [[decision-case-1045]]
- 2026-11-25 status: pending → passed · raw/2026-11-25/0605/ledger.md#L21
