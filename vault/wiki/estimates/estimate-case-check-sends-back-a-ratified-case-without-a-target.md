---
type: estimate
kind: QA
status: pending
target: "[[rule-case-check]]"
purpose: Whether a Case that has decision lines in the session and comes back from case-guppi under its number without the item of one of those lines goes back to case-guppi with a new number to build it under
method: uv run pytest tests/test_casecheck.py -k dropped_target
origin: raw/2026-10-05/1831/ledger.md#case-671.1
sprint: migration
created: 2026-10-05
tags: [hooks, harness, workflow]
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run guppi casecheck --subagent` of `guppi/casecheck.py` reads the Cases of that file and the decision lines of the session's `raw/<date>/<hi HHMM>/ledger.md`.

Then:
For each number of the family of a top-level Case N in the file that has a section in the file and no sub-case under it, the hook reads the decision lines of that number in the session's ledger, of a kind other than `defer`.
**＋** A line whose kind and slug has no item under that number, in the `then` block that the hook builds from the file, gives Case N a finding. The judgment of an item is `line_has_item` of `guppi/prespec.py`, imported.
**＋** The finding names the number and the line, and tells `case-guppi` to build the Case under the number that `new_number` of `guppi/casecheck.py` gives. Its decision lines carry one `{supersedes:case N}` for the number N, and one `{supersedes:case M}` for each number M of the family that has a decision line.
**＋** The hook exits 2 with the finding on stderr. `case-guppi` fixes the file by `Edit`: it puts the item back, or it changes the number in the headings and the ledger lines and adds the marks. It does not write the whole Case again.
**－** A `defer` line gives no finding of this check.
**－** A number with no section in the file, or with a sub-case in the file, gets no finding of this check.
**－** A Case whose items hold each decision line of its numbers gets no finding of this check, whatever items it adds.

## History

- 2026-10-05 created · [[decision-case-671.1]]
