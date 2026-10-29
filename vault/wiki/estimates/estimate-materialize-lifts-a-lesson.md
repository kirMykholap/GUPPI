---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: A lesson line carries its source into the entry
method: pytest in .guppi/tests/test_materialize.py, the tests of the lesson entry
checked: 2026-10-29
origin: raw/2026-09-16/1034/ledger.md#case-189
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger]
---

## Criterion

When:
`guppi materialize` reads a `- lesson[...]` ledger line whose braces carry `{source:...}`.

Then:
The entry carries `source` in its `fields`, and `generate` writes it into the page's frontmatter.
**＋** A `knowledge` lesson whose line carries no `source` is still marked `incomplete: [source]`; an `error` lesson never is.
**－** The applied entries of the yamls of earlier sessions are not rewritten: each records what the parser did in its own session.

## Result

2026-10-29, Retro of session 0327: pytest .guppi/tests/test_materialize.py -k "lesson or source": 13 passed

## History

- 2026-09-16 created · [[decision-case-189]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1651/ledger.md#L30
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-29 updated: the Criterion replaced whole — the yamls of earlier sessions, not a past day of GUPPI · [[decision-case-901.4]]
- 2026-10-29 status: pending → passed · raw/2026-10-29/0327/ledger.md#L40
