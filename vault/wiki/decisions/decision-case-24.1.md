---
type: decision
case: "24.1"
status: current
targets:
  - {kind: create, category: rules, slug: rule-pretask-hook, ref: rule-plan-mode}
  - {kind: create, category: estimates, slug: estimate-pretask-hook-gates, ref: rule-pretask-hook}
  - {kind: update, category: rules, slug: rule-hook-registry}
origin: raw/2026-09-09/ledger.md#case-24.1
sprint: migration
created: 2026-09-09
tags: [session, workflow, hooks, harness, render]
---

## Then

```
create:
  slug: rule-pretask-hook
  type: rule
  kind: Leaf
  purpose: Prevents a Spec from being approved before its decisions were checked against each other and the vault
  enforcement: hook
  implementation_ref: [guppi/pretask.py, .claude/settings.json]
  parent: rule-plan-mode
  tags: [session, workflow, hooks, harness]
  estimate:
    slug: estimate-pretask-hook-gates
    kind: QA
    criterion: given a PreToolUse payload naming ExitPlanMode — with no `pretask` line after this session's `hi` in the event log, exit 2 with a reason naming /pre-task and the session; with the line, exit 0; any other tool, exit 0; the live approval of the next plan passes only after /pre-task ran
    method: pytest in tests/test_pretask.py with piped payloads against a temp event log; the live reading once by hand
update:
  slug: rule-hook-registry
  change: PreToolUse, matcher ExitPlanMode → `uv run guppi pretask`
```

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-24.1
