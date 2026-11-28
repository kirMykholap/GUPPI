---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, when its Case adds a member to a list that texts spell out one by one, a hook of an event, a command or a list in a comment or docstring of code among them, searches for a member already in the list, enters each text that would miss the new member in the Case or names it in context, and names that search in context
method: "by hand, after the first build of case-guppi in a later session whose Case adds a member to a list that texts spell out one by one: the agent transcript of that build under ~/.claude/projects/ read for its search of a member that stands in the list already and the hits it read, and its case file read for each text that lists the members and for the search named in context, both against the Criterion, recorded in one estimate line with the transcript and the case file"
checked: 2026-11-25
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [session, workflow, harness, case-build]
core: true
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case that adds a member to a list that texts spell out one by one, such as a key of an item, a kind, a status, a field, a hook of an event, a command or an item of a list in a comment or a docstring of code, and is about to answer with its summary.

Then:
It searches for a member that stands in the list already by one Grep that prints only the paths of the files, its path the root of the repository and its glob `{vault/wiki,.claude,.guppi/guppi}/**`.
**＋** It reads each hit that lists the members of the list.
**＋** A hit in a comment or a docstring of code under `.guppi/guppi/` that lists the members is read like a hit in a page.
**＋** Each text that lists the members and would miss the new member enters the Case, or the `context` of the Case names it and says why it stands.
**＋** The `context` of the Case names that search: the member it searched for, its pattern, its paths, and each file it printed or the count it printed.
**－** A hit in a History line, in `log.md` or in `brief.md` is not read.

## Result

2026-11-25, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
