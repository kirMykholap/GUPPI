---
type: estimate
kind: QA
status: archived
target: "[[rule-case-check]]"
purpose: Whether the check of an answer of case-guppi that holds sub-cases alone judges their frame against the given of their stored parent, and gives the answer no finding of the parent itself
method: uv run pytest tests/test_casecheck.py -k lone
checked: 2026-10-05
origin: raw/2026-10-04/1439/ledger.md#case-629.3
sprint: migration
created: 2026-10-04
tags: [hooks, harness, workflow]
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` answers with sub-cases of a Case N alone, and `<plan>.checked.json` beside the plan file of the session holds Case N under its number alone.
**＋** Or `tests/test_casecheck.py` runs `uv run guppi casecheck --subagent` over such an answer and a made-up store.

Then:
The hook builds the Spec text it judges with the stored section of Case N before the sub-cases of the answer, so `prespec.judge` of `guppi/prespec.py` reads the `given` and `context` of Case N for a sub-case of the answer that has none of its own, as `/pre-spec` reads them in the plan.
**＋** A slug or a path in a code span of the `when` or `then` of such a sub-case, or a slug of its `then` block, that the `given` of Case N does not name is a finding of that sub-case, stored and sent back as any other finding.
**－** A finding or a note on Case N itself is not given to the answer, and Case N is neither stored nor written again from this answer.
**－** With no stored Case N, the sub-cases are judged alone, and a sub-case with no `given` of its own gets no finding on its frame.

## Result

2026-10-05, at the /hi of session 0109: uv run pytest -q tests/test_casecheck.py -k lone 11 passed, 119 deselected

## History

- 2026-10-04 created · [[decision-case-629.3]]
- 2026-10-05 updated: the method is pytest alone; the live send-back is no longer waited for (case 637.1) · [[decision-case-637.1]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/0109/ledger.md#L3
- 2026-10-05 deleted · [[decision-case-645.2]]
- 2026-10-05 archived · cleanup
