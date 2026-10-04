---
type: estimate
kind: QA
status: pending
target: "[[rule-prespec]]"
purpose: Whether after the findings of pre-spec the same ask-guppi runs confirm their own findings once on the Cases built again, before those Cases are shown, with no Grep, one line per finding, closed or not closed and no new finding, a finding not closed fixed or left by the person's answer to a question after the confirmation, the result standing after the horizontal rule of the showing, and no Case confirmed twice
method: "by hand at the /pre-spec of a later session whose findings send a Case back to its case-guppi, after the render of .claude/skills/pre-spec/SKILL.md and .claude/agents/ask-guppi.md by case 634.2: the SendMessage calls to ask-guppi, its tool calls and answers, and the replies up to the showing of the Cases built again, read in the transcript against the Criterion, recorded in the estimate line"
origin: raw/2026-10-04/2041/ledger.md#case-634.2
sprint: migration
created: 2026-10-04
tags: [session, workflow, harness]
---

## Criterion

When:
`/pre-spec` has reported findings that sent Cases of the plan back, and every `case-guppi` that got a finding has answered with its Case built again, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec` and `.claude/agents/ask-guppi.md` rendered from `rule-ask`.

Then:
The main agent sends each `ask-guppi` run whose findings sent a Case back the Cases built again on them, by `SendMessage`, all in one message, and asks whether each of its findings is closed.
**＋** Each `ask-guppi` answers with one line per finding of its own, under its number: `closed`, or `not closed` with one sentence on what still stands.
**＋** The main agent asks the person a question after the confirmation, in the shape of `.claude/skills/grill-me/SKILL.md`: whether each finding not closed is fixed or left; it sends a finding to be fixed to the `case-guppi` of its Case.
**＋** It then shows every Case built again in one reply, for one ratification, and writes what the confirmation found closed and not closed in its own text after the horizontal rule.
**－** No Case goes to `ask-guppi` a second time, and no new `ask-guppi` is dispatched.
**－** The answer of `ask-guppi` names no new finding; it runs no Grep, the Grep of the rules included, and reads only the Cases built again and the pages its findings name.
**－** After that ratification the hook of `rule-prespec-onward` sends the agent to the check and the exit, as before.

## History

- 2026-10-04 created · [[decision-case-634.2]]
