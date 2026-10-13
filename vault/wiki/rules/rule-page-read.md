---
type: rule
kind: Leaf
purpose: Prevents an agent from reading the History of a vault page it did not ask for
status: built
enforcement: hook
implementation_ref: [guppi/pageread.py, guppi/pages.py, tests/test_pageread.py, .claude/settings.json]
parent: "[[rule-harness]]"
estimates: ["[[estimate-page-read-cuts-the-history]]"]
origin: raw/2026-09-25/1228/ledger.md#case-420.1
sprint: migration
created: 2026-09-25
tags: [hooks, harness]
core: true
---

## Purpose

Prevents an agent from reading the History of a vault page it did not ask for. Every page ends with `## History`, the record of its changes; it is a third of the text of a rule and a quarter of an Estimate, and an agent that reads it takes old wordings for the current rule — in session 0051 an agent read the order of the `Stop` hooks from the History of `rule-hook-registry` ([[lesson-hooks-matching-hooks-of-one-event-run-in-parallel]]). The page keeps its History, whole in Obsidian; a hook cuts it from a read, and the agent reads it only by asking for its lines. A rule in `.claude/rules/` was weighed and not taken: it is text the agent may follow, and whether it loads inside a subagent is not documented.

## How it works

`uv run guppi pageread` on `PreToolUse` of `Read`. For a file under `vault/wiki/` read with neither `offset` nor `limit`, it finds the line of the page's own `## History` heading by `pages.history_line` — the walk of `split_sections`, so a heading inside a render block does not count — and returns `updatedInput` with `limit` set to the line before it, with no permission decision. `uv run guppi pageread --after` on `PostToolUse` of `Read` adds one line of `additionalContext` after such a call: the History is cut, its first and last line, and a `Read` with `offset` at its first line shows it. A call with its own `offset` or `limit`, a file with no `## History` — `brief.md`, `sprint.md`, `glossary.md`, `log.md`, `case-schema.md` — and a file outside `vault/wiki/` pass unchanged. The page on disk is never changed. The hooks read stdin as UTF-8 and never raise; an error lets the call pass whole.

## History

- 2026-09-25 created · [[decision-case-420.1]]
- 2026-09-25 estimate estimate-page-read-cuts-the-history added · [[decision-case-420.1]]
- 2026-09-25 status: draft → built · cascade
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
