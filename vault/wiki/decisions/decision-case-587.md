---
type: decision
case: "587"
status: current
create: ["[[estimate-lint-runs-every-step]]"]
update: ["[[rule-lint]]"]
origin: raw/2026-10-02/1202/ledger.md#case-587
sprint: migration
created: 2026-10-02
tags: [harness, workflow]
---

## Problem

`make lint` stops at its first red step. The backlog step is red in nearly every session that puts an item off, so the Baseline of `/work` and the librarian's runs lose the findings of the later steps, the page findings included. The question was where the fix goes.

## Recommend

- **Where the fix for the hidden findings goes**
  - Recommended: (a) `make lint` runs every step, each prints its own findings, and it exits non-zero when any step is red; only the `Makefile` changes, and the backlog red stays as a signal.
  - Answer: (a), agreed.
- **How the change is checked**
  - Recommended: (a) a new Estimate of its own, `estimate-lint-runs-every-step` on `rule-lint`, read by hand at the next session's Baseline, where the backlog step is expected to be red; `estimate-harness-pipeline` stays as it is.
  - Answer: (a), agreed.

## History

- 2026-10-02 created · raw/2026-10-02/1202/ledger.md#case-587
