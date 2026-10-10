---
type: decision
case: "567"
status: archived
children: ["[[decision-case-567.1]]", "[[decision-case-567.2]]"]
origin: raw/2026-10-01/1237/ledger.md#case-567
sprint: migration
created: 2026-10-01
tags: [session, workflow, harness, librarian, render]
---

## Problem

The rule that flags every read outside four listed reasons recorded a failure for a harmless read of a live page. Opening a page to learn its field names was a step of the fourth reason. The rule asks for flags and report lines on pages that tell nothing about a gap in the frame. Meanwhile the reads that once showed such a gap are the ones the frame already says the job does not need. The flag rule and the report rule must be narrowed to those reads and to the pages behind a judgment. The brief section must also name the fields it reads, so that no page has to be opened to learn them.

## Recommend

- **Which reads must the librarian still flag in the brief?**
  - Recommended: (b) flag only the reads the instructions say the job does not need; a live page under `vault/wiki/` is free to open with no flag.
  - Answer: (b), agreed with the recommendations.
- **Does the report still name every page the librarian opens?**
  - Recommended: (a) name only the pages that decided something: a copy-or-close judgment, a shared-cause judgment, a script error.
  - Answer: (a), agreed with the recommendations.

## History

- 2026-10-01 created · raw/2026-10-01/1237/ledger.md#case-567
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
