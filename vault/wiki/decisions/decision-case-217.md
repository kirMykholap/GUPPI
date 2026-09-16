---
type: decision
case: "217"
status: current
defer: ["[[rule-page-generation]]"]
origin: raw/2026-09-16/2238/ledger.md#case-217
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger]
---

## Context

`rule-page-generation` applies the entries of a yaml to pages and knows nothing of the Spec; `rule-work-mode` (`draft`, Slice 3b) ticks the task lines of `spec.md` as the work goes; the librarian is forbidden to read the Spec (`estimate-documentation-completes`). The yaml lies in the session's folder beside `spec.md`; each entry carries `case`, `kind` and `slug`.

## Problem

Nobody ticks the task lines on a `create` or `update` of a page or on `guppi render`: every Spec ends its session with them open, and Retro counts them as debt — 21 in the Spec of 1955.

## Deferred

### [[rule-page-generation]]

generate ticks, in the session's spec.md, the task line under the entry's Case whose kind and slug it names — `- [ ] create <slug>` / `update <slug>` / `defer <slug>` — once the entry applied, and the librarian's render step ticks its `guppi render` line the same way; a line not found is no error; the lines on code, tests, migrations and readings stay the agent's; the script reads the Spec, not the librarian — said in the Criterion; a one-off tick of the older Specs is case 216, not this; with Slice 3b, which fixes who ticks what

## History

- 2026-09-17 created · raw/2026-09-16/2238/ledger.md#case-217
