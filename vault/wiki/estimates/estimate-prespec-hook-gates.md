---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec-hook]]"
method: pytest in tests/test_prespec.py with piped payloads against a temp event log; the live reading once by hand, written into the estimate line
checked: 2026-09-20
origin: raw/2026-09-09/ledger.md#case-24.1
sprint: migration
created: 2026-09-09
tags: [session, workflow, hooks, harness]
---

## Criterion

Given:
A `PreToolUse` payload naming `ExitPlanMode`, with the session's stamp.
**＋** The ledger hook reads the event logs from today back to the date of this session's `session-start` (`ledger.session_event_logs`, case 55.1).
**＋** The tests in `tests/test_prespec.py` fix the hook with piped payloads against a temp event log; the live reading is the approval of the next plan after the render of case 261.
**－** The `--check` pass of `rule-prespec` does not change here.

When:
The hook `guppi prespec` on `ExitPlanMode` asks whether `/pre-spec` ran in this session.

Then:
With no `prespec` line of this session's stamp after its `hi`, exit 2 with a reason naming `/pre-spec` and the session; with the line, exit 0; any other tool, exit 0.
**＋** The window is open when the logs hold a `hi` of the session's stamp and a `prespec` of the same stamp after it; a mark of another stamp or `--------` does not count; a foreign `session-start` resets nothing (case 136.2).
**＋** The logs it reads are the ledger hook's — from today back to the date of this session's `session-start` — so the `hi` and the `prespec` of yesterday's session are found after midnight (case 213.2).
**－** Without a `hi` of this session the call passes, as before.

## Result

2026-09-20, `pytest tests/test_prespec.py` after the move: the ExitPlanMode hook looks for the mark `prespec` of the session's stamp after its `hi`, yesterday's mark releases after midnight, the refusal names /pre-spec; `guppi gate` writes `prespec` on a call of `pre-spec` (tests/test_gate.py, 119 green with test_ledger); the live part is the approval of the next plan after the render

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
