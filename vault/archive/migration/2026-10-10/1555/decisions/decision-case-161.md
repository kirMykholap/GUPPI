---
type: decision
case: "161"
status: archived
update: ["[[rule-materialize]]"]
origin: raw/2026-09-15/1110/ledger.md#case-161
sprint: migration
created: 2026-09-15
tags: [harness, workflow, ledger]
---

## Context

A change of a Rule-class file — `index.md`, `glossary.md`, `case-schema.md`, any `schema.md` — is written in the Spec as `case-schema.md` says: an `update` with the keys `file` and `change`, no `slug`. The ledger line carries a slug — `case-schema`, `index`. `materialize` looks for the `then` item of a ledger line by `slug` only; it finds none and marks the entry `incomplete: [then]`, though the item is there and the path of the file is derived from the slug anyway. So were the 13 entries of the run of P marked, and the entry of 133 in the run of O; the brief lists them under Flags each time as "the same class". The test of this case seeds an item with `slug` and `file` together — so it is green while a Spec written by the schema is red.

## Problem

Every session that touches a Rule-class file leaves false `incomplete` marks in the yaml, and the brief lists them; the code or the shape of the item in the Spec has to change.

## Given

`materialize.py` `find_item` compares `item["slug"]` with the slug of the line; `rule_class_path(slug)` gives the path for `index`, `glossary`, `case-schema`, `<category>-schema[-yaml]`; the branch "an item with `file`" after `find_item` is unreachable for an item without `slug`.
**＋** `case-schema.md`: "A Rule-class file … is an `update` with `file` and `change`"; the Spec of this session (Case 159) is written that way.
**＋** `tests/test_materialize.py:303` seeds `slug: glossary` with `file` — passes; no test seeds an item without `slug`.
**＋** `rule-materialize` (`built`, `estimates: [estimate-materialize-assembles]`, `pending` by 158): "a Rule-class file is `file` with its `path`"; how the item is found the text does not say.
**－** `generate` does not change: it skips a `file` entry with the line "applied by hand" as today.

## Criterion

- [[estimate-materialize-assembles]] § case 161

## History

- 2026-09-15 created · raw/2026-09-15/1110/ledger.md#case-161
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
