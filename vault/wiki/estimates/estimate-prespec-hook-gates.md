---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec-hook]]"
purpose: The ExitPlanMode hook holds a working session in Plan Mode until /pre-spec has run in it and the check of its plan finds nothing, across midnight too
method: pytest in .guppi/tests/test_prespec.py with piped payloads against a temp event log; the live reading once by hand, written into the estimate line
checked: 2026-10-01
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, hooks, harness]
core: true
---

## Criterion

When:
The hook `guppi prespec` receives a `PreToolUse` payload naming `ExitPlanMode` with the session's stamp, and asks whether `/pre-spec` ran in this session.

Then:
With no `prespec` line of this session's stamp after its `hi`, the hook exits 2 with a reason that names `/pre-spec` and the session.
**＋** With the line, it finds the plan file of the session by `plan_path` of `.guppi/guppi/ledger.py`, runs on it the judgment of `uv run --project .guppi guppi prespec --check`, and exits 2 with the findings on stderr while the judgment finds one.
**＋** With the line and a judgment that finds nothing it exits 0; a line that opens with `note:` does not block.
**＋** With the line and no plan file of the session it exits 0.
**＋** The window is open when the logs hold a `hi` of the session's stamp and a `prespec` of the same stamp after it; a mark of another stamp or `--------` does not count; a foreign `session-start` resets nothing.
**＋** The logs it reads are the ledger hook's, from today back to the date of this session's `session-start`, so the `hi` and the `prespec` of yesterday's session are found after midnight.
**＋** Any other tool exits 0.
**－** Without a `hi` of this session the call passes.
**－** An error of the hook itself prints `prespec: check skipped: <error>` on stderr and exits 0.

## Result

2026-10-01, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
