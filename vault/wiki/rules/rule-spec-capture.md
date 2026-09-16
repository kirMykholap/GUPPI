---
type: rule
kind: Leaf
purpose: Prevents an approved Spec from existing only in Claude Code's plan file, outside the repository
status: built
enforcement: hook
implementation_ref: [guppi/spec.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-spec-capture-appends]]"]
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

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-20
- 2026-09-10 status: draft → built · cascade
- 2026-09-11 updated: spec.md has two writers: the hook at ExitPlanMode and the agent at Retro under ## Retro · [[decision-case-57]]
- 2026-09-11 status: built → draft · cascade
- 2026-09-12 updated: Work Mode is the third writer of spec.md, ticking boxes only (case 59.3) · [[decision-case-59.3]]
- 2026-09-12 updated: the Deferred heading, written at the close of Plan Mode and at Retro (case 59.5) · [[decision-case-59.5]]
- 2026-09-12 status: draft → built · cascade
- 2026-09-12 updated: the Spec lands in the session's folder raw/<hi date>/<hi HHMM>/ (case 73.2) · [[decision-case-73.2]]
- 2026-09-12 status: built → draft · cascade
- 2026-09-14 status: draft → built · cascade
