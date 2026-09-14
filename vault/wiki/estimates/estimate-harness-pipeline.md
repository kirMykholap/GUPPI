---
type: estimate
kind: QA
status: passed
target: "[[rule-harness]]"
origin: raw/2026-09-10/ledger.md#case-37
sprint: migration
created: 2026-09-10
tags: [harness, workflow]
---

## Context

The four tools guard each other: a renderer that drifts is caught by lint, an index that lags by its check.

## Criterion

make test-harness runs the tests of the renderer, lint and the indexes as one
pipeline, green; make lint runs render --check, then index --check, then guppi
lint, and the first two exit 0 on the committed tree.

## Method

`make test-harness`, the pipeline over tests/test_render.py, tests/test_lint.py and tests/test_index.py; the live reading of make lint by hand

## Result

`make test-harness` 44 green; `make lint` ran render --check (exit 0), index --check (exit 0), guppi lint (159 findings, the known list) in that order

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-37
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L74
