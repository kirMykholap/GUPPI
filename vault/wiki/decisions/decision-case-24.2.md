---
type: decision
case: "24.2"
status: superseded
targets:
  - {kind: create, category: rules, slug: rule-pretask, ref: rule-plan-mode}
  - {kind: create, category: estimates, slug: estimate-pretask-reconciles, ref: rule-pretask}
superseded_by: [decision-case-26.1]
origin: raw/2026-09-09/ledger.md#case-24.2
sprint: migration
created: 2026-09-09
tags: [session, workflow, harness]
---

## Then

```
create:
  slug: rule-pretask
  type: rule
  kind: Leaf
  purpose: Prevents a set of ratified decisions from reaching the Spec with a contradiction between them or with the vault
  enforcement: render
  governs: .claude/skills/pre-task/SKILL.md
  render_mode: full
  parent: rule-plan-mode
  tags: [session, workflow, harness]
  estimate:
    slug: estimate-pretask-reconciles
    kind: QA
    criterion: one live run before a plan approval — the event log gains a `pretask` line, the ask-guppi agent is dispatched once with the list of this Plan Mode's decisions, and every finding it returns is either raised as a Case or named as already known in the reply
    method: one reading by hand — the exception the Method rule allows
```

Текст рендера:

```markdown
---
name: pre-task
description: Check this Plan Mode's ratified decisions against each other and the vault before the Spec is approved.
---
Recorded: !`uv run guppi event pretask --session "${CLAUDE_SESSION_ID:-}"`

List every decision ratified in this Plan Mode, one line each: slug — decision type —
purpose. Dispatch the `ask-guppi` agent once with that list and the question: which of
these contradict a page of the vault, a rule of `index.md`, or each other. Raise each
finding as a Case, or say in one line why it is already known. Then exit Plan Mode again.
```

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-24.2
- 2026-09-09 superseded by decision-case-26.1 · raw/2026-09-09/ledger.md#case-26.1
