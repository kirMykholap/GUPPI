---
type: decision
case: "294"
status: current
update: ["[[rule-case-protocol]]", "[[estimate-case-protocol-loaded]]"]
origin: raw/2026-09-21/1315/ledger.md#case-294
sprint: migration
created: 2026-09-21
tags: [session, workflow, ledger]
---

## Context

`case-schema.md` describes one form of an `update` of an Estimate: "carries `slug`, `set: {status: pending}` and `change`… the scripts replace its Criterion". After 296 there is a second form — the item names a part, the Criterion and the status stand unless the Criterion is touched — and an agent reading the schema at `/hi` does not learn it: the same two texts that led to 290.3. Case 291 proposed to leave the schema alone so that `estimate-case-protocol-loaded` would not go `pending`; pre-spec showed the cost of the silence. The pages: `rule-case-protocol` `draft`; of its Estimates the Case touches `estimate-case-protocol-loaded` (its reading `passed` in this session's ledger; the page `pending` until the librarian applies it), not `estimate-ratification-ledger-line-form`; an `update` with a `ref`.

## Problem

The schema says every `update` of an Estimate carries `set: {status: pending}`; the mechanism of 296 tells two forms apart. Either the schema says both, or the agent learns the second from `rule-materialize` alone.

## History

- 2026-09-21 created · raw/2026-09-21/1315/ledger.md#case-294
