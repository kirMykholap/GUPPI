---
type: estimate
kind: QA
status: pending
target: "[[rule-plugin-install]]"
purpose: Whether /guppi:install, where uv is missing, asks to install uv by its standalone installer, stops with nothing written on a no, and on a yes goes on once uv --version passes or sends the person to a new terminal
method: "by hand, after the librarian's run of the session that sets this Criterion, with a tag prod-x.y.z in the history of HEAD: the clean version written into a local folder by uv run --project .guppi guppi ship --allow-draft, that folder added as a catalogue by /plugin marketplace add and guppi installed from it by /plugin install guppi@guppi-marketplace; in an empty project with Claude Code started from a terminal whose PATH holds no folder of uv, /guppi:install typed and the offer answered no, then /guppi:install typed again and the offer answered yes; the replies, the files of the project and uv --version in a new terminal read against the Criterion"
origin: raw/2026-10-16/0342/ledger.md#case-852.1
sprint: plugin
created: 2026-10-16
tags: [plugin, harness]
---

## Criterion

When:
The person types `/guppi:install` of `plugin/skills/install/SKILL.md` in an empty project open in Claude Code, where `uv --version` fails.

Then:
Before it writes anything, the agent says that GUPPI needs the tool `uv` and asks the person whether it installs `uv` now by the standalone installer of `uv` for the system: a PowerShell command on Windows, a shell command on macOS and Linux.
**＋** On the person's no, it shows that command, says that the person installs `uv` with it and types `/guppi:install` again, and stops.
**＋** On the person's yes, it runs that command, and then `uv --version` again.
**＋** When `uv --version` then passes, it goes on with the install in the same session, and its last message tells the person to start Claude Code in the project from a new terminal and type `/hi`.
**＋** When `uv --version` still fails, it says that this session of Claude Code does not find the new `uv`, and that the person opens a new terminal, starts Claude Code there and types `/guppi:install` again, and stops.
**－** When the installer fails or Claude Code does not run it, the agent shows its output and the command, says that the person installs `uv` with it and types `/guppi:install` again, and stops.
**－** It writes nothing into the project before `uv --version` passes.

## History

- 2026-10-16 created · [[decision-case-852.1]]
