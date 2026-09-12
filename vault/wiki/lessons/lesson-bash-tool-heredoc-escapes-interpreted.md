---
type: lesson
kind: knowledge
root_cause: the tool's shell layer on Windows interprets backslash escapes before python reads the script, and the quoting of the heredoc marker does not protect them; a multi-line edit script is written to the session scratchpad with the Write tool and run as python path, and console output with characters outside cp1252 needs PYTHONIOENCODING=utf-8 or the script dies at the print
status: new
origin: raw/2026-09-12/ledger.md#L2
sprint: migration
created: 2026-09-12
tags: [harness]
---

## Trigger

a python - <<'EOF' heredoc in the Bash tool on this Windows machine turned "\n" inside the python source into a real newline and broke the edited file three times; a heredoc holding quotes and \| failed to parse with "unexpected EOF while looking for matching quote"

## Root cause

the tool's shell layer on Windows interprets backslash escapes before python reads the script, and the quoting of the heredoc marker does not protect them; a multi-line edit script is written to the session scratchpad with the Write tool and run as python path, and console output with characters outside cp1252 needs PYTHONIOENCODING=utf-8 or the script dies at the print

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#L2
