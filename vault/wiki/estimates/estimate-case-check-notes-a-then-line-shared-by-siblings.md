---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Two then lines of sibling sub-cases that share most of their words are a note of the answer of case-guppi and of pre-spec
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py .guppi/tests/test_prespec.py -k sibling
checked: 2026-10-15
origin: raw/2026-09-28/0000/ledger.md#case-472.2
sprint: migration
created: 2026-09-28
tags: [hooks, harness, workflow]
---

## Criterion

When:
`uv run --project .guppi guppi casecheck --subagent` checks an answer of `case-guppi` on `SubagentStop`, or `uv run --project .guppi guppi prespec --check <plan>` checks the plan, and the answer or the plan holds two or more sub-cases of one parent.

Then:
Two `then` lines of two sibling sub-cases (sub-cases of one parent, such as N.1 and N.2) are a note when the words that both lines hold make 60 percent or more of the words of the shorter line. A word is a run of letters and digits of four or more characters, and the case of letters is set aside.
**＋** The note names both Cases and both lines, and it goes where every other note of the check goes (the notes of case 472.1).
**－** A line with no word of four or more characters is compared with no line.
**－** A sub-case that the answer holds alone has no sibling in the answer and gets no note from `guppi casecheck`. `guppi prespec --check` compares it with its siblings in the plan.

## Result

2026-10-15, the Retro of session 1959: `uv run --project .guppi pytest -q .guppi/tests/test_casecheck.py .guppi/tests/test_prespec.py -k sibling` 6 passed, read on the Criterion of Case 823.2, which promises the note of the hook alone

## History

- 2026-09-28 created · [[decision-case-472.2]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L40
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 updated: the Criterion replaced whole — its pointer stands in a bracket, it promises the note of the hook alone, and the method keeps its pytest run alone · [[decision-case-823.2]]
- 2026-10-15 status: pending → passed · raw/2026-10-15/1959/ledger.md#L66
