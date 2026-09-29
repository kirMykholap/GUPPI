---
type: estimate
kind: QA
status: pending
target: "[[rule-prespec]]"
purpose: The Frontier of the session exists and every closed line has a box and a closer that agree with its source
method: uv run pytest tests/test_prespec.py
checked: 2026-09-27
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
**＋** An open line under `## Cases` is a finding. An open line under `## Work` or `## Ask` is not.
**＋** A closed line whose last segment after ` · ` is none of `case N`, `work`, `defer`, `kept` and `defer case N` is a finding.
**＋** These pairings of box and closer are findings: `[x]` with `defer`, `kept` or `defer case N`, and `[-]` with `case N` or `work`.
**＋** `defer` is clean only after the source segment `sprint`, the segment before the closer. `kept` is clean only after the source `backlog`. After any other source, each one is a finding.
**＋** `defer case N` after the source `sprint` or `backlog` is a finding. After another source, it is a finding when there is no `defer` item under Case N.
**＋** A line closed `case N` is a finding when the plan has no heading of Case N.
**－** A line that is not a box line, such as `Backlog: N items` or an indented `- near` line, is not read. No line of another session's Frontier file is read.

## Result

2026-09-27, uv run pytest tests/test_prespec.py: 144 passed

## History

- 2026-09-25 created · [[decision-case-399.3]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L39
- 2026-09-25 updated: the Criterion replaced whole — the closer kept (case 421.3) · [[decision-case-421.3]]
- 2026-09-25 status: pending → passed · raw/2026-09-25/1654/ledger.md#L31
- 2026-09-27 updated: the Criterion replaced whole — the box, the closer and the source checked both ways (case 451.2) · [[decision-case-451.2]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/1819/ledger.md#L27
- 2026-09-30 updated: the Criterion replaced whole — an open line under ## Ask is no finding, as one under ## Work (case 531.12) · [[decision-case-531.12]]
