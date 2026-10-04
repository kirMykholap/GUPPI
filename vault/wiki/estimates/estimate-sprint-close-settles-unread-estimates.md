---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint-close]]"
purpose: At the close of a sprint each pending or failed Estimate is put to the person, who has it read, carries it into the next sprint or archives it unread, before any page moves; an Estimate of the sprint page is read or archived with the sprint page and never carried, and a reading that comes out failed settles its Estimate
method: pytest tests/test_sprint_close.py -k settle; by hand, the output of the preview uv run guppi sprint-close --sprint migration over the live vault read against the Then
checked: 2026-10-04
origin: raw/2026-10-03/0317/ledger.md#case-612.4
sprint: migration
created: 2026-10-03
tags: [sprint, workflow]
---

## Criterion

When:
`uv run guppi sprint-close --sprint <id>` closes the sprint `entity-sprint-<id>` of the made-up vault of `tests/test_sprint_close.py`, its preview first and then its run with `--apply`, after each Estimate that `entity-sprint-<id>` lists and that does not stand `passed` is read or archived unread, as the person chooses; someone reads the record of the close, `vault/wiki/estimates/` and `vault/archive/` after it.
**＋** Or the preview `uv run guppi sprint-close --sprint <id>` runs over the live vault, and someone reads its output against `vault/wiki/estimates/`.

Then:
Before any page of the close moves, the close lists to the person each Estimate under `vault/wiki/estimates/` that stands `pending` or `failed`.
**＋** For each listed Estimate the person chooses one way: read it now, carry it into the next sprint, or archive it unread.
**＋** An Estimate read now has its reading in the ledger.
**＋** An Estimate read now whose reading comes out `failed` counts as settled: it is carried into the next sprint, or, when `entity-sprint-<id>` lists it, it stands under `vault/archive/` with the sprint page; the record of the close keeps its status.
**＋** An Estimate carried into the next sprint stays under `vault/wiki/estimates/` with its status.
**＋** An Estimate archived unread stands under `vault/archive/`, and the page that listed it no longer lists it in `estimates`.
**－** No page of the close moves before the person has chosen for each listed Estimate.
**－** An Estimate that `entity-sprint-<id>` lists is not carried into the next sprint: the person reads it now or archives it unread.

## Result

2026-10-04, at the /hi of session 2041: uv run pytest tests/test_sprint_close.py -k settle 6 passed; the preview uv run guppi sprint-close --sprint migration over the live vault lists the 31 Estimates standing pending or failed under vault/wiki/estimates/, the same set as the frontmatter, each marked not settled with a line asking to read it now or name it by --carry or --archive-unread; git status clean after it

## History

- 2026-10-03 created · [[decision-case-612.4]]
- 2026-10-04 updated: the Criterion replaced whole — the run over a made-up vault or the preview over the live vault; an Estimate of the sprint page that has not passed is read or archived unread and never carried; a reading that comes out failed settles its Estimate, carried or archived with the sprint page; the method a pytest test and the preview of migration (case 627.4) · [[decision-case-627.4]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/2041/ledger.md#L4
