---
type: estimate
kind: QA
status: passed
target: "[[rule-index-check]]"
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

### case 147.3

When:
The librarian does the index check.

Then:
"for each `create` entry … run the Grep of its category yourself — `^(purpose|deferred_by):` over `vault/wiki/<category>/` (`root_cause` for lessons, `pattern` for insights) — and compare the entry's `purpose` (`root_cause` for a lesson) with every index line it returns"; the rest as it is.
**＋** The report names the Grep and the number of lines compared with.
**－** The name of the rule does not change.

## Method

one reading by hand after the first librarian run, recorded in the estimate line

## Result

live 2026-09-15, the librarian's run of session Q read against the brief: four lesson creates compared against the Grep `^(root_cause|deferred_by):` over `wiki/lessons/`, 27 lines named with their count; 0 merged and none was due; 1 near (`lesson-retro-typed-still-bypasses-the-skill-tool-after-150` near `lesson-retro-typed-by-the-person-bypasses-the-skill-tool-and-the-gate`) settled on the index line with the reason; no page opened; no create in another category, the Greps of `rules/` and `entities/` not run; no comparison crossed categories

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-35.1
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L90
- 2026-09-10 updated: an opened page is named in the report with the index line that did not settle it · raw/2026-09-10/ledger.md#case-49
- 2026-09-11 status: passed → passed · raw/2026-09-10/ledger.md#L125
- 2026-09-14 criterion: case 147.3 added · [[decision-case-147.3]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1448/ledger.md#L1
