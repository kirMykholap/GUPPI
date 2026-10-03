---
type: decision
case: "619"
status: current
children: ["[[decision-case-619.1]]", "[[decision-case-619.2]]"]
origin: raw/2026-10-04/0004/ledger.md#case-619
sprint: migration
created: 2026-10-04
tags: [workflow, librarian]
---

## Problem

The test page has served its purpose except for one moment: a live reword. It keeps `make lint` red and must be gone before any close of the sprint. The question is how to bring on the reword and remove the page in one session, with each step checked on its own.

## Recommend

- **One decision or two?**
  - Recommended: (b) two sub-cases under one Case, the reword first and the delete second, since the reword can fail on its own and its fix differs from the fix of a delete.
  - Answer: Agreed with the recommendation.
- **Does the delete wait for the word change to be read?**
  - Recommended: (a) both in this session. The reading loses nothing with the delete, and the lint findings clear soonest.
  - Answer: Agreed with the recommendation.

## History

- 2026-10-04 created · raw/2026-10-04/0004/ledger.md#case-619
