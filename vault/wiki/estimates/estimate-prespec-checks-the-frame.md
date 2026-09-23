---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: A Case names in when, then and its then block only what its given names
method: pytest tests/test_prespec.py on a temp plan
origin: raw/2026-09-23/1355/ledger.md#case-378.7
sprint: migration
created: 2026-09-23
tags: [harness, workflow]
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

2026-09-23, uv run pytest tests/test_prespec.py -k "frame or slug_in_then or target_of_the_then or slash_command or lone_slash or sub_case_is_checked or without_given_is_not": 7 passed — a slug in then, a then-block target and /hi outside given are findings; a lone / span is clean; a sub-case is checked by its parent's given; a Case without given is not checked; live — guppi prespec --check on the Spec of session 1355 exit 0

## History

- 2026-09-23 created · [[decision-case-378.7]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1355/ledger.md#L42
