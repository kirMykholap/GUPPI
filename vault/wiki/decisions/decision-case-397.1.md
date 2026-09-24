---
type: decision
case: "397.1"
status: current
update: ["[[estimate-materialize-assembles]]"]
origin: raw/2026-09-24/1916/ledger.md#case-397.1
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

`estimate-materialize-assembles` — the Estimate whose Criterion is replaced and whose `purpose` is set.
**＋** `guppi/materialize.py` — `assemble`, `lift_line`, `_lift_item`, `decision_record`, `fold_estimate`.
**＋** `tests/test_materialize.py` — fixes the assembly.
**＋** `vault/raw/<date>/<HHMM>/` — a unit: `ledger.md`, `spec.md`, `materialize.yaml`.

## History

- 2026-09-25 created · raw/2026-09-24/1916/ledger.md#case-397.1
