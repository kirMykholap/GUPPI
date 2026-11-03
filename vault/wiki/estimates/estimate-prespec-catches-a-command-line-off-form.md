---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: A tasks line that names render or sprint outside the first code span is a finding of prespec --check; the ticker's form passes
method: "pytest .guppi/tests/test_prespec.py on a temp plan; by hand, after a /pre-spec: its findings on its own plan read against the Criterion"
checked: 2026-10-17
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi prespec --check <plan> --session <id>` reads the `tasks` block of every Case of a plan, as `/pre-spec` runs it on the plan of this Plan Mode.

Then:
A `tasks` line whose text after the box opens with the word `render` or `sprint`, or with `guppi render`, `guppi sprint`, `uv run --project .guppi guppi render` or `uv run --project .guppi guppi sprint` outside a code span, is a finding `case N: render line off form: <line>`.
**＋** The form the tickers of `render` and `sprint` match is `` - [ ] `uv run --project .guppi guppi render`: … `` and `` - [ ] `uv run --project .guppi guppi sprint` ``, the command in the first code span.
**－** A line that opens with a code span holding the command is no finding; a `read` line that names the command in a later span is no finding.

## Result

2026-10-17, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
