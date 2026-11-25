---
type: estimate
kind: QA
status: passed
target: "[[rule-plugin-install]]"
purpose: Whether /guppi:install moves each file of the project at a path of the install that is CLAUDE.md, a file under .claude/, .gitattributes or .github/workflows/checks.yml into guppi-set-aside/ with .set-aside added, the settings file only after uv sync passes, lists them in its last message, puts them back when uv sync fails, and stops on a clash at any other path
method: "by hand, after the install stop of the Work Mode that sets this method: with a tag prod-x.y.z in the history of HEAD, the clean version written into a local folder by uv run --project .guppi guppi ship --allow-draft, that folder added as a catalogue by /plugin marketplace add and guppi installed from it by /plugin install guppi@guppi-marketplace; in a project that holds a CLAUDE.md, a .claude/settings.json with a hook and a .gitattributes of its own, /guppi:install typed; in a second such project with Claude Code started from a terminal with UV_OFFLINE=1 and UV_CACHE_DIR set to an empty folder, /guppi:install typed; in a third project with a vault/wiki/glossary.md of its own, a path the install writes, /guppi:install typed; the transcripts and the files of the three projects before and after read against the Criterion, recorded in the estimate line"
checked: 2026-11-25
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

## Result

2026-11-25, Retro of session 0816, the install stop of its Work Mode: p3-set-aside (f3e37d51-edd1-439e-902b-6bbd61910e9e.jsonl) moved CLAUDE.md and .gitattributes into guppi-set-aside/ with .set-aside before the copy, and .claude/settings.json only after uv sync passed, just before the copy of GUPPI's; its last message listed the three paths and said none loads or runs until the first /hi; p4-offline (df6d0509-3c19-408f-9da5-ec63bf1dd2e5.jsonl, UV_OFFLINE=1, an empty UV_CACHE_DIR) set aside two files, copied, uv sync failed on ruff==0.16.1, it deleted what it copied, moved both back and deleted guppi-set-aside/, and the folder holds the three files again, byte-equal by cmp to the set-aside copies of p3; p5-clash (3d47a486-481b-45f0-b077-40719bccc4b2.jsonl) listed vault/wiki/glossary.md, made no plan, wrote and moved nothing, and the folder holds that one file; no text of a set-aside file changed, and no guppi or git command ran

## History

- 2026-10-30 created · [[decision-case-932.1]]
- 2026-10-31 deferred · [[decision-case-949]]
- 2026-11-25 defer by decision-case-949 superseded · [[decision-case-1055.5]]
- 2026-11-25 updated: the put-off retired before it was applied; the reading taken at the install stop of Work Mode · [[decision-case-1055.5]]
- 2026-11-25 status: pending → passed · raw/2026-11-25/0816/ledger.md#L29
