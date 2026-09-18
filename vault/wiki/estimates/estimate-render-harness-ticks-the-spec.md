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

Given:
`guppi render` without a flag writes every governed file and exits 0, or writes nothing and exits 1.
**＋** The units under `raw/` with a yaml are `units_with`; a yaml is applied whole when every entry carries `applied` or `superseded_by` and none `failed`, as `guppi archive` counts it (case 250.1).
**＋** `tests/test_render.py` fixes the behaviour on a temp vault.

When:
`guppi render` without a flag wrote the files and exits 0.

Then:
In the `spec.md` of every unit under `raw/` whose yaml is applied whole, every unticked task line whose text opens with a code span holding `guppi render` becomes `- [x]`; nothing else changes.
**－** A line where `guppi render` sits in a later code span — a `read `<slug>`` line, a line that names the command in its description — is not ticked.
**－** `--check` and `--sync` tick nothing; exit 1 ticks nothing.
**－** A unit without a yaml, with an entry that carries neither `applied` nor `superseded_by`, with a `failed` entry, or marked by `carry.md`, is not touched.

## Result

2026-09-18, `uv run pytest tests/test_render.py` and the Spec of `archive/migration/2026-09-17/1119/raw/spec.md` after the librarian's run of 1252: tests green (35 with test_sprint.py); the five `- [x] `uv run guppi render`: …` lines ticked (105, 441, 494, 565, 646); the read line 260, returned to `[ ]` in session 1252, still `[ ]` — a `guppi render` in a later code span is not ticked; the 1252 Spec holds no render line and nothing there changed

## History

- 2026-09-18 created · [[decision-case-226.2]]
- 2026-09-18 updated: the Criterion replaced whole — a render line opens with the code span holding guppi render (case 235) · [[decision-case-235]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/1957/ledger.md#L1
- 2026-09-18 updated: the Criterion replaced whole — a yaml is applied whole when every entry carries applied or superseded_by and none failed, as guppi archive counts it (case 250.1) · [[decision-case-250.1]]
