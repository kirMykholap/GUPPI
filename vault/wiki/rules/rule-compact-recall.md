---
type: rule
kind: Leaf
purpose: Prevents a working session from going on after a compaction without the Case schema, the Frontier and the Spec in its context
status: draft
enforcement: hook
implementation_ref: [guppi/recall.py, guppi/cli.py, tests/test_recall.py, .claude/settings.json]
parent: "[[rule-session-start]]"
estimates: ["[[estimate-compact-recall-reloads]]"]
origin: raw/2026-09-21/0019/ledger.md#case-287
sprint: migration
created: 2026-09-21
tags: [session, hooks, harness]
---

## Purpose

Prevents a working session from going on after a compaction without the Case schema, the Frontier and the Spec in its context. `/hi` loads the session's texts once, through the `@` lines of its skill; a compaction keeps `CLAUDE.md` and a capped part of the skill's body, and the rest survives only in the summary. This hook fires on `SessionStart` with `source: compact` and prints what to read back: the paths of the files `/hi` imports, the session's `frontier.md` and its Spec, and the Frontier's text itself. Paths, not texts: a hook's stdout over 10,000 characters is saved to a file and the agent gets a preview (case 287).

## How it works

`uv run guppi recall`, registered on `SessionStart` with the matcher `compact` (`rule-hook-registry`). Reads the payload from stdin; with a `source` other than `compact` or without a `hi` in the session's window — `session_dir` of `guppi/ledger.py`, the ledger hook's own — it prints nothing, exit 0. Otherwise stdout holds one header line naming the time and the session's folder, then one path per line: the `@` lines of `.claude/skills/hi/SKILL.md` in their order, the folder's `frontier.md` when it exists, the Spec — `spec.md` of the folder, or before the approval the plan file the event log names last under `.claude/plans/`, as `guppi gate` finds it (case 122) — then `Frontier:` and the text of `frontier.md`. The list of files is the skill file's, never a copy in the code. Exit 0 always; the hook writes nothing.

## History

- 2026-09-21 created · [[decision-case-287]]
- 2026-09-21 estimate estimate-compact-recall-reloads added · [[decision-case-287]]
- 2026-09-22 status: draft → built · cascade
- 2026-09-29 status: built → draft · cascade
