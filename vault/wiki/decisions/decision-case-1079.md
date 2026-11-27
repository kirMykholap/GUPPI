---
type: decision
case: "1079"
status: current
children: ["[[decision-case-1079.1]]", "[[decision-case-1079.2]]"]
origin: raw/2026-11-27/0947/ledger.md#case-1079
sprint: plugin
created: 2026-11-27
tags: [sprint, harness, hooks]
---

## Problem

Code Mode may save tokens and time, but no figure shows it for our work. The harness rests on hooks, and the documentation does not say whether all of them answer a call made from code. A trial in this repository could change pages or harness files with no ratified Case wherever a hook does not fire.

## Recommend

- **Where the trial runs**
  - Recommended: (a) a clone outside the repository.
  - Answer: agreed, (a).
- **When the trial runs**
  - Recommended: (a) in Work Mode of this session, by a `stop:` task while the person runs the sessions.
  - Answer: agreed, (a).
- **Which task is measured with and without Code Mode**
  - Recommended: (a) a read-only task with many tool calls, the hook check run apart in a Code Mode session.
  - Answer: agreed, (a).

## History

- 2026-11-27 created · raw/2026-11-27/0947/ledger.md#case-1079
