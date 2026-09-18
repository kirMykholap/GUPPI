---
type: estimate
kind: QA
status: pending
target: "[[rule-render-harness]]"
purpose: render, once it wrote the harness and exits 0, ticks the guppi render lines of every Spec under raw/ whose yaml is applied whole
method: pytest tests/test_render.py, plus one reading of this session's spec.md after the librarian's run
origin: raw/2026-09-17/1119/ledger.md#case-226.2
sprint: migration
created: 2026-09-17
tags: [harness, render]
---

## Criterion

Given:
`guppi render` without a flag writes every governed file and exits 0, or writes nothing and exits 1.
**＋** The units under `raw/` with a yaml are `units_with`; a yaml is applied whole when every entry carries `applied`.
**＋** `tests/test_render.py` fixes the behaviour on a temp vault.

When:
`guppi render` without a flag wrote the files and exits 0.

Then:
In the `spec.md` of every unit under `raw/` whose yaml is applied whole, every unticked task line whose text opens with a code span holding `guppi render` becomes `- [x]`; nothing else changes.
**－** A line where `guppi render` sits in a later code span — a `read `<slug>`` line, a line that names the command in its description — is not ticked.
**－** `--check` and `--sync` tick nothing; exit 1 ticks nothing.
**－** A unit without a yaml, with an unapplied or `failed` entry, or marked by `carry.md`, is not touched.

## History

- 2026-09-18 created · [[decision-case-226.2]]
- 2026-09-18 updated: the Criterion replaced whole — a render line opens with the code span holding guppi render (case 235) · [[decision-case-235]]
