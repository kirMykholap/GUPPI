---
type: estimate
kind: QA
status: passed
target: "[[rule-clean-branch]]"
purpose: Whether the code, the tests and the root files of this repository hold each pointer to a case, a decision or a session in a bracket of its own, and no case number without the word case before it, so that guppi ship --check prints no line on them and no bracket it removes from them holds a word the sentence needs
method: "by hand, at Retro: the lines of uv run --project .guppi guppi ship --check over the working tree, and of uv run --project .guppi guppi ship --review into an empty temporary folder, on .guppi/guppi/, .guppi/tests/, Makefile, pyproject.toml and .gitattributes, read against the Criterion"
checked: 2026-10-28
origin: raw/2026-10-13/2118/ledger.md#case-807.3
sprint: plugin
created: 2026-10-13
tags: [ci, plugin]
---

## Criterion

When:
At Retro of the session, `uv run --project .guppi guppi ship --check` of `.guppi/guppi/ship.py` judges the working tree, and `uv run --project .guppi guppi ship --review <folder>` builds the clean version into an empty folder.

Then:
`uv run --project .guppi guppi ship --check` prints no line on a file under `.guppi/guppi/` or `.guppi/tests/`, on `Makefile`, on `pyproject.toml` or on `.gitattributes`, a bare case number in a comment or a docstring included.
**＋** Each line of `--review` on those files shows a bracket that holds only pointers and the words that go with them, such as what a pointer sets, when a thing was measured or which session a pointer names.
**＋** In `.guppi/tests/test_casecheck.py`, the docstring of `built_again_sibling` and the comment after `plan_with(working, PLANNED_5)` name the made-up Case of the test as the sibling Case, with no number.
**－** The rewording changes no line but a comment or a docstring, and `uv run --project .guppi guppi test` has no failing test that it did not have before the change.
**－** A line of `--check` on `.claude/` or `CLAUDE.md` is no part of this promise: it goes into the handoff with the pages, and the red of `uv run --project .guppi guppi check` it makes is a note for the handoff by `rule-retro`.

## Result

2026-10-28, Retro: uv run --project .guppi guppi ship --check printed 0 lines; uv run --project .guppi guppi ship --review --allow-draft into an empty temporary folder printed 67 lines on .guppi/guppi/ and .guppi/tests/ and none on Makefile, pyproject.toml or .gitattributes, each a bracket of pointers and the words that go with them (what a pointer sets, a measurement date, a session); in test_casecheck.py the docstring of built_again_sibling and the comment after plan_with(working, PLANNED_5) name the sibling Case with no number; the rewording changed only that comment and that docstring, and uv run --project .guppi guppi test gives 1790 passed, 6 skipped, 1 deselected, no failing test

## History

- 2026-10-14 created · [[decision-case-807.3]]
- 2026-10-14 status: pending → passed · raw/2026-10-13/2118/ledger.md#L22
- 2026-10-14 updated: the Criterion replaced whole — the code writes each case number with its word · [[decision-case-808.2]]
- 2026-10-14 status: pending → passed · raw/2026-10-14/0101/ledger.md#L57
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `make lint` → `uv run --project .guppi guppi check` · [[decision-case-820.7]]
- 2026-10-15 reworded: `make test` → `uv run --project .guppi guppi test` · [[decision-case-820.7]]
- 2026-10-28 updated: the Criterion replaced whole — the tests under .guppi/tests/ hold pointers only in brackets too · [[decision-case-892]]
- 2026-10-28 status: pending → passed · raw/2026-10-28/1907/ledger.md#L15
