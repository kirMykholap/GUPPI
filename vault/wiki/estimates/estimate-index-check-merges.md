---
type: estimate
kind: QA
status: passed
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
with no other field changed; a near match was kept with near: <slug>; every page
opened is named in the report with the index line that did not settle same or
near; no comparison crossed categories.

## Method

one reading by hand after the first librarian run, recorded in the estimate line

## Result

live 2026-09-10: the report names the outcome per category (estimates: two near, lessons: one near, no merge); the three `near:` marks in materialize.yaml (lines 2181, 2295, 2347) point at pages of the same category, no other field of those entries changed; no create was turned into an update, and none should have been (each new page checks a behaviour its neighbour does not); the one page opened is the lesson read of 11:49:55, counted against synthesis; weak point: the report lists outcomes, not the comparisons made

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-35.1
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L90
- 2026-09-10 updated: an opened page is named in the report with the index line that did not settle it · raw/2026-09-10/ledger.md#case-49
