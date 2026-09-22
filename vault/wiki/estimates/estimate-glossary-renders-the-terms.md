---
type: estimate
kind: QA
status: passed
target: "[[rule-glossary]]"
purpose: guppi glossary writes glossary.md from the Terms of entity-glossary, one group per parent MOC of where, and refuses a term with no page
method: pytest tests/test_glossary.py, plus one reading of the rendered glossary.md after the librarian's run
origin: raw/2026-09-22/0014/ledger.md#case-306.4
sprint: migration
created: 2026-09-22
tags: [harness, workflow, librarian, session]
---

## Criterion

Given:
`rule-sprint`: a `check` rule with `governs`; the script writes the file from a page, `--check` compares in memory, writes nothing, exit 1 on a difference; once it wrote the file it ticks its Spec lines (250.2).
**＋** `rule-governed-files-hook` refuses a hand edit of `governs`.
**＋** Case 240.1: a MOC is a thing whose parts the person named as built; a Leaf is not, and a Leaf carries `parent`. Case 240.2: the guard of an Entity is a separate Rule — the edge `applies_to` (305).
**＋** Case 299.1: a Case superseded in its own session leaves the Spec, the superseding Case is written whole.
**＋** `tests/test_glossary.py` fixes the behaviour on a temp vault.

When:
The librarian, step 6 of the frame: `uv run guppi glossary`.

Then:
`vault/wiki/glossary.md` is written: `# Glossary`, the line "Written by `guppi glossary` from the `## Terms` of `entity-glossary`; a term changes by an `update` of that page", then for each parent MOC of the pages in `where` a group `## [[<moc>]]` in the order of first appearance in the table (a page without a parent — a root MOC, or a placeholder not yet placed — under itself), in it `| term | meaning | where |` in the order of the table.
**＋** A `where` with no live page, a row not of three columns, a term twice: one line on stderr, exit 1, the file is not written.
**＋** The frame of the librarian has step 6: "Run `uv run guppi glossary`. It writes `vault/wiki/glossary.md` from the `## Terms` of `entity-glossary`. Every line on its stderr is a flag."
**－** `index.md` is not read; no row that is not derived from the table.

## Result

2026-09-22, uv run pytest tests/test_glossary.py, 8 passed: glossary.md written from the Terms of entity-glossary, one group per parent MOC of where in the order of first appearance, a page without a parent under itself, the rows in table order; a where with no live page, a row of two cells, a bare where, a term twice, no page and no Terms section each refused on stderr with nothing written; the cli knows the command; the live reading of the rendered glossary.md after the librarian's run not taken

## History

- 2026-09-22 created · [[decision-case-306.4]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L61
