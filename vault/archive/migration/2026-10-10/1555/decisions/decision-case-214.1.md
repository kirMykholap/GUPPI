---
type: decision
case: "214.1"
status: archived
update: ["[[estimate-materialize-assembles]]"]
origin: raw/2026-09-16/2238/ledger.md#case-214.1
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger]
---

## Context

`insight-materialize-lift-loses-a-schema-field` (`open`, severity 1, three lessons) was actioned by case 144.3 — "the table exists in code, `REQUIRED`" — and reopened by the librarian of 1955 with a third lesson: `_lift_item` copies every key of a `then` item into `fields` except a fixed skip list; case 194.1 gave the Estimate item a `ref`, the list was not extended, and `ref` landed on 15 pages as a field (F3, case 210). `REQUIRED` is the table of what is missing; the table of what *may* land on a page is not in the code — it is on disk: the `schema.yaml` of each category lists its `required` and `optional` fields. The Case touches one promise of `rule-materialize` — `estimate-materialize-assembles` (it gets `method` from 211.3, earlier in ledger order); `-marks-superseded`, `-fails-alone`, `-shows` and the others it does not touch.

## Problem

A skip list is wrong by construction: every new key of an item becomes a page field until somebody remembers the list. Three lessons are three times the same thing: the parser decided what reaches the page and was wrong, and lint named the page.

## History

- 2026-09-17 created · raw/2026-09-16/2238/ledger.md#case-214.1
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
