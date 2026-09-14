---
type: decision
case: "118"
status: archived
defer: ["[[rule-retro]]"]
superseded_by: ["[[decision-case-126]]"]
origin: raw/2026-09-14/0747/ledger.md#case-118
sprint: migration
created: 2026-09-14
tags: [session, workflow, harness, render]
---

## Context

The Render of `rule-retro` (109.1) reads the ledgers of the day with `cat vault/raw/$(date +%F)/ledger.md vault/raw/$(date +%F)/*/ledger.md 2>/dev/null`. On 2026-09-14 no date-level ledger exists — the first day with the session form of case 103 alone — so `cat` exits 1, the harness reports the substitution failed, and the skill text does not reach the agent; the `retro` event was still recorded.

## Problem

A substitution that names a file which the model of case 103 no longer guarantees fails on every session from now on. The fix is one `|| true` or a glob-only form; it is an `update` of `rule-retro`, which Retro cannot ratify.

## History

- 2026-09-14 created · raw/2026-09-14/0747/ledger.md#case-118
- 2026-09-14 superseded by decision-case-126 · [[decision-case-126]]
- 2026-09-14 archived · superseded
- 2026-09-14 archived · cleanup
