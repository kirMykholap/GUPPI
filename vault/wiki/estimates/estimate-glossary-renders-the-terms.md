---
type: estimate
kind: QA
status: passed
target: "[[rule-glossary]]"
purpose: guppi glossary writes glossary.md from the Terms of entity-glossary, one group per parent MOC of where, and refuses a term with no page
method: pytest .guppi/tests/test_glossary.py, plus one reading of the rendered glossary.md after the librarian's run
checked: 2026-09-29
origin: raw/2026-09-22/0014/ledger.md#case-306.4
sprint: migration
created: 2026-09-22
tags: [harness, workflow, librarian, session]
---

## Criterion

When:
`uv run --project .guppi guppi glossary` runs without a flag, from step 6 of the librarian's frame in `.claude/agents/librarian-guppi.md` or by hand, and reads the `## Terms` table of `entity-glossary`.

Then:
`vault/wiki/glossary.md` is written and the run exits 0. The file holds `# Glossary`, then the line "Written by `guppi glossary` from the `## Terms` of `entity-glossary`; a term changes by an `update` of that page", then one group `## [[<moc>]]` for each parent MOC of the pages in `where`, in the order of first appearance in the table. Each group holds the table `| term | meaning | where |` with its rows in the order of the table.
**＋** A page in `where` that has no `parent`, such as a root MOC or a placeholder not yet placed, is its own group.
**＋** A `where` with no live page, a `where` that is no `[[slug]]`, a row that is not three cells, a term twice, no `## Terms` section, or no single live `entity-glossary` gives one line on stderr and exit 1, and the file is not written.
**＋** The librarian's frame takes each line on stderr of the run as a flag.
**－** The file holds no line that the table does not give, apart from the heading and the source line.

## Result

2026-09-29, tests/test_glossary.py 8 passed; glossary.md holds the heading, the source line, 10 groups and the 49 rows of Terms in order; the run of ff62585 left it unchanged, exit 0

## History

- 2026-09-22 created · [[decision-case-306.4]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L61
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given and the index.md line out (case 488.1) · [[decision-case-488.1]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L58
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
