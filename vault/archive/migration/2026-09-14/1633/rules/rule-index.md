---
type: rule
kind: Leaf
purpose: Prevents a pre-task check from reading every page of a category to learn what already exists
status: archived
enforcement: check
implementation_ref: [guppi/index.py, tests/test_index.py, Makefile]
parent: "[[rule-harness]]"
estimates: ["[[estimate-index-lists]]"]
origin: raw/2026-09-09/ledger.md#case-22
sprint: migration
created: 2026-09-09
tags: [harness, workflow]
---

## Purpose

Prevents a pre-task check from reading every page of a category to learn what already
exists. Without one line per page the vault is searched by opening files, which stops
being done long before the vault is large. `uv run guppi index` writes `vault/wiki/<category>-index.md` for entities, rules, lessons and insights — there is no estimates index: an Estimate is reached through the `estimates` field of its target, and nothing searches by criterion; the line of a page carrying `deferred_by` ends with ` · deferred_by: <slugs>`, so a deferred decision is visible without opening the page;
`--check` reports a stale one and is what `make lint` runs. The files are committed: the
`ask-guppi` agent reads them.

`parent: rule-harness` names the MOC of the harness tools: the indexes are written and checked with the renderer and lint, in no phase of the session.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-22
- 2026-09-09 updated: the files are `<category>-index.md` · raw/2026-09-09/ledger.md#case-27
- 2026-09-10 updated: parent is rule-harness · raw/2026-09-10/ledger.md#case-37
- 2026-09-10 status: draft → built · cascade
- 2026-09-11 updated: a line of a page with deferred_by ends with · deferred_by: <slugs> · [[decision-case-52.3]]
- 2026-09-11 updated: four category files; no estimates index · [[decision-case-53.4]]
- 2026-09-14 deleted · [[decision-case-147.1]]
- 2026-09-14 archived · cleanup
