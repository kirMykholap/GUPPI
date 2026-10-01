---
type: estimate
kind: QA
status: passed
target: "[[rule-context-size]]"
purpose: Whether the Stop run of guppi context prints its own error as the systemMessage in place of the size line and exits 0, and the --prompt run keeps its error on stderr with exit 0
method: uv run pytest tests/test_context.py — piped payloads, a function of the hook patched to raise
checked: 2026-10-01
origin: raw/2026-09-30/2042/ledger.md#case-555.2
sprint: migration
created: 2026-09-30
tags: [hooks, harness, session]
---

## Criterion

When:
The `Stop` hook `uv run guppi context` fires, and an exception rises in `guppi/context.py` while it counts the tokens of the records it read from the transcript.

Then:
`guppi context` prints JSON with a `systemMessage` of one line, `context: not counted: <error>`, in place of the size line, so the person sees the error after that reply.
**－** `guppi context` exits 0 on its own error too, so it never blocks the reply.
**－** On the re-fire after a block (`stop_hook_active`), with a transcript it cannot read, or with no call that carries `usage`, `guppi context` prints nothing, as before.
**－** The run `uv run guppi context --prompt` on `UserPromptSubmit` keeps its error on stderr and exit 0, since a block there would block the person's message.

## Result

2026-10-01, uv run pytest tests/test_context.py: 9 passed (-k error: 2 passed)

## History

- 2026-09-30 created · [[decision-case-555.2]]
- 2026-10-01 status: pending → passed · raw/2026-09-30/2356/ledger.md#L41
