---
type: rule
kind: Leaf
purpose: Prevents an agent from reading the History of a vault page it did not ask for
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/pageread.py, .guppi/guppi/pages.py, .guppi/tests/test_pageread.py, .claude/settings.json]
parent: "[[rule-harness]]"
estimates: ["[[estimate-page-read-cuts-the-history]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness]
core: true
---

## Purpose

Prevents an agent from reading the History of a vault page it did not ask for. Every page ends with `## History`, the record of its changes; it is a third of the text of a rule and a quarter of an Estimate, and an agent that reads it takes old wordings for the current rule. The page keeps its History, whole in Obsidian; a hook cuts it from a read, and the agent reads it only by asking for its lines. The cut is a hook and not a file under `.claude/rules/`, since such a file is text that the agent may follow.

## History

- 2026-11-03 shipped with GUPPI
