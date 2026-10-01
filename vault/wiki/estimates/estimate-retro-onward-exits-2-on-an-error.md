---
type: estimate
kind: QA
status: pending
target: "[[rule-retro-onward]]"
purpose: Whether guppi onward exits 2 with the error and the advice to call /handoff on stderr when it raises after reading the payload, once a stretch by its own refusal in the transcript, and exits 0 on an empty payload
method: uv run pytest tests/test_onward.py — piped payloads, a function of the hook patched to raise
checked: 2026-10-01
origin: raw/2026-09-30/2042/ledger.md#case-555.3
sprint: migration
created: 2026-09-30
tags: [session, workflow, hooks, harness]
---

## Criterion

When:
The `Stop` hook `uv run guppi onward` fires, and an exception rises in `guppi/onward.py` after the hook has read the payload: while it reads the reply, the session folder, the event log or the transcript.

Then:
`guppi onward` exits 2. Its stderr holds `onward: not checked: <error>` and the advice: if Retro has ended and `handoff.md` does not stand, commit the session folder and call `/handoff`.
**＋** While the cause stands, `guppi onward` blocks with the same error at the first `Stop` of each stretch of the session, before Retro too.
**－** An empty payload of `guppi onward` exits 0 with nothing on stderr.
**－** It exits 0 and prints nothing when its own refusal stands in the stretch, as `estimate-retro-onward-sends-the-agent-to-the-handoff` judges it, or when `stop_hook_active` is set and it cannot tell whether one stands, so it fires at most once a stretch.
**－** With no error, `guppi onward` exits 2 or 0 by its own judgment, as before.

## Result

2026-10-01, uv run pytest tests/test_onward.py: 25 passed (-k error: 4 passed), the run without --plan unchanged beside the new --plan run of case 561.5

## History

- 2026-09-30 created · [[decision-case-555.3]]
- 2026-10-01 status: pending → passed · raw/2026-09-30/2356/ledger.md#L42
- 2026-10-01 updated: the Criterion replaced whole — the error comes back once a stretch, judged by the hook's own refusal in the transcript, not by stop_hook_active (case 577.2) · [[decision-case-577.2]]
