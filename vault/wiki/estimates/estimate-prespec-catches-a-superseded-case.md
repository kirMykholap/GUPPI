---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: A supersedes of the session's window whose Case still stands in the plan is a finding of prespec --check; a line of the superseded Case needs no item
method: pytest tests/test_prespec.py on a temp plan; the live reading the first /pre-spec of a later session whose window holds a supersedes of a Case of that session — this session's /pre-spec runs on the old check
origin: raw/2026-09-21/1853/ledger.md#case-299.2
sprint: migration
created: 2026-09-21
tags: [harness, workflow]
---

## Criterion

Given:
`{supersedes:case N}` on a decision line marks every entry of Case N `superseded_by` in the yaml of any unit (175, 177); `generate` applies none of them and ticks none of their lines (151, 286); Retro does not count them (282).
**＋** The Spec of a session is the plan approved at the end of Plan Mode, copied to `raw/<date>/<hi HHMM>/spec.md` (73.1); `## Case N — …` or `### Case N.M — …` is a heading, its section runs to the next such heading.
**＋** `prespec --check` runs every record line of the session's window through `materialize.parse_line` (75.2) and prints a finding for a decision line whose Case has no heading in the plan (59.1).
**＋** `tests/test_prespec.py` fixes the behaviour on a temp plan.

When:
`/pre-spec` — `guppi prespec --check` on the plan of this Plan Mode.

Then:
A `{supersedes:case N}` in the session's window while `## Case N` or `### Case N` still stands in the plan is a finding `case N: superseded by case M, still in the plan`.
**＋** A decision line of Case N, N superseded by a line of the window, is no finding "no Case N heading" and needs no item in the plan.
**＋** A superseded sub-case: the one heading `### Case N.M` leaves; the parent with its other sub-cases stays.
**－** A `{supersedes:case N}` on a Case of an earlier session — a defer taken up — finds no heading N in the plan and is no finding.
**－** A Frontier line closed `· case N` with N superseded is a finding as today; the agent closes it with the superseding Case.
**－** Nothing else in pre-spec changes.

## Result

2026-09-21, uv run pytest tests/test_prespec.py 68 green, four new — a superseded Case still in the plan prints case 1: superseded by case 3, still in the plan; a line of the superseded Case with no heading is no finding, needs no item and no tasks block; a superseded sub-case leaves alone and its parent stays; a supersedes of an earlier session's Case prints nothing; live — the first /pre-spec of a later session whose window holds a supersedes of its own Case, not taken here: this session's /pre-spec ran on the old check

## History

- 2026-09-22 created · [[decision-case-299.2]]
- 2026-09-22 status: pending → passed · raw/2026-09-21/1853/ledger.md#L25
