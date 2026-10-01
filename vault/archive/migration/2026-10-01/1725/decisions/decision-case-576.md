---
type: decision
case: "576"
status: archived
defer: ["[[estimate-estimates-schema-checked]]"]
superseded_by: ["[[decision-case-583]]"]
origin: raw/2026-10-01/1237/ledger.md#case-576
sprint: migration
created: 2026-10-01
tags: [harness, render, schema]
---

## Context

At the Work readings of session 2356, `uv run pytest tests/test_schemas.py -k estimate` gave 5 passed and 1 skipped, "no conditional on a field". The Criterion of `estimate-estimates-schema-checked` names a section required on `passed` and `failed`. Whether the skip leaves that untested was not settled. The person put the remaining items off to go to work.

## Problem

The question whether the skipped test leaves the required section untested is put off.

## Deferred

### [[estimate-estimates-schema-checked]]

Whether the skip no conditional on a field of tests/test_schemas.py -k estimate leaves untested the section the Criterion requires on passed and failed

## History

- 2026-10-01 created · raw/2026-10-01/1237/ledger.md#case-576
- 2026-10-01 superseded by decision-case-583 · [[decision-case-583]]
- 2026-10-01 archived · superseded
- 2026-10-01 archived · cleanup
