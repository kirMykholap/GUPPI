---
type: decision
case: "19"
status: current
create: ["[[rule-plan-mode]]", "[[estimate-plan-mode-verified]]"]
origin: raw/2026-09-09/ledger.md#case-19
sprint: migration
created: 2026-09-09
tags: [session, workflow]
---

## When

```
create:
  slug: rule-plan-mode
  type: rule
  kind: MOC
  purpose: Prevents work being planned against stale or contradictory vault state
  children: [rule-case-protocol, rule-ask, rule-prespec-hook, rule-prespec, rule-spec-capture]   # after case 20
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
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
