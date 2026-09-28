---
type: estimate
kind: QA
status: pending
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

When:
Someone reads the tree for `vault/wiki/index.md`, and reads `vault/wiki/`, `.claude/`, `guppi/` and `CLAUDE.md` for a `§N` and for `index.md`, each hit by hand.

Then:
`vault/wiki/index.md` does not exist.
**＋** No live page of `vault/wiki/`, no harness file and no docstring of `guppi/` points at a `§N` or at `index.md` as a source.
**－** The archive and the ledgers under `vault/raw/` keep their pointers.

## Result

2026-09-23, test -e vault/wiki/index.md exit 1 (absent); rg '§ ?[0-9]|index\.md' over .claude, guppi, CLAUDE.md: no hit; over vault/wiki/{entities,estimates,rules,lessons,insights}: 33 hits, each read by hand — History lines, Results, negations, the sprint's own goal, and the Givens of this page and of estimate-sprint-migration-rule-class-files-dissolved, which state the old state and send no reader to the file; the hits in decisions/, log.md, sprint.md and brief.md counted by file and taken as records by category, not read line by line; outside the method, .gitignore:46 still names index.md §1

## History

- 2026-09-22 created · [[decision-case-310.3]]
- 2026-09-23 updated: the method names its reading — read by hand — and drops the moment of theme 4 (case 329) · [[decision-case-329]]
- 2026-09-23 status: pending → failed · raw/2026-09-23/0034/ledger.md#L63
- 2026-09-24 status: failed → passed · raw/2026-09-23/1859/ledger.md#L1
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given out, the one-time trigger of theme 4 replaced by the reading of the method (case 494.5) · [[decision-case-494.5]]
