---
type: decision
case: "368"
status: current
update: ["[[rule-case-protocol]]", "[[estimate-case-protocol-case-form]]", "[[estimate-case-protocol-loaded]]", "[[estimate-case-protocol-acknowledging-reply]]"]
origin: raw/2026-09-23/1126/ledger.md#case-368
sprint: migration
created: 2026-09-23
tags: [session, workflow, ledger]
---

## Context

The Case schema (`case-schema.md`, the Render of `rule-case-protocol`) names the eight sections of a Case and their order, but not where a Case begins or under which heading. It names a heading in the chat only for a sub-case (`### Case N.M — name`), for the short form of a defer (`## Case N — name`) and for the acknowledging reply (`## Case N — ratified`). In the Spec the heading `## Case N — name` stands, because the earlier Specs were written so and the scripts find a Case by its heading. In the chat of this session the Cases 363–367 opened straight with `context`, while the sub-cases 364.1–364.3 opened with their heading; the lesson is `lesson-case-protocol-chat-case-without-heading`.
`rule-case-protocol` stands `draft`; the Case touches `estimate-case-protocol-case-form` (`pending`), whose Then describes the form of a Case in the chat, `estimate-case-protocol-loaded`, the live reading of the Render (case 187), and `estimate-case-protocol-acknowledging-reply`, whose "the reply that carries a Case … stay as today" the heading changes; it does not touch `estimate-case-protocol-ledger-line-form`; no `create`.

## Problem

A full Case in the chat has no named heading; the agent follows the text literally and shows the Case without one, while a sub-case of the same reply has it.

## History

- 2026-09-23 created · raw/2026-09-23/1126/ledger.md#case-368
