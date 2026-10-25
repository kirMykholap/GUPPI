---
type: estimate
kind: QA
status: passed
target: "[[rule-glossary]]"
purpose: glossary --check names glossary.md when it differs from the render of entity-glossary, exit 1, and writes nothing
method: "uv run --project .guppi pytest .guppi/tests/test_glossary.py; uv run --project .guppi guppi glossary --check in the working tree at Retro: exit 0 and no output"
checked: 2026-10-26
origin: raw/2026-09-22/0014/ledger.md#case-306.5
sprint: migration
created: 2026-09-22
tags: [harness, workflow, librarian, session]
---

## Criterion

When:
`uv run --project .guppi guppi glossary --check` runs, as `uv run --project .guppi guppi check` runs it, and renders the file from `entity-glossary` in memory.

Then:
When `vault/wiki/glossary.md` differs from the render or is missing, stdout holds one line `glossary: <file> differs from entity-glossary`, the file named by its path from the project root, and the check exits 1.
**＋** When the file equals the render, the check exits 0 with no output.
**－** The check writes no file and ticks no line of a Spec.

## Result

2026-10-26, Retro: `uv run --project .guppi pytest .guppi/tests/test_glossary.py` 8 passed; `uv run --project .guppi guppi glossary --check` in the working tree exit 0, no output

## History

- 2026-09-22 created · [[decision-case-306.5]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L62
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given and the order in make lint out (case 488.2) · [[decision-case-488.2]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L57
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `make lint` → `uv run --project .guppi guppi check` · [[decision-case-820.7]]
- 2026-10-26 updated: the Criterion replaced whole — the check runs as guppi check runs it, not as a target of the Makefile; the method reads at Retro · [[decision-case-882.1]]
- 2026-10-26 status: pending → passed · raw/2026-10-17/2307/ledger.md#L50
