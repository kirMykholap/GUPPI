---
type: estimate
kind: QA
status: passed
target: "[[rule-rules-schema]]"
purpose: A Rule page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
method: "pytest .guppi/tests/test_schemas.py -k rules on the live vault/wiki/rules/schema.yaml — a page in the shape, then one defect at a time; by hand, after a librarian's run: the live vault/wiki/rules/schema.yaml read against the Criterion, and the live reading uv run --project .guppi guppi check, no schema finding on wiki/rules/ but the placeholders"
checked: 2026-10-30
origin: raw/2026-09-22/0014/ledger.md#case-305.1
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Criterion

When:
`guppi render` writes `vault/wiki/rules/schema.yaml` from `rule-rules-schema`, and `guppi lint` reads a page of `vault/wiki/rules/`.

Then:
The file equals the Render. Lint reads from it: required `type, kind, purpose, status, estimates, origin, sprint, created, tags`; optional `enforcement, implementation_ref, governs, render_mode, parent, children, deferred_by, applies_to, core`; values `kind: MOC | Leaf`, `status: draft | built | archived`, `enforcement: hook | check | render`, `render_mode: full | partial`, `core: true`; conditional — `hook` and `check` require `implementation_ref`, `render` requires `governs`, `render_mode` and the section `## Render`, `MOC` requires `children` and forbids `enforcement: hook | check`; the sections `## Purpose` and `## History` required, `## Render` and `## How it works` optional.
**＋** The file also holds `ordered_children: true`, which lint does not read.
**＋** A Rule page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect; a rule with `applies_to` on a live Entity has none.
**＋** A Rule page in the shape with `core: true`, `origin: guppi` and `sprint: guppi` has no `schema` finding.
**＋** `fields` and `sections` describe each name of these lists, `core` among them, and the descriptions of `origin` and `sprint` name the value `guppi` on a page with `core: true` in the clean version; `description` holds the introduction, Ordering, MOCs and enforcement, Enforcement, the sentence on the edge Rule → Entity, the one on the guard of the agent's own conduct and the one on the Estimates that a shipped page brings along; `examples` holds the example pages.
**＋** That last sentence says that a shipped page arrives with each of its Estimates that passed in the repository it came from and whose `method` names no target of the `Makefile`, and that the receiving project writes its other Estimates through its own Cases.
**＋** The description of `## How it works` under `sections` says that the section is for a MOC alone and that a Leaf carries none, and no example of a Leaf under `examples` carries the section.

## Result

2026-10-30, /hi of session 2345: uv run --project .guppi pytest .guppi/tests/test_schemas.py -k rules 7 passed; the live vault/wiki/rules/schema.yaml read against the Criterion: required, optional, values, conditional, ordered_children and body as the Criterion lists them; fields and sections describe each name, core among them, and origin and sprint name the value guppi; description holds the introduction, Ordering, MOCs and enforcement, Enforcement, the edge Rule → Entity, the guard of the agent's own conduct and the sentence on the Estimates a page with core: true brings along; the description of ## How it works says MOC only and that a Leaf carries none, and no Leaf example carries the section; uv run --project .guppi guppi check 13 lines (exit 1), none a schema finding, its lines on rules/ "status: a page with core: true that is draft"

## History

- 2026-09-22 created · [[decision-case-305.1]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L80
- 2026-09-23 updated: the Given names properties.single among the keys lint reads (case 362.1) · [[decision-case-362.1]]
- 2026-09-23 updated: the Criterion names the sentence on the guard of the agent's own conduct (case 372) · [[decision-case-372]]
- 2026-09-24 status: pending → passed · raw/2026-09-24/1303/ledger.md#L24
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given, the history of schema.md and the ordered_children read by lint out (case 490.2) · [[decision-case-490.2]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L63
- 2026-10-13 updated: the Criterion replaced whole — the field core and the shipped values (case 804) · [[decision-case-804.2]]
- 2026-10-13 status: pending → passed · raw/2026-10-13/1753/ledger.md#L117
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `make lint` → `uv run --project .guppi guppi check` · [[decision-case-820.7]]
- 2026-10-16 updated: the Criterion replaced whole — the description says that a page with core: true comes into a new project with its passed Estimates · [[decision-case-856.3]]
- 2026-10-17 status: pending → passed · raw/2026-10-16/2104/ledger.md#L1
- 2026-10-17 updated: the method waits for a librarian's run, with no past moment · [[decision-case-875]]
- 2026-10-30 updated: the Criterion replaced whole — the description of How it works says a Leaf carries none, and no example of a Leaf carries it · [[decision-case-942.2]]
- 2026-10-31 status: pending → passed · raw/2026-10-30/2345/ledger.md#L2
