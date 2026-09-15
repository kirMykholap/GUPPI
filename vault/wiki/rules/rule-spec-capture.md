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

## How it works

`uv run guppi spec` on `PostToolUse` of `ExitPlanMode` appends the approved plan to `raw/<hi date>/<hi HHMM>/spec.md` — the session's folder, named by the time of its `hi` line (case 73) — a `---` separator when the file has content, the stamp
`<!-- approved HH:MM:SS · session xxxxxxxx -->`, the plan text, once. The file has
two more writers: in Work Mode the agent ticks the boxes of the `tasks` blocks, and
nothing else; at the close of Plan Mode and at Retro the agent appends the short-form Cases
under the `## Deferred` heading, before their ledger lines (`rule-retro`). `guppi materialize` reads both by
their `## Case N` headings, so a Retro defer gets its Decision page like any other.

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
