---
type: decision
case: "58"
status: current
update: ["[[rule-documentation]]", "[[estimate-documentation-completes]]"]
origin: raw/2026-09-12/ledger.md#case-58
sprint: migration
created: 2026-09-12
tags: [session, workflow, harness, librarian, render]
---

## Context

Slice 3 closes when `estimate-documentation-completes` passes. It failed three times,
each time on a read outside the librarian's frame. In session H the one read was the
Makefile: `make lint` stopped at its first step (`render --check` red), the brief needs
the lint output, and the agent opened the Makefile to learn the three steps and run them
apart.

## Problem

The frame's ban on reads names the wrong set. Its purpose is to keep the librarian out of
the wiki, where a page opened at will costs context and there are many. It also names
`guppi/` and `tests/`, and the criterion counts the Makefile as a read outside the frame.
The scripts' own files are not the problem the ban solves, and the reading fails on them.

## Given

`rule-documentation` (MOC, `draft`, Render is the librarian's frame) says: "Never read
`ledger.md`, `spec.md`, `plan.md`, `wiki/decisions/`, `vault/archived/`, or any file under
`guppi/` or `tests/`: what the scripts do with the yaml is written here."
**＋** `estimate-documentation-completes` (`pending` on the page, `failed` by the ledger
line of 2026-09-11 12:24:05, applied at the next materialize before this Case) says in its
Criterion "and no ledger, Spec, plan, Decision page, archive file, or file under guppi/ or
tests/".
**＋** The librarian's run of session H (event log 12:10–12:21) read the Makefile once and
no other file outside the frame; every other clause of the criterion passed, as the
`failed` line records.
**＋** `rule-brief` keeps `make lint`; its Render and `estimate-brief-written` are not
changed.
**－** The ban on the session artifacts and the vault stays: `ledger.md`, `spec.md`,
`plan.md`, `wiki/decisions/`, `vault/archived/`, and wiki pages beyond the four reasons.

## When

The librarian runs, and the reading of `estimate-documentation-completes` is taken against
its event log.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-58
