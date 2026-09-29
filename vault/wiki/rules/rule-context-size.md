---
type: rule
kind: Leaf
purpose: Prevents a session from running on while the person cannot see how full the context window is
status: built
enforcement: hook
implementation_ref: [guppi/context.py, tests/test_context.py, .claude/settings.json]
parent: "[[rule-harness]]"
estimates: ["[[estimate-context-size-shown-after-each-reply]]", "[[estimate-context-size-warns-past-the-limit]]"]
origin: raw/2026-09-24/1303/ledger.md#case-392.1
sprint: migration
created: 2026-09-24
tags: [hooks, harness, session]
---

## Purpose

Prevents a session from running on while the person cannot see how full the context window is. In the VS Code extension the context indicator shows only past half of the window, and `/context` is typed by hand; no hook payload carries the size, only `transcript_path`. The size is counted from the transcript, where every API call of the model carries its `usage`.

## How it works

`uv run guppi context` on `Stop`. It reads the transcript at `transcript_path`, skips the records of a subagent (`isSidechain`), and takes N, the sum of the input, cache read, cache creation and output tokens of the last main-agent call the transcript holds — at `Stop` the last call may not be there yet, so N may lag one call — and D, N less the same sum at the last call before the person's last prompt. It prints JSON with a `systemMessage`: `context: <N> tokens (<+D> since the last reply)`. On the re-fire (`stop_hook_active`), with a transcript it cannot read, or with no call carrying `usage`, it prints nothing; it exits 0 always. At N of 400 000 or more the line ends with `— past 400 000: costly, better take no more work`, and `uv run guppi context --prompt` on `UserPromptSubmit` prints to the agent's context the size and a note for the agent to pass to the person, not an order: the session is already costly, taking on more work is not recommended, and while the Frontier holds open items, deferring them is the better course (case 430); below the limit it prints nothing.

## History

- 2026-09-24 created · [[decision-case-392.1]]
- 2026-09-24 estimate estimate-context-size-shown-after-each-reply added · [[decision-case-392.1]]
- 2026-09-24 updated: the warning past 400 000 tokens (case 392.2) · [[decision-case-392.2]]
- 2026-09-24 estimate estimate-context-size-warns-past-the-limit added · [[decision-case-392.2]]
- 2026-09-25 deferred · [[decision-case-404]]
- 2026-09-25 deferred · [[decision-case-409]]
- 2026-09-25 deferred · [[decision-case-418]]
- 2026-09-25 deferred · [[decision-case-422]]
- 2026-09-25 defer by decision-case-404 superseded · [[decision-case-430]]
- 2026-09-25 defer by decision-case-409 superseded · [[decision-case-430]]
- 2026-09-25 defer by decision-case-418 superseded · [[decision-case-430]]
- 2026-09-25 defer by decision-case-422 superseded · [[decision-case-430]]
- 2026-09-25 updated: past 400 000 tokens both hooks give a note, not an order to close the session; the limit stays (case 430) · [[decision-case-430]]
- 2026-09-30 status: draft → built · cascade
