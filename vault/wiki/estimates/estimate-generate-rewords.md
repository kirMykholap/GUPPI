---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
purpose: An update item with reword replaces its pairs as whole words, or a pair whose old ends with / as the start of a path in the link fields too, on every live page but History and Result, one History line each, and fails on a pair with no hit or a new the owner does not carry
method: uv run --project .guppi pytest .guppi/tests/test_generate.py on a temp vault whose pages hold paths in their text and their link fields
checked: 2026-10-16
origin: raw/2026-09-20/1308/ledger.md#case-274.1
sprint: migration
created: 2026-09-20
tags: [harness, workflow, ledger]
---

## Criterion

When:
`guppi generate` applies an `update` entry whose item carries `reword`, a list of `{old, new}` pairs.

Then:
A pair whose `old` does not end with `/` is replaced as a whole word, with no letter, digit, `_` or `-` right before or after it.
**＋** A pair whose `old` ends with `/`, such as `docs/`, is replaced as the start of a path: where no letter, digit, `_`, `-`, `.` or `/` stands right before it, whatever follows it, so the pair `docs/` → `site/docs/` turns `docs/intro.md` into `site/docs/intro.md` and leaves `site/docs/` and `cart/docs/` as they are.
**＋** The replace runs on every live page of the folders `rules`, `entities` and `estimates` of `vault/wiki/`, in every section but History and Result and in the fields `purpose` and `method`, and a pair whose `old` ends with `/` runs in the fields `implementation_ref`, `governs` and `code_ref` too.
**＋** Each page touched gets one History line `reworded: old → new · [[decision-case-N]]`, and stdout has one line per page with the count.
**＋** The other keys of the item — `set`, `replace`, `sections`, `change` — apply to the page itself as before; an item that carries `reword` alone is content and applies.
**＋** `uv run --project .guppi guppi prespec --check` previews each pair by the same matching as `guppi generate`.
**－** A pair with no hit on any live page fails the entry with the reason, and so does a pair whose `new` is absent from the text of the page of the item: its `purpose`, `governs`, `implementation_ref`, Purpose and Render, compared without regard to case. Nothing is applied.
**－** The Decision pages, the lessons and the Insights, `vault/archive/`, `vault/raw/`, `log.md`, `brief.md` and `sprint.md` are not touched; the status of no Estimate changes.

## Result

2026-10-16, Retro of session 0104, uv run --project .guppi pytest .guppi/tests/test_generate.py: 131 passed; the matching of a reword pair whose old ends with / is unchanged in .guppi/guppi/generate.py, and the example docs/ → site/docs/ of Case 840.1 is that matching on another folder; the pages change at the librarian's run

## History

- 2026-09-20 created · [[decision-case-274.1]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L3
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given and the Rule-class files out (case 489.4) · [[decision-case-489.4]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/0112/ledger.md#L1
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 updated: the Criterion replaced whole — a pair whose old ends with / matches the start of a path, in the link fields too · [[decision-case-819.2]]
- 2026-10-15 status: pending → passed · raw/2026-10-15/1959/ledger.md#L2
- 2026-10-16 updated: the Criterion replaced whole — the example of a path pair is docs/ → site/docs/; the method keeps the test alone · [[decision-case-840.1]]
- 2026-10-16 status: pending → passed · raw/2026-10-16/0104/ledger.md#L15
