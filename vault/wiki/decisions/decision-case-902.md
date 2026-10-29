---
type: decision
case: "902"
status: current
update: ["[[estimate-spec-write-writes-a-defer]]"]
supersedes: ["[[decision-case-885]]", "[[decision-case-891]]"]
origin: raw/2026-10-29/1930/ledger.md#case-902
sprint: plugin
created: 2026-10-29
tags: [hooks, harness, workflow]
---

## Problem

`estimate-spec-write-writes-a-defer` passed its reading, but it stays on the backlog list. The two Decisions that put it off are archived and were never taken up for it.

## Recommend

- **What this item fixes**
  - Recommended: (a) no code change: take up the open defers, since `generate` already clears a defer from an archived Decision for the pages that the superseding Case names.
  - Answer: agreed, (a).
- **Which of the two checks this Case takes up**
  - Recommended: (a) `estimate-spec-write-writes-a-defer` only, with a History line and both defers superseded; the defer of `estimate-close-commits` is retired by the Case that rewords its `method`.
  - Answer: agreed, (a).

## History

- 2026-10-29 created · raw/2026-10-29/1930/ledger.md#case-902
