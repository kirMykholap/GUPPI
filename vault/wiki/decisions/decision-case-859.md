---
type: decision
case: "859"
status: current
update: ["[[estimate-clean-branch-writes-the-session-files]]"]
supersedes: ["[[decision-case-855]]"]
origin: raw/2026-10-16/1712/ledger.md#case-859
sprint: plugin
created: 2026-10-16
tags: [plugin, ci]
---

## Problem

The last promise of `estimate-clean-branch-writes-the-session-files` says that the first `/hi` in an empty project starts `/sprint-open`. Since the git step of `/hi`, that `/hi` ends in a folder with no git, so the Estimate cannot pass there, and it stays failed and put off although the event its defer waited for has come.

## Recommend

- **What should the last promise say about the first `/hi`?**
  - Recommended: (a) the first `/hi` in a git repository: replace the Criterion whole, its last line on the first `/hi` whose `Branch:` line names a branch, with the purpose and the method written again to match.
  - Answer: agreed, (a).
- **Should the Estimate leave the backlog now?**
  - Recommended: (a) take it up now: retire the defer, and run the reading in the same empty folder with no git as the reading of `estimate-git-context-offers-git-init`.
  - Answer: agreed, (a). Before the answer, the main agent noted that the new Criterion lands on the page only at the librarian's run of this session, so the hand reading runs in the install session of item C3, after that run.

## History

- 2026-10-16 created · raw/2026-10-16/1712/ledger.md#case-859
