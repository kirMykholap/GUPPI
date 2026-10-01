---
type: estimate
kind: QA
status: pending
target: "[[rule-prespec]]"
purpose: Whether after the findings of pre-spec the main agent sends the fixes to their case-guppi at once, stays quiet while answers are out, gathers every question into one numbered list, and shows the Cases built again in one reply
method: by hand at the /pre-spec of a later session whose report sends findings to two or more case-guppi, the replies between the report and the showing again and the SendMessage calls read in the transcript
origin: raw/2026-09-30/2356/ledger.md#case-561.2
sprint: migration
created: 2026-09-30
tags: [session, workflow]
---

## Criterion

When:
`/pre-spec` has reported findings in Cases of the plan, and the main agent sends them to the `case-guppi` of those Cases.

Then:
The main agent sends each finding in a Case that needs no word of the person to the `case-guppi` of that Case by `SendMessage`, all of them in one message, and holds back a finding whose fix waits for the person's answer.
**＋** It writes nothing in the chat while an answer of a `case-guppi` it sent is still out, and passes on no answer of one `case-guppi` alone.
**＋** It then shows the person one list of what to answer: its own questions still open and every round that came back, each question in the shape of `.claude/skills/grill-me/SKILL.md` and numbered `<Case id>.Q<n>` by the Case it belongs to.
**＋** It sends each answer, with each finding held back for it, to the `case-guppi` of its Case in one message, and repeats the wait and the list until every `case-guppi` it sent has answered with its Case.
**＋** It then shows every Case built again in one reply, for one ratification.
**－** Outside this loop no Case is taken up before the current one is ratified or deferred.
**－** A question that no answer settles stays in the next list under its number.

## History

- 2026-10-01 created · [[decision-case-561.2]]
