---
type: estimate
kind: QA
status: pending
target: "[[rule-retro]]"
purpose: Whether /retro loads while guppi test or guppi style finds something, its lines Tests and Style running both commands with --exit-zero and ending with the line that names the exit code
method: "by hand, after the librarian's render that writes .claude/skills/retro/SKILL.md from the Render of rule-retro with --exit-zero on its lines Tests and Style: the text of .claude/skills/retro/SKILL.md read against the Criterion, and the first load of /retro after that render read in the transcript of its session under ~/.claude/projects/, the skill loaded and its lines Tests and Style each ending with the line that names the exit code; recorded in the estimate line with the transcript named"
deferred_by: ["[[decision-case-1007]]"]
origin: raw/2026-11-02/1337/ledger.md#case-1003.4
sprint: plugin
created: 2026-11-02
tags: [session, workflow, harness]
---

## Criterion

When:
The agent calls `/retro` of `.claude/skills/retro/SKILL.md` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, after `uv run --project .guppi guppi render` wrote that file from `rule-retro`.

Then:
The skill loads whatever `uv run --project .guppi guppi test` and `uv run --project .guppi guppi style` find: its lines Tests and Style run both commands with `--exit-zero`.
**＋** Each of those lines comes back with the output of its command and a last line that names the exit code of its run, and the agent takes each failing test and each style finding from it.
**－** The line Ledger runs `uv run --project .guppi guppi tail` as before.

## History

- 2026-11-02 created · [[decision-case-1003.4]]
- 2026-11-02 deferred · [[decision-case-1007]]
