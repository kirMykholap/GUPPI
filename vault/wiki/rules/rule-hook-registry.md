---
type: rule
kind: Leaf
purpose: Prevents a hook from being registered by hand, outside a ratified decision
status: built
enforcement: render
governs: .claude/settings.json
render_mode: full
parent: rule-harness
estimates: [estimate-hook-registry-rendered]
origin: raw/2026-09-09/ledger.md#case-18.2
sprint: migration
created: 2026-09-09
tags: [hooks, harness, render]
---

## Purpose

Prevents a hook from being registered by hand, outside a ratified decision. A hook Rule
names `.claude/settings.json` in `implementation_ref`, but nothing ties the file to the
pages: a registration added or dropped by hand changes what fires with no ledger line
behind it. The Render body is the file; adding a hook is an `update` of this page in the
same Case that creates the hook's Rule. `defaultMode: plan` lives here too: it is harness
configuration, and one file has one source.

`parent: rule-harness`: the registry holds the hooks of every phase, so it sits with the tools of the harness, in no phase. A hook in an agent's own frontmatter is part of that agent's Render and is ratified with it; this registry holds `settings.json` only.

## Render

<!-- rule-hook-registry -->
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
        "hooks": [ { "type": "command", "command": "uv run guppi pretask", "timeout": 30 } ] },
      { "matcher": "Skill",
        "hooks": [ { "type": "command", "command": "uv run guppi gate", "timeout": 30 } ] }
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
<!-- /rule-hook-registry -->

## Estimates

- [[estimate-hook-registry-rendered]]

## Parent

- [[rule-session-start]]

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-18.2
- 2026-09-09 updated: PostToolUse ExitPlanMode → guppi spec · raw/2026-09-09/ledger.md#case-20
- 2026-09-09 updated: PreToolUse ExitPlanMode → guppi pretask · raw/2026-09-09/ledger.md#case-24.1
- 2026-09-10 updated: parent is rule-harness · raw/2026-09-10/ledger.md#case-37
- 2026-09-10 updated: PreToolUse, matcher Skill → uv run guppi gate · raw/2026-09-10/ledger.md#case-38.2
- 2026-09-10 status: draft → built · cascade
