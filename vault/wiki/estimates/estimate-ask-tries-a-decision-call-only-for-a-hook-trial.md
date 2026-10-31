---
type: estimate
kind: QA
status: passed
target: "[[rule-ask]]"
purpose: Whether ask-guppi makes a Read or a Grep on vault/wiki/decisions/ only for a hook trial that a ratified Case names and its prompt names, once each, and answers with each refusal and none of the text of a page
method: "by hand, after the librarian's run that renders .claude/agents/ask-guppi.md and .claude/rules/search-leaves-out-decisions.md with the hook trial: the calls and the answer of ask-guppi in the trial of the session whose brief puts the reading of estimate-search-leaves-out-decisions-refuses-ask-guppi under Work, in its transcript, read against the Criterion, recorded in the estimate line"
checked: 2026-10-31
origin: raw/2026-10-31/0128/ledger.md#case-954.3
sprint: plugin
created: 2026-10-31
tags: [session, workflow, harness]
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

2026-10-31, Work Mode of session 0431, transcript subagents/agent-a1c55a96bf027c3dc.jsonl of session 8727d5ce: ask-guppi made the Read and the Grep the prompt named, once each, no other call on vault/wiki/decisions/, and answered with one line per call giving the reason of its refusal as the hook gave it and none of the text of a page; the run of ask-guppi at /pre-spec (agent-a3a2b4d5034e84cde.jsonl) made no call on the Decision folder by its own report

## History

- 2026-10-31 created · [[decision-case-954.3]]
- 2026-10-31 status: pending → passed · raw/2026-10-31/0431/ledger.md#L38
