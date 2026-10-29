---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, before it states what a function or a script of the repository does, prints or leaves out, reads whole the function that decides it, names its file and the function in context, and keeps out a claim about code it did not read
method: "by hand, after the first /pre-spec of a session whose Cases case-guppi built with .claude/agents/case-guppi.md rendered from the Render of rule-case-build that sets this Criterion: the findings of ask-guppi at that /pre-spec read for a claim of a Case about what code of the repository does that its context does not back by the function it read, the count in the estimate line"
checked: 2026-10-17
origin: raw/2026-10-16/2104/ledger.md#case-869
sprint: plugin
created: 2026-10-16
tags: [session, workflow, harness, case-build]
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case and states in a round, in `context`, in `then` or in a text a task writes what a function or a script of the repository does, prints or leaves out.

Then:
Before it states the claim, `case-guppi` reads whole the function that decides it, each of its conditions and not only the line it cites.
**＋** The `context` of the Case names the file and the function that `case-guppi` read for the claim.
**＋** A claim about code that `case-guppi` did not read stays out of the Case.
**－** `case-guppi` still reads a module of code in parts: the deciding function is one of those parts.

## Result

2026-10-17, Work readings of session 1805: the findings of ask-guppi at the /pre-spec of session 1805, whose Cases 878, 879 and 880 case-guppi built with .claude/agents/case-guppi.md rendered from the Render of rule-case-build (the findings of the first such /pre-spec, of session 0027, stand only in its transcript, which a reading does not open); seven findings, on a contradiction of two sub-cases, pointers in brackets, a term after Case 879, an Estimate left unnamed, a method this session could not take and a check of the librarian's run; 0 claims of a Case about what code of the repository does that its context does not back by the function it read

## History

- 2026-10-17 created · [[decision-case-869]]
- 2026-10-17 status: pending → passed · raw/2026-10-17/1805/ledger.md#L53
- 2026-10-29 updated: the method waits for the first /pre-spec after the Render; the reading at the Retro of a past session is gone · [[decision-case-897.5]]
