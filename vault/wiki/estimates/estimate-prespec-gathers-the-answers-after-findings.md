---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: Whether after the findings of pre-spec the main agent sends the fixes to their case-guppi at once, ends each waiting turn with one labelled line naming the Cases answered and still out and writes nothing else while answers are out, gathers every question into one numbered list, and shows the Cases built again in one reply
method: by hand at the /pre-spec of a later session after the render whose report sends findings to two or more case-guppi, the replies between the report and the showing again, the SendMessage calls and any refusal of guppi casecheck read in the transcript
checked: 2026-10-02
origin: raw/2026-09-30/2356/ledger.md#case-561.2
sprint: migration
created: 2026-09-30
tags: [session, workflow]
---

## Criterion

When:
`/pre-spec` has reported findings in Cases of the plan, and the main agent sends them to the `case-guppi` of those Cases, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec`.

Then:
The main agent sends each finding in a Case that needs no word of the person to the `case-guppi` of that Case by `SendMessage`, all of them in one message, and holds back a finding whose fix waits for the person's answer.
**＋** It ends each turn that sends to a `case-guppi`, and each turn that an answer opens while another answer it sent is still out, with one line that opens with a bold label ending in a colon and names the Cases that have answered and the Cases still out.
**＋** That line holds nothing of what an answer says and no question, and the main agent writes nothing else in the chat while an answer is out and passes on no answer of one `case-guppi` alone.
**＋** It then shows the person one list of what to answer: its own questions still open and every round that came back, each question in the shape of `.claude/skills/grill-me/SKILL.md` and numbered `<Case id>.Q<n>` by the Case it belongs to.
**＋** It sends each answer, with each finding held back for it, to the `case-guppi` of its Case in one message, and repeats the wait and the list until every `case-guppi` it sent has answered with its Case.
**＋** It then shows every Case built again in one reply, for one ratification.
**－** When an answer brings back a round while another answer is still out, the round is not shown in that turn, and `uv run guppi casecheck` does not refuse the reply that opens with the labelled line.
**－** Outside this loop no Case is taken up before the current one is ratified or deferred.
**－** A question that no answer settles stays in the next list under its number.

## Result

2026-10-02, by hand at the /pre-spec of session 1202 in the transcript of session 1a155152: the report numbered 13 findings and asked one question in the grill-me shape; findings 1–12 went to the case-guppi of 588, 590 and 591 in one SendMessage each, the finding on How it works held back for 589 and 590 until the person's answer; each turn while an answer was out ended with one line under the bold label Ожидание naming the Cases answered and still out, with no question; the round 590.Q6 that came back while 588 and 591 were out was not shown in that turn; once all answered, one list showed 589.Q1 and 590.Q6 numbered by Case; the answers went back in one message each; the four Cases built again were shown in one reply for one ratification; guppi casecheck refused no reply of the loop

## History

- 2026-10-01 created · [[decision-case-561.2]]
- 2026-10-01 status: pending → failed · raw/2026-10-01/1237/ledger.md#L37
- 2026-10-01 updated: the Criterion replaced whole — one labelled line per waiting turn instead of no text while answers are out (case 581.1) · [[decision-case-581.1]]
- 2026-10-02 status: pending → passed · raw/2026-10-02/1202/ledger.md#L56
