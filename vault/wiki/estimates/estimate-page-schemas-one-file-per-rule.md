---
type: estimate
kind: QA
status: passed
target: "[[rule-page-schemas]]"
purpose: Each vault/wiki/<category>/schema.yaml is written by guppi render from exactly one rule page, no schema.md remains, lint reads every file and a hand edit is refused
method: make lint — render --check exit 0 and no path or schema-description finding on a <category>/schema; tests/test_render.py for two full pages on one file; the live reading by hand after the librarian's first render
checked: 2026-09-29
origin: raw/2026-09-22/0014/ledger.md#case-304.1
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
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

2026-09-29, six schema.yaml, one per governs of the six children of rule-page-schemas, no schema.md; render --check exit 0; no path or schema-description finding; tests/test_render.py 34 passed

## History

- 2026-09-22 created · [[decision-case-304.1]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L82
- 2026-09-23 updated: the Given names properties.single among the keys lint reads (case 362.1) · [[decision-case-362.1]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1126/ledger.md#L32
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given out, the count of files out, the missing file stated (case 490.1) · [[decision-case-490.1]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L60
