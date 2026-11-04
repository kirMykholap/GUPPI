---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, when a task of its Case adds a file that is no page, searches for the paths of the folders from its own up to the root of the repository but for the root, and for the calls that walk a folder, reads the ignore file of git and each reader that takes every file of a folder in each folder from its own up to the root, the root included, enters each one the new file makes wrong in the Case or names it in context, and names in context each of those searches and readings
method: by hand, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec read against the Criterion, recorded in the estimate line
checked: 2026-11-04
origin: raw/2026-10-31/2307/ledger.md#case-974
sprint: plugin
created: 2026-10-31
tags: [session, workflow, harness, case-build]
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case with a task that adds a file that is no page of `vault/wiki/`, and is about to answer with its summary.

Then:
It searches `.guppi/guppi/`, `.claude/` and the Rule pages of `vault/wiki/` for the path and the bare name of each folder from the folder of the new file up to the root of the repository.
**＋** It searches `.guppi/guppi/` and `.guppi/tests/` for the calls that walk a folder, such as `os.walk`, `rglob`, `glob` and `iterdir`.
**＋** It reads each ignore file of git in each folder from the folder of the new file up to the root of the repository, the root included.
**＋** It reads each reader that takes every file of a folder from the folder of the new file up to the root of the repository, the root included.
**＋** Each reader that the new file makes wrong enters the Case, or the `context` of the Case names it and says why it stands.
**＋** The `context` of the Case names each of those searches, with its pattern, its paths and each file it printed or the count it printed, and each ignore file of git and each reader it read, with whether the new file makes it wrong.
**－** The root of the repository, which has no path, gets no search for its path.
**－** A page that a `create` adds under `vault/wiki/` starts no such search.

## Result

2026-11-04, Retro of session 0358, the new Render of rule-case-build in the Spec, Case 1025.2, read against its Criterion: the three replace items match the live sentence of line 49 of vault/wiki/rules/rule-case-build.md, and with them the sentence searches the path and the bare name of each folder from the folder of the new file up to the root, the root left out, searches the calls that walk a folder, reads each .gitignore and each reader of each folder up to the root, the root included, enters each reader made wrong or names it in context, has context name each search with its pattern, paths and files or count and each ignore file and reader read, and starts for a file that is no page of vault/wiki/ only

## History

- 2026-11-01 created · [[decision-case-974]]
- 2026-11-01 status: pending → failed · raw/2026-11-01/2038/ledger.md#L17
- 2026-11-02 updated: the Criterion replaced whole — the context names each search and reading for the folders of a new file · [[decision-case-995.1]]
- 2026-11-03 updated: the method reads the Render of rule-case-build and no transcript; the Criterion written again as it stood; the build of session 2155 is read once by an Estimate of entity-sprint-plugin · [[decision-case-1019.2]]
- 2026-11-03 status: pending → passed · raw/2026-11-03/1825/ledger.md#L13
- 2026-11-04 updated: the Criterion replaced whole — the searches and readings for the folders of a new file go up to the root of the repository, the root left out of the path search · [[decision-case-1025.2]]
- 2026-11-04 status: pending → passed · raw/2026-11-04/0358/ledger.md#L30
