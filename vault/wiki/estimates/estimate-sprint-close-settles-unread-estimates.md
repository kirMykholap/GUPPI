---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint-close]]"
purpose: At the close of a sprint each pending or failed Estimate is put to the person, who has it read, carries it into the next sprint or archives it unread, before any page moves; an Estimate of the sprint page is read or archived unread and never carried, one that stands failed too; no listed Estimate is settled until the close names it
method: pytest .guppi/tests/test_sprint_close.py -k settle
checked: 2026-11-25
origin: raw/2026-10-03/0317/ledger.md#case-612.4
sprint: migration
created: 2026-10-03
tags: [sprint, workflow]
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

2026-11-25, Retro of session 0816, `uv run --project .guppi pytest .guppi/tests/test_sprint_close.py -k settle`: 6 passed, 16 deselected; `test_settle_failed_sprint_page_estimate_only_by_archive_unread` refuses an unnamed failed Estimate of the sprint page, moving nothing, and archives it by --archive-unread; the preview `uv run --project .guppi guppi sprint-close --sprint plugin` over the live vault printed 30 unread lines, and a Grep of status pending or failed under vault/wiki/estimates/ counted 30 files; estimate-sprint-plugin-frontierguard-build-read-its-folders-readers stands failed · not settled, with the refusal "read it now or name it by --archive-unread"

## History

- 2026-10-03 created · [[decision-case-612.4]]
- 2026-10-04 updated: the Criterion replaced whole — the run over a made-up vault or the preview over the live vault; an Estimate of the sprint page that has not passed is read or archived unread and never carried; a reading that comes out failed settles its Estimate, carried or archived with the sprint page; the method a pytest test and the preview of migration (case 627.4) · [[decision-case-627.4]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/2041/ledger.md#L4
- 2026-10-10 updated: the Criterion replaced whole — a failed Estimate outside the sprint page is settled only when --carry or --archive-unread names it, as guppi/sprint_close.py does; the purpose set anew; the method the pytest run alone, since no sprint page is live to preview · [[decision-case-763.1]]
- 2026-10-10 status: pending → passed · raw/2026-10-10/1713/ledger.md#L21
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-11-25 updated: the Criterion replaced whole — a failed Estimate of the sprint page is settled only by --archive-unread · [[decision-case-1057.3]]
- 2026-11-25 status: pending → passed · raw/2026-11-25/0816/ledger.md#L31
