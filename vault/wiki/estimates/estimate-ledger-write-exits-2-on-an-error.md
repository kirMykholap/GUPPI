---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-write]]"
purpose: Whether the ledger hook exits 2 with the error on stderr when it raises after reading the payload, once a stretch by its own refusal in the transcript, and exits 0 on an error while reading the payload
method: uv run --project .guppi pytest .guppi/tests/test_ledger.py — piped payloads, a function of the hook patched to raise
checked: 2026-10-01
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, hooks, harness, ledger]
core: true
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi ledger` fires, and an exception rises in `run` of `.guppi/guppi/ledger.py` after it has read the payload: while it reads the transcript, the event log or the ledger, or while it judges or appends the lines.

Then:
The hook exits 2 with `ledger: ledger.md not written: <error>` on stderr, so the agent sees the error at the end of that reply.
**＋** A line not yet appended when the error rose waits for the next `Stop` of the session, which reads the transcript again.
**＋** While the cause stands, the error comes back at the first `Stop` of each stretch.
**－** An error while the hook reads the payload exits 0 with the error on stderr: the hook cannot tell its own refusal then, and exit 2 could loop.
**－** When a refusal of its own stands in the stretch, as `estimate-ledger-write-lifts` judges it, or when `stop_hook_active` is set and it cannot tell whether one stands, the hook exits 0 and prints nothing, so it cannot loop.
**－** A refusal of the hook with no error — no `hi`, or a refused line — keeps its own stderr line, and its exit as `estimate-ledger-write-lifts` sets it.

## Result

2026-10-01, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
