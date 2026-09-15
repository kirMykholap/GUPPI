---
type: estimate
kind: QA
status: pending
target: "[[rule-retro-commit]]"
origin: raw/2026-09-10/ledger.md#case-38.2
sprint: migration
created: 2026-09-10
tags: [session, workflow, hooks, harness, git]
---

## Context

Without the gate, session work and librarian work land in one undifferentiated diff.

## Criterion

Given a PreToolUse payload naming the Skill tool with skill handoff: with a dirty
tree, exit 2 with a reason naming commit first; with a clean tree, exit 0; another
skill or another tool, exit 0 whatever the tree. Live: the first /handoff called
from Retro on a dirty tree is refused, and passes after the commit.

### case 169.1

When:
The `UserPromptSubmit` hook calls `guppi gate` with a payload whose `prompt`, trimmed, is `/pre-task`, `/retro` or `/handoff`, with or without arguments.

Then:
The gate makes the same checks as for a call through `Skill`: the Spec against the ledger of the session; for `/handoff` the cleanness of the tree; letting it through, it writes the same mark `pretask`/`retro`/`handoff` into the event log.
**＋** A refusal is exit 2 with the reason on stderr, for the person: "gate: /retro refused — N item(s) of the Spec have no ledger line (case A). Ask the agent to end its reply with the LEDGER block, then type /retro again" or "commit first"; the client blocks the prompt.
**＋** Any other prompt, `/hi` included — exit 0, no output, no mark; a payload with `tool_name` — as today.
**－** `guppi event prompt` does not change and does not fail; the text of `rule-event-log` and `rule-ledger-write` names the second entry, their contracts the same.

## Method

pytest in tests/test_gate.py with piped payloads against a temp repository; the live reading once by hand

## Result

tests/test_gate.py 6 green; live: the agent called /handoff through the Skill tool on a dirty tree at the close of session E, the PreToolUse hook refused with `gate: /handoff refused — commit first. 162 path(s) uncommitted`, the skill did not run

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.2
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L78
- 2026-09-15 criterion: case 169.1 added · [[decision-case-169.1]]
