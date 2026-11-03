---
type: estimate
kind: QA
status: passed
target: "[[rule-render-harness]]"
purpose: render, once it wrote the harness and exits 0, ticks the guppi render lines of every Spec under raw/ whose yaml is applied whole
method: "pytest .guppi/tests/test_render.py; by hand, after a librarian's run: the spec.md of its session read against the Criterion"
checked: 2026-09-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, render]
core: true
---

## Criterion

When:
`guppi render` without a flag wrote the governed files and exits 0, and reads the units under `vault/raw/` that have a `materialize.yaml`.

Then:
In the `spec.md` of every unit whose yaml is applied whole, every unticked task line whose text opens with a code span holding `guppi render` becomes `- [x]`. A yaml is applied whole when each entry carries `applied` or `superseded_by` and none carries `failed`, as `guppi archive` counts it. Nothing else in the file changes.
**－** A line where `guppi render` sits in a later code span, such as a `read` line or a line that names the command in its description, is not ticked.
**－** `--check` and `--sync` tick nothing, and a run that exits 1 ticks nothing.
**－** A unit without a yaml, with an entry that carries neither `applied` nor `superseded_by`, with a `failed` entry, or marked by `carry.md`, is not touched.

## Result

2026-09-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
