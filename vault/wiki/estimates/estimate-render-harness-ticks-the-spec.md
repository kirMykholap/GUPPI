---
type: estimate
kind: QA
status: passed
target: "[[rule-render-harness]]"
purpose: render, once it wrote the harness and exits 0, ticks the guppi render lines of every Spec under raw/ whose yaml is applied whole
method: "pytest .guppi/tests/test_render.py; by hand, after a librarian's run: the spec.md of its session read against the Criterion"
checked: 2026-11-27
origin: raw/2026-09-17/1119/ledger.md#case-226.2
sprint: migration
created: 2026-09-17
tags: [harness, render]
---

## Criterion

When:
`guppi render` without a flag wrote the governed files and exits 0, and reads the units under `vault/raw/` that have a `materialize.yaml`.

Then:
In the `spec.md` of every unit whose yaml is applied whole, every unticked task line whose text opens with a code span holding `guppi render` becomes `- [x]`. A yaml is applied whole when each entry carries `applied` or `superseded_by` and none carries `failed`, as `guppi archive` counts it. Nothing else in the file changes, but the map at the head of an approved document that holds one, which `rule-spec-write` rebuilds.
**－** A line where `guppi render` sits in a later code span, such as a `read` line or a line that names the command in its description, is not ticked.
**－** `--check` and `--sync` tick nothing, and a run that exits 1 ticks nothing.
**－** A unit without a yaml, with an entry that carries neither `applied` nor `superseded_by`, with a `failed` entry, or marked by `carry.md`, is not touched.

## Result

2026-11-27, at the /hi of session 2214: uv run --project .guppi pytest .guppi/tests/test_render.py 44 passed; by hand, git diff def97898^ def97898 on vault/raw/2026-11-27/1402/spec.md, the librarian's run of session 1402, whose yaml the brief gives as applied whole (21 entries applied, line 3 superseded_by 1086, none failed): the two task lines opening with a code span holding guppi render, lines 154 and 299, went from - [ ] to - [x]; every other changed line below the map is a tick of a task line, and the map at the head was rebuilt; the read line of this Estimate stays - [ ]; the seven guppi render lines of the 0947 Spec stood ticked before the run

## History

- 2026-09-18 created · [[decision-case-226.2]]
- 2026-09-18 updated: the Criterion replaced whole — a render line opens with the code span holding guppi render (case 235) · [[decision-case-235]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/1957/ledger.md#L1
- 2026-09-18 updated: the Criterion replaced whole — a yaml is applied whole when every entry carries applied or superseded_by and none failed, as guppi archive counts it (case 250.1) · [[decision-case-250.1]]
- 2026-09-20 status: pending → passed · raw/2026-09-18/2253/ledger.md#L5
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given out, the yaml applied whole stated (case 491.4) · [[decision-case-491.4]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L62
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-17 updated: the method waits for a librarian's run, with no past moment · [[decision-case-875]]
- 2026-11-27 updated: the Criterion replaced whole — nothing else in the file changes but the map of an approved document · [[decision-case-1085.6]]
- 2026-11-28 status: pending → passed · raw/2026-11-27/2214/ledger.md#L1
