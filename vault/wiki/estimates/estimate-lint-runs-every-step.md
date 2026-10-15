---
type: estimate
kind: QA
status: passed
target: "[[rule-lint]]"
purpose: Whether guppi check runs every step, guppi ship --check last, when an earlier one is red, prints the lines of each, exits non-zero when any step is red, and skips guppi ship --check where the command ship is missing
method: "uv run --project .guppi pytest .guppi/tests/test_check.py; by hand, after the librarian's run that applies the reword of this change: a Grep of make with the target lint over the live rules, entities and Estimates and over .claude/, read against the Criterion"
checked: 2026-10-15
origin: raw/2026-10-02/1202/ledger.md#case-587
sprint: migration
created: 2026-10-02
tags: [harness, workflow]
---

## Criterion

When:
Someone runs `uv run --project .guppi guppi check` in a project: by hand, in the Baseline of `/work`, in the librarian's run of `.claude/agents/librarian-guppi.md`, or in the job `lint` of `.github/workflows/checks.yml`.
**＋** Or `.guppi/tests/test_check.py` runs it in a temporary project whose steps record each call: once with the step `guppi backlog --check` failing, once with every step exiting 0, and once with no module `.guppi/guppi/ship.py`.

Then:
It runs `guppi render --check`, `guppi sprint --check`, `guppi backlog --check`, `guppi glossary --check`, `guppi lint` and `guppi ship --check`, in that order, whether an earlier step exited 0 or not.
**＋** Each step prints its own lines as it does when it runs alone, so a red step hides no finding of a later step.
**＋** It exits non-zero when any step exits non-zero, and 0 only when every step exits 0.
**＋** No live rule, entity or Estimate outside History and Result, and no file of `.claude/`, names make with the target `lint` as the way to run the vault checks.
**－** Where the module `.guppi/guppi/ship.py` is missing, as in a project that installed GUPPI, it runs the other five steps and prints one line that it skips `guppi ship --check`, and that skip sets no exit code.
**－** No step reads the stdin of its caller, and it writes nothing to the tree.

## Result

2026-10-15, the /hi of session 1959: `uv run --project .guppi pytest -q .guppi/tests/test_check.py` 7 passed; a search for `make lint` as whole words outside History and Result over the live rules, entities and Estimates and every file of `.claude/`: 0 hits

## History

- 2026-10-02 created · [[decision-case-587]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 deferred · [[decision-case-631]]
- 2026-10-05 updated: the Criterion replaced whole — tests run make lint with a fake uv, one whose backlog step is red and one whose steps are all green; the method is those tests, and the defer of case 631 is taken up (case 637.3) · [[decision-case-637.3]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/0109/ledger.md#L2
- 2026-10-14 updated: the Criterion replaced whole — guppi ship --check is the last step of make lint (case 807.2) · [[decision-case-807.2]]
- 2026-10-14 status: pending → passed · raw/2026-10-13/2118/ledger.md#L21
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 updated: the Criterion replaced whole — guppi check runs the vault checks in place of the target lint of the Makefile · [[decision-case-820.1]]
- 2026-10-15 status: pending → passed · raw/2026-10-15/1959/ledger.md#L4
