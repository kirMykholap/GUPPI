## Case 905 — The install copies the settings of the project after uv sync

> **context:**
> `/guppi:install` copies every file of GUPPI into the project in one step, `.claude/settings.json` with them, and only then runs `uv sync --project .guppi`. Claude Code picks up that settings file in the same session, so each hook of the copy runs `uv run --project .guppi` at the next tool call. On a good install a hook builds `.guppi/.venv/` before `uv sync` does; on a failed `uv sync` the rollback deletes `.guppi/`, and each later command of that session shows a hook error. `lesson-plugin-install-hooks-of-the-copy-run-at-once` (L44 of session 0327) records both, and the Result of `estimate-guppi-package-is-ready-after-the-install` shows the folder made by a hook two seconds before `uv sync` printed "Checked 9 packages". The hooks documentation of Claude Code (https://code.claude.com/docs/en/hooks) says that direct edits to hooks in settings files are normally picked up automatically by the file watcher; the chosen fix does not rest on that timing, since a settings file that does not stand yet runs no hook. The person chose to copy `.claude/settings.json` only after `uv sync` passes. The pair on the Purpose of `rule-plugin-install` adds that order beside the sentence on `uv sync`; the other sentences of the Purpose stand, since the install still copies each file and the rollback still deletes each file it copied. In the Render, step 4 leaves the settings file out, a new step 7 copies it and checks it stands, and the old step 7 becomes step 8; the Render holds no case number, since `guppi ship --check` refuses one in `plugin/skills/install/SKILL.md`. A Grep for `uv sync` over `vault/wiki/` without `brief.md`, `sprint.md` and `log.md` printed five files: `rule-plugin-install.md`, `lesson-plugin-install-hooks-of-the-copy-run-at-once.md`, `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails.md`, `estimate-plugin-install-offers-to-install-uv.md` and `estimate-guppi-package-is-ready-after-the-install.md`. The Criteria of the three Estimates stand: the rollback still deletes each file it copied, `uv --version` still runs first, and `uv sync` still runs after the files of step 4 and before the person is sent to `/hi`; the Criterion of `estimate-plugin-install-writes-guppi-into-an-empty-project` stands too, since the install still copies `.claude/settings.json` and checks each copied file. The new Estimate `estimate-plugin-install-runs-no-hook-before-uv-sync` checks the order, read by hand after the librarian's run like the other install Estimates. A project that already holds its own settings is outside this Case: step 3 still refuses it, and the person's new item on installing into such a project is a Case of its own. The lesson belongs to another session, so no decision line carries `{addresses:...}`.

> **problem:**
> The hooks of the copied settings run inside the install session itself: they build `.guppi/.venv/` before `uv sync`, and they fail at each command after a rollback.

> **recommend:**
> - **How the install keeps the copied hooks from running**
>   - Recommended: (a) copy `.claude/settings.json` last, after `uv sync` passes.
>   - Answer: agreed, (a).
> - **Which Estimate checks the fix**
>   - Recommended: (a) a new Estimate `estimate-plugin-install-runs-no-hook-before-uv-sync` on `rule-plugin-install`.
>   - Answer: agreed, (a).
> - **When the new check is read**
>   - Recommended: (a) by hand, after the librarian's run, like the other install Estimates: one install where `uv sync` passes and one offline.
>   - Answer: agreed, (a).

> **given:**
> `rule-plugin-install`: the rule of the install skill, its Purpose and its Render.
> **＋** `plugin/skills/install/SKILL.md`: the skill that the Render writes.
> **＋** `/guppi:install`: the command by which the person runs that skill.
> **＋** `.guppi/.venv/`: the Python environment that `uv sync` builds.
> **＋** `/hi`: the skill to which the install sends the person at its end.
> **＋** `.claude/settings.json`: the settings file of the copy, which holds the hooks of the project.
> **＋** `estimate-plugin-install-runs-no-hook-before-uv-sync`: the new check of the order.

> **when:**
> The person types `/guppi:install` of `plugin/skills/install/SKILL.md` in an empty project open in Claude Code, where `uv --version` passes.

> **then:**
> Until `uv sync --project .guppi` passes, the project holds no `.claude/settings.json`, so no hook of the copy runs.
> **＋** `uv sync --project .guppi` builds `.guppi/.venv/`, which no hook made before it.
> **＋** When `uv sync` passes, the agent copies `.claude/settings.json` from the plugin, checks that it stands, and then tells the person to reopen Claude Code and type `/hi`.
> **＋** When `uv sync` fails, the project never holds `.claude/settings.json`, and no later command of that session shows a hook error.
> **－** In a project that already holds `.claude/settings.json` or another file of the install, the agent still lists them, writes nothing and stops.

> **tasks:**
> - [ ] update `rule-plugin-install`
>   - old: `does not wait for it ([[rule-guppi-package]], case 819).`
>   - new: `` does not wait for it ([[rule-guppi-package]], case 819). It copies `.claude/settings.json`, which holds the hooks of the project, only after `uv sync` passes, since Claude Code picks up that file in the same session: no hook of the copy runs before `uv sync` builds `.guppi/.venv/`, and none runs after a failed `uv sync` (as set in case 905). ``
>   - old: `4. Otherwise copy each file to its path in the project, with the folders it needs.`
>   - new: `` 4. Otherwise copy each file to its path in the project, with the folders it needs, but `.claude/settings.json`, which step 7 copies once `uv sync` passes, so that no hook of the project runs before then. ``
>   - old: `7. Say that GUPPI is installed,`
>   - new:
>     ````
>     7. Copy `.claude/settings.json` from `${CLAUDE_PLUGIN_ROOT}` to its path in the project, and check that it stands. When it is missing, name it and stop.
>     8. Say that GUPPI is installed,
>     ````
>   - change: `the install copies .claude/settings.json only after uv sync passes, so no hook of the copy runs before uv sync or after a rollback`
> - [ ] `uv run --project .guppi guppi render`: `plugin/skills/install/SKILL.md`
> - [ ] create `estimate-plugin-install-runs-no-hook-before-uv-sync`
>   - ref: `rule-plugin-install`
>   - kind: `QA`
>   - purpose: `Whether /guppi:install copies .claude/settings.json only after uv sync passes, so that no hook of the copied project builds .guppi/.venv before uv sync or fails after a rollback`
>   - method: `by hand, after the librarian's run of the session that sets this Criterion, with a tag prod-x.y.z in the history of HEAD: the clean version written into a local folder by uv run --project .guppi guppi ship --allow-draft, that folder added as a catalogue by /plugin marketplace add and guppi installed from it by /plugin install guppi@guppi-marketplace; in an empty project where uv --version passes, /guppi:install typed, and the output of uv sync and the time .guppi/.venv was made read; in a second empty project with Claude Code started from a terminal with UV_OFFLINE=1 and UV_CACHE_DIR set to an empty folder, /guppi:install typed and a command run after its rollback; the transcripts and the files of both projects read against the Criterion`
>   - tags: `[plugin, hooks]`
> - [ ] read `estimate-plugin-install-runs-no-hook-before-uv-sync`

> **ratification:**
> ```
> - decision[case 905][update][rule-plugin-install]{ref:rule-plugin-install}
> - decision[case 905][create][estimate-plugin-install-runs-no-hook-before-uv-sync]{ref:rule-plugin-install}{tags:plugin,hooks}
> ```
