---
type: decision
case: "662"
status: current
children: ["[[decision-case-662.1]]", "[[decision-case-662.2]]", "[[decision-case-662.3]]"]
origin: raw/2026-10-05/1616/ledger.md#case-662
sprint: migration
created: 2026-10-05
tags: [hooks, harness, workflow, session]
---

## Problem

The summary of `case-guppi` gives no name for a top-level Case with sub-cases, and the main agent may not read the file, so it shows the Case under a heading of its own words. The person ratifies a Case under a name its file does not hold. The question was where the heading takes its name, whether a script checks it, and what happens to the open Insight.

## Recommend

- **Where the main agent gets the name of the heading**
  - Recommended: (a) a labelled `**Case:**` line in the summary, right after `**Built:**`, with the id and name as the file's heading holds them, not a Markdown heading.
  - Answer: agreed, (a).
- **Whether a script checks that the summary names the top-level Case**
  - Recommended: (a) the check that runs when `case-guppi` stops sends back a summary whose line is missing or differs from the file's heading.
  - Answer: agreed, (a).
- **What happens to the open Insight**
  - Recommended: (a) leave it open; the `context` names it and says this Case fixes the heading part only.
  - Answer: agreed, (a).

## History

- 2026-10-05 created · raw/2026-10-05/1616/ledger.md#case-662
