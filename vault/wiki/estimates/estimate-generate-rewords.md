---
type: estimate
kind: QA
status: pending
target: "[[rule-page-generation]]"
purpose: An update item with reword replaces its pairs as whole words, or a pair whose old ends with / as the start of a path in the link fields too, on every live page but History and Result, one History line each, and fails on a pair with no hit or a new the owner does not carry
method: "uv run --project .guppi pytest .guppi/tests/test_generate.py on a temp vault whose pages hold paths in their text and their link fields; by hand, after the librarian's run that applies the reword of rule-guppi-package: the pages it touched and its stdout read against the Criterion"
checked: 2026-10-04
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
**＋** A pair whose `old` ends with `/`, such as `tests/`, is replaced as the start of a path: where no letter, digit, `_`, `-`, `.` or `/` stands right before it, whatever follows it, so the pair `tests/` → `.guppi/tests/` turns `tests/test_ship.py` into `.guppi/tests/test_ship.py` and leaves `.guppi/tests/` and `cart/tests/` as they are.
**＋** The replace runs on every live page of the folders `rules`, `entities` and `estimates` of `vault/wiki/`, in every section but History and Result and in the fields `purpose` and `method`, and a pair whose `old` ends with `/` runs in the fields `implementation_ref`, `governs` and `code_ref` too.
**＋** Each page touched gets one History line `reworded: old → new · [[decision-case-N]]`, and stdout has one line per page with the count.
**＋** The other keys of the item — `set`, `replace`, `sections`, `change` — apply to the page itself as before; an item that carries `reword` alone is content and applies.
**＋** `uv run --project .guppi guppi prespec --check` previews each pair by the same matching as `guppi generate`.
**－** A pair with no hit on any live page fails the entry with the reason, and so does a pair whose `new` is absent from the text of the page of the item: its `purpose`, `governs`, `implementation_ref`, Purpose and Render, compared without regard to case. Nothing is applied.
**－** The Decision pages, the lessons and the Insights, `vault/archive/`, `vault/raw/`, `log.md`, `brief.md` and `sprint.md` are not touched; the status of no Estimate changes.

## Result

2026-10-04, at the /hi of session 0112: `uv run pytest -q tests/test_generate.py -k reword` 4 passed; live, the librarian's run of session 0004 (transcript a17e0a5f, agent ad4261a2ebbd0c947): yaml line 7, an `update` of entity-reading-probe carrying `change` and `reword` [quillwort → bramblewort]; `guppi generate` printed `generate: reword `quillwort` → `bramblewort`: entities/entity-reading-probe (1)`; the page, archived at vault/archive/migration/2026-10-04/0004/entities/entity-reading-probe.md, holds bramblewort in its body and the History lines `reworded: `quillwort` → `bramblewort` · [[decision-case-619.1]]` and the `updated:` line of its `change`, before `deleted · [[decision-case-619.2]]`; a count of quillwort over vault/wiki/ finds it in brief.md (2) and log.md (2) only, neither touched by the reword; no Estimate status line of log.md cites Case 619; not exercised live: a pair with no hit, a `new` absent from the page of the item, a hit on a Decision page, a lesson, an Insight or the archive — the tests hold them

## History

- 2026-09-20 created · [[decision-case-274.1]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L3
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given and the Rule-class files out (case 489.4) · [[decision-case-489.4]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/0112/ledger.md#L1
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 updated: the Criterion replaced whole — a pair whose old ends with / matches the start of a path, in the link fields too · [[decision-case-819.2]]
