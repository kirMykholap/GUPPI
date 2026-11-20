---
type: lesson
kind: knowledge
root_cause: a background agent does not outlive the process; its transcript and its files stand, and a SendMessage to it resumes it from its transcript, so the main agent checks its case file and note and resumes it with what is left
status: new
source: the task-notification records of session 0807, f7321efe, Claude Code 2.1.317
origin: raw/2026-11-04/0807/ledger.md#L58
sprint: plugin
created: 2026-11-04
tags: [session]
---

## Trigger

twice the Claude Code process ended while a background agent ran (the case-guppi of Case 1031 and the ask-guppi of /pre-spec), and the notice said "didn't finish before the previous session ended"

## Root cause

a background agent does not outlive the process; its transcript and its files stand, and a SendMessage to it resumes it from its transcript, so the main agent checks its case file and note and resumes it with what is left

## History

- 2026-11-20 created · raw/2026-11-04/0807/ledger.md#L58
