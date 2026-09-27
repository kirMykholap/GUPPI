---
type: decision
case: "456"
status: current
defer: ["[[rule-page-generation]]"]
origin: raw/2026-09-27/1255/ledger.md#case-456
sprint: migration
created: 2026-09-27
tags: [harness, workflow, ledger]
---

## Context

Case 445.4 deleted `estimate-prespec-checks-the-ratified-copy`. Its `read` box in `archive/migration/2026-09-26/1745/raw/spec.md` line 413 stays unticked, because no reading of a deleted page will stand in the ledger, and Retro counts it as debt.

## Problem

Whether `generate` ticks or drops the `read` line of an Estimate a `delete` removes, or the box is left as it stands. The person defers it to a later session.

## Deferred

### [[rule-page-generation]]

A read box of an Estimate that a delete removed stays unticked in its Spec, since no reading of it will stand in the ledger

## History

- 2026-09-27 created · raw/2026-09-27/1255/ledger.md#case-456
