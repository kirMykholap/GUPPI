---
type: decision
case: "153"
status: current
update: ["[[rule-harness]]"]
origin: raw/2026-09-14/1633/ledger.md#case-153
sprint: migration
created: 2026-09-14
tags: [harness, workflow]
---

## Context

`rule-harness` Purpose: "Four rules belong to no phase of the session: … lint and the indexes. They run together in `make lint` … the indexes before the pages. Three more belong here and run in no pipeline …"; `estimate-harness-pipeline` `passed`, its Criterion and Method name "then index --check" and `tests/test_index.py`. 145.2 changes `children` only (pre-task).

## Problem

After 147.1 there is no index step and after 145.1 there is a fourth child outside `make lint`; the Purpose and the Method are wrong twice. Decide: the Purpose rewritten, the Method without `tests/test_index.py`.

## Given

`rule-harness` MOC `built`, `estimates: [estimate-harness-pipeline]`; Makefile `test-harness` loses `tests/test_index.py` by 147.1.
**－** A MOC's `update` with `contract: changed` appends the block and sets the Estimate `pending`; `method` rewrites its Method.

## Criterion

- [[estimate-harness-pipeline]] § case 153

## History

- 2026-09-14 created · raw/2026-09-14/1633/ledger.md#case-153
