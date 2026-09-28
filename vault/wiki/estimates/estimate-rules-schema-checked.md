---
type: estimate
kind: QA
status: pending
target: "[[rule-rules-schema]]"
purpose: A Rule page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
method: pytest tests/test_schemas.py -k rules on the live vault/wiki/rules/schema.yaml — a page in the shape, then one defect at a time; the live reading make lint, no schema finding on wiki/rules/ but the placeholders
checked: 2026-09-24
origin: raw/2026-09-22/0014/ledger.md#case-305.1
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Criterion

When:
`guppi render` writes `vault/wiki/rules/schema.yaml` from `rule-rules-schema`, and `guppi lint` reads a page of `vault/wiki/rules/`.

Then:
The file equals the Render. Lint reads from it: required `type, kind, purpose, status, estimates, origin, sprint, created, tags`; optional `enforcement, implementation_ref, governs, render_mode, parent, children, deferred_by, applies_to`; values `kind: MOC | Leaf`, `status: draft | built | archived`, `enforcement: hook | check | render`, `render_mode: full | partial`; conditional — `hook` and `check` require `implementation_ref`, `render` requires `governs`, `render_mode` and the section `## Render`, `MOC` requires `children` and forbids `enforcement: hook | check`; the sections `## Purpose` and `## History` required, `## Render` and `## How it works` optional.
**＋** The file also holds `ordered_children: true`, which lint does not read.
**＋** A Rule page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect; a rule with `applies_to` on a live Entity has none.
**＋** `fields` and `sections` describe each name of these lists; `description` holds the introduction, Ordering, MOCs and enforcement, Enforcement, the sentence on the edge Rule → Entity and the one on the guard of the agent's own conduct; `examples` holds the example pages.

## Result

2026-09-24, uv run pytest tests/test_schemas.py -k rules: 5 passed; guppi render --check exit 0; vault/wiki/rules/schema.md absent; guppi lint on wiki/rules/: schema findings only on the placeholder rule-spec-box (missing kind, missing estimates) and its orphan finding

## History

- 2026-09-22 created · [[decision-case-305.1]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L80
- 2026-09-23 updated: the Given names properties.single among the keys lint reads (case 362.1) · [[decision-case-362.1]]
- 2026-09-23 updated: the Criterion names the sentence on the guard of the agent's own conduct (case 372) · [[decision-case-372]]
- 2026-09-24 status: pending → passed · raw/2026-09-24/1303/ledger.md#L24
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given, the history of schema.md and the ordered_children read by lint out (case 490.2) · [[decision-case-490.2]]
