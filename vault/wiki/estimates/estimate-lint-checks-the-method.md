---
type: estimate
kind: QA
status: passed
target: "[[rule-lint]]"
purpose: An Estimate whose method names no form of reading, or a test file or make target that does not exist, is a finding of lint
method: uv run --project .guppi pytest .guppi/tests/test_lint.py
checked: 2026-10-15
origin: raw/2026-09-24/1916/ledger.md#case-401.4
sprint: migration
created: 2026-09-24
tags: [harness, workflow]
---

## Criterion

When:
`uv run --project .guppi guppi lint` reads the `method` field of each live Estimate.

Then:
For an Estimate of a Leaf, a test file that exists, the word `pytest`, a `make <target>` of the `Makefile`, one of the commands `guppi test`, `guppi check` and `guppi style`, or `by hand` passes; else the finding "method: names no test file, pytest, guppi command or make target and is not a reading".
**＋** A named test file that does not exist, or a `make <target>` that the `Makefile` does not hold, is a finding.
**＋** For an Estimate of a MOC, a `make <target>` of the `Makefile` passes whatever stands beside it, and so does the word `pytest` with one or more test files, each of which exists.
**＋** For an Estimate of a MOC, `by hand` without either passes when every counted Estimate of the children is a reading or a sibling Estimate names either; else a finding.
**＋** On a MOC with `render_mode: full`, the Estimates of a child with `enforcement: render` are not counted.
**＋** `estimate-claude-md-rendered` gets no `method` finding.
**－** On a MOC, the word `pytest` with no test file, a test file with no `pytest`, and a command `guppi test`, `guppi check` or `guppi style` alone are each a finding.
**－** On a MOC with `render_mode: full`, the Estimates of a child without `enforcement: render` are counted.
**－** On a MOC without `render_mode: full`, the Estimates of every child are counted, a child with `enforcement: render` included.
**－** A `## Method` section is not read as the `method` of a page.

## Result

2026-10-15, uv run --project .guppi pytest .guppi/tests/test_lint.py: 110 passed, exit 0

## History

- 2026-09-25 created · [[decision-case-401.4]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L45
- 2026-09-27 updated: the Criterion replaced whole — on a MOC with render_mode: full the Estimates of a child with enforcement: render are not counted (case 459) · [[decision-case-459]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/2050/ledger.md#L19
- 2026-09-29 updated: the Criterion replaced whole — the method field only, no ## Method section read (case 506.3) · [[decision-case-506.3]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1432/ledger.md#L25
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 updated: the Criterion replaced whole — the commands guppi test, guppi check and guppi style are forms, and on a MOC pytest with test files that exist passes · [[decision-case-820.3]]
- 2026-10-15 status: pending → passed · raw/2026-10-15/1739/ledger.md#L7
