---
type: estimate
kind: QA
status: passed
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

## Result

Passing. pytest: twelve cases in `tests/test_event.py`. By hand, 2026-09-09 session B:
`session-start clear` and `session-start resume` stamped `44c1aae1`, then `hi`, then the
`tool` lines, in order; `git check-ignore -v` → `.gitignore:47`; three piped invocations
of `guppi event tool` exited 0 in 0.10 s each. A UTF-8 payload through the cp1252 stdin a
hook gets on Windows came out as mojibake until `read_text` took the bytes
(`lesson-hooks-windows-stdin-encoding`); a test covers it since.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-9
- 2026-09-09 status: pending → passed · written by hand, no generator yet
