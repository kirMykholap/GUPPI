---
type: estimate
kind: QA
status: pending
target: "[[rule-prespec]]"
purpose: Whether after the findings of pre-spec the same ask-guppi runs confirm their own findings once on the Cases built again, before those Cases are shown, asked by a message that invites no new finding, with no Grep, a verdict line closed or not closed per finding and at most three sentences on why, then a list of what was not checked ending with a line per rule a search broke, and the list of the files read and nothing else, no new finding, a finding not closed fixed or left by the person's answer to a question after the confirmation, the result standing after the horizontal rule of the showing, and no Case confirmed twice
method: "by hand at the /pre-spec of a later session whose findings send a Case back to its case-guppi, after the render of .claude/skills/pre-spec/SKILL.md and .claude/agents/ask-guppi.md by case 638: the SendMessage calls to ask-guppi, its tool calls and answers, and the replies up to the showing of the Cases built again, read in the transcript against the Criterion, recorded in the estimate line"
checked: 2026-10-04
origin: raw/2026-10-04/2041/ledger.md#case-634.2
sprint: migration
created: 2026-10-04
tags: [session, workflow, harness]
---

## Criterion

When:
`/pre-spec` has reported findings that sent Cases of the plan back, and every `case-guppi` that got a finding has answered with its Case built again, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec` and `.claude/agents/ask-guppi.md` rendered from `rule-ask`.

Then:
The main agent sends each `ask-guppi` run whose findings sent a Case back the Cases built again on them, by `SendMessage`, all in one message, and asks only whether each of its findings is closed.
**＋** For each finding of its own, under the finding's number, each `ask-guppi` answers with a line that holds `closed` or `not closed`, and under it at most a short paragraph of up to three sentences on why.
**＋** After the findings stands one list of what the agent did not check in confirming them. The list says "none" when it checked all of it and its searches broke no rule. Its last lines name each rule that a search of the agent broke, one line each, and say whether a verdict rests on what that search printed. Then stands a list of the paths of the files the agent read, and nothing else stands before or after.
**＋** The main agent asks the person a question after the confirmation, in the shape of `.claude/skills/grill-me/SKILL.md`: whether each finding not closed is fixed or left; it sends a finding to be fixed to the `case-guppi` of its Case.
**＋** It then shows every Case built again in one reply, for one ratification, and writes what the confirmation found closed and not closed in its own text after the horizontal rule.
**－** The message of the main agent invites no new finding and no new judgment of a Case beyond those findings.
**－** No Case goes to `ask-guppi` a second time, and no new `ask-guppi` is dispatched.
**－** The answer of `ask-guppi` names no new finding; it runs no Grep, the Grep of the rules included, and reads only the Cases built again and the pages its findings name.
**－** After that ratification the hook of `rule-prespec-onward` sends the agent to the check and the exit, as before.

## Result

2026-10-04, at the /pre-spec of session 2245, by hand from its transcript: the main agent sent both ask-guppi runs the rebuilt Cases in one message and asked whether each finding is closed; it asked the person in the grill-me shape whether the not-closed finding 3.1 of Case 636 is fixed or left and sent it to that case-guppi; it showed both rebuilt Cases in one reply, what the confirmation found standing in its text after the rule; no Case went to ask-guppi a second time and no new ask-guppi ran; the two runs ran no Grep and named no new finding (1 and 2 tool calls, reading the case files and rule-case-build.md, which a finding named); but their answers do not hold one line per finding with one sentence: the run of 636 put each number on a line of its own with closed or not closed and then 1 to 4 sentences under it, the run of 637 gave each finding a paragraph of 2 to 4 sentences; and the main agent's SendMessage invited "a new defect the rebuild itself brought in", which the Criterion's line that the answer names no new finding rules out — both runs declined it

## History

- 2026-10-04 created · [[decision-case-634.2]]
- 2026-10-05 status: pending → failed · raw/2026-10-04/2245/ledger.md#L16
- 2026-10-05 updated: the Criterion replaced whole — a verdict line and at most three sentences per finding, then what was not checked and the files read; the confirmation message invites no new finding (case 638) · [[decision-case-638]]
