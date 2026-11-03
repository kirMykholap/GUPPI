---
type: rule
kind: Leaf
purpose: Prevents the handoff from starting on an uncommitted tree
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/gate.py, .guppi/tests/test_gate.py, .claude/settings.json]
parent: "[[rule-end-of-work]]"
estimates: ["[[estimate-retro-commit-gates]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, hooks, harness, git]
core: true
---

## Purpose

Prevents the handoff from starting on an uncommitted tree. An instruction to commit
before handoff is a step an agent can skip; a `PreToolUse` hook cannot be skipped.
The commit is what makes everything the librarian writes afterwards readable as a
separate layer.

## History

- 2026-11-03 shipped with GUPPI
