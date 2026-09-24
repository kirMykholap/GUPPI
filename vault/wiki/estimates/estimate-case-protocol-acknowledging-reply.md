---
type: estimate
kind: QA
status: passed
target: "[[rule-case-protocol]]"
purpose: The reply that acknowledges a ratification has four parts in order
method: one reading by hand of the first acknowledging reply of a session
checked: 2026-09-24
origin: raw/2026-09-16/1034/ledger.md#case-188
sprint: migration
created: 2026-09-16
tags: [session, workflow, ledger]
---

## Criterion

When:
The person ratifies a Case, or ratifies again a Case shown again after its ratification, and the agent writes the reply that acknowledges it.

Then:
The reply has four parts, in this order: the `LEDGER` block first; the heading `## Case N — ratified` and a paragraph `Changes:` — what changes, in one or two sentences; a paragraph `Notes:` — facts that did not enter the Case, omitted when there are none; the heading `## Frontier` and the lines of `frontier.md` as a checklist — the closed lines folded into one, the open ones one per line with a short title, the deferred as `[-] … · defer case N` — and the question which item is next, last.
**＋** For a Case with sub-cases, one reply acknowledges every sub-case ratified: one `LEDGER` block with all their lines, one heading `## Case N — ratified` naming the ids, one Frontier.
**＋** The reply that acknowledges a re-ratification carries the `LEDGER` block with the decision lines of each Case ratified again, as at its first ratification.
**＋** The headings and labels are in the language of the chat.
**＋** No tool call follows the `LEDGER` block in the same reply.
**－** The ledger hook of `rule-ledger-write` does not append a repeated decision line a second time.

## Result

2026-09-24, by hand in session 1303, against the Criterion of Case 390: the reply that acknowledged the re-ratification of Case 392.1 opened with the LEDGER block holding the three decision lines of 392.1 again, then the heading "Case 392.1 — ратифицирован повторно", Changes, Notes, the Frontier with the closed lines folded, and the question last, headings in the chat's language, no tool call after the block; the ledger after it holds 15 lines, the six of case 392 once each, and the hook of rule-spec-write wrote 392.1 into the plan file and its ratified copy

## History

- 2026-09-16 created · [[decision-case-188]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L36
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
- 2026-09-23 updated: the Criterion names the one acknowledging reply of a Case with sub-cases (case 355.2) · [[decision-case-355.2]]
- 2026-09-23 updated: the other replies are not measured here, their form stands in the schema (case 368) · [[decision-case-368]]
- 2026-09-24 updated: the Criterion replaced whole — the LEDGER block of a re-ratification (case 390) · [[decision-case-390]]
- 2026-09-24 status: pending → passed · raw/2026-09-24/1303/ledger.md#L16
