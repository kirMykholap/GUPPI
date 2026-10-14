---
type: rule
kind: Leaf
purpose: Prevents a harness file rendered from a Rule page from being edited by hand
status: built
enforcement: hook
implementation_ref: [guppi/guard.py, tests/test_guard.py, .claude/settings.json]
parent: "[[rule-harness]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [hooks, harness, render]
core: true
---

## Purpose

Prevents a harness file rendered from a Rule page from being edited by hand. The
renderer makes the page and the file one text; an edit to the file alone is lost at
the next render, and what it carried was ratified for the page, not the file.

## How it works

`uv run guppi guard` on `PreToolUse` of `Edit`, `Write` and `MultiEdit`. It reads
the `governs` field of every live Rule page under `vault/wiki/rules/`. A call whose
`file_path` is a governed path exits 2 with the rule's slug and the file, which
blocks the tool, and one line goes to `vault/raw/<date>/event_log.md` before that:
a blocked call has no `PostToolUse`, so a refusal the hook does not write is
nowhere. No governed file has a hand-written part; `CLAUDE.md` is a full
Render. Any other tool, an ungoverned path, or a payload the hook cannot
read: exit 0, the last with one line on stderr. `guppi render` writes through Bash
and passes; subagents inherit no project hook.

## History

- 2026-10-14 shipped with GUPPI
