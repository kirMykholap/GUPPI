---
type: rule
kind: Leaf
purpose: Prevents a line of the Frontier from keeping its open box beside a closer, so that the line reads as open though the agent closed it
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/frontierguard.py, .guppi/tests/test_frontierguard.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-frontier-hook-refuses-an-open-box-with-a-closer]]"]
origin: raw/2026-11-02/2155/ledger.md#case-1012
sprint: plugin
created: 2026-11-02
tags: [hooks, harness, session]
core: true
---

## Purpose

Prevents a line of the Frontier from keeping its open box beside a closer, so that the line reads as open though the agent closed it. The main agent closed lines of `frontier.md` by an `Edit` that matched only the tail of the line and appended the closer, the box left `[ ]`, and `/pre-spec` then printed each line as open (as set in case 1012). A text the agent has to remember did not stop it; the `PreToolUse` hook `uv run --project .guppi guppi frontierguard` refuses such an `Edit`, `Write` or `MultiEdit` before it runs, and its mechanism stands in the docstring of `.guppi/guppi/frontierguard.py`.

## History

- 2026-11-03 created · [[decision-case-1012]]
- 2026-11-03 estimate estimate-frontier-hook-refuses-an-open-box-with-a-closer added · [[decision-case-1012]]
- 2026-11-03 status: draft → built · cascade
