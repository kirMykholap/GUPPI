---
type: decision
case: "250.2"
status: current
create: ["[[estimate-sprint-ticks-the-spec]]"]
update: ["[[rule-sprint]]"]
origin: raw/2026-09-18/2054/ledger.md#case-250.2
sprint: migration
created: 2026-09-18
tags: [harness, sprint, session, workflow, librarian]
---

## Context

`rule-sprint` is the rule by which `guppi sprint` writes `vault/wiki/sprint.md` from the sprint page; the librarian runs it after `cleanup` and `render`. `rule-render-harness` since case 226.2 ticks the Spec lines that open with a code span holding `guppi render`, in every unit under `raw/` whose yaml is applied whole; `generate` ticks the page lines (226.1). The lines `- [ ] `uv run guppi sprint` at the librarian's run` — three in the Spec of session 1957 — are ticked by nobody: `guppi sprint` knows nothing of the Spec. A second finding: `render` counts a yaml applied whole when every entry carries `applied`; the entry of case 247 in the 1957 yaml carries `superseded_by` and no `applied`, so `render` would never touch that unit, while `guppi archive` (`rule-raw-archive`) counts such an entry closed. The Case touches `estimate-render-harness-ticks-the-spec` and no other Estimate of `rule-render-harness`; on `rule-sprint` it touches neither `estimate-sprint-renders-the-backlog` nor `estimate-sprint-checks-the-file` and creates a third; the slug `estimate-sprint-ticks-the-spec` is free in `wiki/` and in the archive.

## Problem

A `guppi sprint` line of the Spec is work a script does, not the agent, and nobody ticks it: Retro counts it as debt in every session that changed the sprint page. Even with a ticking `sprint`, the unit of 1957 would stay untouched: a yaml with a superseded entry does not count as applied whole.

## History

- 2026-09-18 created · raw/2026-09-18/2054/ledger.md#case-250.2
