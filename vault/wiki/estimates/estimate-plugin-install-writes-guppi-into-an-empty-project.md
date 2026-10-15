---
type: estimate
kind: QA
status: failed
target: "[[rule-plugin-install]]"
purpose: Whether guppi ship puts the skill install into the clean version, and whether /guppi:install copies every file of the plugin but its own into a project that holds none of them, and writes nothing into one that holds one
method: "uv run --project .guppi pytest .guppi/tests/test_ship.py -k plugin_skill; by hand, after the Work Mode of this change: the clean version written into a local folder by uv run --project .guppi guppi ship --allow-draft; in an empty project, that folder added as a catalogue by /plugin marketplace add, guppi installed by /plugin install guppi@guppi-marketplace, /guppi:install typed and the files of the project read against those of the plugin; in a second empty project with a file CLAUDE.md of its own, /guppi:install typed and its output and the files of that project read against the Criterion"
checked: 2026-10-15
origin: raw/2026-10-15/0553/ledger.md#case-818.1
sprint: plugin
created: 2026-10-15
tags: [plugin, harness]
---

## Criterion

When:
`uv run --project .guppi guppi ship <folder>` builds the clean version, as `rule-clean-branch` sets it, and `uv run --project .guppi guppi ship --check` judges the working tree.
**＋** The person writes the clean version into a local folder by `uv run --project .guppi guppi ship --allow-draft <folder>`, adds that folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` in the project open in Claude Code, as `rule-plugin-install` sets it.

Then:
`uv run --project .guppi guppi ship <folder>` writes `plugin/skills/install/SKILL.md` to `skills/install/SKILL.md` of the clean version and cleans it like each other file it writes, and the clean version holds no file under `plugin/skills/`.
**＋** `uv run --project .guppi guppi ship --check` judges `plugin/skills/install/SKILL.md` in place, as it judges each other file outside `vault/`.
**＋** The installed plugin offers the skill `install`, which the person types as `/guppi:install`.
**＋** In a project that holds none of the files it would write, `/guppi:install` copies each file of the plugin to the same path in the project, but those under `.claude-plugin/`, `skills/` and `.git/`, such as `CLAUDE.md`, `.claude/settings.json`, the code under `.guppi/` and the pages under `vault/wiki/`.
**＋** It checks that each copied file stands, and its last message tells the person to reopen Claude Code in the project and type `/hi`.
**－** In a project where one or more of those files already stand, it lists them, writes nothing and stops.
**－** It writes nothing into the folder of the plugin, and runs no `guppi` command and no `git` command.
**－** The skills it copies under `.claude/skills/` keep their bare names, such as `hi`.
**－** Which files a new project needs, and what the install does about `uv` and the Python environment under `.guppi/`, are no part of this promise.

## Result

2026-10-15, Retro, not read: plugin/skills/install/SKILL.md is written only by the librarian's render of rule-plugin-install, and guppi ship --allow-draft exits 1 with no tag prod-x.y.z, so no local copy holds the skill install after the Work Mode

## History

- 2026-10-15 created · [[decision-case-818.1]]
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 status: pending → failed · raw/2026-10-15/1739/ledger.md#L13
