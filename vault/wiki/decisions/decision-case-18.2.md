---
type: decision
case: "18.2"
status: current
kind: [create, create, update]
target_slug: [rule-hook-registry, estimate-hook-registry-rendered, rule-session-start]
origin: raw/2026-09-09/ledger.md#case-18.2
sprint: migration
created: 2026-09-09
tags: [hooks, harness, render, session, workflow]
---

## When

```
create:
  slug: rule-hook-registry
  type: rule
  kind: Leaf
  purpose: Prevents a hook from being registered by hand, outside a ratified decision
  enforcement: render
  governs: .claude/settings.json
  render_mode: full
  parent: rule-session-start         # temporary; moves under a harness MOC when one exists
  tags: [hooks, harness, render]
  estimate:
    slug: estimate-hook-registry-rendered
    kind: QA
    criterion: `uv run guppi render` leaves .claude/settings.json byte-identical to the ratified Render body (git diff empty after the two hook additions of cases 20 and 24.1 are applied by hand once), the file parses as JSON, and the next session start still writes a session-start line into event_log.md
    method: the JSON case in tests/test_render.py; the live reading once by hand
update:
  slug: rule-session-start
  change: children → [rule-skill-hi, rule-event-log, rule-ledger-write, rule-hook-registry]; ## Children gets the fourth line; one sentence in How it works — the registry comes last because it records the registration of children 2–3, it is not a step of the session
```

Render body (final, after cases 20 and 24.1):

```json
{
  "permissions": {
    "defaultMode": "plan"
  },
  "hooks": {
    "SessionStart": [
      { "hooks": [ { "type": "command", "command": "uv run guppi event session-start", "timeout": 30 } ] }
    ],
    "PreToolUse": [
      { "matcher": "ExitPlanMode",
        "hooks": [ { "type": "command", "command": "uv run guppi pretask", "timeout": 30 } ] }
    ],
    "PostToolUse": [
      { "hooks": [ { "type": "command", "command": "uv run guppi event tool", "timeout": 30 } ] },
      { "matcher": "ExitPlanMode",
        "hooks": [ { "type": "command", "command": "uv run guppi spec", "timeout": 30 } ] }
    ],
    "Stop": [
      { "hooks": [ { "type": "command", "command": "uv run guppi ledger", "timeout": 30 } ] }
    ]
  }
}
```

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-18.2
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
