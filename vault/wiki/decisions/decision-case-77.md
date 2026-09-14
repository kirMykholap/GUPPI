---
type: decision
case: "77"
status: current
update: ["[[rule-claude-md]]"]
origin: raw/2026-09-12/ledger.md#case-77
sprint: migration
created: 2026-09-12
tags: [harness, render]
---

## Context

Case 59.8 wrote "How it works" of `rule-claude-md` before Case 66 moved
`rule-case-protocol` under it; the brief flags the sentence as stale.

## Problem

The section says "`rule-case-protocol` keeps its parent `rule-plan-mode`; it is listed
here for the renderer only", and the frontmatter of both pages says the opposite.

## Given

`rule-claude-md` `children: [rule-case-protocol]`; `rule-case-protocol` `parent:
rule-claude-md` (case 66). The sentence is the last of "How it works". 73.10 updates
the Render of the same page; different sentence.

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-77
