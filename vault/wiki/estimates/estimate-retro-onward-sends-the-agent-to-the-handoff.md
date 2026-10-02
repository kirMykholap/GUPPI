---
type: estimate
kind: QA
status: pending
target: "[[rule-retro-onward]]"
purpose: Whether guppi onward refuses the end of a reply after the retro mark while handoff.md does not stand, once a stretch and once more after each reply the ledger hook refused, judged by the refusals in the transcript whatever stop_hook_active says, not on a reply that opens with STOP:, and is silent otherwise, counting nothing
method: "uv run pytest tests/test_onward.py tests/test_ledger.py; by hand at the first end of Retro at which the ledger hook refuses a line: the transcript, the event log and handoff.md, recorded in the estimate line"
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
It exits 2 when the event log of the session's window holds the mark `retro` of this session, `raw/<date>/<hi HHMM>/handoff.md` does not stand, the reply that ended does not open with `STOP:`, and its own refusal is not spent.
**＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`. A refusal of a `Stop` hook is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line that opens with `[<command>]: `. Its own command is `uv run guppi onward`, and the command of the ledger hook is `uv run guppi ledger`.
**＋** Its own refusal is spent when its last refusal stands in the stretch and no refusal of the ledger hook follows the same reply of the agent or a later one. So after a reply that the ledger hook refused, it sends the agent on again at the end of the next reply, the one that writes the refused lines again.
**＋** A refusal of another `Stop` hook in the stretch neither silences it nor sends it on again, and neither does `stop_hook_active`.
**＋** Its reason on stderr tells the agent to commit the session folder and call `/handoff`, and, when a condition of `vault/wiki/where-to-stop.md` holds, to open its reply with `STOP:` and ask the person instead.
**＋** In every other case with no error of its own, it exits 0 and prints nothing. This holds before the mark `retro`, once `handoff.md` stands, once its own refusal is spent, on a reply that opens with `STOP:`, and with `stop_hook_active` set when it cannot read the transcript.
**＋** It judges the stretch and the refusals in it by `guppi/ledger.py`, whose function of the stretch the ledger hook calls too.
**＋** `.claude/settings.json` registers it on `Stop`, after `uv run guppi ledger`, `uv run guppi ratified`, `uv run guppi casecheck` and `uv run guppi context`.
**－** It counts nothing, reads no test result and calls no model. Its judgment is the mark, the file, the refusals in the transcript and the first word of the reply.
**－** Without a `hi` of the session in the event log, and with no error of its own, it exits 0.
**－** It writes no file and no mark.
**－** `uv run guppi onward --plan` keeps its own judgment, set by `rule-prespec-onward`.

## Result

2026-10-01, uv run pytest tests/test_onward.py: 25 passed; by hand, the transcript of session 4ba72976, vault/raw/2026-10-01/event_log.md and raw/2026-09-30/2356/handoff.md: after the retro mark of 03:09:42, guppi onward refused the reply that ended Retro at 03:10:52 once, its reason to commit the session folder and call /handoff with the STOP: clause; the agent committed at 03:11:01 and called /handoff at 03:11:02; the hook ran on Stop after ledger, ratified, casecheck and context; at the last reply, 03:18:55, with handoff.md standing since 03:11:35, it printed nothing; no reply opened with STOP: and no reply ended before the retro mark in that turn, so those clauses were read in the tests only

## History

- 2026-09-30 created · [[decision-case-531.9]]
- 2026-09-30 updated: the Criterion replaced whole — the exits 0 of the judgment hold with no error of the hook's own (case 555.4) · [[decision-case-555.4]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L3
- 2026-10-01 updated: the Criterion replaced whole — the hook fires once a stretch, judged by its own refusal in the transcript, and stop_hook_active no longer silences it (case 577.1) · [[decision-case-577.1]]
- 2026-10-02 updated: the Criterion replaced whole — the hook speaks again after each reply the ledger hook refused (case 596) · [[decision-case-596.1]]
