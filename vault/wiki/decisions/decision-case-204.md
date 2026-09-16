---
type: decision
case: "204"
status: current
update: ["[[rule-materialize]]", "[[estimate-materialize-assembles]]"]
origin: raw/2026-09-16/1955/ledger.md#case-204
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger]
---

## Context

`rule-materialize` is a Leaf, `enforcement: check`, its code `guppi/materialize.py`; nine Estimates, among them `estimate-materialize-assembles` — `pending` with the Criterion of 194.1, its reading not yet taken. The Purpose of the rule says: the Criterion of an Estimate is the `given`, `when`, `then` of the Case, lifted verbatim into the entry's `sections`. The Criterion of `-assembles` says the same for an `update` and allows a written text for a `create` only: "from the block's `sections` when one is written, else from the Case". The code (`lift_criterion`) keeps a written `sections.Criterion` in both cases — on a `create` and on an `update` — and sets `pending` unless the item set a status itself. The handoff of 1651 named the divergence: 188 updated `estimate-case-protocol-loaded` with a written Criterion and the text stayed, although the `then` of 194.1 says the entry carries the Case's text. `case-schema.md` already allows both paths for a `create` (194.1), and Case 203.1 of this session leans on a written Criterion as the signature of a separate promise. The Case touches one Estimate — `-assembles`; the other eight it does not touch.

## Problem

Two texts speak of an Estimate `update` differently: the rule and the Criterion say "the Case's text replaces", the code says "the written text stands". Until this is signed, `estimate-case-protocol-loaded` carries a Criterion that by the letter of the rule should not have stayed, and 203.1 treats an item with a written Criterion as a separately signed promise without a rule that says so. The question: which of the two texts is the signature when the item wrote `sections: Criterion` itself.

## History

- 2026-09-16 created · raw/2026-09-16/1955/ledger.md#case-204
