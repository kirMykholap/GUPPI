---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether each reply of case-guppi that the main agent shows — a round, a Fact answer or a built Case — stands between two horizontal rules, with the agent's own text after the second
method: "by hand: the Render of rule-orchestration in vault/wiki/orchestration.md read against the Criterion, recorded in the estimate line"
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow]
core: true
---

## Criterion

When:
The main agent shows in the chat a reply of `case-guppi` — a round of questions, a `**Fact:**` answer it passes on, or a built Case with its list and its `ratification` — with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

Then:
A horizontal rule stands on its own line before the reply of `case-guppi`.
**＋** A second horizontal rule stands after the reply; the main agent's own text follows it, or, in a batch, the next reply of `case-guppi`, for which that rule is the rule before it.
**＋** Each rule is the line `---` alone, with a blank line after it, and with a blank line before it unless it opens the reply, so that Markdown does not read the line above it as the underline of a heading.
**－** A `**Waiting:**` line, the acknowledging reply and a Case in the short form are no reply of `case-guppi` and get no such rules.

## Result

2026-10-09, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
