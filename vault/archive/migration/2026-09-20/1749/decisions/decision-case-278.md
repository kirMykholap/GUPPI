---
type: decision
case: "278"
status: archived
update: ["[[estimate-case-protocol-loaded]]"]
superseded_by: ["[[decision-case-279.1]]"]
origin: raw/2026-09-20/1749/ledger.md#case-278
sprint: migration
created: 2026-09-20
tags: [session, workflow, ledger]
---

## Context

`estimate-case-protocol-loaded` is an Estimate of `rule-case-protocol`: the Case schema is present in a session from the first turn. While the schema lived inside `CLAUDE.md`, the only way to check that was the agent's behaviour: in the reply to `/hi` the agent named the `LEDGER`-block rule and the one-Case-at-a-time rule by itself. Since case 273 the schema is the Render of `rule-case-protocol` in `case-schema.md`, and `/hi` brings its text into the context; the presence of the text is checked by `estimate-internal-context-loaded` (`passed` today). The Criterion line on the statement stayed, no instruction asks for that act, and today's reading gave `failed` on that line alone.
The page stands `pending` since 273.1, `failed` today; in the old shape — `method` and `checked`, no `purpose`; lint counts it among the unmigrated. One Estimate of `rule-case-protocol` is touched; the other three (`case-form`, `acknowledging-reply`, `ledger-line-form`) are not.

## Problem

The Criterion asks for a behaviour no instruction sets, and checks a second time what `estimate-internal-context-loaded` already checks. Either the instruction catches up with the Criterion, or the Criterion loses the line.

## History

- 2026-09-20 created · raw/2026-09-20/1749/ledger.md#case-278
- 2026-09-20 superseded by decision-case-279.1 · [[decision-case-279.1]]
- 2026-09-20 archived · superseded
- 2026-09-20 archived · cleanup
