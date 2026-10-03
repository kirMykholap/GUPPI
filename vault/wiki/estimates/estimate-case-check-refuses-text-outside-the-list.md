---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the Stop run of the Case check refuses a reply that shows a Case with a text of the main agent's own before its first Case heading, under a heading outside the list and the ratification, or before the last tool call of the turn
method: uv run pytest tests/test_casecheck.py; by hand in a later session, the showings of Cases and the hook's refusals of them read in the transcript
checked: 2026-10-03
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
**－** On the re-fire (`stop_hook_active`) it exits 0, so the Case shown again after a refusal is not judged again.
**－** It stores nothing and writes no file.

## Result

2026-10-03, at the /hi of session 1416: `uv run pytest tests/test_casecheck.py` 117 passed; by hand, session 1341 (transcript 26e79919): Case 614 shown twice, at 14:05:27 and 14:12:13, each reply opening with its `## Case 614 —` heading, then list items, a line indented under a list item and the `ratification` blockquote, the agent's own text after `---`, and no text of the main agent before the last tool call of either turn; no refusal of `uv run guppi casecheck` in the session, the only two Stop refusals being `uv run guppi onward --plan` at 14:08:32 and 14:12:51; not exercised: a live refusal, since no showing held text outside the list

## History

- 2026-10-03 created · [[decision-case-611]]
- 2026-10-03 status: pending → passed · raw/2026-10-03/1416/ledger.md#L1
