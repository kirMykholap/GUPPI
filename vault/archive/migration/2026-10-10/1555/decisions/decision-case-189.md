---
type: decision
case: "189"
status: archived
create: ["[[estimate-materialize-shows]]", "[[estimate-materialize-lifts-a-lesson]]", "[[estimate-materialize-marks-exists]]", "[[estimate-materialize-fails-alone]]", "[[estimate-materialize-finds-a-rule-class-item]]", "[[estimate-materialize-marks-superseded]]"]
update: ["[[rule-materialize]]", "[[estimate-materialize-assembles]]", "[[estimate-materialize-walks-dates]]"]
origin: raw/2026-09-16/1034/ledger.md#case-189
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger, tests, librarian]
---

## Context

`rule-materialize` is a Leaf, `enforcement: check`, its code `guppi/materialize.py`. Today
the script guesses which Estimate a Case touched: from a Leaf `create` it reads `method`
and builds the Estimate page with a derived slug; from an `update` it reads
`contract: changed` and appends a `### case N` block; from `{supersedes:case N}` it derives
a block removal. The page carries two Estimates, `-assembles` with a head Criterion and
nine blocks, and `-walks-dates`. Case 182 deferred it with the whole model; this Case takes
points 7, 9 and 14. The vault was asked: six slugs are free, and a seventh is not needed —
block 73.5 is already covered by `-walks-dates`.

## Problem

The script derives the contract from flags, and every derivation is a place where the
signed text and the written text come apart. `contract: changed` does not say which of a
page's promises is touched, so with two Estimates the script either guesses or writes
`incomplete: [estimate]`. A derived Estimate slug can collide with a live page, so a fourth
key, `estimate_slug`, exists to correct the third. `remove_criterion` is derived from
`supersedes` and in three cases out of three last session found no block to remove. All
three derivations exist only because a Criterion is stitched from blocks instead of being
replaced whole.

## Given

`materialize.py:583` derives the Estimate update from `contract: changed`; `DERIVED_KEYS`
holds `method`, `contract`, `estimate_slug`, `estimate_kind`.
**＋** the Criterion of `-assembles` is the head text plus nine blocks: 73.5, 76, 87, 90.1,
105.2, 142.1, 158, 161, 175.
**＋** block 73.5 is covered by `-walks-dates`: its block 103.2 fixes the Spec of a session
unit and block 142.4 carries the "a Case heading in two files stops the walk" line word for
word; only the yaml's `spec` field is uncovered.
**＋** block 90.1 is wholly about the derivation from `contract: changed`; it dies with the
derivation and is carried nowhere.
**＋** blocks 142.1 and 158 promise one thing — one bad entry does not stop the run; 158
only makes the wording of 142.1 precise.
**＋** the `＋` line of 105.2 on the `generate` collision on stderr is the promise of
`rule-page-generation`.
**＋** the clause of 142.1 on the field list in `## How it works` is not carried as it
stands: point 3 drops the section from a Leaf, and the field list moves to the docstring of
`guppi/materialize.py`.
**＋** the six slugs are free in the vault and in the archive; `harness`, `workflow` and
`ledger` fit all six, `librarian` two, `tests` two.
**－** `{supersedes:case N}` stays: point 14 keeps it for Decision pages and yaml entries.
**－** lessons and Insights do not change.

## History

- 2026-09-16 created · raw/2026-09-16/1034/ledger.md#case-189
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
