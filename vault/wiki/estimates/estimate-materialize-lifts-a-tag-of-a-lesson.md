---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: Whether a tag that a newtag block of a lesson line declares reaches the new_tags of materialize.yaml once, with its meaning and aliases
method: uv run --project .guppi pytest .guppi/tests/test_materialize.py -k newtag
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, ledger]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi materialize` lifts a `lesson[...]` line of the `raw/<date>/<hi HHMM>/ledger.md` of a unit that carries a `{newtag:<tag>|<meaning>|<aliases>}` block.

Then:
The `new_tags` of the `raw/<date>/<hi HHMM>/materialize.yaml` of the unit hold the tag once, with its meaning and its aliases.
**＋** The tags that the Cases of the `raw/<date>/<hi HHMM>/spec.md` of the unit declare stand first, and a tag that one of them declares keeps the meaning and aliases of that Case.
**＋** A tag that two lesson lines declare keeps the declaration of the earlier line.
**＋** The lesson entry carries its tags, its trigger and its root cause as before.
**－** The yaml gains no entry from a lesson record of `.guppi/guppi/materialize.py` that holds no `new_tags`.

## Result

2026-10-15, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
