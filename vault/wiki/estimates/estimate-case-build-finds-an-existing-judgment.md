---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi searches .guppi/guppi/ for an existing implementation of a judgment before a task of its Case adds code that judges a text, reads whole the function each side calls for it, asks the person where they answer differently, and the task imports one judgment and tests both sides where they parted
method: "by hand at the Retro of this session: the new Render of rule-case-build in raw/<date>/<hi HHMM>/spec.md read against the Criterion, and the findings of ask-guppi at the /pre-spec of this session read for a task of a Case built by case-guppi that adds a second copy of a judgment or names as shared a function that answers differently from the one the other side calls, the count in the estimate line"
checked: 2026-10-13
origin: raw/2026-10-09/2049/ledger.md#case-752
sprint: migration
created: 2026-10-09
tags: [session, workflow, harness]
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

2026-10-13, Retro by hand: the new Render of rule-case-build in raw/2026-10-12/2349/spec.md (case 785) has case-guppi read whole the function each side calls, judge where they part, ask the person in a round and add a test over that input, and name each function in context — each line of the Criterion stands in it; the ask-guppi run at the /pre-spec of this session found 2 such tasks (findings 11 and 12, Case 788), both in Cases built on the Render before case 785

## History

- 2026-10-09 created · [[decision-case-752]]
- 2026-10-09 status: pending → passed · raw/2026-10-09/2049/ledger.md#L20
- 2026-10-13 updated: the Criterion replaced whole — case-guppi reads the function each side calls before it names a shared judgment, asks the person where they part, and a test runs both sides over that input (case 785) · [[decision-case-785]]
- 2026-10-13 status: pending → passed · raw/2026-10-12/2349/ledger.md#L44
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
