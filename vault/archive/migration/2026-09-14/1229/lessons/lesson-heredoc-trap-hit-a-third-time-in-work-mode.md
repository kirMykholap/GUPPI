---
type: lesson
kind: error
root_cause: "the same trap as lesson-bash-tool-heredoc-escapes-interpreted and lesson-heredoc-trap-hit-twice-with-its-lesson-live, with both lessons and insight-session-vault-knowledge-not-loaded (severity 3) live: nothing puts the lesson in front of the agent at the moment it reaches for the Bash tool with a heredoc, and the agent reached for it first each time."
status: archived
insight: "[[insight-session-vault-knowledge-not-loaded]]"
origin: raw/2026-09-14/0747/ledger.md#L51
sprint: migration
created: 2026-09-14
tags: [harness, workflow, tests]
---

## Trigger

three edit scripts of Work Mode in session M, passed to the Bash tool as heredocs, had their backslash-n sequences turned into real newlines — a newline argument in tests/test_generate.py, a strip call in guppi/generate.py, the search strings of a test-editing script — each caught by a SyntaxError or a failed assertion; the agent then wrote the scripts with the Write tool.

## Root cause

the same trap as lesson-bash-tool-heredoc-escapes-interpreted and lesson-heredoc-trap-hit-twice-with-its-lesson-live, with both lessons and insight-session-vault-knowledge-not-loaded (severity 3) live: nothing puts the lesson in front of the agent at the moment it reaches for the Bash tool with a heredoc, and the agent reached for it first each time.

## Insight

- [[insight-session-vault-knowledge-not-loaded]]

## History

- 2026-09-14 created · raw/2026-09-14/0747/ledger.md#L51
- 2026-09-14 updated: clustered under insight-session-vault-knowledge-not-loaded · raw/2026-09-14/0747/ledger.md#L51
- 2026-09-14 archived · insight actioned
- 2026-09-14 archived · cleanup
