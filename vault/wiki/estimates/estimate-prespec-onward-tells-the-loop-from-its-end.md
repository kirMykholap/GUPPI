---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec-onward]]"
purpose: Whether guppi onward --plan, after /pre-spec, sends the agent to the check and the exit only when a file under cases/ was written after the last prespec line of the session, and on with the loop after the findings when none was
method: uv run pytest tests/test_onward.py — piped payloads, an event log with a prespec line and files under cases/ in a temp vault
origin: raw/2026-10-06/0104/ledger.md#case-686.1
sprint: migration
created: 2026-10-06
tags: [session, workflow, hooks, harness]
---

## Criterion

When:
The `Stop` hook `uv run guppi onward --plan` of `guppi/onward.py` receives the end of a reply of the main agent that carries a `LEDGER` block, the event log holds a `prespec` line of this session after its `hi`, and every other condition holds under which the hook sends the agent on.

Then:
When a file under `raw/<date>/<hi HHMM>/cases/` was written after the last `prespec` line of the session, the hook exits 2 and tells the agent that the Cases built again on the findings of `/pre-spec` are ratified, to run `uv run guppi prespec --check` on the plan file with `--session <id>`, to fix what it prints, and to call `ExitPlanMode` when it prints no finding.
**＋** When no file under `cases/` was written after that line, the hook exits 2 and tells the agent to go on with the loop after the findings of `/pre-spec`: to send each finding in a Case to its `case-guppi`, or, when no Case goes back, to run the check and exit as above.
**＋** The hook reads the time of the `prespec` line, on the date of the event log that holds it, through the one function of `guppi/prespec.py` that `window` uses to find the line.
**－** A reply that writes a defer or a lesson after `/pre-spec` and before any Case is built again never gets the message that the Cases built again are ratified.
**－** A Case built again and not yet ratified keeps the hook silent, as before.

## Result

2026-10-06, uv run pytest tests/test_onward.py tests/test_prespec.py: 246 passed; no case file after the prespec line, or only older ones, gives TO_LOOP; one written after it and ratified gives TO_EXIT; one not ratified keeps it silent; the last prespec line counts; a session across midnight reads the line on its date; prespec_mark is the one reading window uses

## History

- 2026-10-06 created · [[decision-case-686.1]]
- 2026-10-06 status: pending → passed · raw/2026-10-06/0104/ledger.md#L35
