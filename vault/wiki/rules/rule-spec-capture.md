---
type: rule
kind: Leaf
purpose: Prevents an approved Spec from existing only in Claude Code's plan file, outside the repository
status: built
enforcement: hook
implementation_ref: [guppi/spec.py, .claude/settings.json]
parent: rule-plan-mode
estimates: [estimate-spec-capture-appends]
origin: raw/2026-09-09/ledger.md#case-20
sprint: migration
created: 2026-09-09
tags: [session, hooks, harness, workflow]
---

## Purpose

Prevents an approved Spec from existing only in Claude Code's plan file, outside the
repository. The ledger's decision lines are routing only; their content is the Spec, and
page `origin` fields point at both. A Spec copied by hand is copied late, partially, or
not at all.

## Estimates

- [[estimate-spec-capture-appends]]

## Parent

- [[rule-plan-mode]]

## Implementation

- `guppi/spec.py`
- `.claude/settings.json`

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-20
- 2026-09-10 status: draft → built · cascade
