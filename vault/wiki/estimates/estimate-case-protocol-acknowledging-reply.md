---
type: estimate
kind: QA
status: pending
target: "[[rule-case-protocol]]"
purpose: The reply that acknowledges a ratification has four parts in order
method: one reading by hand of the first acknowledging reply of a session
checked: 2026-09-16
origin: raw/2026-09-16/1034/ledger.md#case-188
sprint: migration
created: 2026-09-16
tags: [session, workflow, ledger]
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
**＋** For a Case with sub-cases, one reply acknowledges every sub-case ratified: one `LEDGER` block with all their lines, one heading `## Case N — ratified` naming the ids, one Frontier (355.2).
**＋** The headings and labels are in the language of the chat.
**－** The replies on readings and lessons, the reply that carries a Case and the
short form of a defer are not measured here — their form stands in `case-schema.md` (368); no tool call follows the block in the same reply.

## Result

2026-09-16, the acknowledging replies of Cases 201, 202, 203, 204, 208 read by hand: the LEDGER block first, `## Case N — ратифицирован`, Изменения, Заметки when present, `## Frontier` as a checklist with the closed lines folded and the deferred as `[-] … · defer case N`, the question last; headings in Russian; no tool call after the block

## History

- 2026-09-16 created · [[decision-case-188]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L36
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
- 2026-09-23 updated: the Criterion names the one acknowledging reply of a Case with sub-cases (case 355.2) · [[decision-case-355.2]]
- 2026-09-23 updated: the other replies are not measured here, their form stands in the schema (case 368) · [[decision-case-368]]
