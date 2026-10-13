---
type: rule
kind: Leaf
purpose: Prevents a harness file rendered from a Rule page from being edited by hand
status: built
enforcement: hook
implementation_ref: [guppi/guard.py, tests/test_guard.py, .claude/settings.json]
parent: "[[rule-harness]]"
estimates: ["[[estimate-governed-files-hook-refuses]]"]
origin: raw/2026-09-12/ledger.md#case-59.6
sprint: migration
created: 2026-09-12
tags: [hooks, harness, render]
core: true
---

## Purpose

Prevents a harness file rendered from a Rule page from being edited by hand. The
renderer makes the page and the file one text; an edit to the file alone is lost at
the next render, and what it carried was ratified for the page, not the file
(case 56, `lesson-render-governed-file-updated-as-rule-class-file`).

## How it works

`uv run guppi guard` on `PreToolUse` of `Edit`, `Write` and `MultiEdit`. It reads
the `governs` field of every live Rule page under `vault/wiki/rules/`. A call whose
`file_path` is a governed path exits 2 with the rule's slug and the file, which
blocks the tool, and one line goes to `vault/raw/<date>/event_log.md` before that:
a blocked call has no `PostToolUse`, so a refusal the hook does not write is
nowhere (case 91). No governed file has a hand-written part; `CLAUDE.md` is a full
Render (case 59.8). Any other tool, an ungoverned path, or a payload the hook cannot
read: exit 0, the last with one line on stderr. `guppi render` writes through Bash
and passes; subagents inherit no project hook.

## History

- 2026-09-12 created · [[decision-case-59.6]]
- 2026-09-12 estimate estimate-governed-files-hook-refuses added · [[decision-case-71.1]]
- 2026-09-12 deferred · [[decision-case-83]]
- 2026-09-12 defer by decision-case-83 superseded · [[decision-case-91]]
- 2026-09-12 updated: the hook writes its own event line on a refusal (case 91) · [[decision-case-91]]
- 2026-09-12 status: draft → built · cascade
- 2026-09-29 status: built → draft · cascade
- 2026-10-01 status: draft → built · cascade
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
