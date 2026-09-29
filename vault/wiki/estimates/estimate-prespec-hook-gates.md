---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec-hook]]"
purpose: The ExitPlanMode hook holds a working session in Plan Mode until /pre-spec has run in it, across midnight too
method: pytest in tests/test_prespec.py with piped payloads against a temp event log; the live reading once by hand, written into the estimate line
checked: 2026-09-29
origin: raw/2026-09-09/ledger.md#case-24.1
sprint: migration
created: 2026-09-09
tags: [session, workflow, hooks, harness]
---

## Criterion

When:
The hook `guppi prespec` receives a `PreToolUse` payload naming `ExitPlanMode` with the session's stamp, and asks whether `/pre-spec` ran in this session.

Then:
With no `prespec` line of this session's stamp after its `hi`, the hook exits 2 with a reason that names `/pre-spec` and the session; with the line, it exits 0; any other tool exits 0.
**＋** The window is open when the logs hold a `hi` of the session's stamp and a `prespec` of the same stamp after it; a mark of another stamp or `--------` does not count; a foreign `session-start` resets nothing.
**＋** The logs it reads are the ledger hook's, from today back to the date of this session's `session-start`, so the `hi` and the `prespec` of yesterday's session are found after midnight.
**－** Without a `hi` of this session the call passes.

## Result

2026-09-29, uv run pytest tests/test_prespec.py -k "hook or gate": 2 passed; live, session 1134: event_log.md holds 13:24:34 d3c46a47 prespec after the hi, and ExitPlanMode at 13:49:20 passed

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
