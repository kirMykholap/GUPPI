---
type: estimate
kind: QA
status: pending
target: "[[rule-lint]]"
purpose: Whether make lint runs all five steps when an earlier one is red, prints the lines of each, and exits non-zero when any step is red
method: uv run pytest tests/test_lint.py -k every_step
origin: raw/2026-10-02/1202/ledger.md#case-587
sprint: migration
created: 2026-10-02
tags: [harness, workflow]
---

## Criterion

When:
Someone runs `make lint` of the `Makefile`: by hand, in the Baseline of `/work`, or in the librarian's run of `.claude/agents/librarian-guppi.md`.
**＋** Or `tests/test_lint.py` runs `make lint` of the `Makefile` in a temp folder, with a fake `uv` first on the search path that records each call and fails the step `guppi backlog --check`.
**＋** Or `tests/test_lint.py` runs it the same way, with a fake `uv` that exits 0 for every step.

Then:
`make lint` runs all five steps in the order `guppi render --check`, `guppi sprint --check`, `guppi backlog --check`, `guppi glossary --check`, `guppi lint`, whether an earlier step exited 0 or not.
**＋** Each step prints its own lines as it does when it runs alone, so a red step hides no finding of a later step.
**＋** `make lint` exits non-zero when any step exits non-zero, and 0 only when every step exits 0.
**－** No step reads the stdin of its caller, and `make lint` writes nothing to the tree.

## History

- 2026-10-02 created · [[decision-case-587]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 deferred · [[decision-case-631]]
- 2026-10-05 updated: the Criterion replaced whole — tests run make lint with a fake uv, one whose backlog step is red and one whose steps are all green; the method is those tests, and the defer of case 631 is taken up (case 637.3) · [[decision-case-637.3]]
