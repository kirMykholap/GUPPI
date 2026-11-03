---
type: estimate
kind: QA
status: passed
target: "[[rule-retro-onward]]"
purpose: Whether guppi onward refuses the end of a reply after the retro mark while handoff.md does not stand, once a stretch and once more after each reply the ledger hook refused, judged by the refusals in the transcript whatever stop_hook_active says, not on a reply that opens with STOP:, and is silent otherwise, counting nothing
method: "uv run --project .guppi pytest .guppi/tests/test_onward.py .guppi/tests/test_ledger.py, which cover a refusal of the ledger hook; by hand at an end of Retro: the transcript, the event log and handoff.md, recorded in the estimate line"
checked: 2026-10-04
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, hooks, harness]
core: true
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi onward` receives the payload of the end of a reply of the main agent.

Then:
It exits 2 when the event log of the session's window holds the mark `retro` of this session, `raw/<date>/<hi HHMM>/handoff.md` does not stand, the reply that ended does not open with `STOP:`, and its own refusal is not spent.
**＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`. A refusal of a `Stop` hook is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line that opens with `[<command>]: `. Its own command is `uv run --project .guppi guppi onward`, and the command of the ledger hook is `uv run --project .guppi guppi ledger`.
**＋** Its own refusal is spent when its last refusal stands in the stretch and no refusal of the ledger hook follows the same reply of the agent or a later one. So after a reply that the ledger hook refused, it sends the agent on again at the end of the next reply, the one that writes the refused lines again.
**＋** A refusal of another `Stop` hook in the stretch neither silences it nor sends it on again, and neither does `stop_hook_active`.
**＋** Its reason on stderr tells the agent to commit the session folder and call `/handoff`, and, when a condition of `vault/wiki/where-to-stop.md` holds, to open its reply with `STOP:` and ask the person instead.
**＋** In every other case with no error of its own, it exits 0 and prints nothing. This holds before the mark `retro`, once `handoff.md` stands, once its own refusal is spent, on a reply that opens with `STOP:`, and with `stop_hook_active` set when it cannot read the transcript.
**＋** It judges the stretch and the refusals in it by `.guppi/guppi/ledger.py`, whose function of the stretch the ledger hook calls too.
**＋** `.claude/settings.json` registers it on `Stop`, after `uv run --project .guppi guppi ledger`, `uv run --project .guppi guppi ratified`, `uv run --project .guppi guppi casecheck` and `uv run --project .guppi guppi context`.
**－** It counts nothing, reads no test result and calls no model. Its judgment is the mark, the file, the refusals in the transcript and the first word of the reply.
**－** Without a `hi` of the session in the event log, and with no error of its own, it exits 0.
**－** It writes no file and no mark.
**－** `uv run --project .guppi guppi onward --plan` keeps its own judgment, set by `rule-prespec-onward`.

## Result

2026-10-04, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
