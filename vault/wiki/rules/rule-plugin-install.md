---
type: rule
kind: Leaf
purpose: Prevents a project that installs the plugin guppi from getting a part of GUPPI, or from losing a file of its own to it
status: draft
enforcement: render
governs: plugin/skills/install/SKILL.md
render_mode: full
parent: "[[rule-harness]]"
estimates: ["[[estimate-plugin-install-writes-guppi-into-an-empty-project]]", "[[estimate-plugin-install-offers-to-install-uv]]", "[[estimate-plugin-install-undoes-the-copy-when-uv-sync-fails]]", "[[estimate-plugin-install-runs-no-hook-before-uv-sync]]", "[[estimate-plugin-install-sets-aside-the-files-of-the-project]]"]
origin: raw/2026-10-15/0553/ledger.md#case-818.1
sprint: plugin
created: 2026-10-15
tags: [harness, plugin, render]
ref: rule-harness
---

## Purpose

Prevents a project that installs the plugin `guppi` from getting a part of GUPPI, or from losing a file of its own to it. The plugin, which the catalogue `guppi-marketplace` on the branch `prod` lists, is an installer. It carries one skill of its own, `install`, which the person types as `/guppi:install` in the project to install into. `guppi ship` copies the skill from `plugin/skills/install/SKILL.md`, which the Render of this page writes, to `skills/install/SKILL.md` of the clean version ([[rule-clean-branch]]). The skill first runs `uv --version`; when the tool `uv` is missing, it says that GUPPI needs it and asks the person whether it installs `uv` by the standalone installer of `uv`, runs that installer on a yes and `uv --version` again, and writes nothing into the project until `uv --version` passes; on a no, a failed installer or a `uv` that this session of Claude Code does not find yet, it stops and tells the person what to do (case 852.1). It copies into the project each file of the plugin but its own files, those under `.claude-plugin/`, `skills/` and `.git/`. Those files are the code of GUPPI in `.guppi/`, the harness `.claude/` and `CLAUDE.md`, the files at the root and the pages with `core: true`, as `guppi ship` built them. Where the project already holds a file at one of those paths that is `CLAUDE.md`, a file under `.claude/`, `.gitattributes` or `.github/workflows/checks.yml`, it moves that file of the project, its text unchanged, to the same path under the folder `guppi-set-aside/`, with `.set-aside` added to its name, such as `guppi-set-aside/CLAUDE.md.set-aside`, so that Claude Code loads and runs none of it. It writes and moves nothing when the project holds a file of the install at any other path, such as under `vault/` or `.guppi/`, or already holds `guppi-set-aside/` (as set in case 932.1). It runs no `guppi` and no `git` command. After the copy it runs `uv sync --project .guppi`, which builds the Python environment `.guppi/.venv/`, so that the first hook of the project does not wait for it ([[rule-guppi-package]], case 819). It copies `.claude/settings.json`, which holds the hooks of the project, only after `uv sync` passes, since Claude Code picks up that file in the same session: no hook of the copy runs before `uv sync` builds `.guppi/.venv/`, and none runs after a failed `uv sync` (as set in case 912). It sets aside a `.claude/settings.json` of the project only then, just before it copies the one of GUPPI, so that the hooks of the project run until then and a failed `uv sync` leaves that file in place (as set in case 932.1). When `uv sync` fails, the skill shows its output, deletes each file it copied and each folder it made, moves each file it set aside back to its old path and deletes `guppi-set-aside/`, says that the install did not finish and that the person types `/guppi:install` again, and does not send the person to `/hi` (case 853). The project then runs on its own copy: its first `/hi` renders the harness from its own rule pages, and [[rule-morph]] sets its settings there. The last message of the install lists each file it set aside, and the setup Case of that first /hi shows what each holds, for the person to keep or drop each part (as set in case 932.1). The skills of the project keep their bare names, such as `/hi`; only the skill of the plugin carries the prefix of the plugin (case 818). This page has no `core: true`, so a project that installs GUPPI does not hold it. What a new project gets beside the pages with `core: true` — the tests, the session files as skeletons and the CI of its checks — is set in [[rule-clean-branch]] (case 822).

## Render

<!-- rule-plugin-install -->
---
name: install
description: "Install GUPPI into the project open in this session: check uv and offer to install it when it is missing, copy its files from this plugin and build its Python environment, then the person reopens Claude Code and types /hi. Run it when the person types /guppi:install."
disable-model-invocation: true
---

Install GUPPI into the project of this session, the folder that Claude Code was opened in. The files come from this plugin, at `${CLAUDE_PLUGIN_ROOT}`. Write nothing into that folder of the plugin.

1. Run `uv --version`. When it passes, go on with step 2. When it fails, say that GUPPI needs the tool `uv`, which installs Python and runs the code of GUPPI, and ask the person whether you install `uv` now by its standalone installer. On Windows its command is `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`; on macOS and Linux it is `curl -LsSf https://astral.sh/uv/install.sh | sh`. Write nothing into the project until `uv --version` passes.
   - On a no, show the command for this system, say that the person installs `uv` with it and types `/guppi:install` again, and stop.
   - On a yes, run the command for this system. When it fails, or Claude Code does not run it, show its output and the command, say that the person installs `uv` with it and types `/guppi:install` again, and stop.
   - Then run `uv --version` again. When it passes, go on with step 2. When it fails, say that this session of Claude Code does not find the new `uv` yet, and that the person opens a new terminal, starts Claude Code there in this project and types `/guppi:install` again, and stop.
