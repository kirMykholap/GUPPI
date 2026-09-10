---
type: estimate
kind: QA
status: pending
target: rule-index-check
origin: raw/2026-09-10/ledger.md#case-35.1
sprint: migration
created: 2026-09-10
tags: [harness, workflow, librarian]
---

## Context

A duplicate the librarian misses is two pages for one thing; one it invents is a ratified page silently merged away.

## Criterion

After a live librarian run: the report names the comparisons made per category; a
create whose purpose an index line already carries was turned into an update of
that slug with change "merged by librarian: ..." and the mark librarian: merged,
with no other field changed; a near match was kept with near: <slug>; no page was
read when its index line sufficed; no comparison crossed categories.

## Method

one reading by hand after the first librarian run, recorded in the estimate line

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-35.1
