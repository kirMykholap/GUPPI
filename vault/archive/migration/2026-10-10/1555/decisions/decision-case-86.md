---
type: decision
case: "86"
status: archived
update: ["[[rule-case-protocol]]", case-schema]
supersedes: ["[[decision-case-81]]"]
origin: raw/2026-09-12/ledger.md#case-86
sprint: migration
created: 2026-09-12
tags: [session, workflow, ledger]
---

## Context

Case 72.1 ratified that a Leaf `create` carries `method`, the Estimate's `kind` (`QA` by
default) and its `slug` (only on a collision). In Work Mode the agent saw that `kind` and
`slug` on the item are already the target page's own fields, chose `estimate_kind` and
`estimate_slug`, and did not return the fork. The code, the tests and `case-schema.md`
write the prefixed names; the ratified text of 72.1 does not. Case 81 deferred it here.

## Problem

Either the two names are ratified as they stand, or the form goes back to one where
`kind` and `slug` are unambiguous. No field the harness reads may carry a name nobody
signed.

## Given

`guppi/materialize.py` holds `DERIVED_KEYS = ("method", "contract", "estimate_slug",
"estimate_kind")`; line 497 takes `item.get("estimate_slug") or derived_slug(...)` and
line 505 `item.get("estimate_kind") or "QA"`. `guppi/pretask.py` prints "estimate <slug>
exists; name estimate_slug". Both names are pinned in `tests/test_materialize.py` and
`tests/test_pretask.py`.
**＋** `case-schema.md` writes both names, in the example block and in the prose, and
nowhere says why the prefix.
**＋** Against what `decision-case-81` records: `index.md` §7 and `glossary.md` name no
item key at all; they describe the derivation without one. The disagreement is between
the ratified text of 72.1 and `case-schema.md` with the code, and nowhere else.
**＋** `rule-case-protocol` is a Leaf, `draft`, `deferred_by: [decision-case-81]`; its
Estimate `estimate-case-protocol-loaded` is `pending` and its Criterion already holds the
clause of 72.1 — a Leaf `create` carries `method` and no nested `estimate`.
**－** `_lift_item` puts every key of a create item that it does not skip into the page's
frontmatter, and `DERIVED_KEYS` keeps these four off the target: without the prefix the
Estimate's `kind` would overwrite the target page's own.

## Criterion

- [[estimate-case-protocol-loaded]] § case 86

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-86
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
