---
type: decision
case: "613"
status: archived
children: ["[[decision-case-613.1]]", "[[decision-case-613.2]]", "[[decision-case-613.3]]"]
origin: raw/2026-10-03/0317/ledger.md#case-613
sprint: migration
created: 2026-10-03
tags: [harness, workflow, render, schema, session, ledger, hooks, git]
---

## Problem

A check by hand is tied to one moment that passes unread, and no step reads it afterwards, so its Estimate waits for good. The question was how a method names its moment, which step reads a moment that came after its session's readings, how the old wording is caught, and what happens to the Estimates that wait today.

## Recommend

- **How should a check by hand name its moment?**
  - Recommended: (a) any such moment counts; the method names the kind of moment, and "the first" stays only for an event that has never happened.
  - Answer: agreed with the recommendation, (a).
- **Which step reads a moment that comes after its session's readings are written?**
  - Recommended: (a) the next `/hi` reads it from the previous session's transcript.
  - Answer: agreed with the recommendation, (a).
- **What happens to the Estimates that wait today?**
  - Recommended: (a) this Case rewrites their methods; they are read from the next session on.
  - Answer: agreed with the recommendation, (a).
- **What happens to an Estimate whose event is rare or has not happened yet?**
  - Recommended: (a) it waits for the event, and the close of the sprint settles the rest.
  - Answer: agreed with the recommendation, (a).
- **What happens to an Estimate that pairs tests with a check by hand?**
  - Recommended: (a) keep both parts in one reading.
  - Answer: agreed with the recommendation, (a).
- **What happens when a method names more than one moment?**
  - Recommended: (a) `/hi` reads each part from the session where its moment came.
  - Answer: agreed with the recommendation, (a).
- **How is the new form of a method checked?**
  - Recommended: (a) one pattern in `guppi/lint.py`, used by `pre-spec` and `make lint`, finds a method that ties its check by hand to "the first ... after the render"; a new Estimate read by tests.
  - Answer: agreed with the recommendation, (a).
- **What happens to the Estimates that already passed but whose method uses the old wording?**
  - Recommended: (a) this Case rewrites their methods too; promise and status stand.
  - Answer: agreed, (a).
- **Does the pattern also catch "after the change"?**
  - Recommended: (a) yes, both "after the render" and "after the change".
  - Answer: agreed, (a).

## History

- 2026-10-03 created · raw/2026-10-03/0317/ledger.md#case-613
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
