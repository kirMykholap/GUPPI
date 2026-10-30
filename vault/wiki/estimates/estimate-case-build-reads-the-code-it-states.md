---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, before it states what a function or a script of the repository does, prints or leaves out, reads whole the function that decides it, each function it calls on the way and the place where its caller takes the input it walks over, takes no name or docstring of a function for a reading of it, names in context the file and each function it read, and keeps out a claim about code it did not read
method: "by hand, after a /pre-spec of a session whose Cases case-guppi built with .claude/agents/case-guppi.md rendered from a Render of rule-case-build that asks, for a claim about code, for each function called on the way and the place where the caller takes the input: the findings of ask-guppi at that /pre-spec read for a claim of a Case about what code of the repository does that its context does not back by the functions it read — the deciding function, each function it calls on the way and the place where its caller takes the input — the count in the estimate line"
checked: 2026-10-30
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
**＋** It reads each function that this function calls on the way to what it states.
**＋** Where the function walks over an input, such as a transcript or a list of files, it reads the place where the caller of the function takes that input.
**＋** The `context` of the Case names the file and the function that `case-guppi` read for the claim.
**＋** The `context` of the Case also names each function called on the way and the place of the input that `case-guppi` read for the claim.
**＋** A claim about code that `case-guppi` did not read stays out of the Case.
**－** The name and the docstring of a function do not stand for a reading of it.
**－** `case-guppi` still reads a module of code in parts: the deciding function is one of those parts.
**－** Each function it reads on the way to the claim is one of those parts too.

## Result

2026-10-30, Retro of session 2005: the findings of ask-guppi (agent a974fa00e14da398d) at the /pre-spec of session 2005, whose Cases case-guppi built on the Render of rule-case-build: 8 findings, on a Purpose that describes behaviour, a split of Case 940, a /box edge, a third copy of one judgment, two Criteria that name the person as the writer of the copy, the uses of --allow-draft and two Estimates left unnamed; 0 claims of a Case about what code of the repository does that its context does not back by the functions it read

## History

- 2026-10-17 created · [[decision-case-869]]
- 2026-10-17 status: pending → passed · raw/2026-10-17/1805/ledger.md#L53
- 2026-10-29 updated: the method waits for the first /pre-spec after the Render; the reading at the Retro of a past session is gone · [[decision-case-897.5]]
- 2026-10-29 updated: method names a kind of moment, not the first /pre-spec under the Render that set this Criterion · [[decision-case-898.2]]
- 2026-10-30 updated: the Criterion replaced whole — the functions called on the way and the source of the input are read too, and a name or a docstring is no reading · [[decision-case-926]]
- 2026-10-30 status: pending → passed · raw/2026-10-30/2005/ledger.md#L55
