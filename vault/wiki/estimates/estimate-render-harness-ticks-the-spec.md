---
type: estimate
kind: QA
status: pending
target: "[[rule-render-harness]]"
purpose: render, once it wrote the harness and exits 0, ticks the guppi render lines of every Spec under raw/ whose yaml is applied whole
method: pytest tests/test_render.py, plus one reading of this session's spec.md after the librarian's run
checked: 2026-09-18
origin: raw/2026-09-17/1119/ledger.md#case-226.2
sprint: migration
created: 2026-09-17
tags: [harness, render]
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

2026-09-18, pytest tests/test_render.py (a yaml with a superseded entry ticked, an unmarked and a failed one not) and the librarian's `uv run guppi render` of commit 3e1251f: the `uv run guppi render` lines 162, 193 of the 2054 Spec ticked, nothing else changed; the 1957 Spec holds no render line, so the superseded entry is read live through `sprint` on the same `applied_whole`, and in the test for `render` itself

## History

- 2026-09-18 created · [[decision-case-226.2]]
- 2026-09-18 updated: the Criterion replaced whole — a render line opens with the code span holding guppi render (case 235) · [[decision-case-235]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/1957/ledger.md#L1
- 2026-09-18 updated: the Criterion replaced whole — a yaml is applied whole when every entry carries applied or superseded_by and none failed, as guppi archive counts it (case 250.1) · [[decision-case-250.1]]
- 2026-09-20 status: pending → passed · raw/2026-09-18/2253/ledger.md#L5
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given out, the yaml applied whole stated (case 491.4) · [[decision-case-491.4]]
