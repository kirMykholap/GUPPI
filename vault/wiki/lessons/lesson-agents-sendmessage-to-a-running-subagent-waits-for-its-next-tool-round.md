---
type: lesson
kind: knowledge
root_cause: a SendMessage to a running subagent reaches it only at its next tool call, so a fact sent while it writes its final answer lands after that answer
status: new
source: transcript of session 6d53e05d, agent a7b182c9a1f27f641
origin: raw/2026-10-05/0311/ledger.md#L41
sprint: migration
created: 2026-10-05
tags: [workflow, session]
---

## Trigger

in the /pre-spec loop of session 0311 the main agent sent the case-guppi of Case 645 the split of 644 while it was building; the tool answered "queued for delivery at its next tool round", the agent made no further tool call and handed back 645 without the fix, and only a second message brought 645.5 in line.

## Root cause

a SendMessage to a running subagent reaches it only at its next tool call, so a fact sent while it writes its final answer lands after that answer

## History

- 2026-10-05 created · raw/2026-10-05/0311/ledger.md#L41
