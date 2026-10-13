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

Prevents a hook from being registered by hand, outside a ratified decision. A hook is a script that Claude Code runs when an event of the session fires, such as `Stop` or `PreToolUse`; the Rule page behind it names the script in `implementation_ref`. A hook
Rule names `.claude/settings.json` in `implementation_ref`, but nothing ties the
file to the pages: a registration added or dropped by hand changes what fires with
no ledger line behind it. This page is the `"hooks"` key of that file; adding a
hook is an `update` of this page in the same Case that creates the hook's Rule.

`parent: rule-settings`: the file is one text of several rules, and the registry is
one of them (case 85.3). A hook in an agent's own frontmatter is part of that
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
- 2026-09-21 updated: guppi recall registered on SessionStart with the matcher compact (case 287) · [[decision-case-287]]
- 2026-09-24 updated: guppi ratified registered on Stop beside guppi ledger (case 387.2) · [[decision-case-387.2]]
- 2026-09-24 updated: guppi ratified --edit registered on PostToolUse of Edit, Write and MultiEdit (case 387.3) · [[decision-case-387.3]]
- 2026-09-24 updated: the Stop hook guppi context registered (case 392.1) · [[decision-case-392.1]]
- 2026-09-24 updated: the UserPromptSubmit hook guppi context --prompt registered (case 392.2) · [[decision-case-392.2]]
- 2026-09-24 status: built → draft · cascade
- 2026-09-25 updated: guppi casecheck --subagent registered on SubagentStop (case 419.3) · [[decision-case-419.3]]
- 2026-09-25 updated: guppi casecheck registered on Stop (case 419.4) · [[decision-case-419.4]]
- 2026-09-25 updated: guppi pageread registered on PreToolUse and PostToolUse of Read (case 420.1) · [[decision-case-420.1]]
- 2026-09-25 status: draft → built · cascade
- 2026-09-27 updated: guppi ratified --guard registered on PreToolUse of Edit, Write and MultiEdit; guppi ratified --edit removed from PostToolUse (case 445.1) · [[decision-case-445.1]]
- 2026-09-30 updated: the Purpose says what a hook is (case 527.1) · [[decision-case-527.1]]
- 2026-09-30 updated: the Stop hook guppi onward of rule-retro-onward registered after guppi context (case 531.9) · [[decision-case-531.9]]
- 2026-09-30 updated: the Purpose no longer counts the rules that share .claude/settings.json; rule-python-utf8 joined them · [[decision-case-534.1]]
- 2026-10-01 updated: guppi onward --plan registered on Stop after guppi onward (case 561.5) · [[decision-case-561.5]]
- 2026-10-05 updated: the hook grepguard registered on PreToolUse of Grep (case 664.1) · [[decision-case-664.1]]
- 2026-10-07 updated: uv run guppi casecheck --prompt registered on UserPromptSubmit (case 699.1) · [[decision-case-699.1]]
- 2026-10-07 updated: guppi shellwrite registered on PostToolUse of Bash and PowerShell (case 710.1) · [[decision-case-710.1]]
- 2026-10-09 updated: UserPromptSubmit runs guppi sprint --hi, which tells the agent at /hi to start /sprint-open when the sprint is closed (case 743.7) · [[decision-case-743.7]]
- 2026-10-13 updated: guppi powershellguard registered on PreToolUse of PowerShell (case 796.2) · [[decision-case-796.2]]
