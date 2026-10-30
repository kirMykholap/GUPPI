---
type: estimate
kind: QA
status: pending
target: "[[rule-plugin-install]]"
purpose: Whether /guppi:install moves each file of the project at a path of the install that is CLAUDE.md, a file under .claude/, .gitattributes or .github/workflows/checks.yml into guppi-set-aside/ with .set-aside added, the settings file only after uv sync passes, lists them in its last message, puts them back when uv sync fails, and stops on a clash at any other path
method: "by hand, after the librarian's run of the session that sets this Criterion, with a tag prod-x.y.z in the history of HEAD: the clean version written into a local folder by uv run --project .guppi guppi ship --allow-draft, that folder added as a catalogue by /plugin marketplace add and guppi installed from it by /plugin install guppi@guppi-marketplace; in a project that holds a CLAUDE.md, a .claude/settings.json with a hook and a .gitattributes of its own, /guppi:install typed; in a second such project with Claude Code started from a terminal with UV_OFFLINE=1 and UV_CACHE_DIR set to an empty folder, /guppi:install typed; in a third project with a file under vault/ of its own, /guppi:install typed; the transcripts and the files of the three projects before and after read against the Criterion"
origin: raw/2026-10-30/1713/ledger.md#case-932.1
sprint: plugin
created: 2026-10-30
tags: [plugin, harness]
---

## Criterion

When:
The person types `/guppi:install` of `plugin/skills/install/SKILL.md` in a project open in Claude Code, where `uv --version` passes, that holds a `CLAUDE.md`, a `.claude/settings.json` and a `.gitattributes` of its own and no other file of the install.

Then:
Before it copies, the agent moves each file of the project at a path of the install that is `CLAUDE.md`, a file under `.claude/` but `.claude/settings.json`, `.gitattributes` or `.github/workflows/checks.yml` into `guppi-set-aside/`, under its old path with `.set-aside` added to its name.
**＋** It moves the `.claude/settings.json` of the project into `guppi-set-aside/` the same way only after `uv sync` passes, just before it copies the `.claude/settings.json` of GUPPI.
**＋** Its last message lists each file it set aside with its path under `guppi-set-aside/`, and says that none of them loads or runs until the person keeps or drops it at the first `/hi`.
**＋** When `uv sync` fails, it deletes what it copied, moves each file it set aside back to its old path and deletes `guppi-set-aside/`, so that the project holds only what it held before.
**－** It changes no text of a file it sets aside, and sets aside no file at a path that the install does not write.
**－** In a project that holds a file of the install at any other path, or that already holds `guppi-set-aside/`, it lists them, writes and moves nothing, and stops.
**－** It writes nothing into the folder of the plugin, and runs no `guppi` command and no `git` command.

## History

- 2026-10-30 created · [[decision-case-932.1]]
