---
type: estimate
kind: QA
status: passed
target: "[[entity-sprint-plugin]]"
purpose: Whether the case-guppi that built the Case adding .guppi/guppi/frontierguard.py and its test, in session 2155, made and named in context each search and reading for the folders of a new file that rule-case-build sets; read once
method: "by hand, in the Work Mode of the session that creates this Estimate: the agent transcript ~/.claude/projects/c--PROJECTS-GUPPI/c818d971-be31-4157-ab5d-802bd511827f/subagents/agent-aaf1016f261a07c9b.jsonl searched by a Grep with lines of context for each search and reading of the Criterion, and the case file vault/archive/plugin/2026-11-02/2155/raw/cases/case-1012.md read for the list of them in its context; the count, the transcript and the case file in the estimate line"
origin: raw/2026-11-03/1825/ledger.md#case-1019.3
sprint: plugin
created: 2026-11-03
tags: [sprint, case-build]
once: true
---

## Criterion

When:
The agent transcript `~/.claude/projects/c--PROJECTS-GUPPI/c818d971-be31-4157-ab5d-802bd511827f/subagents/agent-aaf1016f261a07c9b.jsonl` of the `case-guppi` that built the Case adding `.guppi/guppi/frontierguard.py` and `.guppi/tests/test_frontierguard.py`, and its case file `vault/archive/plugin/2026-11-02/2155/raw/cases/case-1012.md`, are read once against this Criterion.

Then:
That build searched `.guppi/guppi/`, `.claude/` and `vault/wiki/rules/` for the path of each folder that holds `.guppi/guppi/frontierguard.py` or `.guppi/tests/test_frontierguard.py`.
**＋** It searched `.guppi/guppi/` and `.guppi/tests/` for the calls that walk a folder, such as `os.walk`, `rglob`, `glob` and `iterdir`.
**＋** It read each ignore file of git in a folder that holds those files.
**＋** It read each reader that takes every file of such a folder.
**＋** Each reader that those files make wrong entered the Case of `vault/archive/plugin/2026-11-02/2155/raw/cases/case-1012.md`, or its `context` names it and says why it stands.
**＋** That `context` names each of those searches, with its pattern, its paths and each file it printed or the count it printed, and each ignore file of git and each reader it read, with whether those files make it wrong.

## Result

2026-11-03, Work Mode of session 1825, ~/.claude/projects/c--PROJECTS-GUPPI/c818d971-be31-4157-ab5d-802bd511827f/subagents/agent-aaf1016f261a07c9b.jsonl (606 lines, 2 matches of Build Case 1012) listed by its tool calls, and vault/archive/plugin/2026-11-02/2155/raw/cases/case-1012.md read: the build ran Greps of \.guppi/guppi and \.guppi/tests over {.guppi/guppi,.claude,vault/wiki/rules}/** (counts 81 and 52) and of the bare names guppi/ and tests/ (47 and 38), Greps of os\.walk|rglob\(|\.glob\(|iterdir\( over .guppi/guppi and .guppi/tests (29 files), read .guppi/.gitignore, ship.py and casecheck.py (tree_files, named_files), and its context (lines 8 and 10) names each search with its pattern, paths and count, each reader with why it stands; .guppi/guppi/ and .guppi/tests/ hold no .gitignore, and the root .gitignore was not read, judged here as no folder that holds the new files, git check-ignore printing neither file

## History

- 2026-11-03 created · [[decision-case-1019.3]]
- 2026-11-03 status: pending → passed · raw/2026-11-03/1825/ledger.md#L14
