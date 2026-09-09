---
type: rule
kind: Leaf
purpose: Prevents a page that breaks the schema, points nowhere, or claims a status its Estimates do not support from sitting in the vault unnoticed
status: draft
enforcement: check
implementation_ref: [guppi/lint.py, tests/test_lint.py, Makefile]
parent: rule-documentation
estimates: [estimate-lint-catches]
origin: raw/2026-09-09/ledger.md#case-21
sprint: migration
created: 2026-09-09
tags: [harness, workflow]
---

## Purpose

Prevents a page that breaks its schema, points at nothing, or claims a status its
Estimates do not support from sitting in the vault unnoticed. Pages are written by hand
until the generator exists and by script after; both drift, and nothing else reads the
whole graph at once. `make lint` runs it after `render --check` and `index --check`; all
three only report, so the Makefile's rule — no target writes to the tree — holds.

`parent: rule-documentation` names the Documentation MOC of Slice 3, which does not exist
yet as a page; the reference dangles until then, on purpose.

## Estimates

- [[estimate-lint-catches]]

## Parent

- [[rule-documentation]]

## Implementation

- `guppi/lint.py`
- `tests/test_lint.py`
- `Makefile`

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-21
- 2026-09-09 updated: the Method check, a Leaf names a test file, a MOC a make target · raw/2026-09-09/ledger.md#case-26.2
