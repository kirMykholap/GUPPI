---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: The Frontier of the session exists, and every closed line names a closer the plan bears out
method: uv run pytest tests/test_prespec.py
checked: 2026-09-24
origin: raw/2026-09-24/1916/ledger.md#case-399.3
sprint: migration
created: 2026-09-24
tags: [session, workflow, harness]
---

## Criterion

When:
`uv run guppi prespec --check <plan>` reads the session's `vault/raw/<date>/<HHMM>/frontier.md`.

Then:
A missing file is the finding `frontier: <path> is missing`.
**＋** A closed line whose last segment after ` · ` is none of `case N`, `work`, `sprint`, `defer case N` is a finding.
**＋** A line closed `case N` with no heading of Case N in the plan is a finding; one closed `defer case N` with no `defer` item under Case N is a finding.
**＋** A line closed `[x]` with `sprint` is a finding.

## Result

2026-09-24, `uv run pytest tests/test_prespec.py`: 108 passed

## History

- 2026-09-25 created · [[decision-case-399.3]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L39
