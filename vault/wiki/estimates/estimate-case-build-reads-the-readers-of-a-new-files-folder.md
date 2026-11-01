---
type: estimate
kind: QA
status: failed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, when a task of its Case adds a file that is no page, searches for the paths of the folders that hold it and for the calls that walk a folder, reads the ignore files of git there and each reader that takes every file of such a folder, and enters each one the new file makes wrong in the Case or names it in context
method: "by hand, after the /pre-spec of the first session whose case-guppi runs on the Render of rule-case-build that holds the sentence on the readers of the folder of a new file and in which a Case adds a file that is no page of vault/wiki/: the agent transcript of the case-guppi of that Case, read for each search and reading of the Criterion, and the findings of ask-guppi at that /pre-spec, read in its agent transcript, for a Case that adds a file and misses a reader of its folder; both under ~/.claude/projects/, the count and the transcripts in the estimate line"
checked: 2026-11-01
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
**－** A page that a `create` adds under `vault/wiki/` starts no such search.

## Result

2026-11-01, Work reading of session 2038, the case-guppi of Case 987 in ~/.claude/projects/c--PROJECTS-GUPPI/cb575daf-7b4e-455c-a22c-1fcffcbdc234/subagents/agent-a5bbc3a9ce87b6a82.jsonl, four passes, and the ask-guppi of /pre-spec in agent-ab3847b0434506da9.jsonl: of 8 searches and readings for the new file .claude/skills/approve-spec/SKILL.md, 2 done (the folder-path Grep and the walk Grep over .guppi/guppi/), 1 in part (ship.py tree_files seen by its grep line, its body not read), 5 missing (the folder-path Grep over .claude/ and over vault/wiki/rules/, the walk Grep over .guppi/tests/, the root .gitignore, callers() of .guppi/tests/test_guppi_package.py, which rglobs .claude); the context names ship.py, links.py, recall.py and two tests with a reason but not callers() or the root .gitignore; ask-guppi raised no finding on a reader of the folder

## History

- 2026-11-01 created · [[decision-case-974]]
- 2026-11-01 status: pending → failed · raw/2026-11-01/2038/ledger.md#L17
