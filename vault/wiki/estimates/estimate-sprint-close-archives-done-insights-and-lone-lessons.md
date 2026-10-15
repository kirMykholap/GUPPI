---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint-close]]"
purpose: At the close of a sprint its actioned Insights and its error lessons that joined no Insight go to the archive, and its knowledge lessons and open Insights stay
method: pytest .guppi/tests/test_sprint_close.py -k insights; by hand, the output of the preview uv run --project .guppi guppi sprint-close --sprint migration over the live vault read against the Then
checked: 2026-10-04
origin: raw/2026-10-03/0317/ledger.md#case-612.2
sprint: migration
created: 2026-10-03
tags: [sprint, workflow]
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

2026-10-04, at the /hi of session 2041: uv run pytest tests/test_sprint_close.py -k insights 1 passed; the preview uv run guppi sprint-close --sprint migration over the live vault names to move the 25 actioned Insights of the sprint and the 42 error lessons of the sprint standing new that no open Insight lists, both sets equal to the frontmatter; none of the 26 knowledge lessons, the 5 open Insights or the 34 lessons their children list is among the moves; nothing moved

## History

- 2026-10-03 created · [[decision-case-612.2]]
- 2026-10-04 updated: the When replaced whole — the run with --apply over a made-up vault, after each Estimate of the sprint page not passed is read or archived unread, or the preview over the live vault; the Then kept, one line on the preview added; the method a pytest test and the preview of migration (case 627.2) · [[decision-case-627.2]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/2041/ledger.md#L2
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
