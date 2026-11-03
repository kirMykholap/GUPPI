---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: A replace pair inside an Estimate's Criterion is refused before the Spec is approved, so a promise changes only whole
method: pytest .guppi/tests/test_prespec.py and .guppi/tests/test_materialize.py on a temp plan and vault
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow]
core: true
---

## Criterion

When:
`guppi prespec --check` reads a plan where an `update` of an Estimate carries a `replace` pair whose `old` stands inside the `## Criterion` of that page.

Then:
`guppi prespec --check` prints a finding with the Case, the slug and the opening of the `old`, and exits 1.
**＋** `guppi materialize` marks such an entry `incomplete: [criterion]` and sets no `pending`.
**－** A pair outside `## Criterion` still changes its part alone, with no `pending`.

## Result

2026-09-23, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
