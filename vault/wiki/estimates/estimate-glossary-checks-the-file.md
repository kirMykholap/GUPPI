---
type: estimate
kind: QA
status: passed
target: "[[rule-glossary]]"
purpose: glossary --check names glossary.md when it differs from the render of entity-glossary, exit 1, and writes nothing
method: "uv run --project .guppi pytest .guppi/tests/test_glossary.py; uv run --project .guppi guppi glossary --check in the working tree at Retro: exit 0 and no output"
checked: 2026-10-26
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, librarian, session]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi glossary --check` runs, as `uv run --project .guppi guppi check` runs it, and renders the file from `entity-glossary` in memory.

Then:
When `vault/wiki/glossary.md` differs from the render or is missing, stdout holds one line `glossary: <file> differs from entity-glossary`, the file named by its path from the project root, and the check exits 1.
**＋** When the file equals the render, the check exits 0 with no output.
**－** The check writes no file and ticks no line of a Spec.

## Result

2026-10-26, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
