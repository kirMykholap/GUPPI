---
type: estimate
kind: QA
status: pending
target: "[[rule-plugin-install]]"
purpose: Whether guppi ship puts the skill install into the clean version, and whether /guppi:install copies every file of the plugin but its own into a project that holds none of them
method: "uv run --project .guppi pytest .guppi/tests/test_ship.py -k plugin_skill; by hand, after the librarian's run of the session that sets this Criterion, with a tag prod-x.y.z in the history of HEAD: the clean version written into a local folder by uv run --project .guppi guppi ship --allow-draft; in an empty project, that folder added as a catalogue by /plugin marketplace add, guppi installed by /plugin install guppi@guppi-marketplace, /guppi:install typed and the files of the project read against those of the plugin and against the Criterion"
checked: 2026-10-16
origin: raw/2026-10-15/0553/ledger.md#case-818.1
sprint: plugin
created: 2026-10-15
tags: [plugin, harness]
---

## Criterion

When:
`uv run --project .guppi guppi ship --allow-draft <folder>` builds the clean version, as `rule-clean-branch` sets it, and `uv run --project .guppi guppi ship --check` judges the working tree.
**＋** The person writes the clean version into a local folder by `uv run --project .guppi guppi ship --allow-draft <folder>`, adds that folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` in the project open in Claude Code, as `rule-plugin-install` sets it.

Then:
`uv run --project .guppi guppi ship --allow-draft <folder>` writes `plugin/skills/install/SKILL.md` to `skills/install/SKILL.md` of the clean version and cleans it like each other file it writes, and the clean version holds no file under `plugin/skills/`.
**＋** `uv run --project .guppi guppi ship --check` judges `plugin/skills/install/SKILL.md` in place, as it judges each other file outside `vault/`.
**＋** The installed plugin offers the skill `install`, which the person types as `/guppi:install`.
**＋** In a project that holds none of the files it would write, `/guppi:install` copies each file of the plugin to the same path in the project, but those under `.claude-plugin/`, `skills/` and `.git/`, such as `CLAUDE.md`, `.claude/settings.json`, the code under `.guppi/` and the pages under `vault/wiki/`.
**＋** It checks that each copied file stands, and its last message tells the person to reopen Claude Code in the project and type `/hi`.
**－** It writes nothing into the folder of the plugin, and runs no `guppi` command and no `git` command.
**－** The skills it copies under `.claude/skills/` keep their bare names, such as `hi`.
**－** Which files a new project needs, what the install does about `uv` and the Python environment under `.guppi/`, and what it does with a file of the project that stands at one of its paths are no part of this promise.

## Result

2026-10-16, Retro of session 0104, tag prod-0.2.0 local: test_ship.py -k plugin_skill 2 passed; guppi ship --allow-draft into scratchpad/ship-plugin wrote skills/install/SKILL.md and no folder plugin/; guppi ship --check printed nothing, exit 0; in C:\PROJECTS\test /guppi:install copied every file of the copy but .claude-plugin/plugin.json, .claude-plugin/marketplace.json and skills/install/SKILL.md, none differing, .claude/skills/ holding hi, work and the other bare names; in C:\PROJECTS\test-claude-md, which held its own CLAUDE.md, it named CLAUDE.md, wrote nothing and stopped; the copy unchanged after the installs

## History

- 2026-10-15 created · [[decision-case-818.1]]
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 status: pending → failed · raw/2026-10-15/1739/ledger.md#L13
- 2026-10-15 deferred · [[decision-case-831]]
- 2026-10-16 defer by decision-case-831 superseded · [[decision-case-843]]
- 2026-10-16 updated: set to pending with its Criterion unchanged, for a reading once a tag prod-x.y.z stands · [[decision-case-843]]
- 2026-10-16 status: pending → passed · raw/2026-10-16/0104/ledger.md#L16
- 2026-10-30 updated: the Criterion replaced whole — the refusal of a project that holds a file of the install leaves it, since the install now sets such files aside · [[decision-case-932.3]]
