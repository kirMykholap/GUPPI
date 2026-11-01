---
type: lesson
kind: error
root_cause: the agent closed a backlog line by the Case built on its item, though the person chose in that Case that the defer of the page stays, and a Case closes a backlog line only when one of its decision lines names the page and retires its defer
status: clustered
insight: "[[insight-frontier-line-closed-by-the-case-built-on-its-item]]"
origin: raw/2026-11-01/1721/ledger.md#L34
sprint: plugin
created: 2026-11-01
tags: [orchestration, session]
---

## Trigger

in session 1721 the main agent closed the Frontier line C8 of the backlog item rule-ratification as [x] … · backlog · case 988, and the first run of guppi prespec --check printed two frontier findings: no decision line of Case 988 names rule-ratification and none carries {supersedes:case 907}; the agent closed the line [-] … · backlog · kept

## Root cause

the agent closed a backlog line by the Case built on its item, though the person chose in that Case that the defer of the page stays, and a Case closes a backlog line only when one of its decision lines names the page and retires its defer

## History

- 2026-11-01 created · raw/2026-11-01/1721/ledger.md#L34
- 2026-11-01 updated: clustered under insight-frontier-line-closed-by-the-case-built-on-its-item (synthesis) · raw/2026-11-01/1721/ledger.md#L34
