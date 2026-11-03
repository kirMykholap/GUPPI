---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: A Case names in when, then and its then block only what its given names
method: pytest .guppi/tests/test_prespec.py on a temp plan
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow]
core: true
---

## Criterion

When:
`guppi prespec --check` reads a plan where a Case names in `when` or `then` a slug or path its `given` does not name, or where the slug of an item of its `then` block is not named in its `given`.

Then:
`guppi prespec --check` prints one finding per such slug or path, with the Case number, and exits 1.
**＋** A slug is the content of a code span with a category prefix by `materialize.category_of`; a path is the content of a code span that holds a `/` and at least one more character; a slash command counts as a path.
**＋** A sub-case without its own `given` is checked against its parent's.
**－** A Case without `given` (defer-only) is not checked.

## Result

2026-09-23, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
