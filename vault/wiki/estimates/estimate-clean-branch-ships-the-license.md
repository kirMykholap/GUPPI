---
type: estimate
kind: QA
status: passed
target: "[[rule-clean-branch]]"
purpose: Whether guppi ship writes the LICENSE of the working tree to the root of the clean version and to .guppi/LICENSE there, judged like each other file, writes neither when the tree holds no LICENSE, and whether --check judges it in place
method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k license
origin: raw/2026-11-25/0605/ledger.md#case-1049.1
sprint: plugin
created: 2026-11-25
tags: [ci, plugin]
---

## Criterion

When:
`uv run --project .guppi guppi ship <folder>` of `.guppi/guppi/ship.py`, as `rule-clean-branch` sets it, builds the clean copy from a working tree that holds `LICENSE` at its root.
**＋** Or it builds the clean copy from a working tree with no `LICENSE`.
**＋** Or `uv run --project .guppi guppi ship --check` judges a working tree that holds `LICENSE`.

Then:
The clean copy holds `LICENSE` at its root, with the text of the `LICENSE` of the working tree, judged and cleaned like each other file it writes.
**＋** It holds the same text at `.guppi/LICENSE`, written from the root file, and the working tree holds no file at that path.
**＋** `--check` judges `LICENSE` in place and prints no line on the text of the MIT license.
**－** From a working tree with no `LICENSE` it writes neither file and prints no line for them.

## Result

2026-11-25, Retro of session 0605: uv run --project .guppi pytest .guppi/tests/test_ship.py -k license 2 passed — a tree with the text of the live LICENSE gives a copy with that text at LICENSE and at .guppi/LICENSE and guppi ship --check exits 0 with no line; a tree with no LICENSE gives a copy with neither file

## History

- 2026-11-25 created · [[decision-case-1049.1]]
- 2026-11-25 status: pending → passed · raw/2026-11-25/0605/ledger.md#L22
