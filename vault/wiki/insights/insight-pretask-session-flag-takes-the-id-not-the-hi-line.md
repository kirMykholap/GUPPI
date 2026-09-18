---
type: insight
pattern: The `/pre-task` skill says "the stamp from the `hi:` line", but `--session` of `guppi pretask` takes the eight-character session id alone, one of the three tokens of that line; a wrong token answers "no hi recorded" with exit 0 and the value cut to eight characters, so the run looks clean and nothing was checked.
status: open
children: ["[[lesson-pretask-session-flag-takes-the-id-not-the-hi-line]]", "[[lesson-pretask-session-flag-took-the-folder-for-the-stamp]]"]
severity: 2
origin: raw/2026-09-18/2253/ledger.md#L3
sprint: migration
created: 2026-09-18
tags: [harness, session]
---

## Pattern

Two lessons, one cause. In session 1252 the agent passed the whole `hi:` line — time and id — as `--session`; in session 2253 it passed the session folder. Both times `guppi pretask --check` answered "no hi recorded for session <value cut to eight characters>; nothing checked" and exited 0, and the check did not run. The skill text of `/pre-task` still says "the stamp from the `hi:` line", while the line carries three tokens — time, session id, folder — and the flag takes the second alone. The first lesson changed no text of the skill; the second is the same reading of the same sentence.

## Proposal

An `update` of the Render of `rule-pretask` that names the eight-character session id — the second token of the `hi:` line — as the value of `--session`, and one line on the reading of the output: the first line, not the exit code. A suggestion, not a decision.

## History

- 2026-09-18 created · raw/2026-09-18/2253/ledger.md#L3
