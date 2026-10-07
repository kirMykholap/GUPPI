---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the Stop run of the Case check lets through a reply that shows a round of case-guppi after a text of the main agent's own, and the run on UserPromptSubmit tells the agent of it at the person's next message, judging only what follows the last refusal in the turn, only the first line after pre-spec, and no turn with no round
method: uv run pytest tests/test_casecheck.py -k round
checked: 2026-10-07
origin: raw/2026-09-30/2356/ledger.md#case-562
sprint: migration
created: 2026-09-30
tags: [hooks, harness, workflow]
---

## Criterion

When:
A reply of the main agent shows a round of `case-guppi`, `Stop` fires and `uv run guppi casecheck` of `guppi/casecheck.py` runs on it. Then the person sends a message, and `uv run guppi casecheck --prompt` runs on `UserPromptSubmit`, as `.claude/settings.json` registers it.

Then:
At `Stop`, `uv run guppi casecheck` refuses no reply for the way it opens a round of `case-guppi`, or for a text of the main agent's own before the round. Its other reasons stand.
**＋** On `UserPromptSubmit`, `uv run guppi casecheck --prompt` judges the last reply of the main agent before the person's message, and the turn that reply ends. The turn holds a round when a text that `case-guppi` gave back in it is a round by `is_round` of `guppi/casecheck.py`.
**＋** It finds a fault when the first line of the reply that is not blank opens neither with `❓ ` nor with a bold label that ends in a colon. While the session's event log holds no `prespec` line of this session after its `hi`, it also finds a fault when the main agent wrote text in the turn after the first round came back and before its last tool call. It judges only the texts after the reply that the last refusal of `uv run guppi casecheck` in the turn follows, judged by `refusals` of `guppi/ledger.py`.
**＋** On a fault it prints one line to stdout, which reaches the agent's context. The line quotes the text before the round, says that the round stands as shown and is not shown again, and tells the agent to open the next round with its Context paragraph or its first question, with nothing before it.
**＋** `.claude/settings.json` registers `uv run guppi casecheck --prompt` on `UserPromptSubmit`, as `rule-hook-registry` renders it.
**－** With no fault, in a turn with no round, and for text after the last question, it prints nothing.
**－** It exits 0 always and never blocks the person's message. An error of its own goes to stderr.
**－** The person sees nothing of the note. It stores nothing and writes no file.
**－** The refusals of the `Stop` run are counted as `estimate-case-check-judges-a-showing-after-a-refusal` sets it, and a layout fault of a round is not one of them.

## Result

2026-10-07, uv run pytest tests/test_casecheck.py -k round: 43 passed; the Stop run lets a round after a text of the agent's own through, casecheck --prompt prints one note on stdout and exits 0, a round with nothing before it, a turn with no round and an unreadable payload print nothing; the UserPromptSubmit registration stands in the new text of rule-hook-registry in the Spec, its anchor once on the page

## History

- 2026-10-01 created · [[decision-case-562]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L29
- 2026-10-01 updated: the Criterion replaced whole — the same behaviour, with the true reason for the exemption after /pre-spec (case 581.2) · [[decision-case-581.2]]
- 2026-10-02 updated: the Criterion replaced whole — the turn of the reply starts at the person's message or a returned answer, by the function of guppi/ledger.py (case 590.3) · [[decision-case-590.3]]
- 2026-10-03 updated: the Criterion replaced whole — a round is known by is_round, the one test of a round (case 601.4) · [[decision-case-601.4]]
- 2026-10-03 status: pending → passed · raw/2026-10-03/0115/ledger.md#L15
- 2026-10-06 updated: the Criterion replaced whole — a round shown again after a refusal is judged again, its reason given as the loop guard sets it; method set to the tests, which run in the session (case 688.5) · [[decision-case-688.5]]
- 2026-10-06 status: pending → passed · raw/2026-10-06/0104/ledger.md#L41
- 2026-10-07 updated: the Criterion replaced whole — only texts written after the round came back and after the last refusal of the check are judged, so one showing again clears a refusal · [[decision-case-692.1]]
- 2026-10-07 status: pending → passed · raw/2026-10-06/1448/ledger.md#L19
- 2026-10-07 updated: the Criterion replaced whole — the Stop run lets a layout fault of a round through, and casecheck --prompt tells the agent at the next message; purpose set anew · [[decision-case-699.1]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/0211/ledger.md#L41
