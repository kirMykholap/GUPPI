---
type: estimate
kind: QA
status: pending
target: "[[rule-sprint-close]]"
purpose: At the close of a sprint each pending or failed Estimate is put to the person, who has it read, carries it into the next sprint or archives it unread, before any page moves
method: by hand, the record of the first close of a sprint, vault/wiki/estimates/ and vault/archive/ read after it
origin: raw/2026-10-03/0317/ledger.md#case-612.4
sprint: migration
created: 2026-10-03
tags: [sprint, workflow]
---

## Criterion

When:
The close of the sprint `entity-sprint-<id>` runs: the Estimates that `entity-sprint-<id>` lists are read in it first, and its pages move once each of them stands `passed`; someone reads the record of the close, `vault/wiki/estimates/` and `vault/archive/` after it.

Then:
Before any page of the close moves, the close lists to the person each Estimate under `vault/wiki/estimates/` that stands `pending` or `failed`.
**＋** For each listed Estimate the person chooses one way: read it now, carry it into the next sprint, or archive it unread.
**＋** An Estimate read now has its reading in the ledger.
**＋** An Estimate carried into the next sprint stays under `vault/wiki/estimates/` with its status.
**＋** An Estimate archived unread stands under `vault/archive/`, and the page that listed it no longer lists it in `estimates`.
**－** No page of the close moves before the person has chosen for each listed Estimate.

## History

- 2026-10-03 created · [[decision-case-612.4]]
