---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi searches .guppi/guppi/ for an existing implementation of a judgment before a task of its Case adds code that judges a text, reads whole the function each side calls for it, asks the person where they answer differently, and the task imports one judgment and tests both sides where they parted
method: "by hand: the Render of rule-case-build in .claude/agents/case-guppi.md read against the Criterion, and the findings of ask-guppi at a /pre-spec read for a task of a Case built by case-guppi that adds a second copy of a judgment or names as shared a function that answers differently from the one the other side calls, the count in the estimate line"
checked: 2026-10-13
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case with a task that adds code under `.guppi/guppi/` that judges a text — a pattern, a map or a predicate.

Then:
Before it writes the task, `case-guppi` searches `.guppi/guppi/` for the words of what the code judges, such as the field, the category or the form of the line, and reads each hit around its line.
**＋** Where code under `.guppi/guppi/` already makes that judgment, the task imports it, or moves it into one module that both sides import, as `rule-one-judgment-one-implementation` sets it.
**＋** Where the two sides cannot share the code, the task adds one test that runs both over the same input and asserts they answer alike.
**＋** Before it names a function as the judgment both sides share, `case-guppi` reads whole the function each side calls today for that judgment, the side the Case does not change included, and judges whether they answer alike on each input where they could part.
**＋** Where they part, `case-guppi` names neither as the shared judgment and asks the person in a round which answer both sides share, with the input and what each answers there.
**＋** Where they parted, the task adds one test that runs both sides over that input and asserts they answer alike.
**＋** The `context` of the Case names that search, its pattern, its paths and what it printed.
**＋** The `context` of the Case names each function it read for the judgment both sides share, and what it found.
**－** A Case whose tasks add no code that judges a text takes no such search.

## Result

2026-10-13, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
