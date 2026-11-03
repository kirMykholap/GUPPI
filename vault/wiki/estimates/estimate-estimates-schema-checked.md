---
type: estimate
kind: QA
status: passed
target: "[[rule-estimates-schema]]"
purpose: An Estimate page in the shape of the rendered schema has no schema finding and a page outside it has one per defect
method: "by hand, after the librarian's run that renders vault/wiki/estimates/schema.yaml from the Render of rule-estimates-schema that holds the field once: the output of uv run --project .guppi pytest .guppi/tests/test_schemas.py -k estimate over that live file, the tests of once among them, and the output of uv run --project .guppi guppi check, no schema finding on wiki/estimates/, read against the Criterion, both outputs in the estimate line"
checked: 2026-10-31
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, render, schema]
core: true
---

## Criterion

When:
`guppi render` writes `vault/wiki/estimates/schema.yaml` from `rule-estimates-schema`, and `guppi lint` reads a page of `vault/wiki/estimates/`.

Then:
The file equals the Render. Lint reads from it: required `type, kind, status, target, method, origin, sprint, created, tags`; optional `purpose, checked, deferred_by, core, once`; values `kind: QA | Research`, `status: pending | passed | failed`, `core: true`, `once: true`; the sections `## Criterion` and `## History` required, `## Result` optional, `## Result` required on `passed` and on `failed`.
**＋** An Estimate page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect.
**＋** An Estimate page without a `method` field has the finding `schema: missing field method`.
**＋** An Estimate page in the shape with `core: true`, `origin: guppi` and `sprint: guppi` has no `schema` finding.
**＋** An Estimate page in the shape with `once: true` has no `schema` finding, and one with any other value of `once` has one finding.
**＋** `fields` and `sections` describe each name of these lists, `core` and `once` among them; the description of `once` says that a one-time Estimate targets the live sprint page and that lint reports one whose target is not a sprint page; the descriptions of `origin` and `sprint` name the value `guppi` on a page with `core: true` in the clean version; `description` holds, among its paragraphs, the introduction, the sentence on a one-time Estimate, the `failed` paragraph, the fields deliberately absent, the two kinds, and the Result and Criterion paragraph; `examples` holds the example pages.
**－** `description`, `fields` and `sections` name no `unmigrated` count, no recut of an older page, no `## Context` or `## Method` section, and no `Given:` kept on an older page.

## Result

2026-10-31, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
