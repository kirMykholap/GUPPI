---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-migration]]"
purpose: No Rule-class file at the close of Slice 3f — the schemas rendered from rule pages, the glossary from entity-glossary, index.md gone, the file route out of the scripts
method: "one reading by hand: ls vault/wiki/*/schema.md empty and vault/wiki/index.md absent; grep -rniE --include='*.py' 'rule.class|applied by hand|prose_names' guppi/ tests/ empty; uv run guppi render --check and uv run guppi glossary --check exit 0"
origin: raw/2026-09-21/1853/ledger.md#case-301
sprint: migration
created: 2026-09-21
tags: [sprint, workflow, harness]
---

## Criterion

Given:
A Rule-class file — `index.md`, `glossary.md`, `<category>/schema.md` and `schema.yaml` — changes only by a ratified `update` with `file`, by hand; its route in the scripts is `RULE_CLASS` and `category: file` in `materialize.py`, "applied by hand" in `generate.py`, `rule_class_path` and `check_governed` in `prespec.py`, `prose_names` in `lint.py`.
**＋** The Render of a rule with `render_mode: full` becomes the file of `governs` whole; `render --check` and the governed-files hook keep them equal (273).
**＋** `guppi sprint` writes `sprint.md` from the sprint page under `rule-sprint`, which carries `governs`, `implementation_ref` and `--check` under `make lint` (209, 227, 229).
**＋** A page has one `parent`; the tree of rules is built by mechanism; the schema has no edge Rule → Entity.
**＋** Lint reads `<category>/schema.yaml`; `materialize.schema_fields` and `generate` read it too.

When:
The reading at the close of Slice 3f: `ls` of the schemas and `index.md`, a grep of the `file` route and of the retired term over `guppi/` and `tests/`, `uv run guppi render --check`, `uv run guppi glossary --check`; `make lint` is the reading of `estimate-sprint-migration-lint-clean`.

Then:
No Rule-class file: every `<category>/schema.yaml` is the Render of the Leaf `rule-<category>-schema` (`enforcement: render`, `governs` that yaml), with the description of its fields as yaml data; no `schema.md`; `glossary.md` is written by `guppi glossary` from the `## Terms` of `entity-glossary`, a table "term — meaning — `[[page]]`" grouped by the parent MOC, under `rule-glossary` with `governs`, `implementation_ref` and `--check`; no `index.md`, every `§N` pointer in the vault replaced by a slug.
**＋** The scripts hold no `file` route: no `RULE_CLASS`, no `category: file`, no "applied by hand", no `rule_class_path`, no `prose_names`; the vault changes only by the scripts, from decisions.
**＋** Every rule has its parent by the criterion of the audit: under a category's MOC a rule that holds for that category alone, the MOC made at two or more such rules, else the schemas under `rule-page-schemas`; `applies_to` on a Rule and `rules` on an Entity carry the edge Rule → Entity, `rule-sprint` → `entity-sprint` the first.
**＋** "Rule-class" is a retired term in the Case schema and in the glossary, and no docstring of `guppi/` and no test name of `tests/` carries it (case 365).
**－** `case-schema.md` and `CLAUDE.md` are not brought into the graph by the Slice: they are Renders already and change by an `update` of `rule-case-protocol` or `rule-claude-md`, as theme 6 does.
**－** No template engine for the renders is built: Backlog.

## History

- 2026-09-22 created · [[decision-case-301]]
- 2026-09-22 updated: the glossary is rendered from entity-glossary, not from a terms field (case 306.7) · [[decision-case-306.7]]
- 2026-09-22 updated: the pointer at §1 of index.md is gone with the file (case 321) · [[decision-case-321]]
- 2026-09-23 updated: the reading of the Slice without make lint, the grep widened to the retired term over guppi/ and tests/ (case 367) · [[decision-case-367]]
