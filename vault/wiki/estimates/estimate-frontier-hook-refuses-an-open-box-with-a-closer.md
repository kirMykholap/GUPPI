---
type: estimate
kind: QA
status: passed
target: "[[rule-frontier-hook]]"
purpose: Whether an Edit, Write or MultiEdit of the frontier.md of a session folder that would leave a line with the box [ ] beside a closer, or with a closed box and no closer, is refused before it runs, with a reason that names each item, and every other such call passes
method: uv run --project .guppi guppi test, which runs .guppi/tests/test_frontierguard.py
checked: 2026-11-26
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [hooks, harness, session]
core: true
---

## Criterion

When:
The agent calls `Edit`, `Write` or `MultiEdit` on a file `vault/raw/<date>/<HHMM>/frontier.md`, and the `PreToolUse` hook `uv run --project .guppi guppi frontierguard` of `.guppi/guppi/frontierguard.py` reads the payload.
**＋** Or `.guppi/tests/test_frontierguard.py` runs the hook over a made-up payload and a made-up `frontier.md`.

Then:
The hook works out the whole text the call would leave: the `content` of a `Write`, or the file with each `old_string` replaced by its `new_string` in order, once or at each match with `replace_all`, by the one function that `builder_write` of `.guppi/guppi/ratified.py` uses too.
**＋** When a box line of that text, under any heading, keeps the box `[ ]` while its last segment after ` · ` is a closer by `CLOSERS` of `.guppi/guppi/prespec.py`, the hook exits 2, and the call does not run.
**＋** When a box line of that text, under any heading, has the box `[x]` or `[-]` while its last segment after ` · ` is no closer by `CLOSERS`, a line with no ` · ` included, the hook exits 2 too, and the call does not run.
**＋** The hook takes that second judgment from the one function of `.guppi/guppi/prespec.py` by which its check of the Frontier reports a line closed without a closer.
**＋** The reason on stderr names each such item, with its closer where the box is open, and says that the box and the closer are written in one edit of the whole line, `[x]` for an item ended and `[-]` for an item put off.
**＋** Before the refusal one line goes to the day's event log, since a blocked call has no `PostToolUse`.
**－** A text whose open lines carry no closer and whose closed lines each carry one exits 0, and so do a file other than such a `frontier.md` and a tool other than `Edit`, `Write`, `MultiEdit`, `Bash` and `PowerShell`.
**－** An old string missing or found more than once without `replace_all`, a file to edit that does not exist, and a payload the hook cannot read exit 0, the last with one line on stderr; the hook never raises.
**－** The findings of the check of the Frontier in `.guppi/guppi/prespec.py`, and their order, stay as they are.

## Result

2026-11-26, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
