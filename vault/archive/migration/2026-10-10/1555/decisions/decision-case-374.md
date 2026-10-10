---
type: decision
case: "374"
status: archived
update: ["[[estimate-atomicity-rendered]]"]
origin: raw/2026-09-23/1126/ledger.md#case-374
sprint: migration
created: 2026-09-23
tags: [harness, workflow]
---

## Context

The `method` of `estimate-atomicity-rendered` reads "make lint — render --check exit 0; the text between the markers of case-schema.md read by hand after the librarian's render". Its Then asks only that `render --check` exits 0 after the render and that the hook refuses a hand edit; it does not ask the whole `make lint` to exit 0. The "make lint —" at the head of the `method` reads two ways: the brief rendered it as "`make lint`, `render --check` exit 0", and the agent read it the same way. The one who reads the Estimate may ask for a clean lint and fail it on 100 findings that are not the rule's.
`estimate-atomicity-rendered` stands `pending`, its target `rule-atomicity`; only the `method` field changes, not the Criterion, which by case 296 leaves the Criterion and the status as they stand; no `create`.

## Problem

The wording of the `method` allows the reading "the whole `make lint`, exit 0", and so ties the Estimate of a rule to the lint of the whole sprint, which its Criterion does not ask.

## History

- 2026-09-23 created · raw/2026-09-23/1126/ledger.md#case-374
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
