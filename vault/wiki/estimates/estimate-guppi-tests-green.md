---
type: estimate
kind: QA
status: passed
target: "[[entity-guppi]]"
purpose: make test is green on the branch — the whole suite of the harness
method: make test, 0 failed; read after each Work Mode
origin: raw/2026-09-22/0014/ledger.md#case-306.2
sprint: migration
created: 2026-09-22
tags: [harness, tests]
---

## Criterion

Given:
`rule-sprint`: a `check` rule with `governs`; the script writes the file from a page, `--check` compares in memory, writes nothing, exit 1 on a difference; once it wrote the file it ticks its Spec lines (250.2).
**＋** `rule-governed-files-hook` refuses a hand edit of `governs`.
**＋** Case 240.1: a MOC is a thing whose parts the person named as built; a Leaf is not, and a Leaf carries `parent`. Case 240.2: the guard of an Entity is a separate Rule — the edge `applies_to` (305).
**＋** Case 299.1: a Case superseded in its own session leaves the Spec, the superseding Case is written whole.
**＋** `tests/test_glossary.py` fixes the behaviour on a temp vault.

When:
The librarian applies the entries; a reader opens the graph.

Then:
`entity-guppi` is a MOC without a parent, `children: [entity-sprint, entity-glossary]`, `code_ref: [guppi/, .claude/]`; `entity-sprint` carries `parent: entity-guppi`; `rule-harness` carries `applies_to: [entity-guppi]`, and the cascade writes `rules: [rule-harness]` on `entity-guppi`.
**＋** `estimate-guppi-tests-green`: `make test` — 0 failed on the branch.
**－** The four phase MOCs carry no `applies_to` — rules of the process.

## Result

2026-09-22, make test after Work Mode: 529 passed, 2 skipped (the conditional cases of insights and decisions in tests/test_schemas.py), 0 failed

## History

- 2026-09-22 created · [[decision-case-306.2]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L64
