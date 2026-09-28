---
type: estimate
kind: QA
status: pending
target: "[[rule-glossary]]"
purpose: glossary --check names glossary.md when it differs from the render of entity-glossary, exit 1, and writes nothing
method: pytest tests/test_glossary.py, plus make lint after the librarian's run — no glossary line
origin: raw/2026-09-22/0014/ledger.md#case-306.5
sprint: migration
created: 2026-09-22
tags: [harness, workflow, librarian, session]
---

## Criterion

When:
`uv run guppi glossary --check` runs, as the target `lint` of the `Makefile` runs it, and renders the file from `entity-glossary` in memory.

Then:
When `vault/wiki/glossary.md` differs from the render or is missing, stdout holds one line `glossary: <file> differs from entity-glossary`, the file named by its path from the project root, and the check exits 1.
**＋** When the file equals the render, the check exits 0 with no output.
**－** The check writes no file and ticks no line of a Spec.

## Result

2026-09-22, uv run pytest tests/test_glossary.py, 8 passed: --check names vault/wiki/glossary.md when it differs from entity-glossary, exit 1, writes nothing, and is silent on the rendered file; make lint after the librarian's run not taken — today it stops at this step, no entity-glossary yet

## History

- 2026-09-22 created · [[decision-case-306.5]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L62
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given and the order in make lint out (case 488.2) · [[decision-case-488.2]]
