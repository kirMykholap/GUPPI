---
type: rule
kind: Leaf
purpose: Prevents the handoff from starting on an uncommitted tree
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/gate.py, .guppi/tests/test_gate.py, .claude/settings.json]
parent: "[[rule-end-of-work]]"
estimates: ["[[estimate-retro-commit-gates]]"]
origin: raw/2026-09-10/ledger.md#case-38.2
sprint: migration
created: 2026-09-10
tags: [session, workflow, hooks, harness, git]
core: true
---

## Purpose

Prevents the handoff from starting on an uncommitted tree. An instruction to commit
before handoff is a step an agent can skip; a `PreToolUse` hook cannot be skipped.
The commit is what makes everything the librarian writes afterwards readable as a
separate layer.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.2
- 2026-09-10 estimate estimate-retro-commit-gates added · raw/2026-09-10/ledger.md#case-38.2
- 2026-09-09 status: draft → built · cascade
- 2026-09-14 updated: the gate's second refusal, on an unwritten ledger line, named beside the tree check (case 132) · [[decision-case-132]]
- 2026-09-15 updated: the gate reads a typed /pre-task, /retro or /handoff from the UserPromptSubmit payload: same checks, same mark, exit 2 for the person (case 169.1) · [[decision-case-169.1]]
- 2026-09-15 status: built → draft · cascade
- 2026-09-16 updated: the gate refuses /retro when the session has no Spec and no ledger line — nothing to review (case 180) · [[decision-case-180]]
- 2026-09-16 status: draft → built · cascade
- 2026-09-29 status: built → draft · cascade
- 2026-09-30 updated: the refusal nothing to review on the agent's call names a stop, not a call in the next reply (case 531.15) · [[decision-case-531.15]]
- 2026-09-30 status: draft → built · cascade
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-14 updated: the slug of rule-ledger-write stands outside the bracket of its pointer · [[decision-case-809]]
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-30 updated: ## How it works left the Leaf, its mechanism in the docstring of .guppi/guppi/gate.py · [[decision-case-942.1]]
