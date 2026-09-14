---
type: decision
case: "20"
status: current
create: ["[[rule-spec-capture]]", "[[estimate-spec-capture-appends]]"]
update: ["[[rule-plan-mode]]", "[[rule-hook-registry]]"]
origin: raw/2026-09-09/ledger.md#case-20
sprint: migration
created: 2026-09-09
tags: [session, hooks, harness, workflow, render]
---

## When

```
create:
  slug: rule-spec-capture
  type: rule
  kind: Leaf
  purpose: Prevents an approved Spec from existing only in Claude Code's plan file, outside the repository
  enforcement: hook
  implementation_ref: [guppi/spec.py, .claude/settings.json]
  parent: rule-plan-mode
  tags: [session, hooks, harness, workflow]
  estimate:
    slug: estimate-spec-capture-appends
    kind: QA
    criterion: given a PostToolUse payload naming ExitPlanMode with a plan and a `hi` recorded — spec.md gains a `---` separator (when the file has content), the stamp `<!-- approved HH:MM:SS · session xxxxxxxx -->` and the plan text, once, even when the hook runs twice; earlier documents stay intact. Without `hi` — exit 2 naming the session, file untouched. Another tool's payload — nothing written, exit 0. Live — the next plan approval lands in raw/<date>/spec.md by the hook, not by hand, and the reading records what a rejected plan produces
    method: pytest in tests/test_spec.py with piped payloads against a temp vault; the live reading once by hand
update:
  slug: rule-plan-mode
  change: children gain rule-spec-capture last
update:
  slug: rule-hook-registry
  change: PostToolUse, matcher ExitPlanMode → `uv run guppi spec`
```

`CLAUDE.md`, migration-абзац: «The approved plan is copied to `vault/raw/<date>/spec.md`»
→ «... copied by the `Stop`-side hook `guppi spec` since Slice 2».

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-20
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
