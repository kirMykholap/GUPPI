---
type: decision
case: "578"
status: archived
children: ["[[decision-case-578.1]]", "[[decision-case-578.2]]"]
origin: raw/2026-10-01/1441/ledger.md#case-578
sprint: migration
created: 2026-10-01
tags: [session, workflow, ledger]
---

## Problem

The schema wants each open line of a later Frontier on its own line, while the first reply of `/hi` folds the Work list. So a long list of open readings pushes the question about the next item far down each reply, and the Estimates fail the fold the person holds to be correct. The question was whether a later Frontier may fold the open `W` lines, and which replies that covers.

## Recommend

- **Should a later Frontier fold the open Work lines into one line?**
  - Recommended: (b) fold the open `W` lines into one line that lists their ids, as `/hi` does; each open `C` and `A` line stays on its own line with its title, and `frontier.md` keeps the full list.
  - Answer: (b). Folding the `W` lines is the norm, so the Estimate is what is wrong.
- **Which replies does the fold cover?**
  - Recommended: (a) every later Frontier in Plan Mode: the reply that closes a line, the acknowledging reply and the defer reply fold alike, and this Case replaces the Criterion of both Estimates.
  - Answer: (a).

## History

- 2026-10-01 created · raw/2026-10-01/1441/ledger.md#case-578
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
