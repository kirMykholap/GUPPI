---
type: decision
case: "120"
status: archived
defer: ["[[rule-bash-guard]]"]
superseded_by: ["[[decision-case-127]]"]
origin: raw/2026-09-14/0747/ledger.md#case-120
sprint: migration
created: 2026-09-14
tags: []
---

## Context

`lesson-bash-tool-heredoc-escapes-interpreted` (session H), `lesson-heredoc-trap-hit-twice-with-its-lesson-live` (L), `lesson-heredoc-trap-hit-a-third-time-in-work-mode` (M): a heredoc passed to the Bash tool has its backslash escapes interpreted, and the agent reaches for a heredoc first every session, with the lesson live. The Insight's Proposal — pages of a phase carry its traps — is Case 119's; the trap itself has a mechanical fix.

## Problem

A lesson the agent has to remember is not a rule. A `PreToolUse Bash` hook that refuses a command whose heredoc body carries a backslash escape — or refuses a heredoc that writes a file at all, pointing at Write and Edit — makes the trap impossible instead of remembered.

## History

- 2026-09-14 created · raw/2026-09-14/0747/ledger.md#case-120
- 2026-09-14 superseded by decision-case-127 · [[decision-case-127]]
- 2026-09-14 archived · superseded
- 2026-09-14 archived · cleanup
