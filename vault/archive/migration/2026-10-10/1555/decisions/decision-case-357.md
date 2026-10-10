---
type: decision
case: "357"
status: archived
update: ["[[rule-documentation]]", "[[estimate-documentation-completes]]"]
origin: raw/2026-09-23/0034/ledger.md#case-357
sprint: migration
created: 2026-09-23
tags: [session, workflow, harness, librarian, render]
---

## Context

Case 349 allowed the librarian one read of `ledger.md`: the count of its lines and the lines the yaml does not account for, named in the report. On that allowance the Criterion of `estimate-documentation-completes` and the Render of `rule-documentation` agree. But a few lines below, the same text keeps the refusal: an instruction of the handoff the frame forbids is not carried out, and the list still names "a read of `ledger.md`" with no exception; the Criterion says "to read the ledger" the same way. A handoff that asks for exactly the allowed read gets both answers. The librarian of 2046 refused for another reason: its frame is loaded at dispatch, and `librarian-guppi.md` is rendered only at step 4 of its own run; a rule page changes only at `generate`, so a change to the librarian's own frame works from the next run.
`rule-documentation` stands `draft`, a MOC with one Estimate, `estimate-documentation-completes`, `pending`; it is touched.

## Problem

The frame allows one read of the ledger and, a few lines later, orders to refuse a handoff that asks for it.

## History

- 2026-09-23 created · raw/2026-09-23/0034/ledger.md#case-357
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
