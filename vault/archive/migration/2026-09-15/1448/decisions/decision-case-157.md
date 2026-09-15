---
type: decision
case: "157"
status: archived
update: ["[[rule-case-protocol]]"]
superseded_by: ["[[decision-case-167]]"]
origin: raw/2026-09-15/1110/ledger.md#case-157
sprint: migration
created: 2026-09-15
tags: [session, workflow, ledger]
---

## Context

`rule-case-protocol` (Render → `CLAUDE.md`) says where the `decision[...]` lines are written — "in the reply that acknowledges ratification" — and that this reply ends in the `LEDGER` block. What the rest of that reply looks like the rule does not say; today it went as one block of running text. The owner chose a shape from the variants shown: a heading, "Changes", "Notes", the frontier as a checklist, the block.

## Problem

The shape of the acknowledging reply is ratified nowhere; the agent is not bound to keep it, and keeping it in the agent's memory is a decision without a Case.

## Given

`rule-case-protocol` (`draft`, `render`, `estimates: [estimate-case-protocol-loaded]` — `passed` today on 144.1): the Render, lines 60–65, the paragraph on the Spec ends "Retro counts the unticked."; lines 79–81: "Write the `- decision[...]` lines only in the reply that acknowledges ratification … A reply that carries a `LEDGER` block ends in that text."
**＋** `rule-skill-hi`: `frontier.md` is `- [ ] F<n> — <title> · <source>`, closed as `[x] … · case N`, `[x] … · work`, `[-] … · defer case N`; the checklist in the reply repeats that form.
**＋** Language: the chat with the owner is in Russian (`rule-claude-md`, Language) — the headings and labels of the reply are in the language of the chat, the rule describes them in English.
**＋** An `update` with a `ref`: the page was read, `ask-guppi` not dispatched (155).
**－** `case-schema.md` does not change: the acknowledging reply is not a section of a Case.

## Criterion

- [[estimate-case-protocol-loaded]] § case 157

## History

- 2026-09-15 created · raw/2026-09-15/1110/ledger.md#case-157
- 2026-09-15 superseded by decision-case-167 · [[decision-case-167]]
- 2026-09-15 archived · superseded
- 2026-09-15 archived · cleanup
