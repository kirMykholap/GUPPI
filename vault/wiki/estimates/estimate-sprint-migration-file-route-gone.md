---
type: estimate
kind: QA
status: passed
target: "[[entity-sprint-migration]]"
purpose: The file route is out of the scripts — no RULE_CLASS, rule_class, applied by hand or prose_names in guppi/; an update item with file is a pre-spec finding; a slug without a prefix lands category unknown; tests green and no lint finding on the schema.yaml of a category folder
method: rg 'RULE_CLASS|rule_class|applied by hand|prose_names' guppi/ empty; uv run pytest tests/test_generate.py -k unknown — the update applied in any folder, the create and the page-less defer failed, the delete outside the vault; make test; make lint — no line on a <category>/schema
checked: 2026-09-28
origin: raw/2026-09-22/1121/ledger.md#case-320
sprint: migration
created: 2026-09-22
tags: [sprint, workflow, harness]
---

## Criterion

When:
`generate` applies a `materialize.yaml` that holds an entry lifted from a ledger line whose slug has no category prefix.
**＋** `make test` and `make lint` run on the tree.

Then:
No file under `guppi/` holds `RULE_CLASS`, `rule_class`, `applied by hand` or `prose_names`.
**＋** An `update` item that carries `file` is a `pre-spec` finding: `check_governed` refuses any such item, not only one on a governed path.
**＋** The entry of a ledger line whose slug has no category prefix lands `category: unknown`.
**＋** `generate` fails a `create` of that entry, and a `defer` of it with no page, with `category 'unknown' is not a vault folder`.
**＋** `generate` applies an `update` of that entry to the page of that slug in any folder, and ticks its line.
**＋** `generate` applies a `delete` of that entry with the stdout line `outside the vault, nothing to archive`, and ticks its line.
**＋** `make test` is green, and `make lint` prints no finding on a `<category>/schema`, the `schema.yaml` of a category folder.
**－** `generate` prints "applied by hand" for no entry.
**－** A `make lint` finding on a page, a missing field or section of a Decision page or a rule page included, is outside this promise: `estimate-sprint-migration-lint-clean` holds it.

## Result

2026-09-28, rg over guppi/ for RULE_CLASS, rule_class, applied by hand, prose_names: none in tracked files (grep finds them only in two stale .pyc files under guppi/__pycache__/, which rg skips by .gitignore); uv run pytest tests/test_generate.py -k unknown: 4 passed; make test 876 passed, 2 skipped; make lint prints no line on a <category>/schema

## History

- 2026-09-22 created · [[decision-case-320]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L95
- 2026-09-27 updated: the Criterion replaced whole — an update of category unknown applies, a delete applies outside the vault, a create and a page-less defer fail; Given out; the method without theme 5 (case 464) · [[decision-case-464]]
- 2026-09-28 updated: the Criterion replaced whole — the lint line names the findings on a <category>/schema, and a finding on a page is left to estimate-sprint-migration-lint-clean; purpose and method reworded to match (case 478.1) · [[decision-case-478.1]]
- 2026-09-28 status: pending → passed · raw/2026-09-28/2000/ledger.md#L23
