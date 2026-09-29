---
type: estimate
kind: QA
status: pending
target: "[[rule-decisions-schema]]"
purpose: A Decision page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
method: "pytest tests/test_schemas.py -k decisions on the live vault/wiki/decisions/schema.yaml — a page in the shape, a page without ## Context, then one defect at a time; the live reading make lint, no schema finding on wiki/decisions/ but the pages of Cases 1–28 without Problem (Slice 5)"
checked: 2026-09-29
origin: raw/2026-09-22/0014/ledger.md#case-304.7
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Criterion

When:
`guppi render` writes `vault/wiki/decisions/schema.yaml` from `rule-decisions-schema`, and `guppi lint` reads a page of `vault/wiki/decisions/`.

Then:
The file equals the Render. Lint reads from it: required `type, case, status, origin, sprint, created, tags`; optional `create, update, delete, defer, source, supersedes, superseded_by`; values `status: current | superseded | archived`; the sections `## Problem` and `## History` required, `## Context`, `## Given`, `## When`, `## Criterion`, `## Deferred`, `## Note` optional.
**＋** A Decision page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list or lacking a required section has one finding per defect.
**＋** A Decision page without `## Context` has no `schema` finding.
**＋** `fields` and `sections` describe each name of these lists; `description` holds the introduction, the Slug, the fields deliberately absent and the body paragraph; `examples` holds the example page.
**＋** The file says that the History of a Decision takes `created`, `superseded by` and one `updated:` line of a Case that signs its text after the fact.
**＋** The file says that the Case file, `cases/case-<N>.md` in the folder of `origin` with N the id of the top-level Case, holds the whole Case, `recommend` included, and moves into the archive with its session.
**＋** The file says that a new page carries `## Context` only for a Case without `given`, the short form of a deferred decision, and in the two-line body of a Case superseded in its own session; that it never carries `## Given`; and that the pages written before keep the sections they carry.
**－** The example page holds no `## Context` and no `## Given`.

## Result

2026-09-29, uv run pytest tests/test_schemas.py -k decisions: 4 passed, 1 skipped; guppi lint: 62 schema lines on decisions/, all on the pages of Cases 1-28 (missing Context and Problem), none other

## History

- 2026-09-22 created · [[decision-case-304.7]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/0014/ledger.md#L57
- 2026-09-23 updated: the Criterion names the updated line of a Decision's History (case 358) · [[decision-case-358]]
- 2026-09-23 updated: the Given names properties.single among the keys lint reads (case 362.1) · [[decision-case-362.1]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1126/ledger.md#L27
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given and the history of schema.md out (case 490.5) · [[decision-case-490.5]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L51
- 2026-09-29 updated: the Criterion replaced whole and the method set anew — Context optional, the Case file named, the example without Context and Given (case 513.1) · [[decision-case-513.1]]
