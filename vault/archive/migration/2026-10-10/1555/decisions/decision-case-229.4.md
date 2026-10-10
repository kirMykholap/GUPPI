---
type: decision
case: "229.4"
status: archived
update: ["[[rule-brief]]", "[[estimate-brief-written]]"]
origin: raw/2026-09-17/1119/ledger.md#case-229.4
sprint: migration
created: 2026-09-17
tags: [harness, workflow, librarian]
---

## Context

`entity-sprint-migration` is the sprint page (case 209): its `estimates` are the Definition of done, its `## Backlog` the Slices, each item a wikilink to a page; `guppi sprint` renders `sprint.md` from it, `/hi` reads the file whole and assembles the Frontier — "where the sprint stands" — and the brief puts every deferred target into Deferred (cap 7, ranked by severity and the count of briefs). The result shows in this session: Slice 5 stands in the Frontier every time, `rule-work-mode` in Deferred for nineteen briefs, and the only place for "some day" is a defer with a placeholder page. The Case touches four rules and one Estimate of three of them: `estimate-sprint-renders-the-backlog` (`pending`, the new shape), `estimate-hi-writes-frontier` (`passed`, the old shape — a recut with `set.method`), `estimate-brief-written` (`pending`, the new shape); the Estimates of `entity-sprint-migration` it does not touch. `generate` puts a new section of a page after the existing ones, before History; the order of a category's sections is `SECTION_ORDER` in the code and `entities/schema.md`.

## Problem

The Frontier and the brief show everything not closed, whoever's turn it is; an item without a turn has no place but Deferred, where it counts briefs and wears the eye. A sprint is an order, not a list.

## History

- 2026-09-18 created · raw/2026-09-17/1119/ledger.md#case-229.4
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
