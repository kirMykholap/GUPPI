---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: Whether after the findings of pre-spec the main agent sends nothing to a case-guppi until the person has answered every question of the report, then sends each case-guppi its findings with the answers in one message, ends each waiting turn with one labelled line and writes nothing else while answers are out, gathers every round into one numbered list, and shows the Cases built again in one reply
method: by hand at the /pre-spec of a later session after the render whose report asks the person a question and sends findings to two or more case-guppi, the replies between the report and the showing again, the SendMessage calls and any refusal of guppi casecheck read in the transcript
checked: 2026-10-03
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
**＋** It then shows every Case built again in one reply, in the showing that `vault/wiki/orchestration.md` sets, for one ratification.
**－** When an answer brings back a round while another answer is still out, the round is not shown in that turn, and `uv run guppi casecheck` does not refuse the reply that opens with the labelled line.
**－** Outside this loop, Cases go out together for one ratification only in a batch, as `vault/wiki/orchestration.md` sets it.
**－** A question that no answer settles stays in the next list under its number.

## Result

2026-10-03, by hand in the transcript of session 2300: the /pre-spec report asked Q1 and Q2 and sent nothing until the person answered; one SendMessage to each of the four case-guppi in one turn; each turn while an answer was out ended with one `**Ожидание:**` line naming the Cases answered and out; the round of 601 came back while 603 and 605 were out and was shown only after all answered, numbered 601.Q1 and 601.Q2; the answers went in one message; 601, 602, 603 and 605 were shown again in one reply for one ratification; the Waiting line of the later fix after the ratification (Case 603 to 606) also named the finding

## History

- 2026-10-01 created · [[decision-case-561.2]]
- 2026-10-01 status: pending → failed · raw/2026-10-01/1237/ledger.md#L37
- 2026-10-01 updated: the Criterion replaced whole — one labelled line per waiting turn instead of no text while answers are out (case 581.1) · [[decision-case-581.1]]
- 2026-10-02 status: pending → passed · raw/2026-10-02/1202/ledger.md#L56
- 2026-10-02 updated: the Criterion replaced whole - nothing goes to a case-guppi before every question of the report is answered (case 595.1) · [[decision-case-595.1]]
- 2026-10-02 updated: the Criterion replaced whole — outside the loop, Cases go out together only in a batch that orchestration.md sets (case 598.3) · [[decision-case-598.3]]
- 2026-10-03 status: pending → passed · raw/2026-10-02/2300/ledger.md#L24
