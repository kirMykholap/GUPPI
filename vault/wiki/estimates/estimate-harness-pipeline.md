---
type: estimate
kind: QA
status: pending
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

### case 153

When:
`make lint` and `make test-harness` run; someone reads `rule-harness`.

Then:
The Purpose: "Three rules belong to no phase of the session: the renderer, the page `.claude/settings.json` is assembled from, and lint. They run together in `make lint`, in this order: the harness files are checked against their pages before the pages. Four more belong here and run in no pipeline: the hook that refuses a hand edit of a rendered file, the hook that refuses a heredoc with a backslash or a file write, the page `CLAUDE.md` is rendered from, and the pinned clock of the tests (cases 59.6, 59.8, 127, 145.1)."
**＋** `estimate-harness-pipeline`: block 153, `pending`; Method: "`make test-harness` over `tests/test_render.py` and `tests/test_lint.py`; the live reading of `make lint` by hand".

## Method

`make test-harness` over tests/test_render.py and tests/test_lint.py; the live reading of make lint by hand

## Result

`make test-harness` 44 green; `make lint` ran render --check (exit 0), index --check (exit 0), guppi lint (159 findings, the known list) in that order

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-37
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L74
- 2026-09-14 criterion: case 153 added · [[decision-case-153]]
