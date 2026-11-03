---
type: estimate
kind: QA
status: passed
target: "[[rule-lint]]"
purpose: An Estimate whose method names no form of reading, or a test file or make target that does not exist, is a finding of lint
method: uv run --project .guppi pytest .guppi/tests/test_lint.py
checked: 2026-10-17
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi lint` reads the `method` field of each live Estimate.

Then:
For an Estimate of a Leaf, a test file that exists, the word `pytest`, a `make <target>` of the `Makefile`, one of the commands `guppi test`, `guppi check` and `guppi style`, or `by hand` passes; else the finding "method: names no test file, pytest, guppi command or make target and is not a reading".
**＋** A named test file that does not exist, or a `make <target>` that the `Makefile` does not hold, is a finding.
**＋** For an Estimate of a MOC, a `make <target>` of the `Makefile` passes whatever stands beside it, and so does the word `pytest` with one or more test files, each of which exists.
**＋** For an Estimate of a MOC with no `parent`, the command `guppi test` passes whatever stands beside it.
**＋** For an Estimate of a MOC, `by hand` without any of these passes when every counted Estimate of the children is a reading or a sibling Estimate names a `make <target>` or `pytest` with test files; else a finding.
**＋** On a MOC with `render_mode: full`, the Estimates of a child with `enforcement: render` are not counted.
**＋** `estimate-claude-md-rendered` gets no `method` finding.
**－** On a MOC, the word `pytest` with no test file, a test file with no `pytest`, and a command `guppi check` or `guppi style` alone are each a finding.
**－** On a MOC with a `parent`, the command `guppi test` alone is a finding.
**－** On a MOC with `render_mode: full`, the Estimates of a child without `enforcement: render` are counted.
**－** On a MOC without `render_mode: full`, the Estimates of every child are counted, a child with `enforcement: render` included.
**－** A `## Method` section is not read as the `method` of a page.

## Result

2026-10-17, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
