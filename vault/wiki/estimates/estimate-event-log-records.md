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

### case 111.1

When:
The person submits a prompt and the `UserPromptSubmit` hook `uv run guppi event prompt` runs.

Then:
When the prompt, trimmed, is `/hi` or starts with `/hi `, and no `hi` of this session's stamp follows its first `session-start` in the logs walked, the log gains `- HH:MM:SS <stamp> hi`, the stamp from the payload's `session_id`.
**＋** A second `/hi` of the same session writes nothing: one session, one `hi` line.
**＋** Any other prompt writes nothing; exit 0 either way, an error on stderr only.
**＋** The "Known limit" paragraph of the page says the limit is lifted by this Case; a `hi` of one session no longer belongs to another.
**＋** `estimate-event-log-records` gets a `### case 111.1` block, `pending`; read at the next `/hi`: the log carries `<stamp> hi` for that session, and a repeated `/hi` adds no line.

### case 125

When:
The person submits `/hi` and the `UserPromptSubmit` hook `uv run guppi event prompt` runs.

Then:
Having written the `hi` line, the hook prints on stdout `hi: HH:MM:SS <stamp> → raw/<date>/<HHMM>/`; when a `hi` of this session already exists it prints `hi: already recorded at HH:MM:SS → raw/<date>/<HHMM>/` and writes nothing; on any other prompt it is silent. The line reaches the session's context.
**＋** The Render of `rule-skill-hi`: "`HHMM` the time of the `hi` line above (case 73)" → "`HHMM` from the `hi:` line the `UserPromptSubmit` hook put in context (cases 73, 125)".
**＋** `estimate-event-log-records` gets a `### case 125` block, `pending`; the test: `/hi` → the line written and stdout `hi: … → raw/…/`; a second `/hi` → stdout `already recorded`, no new line in the log; `hello` → stdout empty. The live reading at the next `/hi`: the `hi:` line is in the context and the folder is named without a read call.
**－** `rule-skill-hi` is a MOC, no `contract` is written; `rule-event-log` is `contract: changed`.

## Method

pytest in `tests/test_event.py` drives `guppi.event` with piped JSON payloads against a
temp vault; the git-ignore and timing readings are taken once by hand, through a pipe, and
written into the estimate line.

## Result

block 125 against tests/test_event.py: /hi prints `hi: 15:02:11 abc12345 → raw/2026-09-09/1502/` and writes the line; a second /hi prints `already recorded at 15:02:11 → raw/2026-09-09/1502/` and adds no line; across midnight the folder is the hi date's; other prompts print nothing; the live half waits for the next /hi

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-9
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-14 criterion: case 111.1 added · [[decision-case-111.1]]
- 2026-09-14 criterion: case 125 added · [[decision-case-125]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1029/ledger.md#L23
- 2026-09-14 status: passed → passed · raw/2026-09-14/1029/ledger.md#L34
