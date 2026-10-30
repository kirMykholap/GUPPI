---
type: decision
case: "945"
status: current
create: ["[[estimate-where-to-stop-writes-each-step-whole]]"]
update: ["[[rule-where-to-stop]]"]
origin: raw/2026-10-30/2345/ledger.md#case-945
sprint: plugin
created: 2026-10-30
tags: [session, workflow, harness, render]
---

## Problem

A stop reply may write a command once and then point to it from a later step. A new window keeps none of the variables, so the person runs a different command than the check needs.

## Recommend

- **Which text carries the guard?**
  - Recommended: (a) `rule-where-to-stop`, a paragraph on the stop reply.
  - Answer: agreed, (a).
- **Which check closes the Case?**
  - Recommended: (a) a new check, read at the next stop with steps by hand.
  - Answer: agreed, (a).

## History

- 2026-10-31 created · raw/2026-10-30/2345/ledger.md#case-945
