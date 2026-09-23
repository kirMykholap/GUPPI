---
type: estimate
kind: QA
status: passed
target: "[[rule-page-schemas]]"
purpose: Each vault/wiki/<category>/schema.yaml is written by guppi render from exactly one rule page, no schema.md remains, lint reads every file and a hand edit is refused
method: make lint — render --check exit 0 and no path or schema-description finding on a <category>/schema; tests/test_render.py for two full pages on one file; the live reading by hand after the librarian's first render
checked: 2026-09-23
origin: raw/2026-09-22/0014/ledger.md#case-304.1
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Criterion

Given:
`rule-render-harness`: the text of a `## Render` section of a page with `render_mode: full`, between its markers, becomes the whole file named by `governs`, without the markers; two `full` pages on one file fail the render (`tests/test_render.py`).
**＋** `rule-governed-files-hook` refuses a hand edit of a file a live rule governs.
**＋** `rule-lint` reads from `vault/wiki/<category>/schema.yaml` `properties.required`, `optional`, `values`, `conditional` and `body.required`, `optional`, `conditional`, and `properties.single` (362.1); a missing file is a finding; other keys it does not read.

When:
`guppi render` writes the files, then `guppi lint` reads the vault.

Then:
The six `vault/wiki/<category>/schema.yaml` are written, each from the one Leaf that governs it; `render --check` after it exits 0; there is no seventh file and no `schema.md` in any category.
**＋** Lint reads each file and gives no `path` and no `schema-description` finding on `<category>/schema`.
**＋** A hand edit of any of the six is refused by the hook.
**－** A second `full` page on one of the files fails the render with the two slugs.

## Result

2026-09-23, six vault/wiki/*/schema.yaml, each named by the governs of one rule page, no seventh file and no schema.md; uv run guppi render --check exit 0; uv run guppi lint: no path and no schema-description finding; tests/test_render.py 26 passed, the two full pages on one file among them; the hook leg by tests/test_guard.py, 20 passed, a governed path refused

## History

- 2026-09-22 created · [[decision-case-304.1]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L82
- 2026-09-23 updated: the Given names properties.single among the keys lint reads (case 362.1) · [[decision-case-362.1]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1126/ledger.md#L32
