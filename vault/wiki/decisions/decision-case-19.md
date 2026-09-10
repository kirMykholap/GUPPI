---
type: decision
case: "19"
status: current
targets:
  - {kind: create, category: rules, slug: rule-plan-mode}
  - {kind: create, category: estimates, slug: estimate-plan-mode-verified, ref: rule-plan-mode}
origin: raw/2026-09-09/ledger.md#case-19
sprint: migration
created: 2026-09-09
tags: [session, workflow]
---

## Then

```
create:
  slug: rule-plan-mode
  type: rule
  kind: MOC
  purpose: Prevents work being planned against stale or contradictory vault state
  children: [rule-case-protocol, rule-ask, rule-pretask-hook, rule-pretask, rule-spec-capture]   # after case 20
  tags: [session, workflow]
  estimate:
    slug: estimate-plan-mode-verified
    kind: QA
    criterion: a `create` for a page whose purpose the index already carries is flagged in the Case's `now` before ratification; the pre-task hook fires before the plan is written and the plan is still written
    method: `make test-plan-mode`, the pipeline over tests/test_spec.py and tests/test_pretask.py; the flagging is one live reading by hand
```

`## Purpose` страницы: purpose плюс одно предложение из черновика — «deciding to build
something that already exists, or ratifying decisions that conflict with each other or
with what is already there». `rule-case-protocol` не трогается: его `parent` перестаёт
висеть сам.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-19
