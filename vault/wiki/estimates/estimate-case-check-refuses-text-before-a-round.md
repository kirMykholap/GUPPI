---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the Stop run of the Case check refuses a reply that shows a round of case-guppi after a text of the main agent's own written after the round came back, judges only what follows its last refusal in the turn, judges only the first line of the reply after pre-spec, and leaves a turn with no round alone
method: uv run pytest tests/test_casecheck.py -k round
checked: 2026-10-07
origin: raw/2026-09-30/2356/ledger.md#case-562
sprint: migration
created: 2026-09-30
tags: [hooks, harness, workflow]
---

## Criterion

When:
`Stop` fires after a reply of the main agent, and `uv run guppi casecheck` runs on it.

Then:
When the turn of the reply, the records after the last `user` record that the function of `guppi/ledger.py` names the person's message or a returned answer, holds a round of `case-guppi`, `uv run guppi casecheck` judges how the reply opens. A round is a text that `case-guppi` gives back to an `Agent` or `SendMessage` call and that `is_round` of `guppi/casecheck.py`, the one test of a round, finds one; it comes back in the `tool_result` of an `Agent` call, or in the returned answer that opens the turn.
**＋** While the session's event log holds no `prespec` line of this session after its `hi`, it exits 2 when the main agent wrote text in the turn after the first round of the turn came back and before its last tool call.
**＋** When the turn holds a refusal of `uv run guppi casecheck`, judged by `refusals` of `guppi/ledger.py`, it judges only the texts after the last such refusal, so a round shown again with nothing before it passes.
**＋** It exits 2 when the first line of the reply that is not blank opens neither with `❓ ` nor with a bold label that ends in a colon, the label of the Context paragraph as it stands translated.
**＋** Its reason on stderr quotes the text that stands before the round and tells the agent to show the round again, opening with its Context paragraph or its first question, with nothing before it.
**＋** The check runs in the same `Stop` run as the comparison of shown Cases, and a reply that both refuse gives both reasons.
**－** A text the main agent wrote in the turn before the first round came back is not judged.
**－** Text after the last question and one horizontal rule is not judged.
**－** Once the session's event log holds a `prespec` line of this session after its `hi`, text before the last tool call of the turn is not judged, and a reply of the loop after the findings of `/pre-spec` is judged only by its first line; in that loop each answer of a `case-guppi` comes back in a turn of its own, and the text the main agent writes there is set by `rule-prespec`.
**－** A turn with no round of `case-guppi` is not judged: the main agent's own questions in the report of `/pre-spec`, at `/hi` or at a stop of Work Mode, a `**Fact:**` answer shown with the question that stood open, and a re-pitch by `.claude/skills/wait-what/SKILL.md`.
**－** With `stop_hook_active` set a round shown again after a refusal is judged again, and the reason is given as `estimate-case-check-judges-a-showing-after-a-refusal` sets it.
**－** It stores nothing and writes no file.

## Result

2026-10-07, uv run pytest tests/test_casecheck.py: 164 passed; a text before the Agent call that brought the round back passes, a text after the round came back and before a later call is refused, a round shown again with nothing before it after a refusal passes, a reply opening with a line of its own after a refusal is refused, a round in the opening answer leaves every text judged; the after-prespec and no-round tests pass as before

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
