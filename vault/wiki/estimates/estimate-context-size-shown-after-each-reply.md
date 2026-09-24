---
type: estimate
kind: QA
status: passed
target: "[[rule-context-size]]"
purpose: After each reply the person sees the size of the context and its change since the last reply
method: uv run pytest tests/test_context.py; the live reading by hand, the line after the replies of a session in the VS Code chat
checked: 2026-09-24
origin: raw/2026-09-24/1303/ledger.md#case-392.1
sprint: migration
created: 2026-09-24
tags: [hooks, harness, session]
---

## Criterion

When:
The `Stop` hook `uv run guppi context` runs after a reply of the main agent and reads the transcript at `transcript_path`.

Then:
The hook prints JSON with a `systemMessage` of one line that opens with `context: <N> tokens (<+D> since the last reply)`.
**＋** N is the sum of the input, cache read, cache creation and output tokens of the last main-agent API call the transcript holds; D is N less the same sum at the last main-agent call before the person's last prompt.
**＋** The records of a subagent (`isSidechain`) are not counted.
**＋** On the re-fire (`stop_hook_active`), with a transcript it cannot read, or with no call that carries `usage`, the hook prints nothing.
**－** The hook never blocks: it exits 0 in every case.

## Result

2026-09-24, `uv run pytest tests/test_context.py`: 7 passed; by hand in the VS Code chat of session 1916: the person reports that the `systemMessage` of the `Stop` hook is shown after each reply

## History

- 2026-09-24 created · [[decision-case-392.1]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/1916/ledger.md#L1
