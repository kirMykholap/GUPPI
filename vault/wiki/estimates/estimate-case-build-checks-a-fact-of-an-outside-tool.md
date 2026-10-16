---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether the Render of rule-case-build gives case-guppi WebFetch among its tools and tells it to read in the documentation of a tool outside the repository the behaviour an option rests on before it recommends that option, to give the address of the page in context, and not to recommend an option whose fact the documentation does not settle
method: "by hand at the Retro of this session: the new Render of rule-case-build in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line"
origin: raw/2026-10-16/2104/ledger.md#case-871
sprint: plugin
created: 2026-10-16
tags: [session, workflow, harness, case-build]
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

2026-10-17, Retro of session 2104: the new Render of rule-case-build in spec.md read against the Criterion of case 871: tools holds WebFetch, the agent reads the documentation of the tool by WebFetch before it recommends an option that rests on it and gives the address in context, an option whose fact the documentation does not settle says it is not checked and is not recommended, and where every option rests on it the choice is left to the person

## History

- 2026-10-17 created · [[decision-case-871]]
- 2026-10-17 status: pending → passed · raw/2026-10-16/2104/ledger.md#L46
