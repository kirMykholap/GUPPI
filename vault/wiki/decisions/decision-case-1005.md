---
type: decision
case: "1005"
status: current
children: ["[[decision-case-1005.1]]", "[[decision-case-1005.2]]", "[[decision-case-1005.3]]"]
origin: raw/2026-11-02/1548/ledger.md#case-1005
sprint: plugin
created: 2026-11-02
tags: [hooks, harness, workflow, case-build, session]
---

## Problem

Two steps of `case-guppi` failed though its Render held them word for word. A new reading of the same text gives little reason to pass, so each step needs a change that leaves the agent no choice of how to search.

## Recommend

- **How the failed names search is answered**
  - Recommended: (c) the hook runs the names search and sends the agent the list.
  - Answer: (c).
- **How the failed list-member search is answered**
  - Recommended: (b) one fixed search in the instructions, then a new reading.
  - Answer: (b).
- **What the hook takes as the things a Case changes**
  - Recommended: (b) the pages the Case updates or deletes, and each existing path in a code span of a task line.
  - Answer: (b).
- **What the note shows for each file it lists**
  - Recommended: (a) the path and the purpose line.
  - Answer: (a).

## History

- 2026-11-02 created · raw/2026-11-02/1548/ledger.md#case-1005
