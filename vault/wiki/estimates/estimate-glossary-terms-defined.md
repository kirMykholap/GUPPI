---
type: estimate
kind: QA
status: passed
target: "[[entity-glossary]]"
purpose: Every term names in where a live page that defines it, and no term stands twice
method: one reading of the table by hand after the librarian's run, plus make lint — no ref finding on entity-glossary
checked: 2026-09-22
origin: raw/2026-09-22/0014/ledger.md#case-306.3
sprint: migration
created: 2026-09-22
tags: [session, harness]
---

## Criterion

Given:
`rule-sprint`: a `check` rule with `governs`; the script writes the file from a page, `--check` compares in memory, writes nothing, exit 1 on a difference; once it wrote the file it ticks its Spec lines (250.2).
**＋** `rule-governed-files-hook` refuses a hand edit of `governs`.
**＋** Case 240.1: a MOC is a thing whose parts the person named as built; a Leaf is not, and a Leaf carries `parent`. Case 240.2: the guard of an Entity is a separate Rule — the edge `applies_to` (305).
**＋** Case 299.1: a Case superseded in its own session leaves the Spec, the superseding Case is written whole.
**＋** `tests/test_glossary.py` fixes the behaviour on a temp vault.

When:
The librarian creates the page; a person or an agent reads a term.

Then:
`entity-glossary` is a Leaf under `entity-guppi`; its `## Terms` is a table of 49 rows: the rows of today's `glossary.md` with their meaning verbatim and `where` a `[[slug]]`; the rows Sprint / `brief.md` and Harness / Hook split in two; the row Rule-class files gone with the term (case 321); the rows on ``here` on the page whose meaning they name.
**＋** A term enters, changes or leaves by an `update` of this page in a Case — a `replace` pair or the section whole; the `change` line is its History; a retired term is a History line, not a row.
**＋** `estimate-glossary-terms-defined`: every `where` is a live page that defines the term; no term stands twice.
**－** C4 model, Delegate and the four Retired terms are not rows; one History line of the page names them.

## Result

2026-09-22, by hand: the ## Terms of entity-glossary holds 49 rows under one header; guppi lint — no ref finding on entity-glossary

## History

- 2026-09-22 created · [[decision-case-306.3]]
- 2026-09-22 updated: the rows on §N are gone with index.md (case 318) · [[decision-case-318]]
- 2026-09-22 updated: the Rule-class row is retired, not rewritten (case 321) · [[decision-case-321]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L84
