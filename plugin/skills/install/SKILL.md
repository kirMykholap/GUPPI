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
