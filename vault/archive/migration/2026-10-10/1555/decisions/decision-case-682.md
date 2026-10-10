---
type: decision
case: "682"
status: archived
children: ["[[decision-case-682.1]]", "[[decision-case-682.2]]"]
origin: raw/2026-10-05/2249/ledger.md#case-682
sprint: migration
created: 2026-10-05
tags: [session, hooks, harness, ledger]
---

## Problem

A lesson line whose cause a Case of the same session closed can be written with no mark, and nothing catches it, so the librarian never links the lesson to its Case.

## Recommend

- **Where the missing mark is caught**
  - Recommended: (a) the ledger hook holds the line once and asks; a line written again with the mark, or unchanged, is then written.
  - Answer: agreed, (a).
- **Which lesson lines the check stops**
  - Recommended: (a) every unmarked lesson line written after a decision line of the session.
  - Answer: agreed, (a).
- **Whether the `{addresses:...}` side is covered too**
  - Recommended: (a) leave it out, and name it as not done.
  - Answer: agreed, (a).
- **Change**
  - Asked: at `/pre-spec` the person agreed to the fix of a finding: the Criterion of Case 682.2 said a lesson line with no mark that the new check does not hold is written, while Case 682.1 drops an unmarked line beside a marked line of the same slug.
  - Taken: the Criterion of Case 682.2 now says a lesson line with no mark is written when the new check neither holds nor drops it.

## History

- 2026-10-06 created · raw/2026-10-05/2249/ledger.md#case-682
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
