---
type: rule
kind: Leaf
purpose: Prevents a hook from being registered by hand, outside a ratified decision
status: built
enforcement: render
governs: .claude/settings.json
render_mode: partial
parent: "[[rule-settings]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [hooks, harness, render]
core: true
---

## Purpose

Prevents a hook from being registered by hand, outside a ratified decision. A hook is a script that Claude Code runs when an event of the session fires, such as `Stop` or `PreToolUse`; the Rule page behind it names the script in `implementation_ref`. A hook
Rule names `.claude/settings.json` in `implementation_ref`, but nothing ties the
file to the pages: a registration added or dropped by hand changes what fires with
no ledger line behind it. This page is the `"hooks"` key of that file; adding a
hook is an `update` of this page in the same Case that creates the hook's Rule.

`parent: rule-settings`: the file is one text of several rules, and the registry is
one of them. A hook in an agent's own frontmatter is part of that
agent's Render and is ratified with it; this page holds the registrations only.

## Render

<!-- rule-hook-registry -->
    "SessionStart": [
      { "hooks": [ { "type": "command", "command": "uv run guppi event session-start", "timeout": 30 },
                   { "type": "command", "command": "uv run guppi render --sync", "timeout": 60 } ] },
      { "matcher": "compact",
        "hooks": [ { "type": "command", "command": "uv run guppi recall", "timeout": 30 } ] }
],
"UserPromptSubmit": [
  { "hooks": [ { "type": "command", "command": "uv run guppi event prompt", "timeout": 30 }, { "type": "command", "command": "uv run guppi context --prompt", "timeout": 30 }, { "type": "command", "command": "uv run guppi casecheck --prompt", "timeout": 30 }, { "type": "command", "command": "uv run guppi sprint --hi", "timeout": 30 },
               { "type": "command", "command": "uv run guppi gate", "timeout": 30 } ] }
],
"PreToolUse": [

      { "matcher": "ExitPlanMode",
        "hooks": [ { "type": "command", "command": "uv run guppi prespec", "timeout": 30 } ] },
      { "matcher": "Skill",
        "hooks": [ { "type": "command", "command": "uv run guppi gate", "timeout": 30 } ] },
      { "matcher": "Edit|Write|MultiEdit",
  "hooks": [ { "type": "command", "command": "uv run guppi guard", "timeout": 30 }, { "type": "command", "command": "uv run guppi ratified --guard", "timeout": 30 } ] },
{ "matcher": "Bash",
  "hooks": [ { "type": "command", "command": "uv run guppi bashguard", "timeout": 30 } ] },
{ "matcher": "PowerShell",
  "hooks": [ { "type": "command", "command": "uv run guppi powershellguard", "timeout": 30 } ] },
{ "matcher": "Read",
  "hooks": [ { "type": "command", "command": "uv run guppi pageread", "timeout": 30 } ] },
{ "matcher": "Grep",
  "hooks": [ { "type": "command", "command": "uv run guppi grepguard", "timeout": 30 } ] }

    ],
    "PostToolUse": [
      { "hooks": [ { "type": "command", "command": "uv run guppi event tool", "timeout": 30 } ] },
      { "matcher": "ExitPlanMode",
        "hooks": [ { "type": "command", "command": "uv run guppi spec", "timeout": 30 } ] }, { "matcher": "Read", "hooks": [ { "type": "command", "command": "uv run guppi pageread --after", "timeout": 30 } ] }, { "matcher": "Bash|PowerShell", "hooks": [ { "type": "command", "command": "uv run guppi shellwrite", "timeout": 30 } ] }
    ],
    "Stop": [
      { "hooks": [ { "type": "command", "command": "uv run guppi ledger", "timeout": 30 }, { "type": "command", "command": "uv run guppi ratified", "timeout": 30 }, { "type": "command", "command": "uv run guppi casecheck", "timeout": 30 }, { "type": "command", "command": "uv run guppi context", "timeout": 30 }, { "type": "command", "command": "uv run guppi onward", "timeout": 30 }, { "type": "command", "command": "uv run guppi onward --plan", "timeout": 30 } ] }
    ],
    "SubagentStop": [
      { "hooks": [ { "type": "command", "command": "uv run guppi casecheck --subagent", "timeout": 30 } ] }
    ]
<!-- /rule-hook-registry -->

## History

- 2026-10-14 shipped with GUPPI
