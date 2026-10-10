---
type: decision
case: "610"
status: archived
children: ["[[decision-case-610.1]]", "[[decision-case-610.2]]"]
origin: raw/2026-10-03/0115/ledger.md#case-610
sprint: migration
created: 2026-10-03
tags: [hooks, harness, workflow, session, ledger]
---

## Problem

A Case can be ratified in the session and then built again in another shape under its old number: whole after sub-cases, with sub-cases after whole, or without a ratified sub-case. The Spec hook then keeps the old parts beside the new ones, and the ledger lines of the first ratification stay. Either the plan signs content twice and is refused, or a dropped sub-case stays signed without anyone noticing. Nothing tells the agent to take a new number before the refusal comes, and nothing stops two Cases from being built under one new number.

## Recommend

- **Which way to close the problem**
  - Recommended: (b) make the new number the rule, with a guard. The check of `case-guppi`'s answer sends back a build that changes the shape of a Case already ratified in the session, the hook stays as it is, the Insight is closed and the put-off change to the hook is retired.
  - Answer: (b).
- **Who picks the new number**
  - Recommended: (a) the check names it: one above the highest Case number in the session's ledger and in the store of checked answers.
  - Answer: agreed with the recommendation, (a).
- **Which changes of shape the check sends back**
  - Recommended: (b) any ratified part missing from a whole answer, and a Case ratified whole that comes back with sub-cases. An answer that holds sub-cases alone is not judged this way.
  - Answer: agreed with the recommendation, (b).
- **Whether the form of a Case states the rule too**
  - Recommended: (a) add one sentence to the splitting part of the form, through `rule-case-protocol`, and keep the check as the guard.
  - Answer: agreed with the recommendation, (a).
- **How done is checked**
  - Recommended: (a) a new Estimate of its own under `rule-case-check`.
  - Answer: agreed with the recommendation, (a).
- **How a clash of the new number is caught**
  - Recommended: (a) the store remembers which agent answered each Case. An answer under a number another agent holds is sent back with a new number and does not replace that entry. This is a sub-case of its own with its own Estimate.
  - Answer: agreed with (a).
- **Where the answer that clashes is kept**
  - Recommended: (c) store it apart, under its number together with its agent's id. Readers by number still find the other agent's entry, and the related Case is not touched.
  - Answer: (c).
- **Change**
  - Asked: at pre-spec, keep the defer of `rule-ledger-line-withdrawn-on-re-ratification`. The context says plainly that a dropped sub-case goes by the new number, while the way without a new Case stays with that rule, and the backlog does not change.
  - Taken: the context says so. No line names that page, and the defer stands.

## History

- 2026-10-03 created · raw/2026-10-03/0115/ledger.md#case-610
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
