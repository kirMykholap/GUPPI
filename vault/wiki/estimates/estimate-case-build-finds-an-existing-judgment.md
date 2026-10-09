---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi searches guppi/ for an existing implementation of a judgment before a task of its Case adds code that judges a text, and the task imports it or moves it into one module
method: "by hand at the Retro of this session: the new Render of rule-case-build in raw/<date>/<hi HHMM>/spec.md read against the Criterion, and the findings of ask-guppi at the /pre-spec of this session read for a task of a Case built by case-guppi that adds a second copy of a judgment, the count in the estimate line"
origin: raw/2026-10-09/2049/ledger.md#case-752
sprint: migration
created: 2026-10-09
tags: [session, workflow, harness]
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case with a task that adds code under `guppi/` that judges a text — a pattern, a map or a predicate.

Then:
Before it writes the task, `case-guppi` searches `guppi/` for the words of what the code judges, such as the field, the category or the form of the line, and reads each hit around its line.
**＋** Where code under `guppi/` already makes that judgment, the task imports it, or moves it into one module that both sides import, as `rule-one-judgment-one-implementation` sets it.
**＋** Where the two sides cannot share the code, the task adds one test that runs both over the same input and asserts they answer alike.
**＋** The `context` of the Case names that search, its pattern, its paths and what it printed.
**－** A Case whose tasks add no code that judges a text takes no such search.
**－** `insight-workflow-case-written-without-reading-the-pages-it-changes` stands `actioned` with `addressed_by: decision-case-752` and leaves the backlog.

## Result

2026-10-09, Retro, by hand: the new Render sentence of rule-case-build in raw/2026-10-09/2049/spec.md (case 752) read against the Criterion — the Grep of guppi/ before a task that judges a text, import or one module, a test over both sides, the search named in context; its anchor stands once; the findings of ask-guppi at the /pre-spec of this session name 0 tasks that add a second copy of a judgment

## History

- 2026-10-09 created · [[decision-case-752]]
- 2026-10-09 status: pending → passed · raw/2026-10-09/2049/ledger.md#L20
