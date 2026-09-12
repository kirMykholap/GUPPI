---
type: decision
case: "91"
status: current
update: [rule-governed-files-hook]
supersedes: [decision-case-83]
origin: raw/2026-09-12/ledger.md#case-91
sprint: migration
created: 2026-09-12
tags: [hooks, harness, render]
---

## Context

A `PreToolUse` hook that blocks a tool leaves no `PostToolUse`, so the call reaches the
event log never. The fact is `lesson-hooks-blocked-pretooluse-leaves-no-posttooluse-event`
(`knowledge`, with the live probe of session J as its source). The live clause of
`estimate-governed-files-hook-refuses` asks for the call in the event log, and the reading
failed on it: two of its three clauses hold. Case 83 deferred the choice here.

## Problem

Either the guard writes the line itself, or the clause leaves the criterion. A refusal is
the one event of a session the log cannot see.

## Given

The guard exits 2 with the rule's slug and the file on stderr, and writes nothing.
**＋** `guppi/event.py` holds `format_line(name, payload, words, session, now)`,
`log_path(project_dir, now)` and `append(path, line)`; `guard.py` already imports
`project_root` and `read_payload` from it. A log line reads
`- 15:57:15 d08a5ca5 tool Read: …`.
**＋** The live clause already asks for the line, so no prose of the Estimate changes: it
takes the `### case 91` block and goes from `failed` to `pending`.
**＋** The reading is taken in this session: one refused `Edit` on any governed file.
**－** Cases 85 and 89 change the world around the guard — what `settings.json` holds and
when the render runs — but not the guard itself. This is the only change of its code in
the session.

## Criterion

- [[estimate-governed-files-hook-refuses]] § case 91

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-91
