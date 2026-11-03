---
type: estimate
kind: QA
status: passed
target: "[[rule-ask]]"
purpose: Whether ask-guppi makes a Read or a Grep on vault/wiki/decisions/ only for a hook trial that a ratified Case names and its prompt names, once each, and answers with each refusal and none of the text of a page
method: "by hand, after the librarian's run that renders .claude/agents/ask-guppi.md and .claude/rules/search-leaves-out-decisions.md with the hook trial: the calls and the answer of ask-guppi in the trial of the session whose brief puts the reading of estimate-search-leaves-out-decisions-refuses-ask-guppi under Work, in its transcript, read against the Criterion, recorded in the estimate line"
checked: 2026-10-31
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
The main agent starts `ask-guppi`, which follows `.claude/agents/ask-guppi.md` rendered from `rule-ask` and `.claude/rules/search-leaves-out-decisions.md` rendered from `rule-search-leaves-out-decisions`, with a prompt that names a trial, named by a ratified Case, of the hook on `vault/wiki/decisions/`, and the Read and the Grep that the trial makes.

Then:
`ask-guppi` makes the Read and the Grep that the prompt names, once each, and no other call on `vault/wiki/decisions/`.
**＋** It answers with one line per call: the call and the reason of its refusal as the hook gave it, or, where the call ran, that it ran, with none of the text it printed.
**－** Without such a trial in its prompt, the agent tries no call on the Decision folder.
**－** Whether the hook refuses the call is outside this promise: `estimate-search-leaves-out-decisions-refuses-ask-guppi` reads it.

## Result

2026-10-31, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
