---
type: decision
case: "1015"
status: current
children: ["[[decision-case-1015.1]]", "[[decision-case-1015.2]]"]
origin: raw/2026-11-03/0316/ledger.md#case-1015
sprint: plugin
created: 2026-11-03
tags: [session, workflow, harness]
---

## Problem

The frame of `ask-guppi` allows one search of the code at `/pre-spec`, but the questions of `/pre-spec` need the code to check the facts of a Case. The agent breaks the limit in each run and reports it as a broken rule, so the limit holds nothing back.

## Recommend

- **Searches of code at pre-spec**
  - Recommended: (a) searches of code as each finding needs; the folder-walk Grep stays required for a Case that adds a new file.
  - Answer: agreed, (a).
- **The archive search in the same report**
  - Recommended: (a) left out of this Case.
  - Answer: agreed, (a).
- **How the change is checked**
  - Recommended: (a) replace the Criterion of `estimate-ask-searches-at-prespec`.
  - Answer: agreed, (a).
- **The check of the folder-walk Grep says no code search otherwise**
  - Recommended: (a) a sub-case replaces its Criterion.
  - Answer: agreed, (a).

## History

- 2026-11-03 created · raw/2026-11-03/0316/ledger.md#case-1015
