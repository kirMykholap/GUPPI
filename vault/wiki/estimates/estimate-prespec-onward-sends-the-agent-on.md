---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec-onward]]"
purpose: Whether guppi onward --plan refuses the end of a reply that leaves no Case open and no Case waiting in Plan Mode, sends the agent to /pre-spec or to the check and the exit, once a turn and not on a reply that opens with STOP, and is silent otherwise
method: uv run pytest tests/test_onward.py; by hand at the first Plan Mode after the render, the replies after the last ratification and after the ratification that follows the findings read in the transcript
checked: 2026-10-01
origin: raw/2026-09-30/2356/ledger.md#case-561.5
sprint: migration
created: 2026-09-30
tags: [session, workflow, hooks, harness]
---

## Criterion

When:
The `Stop` hook `uv run guppi onward --plan` receives the payload of the end of a reply of the main agent.

Then:
It exits 2 when all of these hold: the event log of the session's window holds a `hi` of this session; `raw/<date>/<hi HHMM>/spec.md` does not stand; `raw/<date>/<hi HHMM>/frontier.md` holds no open line under `## Cases`; the reply carries a `LEDGER` block; no file under `raw/<date>/<hi HHMM>/cases/` was written after the last decision line of its Case, or of a sub-case, in `raw/<date>/<hi HHMM>/ledger.md` or in that block; `stop_hook_active` is false; and the reply does not open with `STOP:`.
**＋** With no `prespec` line of this session after its `hi` in the event log, its reason on stderr tells the agent to call `/pre-spec` now.
**＋** With that line, its reason tells the agent to run `uv run guppi prespec --check` on the plan file with `--session <id>`, to fix what it prints, and to call `ExitPlanMode` when it prints no finding.
**＋** Each reason adds that, when only the person can go on — a Case still out with its `case-guppi`, or a question the person must answer — the agent opens its reply with `STOP:` and asks the person instead.
**＋** In every other case with no error of its own it exits 0 and prints nothing.
**＋** An error of its own after it has read the payload exits 2 with `onward: not checked: <error>` on stderr and the advice to call `/pre-spec`, or to run the check and exit Plan Mode, when no Case is left open; an empty payload exits 0.
**＋** `.claude/settings.json` registers it on `Stop`, after `uv run guppi onward`.
**－** On the re-fire (`stop_hook_active`) it exits 0, so it fires at most once a turn.
**－** It counts nothing, calls no model and writes no file and no mark: its judgment is the marks, the files and their times, the flag and the first word of the reply.
**－** `uv run guppi onward` without `--plan` keeps its own judgment, the run from Retro to `/handoff`.

## Result

2026-10-01, uv run pytest tests/test_onward.py: 25 passed; by hand, the first Plan Mode after the render, session 1237: after the defer reply of 14:08:36, the last line under Cases closed and its LEDGER block carried, guppi onward --plan exited 2 telling the agent to call /pre-spec now, with the STOP: clause; after the re-ratification of 567 and 569 at 14:19:47 it exited 2 telling the agent to run guppi prespec --check, fix what it prints and call ExitPlanMode; after the acknowledging replies of 567, 568 and 569 with Cases lines open it printed nothing; it fired once in each turn; unlike the observation of session 2356, it fired after a re-ratification whose decision lines the ledger already held

## History

- 2026-10-01 created · [[decision-case-561.5]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L39
