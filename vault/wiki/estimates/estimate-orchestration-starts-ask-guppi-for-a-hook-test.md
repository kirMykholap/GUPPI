---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether the main agent starts ask-guppi outside pre-spec only in Work Mode, for a test by hand of a hook that judges its calls that a task of a ratified Case or a Work reading names, with a prompt that says the calls are a test of that hook
method: "by hand, after the librarian's run that renders vault/wiki/orchestration.md with the start of ask-guppi for a test of a hook that judges its calls: the Agent calls of the main agent in the Work Mode of the session whose brief puts the reading of estimate-search-leaves-out-decisions-refuses-ask-guppi under Work, in its transcript, read against the Criterion, recorded in the estimate line"
checked: 2026-10-31
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
In Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, the main agent takes a task of a ratified Case, or the Work reading of an Estimate whose `method` a ratified Case set, that names a test by hand of a hook which judges a call of `ask-guppi` apart from the same call of another agent.

Then:
The main agent starts `ask-guppi` through the Agent tool for that test, with a prompt that says the calls it asks for are a test of that hook.
**＋** In Work Mode the main agent starts `ask-guppi` for no other reason.
**－** A test of a hook that judges the calls of every agent alike starts no `ask-guppi`.
**－** The run of `ask-guppi` at `/pre-spec` keeps the form that `rule-prespec` sets.

## Result

2026-10-31, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
