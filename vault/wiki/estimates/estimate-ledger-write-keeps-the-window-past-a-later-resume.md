---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-write]]"
purpose: A session resumed or compacted on a later date than its /hi, or whose log on a later date holds a tool line with the text of its start line, keeps its hi, its folder and its plan file in every reader of its window
method: uv run --project .guppi pytest .guppi/tests/test_ledger.py -k later_date
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, hooks, ledger]
core: true
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi ledger` of `.guppi/guppi/ledger.py`, or `uv run --project .guppi guppi caseid --next --session <stamp>` of `.guppi/guppi/caseid.py`, runs on a later date than the `hi` of the session, and the event log of a later date holds a start line of the stamp of the kind `resume` or `compact`, or a tool line whose text holds the stamp, a space and the word `session-start`.

Then:
`session_event_logs` of `.guppi/guppi/ledger.py` walks back past each start line of the stamp of the kind `resume`, `compact` or `clear`, and stops at the newest date that holds a `startup` or a `fork` start line of the stamp, a line of the form `- HH:MM:SS <stamp> session-start <kind>`.
**＋** `session_dir` names the folder of the date and the time of the session's `hi`, and the ledger hook writes the lines of the session into its `ledger.md`.
**＋** `plan_path` names the plan file that the session wrote before the resume, so `guppi caseid` prints an id.
**－** With no `startup` or `fork` start line of the stamp on any date, the walk reads every event log up to today, and the window opens at the first start line of the stamp.
**－** A `startup` start line of the stamp on a later date than an older `hi` still ends the walk, so that older `hi` opens no window.
**－** A tool line whose text holds the stamp and the word `session-start`, such as a logged search or command, ends no walk.

## Result

2026-10-26, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
