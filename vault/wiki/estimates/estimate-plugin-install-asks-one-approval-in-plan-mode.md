---
type: estimate
kind: QA
status: pending
target: "[[rule-plugin-install]]"
purpose: Whether /guppi:install, in a session that stands in Plan Mode, shows one plan of the files it copies and the files of the project it sets aside, with the installer of uv first where the person said yes to it, asks the approval once and names none of its options, writes nothing before it, and stops with nothing written when the person does not approve it
method: "by hand, after the librarian's run of the session that sets this Criterion: the clean version written into a local folder by uv run --project .guppi guppi ship --allow-draft, that folder added as a catalogue by /plugin marketplace add and guppi installed from it by /plugin install guppi@guppi-marketplace; in a project that holds a CLAUDE.md of its own, Claude Code started by claude --permission-mode plan and /guppi:install typed; in a second such project, Claude Code started the same way from a terminal whose PATH holds no folder of uv, /guppi:install typed and the offer of uv answered yes; in a third such project, /guppi:install typed and the plan not approved; the transcripts of the three sessions under ~/.claude/projects/ and the files of the three projects before and after read against the Criterion"
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

## History

- 2026-11-23 created · [[decision-case-1040]]
