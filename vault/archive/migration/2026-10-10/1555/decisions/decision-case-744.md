---
type: decision
case: "744"
status: archived
children: ["[[decision-case-744.1]]", "[[decision-case-744.2]]"]
origin: raw/2026-10-08/2352/ledger.md#case-744
sprint: migration
created: 2026-10-08
tags: [harness, workflow, hooks]
---

## Problem

The template of `grill-me` puts a list dash before the `**After:**` label of each option, and the person wants it gone. The check of a round requires the dash, and the skill text describes the line as a nested item, so removing the dash from the template alone would get every round sent back and leave the skill in contradiction with itself.

## Recommend

- **What the round check accepts as the After line**
  - Recommended: (a) accept the line with or without the dash; the tests of the check and its promise change to match.
  - Answer: agreed, (a).
- **Where the After line stands without the dash**
  - Recommended: (a) directly under the option name, indented two spaces, only the dash removed.
  - Answer: agreed, (a).
- **The skill sentences that call the After line a nested item**
  - Recommended: (a) reword them for an `**After:**` line; a quotation or a list under it is indented as far as the label, and the sample quotation line moves to match.
  - Answer: agreed, (a).

## History

- 2026-10-09 created · raw/2026-10-08/2352/ledger.md#case-744
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
