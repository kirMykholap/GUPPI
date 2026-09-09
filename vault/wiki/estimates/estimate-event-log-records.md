---
type: estimate
kind: QA
status: pending
target: rule-event-log
origin: raw/2026-09-09/ledger.md#case-9
sprint: migration
created: 2026-09-09
tags: [session, hooks, harness]
---

## Context

The ledger hook trusts this log to say whether `/hi` happened, so the lines it needs — the
session's start and the `hi` mark — must land in the right file, in order, and the file
must stay out of git. The timing is read through a pipe, the only shape a hook runs in.

## Criterion

After a session starts and one tool call completes, `raw/<date>/event_log.md` carries a
`session-start` line with this session's id and a `tool` line after it; after `/hi` it
carries a `hi` line; `git check-ignore` reports the file ignored; and a hook invocation
with piped stdin exits 0 and finishes under 2 s.

## Method

pytest in `tests/test_event.py` drives `guppi.event` with piped JSON payloads against a
temp vault; the git-ignore and timing readings are taken once by hand, through a pipe, and
written into the estimate line.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-9
