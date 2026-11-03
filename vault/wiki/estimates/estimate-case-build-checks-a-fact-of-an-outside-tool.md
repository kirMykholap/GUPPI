---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether the Render of rule-case-build gives case-guppi WebFetch among its tools and tells it to read in the documentation of a tool outside the repository the behaviour an option rests on before it recommends that option, to give the address of the page in context, and not to recommend an option whose fact the documentation does not settle
method: "by hand: the Render of rule-case-build in .claude/agents/case-guppi.md read against the Criterion, recorded in the estimate line"
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness, case-build]
core: true
---

## Criterion

When:
The Render of `rule-case-build` in `raw/<date>/<hi HHMM>/spec.md`, the text that `.claude/agents/case-guppi.md` is rendered from, is read at the Retro of the session that changes it.

Then:
Its `tools` line holds `WebFetch`.
**＋** It tells `case-guppi`, before it recommends an option that rests on how a tool outside the repository behaves, to read that behaviour in the documentation of the tool by `WebFetch` and to give in `context` the address of the page it read and what the page says of the fact.
**＋** It tells `case-guppi` that, where the documentation it read does not settle the fact, the `**After:**` line of the option and `context` say that the fact is not checked, and the option is not recommended.
**＋** It tells `case-guppi` that, where each option of the question rests on that fact, the `➡️` line says that the fact is not checked and leaves the choice to the person.
**－** It leaves an option that rests on whether a check passes to the reading of the last output of that check.

## Result

2026-10-17, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
