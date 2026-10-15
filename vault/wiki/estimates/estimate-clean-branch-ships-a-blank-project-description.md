---
type: estimate
kind: QA
status: passed
target: "[[rule-clean-branch]]"
purpose: Whether guppi ship writes, between the marker lines of the description in rule-claude-md and CLAUDE.md, a heading and a line that says the description is not set yet, and leaves every other line and the render check of the copy as they are
method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k description
checked: 2026-10-15
origin: raw/2026-10-15/0553/ledger.md#case-822.4
sprint: plugin
created: 2026-10-15
tags: [plugin, render]
---

## Criterion

When:
`uv run --project .guppi guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.

Then:
In the Render of `rule-claude-md` and in `CLAUDE.md` that it writes, the lines between `<!-- project-description -->` and `<!-- /project-description -->` are the heading `# Project`, a blank line and the line `Project description: not set yet.`, and nothing else.
**＋** Every other line of that Render and of that `CLAUDE.md` stays as the project it builds from holds it.
**＋** `uv run --project .guppi guppi render --check` over the clean version names no file that differs.
**－** In the project it builds from, `rule-claude-md` and `CLAUDE.md` keep the heading and the description of that project.

## Result

2026-10-15, uv run --project .guppi pytest .guppi/tests/test_ship.py -k description: 3 passed, exit 0

## History

- 2026-10-15 created · [[decision-case-822.4]]
- 2026-10-15 status: pending → passed · raw/2026-10-15/1739/ledger.md#L6
