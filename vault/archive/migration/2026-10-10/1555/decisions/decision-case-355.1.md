---
type: decision
case: "355.1"
status: archived
update: ["[[rule-case-protocol]]", "[[estimate-case-protocol-loaded]]", "[[estimate-case-protocol-case-form]]"]
origin: raw/2026-09-23/0034/ledger.md#case-355.1
sprint: migration
created: 2026-09-23
tags: [session, workflow, ledger]
---

## Context

`case-schema.md` describes `ratification` as the human's sign-off, question or own alternative, ending with a preview of the ledger lines. It does not forbid the agent's text there, and in Case 354 the agent wrote the effect of a first run and its own notes into `ratification`. The place for the agent's text already stands: one horizontal rule after the Case, by the section Language. The schema describes a sub-case as `### Case N.M` under its parent with its own `ratification`, and a parent's sign-off does not cover its children; it does not say whether sub-cases are shown in one reply or one by one. In Case 354 they were shown one by one: four acknowledgements, four Frontiers, and the parent's `context` out of view.
`rule-case-protocol` stands `draft`; the live reading of its Render is `estimate-case-protocol-loaded`, `pending`; the form of a Case in the chat is read by `estimate-case-protocol-case-form`, `pending`; each gets a line in its Criterion, and the other Estimates of the rule are not touched.

## Problem

The schema does not separate the section of the person from the agent's text, and does not say how a Case with sub-cases is shown; the agent picks the form itself.

## History

- 2026-09-23 created · raw/2026-09-23/0034/ledger.md#case-355.1
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
