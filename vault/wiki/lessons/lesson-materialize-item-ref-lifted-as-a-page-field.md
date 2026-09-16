---
type: lesson
kind: error
root_cause: "`_lift_item` copies every key of a `then` item into `fields` except a fixed list; case 194.1 gave the Estimate item a `ref` and the list was not extended, so the entry's `ref` and a page field were written from the same key"
status: clustered
insight: "[[insight-materialize-lift-loses-a-schema-field]]"
origin: raw/2026-09-16/1955/ledger.md#L40
sprint: migration
created: 2026-09-16
tags: [harness, ledger]
---

## Trigger

the yaml preview of session 1955 showed `ref: rule-page-generation` under `fields` of every Estimate create, and the 13 Estimate pages born of cases 188 and 189 carry a stray `ref` field beside `target`

## Root cause

`_lift_item` copies every key of a `then` item into `fields` except a fixed list; case 194.1 gave the Estimate item a `ref` and the list was not extended, so the entry's `ref` and a page field were written from the same key

## History

- 2026-09-16 created · raw/2026-09-16/1955/ledger.md#L40
- 2026-09-16 updated: clustered by librarian under insight-materialize-lift-loses-a-schema-field
