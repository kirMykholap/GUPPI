---
type: rule
kind: Leaf
purpose: Prevents a line of the Frontier from keeping its open box beside a closer, or its closed box [x] or [-] with no closer, so that the box and the closer of a line change in one edit
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/frontierguard.py, .guppi/tests/test_frontierguard.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-frontier-hook-refuses-an-open-box-with-a-closer]]", "[[estimate-frontier-hook-refuses-a-shell-command-on-the-frontier]]"]
origin: raw/2026-11-02/2155/ledger.md#case-1012
sprint: plugin
created: 2026-11-02
tags: [hooks, harness, session]
core: true
---

## Purpose

Prevents a line of the Frontier from keeping its open box beside a closer, or its closed box [x] or [-] with no closer, so that the box and the closer of a line change in one edit. The main agent closed lines of `frontier.md` by an `Edit` that matched only the tail of the line and appended the closer, the box left `[ ]`, and `/pre-spec` then printed each line as open (as set in case 1012). A text the agent has to remember did not stop it; the `PreToolUse` hook `uv run --project .guppi guppi frontierguard` refuses such an `Edit`, `Write` or `MultiEdit` before it runs. The same hook refuses before it runs a `Bash` or `PowerShell` call whose command names `frontier.md`, since a box ticked alone through Bash got past the check of an edit (as set in case 1069.1). Its mechanism stands in the docstring of `.guppi/guppi/frontierguard.py`.

## History

- 2026-11-03 created · [[decision-case-1012]]
- 2026-11-03 estimate estimate-frontier-hook-refuses-an-open-box-with-a-closer added · [[decision-case-1012]]
- 2026-11-03 status: draft → built · cascade
- 2026-11-26 updated: the hook refuses a Bash or PowerShell command that names frontier.md · [[decision-case-1069.1]]
- 2026-11-26 estimate estimate-frontier-hook-refuses-a-shell-command-on-the-frontier added · [[decision-case-1069.1]]
- 2026-11-26 updated: the hook refuses a closed box with no closer too · [[decision-case-1069.2]]
