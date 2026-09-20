---
type: decision
case: "212"
status: current
update: ["[[estimate-lint-catches]]"]
origin: raw/2026-09-16/2238/ledger.md#case-212
sprint: migration
created: 2026-09-16
tags: [harness, workflow]
---

## Context

`rule-plan-mode` is a MOC with four children and two Estimates: `estimate-plan-mode-verified` (`method: make test-plan-mode`, the pipeline over the children) and `estimate-plan-mode-names-its-estimates` (case 187, `method` a live reading of the Spec at the close: every Case names its Estimate by slug). The clause of 112.1 in `rule-lint` (`estimate-lint-catches`): a MOC's Estimate with a `make <target>` passes always, and "by hand" passes only when every child's Estimate is a reading too. The children of Plan Mode — `rule-prespec` among them — have tests, so lint prints `method: says by hand while estimate-prespec-checks-the-plan names a test file`. The Case touches one promise of `rule-lint` — `estimate-lint-catches`; the other Estimates of lint it does not touch. `estimate-lint-catches` gets its `method` field from 211.3 in the same yaml, earlier in ledger order.

## Problem

The clause of 112.1 was written when a MOC had one Estimate covering its children: "by hand" on such a MOC would hide the children's tests. Now a MOC can carry a second, cross-cutting Estimate — a reading of the behaviour of Plan Mode itself, not a pipeline; no test checks it, and naming `make test-plan-mode` in its `method` would be false. Lint names a contradiction that is none.

## History

- 2026-09-17 created · raw/2026-09-16/2238/ledger.md#case-212
