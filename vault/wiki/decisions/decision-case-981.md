---
type: decision
case: "981"
status: current
children: ["[[decision-case-981.1]]", "[[decision-case-981.2]]"]
origin: raw/2026-11-01/0141/ledger.md#case-981
sprint: plugin
created: 2026-11-01
tags: [hooks, harness, workflow, session]
---

## Problem

An answer of `case-guppi` with prose before its `**Built:**` line reaches the main agent unchecked and is shown as a built Case, and the check of that showing failed and has been put off for four sessions.

## Recommend

- **What settles the failed check?**
  - Recommended: (a) the hook sends such an answer back, and the check is read again in this session.
  - Answer: agreed, (a).

## History

- 2026-11-01 created · raw/2026-11-01/0141/ledger.md#case-981
