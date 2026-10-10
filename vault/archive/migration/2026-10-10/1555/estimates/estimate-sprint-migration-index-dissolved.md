---
type: estimate
kind: QA
status: archived
target: "[[entity-sprint-migration]]"
purpose: index.md is gone and no live page, harness file or script docstring points at a §N of it or at the file as a source
method: test -e vault/wiki/index.md false; rg over vault/wiki, .claude, guppi and CLAUDE.md for §N and index.md, every hit read by hand — only a live pointer, a page that sends a reader to the file, is a failure; the archive and raw/ are not read
checked: 2026-09-29
origin: raw/2026-09-22/1121/ledger.md#case-310.3
sprint: migration
created: 2026-09-22
tags: [sprint, workflow, harness]
---

## Criterion

When:
Someone reads the tree for `vault/wiki/index.md`, and reads `vault/wiki/`, `.claude/`, `guppi/` and `CLAUDE.md` for a `§N` and for `index.md`, each hit by hand.

Then:
`vault/wiki/index.md` does not exist.
**＋** No live page of `vault/wiki/`, no harness file and no docstring of `guppi/` points at a `§N` or at `index.md` as a source.
**－** The archive and the ledgers under `vault/raw/` keep their pointers.

## Result

2026-09-29, test -e vault/wiki/index.md exit 1 (absent); grep for §N and index.md over vault/wiki, .claude, guppi and CLAUDE.md: no hit in .claude, guppi or CLAUDE.md; the hits in vault/wiki are History and log.md lines, Decision pages, Results, the lesson trigger of lesson-agents-at-import-not-expanded, the Estimates that name the file as gone, and entity-sprint-migration saying index.md is gone; none points at the file or a §N as a source

## History

- 2026-09-22 created · [[decision-case-310.3]]
- 2026-09-23 updated: the method names its reading — read by hand — and drops the moment of theme 4 (case 329) · [[decision-case-329]]
- 2026-09-23 status: pending → failed · raw/2026-09-23/0034/ledger.md#L63
- 2026-09-24 status: failed → passed · raw/2026-09-23/1859/ledger.md#L1
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given out, the one-time trigger of theme 4 replaced by the reading of the method (case 494.5) · [[decision-case-494.5]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1432/ledger.md#L28
- 2026-10-10 status: passed → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
