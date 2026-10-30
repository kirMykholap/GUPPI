---
type: rule
kind: Leaf
purpose: Prevents an agent from reading the History of a vault page it did not ask for
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/pageread.py, .guppi/guppi/pages.py, .guppi/tests/test_pageread.py, .claude/settings.json]
parent: "[[rule-harness]]"
estimates: ["[[estimate-page-read-cuts-the-history]]"]
origin: raw/2026-09-25/1228/ledger.md#case-420.1
sprint: migration
created: 2026-09-25
tags: [hooks, harness]
core: true
---

## Purpose

Prevents an agent from reading the History of a vault page it did not ask for. Every page ends with `## History`, the record of its changes; it is a third of the text of a rule and a quarter of an Estimate, and an agent that reads it takes old wordings for the current rule (an agent read the order of the `Stop` hooks from the History of `rule-hook-registry`, in session 0051, [[lesson-hooks-matching-hooks-of-one-event-run-in-parallel]]). The page keeps its History, whole in Obsidian; a hook cuts it from a read, and the agent reads it only by asking for its lines. The cut is a hook and not a file under `.claude/rules/`, since such a file is text that the agent may follow (a rule in `.claude/rules/` was weighed and not taken, case 420.1).

## History

- 2026-09-25 created · [[decision-case-420.1]]
- 2026-09-25 estimate estimate-page-read-cuts-the-history added · [[decision-case-420.1]]
- 2026-09-25 status: draft → built · cascade
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-14 updated: the session stands in the bracket of the lesson · [[decision-case-809]]
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-17 updated: the event of the Purpose moves into the bracket of its pointer · [[decision-case-875]]
- 2026-10-26 updated: the reason for a hook given without the old doubt, the weighing in the bracket of its case · [[decision-case-881.17]]
- 2026-10-30 updated: ## How it works left the Leaf, its mechanism in the docstring of .guppi/guppi/pageread.py · [[decision-case-942.1]]
