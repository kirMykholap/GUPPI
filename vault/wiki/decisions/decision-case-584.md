---
type: decision
case: "584"
status: current
update: ["[[rule-case-check]]"]
origin: raw/2026-10-01/1725/ledger.md#case-584
sprint: migration
created: 2026-10-01
tags: [hooks, harness, workflow, session]
---

## Problem

The module docstring of `guppi/casecheck.py` says a refusal of a `Stop` hook adds no `user` record, and the transcripts show one, marked `isMeta`. A later fix of `turn_of_reply` that trusts the docstring could treat the refusal as the start of a turn. The hook would then refuse a Case whose file was already sent, and no test would catch it. The question was how far the fix goes.

## Recommend

- **How far should the fix go?**
  - Recommended: (b) fix the docstring and add a test, with a name that holds `stop`, in which a file is sent, a refusal record follows and the Case is shown again; the Criterion of `estimate-case-check-shows-only-the-checked-case` stands.
  - Answer: agreed, (b).

## History

- 2026-10-01 created · raw/2026-10-01/1725/ledger.md#case-584
