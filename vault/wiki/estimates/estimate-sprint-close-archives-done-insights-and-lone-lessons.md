---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint-close]]"
purpose: At the close of a sprint its actioned Insights and its error lessons that joined no Insight go to the archive, and its knowledge lessons and open Insights stay
method: pytest .guppi/tests/test_sprint_close.py -k insights; by hand, the output of the preview uv run --project .guppi guppi sprint-close --sprint <id> over the live vault, <id> the sprint that vault/wiki/sprint.md names, read against the Then
checked: 2026-10-04
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [sprint, workflow]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi sprint-close --sprint <id> --apply` closes the sprint `entity-sprint-<id>` of the made-up vault of `.guppi/tests/test_sprint_close.py`, after each Estimate that `entity-sprint-<id>` lists and that does not stand `passed` is read or archived unread, as the person chooses; someone reads `vault/wiki/insights/`, `vault/wiki/lessons/` and `vault/archive/` after it.
**＋** Or the preview `uv run --project .guppi guppi sprint-close --sprint <id>` runs over the live vault, and someone reads its output against `vault/wiki/insights/` and `vault/wiki/lessons/`.

Then:
Each Insight under `vault/wiki/insights/` whose `sprint` is `<id>` and that stands `actioned` stands under `vault/archive/`.
**＋** Each lesson under `vault/wiki/lessons/` whose `sprint` is `<id>`, whose `kind` is `error` and that stands `new` stands under `vault/archive/`.
**＋** The preview names each such Insight and lesson among the pages the close would move, and moves none.
**－** A lesson whose `kind` is `knowledge` stays under `vault/wiki/lessons/`.
**－** An Insight that stands `open`, and each lesson its `children` lists, stay live.

## Result

2026-10-04, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
