---
type: decision
case: "656"
status: archived
update: ["[[rule-permissions]]", "[[estimate-permissions]]", "[[rule-settings]]"]
origin: raw/2026-10-05/1343/ledger.md#case-656
sprint: migration
created: 2026-10-05
tags: [harness, session, render]
---

## Problem

A builder that searches the saved transcripts of past sessions stops on a permission prompt for each call. The question was how those reads stop asking, and whether the mode line of the builder stays.

## Recommend

- **How the builder's reads of past transcripts stop asking you**
  - Recommended: (a) allow reading this project's transcript folder by one allow rule in the project settings, and keep `acceptEdits`.
  - Answer: none of the options; the person proposed to remove `acceptEdits`, since the builder ran with no mode line before and nothing asked, and to check that. The later question Whether to remove the builder's mode line, given that the builder now writes its own file took this up.
- **Whether to remove the builder's mode line, given that the builder now writes its own file**
  - Recommended: (b) keep the line and allow reading this project's transcript folder; the check is the person's word in the next session on whether a builder's search of past transcripts asked.
  - Answer: agreed, (b).

## History

- 2026-10-05 created · raw/2026-10-05/1343/ledger.md#case-656
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
