---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether a subagent with its own autoCompactWindow compacts before it reaches that size, keeps its earlier lines in its transcript file, still fires SubagentStop after the compaction, and goes on from its interim file, as the procedure for a full case-guppi rests on
method: "by hand, in the Work Mode of the session that replaces this Criterion: the transcript of the test helper under ~/.claude/projects/ and the log of the test folder, as a run of the test by claude -p left them, read against the Criterion and recorded in the estimate line (as set in case 896.1, which reads the saved files of the run of session 1907 with no new run)"
checked: 2026-10-29
origin: raw/2026-10-28/1907/ledger.md#case-895
sprint: plugin
created: 2026-10-28
tags: [harness, hooks, case-build]
---

## Criterion

When:
The main agent runs `claude -p` in a test folder outside the repository, whose agent file of a test helper sets `autoCompactWindow: 100000` and tells it to read its interim file again after a compaction, and whose hooks log each `SubagentStop` and `PostCompact` event.
**＋** The first run starts the test helper, has it read text files and write its interim file; a second run with `--resume` sends it more files, past 100000 tokens in all; a third run with `--resume` asks it to go on.

Then:
The transcript of the test helper under `~/.claude/projects/` holds a `compact_boundary` record whose `preTokens` is below 100000: the helper compacts before it reaches the size its agent file sets.
**＋** That transcript file keeps the lines of the helper before the `compact_boundary` record.
**＋** The log of the test folder holds a `SubagentStop` line of the test helper after the compaction.
**＋** After the compaction the interim file stands in the context of the test helper again, read by its own `Read` call or put back by Claude Code, and the helper goes on from what it says.
**－** The size of 100000 tokens binds the test helper alone, through its agent file, and no size is set in the shell of `claude -p`.
**－** No file of the repository changes by the test.

## Result

2026-10-29, Retro of session 2312, the saved files of the test run of session 1907 read with no new run: the transcript agent-a12be5ab8317687d5.jsonl of the test helper holds compact_boundary records with preTokens 72126, 74307 and 75012, all below the 100000 that its agent file tester.md sets; its lines 1–31 before the first record stand; log.txt holds SubagentStop tester a12be5ab8317687d5 at 22:33:19 and 22:34:13, after the PostCompact lines at 22:32:19, 22:32:44 and 22:33:05; after the first compaction the helper read interim.md by its own Read, after the second and third Claude Code put it back, and it gave the eight secret words; the test folder lies outside the repository

## History

- 2026-10-28 created · [[decision-case-895]]
- 2026-10-28 status: pending → failed · raw/2026-10-28/1907/ledger.md#L19
- 2026-10-29 updated: the Criterion replaced whole — the compaction comes below the set size, as the test showed · [[decision-case-896.1]]
- 2026-10-29 status: pending → passed · raw/2026-10-28/2312/ledger.md#L24
