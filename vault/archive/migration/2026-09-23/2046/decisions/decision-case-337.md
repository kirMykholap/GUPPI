---
type: decision
case: "337"
status: archived
update: ["[[rule-case-protocol]]"]
supersedes: ["[[decision-case-332.1]]"]
superseded_by: ["[[decision-case-341]]"]
origin: raw/2026-09-22/1724/ledger.md#case-337
sprint: migration
created: 2026-09-22
tags: [session, workflow, ledger]
---

## Context

Case 332.1 wrote the procedure of signing a pair into the description of `replace` in `case-schema.md` and carried it in words to `reword`. `/pre-spec` showed that `reword` is not described in that file at all: the keys of an `update` there are `set`, `sections`, `replace`, `change` and `rename`. The cause is older than a slip — the key was introduced by cases 274.1 and 274.3, written into `guppi/generate.py`, `guppi/materialize.py` and the page `rule-materialize`, and the schema of a Case was never brought along. So an agent writing a `then` block does not learn from its own file that `reword` exists.
`rule-case-protocol` stands `draft` and renders `case-schema.md`; case 324 of this session carries only a History line onto it, so nothing meets. The page's four Estimates are not named: `estimate-case-protocol-case-form` and `-ledger-line-form` already stand `pending` and are due in W2 to be read after the render.

## Problem

A key a Case may use is not described in the schema of a Case, and the procedure of signing a pair has nowhere to stand that covers both forms in one place.

## History

- 2026-09-23 created · raw/2026-09-22/1724/ledger.md#case-337
- 2026-09-23 superseded by decision-case-341 · [[decision-case-341]]
- 2026-09-23 archived · superseded
- 2026-09-23 archived · cleanup
