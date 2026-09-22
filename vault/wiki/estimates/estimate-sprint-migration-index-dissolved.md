---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-migration]]"
purpose: index.md is gone and no live page, harness file or script docstring points at a §N of it or at the file as a source
method: at the close of theme 4 — test -e vault/wiki/index.md false; rg over vault/wiki, .claude, guppi and CLAUDE.md for §N and index.md, every hit read by eye, only a live pointer — a page that sends a reader to the file — a failure; the archive and raw/ are not read
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

## History

- 2026-09-22 created · [[decision-case-310.3]]
