---
type: decision
case: "555"
status: archived
children: ["[[decision-case-555.1]]", "[[decision-case-555.2]]", "[[decision-case-555.3]]", "[[decision-case-555.4]]", "[[decision-case-555.5]]"]
origin: raw/2026-09-30/2042/ledger.md#case-555
sprint: migration
created: 2026-09-30
tags: [hooks, harness, workflow, session]
---

## Problem

`guppi casecheck`, `guppi context` and `guppi onward` swallow their own errors with exit 0. A Case can then be shown unchecked, the size line can go missing, or the run can stop before `/handoff`, and the agent never sees why. The question is what each hook does on its own error, and how the promise is recorded.

## Recommend

- **How the change is recorded**
  Recommended: (a) one sub-case per hook that changes, each with a new Estimate for its error path; no existing Estimate changes.
  Answer: (a), yes. A later question and a later change each made one exception: the existing promises of `guppi onward` and of `guppi context` are reworded, in Cases 555.4 and 555.5.

## History

- 2026-09-30 created · raw/2026-09-30/2042/ledger.md#case-555
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
