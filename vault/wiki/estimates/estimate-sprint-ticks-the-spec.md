---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint]]"
purpose: sprint, once it wrote sprint.md and exits 0, ticks the guppi sprint lines of every Spec under raw/ whose yaml is applied whole
method: "pytest .guppi/tests/test_sprint.py; by hand, after a librarian's run: the spec.md of each unit under vault/raw/ whose guppi sprint line it ticked, and any guppi sprint-close line there left as it stood"
checked: 2026-11-27
origin: raw/2026-09-18/2054/ledger.md#case-250.2
sprint: migration
created: 2026-09-18
tags: [harness, sprint]
---

## Criterion

When:
`guppi sprint` without a flag wrote `vault/wiki/sprint.md` and exits 0, and reads the units under `vault/raw/` that have a `materialize.yaml`.

Then:
In the `spec.md` of every unit whose yaml is applied whole, every unticked task line that opens with a code span holding `guppi sprint` becomes `- [x]`. A yaml is applied whole when each entry carries `applied` or `superseded_by` and none carries `failed`. Nothing else in the file changes, but the map at the head of an approved document that holds one, which `rule-spec-write` rebuilds.
**－** A line where `guppi sprint` sits in a later code span, such as a `read` line or a description, is not ticked.
**－** A line whose first code span holds `guppi sprint-close` is not ticked: `guppi sprint-close` ticks it.
**－** `--check` ticks nothing, and a run that exits 1 ticks nothing.
**－** A unit without a yaml, with an entry not applied, with a `failed` entry, or marked by `carry.md`, is not touched.

## Result

2026-11-27, at the /hi of session 2214: uv run --project .guppi pytest .guppi/tests/test_sprint.py 35 passed; by hand, the librarian's run of session 1402 (commit def97898): no task line of vault/raw/2026-11-27/1402/spec.md or vault/raw/2026-11-27/0947/spec.md opens with a code span holding guppi sprint or guppi sprint-close (grep), so the run ticked none, and the diff of both Specs in that commit is ticks of task lines and the rebuilt map only; the tick clause and the sprint-close clause were not exercised live

## History

- 2026-09-18 created · [[decision-case-250.2]]
- 2026-09-20 status: pending → passed · raw/2026-09-18/2253/ledger.md#L4
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given out, the yaml applied whole stated (case 491.1) · [[decision-case-491.1]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L66
- 2026-10-04 updated: the Criterion replaced whole — a guppi sprint-close line is not ticked by guppi sprint (case 628.5) · [[decision-case-628.5]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/2041/ledger.md#L5
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-11-27 updated: the Criterion replaced whole — nothing else in the file changes but the map of an approved document; the method names the librarian's run as the event it waits for · [[decision-case-1085.7]]
- 2026-11-28 status: pending → passed · raw/2026-11-27/2214/ledger.md#L2
