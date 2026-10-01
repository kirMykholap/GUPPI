---
type: estimate
kind: QA
status: passed
target: "[[rule-retro-onward]]"
purpose: Whether guppi onward exits 2 with the error and the advice to call /handoff on stderr when it raises after reading the payload, and exits 0 on the re-fire and on an empty payload
method: uv run pytest tests/test_onward.py — piped payloads, a function of the hook patched to raise
checked: 2026-10-01
origin: raw/2026-09-30/2042/ledger.md#case-555.3
sprint: migration
created: 2026-09-30
tags: [session, workflow, hooks, harness]
---

## Criterion

When:
The `Stop` hook `uv run guppi onward` fires, and an exception rises in `guppi/onward.py` after the hook has read the payload: while it reads the reply, the session folder or the event log.

Then:
`guppi onward` exits 2. Its stderr holds `onward: not checked: <error>` and the advice: if Retro has ended and `handoff.md` does not stand, commit the session folder and call `/handoff`.
**＋** While the cause stands, `guppi onward` blocks with the same error at every `Stop` of the session, before Retro too.
**－** An empty payload of `guppi onward` exits 0 with nothing on stderr.
**－** On the re-fire after a block (`stop_hook_active`), `guppi onward` exits 0 and prints nothing, so it fires at most once a turn.
**－** With no error, `guppi onward` exits 2 or 0 by its own judgment, as before.

## Result

2026-10-01, uv run pytest tests/test_onward.py: 25 passed (-k error: 4 passed), the run without --plan unchanged beside the new --plan run of case 561.5

## History

- 2026-09-30 created · [[decision-case-555.3]]
- 2026-10-01 status: pending → passed · raw/2026-09-30/2356/ledger.md#L42
