---
type: decision
case: "226.1"
status: archived
create: ["[[estimate-generate-ticks-the-spec]]"]
update: ["[[rule-page-generation]]"]
supersedes: ["[[decision-case-217]]"]
origin: raw/2026-09-17/1119/ledger.md#case-226.1
sprint: migration
created: 2026-09-17
tags: [harness, workflow, ledger]
---

## Context

`rule-page-generation` applies the entries of `materialize.yaml` to pages and knows nothing of the Spec; `rule-render-harness` writes the harness files from the Rule pages and knows nothing of the Spec either. The task lines of a Spec — `- [ ] create `slug``, `update `slug``, `guppi render` — stay open at the end of every session: the librarian is forbidden to read the Spec (`estimate-documentation-completes`), and the agent in Work Mode does none of these actions — the librarian does. Case 216 ticked 21 lines of the 1955 Spec by hand; case 217 deferred the mechanism to this Plan Mode; the 2238 Spec holds 36 unticked lines, 29 of them pages and renders. The yaml lies in the session's folder beside `spec.md`, each entry carries `case`, `kind` and `slug`; `generate` marks an entry `applied` once applied; `render` without a flag writes every governed file and exits 0, `--sync` is the `SessionStart` hook, `--check` writes nothing. The Case creates one new promise per rule and touches none of the five Estimates of `rule-page-generation` nor the two of `rule-render-harness`; the slugs `estimate-generate-ticks-the-spec` and `estimate-render-harness-ticks-the-spec` are free, in `wiki/` and in the archive. The question of 3b — who ticks what — this Case does not settle: the lines on code, tests, migrations and readings stay the agent's, as 217 said.

## Problem

The lines whose work a script does are ticked by nobody: Retro counts them as debt, and every session ends either in a tick by hand after the fact or in false debt.

## History

- 2026-09-18 created · raw/2026-09-17/1119/ledger.md#case-226.1
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