2. List each file under `${CLAUDE_PLUGIN_ROOT}`, but the files under `.claude-plugin/`, `skills/` and `.git/`. These are the files to install, each at the same path in the project.
3. Check which of those paths already stand in the project, and whether the folder `guppi-set-aside/` stands there. When that folder stands, or when one of those paths is not `CLAUDE.md`, a file under `.claude/`, `.gitattributes` or `.github/workflows/checks.yml`, such as a path under `vault/` or `.guppi/`, list them, say that the install writes nothing into a project that already holds them, and stop. Write and move nothing.
4. Otherwise set aside each of those paths that stands in the project, but `.claude/settings.json`: move the file of the project, its text unchanged, to the same path under `guppi-set-aside/`, with `.set-aside` added to its name, such as `guppi-set-aside/CLAUDE.md.set-aside`. Then copy each file to its path in the project, with the folders it needs, but `.claude/settings.json`, which step 7 copies once `uv sync` passes, so that no hook of GUPPI runs before then. Change no other file. Run no `guppi` command and no `git` command.
5. Check that each file you copied in step 4 now stands in the project. When one is missing, name it and stop.
6. Run `uv sync --project .guppi` in the project, which builds the Python environment of GUPPI in `.guppi/.venv/`. When it fails, show its output, then delete each file you copied in step 4 and each folder you made for them, `.guppi/` with its `.venv/` included, move each file you set aside in step 4 back to its old path, and delete `guppi-set-aside/`, so that the project holds only what it held before. Delete nothing else. Say that the install did not finish and that the project stands as before, and that the person types `/guppi:install` again once the cause that the output shows is fixed, and stop. Do not tell the person to run `uv sync`, to reopen Claude Code or to type `/hi`.
7. When the project holds a `.claude/settings.json` of its own, move it, its text unchanged, to `guppi-set-aside/.claude/settings.json.set-aside`. Then copy `.claude/settings.json` from `${CLAUDE_PLUGIN_ROOT}` to its path in the project, and check that it stands. When it is missing, name it and stop.
8. Say that GUPPI is installed, and that the person reopens Claude Code in this project and types `/hi`. When step 4 or step 7 set aside files, list each of them with its path under `guppi-set-aside/`, and say that the setup Case of the first `/hi` shows what each holds, for the person to keep or drop each part, and that until then none of them loads or runs. When step 1 installed `uv`, say that the person starts Claude Code from a new terminal, so that the hooks of the project find `uv`.
<!-- /rule-plugin-install -->

## History

- 2026-10-15 created · [[decision-case-818.1]]
- 2026-10-15 estimate estimate-plugin-install-writes-guppi-into-an-empty-project added · [[decision-case-818.1]]
- 2026-10-15 updated: /guppi:install checks uv before it writes and builds the Python environment by uv sync after the copy · [[decision-case-819.4]]
- 2026-10-15 updated: what a new project gets is set in rule-clean-branch · [[decision-case-822.3]]
- 2026-10-16 status: draft → built · cascade
- 2026-10-16 updated: when uv is missing, /guppi:install asks to install it by the standalone installer of uv and goes on once uv --version passes · [[decision-case-852.1]]
- 2026-10-16 estimate estimate-plugin-install-offers-to-install-uv added · [[decision-case-852.1]]
- 2026-10-16 updated: when uv sync fails, /guppi:install deletes what it copied, says the install did not finish and sends the person to /guppi:install, not to /hi · [[decision-case-853]]
- 2026-10-16 estimate estimate-plugin-install-undoes-the-copy-when-uv-sync-fails added · [[decision-case-853]]
- 2026-10-16 status: built → draft · cascade
- 2026-10-29 status: draft → built · cascade
- 2026-10-29 deferred · [[decision-case-911]]
- 2026-10-29 updated: the install copies .claude/settings.json only after uv sync passes, so no hook of the copy runs before uv sync or after a rollback · [[decision-case-912.1]]
- 2026-10-29 estimate estimate-plugin-install-runs-no-hook-before-uv-sync added · [[decision-case-912.1]]
- 2026-10-29 status: built → draft · cascade
- 2026-10-30 status: draft → built · cascade
- 2026-10-30 defer by decision-case-911 superseded · [[decision-case-932.1]]
- 2026-10-30 updated: taken up: the install sets aside a CLAUDE.md, a file under .claude/, a .gitattributes or a .github/workflows/checks.yml of the project in guppi-set-aside/, the settings file only after uv sync passes, and stops only on a clash elsewhere · [[decision-case-932.1]]
- 2026-10-30 estimate estimate-plugin-install-sets-aside-the-files-of-the-project added · [[decision-case-932.1]]
- 2026-10-30 status: built → draft · cascade
- 2026-10-30 updated: the install by hand of its readings taken at a stop of Work Mode of session 2005 · [[decision-case-943.1]]
