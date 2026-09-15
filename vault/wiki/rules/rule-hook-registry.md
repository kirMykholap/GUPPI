---
type: rule
kind: Leaf
purpose: Prevents a hook from being registered by hand, outside a ratified decision
status: built
enforcement: render
governs: .claude/settings.json
render_mode: partial
parent: "[[rule-settings]]"
estimates: ["[[estimate-hook-registry-rendered]]"]
origin: raw/2026-09-09/ledger.md#case-18.2
sprint: migration
created: 2026-09-09
tags: [hooks, harness, render]
---

## Purpose

Prevents a hook from being registered by hand, outside a ratified decision. A hook
Rule names `.claude/settings.json` in `implementation_ref`, but nothing ties the
file to the pages: a registration added or dropped by hand changes what fires with
no ledger line behind it. This page is the `"hooks"` key of that file; adding a
hook is an `update` of this page in the same Case that creates the hook's Rule.

`parent: rule-settings`: the file is one text of three rules, and the registry is
one of them (case 85.3). A hook in an agent's own frontmatter is part of that
agent's Render and is ratified with it; this page holds the registrations only.

## Render

<!-- rule-hook-registry -->
    "SessionStart": [
      { "hooks": [ { "type": "command", "command": "uv run guppi event session-start", "timeout": 30 },
                   { "type": "command", "command": "uv run guppi render --sync", "timeout": 60 } ] }
],
"UserPromptSubmit": [
  { "hooks": [ { "type": "command", "command": "uv run guppi event prompt", "timeout": 30 },
               { "type": "command", "command": "uv run guppi gate", "timeout": 30 } ] }
],
"PreToolUse": [

      { "matcher": "ExitPlanMode",
        "hooks": [ { "type": "command", "command": "uv run guppi pretask", "timeout": 30 } ] },
      { "matcher": "Skill",
        "hooks": [ { "type": "command", "command": "uv run guppi gate", "timeout": 30 } ] },
      { "matcher": "Edit|Write|MultiEdit",
  "hooks": [ { "type": "command", "command": "uv run guppi guard", "timeout": 30 } ] },
{ "matcher": "Bash",
  "hooks": [ { "type": "command", "command": "uv run guppi bashguard", "timeout": 30 } ] }

    ],
    "PostToolUse": [
      { "hooks": [ { "type": "command", "command": "uv run guppi event tool", "timeout": 30 } ] },
      { "matcher": "ExitPlanMode",
        "hooks": [ { "type": "command", "command": "uv run guppi spec", "timeout": 30 } ] }
    ],
    "Stop": [
      { "hooks": [ { "type": "command", "command": "uv run guppi ledger", "timeout": 30 } ] }
    ]
<!-- /rule-hook-registry -->

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-18.2
- 2026-09-09 updated: PostToolUse ExitPlanMode → guppi spec · raw/2026-09-09/ledger.md#case-20
- 2026-09-09 updated: PreToolUse ExitPlanMode → guppi pretask · raw/2026-09-09/ledger.md#case-24.1
- 2026-09-10 updated: parent is rule-harness · raw/2026-09-10/ledger.md#case-37
- 2026-09-10 updated: PreToolUse, matcher Skill → uv run guppi gate · raw/2026-09-10/ledger.md#case-38.2
- 2026-09-10 status: draft → built · cascade
- 2026-09-12 updated: guppi guard registered on PreToolUse of Edit, Write and MultiEdit (case 59.6) · [[decision-case-59.6]]
- 2026-09-12 updated: guppi render --sync registered as the second SessionStart hook (case 59.7) · [[decision-case-59.7]]
- 2026-09-12 updated: the page renders the hooks key only, as a partial child of rule-settings (case 85.3) · [[decision-case-85.3]]
- 2026-09-12 status: built → draft · cascade
- 2026-09-13 status: draft → built · cascade
- 2026-09-14 updated: guppi event prompt registered on UserPromptSubmit (case 111.2) · [[decision-case-111.2]]
- 2026-09-14 updated: a PreToolUse hook on Bash, guppi bashguard, against the heredoc trap (case 127) · [[decision-case-127]]
- 2026-09-15 updated: UserPromptSubmit runs guppi gate after guppi event prompt (case 169.2) · [[decision-case-169.2]]
- 2026-09-15 status: built → draft · cascade
- 2026-09-15 status: draft → built · cascade
