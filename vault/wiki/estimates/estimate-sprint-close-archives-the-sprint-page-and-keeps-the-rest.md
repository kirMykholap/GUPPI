---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint-close]]"
purpose: At the close of a sprint the sprint page and its own Estimates go to the archive, and every other passed Estimate stays live
method: pytest .guppi/tests/test_sprint_close.py -k sprint_page; by hand, the output of the preview uv run --project .guppi guppi sprint-close --sprint <id> over the live vault, <id> the sprint that vault/wiki/sprint.md names, read against the Then
checked: 2026-10-04
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [sprint, workflow]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi sprint-close --sprint <id> --apply` closes the sprint `entity-sprint-<id>` of the made-up vault of `.guppi/tests/test_sprint_close.py`, after each Estimate that `entity-sprint-<id>` lists and that does not stand `passed` is read or archived unread, as the person chooses; someone reads `vault/wiki/entities/`, `vault/wiki/estimates/` and `vault/archive/` after it.
**＋** Or the preview `uv run --project .guppi guppi sprint-close --sprint <id>` runs over the live vault, and someone reads its output against `vault/wiki/entities/` and `vault/wiki/estimates/`.

Then:
`entity-sprint-<id>` and each Estimate its `estimates` lists stand under `vault/archive/`.
**＋** The preview names `entity-sprint-<id>` and each of those Estimates among the pages the close would move, and moves none.
**－** Every other Estimate that stands `passed` stays under `vault/wiki/estimates/`, and the rule or Entity that lists it keeps it in `estimates`.
**－** The close does not archive the MOC `entity-sprint`.

## Result

2026-10-04, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
