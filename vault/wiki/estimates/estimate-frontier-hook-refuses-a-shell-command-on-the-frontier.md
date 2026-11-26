---
type: estimate
kind: QA
status: passed
target: "[[rule-frontier-hook]]"
purpose: Whether a Bash or PowerShell call whose command names frontier.md is refused before it runs, with a reason that says how the file is changed and read, and every other shell call passes
method: uv run --project .guppi guppi test, which runs .guppi/tests/test_frontierguard.py
origin: raw/2026-11-26/1515/ledger.md#case-1069.1
sprint: plugin
created: 2026-11-26
tags: [hooks, harness, session]
---

## Criterion

When:
The agent calls `Bash` or `PowerShell`, and the `PreToolUse` hook `uv run --project .guppi guppi frontierguard` of `.guppi/guppi/frontierguard.py` reads `tool_input.command` of the payload.
**＋** Or `.guppi/tests/test_frontierguard.py` runs the hook over a made-up payload of `Bash` or `PowerShell`.

Then:
When the command names `frontier.md`, in any letter case, the hook exits 2, and the call does not run.
**＋** The reason on stderr says that `frontier.md` changes only by an `Edit` of the whole line or by a `Write`, and is read by `Read` or `Grep`, never through a shell command.
**＋** The same reason says that a commit message names the Frontier in words, since a `git commit` whose message names `frontier.md` is refused too.
**＋** Before the refusal one line goes to the day's event log, since a blocked call has no `PostToolUse`.
**－** A command that does not name `frontier.md` exits 0, and a payload the hook cannot read exits 0 with one line on stderr; the hook never raises.
**－** A script that a command runs by its path and that writes `frontier.md` is not seen; the check of the Frontier in `.guppi/guppi/prespec.py` still reports a line it leaves wrong.

## Result

2026-11-26, Retro, uv run --project .guppi pytest .guppi/tests/test_frontierguard.py: 23 passed; a Bash sed -i, a PowerShell Set-Content, a cat, a git commit -m naming frontier.md and FRONTIER.MD are refused by exit 2 with the reason on how the file is changed and read and on a commit message, one event log line each; commands that name no frontier.md exit 0 with no log line; the full guppi test 2034 passed

## History

- 2026-11-26 created · [[decision-case-1069.1]]
- 2026-11-26 status: pending → passed · raw/2026-11-26/1515/ledger.md#L35
