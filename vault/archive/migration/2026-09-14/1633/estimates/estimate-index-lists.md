---
type: estimate
kind: QA
status: archived
target: "[[rule-index]]"
origin: raw/2026-09-09/ledger.md#case-22
sprint: migration
created: 2026-09-09
tags: [harness, workflow]
---

## Context

The indexes are what the `ask-guppi` agent and, from Slice 3, the librarian read instead
of pages. A line missing, stale or out of order is a page the search cannot find.

## Criterion

Against a temp vault: each category file holds exactly one line per live page in slug order with the field its schema names, a page with deferred_by ending with · deferred_by: <slugs>; an archived page and a decision have no line; an empty category yields an empty
file; `--check` exits 1 naming a stale file and 0 when all match, writing nothing. Against
the live vault: four files appear and none for estimates, `rules-index.md` has one line per page of `rules/`,
and `--check` exits 0 right after.

## Method

pytest in `tests/test_index.py`; the live reading once by hand, written into the estimate
line.

## Result

tests/test_index.py 6 green with four files, no estimates file and the deferred_by suffix; live 2026-09-11 after the migrations: uv run guppi index wrote four files, rules-index.md has 33 lines for 33 pages of rules/, five of them ending in · deferred_by: (decision-case-29, 45, 50, 51), estimates-index.md is gone, index --check exit 0 right after

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-22
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-11 updated: no estimates index; four files; the deferred_by suffix · [[decision-case-53.4]]
- 2026-09-11 status: pending → passed · raw/2026-09-11/ledger.md#L68
- 2026-09-14 deleted · [[decision-case-147.1]]
- 2026-09-14 archived · cleanup
