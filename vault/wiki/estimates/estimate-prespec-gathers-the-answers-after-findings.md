---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: Whether after the findings of pre-spec the main agent sends nothing to a case-guppi until the person has answered every question of the report, then sends each case-guppi its findings with the answers in one message, ends each waiting turn with one labelled line and writes nothing else while answers are out, gathers every round into one numbered list, and shows the Cases built again in one reply
method: "by hand at the Retro of this session: the new Render of rule-prespec in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line"
checked: 2026-10-09
origin: raw/2026-09-30/2356/ledger.md#case-561.2
sprint: migration
created: 2026-09-30
tags: [session, workflow]
---

## Criterion

When:
`/pre-spec` has reported findings in Cases of the plan, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec`.

Then:
The main agent sends each finding in a Case, with each answer of the report that bears on that Case, to the `case-guppi` of that Case by `SendMessage`, one message to each `case-guppi`, as soon as the report asks the person no question or the person has answered every question of the report.
**＋** While a question of the report is unanswered, the main agent sends nothing to any `case-guppi`.
**＋** A question of the report that the person leaves unanswered is asked again in the shape of `.claude/skills/grill-me/SKILL.md` under its number.
**＋** The main agent ends each turn that sends to a `case-guppi`, and each turn that an answer opens while another answer it sent is still out, with one line that opens with a bold label ending in a colon and names the Cases that have answered and the Cases still out.
**＋** That line holds nothing of what an answer says and no question, and the main agent writes nothing else in the chat while an answer is out and passes on no answer of one `case-guppi` alone.
**＋** It then shows the person one list of every round that came back, each question in the shape of `.claude/skills/grill-me/SKILL.md` and numbered `<Case id>.Q<n>` by the Case it belongs to, sends each answer to the `case-guppi` of its Case in one message, and repeats the wait and the list until every `case-guppi` it sent has answered with its Case.
**＋** In that list the `**Context:**` label of each first round on an item names its Case id and its item of `raw/<date>/<hi HHMM>/frontier.md`, translated, such as `**Context — Case 7 (C2):**`; a horizontal rule stands before the first round of the list and one between the last question of one Case and the round of the next, and no heading or other line of the main agent's own but such a rule marks where a round begins.
**＋** It then shows every Case built again in one reply, in the showing that `vault/wiki/orchestration.md` sets, for one ratification.
**－** When an answer brings back a round while another answer is still out, the round is not shown in that turn, and `uv run guppi casecheck` does not refuse the reply that opens with the labelled line.
**－** Outside this loop, Cases go out together for one ratification only in a batch, as `vault/wiki/orchestration.md` sets it.
**－** A question that no answer settles stays in the next list under its number.

## Result

2026-10-09, Retro, by hand: the replace of case 751.3 in raw/2026-10-09/2049/spec.md read with the standing steps 1–7 of the Render of rule-prespec; the list opens with a rule and puts one between the rounds of two Cases, the other lines of the Criterion stand in the steps as rendered; the anchor stands once

## History

- 2026-10-01 created · [[decision-case-561.2]]
- 2026-10-01 status: pending → failed · raw/2026-10-01/1237/ledger.md#L37
- 2026-10-01 updated: the Criterion replaced whole — one labelled line per waiting turn instead of no text while answers are out (case 581.1) · [[decision-case-581.1]]
- 2026-10-02 status: pending → passed · raw/2026-10-02/1202/ledger.md#L56
- 2026-10-02 updated: the Criterion replaced whole - nothing goes to a case-guppi before every question of the report is answered (case 595.1) · [[decision-case-595.1]]
- 2026-10-02 updated: the Criterion replaced whole — outside the loop, Cases go out together only in a batch that orchestration.md sets (case 598.3) · [[decision-case-598.3]]
- 2026-10-03 status: pending → passed · raw/2026-10-02/2300/ledger.md#L24
- 2026-10-07 updated: the Criterion replaced whole — the Context label of each first round in the list names its Case; method set to the reading of the Spec at Retro · [[decision-case-699.7]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/0211/ledger.md#L47
- 2026-10-09 updated: the Criterion replaced whole — a horizontal rule between the rounds of two Cases in the list · [[decision-case-751.3]]
- 2026-10-09 status: pending → passed · raw/2026-10-09/2049/ledger.md#L16
