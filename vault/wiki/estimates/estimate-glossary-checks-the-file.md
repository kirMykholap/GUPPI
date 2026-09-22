---
type: estimate
kind: QA
status: passed
target: "[[rule-glossary]]"
purpose: glossary --check names glossary.md when it differs from the render of entity-glossary, exit 1, and writes nothing
method: pytest tests/test_glossary.py, plus make lint after the librarian's run — no glossary line
origin: raw/2026-09-22/0014/ledger.md#case-306.5
sprint: migration
created: 2026-09-22
tags: [harness, workflow, librarian, session]
---

## Criterion

Given:
`rule-sprint`: a `check` rule with `governs`; the script writes the file from a page, `--check` compares in memory, writes nothing, exit 1 on a difference; once it wrote the file it ticks its Spec lines (250.2).
**＋** `rule-governed-files-hook` refuses a hand edit of `governs`.
**＋** Case 240.1: a MOC is a thing whose parts the person named as built; a Leaf is not, and a Leaf carries `parent`. Case 240.2: the guard of an Entity is a separate Rule — the edge `applies_to` (305).
**＋** Case 299.1: a Case superseded in its own session leaves the Spec, the superseding Case is written whole.
**＋** `tests/test_glossary.py` fixes the behaviour on a temp vault.

When:
`uv run guppi glossary --check`, in `make lint` after `sprint --check`.

Then:
The render in memory; a difference is one line `glossary: vault/wiki/glossary.md differs from entity-glossary`, exit 1, nothing written; equal — exit 0 and no output.
**－** `--check` ticks nothing.

## Result

2026-09-22, uv run pytest tests/test_glossary.py, 8 passed: --check names vault/wiki/glossary.md when it differs from entity-glossary, exit 1, writes nothing, and is silent on the rendered file; make lint after the librarian's run not taken — today it stops at this step, no entity-glossary yet

## History

- 2026-09-22 created · [[decision-case-306.5]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L62
