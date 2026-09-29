---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Two then lines of sibling sub-cases that share most of their words are a note of the answer of case-guppi and of pre-spec
method: uv run pytest tests/test_casecheck.py tests/test_prespec.py -k sibling, then by hand the first sibling note the hook sends back to case-guppi
checked: 2026-09-29
origin: raw/2026-09-28/0000/ledger.md#case-472.2
sprint: migration
created: 2026-09-28
tags: [hooks, harness, workflow]
---

## Criterion

When:
`uv run guppi casecheck --subagent` checks an answer of `case-guppi` on `SubagentStop`, or `uv run guppi prespec --check <plan>` checks the plan, and the answer or the plan holds two or more sub-cases of one parent.

Then:
Two `then` lines of two sibling sub-cases (sub-cases of one parent, such as N.1 and N.2) are a note when the words that both lines hold make 60 percent or more of the words of the shorter line. A word is a run of letters and digits of four or more characters, and the case of letters is set aside.
**＋** The note names both Cases and both lines, and it is a note in the sense of case 472.1: it goes where that Case sends a note. `case-guppi` signs the promise in one sub-case, or it keeps both lines and says why in `context`.
**－** A line with no word of four or more characters is compared with no line.
**－** A sub-case that the answer holds alone has no sibling in the answer and gets no note from `guppi casecheck`. `guppi prespec --check` compares it with its siblings in the plan.

## Result

2026-09-29, uv run pytest tests/test_casecheck.py tests/test_prespec.py -k sibling: 6 passed; by hand, session 1134: the check noted then lines of 506.2 and 506.3 shared with 506.1, and case-guppi kept both and said why in context

## History

- 2026-09-28 created · [[decision-case-472.2]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L40
