---
type: estimate
kind: QA
status: passed
target: "[[rule-clean-branch]]"
purpose: Whether the code, the tests and the root files of this repository hold each pointer to a case, a decision or a session in a bracket of its own, and no case number without the word case before it, so that guppi ship --check prints no line on them and no bracket it removes from them holds a word the sentence needs
method: "by hand, at Retro: the lines of uv run --project .guppi guppi ship --check --review over the working tree on .guppi/guppi/, .guppi/tests/, Makefile, pyproject.toml and .gitattributes, read against the Criterion"
checked: 2026-10-30
origin: raw/2026-10-13/2118/ledger.md#case-807.3
sprint: plugin
created: 2026-10-13
tags: [ci, plugin]
---

## Criterion

When:
At Retro of the session, `uv run --project .guppi guppi ship --check --review` of `.guppi/guppi/ship.py` judges the working tree in place and writes no folder.

Then:
It prints no line on a pointer outside its bracket in a file under `.guppi/guppi/` or `.guppi/tests/`, on `Makefile`, on `pyproject.toml` or on `.gitattributes`, a bare case number in a comment or a docstring included.
**＋** Each line of `--review` on those files shows a bracket that holds only pointers and the words that go with them, such as what a pointer sets, when a thing was measured or which session a pointer names.
**＋** In `.guppi/tests/test_casecheck.py`, the docstring of `built_again_sibling` and the comment after `plan_with(working, PLANNED_5)` name the made-up Case of the test as the sibling Case, with no number.
**－** A page with `core: true` that stands `draft` does not stop the run, and no tag `prod-x.y.z` is needed.
**－** A rewording of a comment or a docstring in those files that moves a pointer into its bracket changes no other line, and `uv run --project .guppi guppi test` has no failing test that it did not have before the change.
**－** A line of the run on `.claude/` or `CLAUDE.md` is no part of this promise: it goes into the handoff with the pages, and the red of `uv run --project .guppi guppi check` it makes is a note for the handoff by `rule-retro`.

## Result

2026-10-30, Retro of session 1713, uv run --project .guppi guppi ship --check --review over the working tree: exit 0 with no folder written, while 12 pages with core: true stand draft and with no tag needed; 98 lines, every one "a bracket with words", 68 of them on .guppi/guppi/ and .guppi/tests/ and none on Makefile, pyproject.toml or .gitattributes; one bracket of this session's own work, ratified.py:37 "(a YAML flow list of section names, case 931)", held words the sentence needs and was reworded so the bracket holds the pointer alone; each other bracket holds pointers and the words that go with them; the docstring of built_again_sibling and the comment after plan_with(working, PLANNED_5) name the sibling Case with no number; guppi test 1814 passed, 6 skipped, 1 deselected

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
- 2026-10-30 updated: pending again: guppi ship --check printed a line on .guppi/tests/test_render.py; the Criterion stands · [[decision-case-919.1]]
- 2026-10-30 status: pending → passed · raw/2026-10-30/0304/ledger.md#L33
- 2026-10-30 updated: the Criterion replaced whole — the reading runs by guppi ship --check --review, which no draft page with core: true stops · [[decision-case-928]]
- 2026-10-30 status: pending → passed · raw/2026-10-30/1713/ledger.md#L22
