---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: Whether after the findings of pre-spec the same ask-guppi runs confirm their own findings once on the Cases built again, before those Cases are shown, asked by a message that invites no new finding, with no Grep, a verdict line closed or not closed per finding and at most three sentences on why, then a list of what was not checked ending with a line per rule a search broke, and the list of the files read and nothing else, no new finding, a finding not closed fixed or left by the person's answer to a question after the confirmation, the result standing after the horizontal rule of the showing, and no Case confirmed twice
method: "by hand, after a /pre-spec whose findings send a Case back to its case-guppi, on the rendered .claude/skills/pre-spec/SKILL.md and .claude/agents/ask-guppi.md: the SendMessage calls to ask-guppi, its tool calls and answers, and the replies up to the showing of the Cases built again, read in the transcript against the Criterion, recorded in the estimate line (the render of case 638)"
checked: 2026-10-05
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

2026-10-05, Plan Mode of session 1831, case 669: set passed by the person's decision, without a reading; a problem seen later in what this Estimate promises comes back as a lesson; the defer of case 666 retired. The last reading before it, which left the page failed: 2026-10-05, by hand at the Work readings of session 1343, the /pre-spec of session 1343 after the render by case 638 (commit 7b089086): seven ask-guppi in one message; the findings to six case-guppi in one message (653 put off by the person's answer); the six runs whose findings sent a Case back asked in one message only whether each finding is closed; each made one Read of its case file, no Grep and no new finding; a verdict line under each finding; one list of what was not checked and the files read; finding 656-1.1 not closed put to the person as a grill-me question, left by the person; the six Cases shown in one reply for one ratification; no second dispatch; failed: under one finding each, the runs on 650 (3.1), 652 (1.1) and 654 (1.1) wrote four sentences, more than the three allowed

## History

- 2026-10-04 created · [[decision-case-634.2]]
- 2026-10-05 status: pending → failed · raw/2026-10-04/2245/ledger.md#L16
- 2026-10-05 updated: the Criterion replaced whole — a verdict line and at most three sentences per finding, then what was not checked and the files read; the confirmation message invites no new finding (case 638) · [[decision-case-638]]
- 2026-10-05 status: pending → failed · raw/2026-10-05/1343/ledger.md#L41
- 2026-10-05 deferred · [[decision-case-666]]
- 2026-10-05 updated: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson; the defer of case 666 retired (case 669) · [[decision-case-669.14]]
- 2026-10-15 updated: the pointer of the method stands in a bracket at its end, and the method waits for the event it names · [[decision-case-823.1]]
