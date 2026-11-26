---
type: lesson
kind: knowledge
root_cause: a project with no settings file of its own can hold one written by Claude Code's plugin install, so /guppi:install meets .claude/settings.json at a path of its install and sets it aside, and the setup Case shows the plugin line to be dropped; in p2-license, p3-set-aside and p4-offline the install that already stood wrote no such file
status: new
source: probe p1-code of session 0816, transcript ~/.claude/projects/C--tmp-guppi-1055-p1-code/66ad2c5f-8c5a-4bda-badd-8f13c00bfa47.jsonl (raw/2026-11-25/0816/ledger.md#L25)
origin: raw/2026-11-25/0816/ledger.md#L32
sprint: plugin
created: 2026-11-25
tags: [plugin]
---

## Trigger

in p1-code of session 0816, after /plugin marketplace remove and add of guppi-marketplace, /plugin install guppi@guppi-marketplace wrote .claude/settings.json with enabledPlugins guppi@guppi-marketplace true into the project, at 17:56 local, before /guppi:install

## Root cause

a project with no settings file of its own can hold one written by Claude Code's plugin install, so /guppi:install meets .claude/settings.json at a path of its install and sets it aside, and the setup Case shows the plugin line to be dropped; in p2-license, p3-set-aside and p4-offline the install that already stood wrote no such file

## History

- 2026-11-25 created · raw/2026-11-25/0816/ledger.md#L32
- 2026-11-26 updated: source set, which its knowledge kind requires · [[decision-case-1058]]
