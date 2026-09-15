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

block 169.1: tests/test_gate.py green (379 total); live 2026-09-15 22:34, session 2225: `/retro` typed before any plan, Spec absent, ledger empty — the gate let it through, the skill loaded with tests and style, and `raw/2026-09-15/event_log.md` carries the mark `22:34:01 8836b091 retro` with no `tool Skill: retro` line after it, the typed path; the refusal text on a Spec item without its line was not seen live — nothing to refuse — and stands on the test `unwritten_item_is_refused_for_the_person`

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.2
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L78
- 2026-09-15 criterion: case 169.1 added · [[decision-case-169.1]]
- 2026-09-16 status: pending → passed · raw/2026-09-15/2225/ledger.md#L1
- 2026-09-16 criterion: case 180 added · [[decision-case-180]]
