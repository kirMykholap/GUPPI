---
type: lesson
kind: error
root_cause: the lesson is a page of the vault and reaches the session only when the agent thinks to read it; nothing in the harness puts a lesson about a tool in front of the agent at the moment it reaches for that tool, so the same trap is hit once per session until the rule lives in a skill, a hook or CLAUDE.md
status: archived
insight: "[[insight-session-vault-knowledge-not-loaded]]"
origin: raw/2026-09-13/0652/ledger.md#L3
sprint: migration
created: 2026-09-13
tags: [harness, workflow, tests]
---

## Trigger

two python edit scripts passed to the Bash tool as heredocs in Work Mode of session L had their backslash-n sequences turned into real newlines — an f-string in tests/test_ledger.py split across three lines, a seed helper in tests/test_archive.py left unreplaced — while lesson-bash-tool-heredoc-escapes-interpreted, written in session I and quoted by lesson-vault-lesson-absent-at-the-moment-it-applies in session K, names the trap and the way around it; the fix was the way the lesson names, a script written with the Write tool and run by path

## Root cause

the lesson is a page of the vault and reaches the session only when the agent thinks to read it; nothing in the harness puts a lesson about a tool in front of the agent at the moment it reaches for that tool, so the same trap is hit once per session until the rule lives in a skill, a hook or CLAUDE.md

## Insight

- [[insight-session-vault-knowledge-not-loaded]]

## History

- 2026-09-13 created · raw/2026-09-13/0652/ledger.md#L3
- 2026-09-13 updated: clustered under insight-session-vault-knowledge-not-loaded · raw/2026-09-13/0652/ledger.md#L3
- 2026-09-14 insight section derived
- 2026-09-14 archived · insight actioned
- 2026-09-14 archived · cleanup
