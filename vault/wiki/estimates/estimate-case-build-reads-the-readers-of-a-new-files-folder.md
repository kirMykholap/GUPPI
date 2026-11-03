---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, when a task of its Case adds a file that is no page, searches for the paths of the folders that hold it and for the calls that walk a folder, reads the ignore files of git there and each reader that takes every file of such a folder, enters each one the new file makes wrong in the Case or names it in context, and names in context each of those searches and readings
method: "by hand: the Render of rule-case-build in .claude/agents/case-guppi.md read against the Criterion, recorded in the estimate line"
checked: 2026-11-03
origin: raw/2026-10-31/2307/ledger.md#case-974
sprint: plugin
created: 2026-10-31
tags: [session, workflow, harness, case-build]
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case with a task that adds a file that is no page of `vault/wiki/`, and is about to answer with its summary.

Then:
It searches `.guppi/guppi/`, `.claude/` and the Rule pages of `vault/wiki/` for the path of each folder that holds the new file.
**＋** It searches `.guppi/guppi/` and `.guppi/tests/` for the calls that walk a folder, such as `os.walk`, `rglob`, `glob` and `iterdir`.
**＋** It reads each ignore file of git in a folder that holds the new file.
**＋** It reads each reader that takes every file of a folder that holds the new file.
**＋** Each reader that the new file makes wrong enters the Case, or the `context` of the Case names it and says why it stands.
**＋** The `context` of the Case names each of those searches, with its pattern, its paths and each file it printed or the count it printed, and each ignore file of git and each reader it read, with whether the new file makes it wrong.
**－** A page that a `create` adds under `vault/wiki/` starts no such search.

## Result

2026-11-03, Retro of session 1825, .claude/agents/case-guppi.md line 25 read against the Criterion: for a task that adds a file that is no page of vault/wiki/ it sets a Grep of .guppi/guppi/, .claude/ and vault/wiki/rules/ for the path of each folder that holds it and its bare name, a Grep of .guppi/guppi/ and .guppi/tests/ for os.walk, rglob, glob and iterdir, a read of each .gitignore in a folder that holds it and of each reader that takes every file of such a folder, each reader made wrong entering the Case or named in context with why it stands, and context naming each search with its pattern, paths and files or count, each .gitignore and each reader read

## History

- 2026-11-01 created · [[decision-case-974]]
- 2026-11-01 status: pending → failed · raw/2026-11-01/2038/ledger.md#L17
- 2026-11-02 updated: the Criterion replaced whole — the context names each search and reading for the folders of a new file · [[decision-case-995.1]]
- 2026-11-03 updated: the method reads the Render of rule-case-build and no transcript; the Criterion written again as it stood; the build of session 2155 is read once by an Estimate of entity-sprint-plugin · [[decision-case-1019.2]]
- 2026-11-03 status: pending → passed · raw/2026-11-03/1825/ledger.md#L13
