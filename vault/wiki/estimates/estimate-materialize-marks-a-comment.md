---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: "A then block that holds a YAML comment gives each decision entry of its Case incomplete: [comment], judged by the one function the Stop hook of rule-spec-write imports"
method: uv run --project .guppi pytest .guppi/tests/test_materialize.py -k comment
checked: 2026-09-30
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, ledger]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi materialize` lifts the entries of a Case N from its fences tagged `then` in `raw/<date>/<HHMM>/spec.md`.

Then:
A fence of Case N that holds a YAML comment — a `#` at the start of a line or after a space or a tab, outside a quoted value and outside a `|` or `>` block — gives each decision entry of Case N `incomplete: [comment]`, and the run does not fail.
**＋** The entry keeps the values that YAML read, and nothing is invented for the text after the `#`.
**＋** The comment is found by the same function of `.guppi/guppi/materialize.py` that the `Stop` hook of `rule-spec-write` imports, so both give the same answer for the same fence.
**－** A `#` inside a quoted value or inside a `|` or `>` block is text and gives no mark.
**－** `generate` still applies an entry so marked, since a page is always created, even incomplete.

## Result

2026-09-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
