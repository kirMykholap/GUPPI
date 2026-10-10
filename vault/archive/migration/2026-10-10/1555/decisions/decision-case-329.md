---
type: decision
case: "329"
status: archived
update: ["[[estimate-sprint-migration-index-dissolved]]"]
origin: raw/2026-09-22/1724/ledger.md#case-329
sprint: migration
created: 2026-09-22
tags: [sprint, workflow, harness]
---

## Context

`check_method` in lint takes one of four things for the Estimate of a Leaf: a file under `tests/`, the word `pytest`, a `make <target>` of the Makefile, or a reading — and a reading is recognised literally, by the words `by hand` or `reading` in the text of `method`. `estimate-sprint-migration-index-dissolved` describes exactly a reading by hand: `test -e vault/wiki/index.md` false, then `rg` over `vault/wiki`, `.claude`, `guppi` and `CLAUDE.md`, every hit read by eye. But the text opens with "at the close of theme 4" and calls the act "read by eye" — neither of the two words lint looks for stands there, and the finding of the class `method` holds. The sibling `estimate-sprint-migration-rule-class-files-dissolved` describes the same kind of work and passes, because it opens with "one reading at the close of Slice 3f".
The page stands `pending` and its reading is due this session; the Case touches neither the Criterion nor the status — by case 296 a `set` without `status` changes the named field alone.

## Problem

The text of `method` describes a reading without calling it one, so lint cannot classify it. Either the wording is fixed, or lint learns to read a shell command as a reading.

## History

- 2026-09-23 created · raw/2026-09-22/1724/ledger.md#case-329
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
