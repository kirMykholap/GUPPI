---
type: lesson
kind: error
root_cause: the same trap as lesson-heredoc-trap-hit-a-third-time-in-work-mode, with Case 127 ratified in this very session and guppi bashguard written an hour later; the hook that refuses the heredoc enters settings.json only with the librarian's render, so nothing mechanical stood between the agent and the trap yet, and the auto-mode instruction to prefer Bash heredocs for file changes pointed straight at it
status: archived
insight: "[[insight-session-vault-knowledge-not-loaded]]"
origin: raw/2026-09-14/1029/ledger.md#L39
sprint: migration
created: 2026-09-14
tags: [hooks, harness, tests]
---

## Trigger

two edit scripts of Work Mode in session N, passed to the Bash tool as heredocs, had their backslash sequences turned into real newlines — three assertion strings in tests/test_event.py split across lines, a replace target in a test_gate edit never matched — each caught by a SyntaxError or a failed assert; the fix was a script written with the Write tool and run by path, and Edit

## Root cause

the same trap as lesson-heredoc-trap-hit-a-third-time-in-work-mode, with Case 127 ratified in this very session and guppi bashguard written an hour later; the hook that refuses the heredoc enters settings.json only with the librarian's render, so nothing mechanical stood between the agent and the trap yet, and the auto-mode instruction to prefer Bash heredocs for file changes pointed straight at it

## Insight

- [[insight-session-vault-knowledge-not-loaded]]

## History

- 2026-09-14 created · raw/2026-09-14/1029/ledger.md#L39
- 2026-09-14 updated: clustered under insight-session-vault-knowledge-not-loaded · raw/2026-09-14/1029/ledger.md#L39
- 2026-09-14 archived · insight actioned
- 2026-09-14 archived · cleanup
