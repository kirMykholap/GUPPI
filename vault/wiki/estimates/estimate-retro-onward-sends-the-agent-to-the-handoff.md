---
type: estimate
kind: QA
status: pending
target: "[[rule-retro-onward]]"
purpose: Whether guppi onward refuses the end of a reply after the retro mark while handoff.md does not stand, once a stretch by its own refusal in the transcript whatever stop_hook_active says, not on a reply that opens with STOP:, and is silent otherwise, counting nothing
method: "uv run pytest tests/test_onward.py; by hand at the first end of Retro after the render that follows a refusal of another Stop hook in the same stretch: the transcript, the event log and handoff.md, recorded in the estimate line"
checked: 2026-10-01
origin: raw/2026-09-29/2024/ledger.md#case-531.9
sprint: migration
created: 2026-09-29
tags: [session, workflow, hooks, harness]
---

## Criterion

When:
The `Stop` hook `uv run guppi onward` receives the payload of the end of a reply of the main agent.

Then:
It exits 2 when the event log of the session's window holds the mark `retro` of this session, `raw/<date>/<hi HHMM>/handoff.md` does not stand, the reply that ended does not open with `STOP:`, and its own refusal does not stand in the stretch.
**＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`. Its own refusal is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line that opens with `[uv run guppi onward]: `.
**＋** A refusal of another `Stop` hook in the stretch does not silence it, and neither does `stop_hook_active`.
**＋** Its reason on stderr tells the agent to commit the session folder and call `/handoff`, and, when a condition of `vault/wiki/where-to-stop.md` holds, to open its reply with `STOP:` and ask the person instead.
**＋** In every other case with no error of its own it exits 0 and prints nothing: before the mark `retro`, once `handoff.md` stands, once its own refusal stands in the stretch, on a reply that opens with `STOP:`, and with `stop_hook_active` set when it cannot read the transcript.
**＋** It judges the stretch and its own refusal by the one function of `guppi/ledger.py` that the ledger hook calls.
**＋** `.claude/settings.json` registers it on `Stop`, after `uv run guppi ledger`, `uv run guppi ratified`, `uv run guppi casecheck` and `uv run guppi context`.
**－** It counts nothing, reads no test result and calls no model: its judgment is the mark, the file, its own refusal in the transcript and the first word of the reply.
**－** Without a `hi` of the session in the event log, and with no error of its own, it exits 0.
**－** It writes no file and no mark.
**－** `uv run guppi onward --plan` keeps `stop_hook_active` as its guard.

## Result

2026-10-01, uv run pytest tests/test_onward.py: 25 passed; by hand, the transcript of session 4ba72976, vault/raw/2026-10-01/event_log.md and raw/2026-09-30/2356/handoff.md: after the retro mark of 03:09:42, guppi onward refused the reply that ended Retro at 03:10:52 once, its reason to commit the session folder and call /handoff with the STOP: clause; the agent committed at 03:11:01 and called /handoff at 03:11:02; the hook ran on Stop after ledger, ratified, casecheck and context; at the last reply, 03:18:55, with handoff.md standing since 03:11:35, it printed nothing; no reply opened with STOP: and no reply ended before the retro mark in that turn, so those clauses were read in the tests only

## History

- 2026-09-30 created · [[decision-case-531.9]]
- 2026-09-30 updated: the Criterion replaced whole — the exits 0 of the judgment hold with no error of the hook's own (case 555.4) · [[decision-case-555.4]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L3
- 2026-10-01 updated: the Criterion replaced whole — the hook fires once a stretch, judged by its own refusal in the transcript, and stop_hook_active no longer silences it (case 577.1) · [[decision-case-577.1]]
