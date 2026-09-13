---
type: lesson
kind: error
root_cause: not yet found; the read-back of case 55.2 was measured on an earlier reply's block, and a block in an intermediate message of one turn seems not to be among the texts transcript_texts collects, or is filtered as not the main agent's; to be read in guppi/ledger.py against the transcript of this session before a fix is proposed
status: archived
insight: insight-ledger-hook-reads-only-the-final-text
origin: raw/2026-09-12/ledger.md#L101
sprint: migration
created: 2026-09-12
tags: [ledger, hooks, harness]
---

## Trigger

the LEDGER blocks of cases 59.1, 59.2, 59.4, 60, 63, 64, 65 and 66 never reached the ledger, while those of 58, 59.3, 59.5–59.8, 61 and 62 did; every lost block sat in a text message followed by tool calls in the same turn, every written one in the turn's last message

## Root cause

not yet found; the read-back of case 55.2 was measured on an earlier reply's block, and a block in an intermediate message of one turn seems not to be among the texts transcript_texts collects, or is filtered as not the main agent's; to be read in guppi/ledger.py against the transcript of this session before a fix is proposed

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#L101
- 2026-09-12 updated: clustered by librarian: the writer reads only the last text of a turn, with lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call · raw/2026-09-12/ledger.md#L101
- 2026-09-12 deleted · [[decision-case-70]]
- 2026-09-12 archived · cleanup
