---
type: rule
kind: Leaf
purpose: Prevents a pre-task check from reading every page of a category to learn what already exists
status: built
enforcement: check
implementation_ref: [guppi/index.py, tests/test_index.py, Makefile]
parent: rule-harness
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

`parent: rule-harness` names the MOC of the harness tools: the indexes are written and checked with the renderer and lint, in no phase of the session.

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
- 2026-09-10 updated: parent is rule-harness · raw/2026-09-10/ledger.md#case-37
- 2026-09-10 status: draft → built · cascade
