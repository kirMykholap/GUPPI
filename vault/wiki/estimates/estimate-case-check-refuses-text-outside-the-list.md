---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the Stop run of the Case check lets through a reply that shows a Case with a text of the main agent's own before its first Case heading, outside its list and its ratification, or written after the summary of case-guppi came back, and the run on UserPromptSubmit tells the agent of it at the person's next message, judging only what follows the last refusal in the turn
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py
checked: 2026-10-09
origin: raw/2026-10-03/0317/ledger.md#case-611
sprint: migration
created: 2026-10-03
tags: [hooks, harness, workflow]
---

## Criterion

When:
A reply of the main agent shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections, not a deferred decision in the short form. `Stop` fires and `uv run --project .guppi guppi casecheck` of `.guppi/guppi/casecheck.py` runs on it. Then the person sends a message, and `uv run --project .guppi guppi casecheck --prompt` runs on `UserPromptSubmit`, as `.claude/settings.json` registers it.

Then:
At `Stop`, `uv run --project .guppi guppi casecheck` refuses no showing for a text of the main agent's own before its first Case heading, outside its list and its `ratification`, or written after the summary of `case-guppi` came back.
**＋** It still refuses a shown Case that differs from the checked text, or whose file was not sent or differs from the store, as `estimate-case-check-shows-only-the-checked-case` sets it.
**＋** On `UserPromptSubmit`, `uv run --project .guppi guppi casecheck --prompt` judges the last reply of the main agent before the person's message, and the turn that reply ends, when that reply shows a Case.
**＋** It finds a fault when a line that is neither blank nor the horizontal rule `---` stands before the first Case heading. It finds a fault when a line between a Case heading and the next Case heading or the horizontal rule `---` is not blank, not a list item — a line that opens with `- `, `* ` or a number and `. ` — not a line indented under a list item, and not a line of the `ratification` blockquote.
**＋** A horizontal rule `---` whose next line that is not blank is a Case heading ends one Case, and the judgment goes on under that heading, so each Case of a batch is judged.
**＋** It finds a fault when the main agent wrote text in the turn after the first summary of `case-guppi` came back — a text given back whose first line that is not blank opens with `**Built:**` — and before its last tool call. It judges only the texts after the reply that the last refusal of `uv run --project .guppi guppi casecheck` in the turn follows, judged by `refusals` of `.guppi/guppi/ledger.py`.
**＋** On a fault it prints one line to stdout, which reaches the agent's context. The line quotes the first such text, says that the Case stands as shown and is not shown again, and tells the agent to write nothing of its own before the Case but a horizontal rule and to keep its own text after the horizontal rule at the next showing.
**－** A showing with no rule before its first Case heading, or with no rule between two Cases, gets no note for it.
**－** A text written before the first summary came back, text after a horizontal rule that no Case heading follows, a reply with no Case heading that holds a section, a fence tagged `DIFF` and a deferred decision in the short form are not judged, and it prints nothing for them.
**－** It exits 0 always and never blocks the person's message. An error of its own goes to stderr.
**－** The person sees nothing of the note. It stores nothing and writes no file.

## Result

2026-10-09, `uv run pytest tests/test_casecheck.py -q -k layout`: 15 passed, among them the three tests of case 751.5 (rules before and between the Cases of a batch, a text in the second Case after a rule, text after a last rule), which failed on the code before commit a80b1dc9

## History

- 2026-10-03 created · [[decision-case-611]]
- 2026-10-03 status: pending → passed · raw/2026-10-03/1416/ledger.md#L1
- 2026-10-06 updated: the Criterion replaced whole — a Case shown again after a refusal is judged again, its reason given as the loop guard sets it; method set to the tests, which run in the session (case 688.6) · [[decision-case-688.6]]
- 2026-10-06 status: pending → passed · raw/2026-10-06/0104/ledger.md#L42
- 2026-10-07 updated: the Criterion replaced whole — only texts written after the summary came back and after the last refusal of the check are judged, so one showing again clears a refusal · [[decision-case-692.2]]
- 2026-10-07 status: pending → passed · raw/2026-10-06/1448/ledger.md#L20
- 2026-10-07 updated: the Criterion replaced whole — the Stop run lets a layout fault of a Case through, and casecheck --prompt tells the agent at the next message; purpose set anew · [[decision-case-699.2]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/0211/ledger.md#L42
- 2026-10-09 updated: the Criterion replaced whole — a horizontal rule before the first Case and between two Cases is no text outside the list, and each Case of a batch is judged · [[decision-case-751.5]]
- 2026-10-09 status: pending → passed · raw/2026-10-09/2049/ledger.md#L18
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
