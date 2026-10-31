---
type: estimate
kind: QA
status: pending
target: "[[rule-materialize]]"
purpose: Whether a field of a create whose allowed values in the schema hold no text, such as core, reaches the then block, the page and pre-spec as its value by one function, and whether a value outside the list is refused by the hook
method: "uv run --project .guppi pytest .guppi/tests/test_materialize.py, which runs the hook's reading, the lift and core_as_left over the same values; by hand, after the first librarian's run that creates a page whose create writes core as true: the core field of that page and the output of uv run --project .guppi guppi lint, read against the Criterion, the result in the estimate line"
origin: raw/2026-10-31/1831/ledger.md#case-968
sprint: plugin
created: 2026-10-31
tags: [harness, schema]
---

## Criterion

When:
The `Stop` hook or the check of a Case file reads a sub-point of a `create` item by `read_tasks` of `.guppi/guppi/ratified.py`.
**＋** `uv run --project .guppi guppi materialize` lifts a `create` item from the `then` block of the Spec.
**＋** `/pre-spec` judges by `core_as_left` of `.guppi/guppi/prespec.py` whether the page of a `create` carries `core: true`.

Then:
A value of a field whose allowed values in `vault/wiki/<category>/schema.yaml` on disk hold no text, written as one code span or a fenced block, is loaded as YAML, so `true` reaches the `then` block, the page and `core_as_left` as the boolean true.
**＋** The three readers load the value by one function of `.guppi/guppi/materialize.py`, and whether a value is one of the allowed values is one function of that module, which `check_schema` of `.guppi/guppi/lint.py` imports.
**＋** A value that loads as none of the allowed values is refused by the hook: exit 2 with `` `<key>`: <value> is not one of <allowed values> `` on stderr, and nothing of the Case is written; the check of a Case file reports the same line as a finding.
**＋** The allowed values are read from the schema on disk also when the session creates or updates the schema rule of that category.
**－** A value of a field whose allowed values hold text, or for which the schema names no allowed values, stays text as before.
**－** `uv run --project .guppi guppi materialize` and `core_as_left` refuse nothing: a value outside the list that reaches them stays as it loads, and `check_schema` reports it on the page.

## History

- 2026-10-31 created · [[decision-case-968]]
