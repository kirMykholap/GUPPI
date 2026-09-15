---
type: decision
case: "167"
status: current
update: ["[[rule-case-protocol]]"]
supersedes: ["[[decision-case-157]]"]
origin: raw/2026-09-15/1448/ledger.md#case-167
sprint: migration
created: 2026-09-15
tags: [session, workflow, ledger]
---

## Context

The reply that acknowledges a ratification has four parts in a fixed order (157): the heading `## Case N — ratified` with a **Changes** paragraph, a **Notes** paragraph, the heading `## Frontier` with the checklist and the question, and the `LEDGER` block last. The `Stop` hook reads the whole text of the reply and takes the record lines from any fenced block tagged `LEDGER`, wherever it stands; its one demand is that no tool call follows the text (122). The place of the block in the text does not matter to the hook: "last" was a choice of form in 157, not a technical need. For the reader the block at the bottom sits after the question "which item is next", so the record comes after the conversation.

## Problem

The order of the parts: the record block at the bottom, after the question, or at the top, before the account of the changes.

## Given

`rule-case-protocol` (`draft`, `render` → `CLAUDE.md`, `estimates: [estimate-case-protocol-loaded]`; blocks 157 and 159 read `passed` today): the paragraph "The reply that acknowledges a ratification has four parts…" ends "the `LEDGER` block, last".
**＋** `guppi/ledger.py`: the record lines are taken from a fenced block tagged `LEDGER` anywhere in the text; `last_assistant_message` and the transcript of the window are read.
**＋** `rule-ledger-write` (122): the text before a tool call is never kept; a reply with a block ends in text — a block at the top does not break this.
**－** `rule-ledger-write`, `guppi gate`, the form of a Case (159) and the short form of a defer do not change.

## Criterion

- [[estimate-case-protocol-loaded]] § case 167

## History

- 2026-09-15 created · raw/2026-09-15/1448/ledger.md#case-167
