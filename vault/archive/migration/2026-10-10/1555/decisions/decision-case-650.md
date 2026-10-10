---
type: decision
case: "650"
status: archived
children: ["[[decision-case-650.1]]", "[[decision-case-650.2]]"]
origin: raw/2026-10-05/1343/ledger.md#case-650
sprint: migration
created: 2026-10-05
tags: [hooks, harness, workflow, session]
---

## Problem

A second `case-guppi` that builds under a number another agent holds replaces that agent's file before any check runs. The first Case can no longer be shown until its agent writes it again, and nothing tells that agent to do so. The question was whether a guard stops the second write and how it knows that a number is taken, what the refused agent does, and how done is checked.

## Recommend

- **Whether a guard stops the second write, and how it knows the number is taken**
  - Recommended: (a) the guard claims the number at the first write: the first builder whose write creates the file is recorded in the store as the holder of the number at once, and a write or edit of that file by any other builder is refused before it runs, with a free number counted as the check counts one; this covers the time between the first builder's write and its stop.
  - Answer: agreed, (a).
- **What the refused builder does next**
  - Recommended: (a) it builds under the free number the refusal names, counted as the check counts one, and the main agent learns the number from the summary.
  - Answer: agreed, (a).
- **How the new refusal is checked**
  - Recommended: (a) a new check for the claim under the guard's rule, and the old check of the guard replaced whole, its line on builders now naming a number held by another builder as the exception; two sub-cases.
  - Answer: agreed, (a).

## History

- 2026-10-05 created · raw/2026-10-05/1343/ledger.md#case-650
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
