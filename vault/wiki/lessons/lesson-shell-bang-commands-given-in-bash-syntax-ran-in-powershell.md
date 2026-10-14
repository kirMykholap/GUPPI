---
type: lesson
kind: error
root_cause: the commands were written for Git Bash, while the ! prompt of this Windows setup runs PowerShell 5.1, which drops an empty "" argument and takes no < redirection
status: new
origin: raw/2026-10-14/1536/ledger.md#L11
sprint: plugin
created: 2026-10-14
tags: [ci]
---

## Trigger

ssh-keygen -N "" -f ~/prod_deploy, given to the owner to type after ! in the prompt, failed with "Too many arguments"

## Root cause

the commands were written for Git Bash, while the ! prompt of this Windows setup runs PowerShell 5.1, which drops an empty "" argument and takes no < redirection

## History

- 2026-10-14 created · raw/2026-10-14/1536/ledger.md#L11
