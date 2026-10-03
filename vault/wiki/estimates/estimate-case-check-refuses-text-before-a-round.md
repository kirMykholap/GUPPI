---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the Stop run of the Case check refuses a reply that shows a round of case-guppi after a text of the main agent's own, judges only the first line of the reply after pre-spec, and leaves a turn with no round alone
method: uv run pytest tests/test_casecheck.py -k round; by hand in a later session, the first rounds of case-guppi shown before and after pre-spec, the replies and the hook's refusals read in the transcript
checked: 2026-10-03
origin: raw/2026-09-30/2356/ledger.md#case-562
sprint: migration
created: 2026-09-30
tags: [hooks, harness, workflow]
---

## Criterion

When:
`Stop` fires after a reply of the main agent, and `uv run guppi casecheck` runs on it.

Then:
When the turn of the reply, the records after the last `user` record that the function of `guppi/ledger.py` names the person's message or a returned answer, holds a round of `case-guppi`, `uv run guppi casecheck` judges how the reply opens. A round is a text that `case-guppi` gives back to an `Agent` or `SendMessage` call and that `is_round` of `guppi/casecheck.py`, the one test of a round, finds one.
**＋** While the session's event log holds no `prespec` line of this session after its `hi`, it exits 2 when the main agent wrote text in the turn before its last tool call.
**＋** It exits 2 when the first line of the reply that is not blank opens neither with `❓ ` nor with a bold label that ends in a colon, the label of the Context paragraph as it stands translated.
**＋** Its reason on stderr quotes the text that stands before the round and tells the agent to show the round again, opening with its Context paragraph or its first question, with nothing before it.
**＋** Text after the last question and one horizontal rule is not judged.
**＋** The check runs in the same `Stop` run as the comparison of shown Cases, and a reply that both refuse gives both reasons.
**－** Once the session's event log holds a `prespec` line of this session after its `hi`, text before the last tool call of the turn is not judged, and a reply of the loop after the findings of `/pre-spec` is judged only by its first line; in that loop each answer of a `case-guppi` comes back in a turn of its own, and the text the main agent writes there is set by `rule-prespec`.
**－** A turn with no round of `case-guppi` is not judged: the main agent's own questions in the report of `/pre-spec`, at `/hi` or at a stop of Work Mode, a `**Fact:**` answer shown with the question that stood open, and a re-pitch by `.claude/skills/wait-what/SKILL.md`.
**－** On the re-fire (`stop_hook_active`) it exits 0, so the round shown again after a refusal is not judged again.
**－** It stores nothing and writes no file.

## Result

2026-10-03, session 0115, `uv run pytest tests/test_casecheck.py -k round` 31 passed; by hand in the transcript: the rounds of case-guppi shown before /pre-spec (Cases 607, 608 twice, 609) opened with the Context label or the first question and were not refused; after /pre-spec the reply that showed round 608.Q1 under a sentence of its own was refused with the reason quoting that sentence and telling the agent to show the round again with nothing before it, the round shown again passed on the re-fire, and the second round 608.Q1 opened with its question and passed; a turn with no round (the answer to the person's question with the Waiting line) was not judged; a reply refused by both checks did not occur

## History

- 2026-10-01 created · [[decision-case-562]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L29
- 2026-10-01 updated: the Criterion replaced whole — the same behaviour, with the true reason for the exemption after /pre-spec (case 581.2) · [[decision-case-581.2]]
- 2026-10-02 updated: the Criterion replaced whole — the turn of the reply starts at the person's message or a returned answer, by the function of guppi/ledger.py (case 590.3) · [[decision-case-590.3]]
- 2026-10-03 updated: the Criterion replaced whole — a round is known by is_round, the one test of a round (case 601.4) · [[decision-case-601.4]]
- 2026-10-03 status: pending → passed · raw/2026-10-03/0115/ledger.md#L15
