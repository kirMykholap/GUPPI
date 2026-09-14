---
type: lesson
kind: knowledge
root_cause: the CLI is enabled in Settings and talks to the running desktop app — "the first command you run launches Obsidian" — so a Stop hook, make lint or CI cannot use it; its orphans (no inbound link at all) is weaker than lint's (no owner in the tree); not adopted, lint stays
status: new
source: https://obsidian.md/help/cli
origin: raw/2026-09-14/1633/ledger.md#L59
sprint: migration
created: 2026-09-14
tags: [harness]
---

## Trigger

session P weighed the Obsidian CLI (1.12.7+, commands orphans, unresolved, backlinks, base:query) as a replacement for guppi lint and the index files

## Root cause

the CLI is enabled in Settings and talks to the running desktop app — "the first command you run launches Obsidian" — so a Stop hook, make lint or CI cannot use it; its orphans (no inbound link at all) is weaker than lint's (no owner in the tree); not adopted, lint stays

## History

- 2026-09-14 created · raw/2026-09-14/1633/ledger.md#L59
