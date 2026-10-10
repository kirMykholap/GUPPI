---
type: decision
case: "194.2"
status: archived
update: ["[[estimate-materialize-walks-dates]]"]
origin: raw/2026-09-16/1651/ledger.md#case-194.2
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger]
---

## Context

`rule-materialize` is a Leaf, `enforcement: check`, its code `guppi/materialize.py`; two Estimates: `estimate-materialize-assembles` (a head Criterion and nine blocks) and `estimate-materialize-walks-dates` (a head and two blocks). Case 189 ratified: the script derives no Estimate from `contract`, `method` or `supersedes`; an Estimate has its own line and its own entry, its Criterion taken from the Case; `## How it works` goes into the docstring; six blocks became their own pages, 73.5 goes to `-walks-dates`, 90.1 dies. Case 190.3 added the skip of a unit holding `carry.md`. But neither 189 nor 190.3 gave the page one line of text, both Estimates carry `set: {status: pending}` with no new Criterion, and `generate` can neither drop a section nor apply a `criterion` key on an `update`: it applies `set`, `sections`, `replace`. The blocks of Case 186 carry `contract: changed` and `estimate_slug`, which 189 does not read. This Case touches both Estimates of the page and not the six new ones: their Criterion is written in the blocks of 189.

## Problem

How 189 and 190.3 reach the page and the code without three holes: the text of `## Purpose` after `## How it works` leaves; the shape of the entry in which the lifted Criterion reaches the page through the existing `generate`; and the Criterion of both Estimates replaced whole without losing the promise of the head. And what to do with the keys of the old shape in the blocks of 186.

## Given

A unit `raw/<date>/<HHMM>/` holds `ledger.md` and `spec.md`; a Case in the Spec has a heading, the sections `given`, `when`, `then` and a `then` block.
**＋** `guppi generate` applies the `sections` of an `update` entry as whole replacements and writes every field of a `create` entry's `fields` into the frontmatter.
**＋** Cases 189 and 190.3 are ratified; their entries for these same pages apply before the entries of this Case, in ledger order.
**－** The tests in `tests/test_materialize.py` fix the behaviour; the live reading is the librarian's run of this session.

## History

- 2026-09-16 created · raw/2026-09-16/1651/ledger.md#case-194.2
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
