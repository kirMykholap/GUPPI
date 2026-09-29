---
type: estimate
kind: QA
status: pending
target: "[[rule-lint]]"
purpose: An Estimate whose method names no form of reading, or a test file or make target that does not exist, is a finding of lint
method: uv run pytest tests/test_lint.py
checked: 2026-09-27
origin: raw/2026-09-24/1916/ledger.md#case-401.4
sprint: migration
created: 2026-09-24
tags: [harness, workflow]
---

## Criterion

When:
`uv run guppi lint` reads the `method` field of each live Estimate.

Then:
For an Estimate of a Leaf, a `tests/` file that exists, the word `pytest`, a `make <target>` of the `Makefile`, or `by hand` passes; else the finding "method: names no tests/ file, pytest or make target and is not a reading".
**＋** A named `tests/` file that does not exist, or a `make <target>` the `Makefile` does not hold, is a finding.
**＋** For an Estimate of a MOC, a `make <target>` of the `Makefile` passes whatever stands beside it; `by hand` without one passes when every counted Estimate of the children is a reading or a sibling Estimate names a `make <target>` of the `Makefile`; else a finding.
**＋** On a MOC with `render_mode: full`, the Estimates of a child with `enforcement: render` are not counted.
**＋** `estimate-claude-md-rendered` gets no `method` finding.
**－** On a MOC with `render_mode: full`, the Estimates of a child without `enforcement: render` are counted.
**－** On a MOC without `render_mode: full`, the Estimates of every child are counted, a child with `enforcement: render` included.
**－** A `## Method` section is not read as the `method` of a page.

## Result

2026-09-27, uv run pytest tests/test_lint.py; 75 passed, and live make lint prints no method finding, none on estimate-claude-md-rendered

## History

- 2026-09-25 created · [[decision-case-401.4]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L45
- 2026-09-27 updated: the Criterion replaced whole — on a MOC with render_mode: full the Estimates of a child with enforcement: render are not counted (case 459) · [[decision-case-459]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/2050/ledger.md#L19
- 2026-09-29 updated: the Criterion replaced whole — the method field only, no ## Method section read (case 506.3) · [[decision-case-506.3]]
