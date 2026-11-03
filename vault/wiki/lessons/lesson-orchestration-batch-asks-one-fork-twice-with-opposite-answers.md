---
type: lesson
kind: error
root_cause: Cases built at the same time read no file of each other until the second pass, so a fork that both Cases touch is asked by each with its own recommendation, and the main agent showed the two questions side by side without merging them into one
status: clustered
insight: "[[insight-case-build-sibling-texts-unchecked-before-the-showing]]"
origin: raw/2026-11-03/0316/ledger.md#L33
sprint: plugin
created: 2026-11-03
tags: [orchestration, case-build]
---

## Trigger

in the batch of Cases 1017 and 1018 both case-guppi asked who proposes the sprint id, 1017.Q12 recommending the main agent and 1018.Q4 the opening Case, and the person's "agree with the rest" took both opposite recommendations, so the fork was asked a third time

## Root cause

Cases built at the same time read no file of each other until the second pass, so a fork that both Cases touch is asked by each with its own recommendation, and the main agent showed the two questions side by side without merging them into one

## History

- 2026-11-03 created · raw/2026-11-03/0316/ledger.md#L33
- 2026-11-03 updated: clustered under insight-case-build-sibling-texts-unchecked-before-the-showing (synthesis) · raw/2026-11-03/0316/ledger.md#L33
