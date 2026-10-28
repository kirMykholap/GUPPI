---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi reads no case file of a Case that its prompt or a message names as built at the same time and names none in given, names in context and in a Sibling line of its summary each such Case its Case rests on, and reads the finished file whole once a message says that build has ended
method: "by hand, after the first send of two or more Cases to case-guppi at the same time under the new Render of rule-case-build: the tool calls and the summary of each case-guppi of that send read against the Criterion, recorded in the estimate line"
checked: 2026-10-28
origin: raw/2026-10-16/2104/ledger.md#case-872.1
sprint: plugin
created: 2026-10-16
tags: [session, workflow, harness, case-build]
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

2026-10-28, Work readings, the subagent transcripts of session 1907 (the send of /pre-spec findings to the case-guppi of Cases 892, 893 and 894 at the same time): no case-guppi read a case file of another Case of that send in that build; Case 893 named Case 894 in its context and in a Sibling line of its summary and named no case file in given; sent the message that the build of 894 had ended, it read case-894.md whole (no offset or limit) and fixed its Case; its Read of case-892.md came in its first build, when no prompt named 892 as built at the same time

## History

- 2026-10-17 created · [[decision-case-872.1]]
- 2026-10-28 status: pending → passed · raw/2026-10-28/1907/ledger.md#L13
