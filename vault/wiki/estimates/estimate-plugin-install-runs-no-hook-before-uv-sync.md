---
type: estimate
kind: QA
status: passed
target: "[[rule-plugin-install]]"
purpose: Whether /guppi:install copies .claude/settings.json only after uv sync passes, so that no hook of the copied project builds .guppi/.venv before uv sync or fails after a rollback
method: "by hand, after the librarian's run of the session that sets this Criterion, with a tag prod-x.y.z in the history of HEAD: the clean version written into a local folder by uv run --project .guppi guppi ship --allow-draft, that folder added as a catalogue by /plugin marketplace add and guppi installed from it by /plugin install guppi@guppi-marketplace; in an empty project where uv --version passes, /guppi:install typed, and the output of uv sync and the time .guppi/.venv was made read; in a second empty project with Claude Code started from a terminal with UV_OFFLINE=1 and UV_CACHE_DIR set to an empty folder, /guppi:install typed and a command run after its rollback; the transcripts and the files of both projects read against the Criterion"
checked: 2026-10-30
origin: raw/2026-10-29/1930/ledger.md#case-912.1
sprint: plugin
created: 2026-10-29
tags: [plugin, hooks]
---

## Criterion

When:
The person types `/guppi:install` of `plugin/skills/install/SKILL.md` in an empty project open in Claude Code, where `uv --version` passes.

Then:
Until `uv sync --project .guppi` passes, the project holds no `.claude/settings.json`, so no hook of the copy runs.
**＋** No hook of the copy has made `.guppi/.venv/` by the time `uv sync` runs.
**＋** When `uv sync` fails, the project never holds `.claude/settings.json`, and no later command of that session shows a hook error.
**－** In a project that already holds `.claude/settings.json` or another file of the install, the agent still lists them, writes nothing and stops.

## Result

2026-10-30, at the /hi of session 0304, the person's answer on the two installs by hand from a clean copy: the project held no .claude/settings.json until uv sync passed, and no hook error showed after the rollback of the offline install; the − line of the Criterion, a project that already holds .claude/settings.json, was not read, since the method installs into empty projects only

## History

- 2026-10-29 created · [[decision-case-912.1]]
- 2026-10-30 status: pending → passed · raw/2026-10-30/0304/ledger.md#L2
