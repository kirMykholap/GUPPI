---
type: decision
case: "171"
status: archived
update: ["[[rule-page-generation]]"]
supersedes: ["[[decision-case-124.2]]"]
origin: raw/2026-09-15/1448/ledger.md#case-171
sprint: migration
created: 2026-09-15
tags: [harness, workflow, ledger]
---

## Context

Case 166.2 carries `{supersedes:case 164}`. By `rule-materialize` the entries of a superseded Case get `superseded_by`, and by 151 they are not applied: the `replace` of 164 never lands on the page, block 164 never appears, and the `remove_criterion` of block 124.2 that the line of 164 yielded is skipped too. After the run `estimate-generate-writes` would hold block 124.2 "an Insight is never created through the yaml" beside block 166.2 "the librarian's create applies", and the text of the rule would say nothing about the librarian's create. Found at pre-task.

## Problem

Who removes block 124.2 and who puts the sentence of 164 on the page, when 164 itself is not applied.

## Given

`rule-materialize`: a line with `{supersedes:case N}` marks the entries of N `superseded_by` and yields a `remove_criterion`; `rule-page-generation` (151): an entry with `superseded_by` is not applied, its Decision page written `superseded`.
**＋** The entries of 164 in this session's yaml — the `update` with `replace`, the `criterion_block` 164, the `remove_criterion` of 124.2 — all get `superseded_by: 166.2`.
**＋** `contract: same` yields the `update` and no block; a supersedes on such a line still yields the `remove_criterion` (`rule-materialize`).
**＋** The `old` text of 164 — "Any other existing page is a collision (case 101.1)." — stands once on the page.
**－** Block 166.2 does not change: the behaviour of the librarian's create is signed there.

## History

- 2026-09-15 created · raw/2026-09-15/1448/ledger.md#case-171
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
