---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec-hook]]"
purpose: The ExitPlanMode hook holds a working session in Plan Mode until /pre-spec has run in it and the check of its plan finds nothing, across midnight too
method: pytest in tests/test_prespec.py with piped payloads against a temp event log; the live reading once by hand, written into the estimate line
checked: 2026-10-01
origin: raw/2026-09-09/ledger.md#case-24.1
sprint: migration
created: 2026-09-09
tags: [session, workflow, hooks, harness]
---

## Criterion

When:
The hook `guppi prespec` receives a `PreToolUse` payload naming `ExitPlanMode` with the session's stamp, and asks whether `/pre-spec` ran in this session.

Then:
With no `prespec` line of this session's stamp after its `hi`, the hook exits 2 with a reason that names `/pre-spec` and the session.
**＋** With the line, it finds the plan file of the session by `plan_path` of `guppi/ledger.py`, runs on it the judgment of `uv run guppi prespec --check`, and exits 2 with the findings on stderr while the judgment finds one.
**＋** With the line and a judgment that finds nothing it exits 0; a line that opens with `note:` does not block.
**＋** With the line and no plan file of the session it exits 0.
**＋** The window is open when the logs hold a `hi` of the session's stamp and a `prespec` of the same stamp after it; a mark of another stamp or `--------` does not count; a foreign `session-start` resets nothing.
**＋** The logs it reads are the ledger hook's, from today back to the date of this session's `session-start`, so the `hi` and the `prespec` of yesterday's session are found after midnight.
**＋** Any other tool exits 0.
**－** Without a `hi` of this session the call passes.
**－** An error of the hook itself prints `prespec: check skipped: <error>` on stderr and exits 0.

## Result

2026-10-01, uv run pytest tests/test_prespec.py: 179 passed; live, session 1237: ExitPlanMode at 14:20:02 after the prespec mark of 14:08:41 of stamp dd5dac5e in the window of its hi of 12:37:19, the check of the plan printing only note lines, was let through and the Spec written to raw/2026-10-01/1237/spec.md; the refusals were read in the tests only

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-24.1
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L76
- 2026-09-14 criterion: case 136.2 added · [[decision-case-136.2]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1229/ledger.md#L26
- 2026-09-17 updated: the Criterion in the form of the model, the block of 136.2 folded in, plus the logs read across midnight; method as a field, the old sections dropped (case 213.2) · [[decision-case-213.2]]
- 2026-09-17 status: pending → passed · raw/2026-09-16/2238/ledger.md#L53
- 2026-09-20 ref `rule-pretask` → `rule-prespec` · [[decision-case-261]]
- 2026-09-20 ref `rule-pretask-hook` → `rule-prespec-hook` · [[decision-case-261]]
- 2026-09-20 renamed from `estimate-pretask-hook-gates` · [[decision-case-261]]
- 2026-09-20 updated: renamed with rule-prespec-hook — the Criterion names guppi prespec, the mark prespec and /pre-spec (case 261) · [[decision-case-261]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/0740/ledger.md#L14
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given and the bounds line out; purpose set (case 493.5) · [[decision-case-493.5]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L74
- 2026-10-01 updated: the Criterion replaced whole and the purpose set anew - with the prespec line the hook runs the check of the plan and refuses while it finds one (case 561.3) · [[decision-case-561.3]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L38
