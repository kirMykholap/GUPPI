---
type: decision
case: "732"
status: current
update: ["[[rule-skill-hi]]", "[[estimate-hi-takes-its-readings]]"]
origin: raw/2026-10-08/0213/ledger.md#case-732
sprint: migration
created: 2026-10-08
tags: [session, harness, workflow]
---

## Problem

`/hi` asks the person for a reading that the person cannot give before a sprint closes, and it asks again at every session until then.

## Recommend

- **Where an Ask line that waits for a later moment is held back**
  - Recommended: (a) at `/hi`: the line stays under `## Ask`, open, and is not put to the person until its moment, as the rule for a waiting `W` line does.
  - Answer: agreed, (a).
- **What the agent reads to judge whether the moment has come**
  - Recommended: (a) the question on the Ask line as the brief gives it, with no page opened; a question that names no moment is asked as today.
  - Answer: agreed, (a).
- **Which moments make an Ask line wait, and how the agent knows a moment has come**
  - Recommended: (a) the same two moments as the `W` rule: the line is asked at the `/hi` whose brief opens its `Cases` with `open the next sprint`, or in the session the person names as the one that closes the sprint.
  - Answer: agreed, (a).
- **Which check proves the change**
  - Recommended: (a) replace the Criterion of `estimate-hi-takes-its-readings` whole, with an exception line for a waiting `A` line, and set its purpose anew.
  - Answer: agreed, (a).

## History

- 2026-10-08 created · raw/2026-10-08/0213/ledger.md#case-732
