---
type: decision
case: "297"
status: archived
update: [estimates-schema, index]
origin: raw/2026-09-21/1315/ledger.md#case-297
sprint: migration
created: 2026-09-21
tags: []
---

## Context

`estimates/schema.md`, the row `## Criterion`: "an `update` that names the Estimate by slug replaces it whole and sets the page `pending`" — after 296 not always. `index.md` §7: "a Case that changes the promise names the Estimate by slug and its `update` replaces the Criterion whole … only a replaced Criterion does" — right for the change of a promise, silent on the second form. Both are Rule-class files: an `update` with `file`, applied by hand in Work Mode; `generate` reports the item as applied by hand. §3 ("only a replaced Criterion sets it `pending`") holds as it is — a pair inside the Criterion is a replaced Criterion.

## Problem

The schema of Estimates says outright that any `update` by slug replaces the Criterion whole; after 296 that is false in the same way as the three `given` lines of 295.

## History

- 2026-09-21 created · raw/2026-09-21/1315/ledger.md#case-297
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
