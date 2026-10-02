---
type: estimate
kind: QA
status: pending
target: "[[rule-case-check]]"
purpose: Whether the Stop run of the Case check refuses a reply that shows a round of case-guppi after a text of the main agent's own, judges only the first line of the reply after pre-spec, and leaves a turn with no round alone
method: uv run pytest tests/test_casecheck.py -k round; by hand in a later session, the first rounds of case-guppi shown before and after pre-spec, the replies and the hook's refusals read in the transcript
checked: 2026-10-01
origin: raw/2026-09-30/2356/ledger.md#case-562
sprint: migration
created: 2026-09-30
tags: [hooks, harness, workflow]
---

## Criterion

When:
`Stop` fires after a reply of the main agent, and `uv run guppi casecheck` runs on it.

Then:
When the turn of the reply, the records after the last `user` record that the function of `guppi/ledger.py` names the person's message or a returned answer, holds a round of `case-guppi`, `uv run guppi casecheck` judges how the reply opens. A round is a text that `case-guppi` gives back to an `Agent` or `SendMessage` call and that holds a question line `❓ **Q<n>** - **<title>**:` of `.claude/skills/grill-me/SKILL.md`, no Case heading and no first line `**Fact:**`.
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

2026-10-01, uv run pytest tests/test_casecheck.py -k round: 14 passed; by hand, session 1237: every round of case-guppi (567 twice, 568 twice, 569 once) came before /pre-spec, each reply showing one opened with the translated Context label or with its first question line, and no text of the main agent stood before the last tool call of those turns; no Stop refusal of guppi casecheck stands in the transcript; not exercised: a refusal, and a round after /pre-spec, since every case-guppi answered the findings with its Case

## History

- 2026-10-01 created · [[decision-case-562]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L29
- 2026-10-01 updated: the Criterion replaced whole — the same behaviour, with the true reason for the exemption after /pre-spec (case 581.2) · [[decision-case-581.2]]
- 2026-10-02 updated: the Criterion replaced whole — the turn of the reply starts at the person's message or a returned answer, by the function of guppi/ledger.py (case 590.3) · [[decision-case-590.3]]
