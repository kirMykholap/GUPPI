---
type: rule
kind: Leaf
purpose: Prevents a Case builder from reading a graph of links that is missing or older than the start of its session
status: draft
enforcement: hook
implementation_ref: [.guppi/guppi/links.py, .guppi/tests/test_links.py, .claude/settings.json]
parent: "[[rule-harness]]"
estimates: ["[[estimate-link-graph-at-session-start-writes-the-file]]"]
applies_to: ["[[entity-link-graph]]"]
origin: raw/2026-10-31/1831/ledger.md#case-967.3
sprint: plugin
created: 2026-10-31
tags: [harness, session]
core: true
---

## Purpose

Prevents a Case builder from reading a graph of links that is missing or older than the start of its session. The builder has no tool that runs a command, so `uv run --project .guppi guppi links --write` runs on `SessionStart` and writes the whole graph into `.guppi/links.md`, which git ignores; the builder reads the block of each page and file its Case changes by a Grep. Pages and rendered files change at the librarian's run, so the file written at the start stays current through the session. The hook takes the text of each rendered file as `guppi render` writes it, and an error prints one line and stops no session (as set in case 967.3).

## History

- 2026-10-31 created · [[decision-case-967.3]]
- 2026-10-31 estimate estimate-link-graph-at-session-start-writes-the-file added · [[decision-case-967.3]]
