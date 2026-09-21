---
type: decision
case: "296"
status: current
update: ["[[rule-materialize]]", "[[estimate-materialize-assembles]]"]
supersedes: ["[[decision-case-291.1]]"]
origin: raw/2026-09-21/1315/ledger.md#case-296
sprint: migration
created: 2026-09-21
tags: [harness, workflow, ledger]
---

## Context

As in 291: `lift_criterion` puts the `given`, `when` and `then` of the Case on every `update` entry of an Estimate and sets `pending` — 290.3 replaced two signed Criteria with one `set: {purpose}`. 291.1 tied the status to whether a part was named; that is a hole — a `replace` pair inside the Criterion changes the promise while the status stands, and a pair cannot set the status honestly, since `status` named means the whole replacement. The pages as in 291: `rule-materialize` `draft`, of its ten Estimates the Case touches `estimate-materialize-assembles` (`passed`, line 30 the promise); an `update` with a `ref`. The `replace` in the Purpose of `rule-materialize` has the `old` of 291.1, which was never applied.

## Problem

Two questions were glued into one sign. *What* changes is decided by the part named. *Whether the status is reset* must be decided by whether the Criterion was touched; today neither the script nor 291.1 tells them apart.

## History

- 2026-09-21 created · raw/2026-09-21/1315/ledger.md#case-296
