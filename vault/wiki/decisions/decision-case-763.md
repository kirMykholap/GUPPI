---
type: decision
case: "763"
status: current
children: ["[[decision-case-763.1]]", "[[decision-case-763.2]]"]
origin: raw/2026-10-10/1713/ledger.md#case-763
sprint: plugin
created: 2026-10-10
tags: [sprint, workflow, harness]
---

## Problem

The Criterion of `estimate-sprint-close-settles-unread-estimates` promises that a `failed` reading of an Estimate outside the sprint page settles that Estimate with no name. `guppi/sprint_close.py` and its tests require a name by `--carry` or `--archive-unread` for it. A signed check that the code does not keep stands `passed`, and the check of the closing session and its skill would leave such an Estimate unnamed.

## Recommend

- **Which side follows the other**
  - Recommended: (a) the check follows the code. The Criterion is replaced so that a `failed` Estimate outside the sprint page must still be named by `--carry` or `--archive-unread`, its `purpose` is reworded, and no code changes.
  - Answer: agreed, (a).
- **How the check of the grouped readings is read in this session**
  - Recommended: (a) read the last close now. The line is fixed so that the close line names an Estimate still unread after Work Mode, or one read `failed` in Work Mode that the sprint page does not list, and the method becomes a reading by hand, in this session, of the closing plan and ledger of the last session that closed a sprint.
  - Answer: agreed, (a).

## History

- 2026-10-10 created · raw/2026-10-10/1713/ledger.md#case-763
