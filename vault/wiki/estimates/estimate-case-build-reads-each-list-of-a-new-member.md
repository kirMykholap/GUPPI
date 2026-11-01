---
type: estimate
kind: QA
status: pending
target: "[[rule-case-build]]"
purpose: Whether case-guppi, when its Case adds a member to a list that texts spell out one by one, a hook of an event, a command or a list in a comment or docstring of code among them, searches for a member already in the list, enters each text that would miss the new member in the Case or names it in context, and names that search in context
method: "by hand, after the first build of case-guppi in a later session whose Case adds a member to a list that texts spell out one by one: the agent transcript of that build under ~/.claude/projects/ read for its search of a member that stands in the list already and the hits it read, and its case file read for each text that lists the members and for the search named in context, both against the Criterion, recorded in one estimate line with the transcript and the case file"
checked: 2026-10-31
origin: raw/2026-10-30/2345/ledger.md#case-948.1
sprint: plugin
created: 2026-10-30
tags: [session, workflow, harness, case-build]
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case that adds a member to a list that texts spell out one by one, such as a key of an item, a kind, a status, a field, a hook of an event, a command or an item of a list in a comment or a docstring of code, and is about to answer with its summary.

Then:
It searches the live pages of `vault/wiki/` outside `decisions/`, `.claude/` and `.guppi/guppi/` for a member that stands in the list already.
**＋** It reads each hit that lists the members of the list.
**＋** A hit in a comment or a docstring of code under `.guppi/guppi/` that lists the members is read like a hit in a page.
**＋** Each text that lists the members and would miss the new member enters the Case, or the `context` of the Case names it and says why it stands.
**＋** The `context` of the Case names that search: the member it searched for, its pattern, its paths, and each file it printed or the count it printed.
**－** A hit in a History line, in `log.md` or in `brief.md` is not read.

## Result

2026-10-31, Retro of session 0431, .claude/agents/case-guppi.md line 25, the build of Case 956.1 (subagents/agent-ad69e15a458d77050.jsonl of session 8727d5ce) and the findings of ask-guppi at its /pre-spec (agent-a3a2b4d5034e84cde.jsonl line 597): the Case adds guppi libreport to the SubagentStop hooks, and its case-guppi ran no search of vault/wiki/, .claude/ and .guppi/guppi/ for a hook that stands in the list already; it read settings.json, rule-hook-registry.md and casecheck.py whole, but not the docstring of .guppi/guppi/cli.py, which lists every hook command, and the Case names that list nowhere (Work Mode added libreport to it); ask-guppi: 0 of 12 findings are a Case that adds a member and misses a text that lists the members

## History

- 2026-10-31 created · [[decision-case-948.1]]
- 2026-10-31 updated: the Criterion written back unchanged; the method reads the live Render with the findings of the first /pre-spec whose plan holds a Case that adds a member to a list, in one estimate line, with no Retro part · [[decision-case-950.1]]
- 2026-10-31 updated: the method reads the build of Case 956 and the /pre-spec of session 0431 in their transcripts, the Criterion written back unchanged · [[decision-case-961.3]]
- 2026-10-31 status: pending → failed · raw/2026-10-31/0431/ledger.md#L47
- 2026-10-31 deferred · [[decision-case-971]]
- 2026-11-01 deferred · [[decision-case-976]]
- 2026-11-01 defer by decision-case-971 superseded · [[decision-case-979]]
- 2026-11-01 defer by decision-case-976 superseded · [[decision-case-979]]
- 2026-11-01 updated: the Criterion replaced whole — the list names a hook of an event, a command and a list in a comment or docstring of code, and context names the search; the purpose and method set anew, the reading after the first build of a later session that adds a member to a list · [[decision-case-979]]
