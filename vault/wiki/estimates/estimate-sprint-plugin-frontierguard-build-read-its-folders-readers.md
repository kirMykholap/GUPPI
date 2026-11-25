---
type: estimate
kind: QA
status: pending
target: "[[entity-sprint-plugin]]"
purpose: Whether a case-guppi build of the sprint plugin that adds a file outside vault/wiki/ makes and names in context each search and reading for the folders of the new file that rule-case-build sets, the root .gitignore included; passes once
method: "by hand, after a case-guppi build of the sprint plugin whose Case adds a file outside vault/wiki/: its agent transcript under ~/.claude/projects/ searched by a Grep with lines of context for each search and reading of the Criterion, and its case file read for the list of them in its context; the transcript, the case file and the result in the estimate line"
checked: 2026-11-04
origin: raw/2026-11-03/1825/ledger.md#case-1019.3
sprint: plugin
created: 2026-11-03
tags: [sprint, case-build]
once: true
---

## Criterion

When:
The agent transcript under `~/.claude/projects/` of a `case-guppi` build of the sprint `plugin` whose Case adds a file outside `vault/wiki/`, and its case file, are read against this Criterion.

Then:
That build searched `.guppi/guppi/`, `.claude/` and `vault/wiki/rules/` for the path of each folder that holds the new file, the root left out.
**＋** It searched `.guppi/guppi/` and `.guppi/tests/` for the calls that walk a folder, such as `os.walk`, `rglob`, `glob` and `iterdir`.
**＋** It read each ignore file of git in each folder from the folder of the new file up to the root of the repository, the root `.gitignore` included.
**＋** It read each reader that takes every file of such a folder.
**＋** Each reader that the new file makes wrong entered the Case, or its `context` names it and says why it stands.
**＋** That `context` names each of those searches, with its pattern, its paths and each file or count it printed, and each ignore file and reader it read, with whether the new file makes it wrong.
**－** Once one such reading passes, this Estimate is not read again.

## Result

2026-11-04, the person's decision, case 1025.1: the root folder holds both new files and git applies the root .gitignore to every file under it, so the root .gitignore is an ignore file of a folder that holds them, and the build did not read it; a reading of its lines in session 0358 found no pattern that matches either file.

2026-11-03, Work Mode of session 1825, ~/.claude/projects/c--PROJECTS-GUPPI/c818d971-be31-4157-ab5d-802bd511827f/subagents/agent-aaf1016f261a07c9b.jsonl (606 lines, 2 matches of Build Case 1012) listed by its tool calls, and vault/archive/plugin/2026-11-02/2155/raw/cases/case-1012.md read: the build ran Greps of \.guppi/guppi and \.guppi/tests over {.guppi/guppi,.claude,vault/wiki/rules}/** (counts 81 and 52) and of the bare names guppi/ and tests/ (47 and 38), Greps of os\.walk|rglob\(|\.glob\(|iterdir\( over .guppi/guppi and .guppi/tests (29 files), read .guppi/.gitignore, ship.py and casecheck.py (tree_files, named_files), and its context (lines 8 and 10) names each search with its pattern, paths and count, each reader with why it stands; .guppi/guppi/ and .guppi/tests/ hold no .gitignore, and the root .gitignore was not read, judged here as no folder that holds the new files, git check-ignore printing neither file

## History

- 2026-11-03 created · [[decision-case-1019.3]]
- 2026-11-03 status: pending → passed · raw/2026-11-03/1825/ledger.md#L14
- 2026-11-04 updated: failed by the person's decision: the root .gitignore is an ignore file of a folder that holds the new files, and the build did not read it · [[decision-case-1025.1]]
- 2026-11-25 updated: the Criterion replaced whole — a fresh build read, since the build of Case 1012 cannot pass · [[decision-case-1057.4]]
