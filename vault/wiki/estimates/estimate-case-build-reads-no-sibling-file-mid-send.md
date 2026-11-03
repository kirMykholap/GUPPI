---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi reads no case file of a Case that its prompt or a message names as built at the same time and names none in given, names in context and in a Sibling line of its summary each such Case its Case rests on, and reads the finished file whole once a message says that build has ended
method: "by hand, after a send of two or more Cases to case-guppi at the same time: the tool calls and the summary of each case-guppi of that send read against the Criterion, recorded in the estimate line"
checked: 2026-10-28
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness, case-build]
core: true
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case from a prompt or a message that names another Case of the session as built at the same time.

Then:
`case-guppi` reads no case file of that other Case in that build, though the prompt or a finding of the check of `rule-case-check` names it.
**＋** It names no case file of that other Case in `given`, so the frame it reads holds none.
**＋** It bounds its Case by the sentence the prompt gives on that other Case.
**＋** Where its Case rests on that other Case — a claim of `context` or a line `**Other Case:**` — its `context` names that Case, and the item of its Case in the summary carries a line `**Sibling:**` that names it.
**＋** Sent a later message that says that the build of that Case has ended, it reads the finished case file whole and fixes its Case against it.
**－** A Case of the session that no prompt or message names as built at the same time it reads as before.

## Result

2026-10-28, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
