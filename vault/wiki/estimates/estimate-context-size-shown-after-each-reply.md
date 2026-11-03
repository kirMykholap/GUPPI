---
type: estimate
kind: QA
status: passed
target: "[[rule-context-size]]"
purpose: After each reply the person sees the size of the context and its change since the last reply
method: uv run --project .guppi pytest .guppi/tests/test_context.py; the live reading by hand, the line after the replies of a session in the chat
checked: 2026-10-02
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, session]
core: true
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi context` runs after a reply of the main agent and reads the transcript at `transcript_path`.

Then:
With no error of its own, the hook prints JSON with a `systemMessage` of one line that opens with `context: <N> tokens (<+D> since the last reply)`.
**＋** N is the sum of the input, cache read, cache creation and output tokens of the last main-agent API call the transcript holds; D is N less the same sum at the last main-agent call before the start of the turn, the last `user` record that the function of `.guppi/guppi/ledger.py` names the person's message or a returned answer.
**＋** The records of a subagent (`isSidechain`) are not counted.
**＋** On the re-fire (`stop_hook_active`), with a transcript it cannot read, or with no call that carries `usage`, the hook prints nothing.
**－** A record with no `origin.kind`, a record marked `isMeta` and a tool result do not move the call that D is counted from.
**－** The hook never blocks: it exits 0 in every case.

## Result

2026-10-02, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
