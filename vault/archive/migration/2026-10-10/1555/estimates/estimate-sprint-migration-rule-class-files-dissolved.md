---
type: estimate
kind: QA
status: archived
target: "[[entity-sprint-migration]]"
purpose: No Rule-class file at the close of Slice 3f — the schemas rendered from rule pages, the glossary from entity-glossary, index.md gone, the file route out of the scripts
method: "one reading by hand: ls vault/wiki/*/schema.md empty and vault/wiki/index.md absent; grep -rniE --include='*.py' 'rule.class|applied by hand|prose_names' guppi/ tests/ empty; uv run guppi render --check and uv run guppi glossary --check exit 0"
checked: 2026-09-29
origin: raw/2026-09-21/1853/ledger.md#case-301
sprint: migration
created: 2026-09-21
tags: [sprint, workflow, harness]
---

## Criterion

When:
The reading at the close of Slice 3f: `ls` of the schemas and `index.md`, a grep of the `file` route and of the retired term over `guppi/` and `tests/`, `uv run guppi render --check` and `uv run guppi glossary --check`.

Then:
No Rule-class file: every `vault/wiki/<category>/schema.yaml` is the Render of the Leaf `rule-<category>-schema` (`enforcement: render`, `governs` that yaml), with the description of its fields as yaml data; no `schema.md`; `glossary.md` is written by `guppi glossary` from the `## Terms` of `entity-glossary`, a table "term — meaning — page" grouped by the parent MOC, under a rule with `governs`, `implementation_ref` and `--check`; no `index.md`, and every §N pointer in the vault replaced by a slug.
**＋** The scripts hold no `file` route: no `RULE_CLASS`, no `category: file`, no "applied by hand", no `rule_class_path`, no `prose_names`; the vault changes only by the scripts, from decisions.
**＋** Every rule has its parent by the criterion of the audit: under a category's MOC a rule that holds for that category alone, the MOC made at two or more such rules, else the schemas under `rule-page-schemas`; `applies_to` on a Rule and `rules` on an Entity carry the edge Rule → Entity, the sprint's rule to the sprint MOC the first.
**＋** "Rule-class" is a retired term in the Case schema and in the glossary, and no docstring of `guppi/` and no test name of `tests/` carries it.

## Result

2026-09-29, no vault/wiki/*/schema.md, vault/wiki/index.md absent; grep for rule.class, applied by hand, prose_names over guppi/ and tests/ empty; render --check and glossary --check exit 0

## History

- 2026-09-22 created · [[decision-case-301]]
- 2026-09-22 updated: the glossary is rendered from entity-glossary, not from a terms field (case 306.7) · [[decision-case-306.7]]
- 2026-09-22 updated: the pointer at §1 of index.md is gone with the file (case 321) · [[decision-case-321]]
- 2026-09-23 updated: the reading of the Slice without make lint, the grep widened to the retired term over guppi/ and tests/ (case 367) · [[decision-case-367]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/2050/ledger.md#L30
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given, the pointer to lint-clean and the bounds of the Slice out (case 494.4) · [[decision-case-494.4]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L65
- 2026-10-10 status: passed → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
