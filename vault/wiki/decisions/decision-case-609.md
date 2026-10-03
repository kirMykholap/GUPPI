---
type: decision
case: "609"
status: current
update: ["[[estimate-orchestration-defers-in-one-reply]]"]
origin: raw/2026-10-03/0115/ledger.md#case-609
sprint: migration
created: 2026-10-03
tags: [session, workflow, ledger]
---

## Problem

The Criterion of `estimate-orchestration-defers-in-one-reply` is triggered by any defer in Plan Mode, but its result fits only a decision put off as a short-form Case. The defer of a sprint item fits the trigger and can never meet the result. So the reading is either skipped, as in session 2300, or taken and wrongly marked `failed`.

## Recommend

- **Which defer should `estimate-orchestration-defers-in-one-reply` read?**
  - Recommended: (a) narrow the trigger to a deferred decision, replacing the Criterion whole, with a `－` line saying that a sprint or backlog item put off is not this moment, and the method naming the same defer. A sprint defer stays checked by the three Estimates that already check it.
  - Answer: agreed with the recommendation, (a).

## History

- 2026-10-03 created · raw/2026-10-03/0115/ledger.md#case-609
