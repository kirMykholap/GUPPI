---
type: decision
case: "554"
status: current
create: ["[[estimate-spec-write-exits-2-on-an-error]]"]
update: ["[[rule-spec-write]]"]
origin: raw/2026-09-30/2042/ledger.md#case-554
sprint: migration
created: 2026-09-30
tags: [hooks, harness, workflow, session]
---

## Problem

The `Stop` run of `guppi ratified` swallows its own errors with exit 0. A Case due to be written is then lost, and no sign reaches the agent. This is how the first showing of Case 551 was lost. The question is what the hook does on its own error, whether the guard changes with it, whether the other `Stop` hooks join, and how the promise is recorded.

## Recommend

- **What the Stop run does when it raises**
  Recommended: (a) exit 2, as the ledger hook does. An error after the payload is read exits 2, the message names the error and says to repeat the ledger lines. An error while reading the payload still exits 0. The re-fire still does nothing.
  Answer: (a) exit 2, as the ledger hook does.
- **The edit guard of the same command**
  Recommended: (a) only the Stop run changes. The guard keeps exit 0 on its own error.
  Answer: (a) only the Stop run changes.
- **The other end-of-reply hooks**
  Recommended: (a) this Case covers `guppi ratified` alone. The other three hooks are decided under their own Frontier item.
  Answer: (a). Those hooks have their own item in the Frontier and are taken separately.
- **How the promise is recorded**
  Recommended: (a) a new Estimate for the error path. The failed Estimate keeps its wording and is read again in a later session.
  Answer: (a) a new Estimate for the error path; the failed one is read again later.

## History

- 2026-09-30 created · raw/2026-09-30/2042/ledger.md#case-554
