---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint-close]]"
purpose: At the close of a sprint each pending or failed Estimate is put to the person, who has it read, carries it into the next sprint or archives it unread, before any page moves; an Estimate of the sprint page is read or archived unread and never carried, one that stands failed too; no listed Estimate is settled until the close names it
method: pytest .guppi/tests/test_sprint_close.py -k settle
checked: 2026-11-25
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [sprint, workflow]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi sprint-close --sprint <id>` closes the sprint `entity-sprint-<id>` of the made-up vault of `.guppi/tests/test_sprint_close.py`, its preview first and then its run with `--apply`; someone reads its output, the record of the close, `vault/wiki/estimates/` and `vault/archive/` after it.
**＋** Or the preview `uv run --project .guppi guppi sprint-close --sprint <id>` runs over the live vault, and someone reads its output against `vault/wiki/estimates/`.

Then:
Before any page of the close moves, the close lists to the person each Estimate under `vault/wiki/estimates/` that stands `pending` or `failed`.
**＋** For each listed Estimate the person chooses one way: read it now, carry it into the next sprint, or archive it unread.
**＋** A listed Estimate counts as settled only when the close names it by `--carry` or `--archive-unread`, one that `entity-sprint-<id>` lists and that stands `failed` included.
**＋** The run with `--apply` refuses, moving nothing, while a listed Estimate is not settled.
**＋** An Estimate carried into the next sprint stays under `vault/wiki/estimates/` with its status.
**＋** An Estimate archived unread stands under `vault/archive/`, its old status kept in its History, and the page that listed it no longer lists it in `estimates`.
**－** An Estimate that `entity-sprint-<id>` lists is not carried into the next sprint: the person reads it now or archives it unread.

## Result

2026-11-25, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
