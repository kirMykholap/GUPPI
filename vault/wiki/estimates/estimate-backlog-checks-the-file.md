---
type: estimate
kind: QA
status: passed
target: "[[rule-backlog]]"
purpose: guppi backlog --check names backlog.md when it differs from the render with every Frontier and from the render without the Frontier of the newest session, exit 1, and writes nothing
method: uv run --project .guppi pytest .guppi/tests/test_backlog.py
checked: 2026-11-01
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, sprint]
core: true
---

## Criterion

When:
Someone runs `uv run --project .guppi guppi backlog --check`, by hand or through `uv run --project .guppi guppi check`, over `vault/wiki/backlog.md` and the `frontier.md` files that `frontiers` of `.guppi/guppi/generate.py` finds.

Then:
The check renders the file in memory once with every Frontier file and once without the Frontier file of the newest session, the first in the order of `frontiers` of `.guppi/guppi/generate.py`.
**＋** When `vault/wiki/backlog.md` equals either render, the check is silent and exits 0.
**＋** When it equals neither, the check prints one line on stdout that names the file and exits 1.
**＋** `uv run --project .guppi guppi backlog` without `--check` writes the render with every Frontier file.
**＋** `uv run --project .guppi guppi check` runs it after `sprint --check` and before `glossary --check`.
**－** The check writes no file in either case.
**－** `uv run --project .guppi guppi check` writes nothing to the tree.
**－** The check reads each Frontier file once, by `frontier_marks` of `.guppi/guppi/generate.py`.

## Result

2026-11-01, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
