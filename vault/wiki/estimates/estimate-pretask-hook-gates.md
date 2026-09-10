---
type: estimate
kind: QA
status: passed
target: rule-pretask-hook
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

## Method

pytest in `tests/test_pretask.py` with piped payloads against a temp event log; the live
reading once by hand, written into the estimate line.

## Result

tests/test_pretask.py green; live: ExitPlanMode at 10:25:13 passed after the pretask line of 09:57:45; the refusal path was not exercised live, the approval came after /pre-task by construction

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-24.1
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L76
