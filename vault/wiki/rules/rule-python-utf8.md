---
type: rule
kind: Leaf
purpose: Prevents a Python script that a session runs on Windows from printing through the code page of the locale, where a dash reaches the agent as U+FFFD and a character outside the code page stops the script
status: built
enforcement: render
governs: .claude/settings.json
render_mode: partial
parent: "[[rule-settings]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [harness, session]
core: true
---

## Purpose

Prevents a Python script that a session runs on Windows from printing through the code page of the locale (measured cp1252, `guppi/cli.py`). The Bash tool reads the output as UTF-8: a character outside the code page stops the script at the print, and a character inside it, such as the dash, reaches the agent as U+FFFD without an error. A reading of 2026-09-30 took that mark for a defect of `guppi context --prompt`, while the transcript held the dash. `PYTHONUTF8=1` in the `env` of `.claude/settings.json` puts every Python process of the session in UTF-8 mode: the console, the pipes and the default encoding of a file opened without one. The `guppi` commands set UTF-8 on their own stdout and stderr in `guppi/cli.py` and do not depend on it.

## Render

<!-- rule-python-utf8 -->
  "env": {
    "PYTHONUTF8": "1"
  }
<!-- /rule-python-utf8 -->

## History

- 2026-10-14 shipped with GUPPI
