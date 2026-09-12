---
type: decision
case: "67"
status: superseded
defer: [rule-case-protocol]
superseded_by: [decision-case-75.1]
origin: raw/2026-09-12/ledger.md#case-67
sprint: migration
created: 2026-09-12
tags: [session, workflow, ledger]
---

## Context

Every decision line of session I up to 10:09 was written `decision[58][update][slug]`;
`materialize.parse_line` reads `decision[case 58][update][slug]` only. The agent took the
placeholder `decision[case_id][kind][slug]` of the table "What a Case produces" in
`case-schema.md` literally, and the Render of `rule-case-protocol` shows the line only as
`- decision[...]`. The lines were written again in the right form; the 33 wrong ones stay
(`lesson-ledger-decision-line-written-without-the-case-word`).

## Problem

Nothing the agent reads at session start shows a decision line as the ledger holds it.
The table of `case-schema.md` and the ledger paragraph of `rule-case-protocol` should show
`- decision[case N][kind][slug]{ref:…}{tags:…}` with a real number, as every earlier
ledger writes it. An `update` of both; the next Plan Mode.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-67
- 2026-09-12 superseded by decision-case-75.1 · [[decision-case-75.1]]
