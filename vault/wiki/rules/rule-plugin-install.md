---
type: rule
kind: Leaf
purpose: Prevents a project that installs the plugin guppi from getting a part of GUPPI, or from losing a file of its own to it
status: draft
enforcement: render
governs: plugin/skills/install/SKILL.md
render_mode: full
parent: "[[rule-harness]]"
estimates: ["[[estimate-plugin-install-writes-guppi-into-an-empty-project]]"]
origin: raw/2026-10-15/0553/ledger.md#case-818.1
sprint: plugin
created: 2026-10-15
tags: [harness, plugin, render]
ref: rule-harness
---

## Purpose

Prevents a project that installs the plugin `guppi` from getting a part of GUPPI, or from losing a file of its own to it. The plugin, which the catalogue `guppi-marketplace` on the branch `prod` lists, is an installer. It carries one skill of its own, `install`, which the person types as `/guppi:install` in the project to install into. `guppi ship` copies the skill from `plugin/skills/install/SKILL.md`, which the Render of this page writes, to `skills/install/SKILL.md` of the clean version ([[rule-clean-branch]]). The skill first runs `uv --version`; when the tool `uv` is missing, it says that GUPPI needs it and writes nothing. It copies into the project each file of the plugin but its own files, those under `.claude-plugin/`, `skills/` and `.git/`. Those files are the code of GUPPI in `.guppi/`, the harness `.claude/` and `CLAUDE.md`, the files at the root and the pages with `core: true`, as `guppi ship` built them. It writes nothing when one of those files already stands in the project, and it runs no `guppi` and no `git` command. After the copy it runs `uv sync --project .guppi`, which builds the Python environment `.guppi/.venv/`, so that the first hook of the project does not wait for it ([[rule-guppi-package]], case 819). The project then runs on its own copy: its first `/hi` renders the harness from its own rule pages, and [[rule-morph]] sets its settings there. The skills of the project keep their bare names, such as `/hi`; only the skill of the plugin carries the prefix of the plugin (case 818). This page has no `core: true`, so a project that installs GUPPI does not hold it. What a new project gets beside the pages with `core: true` — the tests, the session files as skeletons and the CI of its checks — is set in [[rule-clean-branch]] (case 822).

## Render

<!-- rule-plugin-install -->
---
name: install
description: "Install GUPPI into the project open in this session: check uv, copy its files from this plugin and build its Python environment, then the person reopens Claude Code and types /hi. Run it when the person types /guppi:install."
disable-model-invocation: true
---

Install GUPPI into the project of this session, the folder that Claude Code was opened in. The files come from this plugin, at `${CLAUDE_PLUGIN_ROOT}`. Write nothing into that folder of the plugin.

1. Run `uv --version`. When it fails, say that GUPPI needs the tool `uv`, which installs Python and runs the code of GUPPI, and that the person installs `uv` and types `/guppi:install` again, and stop. Write nothing.
2. List each file under `${CLAUDE_PLUGIN_ROOT}`, but the files under `.claude-plugin/`, `skills/` and `.git/`. These are the files to install, each at the same path in the project.
3. Check which of those paths already stand in the project. When one or more stand, list them, say that the install writes nothing into a project that already holds one of its files, and stop. Write nothing.
4. Otherwise copy each file to its path in the project, with the folders it needs. Change no other file. Run no `guppi` command and no `git` command.
5. Check that each file now stands in the project. When one is missing, name it and stop.
6. Run `uv sync --project .guppi` in the project, which builds the Python environment of GUPPI in `.guppi/.venv/`. When it fails, show its output and stop.
7. Say that GUPPI is installed, and that the person reopens Claude Code in this project and types `/hi`.
<!-- /rule-plugin-install -->

## History

- 2026-10-15 created · [[decision-case-818.1]]
- 2026-10-15 estimate estimate-plugin-install-writes-guppi-into-an-empty-project added · [[decision-case-818.1]]
- 2026-10-15 updated: /guppi:install checks uv before it writes and builds the Python environment by uv sync after the copy · [[decision-case-819.4]]
- 2026-10-15 updated: what a new project gets is set in rule-clean-branch · [[decision-case-822.3]]
