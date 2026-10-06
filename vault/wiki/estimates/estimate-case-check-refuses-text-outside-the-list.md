---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the Stop run of the Case check refuses a reply that shows a Case with a text of the main agent's own before its first Case heading, under a heading outside the list and the ratification, or written after the summary of case-guppi came back and before the last tool call of the turn, judging only what follows its last refusal in the turn
method: uv run pytest tests/test_casecheck.py
checked: 2026-10-07
origin: raw/2026-10-03/0317/ledger.md#case-611
sprint: migration
created: 2026-10-03
tags: [hooks, harness, workflow]
---

## Criterion

When:
`Stop` fires after a reply of the main agent that shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections, not a deferred decision in the short form, and `uv run guppi casecheck` runs on it, as `.claude/settings.json` registers it.

Then:
`uv run guppi casecheck` exits 2 when a line that is not blank stands in the reply before its first Case heading.
**＋** It exits 2 when a line stands between a Case heading and the next Case heading or the horizontal rule `---` that is not blank, not a list item — a line that opens with `- `, `* ` or a number and `. ` — not a line indented under a list item, and not a line of the `ratification` blockquote, its `> **ratification:**` line and the `>` lines after it.
**＋** It exits 2 when the main agent wrote text in the turn of the reply after the first summary of `case-guppi` came back and before its last tool call; a summary is a text given back to an `Agent` or `SendMessage` call whose first line that is not blank opens with `**Built:**`, in the `tool_result` of an `Agent` call or in the returned answer that opens the turn.
**＋** When the turn holds a refusal of `uv run guppi casecheck`, judged by `refusals` of `guppi/ledger.py`, it judges only the texts after the last such refusal, so a Case shown again with no text of its own before its last tool call passes.
**＋** Its reason on stderr quotes the first such text and tells the agent to show the Case again with nothing of its own before it and its own text after the horizontal rule.
**＋** The check runs in the same `Stop` run as the comparison of shown Cases with the stored answer and the check of how a round opens, and a reply that more than one of them refuse gives each reason.
**－** A text the main agent wrote in the turn before the first summary came back is not judged, and a turn with no summary judges no text before its last tool call.
**－** Text after the horizontal rule is not judged.
**－** A reply with no Case heading that holds a section, the acknowledging reply among them, a fence tagged `DIFF`, and a deferred decision in the short form are not judged.
**－** With `stop_hook_active` set a Case shown again after a refusal is judged again, and the reason is given as `estimate-case-check-judges-a-showing-after-a-refusal` sets it.
**－** It stores nothing and writes no file.

## Result

2026-10-07, uv run pytest tests/test_casecheck.py: 164 passed; a text after the summary came back is refused with the reason to show the Case again with nothing of your own before it, a text before the call that brought the summary passes, a Case shown again after a refusal passes, a turn with no summary judges no text before its last call; the layout tests pass as before

## History

- 2026-10-03 created · [[decision-case-611]]
- 2026-10-03 status: pending → passed · raw/2026-10-03/1416/ledger.md#L1
- 2026-10-06 updated: the Criterion replaced whole — a Case shown again after a refusal is judged again, its reason given as the loop guard sets it; method set to the tests, which run in the session (case 688.6) · [[decision-case-688.6]]
- 2026-10-06 status: pending → passed · raw/2026-10-06/0104/ledger.md#L42
- 2026-10-07 updated: the Criterion replaced whole — only texts written after the summary came back and after the last refusal of the check are judged, so one showing again clears a refusal · [[decision-case-692.2]]
- 2026-10-07 status: pending → passed · raw/2026-10-06/1448/ledger.md#L20
