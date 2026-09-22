---
type: estimate
kind: QA
status: passed
target: "[[entity-sprint-migration]]"
purpose: The file route is out of the scripts — no RULE_CLASS, rule_class, applied by hand or prose_names in guppi/; an update item with file is a pre-spec finding; a slug without a prefix lands category unknown; tests green and lint clean on the schemas
method: at the close of theme 5 — rg 'RULE_CLASS|rule_class|applied by hand|prose_names' guppi/ empty; make test; make lint
origin: raw/2026-09-22/1121/ledger.md#case-320
sprint: migration
created: 2026-09-22
tags: [sprint, workflow, harness]
---

## Criterion

Given:
No Rule-class file is left: the schemas are Renders of rules (304), the glossary (306), `index.md` is deleted (318), `case-schema.md` and `CLAUDE.md` are Renders (273, 59.8).
**＋** `category_of` returns `None` for a slug without a prefix, and the entry lands `category: unknown`.
**＋** A `replace` inside a Criterion sets the Estimate `pending` (case 296).
**＋** `tests/test_materialize.py`, `tests/test_generate.py` and `tests/test_prespec.py` fix the behaviour.

When:
`make test` and `make lint` run after the route is removed.

Then:
`rg 'RULE_CLASS|rule_class|applied by hand|prose_names' guppi/` is empty.
**＋** An `update` item carrying `file` is a `pre-spec` finding — the file route is gone; `check_governed` refuses any such item, not only one on a governed path.
**＋** A ledger line whose slug has no category prefix lands `category: unknown`, and `generate` reports an error instead of "applied by hand".
**＋** `make test` is green and `make lint` has no finding on a schema.
**－** `rule-morph` is untouched: the category set is its business, not the file route.

## Result

2026-09-22, grep -rn "RULE_CLASS|rule_class|applied by hand|prose_names" guppi/: empty; make test 548 passed, 2 skipped; make lint — no finding on a <category>/schema

## History

- 2026-09-22 created · [[decision-case-320]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L95
