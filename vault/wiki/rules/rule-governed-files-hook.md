---
type: rule
kind: Leaf
purpose: Prevents a harness file rendered from a Rule page from being edited by hand
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/guard.py, .guppi/tests/test_guard.py, .claude/settings.json]
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
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-30 updated: ## How it works left the Leaf, its mechanism in the docstring of .guppi/guppi/guard.py · [[decision-case-942.1]]
