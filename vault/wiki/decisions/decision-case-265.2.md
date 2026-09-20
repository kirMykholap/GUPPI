---
type: decision
case: "265.2"
status: current
update: ["[[estimate-retro-commit-gates]]"]
origin: raw/2026-09-20/0958/ledger.md#case-265.2
sprint: migration
created: 2026-09-20
tags: [session, workflow, hooks, harness, git]
---

## Context

Case 261 renamed `rule-pretask` to `rule-prespec` and moved the word in the code, the tests and the prose of the live pages; the Criteria and `method` of seven Estimates it left to their next `update`. On three the word stands in text of the shape of 193: `estimate-hi-writes-frontier` (`passed`, under `rule-skill-hi`) — its `method` names `guppi pretask --check` and `tests/test_pretask.py`, its Given "`/pre-task` fails on an open line"; `estimate-generate-writes` and `estimate-generate-walks-dates` (`passed`, under `rule-page-generation`) — "`pretask` does not change" and the slug `-pretask-reconciles`. On four the Criterion is in the shape before 193, with `### case N` blocks: `estimate-event-log-records` (`rule-event-log`; the base text plus 111.1, 125, 136.1), `estimate-retro-commit-gates` (`rule-retro-commit`; the base plus 169.1, 180), `estimate-plan-mode-verified` (`rule-plan-mode`, the cross-cutting Estimate of the MOC; one paragraph), `estimate-documentation-completes` (`rule-documentation`; the base plus 73.8, 89.1, 90.3, 100.2, 147.5); on the first three `method` is a section, not a field. Touching one of them is a recut by 211: one Criterion of Given/When/Then in place of the blocks, `method` as a field, `pending` and a reading — one sub-case per page. No other Estimate of these rules is touched.

## Problem

Three pages point at a file, a command and a slug that no longer exist; four cannot be repaired by the word, only by a recut, and the person takes all seven now. The recut folds the blocks into one promise: the lines on a Render, a `contract` or "gets a block" are the bookkeeping of those Cases and do not enter the Criterion.

## History

- 2026-09-20 created · raw/2026-09-20/0958/ledger.md#case-265.2
