---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint-close]]"
purpose: At the close of a sprint its Decision pages go to the archive, but those a live page names in deferred_by or addressed_by
method: pytest .guppi/tests/test_sprint_close.py -k decisions; by hand, the output of the preview uv run --project .guppi guppi sprint-close --sprint migration over the live vault read against the Then
checked: 2026-10-04
origin: raw/2026-10-03/0317/ledger.md#case-612.1
sprint: migration
created: 2026-10-03
tags: [sprint, workflow]
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

2026-10-04, at the /hi of session 2041: uv run pytest tests/test_sprint_close.py -k decisions 1 passed; the preview uv run guppi sprint-close --sprint migration over the live vault, exit 0, git status clean after it, read by a script against the frontmatter of vault/wiki/: 1055 Decision pages stand sprint migration and none another sprint; the preview names 1043 of them to move, the same set as those that no page staying live names in deferred_by or addressed_by, and keeps the other 12, each with the page that names it; 24 of the 1043 are named only in addressed_by of an actioned Insight that moves with them

## History

- 2026-10-03 created · [[decision-case-612.1]]
- 2026-10-04 updated: the When replaced whole — the run with --apply over a made-up vault, after each Estimate of the sprint page not passed is read or archived unread, or the preview over the live vault; the Then kept, one line on the preview added; the method a pytest test and the preview of migration (case 627.1) · [[decision-case-627.1]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/2041/ledger.md#L1
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
