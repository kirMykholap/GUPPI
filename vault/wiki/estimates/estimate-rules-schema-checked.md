---
type: estimate
kind: QA
status: pending
target: "[[rule-rules-schema]]"
purpose: A Rule page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
method: pytest tests/test_schemas.py -k rules on the live vault/wiki/rules/schema.yaml — a page in the shape, then one defect at a time; the live reading make lint, no schema finding on wiki/rules/ but the placeholders
origin: raw/2026-09-22/0014/ledger.md#case-305.1
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Criterion

Given:
`rule-render-harness`: the text of a `## Render` section of a page with `render_mode: full`, between its markers, becomes the whole file named by `governs`, without the markers; two `full` pages on one file fail the render (`tests/test_render.py`).
**＋** `rule-governed-files-hook` refuses a hand edit of a file a live rule governs.
**＋** `rule-lint` reads from `vault/wiki/<category>/schema.yaml` `properties.required`, `optional`, `values`, `conditional` and `body.required`, `optional`, `conditional`; a missing file is a finding; other keys it does not read.
**＋** `tests/test_schemas.py` fixes the behaviour on the live `vault/wiki/rules/schema.yaml`: a page in the shape, then one defect at a time.

When:
`guppi render` writes `vault/wiki/rules/schema.yaml` from `rule-rules-schema`; `guppi lint` reads a page of `wiki/rules/`.

Then:
The file equals the Render. Lint reads from it: required `type, kind, purpose, status, estimates, origin, sprint, created, tags`; optional `enforcement, implementation_ref, governs, render_mode, parent, children, deferred_by, applies_to`; values `kind: MOC | Leaf`, `status: draft | built | archived`, `enforcement: hook | check | render`, `render_mode: full | partial`; conditional — `hook` and `check` require `implementation_ref`, `render` requires `governs`, `render_mode` and the section `## Render`, `MOC` requires `children` and forbids `enforcement: hook | check`; the sections `## Purpose` and `## History` required, `## Render` and `## How it works` optional; `ordered_children: true`.
**＋** A Rule page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect; a rule with `applies_to` on a live Entity has none.
**＋** The prose of the former `schema.md` stands in the file as data: `description` — the introduction, Ordering, MOCs and enforcement, Enforcement, verbatim, and one sentence on the edge Rule → Entity after the paragraph of case 240.2; `fields` and `sections` — the rows of the tables whole, `applies_to` among them; `examples` — the four example pages.
**－** `vault/wiki/rules/schema.md` does not exist.

## History

- 2026-09-22 created · [[decision-case-305.1]]
