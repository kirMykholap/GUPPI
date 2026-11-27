---
type: estimate
kind: Research
status: passed
target: "[[entity-sprint-plugin]]"
purpose: "Whether the hooks of the harness answer the calls made inside Code Mode code as they answer them outside it: the refusals of guard and bashguard, the inputs that grepguard and pageread rewrite, and the PostToolUse hooks"
method: "by hand, after the person's word that the hook session in the clone C:/PROJECTS/guppi-codemode-trial ran: its transcript, in the folder of the clone under ~/.claude/projects/, the event_log.md of the day under vault/raw/ of the clone and the output of git -C C:/PROJECTS/guppi-codemode-trial status --short read against the Criterion, the transcript and the findings in the estimate line"
origin: raw/2026-11-27/0947/ledger.md#case-1079.2
sprint: plugin
created: 2026-11-27
tags: [sprint, harness, hooks]
once: true
---

## Criterion

When:
The person runs a session of `claude` in a terminal in `C:/PROJECTS/guppi-codemode-trial`, with `CLAUDE_CODE_EXPERIMENTAL_CODE_MODE` set to `1` and outside Plan Mode, on a prompt that asks for one piece of code that makes four tool calls.
**＋** The code edits `CLAUDE.md`, greps `vault/wiki/` for `^type: decision` for file paths only, runs a Bash heredoc that writes a file, and reads the page of `entity-sprint-plugin` with no offset and no limit.

Then:
Determine under which tool name each call from the code reached the hooks of `.claude/settings.json`.
**＋** Determine whether `guppi guard` and `guppi bashguard` of `.guppi/guppi/` refused the edit and the heredoc, as they refuse them outside Code Mode.
**＋** Determine whether the input that `guppi grepguard` and `guppi pageread` rewrite reached the calls: a Grep that prints no path of a Decision page, and a Read cut before the `## History` of the page.
**＋** Determine whether the `PostToolUse` hooks ran on the calls that ran: the note of `guppi pageread --after` in the result, and one line of `guppi event tool` per call in the event log of the clone.
**－** Where a hook did not fire, the change stays in the clone: nothing of the clone is pushed or pulled into this repository.

## Result

2026-11-27, after the person's word, the transcript ea7156d9 in ~/.claude/projects/C--PROJECTS-guppi-codemode-trial/, vault/raw/2026-11-27/event_log.md of the clone and git -C C:/PROJECTS/guppi-codemode-trial status --short (no line): one REPL call made Edit, Grep, Bash and Read, each reaching the hooks under its own tool name; guard refused the Edit of CLAUDE.md (rule-claude-md) and bashguard refused the heredoc that writes trial.txt, both with event lines; the Grep printed only vault/wiki/rules/rule-decisions-schema.md, so the exclusion of grepguard reached it; the Read came back cut before the History with the PostToolUse note of pageread (lines 43–95); the event log holds tool lines for Grep, Read and REPL; CLAUDE.md unchanged and no trial.txt

## History

- 2026-11-27 created · [[decision-case-1079.2]]
- 2026-11-27 status: pending → passed · raw/2026-11-27/0947/ledger.md#L34
