---
type: decision
case: "94"
status: current
defer: [rule-ask]
supersedes: [decision-case-80]
origin: raw/2026-09-12/ledger.md#case-94
sprint: migration
created: 2026-09-12
tags: [session, workflow, harness]
---

## Context

The search agent reads the four live indexes and never `vault/archived/`, which holds 22
pages. A `create` whose slug was archived comes back as free.

## Problem

A named slug has to be checked against the archive, and the answer has to say which of
the two it found.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-94
