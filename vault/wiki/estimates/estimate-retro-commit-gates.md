---
type: estimate
kind: QA
status: pending
target: rule-retro-commit
origin: raw/2026-09-10/ledger.md#case-38.2
sprint: migration
created: 2026-09-10
tags: [session, workflow, hooks, harness, git]
---

## Context

Without the gate, session work and librarian work land in one undifferentiated diff.

## Criterion

Given a PreToolUse payload naming the Skill tool with skill handoff: with a dirty
tree, exit 2 with a reason naming commit first; with a clean tree, exit 0; another
skill or another tool, exit 0 whatever the tree. Live: the first /handoff called
from Retro on a dirty tree is refused, and passes after the commit.

## Method

pytest in tests/test_gate.py with piped payloads against a temp repository; the live reading once by hand

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.2
