---
type: estimate
kind: QA
status: pending
target: "[[rule-sprint-close]]"
purpose: At the close of a sprint its Decision pages go to the archive, but those a live page names in deferred_by or addressed_by
method: pytest tests/test_sprint_close.py -k decisions; by hand, the output of the preview uv run guppi sprint-close --sprint migration over the live vault read against the Then
origin: raw/2026-10-03/0317/ledger.md#case-612.1
sprint: migration
created: 2026-10-03
tags: [sprint, workflow]
---

## Criterion

When:
`uv run guppi sprint-close --sprint <id> --apply` closes the sprint `entity-sprint-<id>` of the made-up vault of `tests/test_sprint_close.py`, after each Estimate that `entity-sprint-<id>` lists and that does not stand `passed` is read or archived unread, as the person chooses; someone reads `vault/wiki/decisions/` and `vault/archive/` after it.
**＋** Or the preview `uv run guppi sprint-close --sprint <id>` runs over the live vault, and someone reads its output against `vault/wiki/decisions/`.

Then:
Each Decision page under `vault/wiki/decisions/` whose `sprint` is `<id>` stands under `vault/archive/`.
**＋** The preview names each such page among the pages the close would move, and moves none.
**－** A Decision page that a live page names in `deferred_by` or `addressed_by` stays under `vault/wiki/decisions/`.
**－** A Decision page whose `sprint` is another sprint does not move.

## History

- 2026-10-03 created · [[decision-case-612.1]]
- 2026-10-04 updated: the When replaced whole — the run with --apply over a made-up vault, after each Estimate of the sprint page not passed is read or archived unread, or the preview over the live vault; the Then kept, one line on the preview added; the method a pytest test and the preview of migration (case 627.1) · [[decision-case-627.1]]
