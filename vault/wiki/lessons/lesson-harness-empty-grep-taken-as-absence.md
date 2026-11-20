---
type: lesson
kind: error
root_cause: a claim of absence rested on one empty search, with no second search or a Read to confirm that the glob reached the files
status: new
origin: raw/2026-11-04/0807/ledger.md#L59
sprint: plugin
created: 2026-11-04
tags: [harness]
---

## Trigger

at the discussion of C15 the main agent told the person that `.claude/agents/*.md` held no `effort` or `model`, from a Grep of `effort|^model:` with the glob `{agents/*.md,settings*.json}` under the path `.claude` that printed nothing; case-guppi then read `model: opus` and `effort: medium` in case-guppi.md

## Root cause

a claim of absence rested on one empty search, with no second search or a Read to confirm that the glob reached the files

## History

- 2026-11-20 created · raw/2026-11-04/0807/ledger.md#L59
