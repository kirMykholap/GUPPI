---
type: decision
case: "256"
status: archived
update: ["[[rule-prespec]]", "[[estimate-prespec-reconciles]]", "[[insight-pretask-session-flag-takes-the-id-not-the-hi-line]]"]
origin: raw/2026-09-20/0527/ledger.md#case-256
sprint: migration
created: 2026-09-20
tags: [session, workflow, harness]
---

## Context

`rule-prespec` is a Leaf, `enforcement: render`, governing `.claude/skills/pre-task/SKILL.md`. Its Render says: run `guppi pretask --check <plan> --session <stamp>`, "the stamp from the `hi:` line". The `hi:` line carries three tokens — the time, the eight-character session id, the folder — and `--session` takes the id alone; `session_stamp` cuts the value to eight characters, so a wrong token answers "no hi recorded for session <8 characters>; nothing checked" on stderr with exit 0, the design of case 213: a check without a `hi` blocks nothing. Twice the agent passed the wrong token: the whole line in 1252, the folder in 2253; both times the check did not run and the run looked clean. The librarian clustered the two lessons into `insight-pretask-session-flag-takes-the-id-not-the-hi-line`, severity 2, `open`, with the proposal: the Render names the id, the second token, and one line on reading the output — its first line, not the exit code. Two Estimates: `estimate-prespec-reconciles` — the live reading of the Render, its Criterion opens with the same phrase "the stamp from the `hi:` line" and is replaced whole; `estimate-prespec-checks-the-plan` — the tests of `--check`, untouched: the code does not change.

## Problem

The text of the rule names the value of the flag with the word "stamp", which in the context also names the whole `hi:` line; the code takes one token of three and answers a wrong one with a silent exit 0. The agent read the text two different ways, and both times `/pre-task` checked nothing. The Render has to name the token exactly and tell the agent to read the first line of the output, not the exit code.

## History

- 2026-09-20 created · raw/2026-09-20/0527/ledger.md#case-256
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
