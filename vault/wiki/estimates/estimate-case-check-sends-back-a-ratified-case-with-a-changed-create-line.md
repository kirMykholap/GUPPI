---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether a Case that has a create line in the session and comes back from case-guppi under its number with another ref or another set of tags on that line goes back to case-guppi with a new number to build it under
method: uv run pytest tests/test_casecheck.py -k changed_create_line
origin: raw/2026-10-09/0200/ledger.md#case-749
sprint: migration
created: 2026-10-09
tags: [hooks, harness, workflow]
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run guppi casecheck --subagent` of `guppi/casecheck.py` reads the Cases of that file, the decision lines of their `ratification`, and the decision lines of the session's `raw/<date>/<hi HHMM>/ledger.md`.

Then:
For each number of the family of a top-level Case N in the file that has a section in the file and no sub-case under it, the hook reads the `create` lines of that number in the session's ledger.
**＋** A `create` line of the ledger gives Case N a finding when the `ratification` of that number in the file holds a `create` line of the same slug whose `ref` differs, or whose tags differ by a tag added or removed.
**＋** The finding names the number, the slug and both lines, and the number that `new_number` of `guppi/casecheck.py` gives. It also names the marks: one `{supersedes:case N}` for the number N, and one `{supersedes:case M}` for each number M of the family that has a decision line.
**＋** The hook exits 2 with the finding on stderr. `case-guppi` fixes the file by `Edit`: it writes the line back as the ledger holds it, or it changes the number in the headings and the ledger lines and adds the marks. It does not write the whole Case again.
**－** The same tags in another order, and a line that differs only by a `{supersedes}` or `{addresses}` mark, give no finding of this check.
**－** A `create` line of the ledger whose slug has no `create` line under that number in the file gives no finding of this check.
**－** An `update`, `delete` or `defer` line gives no finding of this check.
**－** A number with no section in the file, or with a sub-case in the file, gets no finding of this check.

## Result

2026-10-09, Retro, uv run pytest tests/test_casecheck.py -k changed_create_line: 7 passed

## History

- 2026-10-09 created · [[decision-case-749]]
- 2026-10-09 status: pending → passed · raw/2026-10-09/0200/ledger.md#L22
