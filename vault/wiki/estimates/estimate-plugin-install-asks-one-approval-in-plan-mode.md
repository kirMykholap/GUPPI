---
type: estimate
kind: QA
status: passed
target: "[[rule-plugin-install]]"
purpose: Whether /guppi:install, in a session that stands in Plan Mode, shows one plan of the files it copies and the files of the project it sets aside, with the installer of uv first where the person said yes to it, asks the approval once and names none of its options, writes nothing before it, and stops with nothing written when the person does not approve it
method: "by hand, after the install stop of the Work Mode that sets this method: the clean version written into C:/tmp/guppi-1055/copy by uv run --project .guppi guppi ship --allow-draft, added as a catalogue by /plugin marketplace add and guppi installed from it by /plugin install guppi@guppi-marketplace; in a folder with no git that holds a CLAUDE.md and a code file of its own, Claude Code started by claude --permission-mode plan from a terminal whose PATH holds no folder of uv, /guppi:install typed, the offer of uv answered yes and the plan not approved, then /guppi:install typed again and the plan approved; the transcript of that session under ~/.claude/projects/ and the files of the folder before, between and after read against the Criterion, recorded in the estimate line"
checked: 2026-11-25
origin: raw/2026-11-20/1353/ledger.md#case-1040
sprint: plugin
created: 2026-11-20
tags: [plugin, harness]
---

## Criterion

When:
The person types `/guppi:install` of `plugin/skills/install/SKILL.md` in a project open in Claude Code whose session stands in Plan Mode, and the project holds a `CLAUDE.md` of its own and no other file of the install.

Then:
Before it writes or moves anything, the agent checks the paths of the install and shows a plan that lists each file it will copy and each file of the project it will set aside under `guppi-set-aside/`, `CLAUDE.md` among them.
**＋** The agent asks the person to approve that plan once, by the plan approval of Claude Code, and names none of its options.
**＋** Once the person approves it, the agent runs the install as `rule-plugin-install` sets it, with no second plan.
**＋** Where `uv --version` fails and the person says yes to installing `uv`, the installer of `uv` is the first item of that plan, and the agent runs it only after the approval.
**－** When the person does not approve the plan, the agent writes and moves nothing in the project and stops.

## Result

2026-11-25, Retro of session 0816, the install stop of its Work Mode, the copy C:/tmp/guppi-1055/copy from guppi ship --allow-draft (version 0.3.0 from the tag prod-0.3.0), ~/.claude/projects/C--tmp-guppi-1055-p1-code/66ad2c5f-8c5a-4bda-badd-8f13c00bfa47.jsonl, started by claude --permission-mode plan with no folder of uv on PATH: uv --version failed, the offer of uv was answered yes, the plan of ExitPlanMode put the uv installer first, listed the 519 files to copy and CLAUDE.md and .claude/settings.json to set aside, and was refused, after which the folder held only app.py, CLAUDE.md and .claude/settings.json; the second /guppi:install gave one plan, approved by the plan approval, no option named, and the installer ran only after it, then the copy, uv sync and the set-aside with no second plan; the folder held one more path of the install than the When names, a .claude/settings.json of enabledPlugins that /plugin install wrote, which the plan listed and set aside

## History

- 2026-11-23 created · [[decision-case-1040]]
- 2026-11-25 updated: the method set anew — one project with no uv on its PATH takes the refused plan and then the approved one, at the install stop of Work Mode · [[decision-case-1055.1]]
- 2026-11-25 status: pending → passed · raw/2026-11-25/0816/ledger.md#L25
