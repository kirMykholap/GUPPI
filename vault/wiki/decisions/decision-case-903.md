---
type: decision
case: "903"
status: current
children: ["[[decision-case-903.1]]", "[[decision-case-903.2]]"]
origin: raw/2026-10-29/1930/ledger.md#case-903
sprint: plugin
created: 2026-10-29
tags: [harness, workflow, librarian, git]
---

## Problem

The `method` of `estimate-close-commits` waits for a moment that comes once in GUPPI only. It also reads the librarian's report in a transcript that `/hi` may not open, so the reading is never taken.

## Recommend

- **Where the librarian's report is read**
  - Recommended: (b) split the report into its own check, answered by the person after `/box` shows the report; `estimate-close-commits` keeps what `git log` and `git status` show.
  - Answer: agreed, (b).
- **Which librarian's run the reading waits for**
  - Recommended: (a) a run that starts with the current text of `rule-close` in its file.
  - Answer: agreed, (a).
- **What checks the new wording**
  - Recommended: (a) no new check: `estimate-clean-branch-ships-neutral-texts` covers it.
  - Answer: agreed, (a).

## History

- 2026-10-29 created · raw/2026-10-29/1930/ledger.md#case-903
