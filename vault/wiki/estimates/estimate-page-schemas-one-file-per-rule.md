---
type: estimate
kind: QA
status: pending
target: "[[rule-page-schemas]]"
purpose: Each vault/wiki/<category>/schema.yaml is written by guppi render from exactly one rule page, no schema.md remains, lint reads every file and a hand edit is refused
method: make lint — render --check exit 0 and no path or schema-description finding on a <category>/schema; tests/test_render.py for two full pages on one file; the live reading by hand after the librarian's first render
origin: raw/2026-09-22/0014/ledger.md#case-304.1
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Criterion

Given:
`rule-render-harness`: the text of a `## Render` section of a page with `render_mode: full`, between its markers, becomes the whole file named by `governs`, without the markers; two `full` pages on one file fail the render (`tests/test_render.py`).
**＋** `rule-governed-files-hook` refuses a hand edit of a file a live rule governs.
**＋** `rule-lint` reads from `vault/wiki/<category>/schema.yaml` `properties.required`, `optional`, `values`, `conditional` and `body.required`, `optional`, `conditional`; a missing file is a finding; other keys it does not read.

When:
`guppi render` writes the files, then `guppi lint` reads the vault.

Then:
The six `vault/wiki/<category>/schema.yaml` are written, each from the one Leaf that governs it; `render --check` after it exits 0; there is no seventh file and no `schema.md` in any category.
**＋** Lint reads each file and gives no `path` and no `schema-description` finding on `<category>/schema`.
**＋** A hand edit of any of the six is refused by the hook.
**－** A second `full` page on one of the files fails the render with the two slugs.

## History

- 2026-09-22 created · [[decision-case-304.1]]
