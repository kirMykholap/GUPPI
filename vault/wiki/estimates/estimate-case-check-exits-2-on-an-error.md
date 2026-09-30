---
type: estimate
kind: QA
status: pending
target: "[[rule-case-check]]"
purpose: Whether the Stop run of the Case check exits 2 with the error on stderr when it raises after reading the payload, and exits 0 on the re-fire, on an empty payload and in the --subagent run
method: uv run pytest tests/test_casecheck.py — piped payloads, a function of the hook patched to raise
origin: raw/2026-09-30/2042/ledger.md#case-555.1
sprint: migration
created: 2026-09-30
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `Stop` hook `uv run guppi casecheck` fires, and an exception rises in `guppi/casecheck.py` after the hook has read the payload: while it reads the transcript, the event log or the store, or while it compares a shown Case or reads a sending.

Then:
`guppi casecheck` exits 2. Its stderr holds `casecheck: not checked: <error>` and the advice to show the Case again once the cause is fixed, so the agent sees the error at the end of that reply.
**＋** While the cause stands, `guppi casecheck` blocks with the same error at every `Stop`.
**－** An empty or unreadable payload of `guppi casecheck` exits 0 with its line on stderr.
**－** On the re-fire after a block (`stop_hook_active`), `guppi casecheck` exits 0 and compares nothing, so it cannot loop.
**－** The run `uv run guppi casecheck --subagent` on `SubagentStop` keeps exit 0 with its error on stderr, since a send-back to `case-guppi` is not ended by `stop_hook_active` and would loop.
**－** A refusal of `guppi casecheck` with no error keeps its own reason on stderr and its exit 2.

## History

- 2026-09-30 created · [[decision-case-555.1]]
