---
type: estimate
kind: QA
status: pending
target: "[[rule-case-protocol]]"
origin: raw/2026-09-16/1034/ledger.md#case-188
sprint: migration
created: 2026-09-16
tags: [session, workflow, ledger]
ref: rule-case-protocol
purpose: The reply that acknowledges a ratification has four parts in order
method: one reading by hand of the first acknowledging reply of a session
---

## Criterion

When:
The owner answers a Case with a ratification; the agent writes the reply that
acknowledges it.

Then:
The reply has four parts, in this order: the `LEDGER` block first; the heading
`## Case N — ratified` and a paragraph **Changes:** — what changes, in one or two
sentences; a paragraph **Notes:** — facts that did not enter the Case, omitted when
there are none; the heading `## Frontier` and the lines of `frontier.md` as a
checklist — the closed lines folded into one, the open ones one per line with a short
title, the deferred as `[-] … · defer case N` — and the question which item is next,
last.
**＋** The headings and labels are in the language of the chat.
**－** The replies on readings and lessons, the reply that carries a Case and the
short form of a defer stay as today; no tool call follows the block in the same reply.

## History

- 2026-09-16 created · [[decision-case-188]]
