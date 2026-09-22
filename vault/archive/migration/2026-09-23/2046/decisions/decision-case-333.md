---
type: decision
case: "333"
status: archived
defer: ["[[rule-documentation]]"]
superseded_by: ["[[decision-case-348]]"]
origin: raw/2026-09-22/1724/ledger.md#case-333
sprint: migration
created: 2026-09-22
tags: [session, workflow, harness, librarian, render]
---

## Context

`estimate-documentation-completes` is a promise of `rule-documentation`, the frame of the librarian. The reading of 2026-09-22 failed on one clause: the librarian of session 0014 read lines 52–64 of `ledger.md` while counting the entries, and the Criterion says the frame reads no ledger. Step 6, the commit and `make test-documentation` were green. The page stands `draft`, the Estimate `failed`, and lint holds a line `unread: failed` on it.

## Problem

One of two things is wrong: the wording of the Criterion that forbids the frame a ledger, or the run itself. Deciding it means reading the frame again and understanding what sent the librarian there — a Case of its own, and this session already carries nine.

## Deferred

### [[rule-documentation]]

Whether the Criterion forbids the librarian a reading it in fact needs, or the run of 0014 stepped outside the frame

## History

- 2026-09-23 created · raw/2026-09-22/1724/ledger.md#case-333
- 2026-09-23 superseded by decision-case-348 · [[decision-case-348]]
- 2026-09-23 archived · superseded
- 2026-09-23 archived · cleanup
