---
type: decision
case: "1036"
status: current
update: ["[[rule-git-context]]", "[[rule-skill-hi]]", "[[rule-default-mode]]", "[[estimate-git-context-offers-git-init]]", "[[estimate-clean-branch-writes-the-session-files]]"]
origin: raw/2026-11-04/0807/ledger.md#case-1036
sprint: plugin
created: 2026-11-04
tags: [session, harness, git, plugin, ci]
---

## Problem

In a new folder the step of `/hi` offers to run `git init -b main`, but the session stands in Plan Mode, where the agent runs no command that writes, so on the person's yes nothing happens and the check of the step fails.

## Recommend

- **How the repository gets made in a new folder**
  - Recommended: (a) the person types the command `! git init -b main`; the step asks no question and the agent runs nothing.
  - Answer: agreed, (a).
- **What the Case covers**
  - Recommended: (a) only the step of `/hi` in a folder with no git repository; the plan approval at install stays as it is.
  - Answer: agreed, (a).

## History

- 2026-11-20 created · raw/2026-11-04/0807/ledger.md#case-1036
