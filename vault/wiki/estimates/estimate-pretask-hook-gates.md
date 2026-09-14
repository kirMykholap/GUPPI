---
type: estimate
kind: QA
status: passed
target: "[[rule-pretask-hook]]"
origin: raw/2026-09-09/ledger.md#case-24.1
sprint: migration
created: 2026-09-09
tags: [session, workflow, hooks, harness]
---

## Context

The gate is worth having only if it holds exactly once: blocks the approval that skipped
the check, and lets the next one through. The unit cases pin that on piped payloads; the
live reading proves the registration and that `exit 2` on `PreToolUse` reaches the agent
as a reason rather than as silence.

## Criterion

Given a `PreToolUse` payload naming `ExitPlanMode`: with no `pretask` line after this
session's `hi` in the event log, exit 2 with a reason naming `/pre-task` and the session;
with the line, exit 0; any other tool, exit 0. Live: the approval of the next plan passes
only after `/pre-task` ran.

### case 136.2

When:
The hook `guppi pretask` on `ExitPlanMode` asks whether `/pre-task` ran in this session.

Then:
The window is open when the log holds a `hi` of the session's stamp and a `pretask` of the same stamp after it; a mark of another stamp or `--------` does not count; a foreign `session-start` resets nothing.
**＋** `rule-pretask-hook` `contract: changed`; `estimate-pretask-hook-gates` gets a `### case 136.2` block, `pending`: the test — a `pretask` of a foreign stamp between our `hi` and `ExitPlanMode` → refused; ours → passes.
**－** The `--check` pass (grammar, `then` items, frontier) of `rule-pretask` does not change.

## Method

pytest in `tests/test_pretask.py` with piped payloads against a temp event log; the live
reading once by hand, written into the estimate line.

## Result

block 136.2 against tests/test_pretask.py: a pretask of our stamp after our hi → exit 0; a pretask of a foreign stamp → 2; an unstamped `--------` pretask → 2; a foreign session-start between our hi and our pretask → 0, nothing reset; built after the live reading of 136.1, as the Spec orders

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-24.1
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L76
- 2026-09-14 criterion: case 136.2 added · [[decision-case-136.2]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1229/ledger.md#L26
