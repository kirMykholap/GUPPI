---
type: estimate
kind: QA
status: pending
target: "[[rule-plugin-install]]"
purpose: Whether guppi ship puts the skill install into the clean version, and whether /guppi:install copies every file of the plugin but its own and the LICENSE at its root into a project that holds none of them, the LICENSE of the project left as it stands
method: "uv run --project .guppi pytest .guppi/tests/test_ship.py -k plugin_skill; by hand, after the librarian's run of the session that sets this Criterion: in a later session, with a tag prod-x.y.z in the history of HEAD, the clean version written by the agent in Work Mode into a local folder by uv run --project .guppi guppi ship --allow-draft; at a stop of that Work Mode, in a project that holds only a LICENSE of its own, the person adds that folder as a catalogue by /plugin marketplace add, installs guppi by /plugin install guppi@guppi-marketplace and types /guppi:install; the files of the project, its LICENSE among them, read against those of the plugin and against the Criterion, and the calls of the install read in the transcript of that session under ~/.claude/projects/"
checked: 2026-10-30
origin: raw/2026-10-15/0553/ledger.md#case-818.1
sprint: plugin
created: 2026-10-15
tags: [plugin, harness]
---

## Criterion

When:
`uv run --project .guppi guppi ship --allow-draft <folder>` builds the clean version, as `rule-clean-branch` sets it, and `uv run --project .guppi guppi ship --check` judges the working tree.
**＋** The agent writes the clean version into a local folder by `uv run --project .guppi guppi ship --allow-draft <folder>`; the person adds that folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` of `plugin/skills/install/SKILL.md`, as `rule-plugin-install` sets it, in a project open in Claude Code that holds a `LICENSE` of its own and none of the files the install writes.

Then:
`uv run --project .guppi guppi ship --allow-draft <folder>` writes `plugin/skills/install/SKILL.md` to `skills/install/SKILL.md` of the clean version and cleans it like each other file it writes, and the clean version holds no file under `plugin/skills/`.
**＋** `uv run --project .guppi guppi ship --check` judges `plugin/skills/install/SKILL.md` in place, as it judges each other file outside `vault/`.
**＋** The installed plugin offers the skill `install`, which the person types as `/guppi:install`.
**＋** `/guppi:install` copies each file of the plugin to the same path in the project, but those under `.claude-plugin/`, `skills/` and `.git/` and the file `LICENSE` at the root of the plugin, such as `CLAUDE.md`, `.claude/settings.json`, `.guppi/LICENSE`, the code under `.guppi/` and the pages under `vault/wiki/`.
**＋** It checks that each copied file stands, and its last message tells the person to reopen Claude Code in the project and type `/hi`.
**－** The `LICENSE` of the project stays at its path with its text unchanged: the install neither stops on it nor sets it aside.
**－** It writes nothing into the folder of the plugin, and runs no `guppi` command and no `git` command.
**－** The skills it copies under `.claude/skills/` keep their bare names, such as `hi`.
**－** Which files a new project needs, what the install does about `uv` and the Python environment under `.guppi/`, and what it does with a file of the project that stands at one of its paths are no part of this promise.

## Result

2026-10-30, Retro of session 2005, tag prod-0.2.0: test_ship.py -k plugin_skill 2 passed; the copy C:/tmp/guppi-2005/copy written by guppi ship --allow-draft holds skills/install/SKILL.md and no plugin/; guppi ship --check exit 0, no line; in the empty project p1-empty /guppi:install (transcript 589efbd9) copied 467 files and then .claude/settings.json, checked each, and its last message said to reopen Claude Code and type /hi; the 468 files of the copy outside .claude-plugin/, skills/ and .git/ all stand in p1-empty, none differing; the other files there are guppi.toml, the event log and __pycache__ written by the hooks of the first /hi; .claude/skills/ holds the bare names (hi, work and the rest); its calls were uv --version, Get-ChildItem, Copy-Item and uv sync, no guppi and no git command; every file of the copy dated 22:01, the time of the build

## History

- 2026-10-15 created · [[decision-case-818.1]]
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 status: pending → failed · raw/2026-10-15/1739/ledger.md#L13
- 2026-10-15 deferred · [[decision-case-831]]
- 2026-10-16 defer by decision-case-831 superseded · [[decision-case-843]]
- 2026-10-16 updated: set to pending with its Criterion unchanged, for a reading once a tag prod-x.y.z stands · [[decision-case-843]]
- 2026-10-16 status: pending → passed · raw/2026-10-16/0104/ledger.md#L16
- 2026-10-30 updated: the Criterion replaced whole — the refusal of a project that holds a file of the install leaves it, since the install now sets such files aside · [[decision-case-932.3]]
- 2026-10-30 updated: the Criterion replaced whole — the agent writes the clean copy; the reading at Retro of the session that sets it · [[decision-case-943.2]]
- 2026-10-30 status: pending → passed · raw/2026-10-30/2005/ledger.md#L49
- 2026-11-25 updated: the Criterion replaced whole — the install leaves the LICENSE at the root of the plugin out and keeps the LICENSE of the project; its reading by hand waits for the librarian's run of the session · [[decision-case-1052]]
