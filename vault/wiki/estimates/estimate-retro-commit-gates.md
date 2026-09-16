---
type: estimate
kind: QA
status: passed
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

### case 180

When:
`guppi gate` receives `/retro` — typed by the person, a `UserPromptSubmit` payload whose `prompt`, trimmed, is `/retro` with or without arguments, or called by the agent through `Skill` with `skill: retro` on `PreToolUse`.

Then:
When the session has a `hi` but its folder holds no `spec.md`, the event log names no plan file, and the session's ledger window holds no `- decision[`, `- estimate[` or `- lesson[` line, the gate refuses: exit 2, the reason on stderr: `gate: /retro refused — nothing to review: no Spec and no ledger line in raw/<date>/<HHMM>/. Ratify a Case or write a reading or a lesson first, then type /retro again.`; on the `Skill` path the same advice for the agent: `…then call /retro in the next reply.`; the client blocks the prompt, no mark is written.
**＋** With at least one of the three ledger lines, or a Spec, or a plan file — the check of 122 and the mark as today.
**＋** Without `hi` — as today: nothing to check, exit 0.
**－** `/pre-task` and `/handoff` are unchanged; `/handoff` in an empty session still checks the tree only.

## Method

pytest in tests/test_gate.py with piped payloads against a temp repository; the live reading once by hand

## Result

block 180: tests/test_gate.py 30 tests green at commit 572df74 (385 total, read 2026-09-16 01:32 on the line of block 184), and both guppi/gate.py and tests/test_gate.py byte-identical at HEAD e970693 with a clean worktree — nothing changed since that run; live, session 1034 of 2026-09-16, after the hi of 10:34:45 — a typed /retro as the first command of the session, with no spec.md in the folder, no plan file named by the event log and no record line in the window, was blocked at UserPromptSubmit with "gate: /retro refused — nothing to review: no Spec and no ledger line in raw/2026-09-16/1034/. Ratify a Case or write a reading or a lesson first, then type /retro again." — the person's advice tail and the session's own folder in the path; no retro mark in raw/2026-09-16/event_log.md, as a refused call leaves none

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.2
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L78
- 2026-09-15 criterion: case 169.1 added · [[decision-case-169.1]]
- 2026-09-16 status: pending → passed · raw/2026-09-15/2225/ledger.md#L1
- 2026-09-16 criterion: case 180 added · [[decision-case-180]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1034/ledger.md#L1
