---
type: rule
kind: Leaf
purpose: Prevents glossary.md from drifting from the terms of entity-glossary, and a term from pointing at no page
status: draft
enforcement: check
implementation_ref: [guppi/glossary.py, tests/test_glossary.py]
governs: vault/wiki/glossary.md
parent: "[[rule-documentation]]"
estimates: ["[[estimate-glossary-renders-the-terms]]", "[[estimate-glossary-checks-the-file]]", "[[estimate-glossary-ticks-the-spec]]"]
applies_to: ["[[entity-glossary]]"]
origin: raw/2026-09-22/0014/ledger.md#case-306.4
sprint: migration
created: 2026-09-22
tags: [harness, workflow, librarian, session]
---

## Purpose

Prevents `vault/wiki/glossary.md` from drifting from the terms of `entity-glossary`, and a term from pointing at no page. The glossary is a page — `entity-glossary`, a Leaf under `entity-guppi`, whose `## Terms` is a flat table `| term | meaning | where |`; `glossary.md` is not a document: `guppi glossary` writes it from that table, one group per parent MOC of the pages in `where` — a page without a parent, a root MOC or a placeholder not yet placed, under itself — in the order of first appearance, the rows in the order of the table; a `where` with no live page, a row of another shape or a term twice stops the write with a line on stderr. `governs` names the file, so the governed-files hook refuses a hand edit; a term changes by an `update` of `entity-glossary`. The librarian runs the script after `sprint`, before the brief. `guppi glossary --check` renders in memory and names the file when it differs, exit 1, writing nothing; `make lint` runs it after `sprint --check`. Once the plain `guppi glossary` wrote the file and exits 0, it ticks every unticked task line of an applied Spec that opens with a code span holding `guppi glossary` — the Spec's bookkeeping, no tick in the glossary itself (case 306).

## History

- 2026-09-22 created · [[decision-case-306.4]]
- 2026-09-22 status: draft → built · cascade
- 2026-09-22 updated: the edge to entity-glossary, dropped by materialize as unknown against the old schema in session 0014 (case 308.1) · [[decision-case-308.1]]
- 2026-09-29 status: built → draft · cascade
