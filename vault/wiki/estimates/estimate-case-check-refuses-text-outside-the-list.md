---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the Stop run of the Case check lets through a reply that shows a Case with a text of the main agent's own before its first Case heading, outside its list and its ratification, or written after the summary of case-guppi came back, and the run on UserPromptSubmit tells the agent of it at the person's next message, judging only what follows the last refusal in the turn
method: uv run pytest tests/test_casecheck.py
checked: 2026-10-07
origin: raw/2026-10-03/0317/ledger.md#case-611
sprint: migration
created: 2026-10-03
tags: [hooks, harness, workflow]
---

## Criterion

When:
A reply of the main agent shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections, not a deferred decision in the short form. `Stop` fires and `uv run guppi casecheck` of `guppi/casecheck.py` runs on it. Then the person sends a message, and `uv run guppi casecheck --prompt` runs on `UserPromptSubmit`, as `.claude/settings.json` registers it.

Then:
At `Stop`, `uv run guppi casecheck` refuses no showing for a text of the main agent's own before its first Case heading, outside its list and its `ratification`, or written after the summary of `case-guppi` came back.
**＋** It still refuses a shown Case that differs from the checked text, or whose file was not sent or differs from the store, as `estimate-case-check-shows-only-the-checked-case` sets it.
**＋** On `UserPromptSubmit`, `uv run guppi casecheck --prompt` judges the last reply of the main agent before the person's message, and the turn that reply ends, when that reply shows a Case.
**＋** It finds a fault when a line that is not blank stands before the first Case heading. It finds a fault when a line between a Case heading and the next Case heading or the horizontal rule `---` is not blank, not a list item — a line that opens with `- `, `* ` or a number and `. ` — not a line indented under a list item, and not a line of the `ratification` blockquote. It finds a fault when the main agent wrote text in the turn after the first summary of `case-guppi` came back — a text given back whose first line that is not blank opens with `**Built:**` — and before its last tool call. It judges only the texts after the reply that the last refusal of `uv run guppi casecheck` in the turn follows, judged by `refusals` of `guppi/ledger.py`.
**＋** On a fault it prints one line to stdout, which reaches the agent's context. The line quotes the first such text, says that the Case stands as shown and is not shown again, and tells the agent to write nothing of its own before the Case and to keep its own text after the horizontal rule at the next showing.
**－** A text written before the first summary came back, text after the horizontal rule, a reply with no Case heading that holds a section, a fence tagged `DIFF` and a deferred decision in the short form are not judged, and it prints nothing for them.
**－** It exits 0 always and never blocks the person's message. An error of its own goes to stderr.
**－** The person sees nothing of the note. It stores nothing and writes no file.

## Result

2026-10-07, uv run pytest tests/test_casecheck.py: 169 passed; a text before the heading, outside the list or after the summary came back passes the Stop run and gets the note of casecheck --prompt; a showing with no file sent is still refused at Stop

## History

- 2026-10-03 created · [[decision-case-611]]
- 2026-10-03 status: pending → passed · raw/2026-10-03/1416/ledger.md#L1
- 2026-10-06 updated: the Criterion replaced whole — a Case shown again after a refusal is judged again, its reason given as the loop guard sets it; method set to the tests, which run in the session (case 688.6) · [[decision-case-688.6]]
- 2026-10-06 status: pending → passed · raw/2026-10-06/0104/ledger.md#L42
- 2026-10-07 updated: the Criterion replaced whole — only texts written after the summary came back and after the last refusal of the check are judged, so one showing again clears a refusal · [[decision-case-692.2]]
- 2026-10-07 status: pending → passed · raw/2026-10-06/1448/ledger.md#L20
- 2026-10-07 updated: the Criterion replaced whole — the Stop run lets a layout fault of a Case through, and casecheck --prompt tells the agent at the next message; purpose set anew · [[decision-case-699.2]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/0211/ledger.md#L42
