---
type: decision
case: "726"
status: current
children: ["[[decision-case-726.1]]", "[[decision-case-726.2]]"]
origin: raw/2026-10-07/2114/ledger.md#case-726
sprint: migration
created: 2026-10-07
tags: [session, workflow, harness]
---

## Problem

A Case that changes a page which another Case of the same plan puts off is judged only by the one `ask-guppi` run at the first `/pre-spec`. A defer added later in the loop is never checked, and a pair the person wants is called a finding.

## Recommend

- **Who reports a page that one Case changes and another Case puts off**
  - Recommended: (b) the script reports it as a note at every run; it does not block the exit from Plan Mode.
  - Answer: agreed, (b).
- **A Case that changes a page and puts the same page off itself**
  - Recommended: (a) no note when the change and the put-off stand in one Case; a Case with sub-cases counts as one.
  - Answer: agreed, (a).
- **Whether the helper agent still judges the pair**
  - Recommended: (a) only the script judges it; the sentence leaves the instructions of the helper agent, and its check gets its last line rewritten.
  - Answer: agreed, (a).
- **What checks that the note works**
  - Recommended: (a) a new check of its own, `estimate-prespec-notes-a-page-another-case-defers`, read by a test in this session.
  - Answer: agreed, (a).

## History

- 2026-10-07 created · raw/2026-10-07/2114/ledger.md#case-726
