---
type: decision
case: "220"
status: current
defer: ["[[rule-git-context]]", "[[rule-github-issues]]"]
origin: raw/2026-09-16/2238/ledger.md#case-220
sprint: migration
created: 2026-09-16
tags: [session, harness, git, github]
---

## Context

`rule-git-context` (`built`) pulls at `/hi` and prints the failure when the branch has no upstream; `rule-github-issues` (`built`) lists the open issues and prints `gh auth login` when `gh` is not logged in. Both print their line at every `/hi`; decisions 11.1 and 11.2 parked them for the close of the sprint, and case 209 lists that close under `estimate-sprint-migration-leftovers-gone`.

## Problem

Whether to set an upstream and log `gh` in, or to keep both lines as they are, is the sprint's closing decision, not this session's; the Frontier names it every session until then.

## Deferred

### [[rule-git-context]]

the pull without an upstream at /hi — set the upstream of `migration`, or keep the printed failure as the decision 11.1 made it; at the close of the sprint, read by estimate-sprint-migration-leftovers-gone

### [[rule-github-issues]]

gh not logged in, no GitHub remote — log in and add the remote, or keep the printed line as decision 11.2 made it; at the close of the sprint, read by estimate-sprint-migration-leftovers-gone

## History

- 2026-09-17 created · raw/2026-09-16/2238/ledger.md#case-220
