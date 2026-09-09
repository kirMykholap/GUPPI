---
type: rule
kind: Leaf
purpose: Prevents a pre-task check from reading every page of a category to learn what already exists
status: draft
enforcement: check
implementation_ref: [guppi/index.py, tests/test_index.py, Makefile]
parent: rule-documentation
estimates: [estimate-index-lists]
origin: raw/2026-09-09/ledger.md#case-22
sprint: migration
created: 2026-09-09
tags: [harness, workflow]
---

## Purpose

Prevents a pre-task check from reading every page of a category to learn what already
exists. Without one line per page the vault is searched by opening files, which stops
being done long before the vault is large. `uv run guppi index` writes
`vault/wiki/<category>-index.md` for entities, rules, estimates, lessons and insights;
`--check` reports a stale one and is what `make lint` runs. The files are committed: the
`ask-guppi` agent reads them.

`parent: rule-documentation` names the Documentation MOC of Slice 3, which does not exist
yet as a page; the reference dangles until then, on purpose.

## Estimates

- [[estimate-index-lists]]

## Parent

- [[rule-documentation]]

## Implementation

- `guppi/index.py`
- `tests/test_index.py`
- `Makefile`

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-22
- 2026-09-09 updated: the files are `<category>-index.md` · raw/2026-09-09/ledger.md#case-27
