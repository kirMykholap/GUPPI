---
type: decision
case: "151"
status: current
update: ["[[rule-page-generation]]"]
origin: raw/2026-09-14/1633/ledger.md#case-151
sprint: migration
created: 2026-09-14
tags: [harness, workflow, ledger]
---

## Context

Entry 112.6 in `raw/2026-09-14/0747/materialize.yaml`: a `replace` whose text was not found on the page — `failed`; Case 130.1 made the same change and marked the entry `superseded_by: '130.1'`. `generate` skips only `applied`, so it retries 112.6 every run — three runs in a row, one stderr line and exit 1. `rule-raw-archive` (130.2) counts `superseded_by` as done — the unit is not held; it goes to the archive at the first run on a later date.

## Problem

A hole in the rule, not in the data: a superseded entry must not be applied — a later Case did its work. But the Decision page of the earlier Case is needed: the later one names it in `supersedes`, and the cascade sets it `superseded` → `archived`. Decide: `generate` skips the action of an entry with `superseded_by` and still writes the Decision page of its Case.

## Given

`rule-page-generation` `built`, `estimates: [estimate-generate-writes, estimate-generate-walks-dates]`; its text: "An entry that fails … is reported on stderr, marked `failed` and skipped; the rest apply; the exit code is 1"; "a stale `failed` mark is dropped on apply (case 53.3)". Code `apply`: `if entry.get("applied"): continue`; then `apply_decision` for the entry's Case; then the action.
**＋** `materialize` (130.2): `{supersedes:case N}` sets `superseded_by` on the entries of Case N in any unit's yaml and in its `decisions`. `generate.decision`: the later page carries `supersedes: [decision-case-N]`; the earlier gets `superseded_by` and `status: superseded`; the cascade — `archived`.
**＋** `rule-raw-archive`: a unit is done when every entry is `applied` or `superseded_by`; `archive.kept_reason` counts so.
**＋** Lint: the `supersedes` of a Decision page must name a live or archived page — the Decision of the earlier Case must exist.
**＋** Entry 112.6: `failed` × 3, `superseded_by: '130.1'`; the Decision page of 112.6 exists since session 0747 (the cascade of 130.1 archived it).
**－** An entry superseded before its first application (a Case ratified and superseded in one session) would be applied today — not after this Case; its Decision page is written.
**－** 142.1/142.2 (an entry without `kind` with `failed` from `materialize`) — another class, no overlap.

## Criterion

- [[estimate-generate-writes]] § case 151

## History

- 2026-09-14 created · raw/2026-09-14/1633/ledger.md#case-151
