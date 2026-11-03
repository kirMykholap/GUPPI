---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the Stop run of the Case check exits 2 with the error on stderr when it raises after reading the payload, at most three times for one error since the person's last message, and exits 0 on an empty payload and in the --subagent run
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py — piped payloads, a function of the hook patched to raise
checked: 2026-10-06
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, workflow]
core: true
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi casecheck` fires, and an exception rises in `.guppi/guppi/casecheck.py` after the hook has read the payload: while it reads the transcript, the event log or the store, or while it compares a shown Case or reads a sending.

Then:
`guppi casecheck` exits 2. Its stderr holds `casecheck: not checked: <error>` and the advice to show the Case again once the cause is fixed, so the agent sees the error at the end of that reply.
**＋** While the cause stands, `guppi casecheck` blocks with the same error at each `Stop`, whether `stop_hook_active` is set or not, until three of its own refusals since the person's last message hold that error; then it exits 0, as `estimate-case-check-judges-a-showing-after-a-refusal` sets it.
**－** An empty or unreadable payload of `guppi casecheck` exits 0 with its line on stderr.
**－** With `stop_hook_active` set and a transcript it cannot read, `guppi casecheck` exits 0 and prints nothing, so it cannot loop.
**－** The run `uv run --project .guppi guppi casecheck --subagent` on `SubagentStop` keeps exit 0 with its error on stderr, since a send-back to `case-guppi` is not ended by `stop_hook_active` and would loop.
**－** A refusal of `guppi casecheck` with no error keeps its own reason on stderr and its exit 2.

## Result

2026-10-06, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
