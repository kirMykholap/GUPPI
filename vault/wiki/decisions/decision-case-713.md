---
type: decision
case: "713"
status: current
create: ["[[estimate-orchestration-takes-back-a-ratified-case]]"]
update: ["[[rule-orchestration]]"]
origin: raw/2026-10-07/1804/ledger.md#case-713
sprint: migration
created: 2026-10-07
tags: [session, workflow, ledger, harness]
---

## Problem

The person cannot take back a ratified Case in its session. The Case stays in the plan, and Work Mode would build it.

## Recommend

- **What does taking back an approved Case leave behind?**
  - Recommended: (a) a short "put off" Case replaces it; its line carries the mark that replaces the old Case, and its pages go to the backlog.
  - Answer: agreed, (a).
- **When can an approved Case be taken back?**
  - Recommended: (a) in Plan Mode only; in Work Mode the agent tells the person that the Case is already being built.
  - Answer: agreed, (a).
- **Can a take-back name a single sub-case?**
  - Recommended: (a) the whole Case or one sub-case.
  - Answer: agreed, (a).
- **How does the item's Frontier line close after a whole take-back?**
  - Recommended: (a) close it the way its source is put off: put off by the short Case, a sprint item put off, or a backlog item kept.
  - Answer: agreed, (a).
- **Which pages does the short Case put off?**
  - Recommended: (a) every page of the approved Case, Estimates included.
  - Answer: agreed, (a); the Estimates were then settled by the question on the Estimates of the approved Case.
- **Which check proves that the take-back works?**
  - Recommended: (a) a new Estimate for the take-back; the put-off check stays as it is.
  - Answer: agreed, (a).
- **What happens to the Estimates of the approved Case when it is taken back?**
  - Recommended: (a) put off each rule, entity and insight page and each Estimate the Case updates, and for each Estimate it creates the page that Estimate would check; the short Case names the Estimates left out.
  - Answer: agreed, (a).

## History

- 2026-10-07 created · raw/2026-10-07/1804/ledger.md#case-713
