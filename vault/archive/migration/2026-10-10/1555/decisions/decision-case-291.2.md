---
type: decision
case: "291.2"
status: archived
update: ["[[estimate-generate-ticks-the-spec]]", "[[estimate-internal-context-loaded]]"]
origin: raw/2026-09-21/1315/ledger.md#case-291.2
sprint: migration
created: 2026-09-21
tags: [harness, workflow, ledger, session]
---

## Context

`materialize` assembles one entry per ledger line. For an `update` of an Estimate, `lift_criterion` in `guppi/materialize.py` always puts `sections.Criterion` on the entry — the `given`, `when` and `then` of the Case — and sets `set.status: pending`, unless the item wrote a Criterion or a status itself. That is right for a change of the promise: the Case schema says such an `update` carries `set: {status: pending}` and `change`, and the Criterion is replaced whole (cases 204, 211). But an `update` that sets one field takes the same path: 290.3 set `purpose` on two Estimates, and the Criterion of 286 on `estimate-generate-ticks-the-spec` and of 288.1 on `estimate-internal-context-loaded` were replaced by the text of 290.3, whose own `then` said the Criterion does not change. Neither pre-spec nor the librarian caught it. The first case of the same root cause is `lesson-estimate-update-must-carry-its-criterion-whole` (session 0958); the second is the lesson of this session.
The pages: `rule-materialize` `draft` (`estimate-materialize-carries-addresses` pending), an `update` with a `ref`, no vault query; of the ten Estimates of the rule the Case touches one, `estimate-materialize-assembles` (`passed`; its line "`set: {status: pending}` unless the item set a status itself" is the promise), the other nine not. `rule-case-protocol` is not touched: the schema already says only a replaced Criterion sets `pending`, and the `update` form of a promise change already carries `set: {status: pending}` — that is the signal.

## Problem

The script knows one kind of `update` of an Estimate — the change of the promise — and replaces the signed Criterion on every `update`. The two Criteria signed in 286 and 288.1 do not stand on their pages; the reading of `estimate-internal-context-loaded` has nowhere to land.

## History

- 2026-09-21 created · raw/2026-09-21/1315/ledger.md#case-291.2
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
