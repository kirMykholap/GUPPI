---
type: estimate
kind: QA
status: passed
target: "[[rule-clean-branch]]"
purpose: "Whether guppi ship writes each passed Estimate of a page it writes, with core: true and a Result of one line, and no Estimate that is pending or failed, whose target it does not write, or whose method names a make target"
method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k estimate
checked: 2026-10-15
origin: raw/2026-10-15/0553/ledger.md#case-822.1
sprint: plugin
created: 2026-10-15
tags: [ci, plugin]
---

## Criterion

When:
`uv run --project .guppi guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.

Then:
It writes each Estimate whose status is `passed` and whose target is a page it writes, with `core: true`, `origin: guppi`, `sprint: guppi` and a `## History` of one line.
**＋** The `## Result` of each Estimate it writes is one line: the date of its `checked` and that it passed in the repository of GUPPI.
**＋** Each Estimate it writes keeps its `status`, `checked`, `purpose`, `method` and `## Criterion`, cleaned as the text of each page it writes.
**＋** The field `estimates` of each page it writes lists the Estimates it writes and no other.
**＋** `uv run --project .guppi guppi lint` over the clean version gives no finding on the `origin` or the `core` of an Estimate it writes.
**－** It writes no Estimate that is `pending` or `failed`, none whose target page it does not write, and none whose `method` names a target of the `Makefile`, by `MAKE_TARGET` of `.guppi/guppi/lint.py`.
**－** No Estimate of the project it builds from carries `core`.
**－** A pointer outside a bracket in the `## Criterion`, the `purpose` or the `method` of an Estimate it writes makes it exit 1, as a pointer in any page does.

## Result

2026-10-15, uv run --project .guppi pytest .guppi/tests/test_ship.py -k estimate: 4 passed, exit 0

## History

- 2026-10-15 created · [[decision-case-822.1]]
- 2026-10-15 status: pending → passed · raw/2026-10-15/1739/ledger.md#L3
