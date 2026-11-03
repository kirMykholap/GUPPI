---
type: estimate
kind: QA
status: passed
target: "[[rule-retro-onward]]"
purpose: Whether guppi onward exits 2 with the error and the advice to call /handoff on stderr when it raises after reading the payload, once a stretch by its own refusal in the transcript, and exits 0 on an empty payload
method: uv run --project .guppi pytest .guppi/tests/test_onward.py — piped payloads, a function of the hook patched to raise
checked: 2026-10-03
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, hooks, harness]
core: true
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi onward` fires, and an exception rises in `.guppi/guppi/onward.py` after the hook has read the payload: while it reads the reply, the session folder, the event log or the transcript.

Then:
`guppi onward` exits 2. Its stderr holds `onward: not checked: <error>` and the advice: if Retro has ended and `handoff.md` does not stand, commit the session folder and call `/handoff`.
**＋** While the cause stands, `guppi onward` blocks with the same error at the first `Stop` of each stretch of the session, before Retro too.
**－** An empty payload of `guppi onward` exits 0 with nothing on stderr.
**－** It exits 0 and prints nothing when its own refusal stands in the stretch, as `estimate-retro-onward-sends-the-agent-to-the-handoff` defines the stretch and its own refusal, whatever the ledger hook refused after it. It also exits 0 when `stop_hook_active` is set and it cannot tell whether one stands, so it fires at most once a stretch.
**－** With no error, `guppi onward` exits 2 or 0 by its own judgment, as before.

## Result

2026-10-03, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
