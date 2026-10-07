---
type: decision
case: "723"
status: current
children: ["[[decision-case-723.1]]", "[[decision-case-723.2]]", "[[decision-case-723.3]]"]
origin: raw/2026-10-07/2114/ledger.md#case-723
sprint: migration
created: 2026-10-07
tags: [session, workflow, harness, ledger]
---

## Problem

The take-back of a ratified Case, as Case 713 set it, gives two closers for one reply and holds a sentence that contradicts itself. It leaves nothing in the backlog when the Case taken back changed only existing Estimates. The check of the put-off reply and the rule of `/hi` with its check still say that a sprint or backlog item never takes a short Case.

## Recommend

- **Does this Case retire last session's take-back decision?**
  - Recommended: (a) retire it: this Case carries the retiring mark and restates the whole take-back rule.
  - Answer: agreed, (a).
- **What reaches the backlog when the Case taken back changed only existing checks?**
  - Recommended: (a) also put off the page each changed check checks, once per page.
  - Answer: agreed, (a).
- **The fault in the Case schema that the C3 Case put off again**
  - Recommended: (b) fix it here; the C3 Case drops its put-off.
  - Answer: first agreed, (b); then (a), leave it out: Case 722 stays as first ratified, its put-off of `rule-case-protocol` for this sentence included, and this Case changes only `rule-orchestration`, its Estimates, and the rule of `/hi` with its Estimate.
- **The same wrong sentence in the rule of `/hi` and its check**
  - Recommended: (a) fix it here.
  - Answer: agreed, (a).
- **When the `/hi` check is read after its wording changes**
  - Recommended: (b) keep the reading after the sprint close.
  - Answer: (b); the check of the Case file then refused the kept `method`, and the question "How the `/hi` check is read, now that keeping its old reading is refused" replaced this one.
- **How the `/hi` check is read, now that keeping its old reading is refused**
  - Recommended: (b) the person's answer at the `/hi` after the sprint close, with the unit tests.
  - Answer: agreed, (b).

## History

- 2026-10-07 created · raw/2026-10-07/2114/ledger.md#case-723
