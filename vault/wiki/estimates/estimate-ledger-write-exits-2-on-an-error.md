---
type: estimate
kind: QA
status: pending
target: "[[rule-ledger-write]]"
purpose: Whether the ledger hook exits 2 with the error on stderr when it raises after reading the payload, once a stretch by its own refusal in the transcript, and exits 0 on an error while reading the payload
method: uv run pytest tests/test_ledger.py — piped payloads, a function of the hook patched to raise
checked: 2026-09-30
origin: raw/2026-09-30/1736/ledger.md#case-552.4
sprint: migration
created: 2026-09-30
tags: [session, hooks, harness, ledger]
---

## Criterion

When:
The `Stop` hook `uv run guppi ledger` fires, and an exception rises in `run` of `guppi/ledger.py` after it has read the payload: while it reads the transcript, the event log or the ledger, or while it judges or appends the lines.

Then:
The hook exits 2 with `ledger: ledger.md not written: <error>` on stderr, so the agent sees the error at the end of that reply.
**＋** A line not yet appended when the error rose waits for the next `Stop` of the session, which reads the transcript again.
**＋** While the cause stands, the error comes back at the first `Stop` of each stretch.
**－** An error while the hook reads the payload exits 0 with the error on stderr: the hook cannot tell its own refusal then, and exit 2 could loop.
**－** When a refusal of its own stands in the stretch, as `estimate-ledger-write-lifts` judges it, or when `stop_hook_active` is set and it cannot tell whether one stands, the hook exits 0 and prints nothing, so it cannot loop.
**－** A refusal of the hook with no error — no `hi`, or a refused line — keeps its own stderr line, and its exit as `estimate-ledger-write-lifts` sets it.

## Result

2026-09-30, uv run pytest tests/test_ledger.py: 63 passed

## History

- 2026-09-30 created · [[decision-case-552.4]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/2042/ledger.md#L31
- 2026-10-01 updated: the Criterion replaced whole — the error comes back once a stretch, judged by the hook's own refusal in the transcript, not by stop_hook_active (case 577.4) · [[decision-case-577.4]]
