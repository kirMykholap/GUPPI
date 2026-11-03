---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: Whether after the findings of pre-spec the main agent sends nothing to a case-guppi until the person has answered every question of the report, then sends each case-guppi its findings with the answers in one message, ends each waiting turn with one labelled line and writes nothing else while answers are out, gathers every round into one numbered list, and shows the Cases built again in one reply, a Case whose stored finding the check refuses sent back and the others shown, as estimate-orchestration-shows-the-clean-cases-of-a-batch-first sets it
method: "by hand at Retro of the session that changes it: the new Render of rule-prespec in the Spec, read against the Criterion, recorded in the estimate line"
checked: 2026-10-26
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow]
core: true
---

## Criterion

When:
`/pre-spec` has reported findings in Cases of the plan, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec`.

Then:
The main agent sends each finding in a Case, with each answer of the report that bears on that Case, to the `case-guppi` of that Case by `SendMessage`, one message to each `case-guppi`, as soon as the report asks the person no question or the person has answered every question of the report.
**＋** While a question of the report is unanswered, the main agent sends nothing to any `case-guppi`.
**＋** A question of the report that the person leaves unanswered is asked again in the shape of `.claude/skills/grill-me/SKILL.md` under its number.
**＋** The main agent ends each turn that sends to a `case-guppi`, and each turn that an answer opens while another answer it sent is still out, with one line that opens with a bold label ending in a colon and names the Cases that have answered and the Cases still out, but for the reply that answers a refusal of the showing of the Cases built again, which ends as `estimate-orchestration-shows-the-clean-cases-of-a-batch-first` sets it.
**＋** That line holds nothing of what an answer says and no question, and but for that reply the main agent writes nothing else in the chat while an answer is out and passes on no answer of one `case-guppi` alone.
**＋** It then shows the person one list of every round that came back, each question in the shape of `.claude/skills/grill-me/SKILL.md` and numbered `<Case id>.Q<n>` by the Case it belongs to, sends each answer to the `case-guppi` of its Case in one message, and repeats the wait and the list until every `case-guppi` it sent has answered with its Case.
**＋** In that list the `**Context:**` label of each first round on an item names its Case id and its item of `raw/<date>/<hi HHMM>/frontier.md`, translated, such as `**Context — Case 7 (C2):**`; a horizontal rule stands before the first round of the list and one between the last question of one Case and the round of the next, and no heading or other line of the main agent's own but such a rule marks where a round begins.
**＋** It then shows every Case built again in one reply, in the showing that `vault/wiki/orchestration.md` sets, for one ratification.
**＋** After a refusal of that reply by `rule-case-check`, step 7 of `.claude/skills/pre-spec/SKILL.md` sends the main agent to the step of `vault/wiki/orchestration.md` that `estimate-orchestration-shows-the-clean-cases-of-a-batch-first` checks.
**－** When an answer brings back a round while another answer is still out, the round is not shown in that turn, and `uv run --project .guppi guppi casecheck` does not refuse the reply that opens with the labelled line.
**－** Outside this loop, Cases go out together for one ratification only in a batch, as `vault/wiki/orchestration.md` sets it.
**－** A question that no answer settles stays in the next list under its number.

## Result

2026-10-26, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
