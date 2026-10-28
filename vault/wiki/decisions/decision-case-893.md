---
type: decision
case: "893"
status: current
children: ["[[decision-case-893.1]]", "[[decision-case-893.2]]"]
origin: raw/2026-10-28/1907/ledger.md#case-893
sprint: plugin
created: 2026-10-28
tags: [ci, git, plugin]
---

## Problem

The clean copy says that the event log is gitignored but ships no file that ignores it, so in a new project those sentences are false and the logs go into git. The Estimate of neutral texts stays failed and put off, and no reading shows whether its promise now holds.

## Recommend

- **How do the event logs stay out of git in an installed project?**
  - Recommended: (a) the copy ships `vault/.gitignore`.
  - Answer: agreed, (a).
- **Is the Estimate read again in this session?**
  - Recommended: (a) read at the Retro of this session.
  - Answer: agreed, (a).
- **How is it checked that the copy writes `vault/.gitignore`?**
  - Recommended: (a) add the file to the list of `estimate-clean-branch-writes-a-clean-copy`.
  - Answer: agreed, (a).
- **Change**
  - Asked: at `/pre-spec`, read the Estimate of neutral texts after the librarian's run of session 1907, at the `/hi` of the next session, so that the copy holds the new texts of Case 894.
  - Taken: 893.2 sets the `method` of `estimate-clean-branch-ships-neutral-texts` to wait for that run, and the reading at Retro is gone.

## History

- 2026-10-28 created · raw/2026-10-28/1907/ledger.md#case-893
