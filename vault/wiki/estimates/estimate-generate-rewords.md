---
type: estimate
kind: QA
status: pending
target: "[[rule-page-generation]]"
purpose: An update item with reword replaces its pairs as whole words on every live page but History and Result, one History line each, and fails on a pair with no hit or a new the owner does not carry
method: pytest tests/test_generate.py on a temp vault with three pages and an archive; the live reading the librarian's run that applies the first reword
origin: raw/2026-09-20/1308/ledger.md#case-274.1
sprint: migration
created: 2026-09-20
tags: [harness, workflow, ledger]
---

## Criterion

Given:
An `update` item of a Rule page carries `reword` — a list of `{old, new}` pairs; the page is the owner: the `new` of every pair stands in its Purpose, Render, `governs` or `implementation_ref`, compared without regard to case.
**＋** A whole word is the boundary of `rename` 258.1: `(?<![\w-])old(?![\w-])`; the slug of a page is renamed by `rename`, not by `reword`.
**＋** `tests/test_generate.py` fixes the behaviour on a temp vault with three pages and an archive.

When:
`guppi generate` applies an `update` entry with `reword`.

Then:
Every pair is replaced as a whole word on every live page of `wiki/rules/`, `wiki/entities/` and `wiki/estimates/`, in every section but History and Result and in the fields `purpose` and `method`; one History line per page touched — `reworded: old → new · [[decision-case-N]]`; stdout one line per page with the count.
**＋** The other keys of the item — `set`, `replace`, `sections`, `change` — apply to the page itself as before; an item that carries `reword` alone is content and applies.
**－** A pair with no hit on any live page, or with a `new` absent from the owner's text, fails the entry with the reason; nothing is applied.
**－** `wiki/decisions/` (the journal, without History), `wiki/lessons/` and `wiki/insights/` (records of the past), the archive, `raw/`, the Rule-class files, `log.md`, `brief.md` and `sprint.md` are not touched; the status of no Estimate changes (case 277).

## History

- 2026-09-20 created · [[decision-case-274.1]]
