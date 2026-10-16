---
type: decision
case: "870"
status: current
update: ["[[rule-case-build]]", "[[estimate-case-build-writes-the-case]]", "[[insight-case-build-opens-a-new-case-where-one-was-named]]"]
origin: raw/2026-10-16/2104/ledger.md#case-870
sprint: plugin
created: 2026-10-16
tags: [session, workflow, harness, case-build, prespec]
---

## Problem

Asked to change a named Case, `case-guppi` may put the change into a new top-level Case under a number it picks. The named Case then stays as it was, and the Cases that name it are built again. The person never chose where the change goes.

## Recommend

- **What should be done with this insight?**
  - Recommended: (a) ask before opening a new Case: a change goes under the number of the Case a message names; where a fix would add a second behaviour to a ratified Case with no sub-cases, `case-guppi` writes no new file and asks in a round whether it goes into that Case or into a new Case beside it; during planning a named Case keeps its number unless the schema sets a new one.
  - Answer: agreed, (a).
- **Which check page proves the change?**
  - Recommended: (a) replace the Criterion of `estimate-case-build-writes-the-case` whole, its old line on a new Case beside a ratified one made three.
  - Answer: agreed, (a).

## History

- 2026-10-17 created · raw/2026-10-16/2104/ledger.md#case-870
