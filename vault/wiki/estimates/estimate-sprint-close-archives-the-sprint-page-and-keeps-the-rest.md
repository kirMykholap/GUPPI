---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint-close]]"
purpose: At the close of a sprint the sprint page and its own Estimates go to the archive, and every other passed Estimate stays live
method: pytest tests/test_sprint_close.py -k sprint_page; by hand, the output of the preview uv run guppi sprint-close --sprint migration over the live vault read against the Then
checked: 2026-10-04
origin: raw/2026-10-03/0317/ledger.md#case-612.3
sprint: migration
created: 2026-10-03
tags: [sprint, workflow]
---

## Criterion

When:
`uv run guppi sprint-close --sprint <id> --apply` closes the sprint `entity-sprint-<id>` of the made-up vault of `tests/test_sprint_close.py`, after each Estimate that `entity-sprint-<id>` lists and that does not stand `passed` is read or archived unread, as the person chooses; someone reads `vault/wiki/entities/`, `vault/wiki/estimates/` and `vault/archive/` after it.
**＋** Or the preview `uv run guppi sprint-close --sprint <id>` runs over the live vault, and someone reads its output against `vault/wiki/entities/` and `vault/wiki/estimates/`.

Then:
`entity-sprint-<id>` and each Estimate its `estimates` lists stand under `vault/archive/`.
**＋** The preview names `entity-sprint-<id>` and each of those Estimates among the pages the close would move, and moves none.
**－** Every other Estimate that stands `passed` stays under `vault/wiki/estimates/`, and the rule or Entity that lists it keeps it in `estimates`.
**－** The close does not archive the MOC `entity-sprint`.

## Result

2026-10-04, at the /hi of session 2041: uv run pytest tests/test_sprint_close.py -k sprint_page 4 passed; the preview uv run guppi sprint-close --sprint migration over the live vault names to move entity-sprint-migration and the 6 Estimates its estimates lists, equal to the frontmatter; none of the 173 other passed Estimates and not entity-sprint; nothing moved

## History

- 2026-10-03 created · [[decision-case-612.3]]
- 2026-10-04 updated: the When replaced whole — the run with --apply over a made-up vault, after each Estimate of the sprint page not passed is read or archived unread, or the preview over the live vault; the Then kept, one line on the preview added; the method a pytest test and the preview of migration (case 627.3) · [[decision-case-627.3]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/2041/ledger.md#L3
