---
type: decision
case: "397.2"
status: archived
create: ["[[estimate-materialize-lifts-a-create-by-the-schema]]"]
origin: raw/2026-09-24/1916/ledger.md#case-397.2
sprint: migration
created: 2026-09-24
tags: [harness, workflow, ledger]
---

## Context

Three Estimates of `rule-materialize` stand on the list of Case 378: `estimate-materialize-assembles`, `-walks-dates` and `-marks-superseded`. All three open with `Given:`, all three carry `－` lines on the bounds of an edit ("as today", "not this one"), and all three repeat promises of their neighbours:
- the lines "`generate` applies none of them" and on the readings of a marked `create` in `-marks-superseded` belong to `generate` and to `estimate-materialize-refolds-a-reading-on-a-supersede`;
- the error of a line and of a unit in `-walks-dates` belong to `estimate-materialize-fails-alone`.

`-assembles` is a journal of 10 `＋` lines that holds three promises: the assembly of an entry, the filter of keys by `schema.yaml` (cases 214.1, 266), and the choice between a part and the whole in an `update` of an Estimate (cases 296, 378.4). Its fifth `＋` line is also out of date: it says a pair inside the Criterion sets `pending`, while since Case 378.4 the code (`lift_criterion`, `touches_criterion`) gives `incomplete: [criterion]` and sets no status. The filter of keys and the choice of a part become Estimates of their own; their slugs are free in `wiki/` and in the archive. `-walks-dates` has no `purpose` and no `method` field, and holds `## Context` and `## Method` of the old shape; `set.method` removes both sections (`generate`, case 211). `-assembles` has no `purpose`.

All three stand `passed`, `rule-materialize` `built`; after the ratification the rule goes `draft` by the cascade until the readings pass. The readings are `pytest` with no change of code and can be taken in this session. Of the other nine Estimates of the rule, `-skips-a-carried-over-unit` is rewritten by Case 401.7, `-lifts-unfiltered-on-a-schema-change` and `-refolds-a-reading-on-a-supersede` still open with `Given:` and wait for C9, and the rest are in the new model; none of them is touched here. Every item an `update` or a `create` with a `ref`, no vault query; `frame-guppi` was not dispatched: the behaviour of the rule does not change. The agent read the code itself.

## Problem

Three Criteria promise the model with `Given:` and repeat the promises of others, and one holds a line out of date; the journal `-assembles` holds three promises that break and are fixed apart.

## Given

`estimate-materialize-lifts-a-create-by-the-schema` — the new promise.
**＋** `guppi/materialize.py` — `_lift_item`, `schema_fields`, `STRUCTURAL_KEYS`, `DEFER_KEYS`.
**＋** `vault/wiki/<category>/schema.yaml` — the fields of a category.
**＋** `tests/test_materialize.py` — fixes the filter.
**＋** `estimate-materialize-lifts-unfiltered-on-a-schema-change` — the exception when the unit creates or updates `rule-<category>-schema`, a promise of its own.

## History

- 2026-09-25 created · raw/2026-09-24/1916/ledger.md#case-397.2
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
