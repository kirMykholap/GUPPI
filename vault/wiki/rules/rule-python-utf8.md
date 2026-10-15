---
type: rule
kind: Leaf
purpose: Prevents a Python script that a session runs on Windows from printing through the code page of the locale, where a dash reaches the agent as U+FFFD and a character outside the code page stops the script
status: built
enforcement: render
governs: .claude/settings.json
render_mode: partial
parent: "[[rule-settings]]"
estimates: ["[[estimate-python-utf8-output-intact]]"]
origin: raw/2026-09-30/0248/ledger.md#case-534.1
sprint: migration
created: 2026-09-30
tags: [harness, session]
core: true
---

## Purpose

Prevents a Python script that a session runs on Windows from printing through the code page of the locale (measured cp1252, `.guppi/guppi/cli.py`). The Bash tool reads the output as UTF-8: a character outside the code page stops the script at the print, and a character inside it, such as the dash, reaches the agent as U+FFFD without an error. A reading of 2026-09-30 took that mark for a defect of `guppi context --prompt`, while the transcript held the dash (case 534). `PYTHONUTF8=1` in the `env` of `.claude/settings.json` puts every Python process of the session in UTF-8 mode: the console, the pipes and the default encoding of a file opened without one. The `guppi` commands set UTF-8 on their own stdout and stderr in `.guppi/guppi/cli.py` and do not depend on it.

## Render

<!-- rule-python-utf8 -->
  "env": {
    "PYTHONUTF8": "1"
  }
<!-- /rule-python-utf8 -->

## History

- 2026-09-30 created · [[decision-case-534.1]]
- 2026-09-30 estimate estimate-python-utf8-output-intact added · [[decision-case-534.1]]
- 2026-10-01 status: draft → built · cascade
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
