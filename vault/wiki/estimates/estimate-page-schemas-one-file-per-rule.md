---
type: estimate
kind: QA
status: passed
target: "[[rule-page-schemas]]"
purpose: Each vault/wiki/<category>/schema.yaml is written by guppi render from exactly one rule page, no schema.md remains, lint reads every file and a hand edit is refused
method: uv run --project .guppi pytest .guppi/tests/test_schemas.py .guppi/tests/test_render.py .guppi/tests/test_lint.py .guppi/tests/test_guard.py; uv run --project .guppi guppi check — render --check exit 0 and no path or schema-description finding on a <category>/schema
checked: 2026-09-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, render, schema]
core: true
---

## Criterion

When:
`guppi render` writes the governed files, and then `guppi lint` reads the vault.

Then:
Each category folder of `vault/wiki/` holds one `schema.yaml`, written from the one child of `rule-page-schemas` that governs it, and `render --check` after the render exits 0.
**＋** No other `schema.yaml` and no `schema.md` stands in a category folder.
**＋** Lint reads each file and gives no finding of the class `path` or `schema-description` on the schema of a category.
**＋** A category folder without its `schema.yaml` is the `schema` finding `schema.yaml is missing`.
**＋** The hook of `rule-governed-files-hook` refuses a hand edit of any of the files.
**－** A second `full` page on one of the files fails the render with the two slugs.

## Result

2026-09-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
