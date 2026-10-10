---
type: lesson
kind: error
root_cause: the command of a check was written into the Case from its pattern and never run before the signature; the folders hold compiled caches that git ignores and grep reads
status: archived
origin: raw/2026-09-23/1126/ledger.md#L41
sprint: migration
created: 2026-09-23
tags: [session, workflow]
---

## Trigger

in session 1126 the tasks line of Case 365 and the method of Case 367 signed `grep -rni 'rule.class' guppi/ tests/`; in Work Mode it matched four stale gitignored `__pycache__/*.pyc` — a cache of another interpreter and those of the removed pretask modules — and both Cases were shown again with `--include='*.py'`

## Root cause

the command of a check was written into the Case from its pattern and never run before the signature; the folders hold compiled caches that git ignores and grep reads

## History

- 2026-09-23 created · raw/2026-09-23/1126/ledger.md#L41
- 2026-10-10 status: new → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
