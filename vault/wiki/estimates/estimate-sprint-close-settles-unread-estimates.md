---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint-close]]"
purpose: At the close of a sprint each pending or failed Estimate is put to the person, who has it read, carries it into the next sprint or archives it unread, before any page moves; an Estimate of the sprint page is read or archived with the sprint page and never carried, and one that stands failed goes with the sprint page; any other Estimate, one whose reading came out failed included, is settled only when the close names it to be carried or archived
method: pytest .guppi/tests/test_sprint_close.py -k settle
checked: 2026-10-10
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [sprint, workflow]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi sprint-close --sprint <id>` closes the sprint `entity-sprint-<id>` of the made-up vault of `.guppi/tests/test_sprint_close.py`, its preview first and then its run with `--apply`, after each Estimate that `entity-sprint-<id>` lists and that does not stand `passed` is read or archived unread, as the person chooses; someone reads the record of the close, `vault/wiki/estimates/` and `vault/archive/` after it.
**＋** Or the preview `uv run --project .guppi guppi sprint-close --sprint <id>` runs over the live vault, and someone reads its output against `vault/wiki/estimates/`.

Then:
Before any page of the close moves, the close lists to the person each Estimate under `vault/wiki/estimates/` that stands `pending` or `failed`.
**＋** For each listed Estimate the person chooses one way: read it now, carry it into the next sprint, or archive it unread.
**＋** An Estimate read now has its reading in the ledger.
**＋** A listed Estimate that `entity-sprint-<id>` lists and that stands `failed` counts as settled: it stands under `vault/archive/` with the sprint page, and the record of the close keeps its status.
**＋** A listed Estimate that `entity-sprint-<id>` does not list counts as settled only when the close names it by `--carry` or `--archive-unread`, also when a reading read now came out `failed`.
**＋** An Estimate carried into the next sprint stays under `vault/wiki/estimates/` with its status.
**＋** An Estimate archived unread stands under `vault/archive/`, and the page that listed it no longer lists it in `estimates`.
**－** No page of the close moves before the person has chosen for each listed Estimate.
**－** An Estimate that `entity-sprint-<id>` lists is not carried into the next sprint: the person reads it now or archives it unread.

## Result

2026-10-10, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
