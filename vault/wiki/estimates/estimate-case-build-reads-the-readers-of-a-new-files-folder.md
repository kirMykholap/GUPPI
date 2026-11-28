---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, when a task of its Case adds a file that is no page, searches for the paths of the folders from its own up to the root of the repository but for the root, and for the calls that walk a folder, reads the ignore file of git and each reader that takes every file of a folder in each folder from its own up to the root, the root included, enters each one the new file makes wrong in the Case or names it in context, and names in context each of those searches and readings
method: by hand, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec read against the Criterion, recorded in the estimate line
checked: 2026-11-04
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [session, workflow, harness, case-build]
core: true
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

2026-11-04, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
