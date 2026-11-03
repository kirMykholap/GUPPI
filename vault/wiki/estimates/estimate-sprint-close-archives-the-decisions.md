---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint-close]]"
purpose: At the close of a sprint its Decision pages go to the archive, but those a live page names in deferred_by or addressed_by
method: pytest .guppi/tests/test_sprint_close.py -k decisions; by hand, the output of the preview uv run --project .guppi guppi sprint-close --sprint <id> over the live vault, <id> the sprint that vault/wiki/sprint.md names, read against the Then
checked: 2026-10-04
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [sprint, workflow]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi sprint-close --sprint <id> --apply` closes the sprint `entity-sprint-<id>` of the made-up vault of `.guppi/tests/test_sprint_close.py`, after each Estimate that `entity-sprint-<id>` lists and that does not stand `passed` is read or archived unread, as the person chooses; someone reads `vault/wiki/decisions/` and `vault/archive/` after it.
**＋** Or the preview `uv run --project .guppi guppi sprint-close --sprint <id>` runs over the live vault, and someone reads its output against `vault/wiki/decisions/`.

Then:
Each Decision page under `vault/wiki/decisions/` whose `sprint` is `<id>` stands under `vault/archive/`.
**＋** The preview names each such page among the pages the close would move, and moves none.
**－** A Decision page that a live page names in `deferred_by` or `addressed_by` stays under `vault/wiki/decisions/`.
**－** A Decision page whose `sprint` is another sprint does not move.

## Result

2026-10-04, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
