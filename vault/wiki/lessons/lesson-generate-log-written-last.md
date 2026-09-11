---
type: lesson
kind: error
root_cause: generate.py writes log.md once at the end of apply (write_log at line 649), so any exception inside apply keeps the page writes and loses the feed; the log must be appended per entry or the run must be atomic
status: new
origin: raw/2026-09-10/ledger.md#L97
sprint: migration
created: 2026-09-10
tags: [harness]
---

## Trigger

after the aborted run the pages and History lines of entries 78–82 existed but their nine lines never reached vault/wiki/log.md

## Root cause

generate.py writes log.md once at the end of apply (write_log at line 649), so any exception inside apply keeps the page writes and loses the feed; the log must be appended per entry or the run must be atomic

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#L97
- 2026-09-11 estimates removed: a lesson has no Estimate · [[decision-case-53.1]]
