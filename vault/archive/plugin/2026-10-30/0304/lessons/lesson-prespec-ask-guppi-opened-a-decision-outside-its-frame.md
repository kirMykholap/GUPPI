---
type: lesson
kind: error
root_cause: a Grep whose path is a file under vault/wiki/decisions/ is left unchanged by the hook of case 664.1, so nothing but the agent's own judgment stops a read of a Decision page for a reason its frame does not name.
status: archived
insight: "[[insight-ask-guppi-reads-a-decision-outside-its-frame]]"
origin: raw/2026-10-28/1907/ledger.md#L22
sprint: plugin
created: 2026-10-28
tags: [prespec, harness]
---

## Trigger

the ask-guppi run of /pre-spec in session 1907 ran a Grep for ^## over vault/wiki/decisions/decision-case-882.3.md, a Decision no finding named, and reported it as a break of its frame and of .claude/rules/search-leaves-out-decisions.md.

## Root cause

a Grep whose path is a file under vault/wiki/decisions/ is left unchanged by the hook of case 664.1, so nothing but the agent's own judgment stops a read of a Decision page for a reason its frame does not name.

## History

- 2026-10-28 created · raw/2026-10-28/1907/ledger.md#L22
- 2026-10-28 updated: clustered under insight-ask-guppi-reads-a-decision-outside-its-frame (synthesis) · raw/2026-10-28/1907/ledger.md#L22
- 2026-10-30 archived · insight actioned
- 2026-10-30 archived · cleanup
