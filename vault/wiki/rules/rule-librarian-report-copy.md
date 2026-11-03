---
type: rule
kind: Leaf
purpose: Prevents the librarian's report from standing in no file when Claude Code refuses the Write of a report file by a subagent
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/libreport.py, .guppi/tests/test_libreport.py, .claude/settings.json]
parent: "[[rule-documentation]]"
estimates: ["[[estimate-librarian-report-copy-writes-the-file]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, librarian]
core: true
---

## Purpose

Prevents the librarian's report from standing in no file when Claude Code refuses the `Write` of a report file by a subagent. Claude Code refused the librarian's `Write` of `report.md` with the message that subagents return findings as text and write no report files. The `SubagentStop` hook `uv run --project .guppi guppi libreport` copies the last output that `librarian-guppi` returned into `report.md` in the session folder by its own code, so no `Write` call of a subagent is made, and `/handoff` or `/box` shows that file and commits it.

## History

- 2026-11-03 shipped with GUPPI
