---
type: rule
kind: Leaf
purpose: Prevents a line of the Frontier from keeping its open box beside a closer, or its closed box [x] or [-] with no closer, so that the box and the closer of a line change in one edit
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/frontierguard.py, .guppi/tests/test_frontierguard.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-frontier-hook-refuses-an-open-box-with-a-closer]]", "[[estimate-frontier-hook-refuses-a-shell-command-on-the-frontier]]"]
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [hooks, harness, session]
core: true
---

## Purpose

Prevents a line of the Frontier from keeping its open box beside a closer, or its closed box [x] or [-] with no closer, so that the box and the closer of a line change in one edit. The main agent closed lines of `frontier.md` by an `Edit` that matched only the tail of the line and appended the closer, the box left `[ ]`, and `/pre-spec` then printed each line as open. A text the agent has to remember did not stop it; the `PreToolUse` hook `uv run --project .guppi guppi frontierguard` refuses such an `Edit`, `Write` or `MultiEdit` before it runs. The same hook refuses before it runs a `Bash` or `PowerShell` call whose command names `frontier.md`, since a box ticked alone through Bash got past the check of an edit. Its mechanism stands in the docstring of `.guppi/guppi/frontierguard.py`.

## History

- 2026-11-28 shipped with GUPPI
