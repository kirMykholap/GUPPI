---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: A Frontier line of the sprint closed by a Case is a finding of prespec --check unless that Case updates the sprint page; a line left [-] with sprint needs nothing
method: uv run pytest tests/test_prespec.py -k sprint — a line `· sprint · case N` with and without an update of entity-sprint-<id> under Case N, a `[-] … · sprint` line, a line whose source segment is not `sprint` while the word stands inside the slug of its title
checked: 2026-09-24
origin: raw/2026-09-22/1121/ledger.md#case-314.2
sprint: migration
created: 2026-09-22
tags: [harness, workflow, sprint]
---

## Criterion

Given:
`prespec.check_frontier` reads every line of the session's `frontier.md`, the closer the last segment after ` · `; the `then` blocks of the plan are parsed beside it.
**＋** The sprint page is the one live Entity whose slug starts with `entity-sprint-` (case 209.1).
**＋** `tests/test_prespec.py` fixes `--check`.

When:
`guppi prespec --check` reads a Frontier line whose source segment — the one before the closer — is `sprint` and whose closer is `case N`.

Then:
An `update` item naming the sprint page under Case N — the parent or any sub-case — is required; without one the finding is `frontier: C<n> closes a sprint item with case N, no update of <sprint slug> under Case N`.
**＋** A line closed `[-] … · sprint` needs nothing from `prespec`: no finding; the item stays in its milestone until `generate` moves it to the Backlog after three such sessions in a row (354.1).
**－** A line whose source segment is not `sprint` is read as today; the word inside the slug of a title is not the source (case 335).

## Result

2026-09-24, uv run pytest tests/test_prespec.py -k sprint: 7 passed, 101 deselected

## History

- 2026-09-22 created · [[decision-case-314.2]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L91
- 2026-09-23 updated: the Criterion and the method speak of the source segment of a Frontier line (case 344, supersedes 338.1) · [[decision-case-344]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/0034/ledger.md#L59
- 2026-09-23 updated: a sprint line put off needs nothing from prespec; the item stays until generate moves it (case 371) · [[decision-case-371]]
- 2026-09-24 status: pending → passed · raw/2026-09-24/1303/ledger.md#L23
