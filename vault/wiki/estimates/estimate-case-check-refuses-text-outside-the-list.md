---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the Stop run of the Case check refuses a reply that shows a Case with a text of the main agent's own before its first Case heading, under a heading outside the list and the ratification, or before the last tool call of the turn
method: uv run pytest tests/test_casecheck.py
checked: 2026-10-06
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
**＋** It exits 2 when the main agent wrote text in the turn of the reply before its last tool call, judged by `texts_before_last_call` of `guppi/casecheck.py`, the judgment the check of a round uses.
**＋** Its reason on stderr quotes the first such text and tells the agent to show the Case again with that text moved after the horizontal rule.
**＋** The check runs in the same `Stop` run as the comparison of shown Cases with the stored answer and the check of how a round opens, and a reply that more than one of them refuse gives each reason.
**－** Text after the horizontal rule is not judged.
**－** A reply with no Case heading that holds a section, the acknowledging reply among them, a fence tagged `DIFF`, and a deferred decision in the short form are not judged.
**－** With `stop_hook_active` set a Case shown again after a refusal is judged again, and the reason is given as `estimate-case-check-judges-a-showing-after-a-refusal` sets it.
**－** It stores nothing and writes no file.

## Result

2026-10-06, uv run pytest tests/test_casecheck.py: 157 passed; a showing with own text before its heading is refused with the flag set after another hook's refusal, and the acknowledging reply is not judged

## History

- 2026-10-03 created · [[decision-case-611]]
- 2026-10-03 status: pending → passed · raw/2026-10-03/1416/ledger.md#L1
- 2026-10-06 updated: the Criterion replaced whole — a Case shown again after a refusal is judged again, its reason given as the loop guard sets it; method set to the tests, which run in the session (case 688.6) · [[decision-case-688.6]]
- 2026-10-06 status: pending → passed · raw/2026-10-06/0104/ledger.md#L42
