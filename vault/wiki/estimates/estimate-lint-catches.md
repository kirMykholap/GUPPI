---
type: estimate
kind: QA
status: passed
target: "[[rule-lint]]"
purpose: lint reads every live page against the schema of its category and prints one line per finding, exit 1 on any
method: pytest in .guppi/tests/test_lint.py, one test per defect class; the live reading once by hand, written into the estimate line
checked: 2026-09-24
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi lint` reads the live pages under `vault/wiki/<category>/`.

Then:
Each finding is one line `<category>/<slug>: <class>: <what>`; exit 1 on any finding, 0 and no output on a clean vault; nothing is written.
**＋** `schema`: a missing required field or section, a value outside the list of `values`, a conditional not met, a field of `properties.single` holding a list; `## When` is never required on a Decision page.
**＋** `schema-description`: a field or section the lists of `schema.yaml` name without a description under `fields` or `sections`, or a description of a name no list carries.
**＋** `layout`: a page whose `type` does not match its folder, a page whose `slug` field is not its filename, a `.md` at the root of `vault/wiki/` that no live rule page names.
**＋** `path`: a file named in `implementation_ref` or `governs` that does not exist.
**＋** `markers`: a page with `enforcement: render` without `## Render`, or whose Render does not open with `<!-- slug -->` and close with `<!-- /slug -->`; a page with `render_mode: full` whose Render holds a closing line `<!-- /child -->` for one of its `children`.
**－** A page under `vault/archive/` is not read.

## Result

2026-09-24, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
