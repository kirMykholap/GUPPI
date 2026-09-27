---
type: estimate
kind: QA
status: pending
target: "[[rule-prespec]]"
purpose: A Frontier line of the sprint closed by a Case is a finding of prespec --check unless that Case updates the sprint page; a line left [-] with sprint · defer needs nothing
method: uv run pytest tests/test_prespec.py -k sprint — a line `· sprint · case N` with and without an update of entity-sprint-<id> under Case N, a `[-] … · sprint · defer` line, a line whose source segment is not `sprint` while the word stands inside the slug of its title
checked: 2026-09-24
origin: raw/2026-09-22/1121/ledger.md#case-314.2
sprint: migration
created: 2026-09-22
tags: [harness, workflow, sprint]
---

## Criterion

When:
`uv run guppi prespec --check <plan>` reads a line of the session's Frontier whose source segment, the one before the closer, is `sprint`.

Then:
A line closed `[x] … · sprint · case N` needs an `update` item of `entity-sprint-<id>` under Case N, in the parent or in any sub-case. Without one, it is the finding `frontier: C<n> closes a sprint item with case N, no update of the sprint page under Case N`.
**＋** A line closed `[-] … · sprint · defer` needs nothing and is no finding. The item stays in its milestone until `generate` moves it to the `## Backlog` of `entity-sprint-<id>` after three such sessions in a row.
**－** A line whose source segment is not `sprint` is read by the other checks of the Frontier. The word inside the slug of a title is not the source.

## Result

2026-09-24, uv run pytest tests/test_prespec.py -k sprint: 7 passed, 101 deselected

## History

- 2026-09-22 created · [[decision-case-314.2]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L91
- 2026-09-23 updated: the Criterion and the method speak of the source segment of a Frontier line (case 344, supersedes 338.1) · [[decision-case-344]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/0034/ledger.md#L59
- 2026-09-23 updated: a sprint line put off needs nothing from prespec; the item stays until generate moves it (case 371) · [[decision-case-371]]
- 2026-09-24 status: pending → passed · raw/2026-09-24/1303/ledger.md#L23
- 2026-09-27 updated: the Criterion replaced whole — a sprint line put off closes [-] · sprint · defer (case 451.3) · [[decision-case-451.3]]
