---
type: estimate
kind: QA
status: failed
target: "[[entity-sprint-migration]]"
purpose: index.md is gone and no live page, harness file or script docstring points at a §N of it or at the file as a source
method: test -e vault/wiki/index.md false; rg over vault/wiki, .claude, guppi and CLAUDE.md for §N and index.md, every hit read by hand — only a live pointer, a page that sends a reader to the file, is a failure; the archive and raw/ are not read
checked: 2026-09-23
origin: raw/2026-09-22/1121/ledger.md#case-310.3
sprint: migration
created: 2026-09-22
tags: [sprint, workflow, harness]
---

## Criterion

Given:
`index.md` is the map of the vault by §; pages, rules and scripts point at `§N` (case 301, theme 4).
**＋** Each § is either covered by a rule page or gets one.

When:
The last Case of theme 4 is applied by the librarian.

Then:
`vault/wiki/index.md` does not exist.
**＋** No live page of `wiki/`, no harness file and no docstring of `guppi/` points at a `§N` or at `index.md` as a source.
**－** The archive and the ledgers under `raw/` keep their pointers.

## Result

2026-09-23, test -e vault/wiki/index.md exit 1 (absent); rg '§ ?[0-9]|index\.md' over vault/wiki, .claude, guppi, CLAUDE.md, every hit read by hand: two live pointers — the docstring of guppi/materialize.py:11 "its route computed from `index.md` §5", and the Given of estimate-case-protocol-case-form.md:18 "`index.md`, `estimates/schema.md` and `schema.yaml` are the Renders of their rule pages"; every other hit is a History line, a Result, a Decision page's record, a negation or the sprint's own goal

## History

- 2026-09-22 created · [[decision-case-310.3]]
- 2026-09-23 updated: the method names its reading — read by hand — and drops the moment of theme 4 (case 329) · [[decision-case-329]]
- 2026-09-23 status: pending → failed · raw/2026-09-23/0034/ledger.md#L63
