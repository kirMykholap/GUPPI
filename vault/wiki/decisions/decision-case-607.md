---
type: decision
case: "607"
status: current
children: ["[[decision-case-607.1]]", "[[decision-case-607.2]]"]
origin: raw/2026-10-03/0115/ledger.md#case-607
sprint: migration
created: 2026-10-03
tags: [hooks, harness, workflow]
---

## Problem

When `case-guppi` answers with a round or a `**Fact:**` answer after a Case it built, the `SubagentStop` check of a Case goes back to that earlier Case and checks it again, against the titles of the new round too. It sends back a sound round for a fault of the earlier Case, and it stores that Case again and writes its file again.

## Recommend

- **Which output should the hook take as the answer?**
  - Recommended: (a) the newest output that is a Case, a round or a Fact answer. A summary after a hand-back is still passed over, and only a Case gets the check of a Case.
  - Answer: agreed with the recommendation, (a).
- **What should become of the round check's promise that both checks run in one exit?**
  - Recommended: (a) replace the Criterion of `estimate-case-check-sends-back-a-faulty-round` too, in a second sub-case. Its line says instead that a round gets no check of a Case in the same run.
  - Answer: agreed with the recommendation, (a).
- **How should done be checked for the main change?**
  - Recommended: (a) replace the Criterion of `estimate-case-check-sends-back-a-faulty-case` whole, and add to its method a check by hand that the first live round after a built Case is not sent back for that Case.
  - Answer: agreed with the recommendation, (a).

## History

- 2026-10-03 created · raw/2026-10-03/0115/ledger.md#case-607
