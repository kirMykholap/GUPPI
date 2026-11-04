---
type: lesson
kind: error
root_cause: "the .claude/settings.json of the clean version sets \"defaultMode\": \"plan\", so the first /hi of a new project opens in Plan Mode, where the step of rule-git-context cannot run its one write"
status: new
origin: raw/2026-11-04/0358/ledger.md#L36
sprint: plugin
created: 2026-11-04
tags: [git, plugin]
---

## Trigger

2026-11-04, the trial session in C:/PROJECTS/guppi-trial-0358/no-git (transcript 2b6bed0c, L64): on the person's yes to git init -b main the agent ran nothing and told the person to type `! git init -b main`, since the session stood in Plan Mode

## Root cause

the .claude/settings.json of the clean version sets "defaultMode": "plan", so the first /hi of a new project opens in Plan Mode, where the step of rule-git-context cannot run its one write

## History

- 2026-11-04 created · raw/2026-11-04/0358/ledger.md#L36
