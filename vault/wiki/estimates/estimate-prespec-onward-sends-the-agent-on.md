---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec-onward]]"
purpose: Whether guppi onward --plan refuses the end of a reply that leaves no Case open and no Case waiting in Plan Mode, sends the agent to /pre-spec or to the check and the exit, once a stretch and once more after each reply the ledger hook refused, judged by the refusals in the transcript whatever stop_hook_active says, not on a reply that opens with STOP:, and is silent otherwise
method: "uv run pytest tests/test_onward.py tests/test_ledger.py; by hand at a Plan Mode at which the ledger hook refuses a line of the reply that acknowledges the last ratification: the transcript, the event log and frontier.md, recorded in the estimate line"
checked: 2026-10-04
origin: raw/2026-09-30/2356/ledger.md#case-561.5
sprint: migration
created: 2026-09-30
tags: [session, workflow, hooks, harness]
---

## Criterion

When:
The `Stop` hook `uv run guppi onward --plan` receives the payload of the end of a reply of the main agent.

Then:
It exits 2 when all of these hold: the event log of the session's window holds a `hi` of this session; `raw/<date>/<hi HHMM>/spec.md` does not stand; `raw/<date>/<hi HHMM>/frontier.md` holds no open line under `## Cases`; the reply carries a `LEDGER` block; no Case is still out, as `rule-prespec-onward` judges it; its own refusal is not spent; and the reply does not open with `STOP:`.
**＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`. A refusal of a `Stop` hook is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line that opens with `[<command>]: `. Its own command is `uv run guppi onward --plan`, and the command of the ledger hook is `uv run guppi ledger`.
**＋** Its own refusal is spent when its last refusal stands in the stretch and no refusal of the ledger hook follows the same reply of the agent or a later one, judged by `guppi/ledger.py`. So after a reply that the ledger hook refused, it sends the agent on again at the end of the next reply, the one that writes the refused lines again.
**＋** A refusal of another `Stop` hook in the stretch neither silences it nor sends it on again, and neither does `stop_hook_active`.
**＋** With no `prespec` line of this session after its `hi` in the event log, its reason on stderr tells the agent to call `/pre-spec` now. With that line, its reason tells the agent to run `uv run guppi prespec --check` on the plan file with `--session <id>`, to fix what it prints, and to call `ExitPlanMode` when it prints no finding.
**＋** Each reason adds that, when only the person can go on — a Case still out with its `case-guppi`, or a question the person must answer — the agent opens its reply with `STOP:` and asks the person instead.
**＋** In every other case with no error of its own, it exits 0 and prints nothing. This holds once its own refusal is spent, on a reply that opens with `STOP:`, and with `stop_hook_active` set when it cannot read the transcript.
**＋** `.claude/settings.json` registers it on `Stop`, after `uv run guppi onward`.
**－** An error of its own after it has read the payload exits 2 with `onward: not checked: <error>` on stderr and the advice to call `/pre-spec`, or to run the check and exit Plan Mode, when no Case is left open. It does so at most once a stretch, judged by its own refusal in the stretch alone. An empty payload exits 0.
**－** It counts nothing, calls no model and writes no file and no mark. Its judgment is the marks, the files and their times, the refusals in the transcript and the first word of the reply.
**－** `uv run guppi onward` without `--plan` keeps its own judgment.

## Result

2026-10-04, session 0004: `uv run pytest -q tests/test_onward.py tests/test_ledger.py` 120 passed; by hand, the Plan Mode of session 1341 (transcript 26e79919): after the reply of 14:08:30 that closed the last open line under Cases and carried a LEDGER block of defers, `uv run guppi onward --plan` refused once at 14:08:32, with no prespec line of the session yet, telling the agent to call /pre-spec now, with the STOP: clause, and the agent called /pre-spec at 14:08:34; after the re-ratification of 614 at 14:12:49, the prespec line standing since 14:08:34, it refused once at 14:12:51 telling the agent to run `uv run guppi prespec --check`, fix what it prints and call ExitPlanMode, which the agent did at 14:12:54 and 14:12:59; after the acknowledging reply of 614 at 14:06:39, lines under Cases open, it printed nothing, and in session 0004 it printed nothing after the acknowledging replies of 619 and 620, lines under Cases open; `.claude/settings.json` registers it on Stop after `uv run guppi onward`; not exercised: a refusal of the ledger hook — the person's word in this session: not met for long, a lesson if it comes —, an error of its own

## History

- 2026-10-01 created · [[decision-case-561.5]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L39
- 2026-10-02 updated: the Criterion replaced whole — the run speaks again after each reply the ledger hook refused (case 597.1) · [[decision-case-597.1]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/0004/ledger.md#L14
