---
type: estimate
kind: QA
status: failed
target: "[[rule-case-build]]"
purpose: Whether a subagent with its own autoCompactWindow compacts past that size, keeps its earlier lines in its transcript file, still fires SubagentStop after the compaction, and reads its interim file again and goes on, as the later procedure for a full case-guppi needs
method: "by hand, in the Work Mode of the session that creates it: the test of the Criterion run by claude -p in a folder under the temporary area of the session, and the transcript of the test helper and the log of the folder read against the Criterion, recorded in the estimate line"
origin: raw/2026-10-28/1907/ledger.md#case-895
sprint: plugin
created: 2026-10-28
tags: [harness, hooks, case-build]
---

## Criterion

When:
The main agent runs `claude -p` in a test folder outside the repository, whose agent file of a test helper sets `autoCompactWindow: 100000` and tells it to read its interim file again after a compaction, and whose hooks log each `SubagentStop` and `PostCompact` event.
**＋** The first run starts the test helper, has it read text files and write its interim file; a second run with `--resume` sends it more files, past 100000 tokens; a third run with `--resume` asks it to go on.

Then:
The transcript of the test helper under `~/.claude/projects/` holds a `compact_boundary` record after it passes 100000 tokens.
**＋** That transcript file keeps the lines of the helper before the `compact_boundary` record.
**＋** The log of the test folder holds a `SubagentStop` line after the compaction.
**＋** After the compaction the test helper reads its interim file again and goes on from what it says.
**－** The size of 100000 tokens binds the test helper alone, through its agent file, and no size is set in the shell of `claude -p`.
**－** No file of the repository changes by the test.

## Result

2026-10-28, Work Mode: claude -p 2.1.301 run three times (the later two with --resume 1d4d9aab-9372-432f-a27f-b283998e8ad1) in scratchpad/compact-test, a test helper tester (model sonnet, autoCompactWindow: 100000) reading part1..part8 (about 17k tokens each); its transcript agent-a12be5ab8317687d5.jsonl holds 3 compact_boundary records (lines 32, 64, 92) with preTokens 72126, 74307 and 75012 and postTokens about 18–19k, so the compaction came before the helper passed 100000 tokens and the first Then line is not shown; the other lines hold: the 31 lines before the first boundary stay in the file, the log holds SubagentStop tester a12be5ab8317687d5 at 22:33:19 and 22:34:13 after the compactions, and after the first compaction the helper read interim.md itself, after the second and third Claude Code put interim.md back as a recently read file, and the helper went on and named all eight secret words from interim.md in the third run without reading a part again

## History

- 2026-10-28 created · [[decision-case-895]]
- 2026-10-28 status: pending → failed · raw/2026-10-28/1907/ledger.md#L19
