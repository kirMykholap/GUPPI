---
type: estimate
kind: QA
status: pending
target: "[[rule-page-generation]]"
purpose: An update item with reword replaces its pairs as whole words on every live page but History and Result, one History line each, and fails on a pair with no hit or a new the owner does not carry
method: pytest tests/test_generate.py on a temp vault with three pages and an archive; the live reading a librarian's run that applies a reword
checked: 2026-09-22
origin: raw/2026-09-20/1308/ledger.md#case-274.1
sprint: migration
created: 2026-09-20
tags: [harness, workflow, ledger]
---

## Criterion

When:
`guppi generate` applies an `update` entry whose item carries `reword`, a list of `{old, new}` pairs.

Then:
Every pair is replaced as a whole word, with no letter, digit, `_` or `-` right before or after it. The replace runs on every live page of the folders `rules`, `entities` and `estimates` of `vault/wiki/`, in every section but History and Result and in the fields `purpose` and `method`. Each page touched gets one History line `reworded: old → new · [[decision-case-N]]`, and stdout has one line per page with the count.
**＋** The other keys of the item — `set`, `replace`, `sections`, `change` — apply to the page itself as before; an item that carries `reword` alone is content and applies.
**－** A pair with no hit on any live page fails the entry with the reason, and so does a pair whose `new` is absent from the text of the page of the item: its `purpose`, `governs`, `implementation_ref`, Purpose and Render, compared without regard to case. Nothing is applied.
**－** The Decision pages, the lessons and the Insights, `vault/archive/`, `vault/raw/`, `log.md`, `brief.md` and `sprint.md` are not touched; the status of no Estimate changes.

## Result

2026-09-22, uv run pytest tests/test_generate.py -k reword, 4 passed: a reword pair is replaced as a whole word on the live rules, entities and estimates with one History line per page and one stdout line per page; decisions, lessons, insights and the archive untouched; reword alone is content and applies; a pair with no hit, a new absent from the owner or a mapping fails the entry with the reason; the live leg, the librarian's run that applies the first reword, not taken

## History

- 2026-09-20 created · [[decision-case-274.1]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L3
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given and the Rule-class files out (case 489.4) · [[decision-case-489.4]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
