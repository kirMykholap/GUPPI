---
type: rule
kind: Leaf
purpose: Prevents a harness file rendered from a Rule page from being edited by hand
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/guard.py, .guppi/tests/test_guard.py, .claude/settings.json]
parent: "[[rule-harness]]"
estimates: ["[[estimate-governed-files-hook-refuses]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, render]
core: true
---

## Purpose

Prevents a harness file rendered from a Rule page from being edited by hand. The
renderer makes the page and the file one text; an edit to the file alone is lost at
the next render, and what it carried was ratified for the page, not the file.

## History

- 2026-11-03 shipped with GUPPI
