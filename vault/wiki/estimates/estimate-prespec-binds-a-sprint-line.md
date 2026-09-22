---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: A Frontier line of the sprint closed by a Case is a finding of prespec --check unless that Case updates the sprint page; a line left [-] with sprint needs nothing
method: uv run pytest tests/test_prespec.py -k sprint — a line `· sprint · case N` with and without an update of entity-sprint-<id> under Case N, a `[-] … · sprint` line, a line without sprint among its segments
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
`guppi prespec --check` reads a Frontier line whose segments hold `sprint` and whose closer is `case N`.

Then:
An `update` item naming the sprint page under Case N — the parent or any sub-case — is required; without one the finding is `frontier: C<n> closes a sprint item with case N, no update of <sprint slug> under Case N`.
**＋** A line closed `[-] … · sprint` needs nothing: the item stays on the page as it is.
**－** A line without `sprint` among its segments is read as today.

## Result

2026-09-22, uv run pytest tests/test_prespec.py -k sprint: 5 passed, 68 deselected

## History

- 2026-09-22 created · [[decision-case-314.2]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L91
