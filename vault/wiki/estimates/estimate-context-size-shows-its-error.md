---
type: estimate
kind: QA
status: passed
target: "[[rule-context-size]]"
purpose: Whether the Stop run of guppi context prints its own error as the systemMessage in place of the size line and exits 0, and the --prompt run keeps its error on stderr with exit 0
method: uv run --project .guppi pytest .guppi/tests/test_context.py — piped payloads, a function of the hook patched to raise
checked: 2026-10-01
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, session]
core: true
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi context` fires, and an exception rises in `.guppi/guppi/context.py` while it counts the tokens of the records it read from the transcript.

Then:
`guppi context` prints JSON with a `systemMessage` of one line, `context: not counted: <error>`, in place of the size line, so the person sees the error after that reply.
**－** `guppi context` exits 0 on its own error too, so it never blocks the reply.
**－** On the re-fire after a block (`stop_hook_active`), with a transcript it cannot read, or with no call that carries `usage`, `guppi context` prints nothing, as before.
**－** The run `uv run --project .guppi guppi context --prompt` on `UserPromptSubmit` keeps its error on stderr and exit 0, since a block there would block the person's message.

## Result

2026-10-01, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
