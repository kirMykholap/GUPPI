---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec-onward]]"
purpose: Whether guppi onward --plan, after /pre-spec, names each Case still out and sends the agent on with it while one is out, sends the agent to the check and the exit only when no Case is out and a file under cases/ that holds more than blank space was written after the last prespec line of the session, and on with the loop after the findings when none was; the emptied file of a dropped Case counts as none
method: uv run --project .guppi pytest .guppi/tests/test_onward.py — piped payloads, an event log with a prespec line and files under cases/ in a temp vault
checked: 2026-10-26
origin: raw/2026-10-06/0104/ledger.md#case-686.1
sprint: migration
created: 2026-10-06
tags: [session, workflow, hooks, harness]
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi onward --plan` of `.guppi/guppi/onward.py` receives the end of a reply of the main agent that carries a `LEDGER` block, the event log holds a `prespec` line of this session after its `hi`, and every other condition holds under which the hook sends the agent on.

Then:
When a Case is still out, as `rule-prespec-onward` judges it, the hook exits 2 and tells the agent that the Cases it names by id were built again and are not ratified yet: to send each one that must change to its `case-guppi`, as the loop after the findings of `/pre-spec` sets it. What the agent does when only the person can go on, or while a `case-guppi` has not answered, is the text that each reason adds, as `estimate-prespec-onward-sends-the-agent-on` sets it.
**＋** It names each Case still out by the N of its file `case-<N>.md` under `raw/<date>/<hi HHMM>/cases/`, found by the one function of `.guppi/guppi/onward.py` that judges whether a Case is still out.
**＋** When no Case is still out and a file under `raw/<date>/<hi HHMM>/cases/` was written after the last `prespec` line of the session, the hook exits 2 and tells the agent that the Cases built again on the findings of `/pre-spec` are ratified, to run `uv run --project .guppi guppi prespec --check` on the plan file with `--session <id>`, to fix what it prints, and to call `ExitPlanMode` when it prints no finding.
**＋** When no Case is still out and no file under `cases/` was written after that line, the hook exits 2 and tells the agent to go on with the loop after the findings of `/pre-spec`: to send each finding in a Case to its `case-guppi`, or, when no Case goes back, to run the check and exit as above.
**＋** The hook reads the time of the `prespec` line, on the date of the event log that holds it, through the one function of `.guppi/guppi/prespec.py` that `window` uses to find the line.
**＋** One function of `.guppi/guppi/casecheck.py` tells whether a file under `raw/<date>/<hi HHMM>/cases/` holds nothing but blank space, both for this judgment and for the judgment whether a Case is still out.
**－** While a Case is still out, the hook never tells the agent that the Cases built again are ratified, and never sends it on with the loop alone.
**－** A reply that writes a defer or a lesson after `/pre-spec` and before any Case is built again never gets the message that the Cases built again are ratified.
**－** An emptied file under `cases/`, the file of a dropped Case, is never taken for a Case built again after the `prespec` line, nor for a Case still out, whatever its time: with no other file written after that line, the agent is sent on with the loop after the findings.

## Result

2026-10-26, Retro of 0118, uv run --project .guppi pytest .guppi/tests/test_onward.py: 74 passed; the third reason names each Case still out by id (cases_out gives ["8", "9"] and not the ratified 5), holds case-guppi, orchestration.md and STOP:, holds neither the reason of the exit nor of the loop, and plan_onward and case_out read the ids from cases_out alone

## History

- 2026-10-06 created · [[decision-case-686.1]]
- 2026-10-06 status: pending → passed · raw/2026-10-06/0104/ledger.md#L35
- 2026-10-07 updated: the Criterion replaced whole — the emptied file of a dropped Case is no Case built again after /pre-spec (case 701.2) · [[decision-case-701.2]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/0425/ledger.md#L20
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-26 updated: the Criterion replaced whole — a third reason names each Case still out in place of the silence · [[decision-case-889.2]]
- 2026-10-26 status: pending → passed · raw/2026-10-26/0118/ledger.md#L19
