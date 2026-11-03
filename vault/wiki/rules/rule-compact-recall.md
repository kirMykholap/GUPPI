---
type: rule
kind: Leaf
purpose: Prevents a working session from going on after a compaction without the texts /hi loads, the Frontier and the Spec in its context
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/recall.py, .guppi/guppi/cli.py, .guppi/tests/test_recall.py, .claude/settings.json]
parent: "[[rule-session-start]]"
estimates: ["[[estimate-compact-recall-reloads]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, hooks, harness]
core: true
---

## Purpose

Prevents a working session from going on after a compaction without the texts `/hi` loads, the Frontier and the Spec in its context. `/hi` loads the session's texts once, through the `@` lines of its skill; a compaction keeps `CLAUDE.md` and a capped part of the skill's body, and the rest survives only in the summary. This hook fires on `SessionStart` with `source: compact` and prints what to read back: the paths of the files `/hi` imports, the session's `frontier.md` and its Spec, and the Frontier's text itself. Paths, not texts: a hook's stdout over 10,000 characters is saved to a file and the agent gets a preview.

## History

- 2026-11-03 shipped with GUPPI
