---
type: estimate
kind: QA
status: passed
target: "[[rule-guppi-package]]"
purpose: Whether .guppi/.gitignore keeps the __pycache__/ folders that Python writes under .guppi/ out of git, so that the gate of /handoff finds no untracked cache in a project that installs GUPPI
method: uv run --project .guppi pytest .guppi/tests/test_guppi_package.py -k caches
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [git, plugin]
core: true
---

## Criterion

When:
In a git project that holds the code of GUPPI under `.guppi/`, the tests run, and Python writes `__pycache__/` folders beside the code and the tests.
**＋** Then `/handoff` is called, and `dirty` of `.guppi/guppi/gate.py` reads `git status --porcelain`.

Then:
`.guppi/.gitignore` holds the line `__pycache__/` beside the line `.venv/`.
**＋** git lists no file of a `__pycache__/` folder under `.guppi/` as untracked, and `dirty` shows none.
**＋** The gate does not refuse `/handoff` for those caches.
**＋** The clean version that `rule-clean-branch` builds holds `.guppi/.gitignore` with that line.
**－** No ignore file outside `.guppi/` changes, the root ignore file of a project included.

## Result

2026-11-20, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
