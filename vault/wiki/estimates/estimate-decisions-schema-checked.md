---
type: estimate
kind: QA
status: passed
target: "[[rule-decisions-schema]]"
purpose: A Decision page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
method: "pytest .guppi/tests/test_schemas.py -k decision on the live vault/wiki/decisions/schema.yaml — a page in the shape, a page without ## Context, a page without ## Problem, then one defect at a time; the live reading uv run --project .guppi guppi check, no schema finding on wiki/decisions/"
checked: 2026-09-30
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, render, schema]
core: true
---

## Criterion

When:
`guppi render` writes `vault/wiki/decisions/schema.yaml` from `rule-decisions-schema`, and `guppi lint` reads a page of `vault/wiki/decisions/`.

Then:
The file equals the Render. Lint reads from it: required `type, case, status, origin, sprint, created, tags`; optional `create, update, delete, defer, source, supersedes, superseded_by, parent, children`; values `status: current | superseded | archived`; the section `## History` required, `## Context`, `## Problem`, `## Recommend`, `## Given`, `## When`, `## Criterion`, `## Deferred`, `## Note` optional.
**＋** A Decision page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list or lacking a required section has one finding per defect.
**＋** A Decision page without `## Context`, and one without `## Problem`, has no `schema` finding.
**＋** `fields` and `sections` describe each name of these lists; `description` holds the introduction, the Slug, the fields deliberately absent and the body paragraph; `examples` holds the example page.
**＋** The file says that the History of a Decision takes `created`, `superseded by` and one `updated:` line of a Case that signs its text after the fact.
**＋** The file says that the Case file, `cases/case-<N>.md` in the folder of `origin` with N the id of the top-level Case, holds the whole Case and moves into the archive with its session; that a new page carries `## Context` only for a Case without `given` and without sub-cases, the short form of a deferred decision, and in the two-line body of a Case superseded in its own session; that it never carries `## Given`; and that the pages written before keep the sections they carry.
**＋** The file says that a new page carries `## Problem` and `## Recommend` for a Case without sub-cases and on the page of a Case with sub-cases, which lists their pages in `children` in place of the kind lists; and that the page of a sub-case carries `parent`, its own `## Recommend` when it has one, and no `## Problem`.
**－** The example page holds no `## Context` and no `## Given`.

## Result

2026-09-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
