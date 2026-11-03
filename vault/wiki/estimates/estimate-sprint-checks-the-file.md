---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint]]"
purpose: sprint --check names sprint.md when it differs from the render of the live sprint page, or from the closed form when no live sprint page stands, exit 1, and writes nothing
method: uv run --project .guppi pytest .guppi/tests/test_sprint.py
checked: 2026-10-17
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, sprint]
core: true
---

## Criterion

When:
Someone runs `uv run --project .guppi guppi sprint --check`, by hand or through `uv run --project .guppi guppi check`, and it renders the file from the sprint page in memory.

Then:
When `vault/wiki/sprint.md` differs from the render of the page, stdout holds one line `sprint: <file> differs from entity-sprint-<id>`, the file named by its path from the project root, and the check exits 1. When the file equals the render, the check exits 0 with no output. The file is written in neither case.
**＋** `uv run --project .guppi guppi check` runs it after `guppi render --check` and before `guppi lint`.
**＋** With no live sprint page, the check compares the file with the closed form that `estimate-sprint-marks-a-closed-sprint` sets, and the line on stdout reads `sprint: <file> differs from the closed form of <id>`.
**－** A render error, such as two sprint pages, a slug with no page, or no sprint page and no file, is one line on stderr and exit 1, as with `guppi sprint`.

## Result

2026-10-17, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
