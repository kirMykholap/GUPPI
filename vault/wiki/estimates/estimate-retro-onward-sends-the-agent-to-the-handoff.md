---
type: estimate
kind: QA
status: passed
target: "[[rule-retro-onward]]"
purpose: Whether guppi onward refuses the end of a reply after the retro mark while handoff.md does not stand, once a stretch and once more after each reply the ledger hook refused, judged by the refusals in the transcript whatever stop_hook_active says, not on a reply that opens with STOP:, and is silent otherwise, counting nothing
method: "uv run pytest tests/test_onward.py tests/test_ledger.py; by hand at an end of Retro at which the ledger hook refuses a line: the transcript, the event log and handoff.md, recorded in the estimate line"
checked: 2026-10-04
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

2026-10-04, session 0004: `uv run pytest -q tests/test_onward.py tests/test_ledger.py` 120 passed; by hand, sessions 0317 (transcript 5b311f89) and 1416 (transcript 682b0e2f): after the retro marks of 05:04:23 and 14:39:41, `uv run guppi onward` refused the reply that ended Retro once each, at 05:06:02 and 14:40:45, its reason to commit the session folder and call /handoff, with the STOP: clause; the agent committed 37c47bd1 and a67b0339 and called /handoff at 05:06:09 and 14:40:53; at the last replies, 05:13:39 and 14:47:46, with handoff.md standing, it printed nothing; `.claude/settings.json` registers it on Stop after ledger, ratified, casecheck and context; not exercised: a refusal of the ledger hook — the person's word in this session: not met for long, a lesson if it comes —, a reply opening with STOP:

## History

- 2026-09-30 created · [[decision-case-531.9]]
- 2026-09-30 updated: the Criterion replaced whole — the exits 0 of the judgment hold with no error of the hook's own (case 555.4) · [[decision-case-555.4]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L3
- 2026-10-01 updated: the Criterion replaced whole — the hook fires once a stretch, judged by its own refusal in the transcript, and stop_hook_active no longer silences it (case 577.1) · [[decision-case-577.1]]
- 2026-10-02 updated: the Criterion replaced whole — the hook speaks again after each reply the ledger hook refused (case 596) · [[decision-case-596.1]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/0004/ledger.md#L15
