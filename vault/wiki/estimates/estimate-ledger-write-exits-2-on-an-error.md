---
type: estimate
kind: QA
status: pending
target: "[[rule-ledger-write]]"
purpose: Whether the ledger hook exits 2 with the error on stderr when it raises after reading the payload, and exits 0 on an error while reading the payload and on the re-fire
method: uv run pytest tests/test_ledger.py — piped payloads, a function of the hook patched to raise
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
**＋** While the cause stands, the error comes back at every `Stop`.
**－** An error while the hook reads the payload exits 0 with the error on stderr: the hook cannot tell a re-fire then, and exit 2 could loop.
**－** With `stop_hook_active` (the re-fire after a block) the hook exits 0 and writes nothing, so it cannot loop.
**－** A refusal of the hook with no error — no `hi`, or a refused line — keeps its own stderr line and exit.

## History

- 2026-09-30 created · [[decision-case-552.4]]
