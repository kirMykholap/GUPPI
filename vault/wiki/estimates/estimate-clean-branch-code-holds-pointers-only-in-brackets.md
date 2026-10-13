---
type: estimate
kind: QA
status: passed
target: "[[rule-clean-branch]]"
purpose: Whether the code and the root files of this repository hold each pointer to a case, a decision or a session in a bracket of its own, so that guppi ship --check prints no line on them and no bracket it removes from them holds a word the sentence needs
method: "by hand, at Retro: the lines of uv run guppi ship --check over the working tree, and of uv run guppi ship --review into an empty temporary folder, on guppi/, Makefile, pyproject.toml and .gitattributes, read against the Criterion"
origin: raw/2026-10-13/2118/ledger.md#case-807.3
sprint: plugin
created: 2026-10-13
tags: [ci, plugin]
---

## Criterion

When:
At Retro of the session, `uv run guppi ship --check` judges the working tree, and `uv run guppi ship --review <folder>` builds the clean version into an empty folder.

Then:
`uv run guppi ship --check` prints no line on a file under `guppi/`, on `Makefile`, on `pyproject.toml` or on `.gitattributes`.
**＋** Each line of `--review` on those files shows a bracket that holds only pointers and the words that go with them, such as what a pointer sets, when a thing was measured or which session a pointer names.
**－** No line of `guppi/` changes but a comment or a docstring, and `make test` has no failing test that it did not have before the change.
**－** A line of `--check` on `.claude/` or `CLAUDE.md` is no part of this promise: it goes into the handoff with the pages, and the red of `make lint` it makes is a note for the handoff by `rule-retro`.

## Result

2026-10-14, Retro: uv run guppi ship --check over the working tree printed no line and exited 0; uv run guppi ship --check --review printed 31 bracket lines on guppi/, each read: each holds only pointers and the words that go with them (the shape before case N, measured <date>, session N, ranges such as cases 711.1–711.3), and the one in a printed string of guppi/sprint.py:287 reads whole without it; an AST comparison of the 21 changed guppi/*.py files with HEAD, docstrings left out, found no code change; make test 1612 passed, 6 skipped

## History

- 2026-10-14 created · [[decision-case-807.3]]
- 2026-10-14 status: pending → passed · raw/2026-10-13/2118/ledger.md#L22
