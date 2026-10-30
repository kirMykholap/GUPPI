## Case 912 — The install copies the settings of the project after uv sync

> **context:**
> `/guppi:install` copies every file of GUPPI into the project in one step, `.claude/settings.json` with them, and only then runs `uv sync --project .guppi`. Claude Code picks up that settings file in the same session, so each hook of the copy runs `uv run --project .guppi` at the next tool call. On a good install a hook builds `.guppi/.venv/` before `uv sync` does; on a failed `uv sync` the rollback deletes `.guppi/`, and each later command of that session shows a hook error. `lesson-plugin-install-hooks-of-the-copy-run-at-once` (L44 of session 0327) records both, and the Result of `estimate-guppi-package-is-ready-after-the-install` shows the folder made by a hook two seconds before `uv sync` printed "Checked 9 packages". The hooks documentation of Claude Code (https://code.claude.com/docs/en/hooks) says that direct edits to hooks in settings files are normally picked up automatically by the file watcher; the chosen fix does not rest on that timing, since a settings file that does not stand yet runs no hook. The person chose to copy `.claude/settings.json` only after `uv sync` passes. This Case replaces Case 905, which was ratified whole: at `/pre-spec` the person agreed to a pair on step 5 of the Render, since that step checks each file of the list of step 2 and would stop on the missing settings file before `uv sync`, and chose that the Case also replace the Criterion of `estimate-guppi-package-is-ready-after-the-install`, whose sentence "After it copies the files, it runs `uv sync`" the new order makes false. That is a second promise, so the Case has two sub-cases and a new number, and its decision lines retire Case 905. Case 912.1 holds the change of `rule-plugin-install` and the new Estimate `estimate-plugin-install-runs-no-hook-before-uv-sync`, which checks that no hook runs before `uv sync` or after a rollback. Case 912.2 replaces the Criterion of the package Estimate with the order of the steps, sets its `purpose` and its `method` anew, and is read in the same installs by hand as the new Estimate. The function `cascade` of `.guppi/guppi/generate.py` sets a rule `draft` while one of its own Estimates does not stand `passed`, so `rule-guppi-package` and `rule-plugin-install` go back to `draft` at the librarian's run and stand `built` again once those readings pass; no task sets that status. In the Purpose of `rule-plugin-install` the other sentences stand, since the install still copies each file and the rollback still deletes each file it copied. In the Render, step 4 leaves out the settings file, step 5 checks the files of step 4, a new step 7 copies the settings file and checks it, and the old step 7 becomes step 8. The Render holds no case number, since `guppi ship --check` refuses one in `plugin/skills/install/SKILL.md`. A Grep for `uv sync` over `vault/wiki/` without `brief.md`, `sprint.md` and `log.md` printed five files: `rule-plugin-install.md`, `lesson-plugin-install-hooks-of-the-copy-run-at-once.md`, `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails.md`, `estimate-plugin-install-offers-to-install-uv.md` and `estimate-guppi-package-is-ready-after-the-install.md`. The Criteria of `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails` and `estimate-plugin-install-offers-to-install-uv` stand: the rollback still deletes each file it copied, and `uv --version` still runs first. The Criterion of `estimate-plugin-install-writes-guppi-into-an-empty-project` stands too, since the install still copies `.claude/settings.json` and checks each copied file. A project that already holds its own settings is outside this Case: step 3 still refuses it, and the person's new item on installing into such a project is a Case of its own. The lesson belongs to another session, so no decision line carries `{addresses:...}`.

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
> - **Change**
>   - Asked: at `/pre-spec`, a pair on step 5 of the Render, so that it checks only the files that step 4 copied.
>   - Taken: Case 912.1 gains that pair.
> - **Change**
>   - Asked: at `/pre-spec`, the Case also replaces the Criterion of `estimate-guppi-package-is-ready-after-the-install`, so that it says the install copies every file but `.claude/settings.json` before `uv sync`; the Estimate goes `pending` and is read in the same installs by hand as the new Estimate.
>   - Taken: Case 912.2, under the new number 912 with sub-cases, which retires Case 905.

### Case 912.1 — No hook of the copy runs before uv sync

> **given:**
> `rule-plugin-install`: the rule of the install skill, its Purpose and its Render.
> **＋** `plugin/skills/install/SKILL.md`: the skill that the Render writes.
> **＋** `/guppi:install`: the command by which the person runs that skill.
> **＋** `.claude/settings.json`: the settings file of the copy, which holds the hooks of the project.
> **＋** `.guppi/.venv/`: the Python environment that `uv sync` builds.
> **＋** `estimate-plugin-install-runs-no-hook-before-uv-sync`: the new check that no hook runs early.

> **when:**
> The person types `/guppi:install` of `plugin/skills/install/SKILL.md` in an empty project open in Claude Code, where `uv --version` passes.

> **then:**
> Until `uv sync --project .guppi` passes, the project holds no `.claude/settings.json`, so no hook of the copy runs.
> **＋** No hook of the copy has made `.guppi/.venv/` by the time `uv sync` runs.
> **＋** When `uv sync` fails, the project never holds `.claude/settings.json`, and no later command of that session shows a hook error.
> **－** In a project that already holds `.claude/settings.json` or another file of the install, the agent still lists them, writes nothing and stops.

> **tasks:**
> - [ ] update `rule-plugin-install`
>   - old: `does not wait for it ([[rule-guppi-package]], case 819).`
>   - new: `` does not wait for it ([[rule-guppi-package]], case 819). It copies `.claude/settings.json`, which holds the hooks of the project, only after `uv sync` passes, since Claude Code picks up that file in the same session: no hook of the copy runs before `uv sync` builds `.guppi/.venv/`, and none runs after a failed `uv sync` (as set in case 912). ``
>   - old: `4. Otherwise copy each file to its path in the project, with the folders it needs.`
>   - new: `` 4. Otherwise copy each file to its path in the project, with the folders it needs, but `.claude/settings.json`, which step 7 copies once `uv sync` passes, so that no hook of the project runs before then. ``
>   - old: `5. Check that each file now stands in the project.`
>   - new: `5. Check that each file you copied in step 4 now stands in the project.`
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
> - decision[case 912.1][update][rule-plugin-install]{ref:rule-plugin-install}{supersedes:case 905}
> - decision[case 912.1][create][estimate-plugin-install-runs-no-hook-before-uv-sync]{ref:rule-plugin-install}{tags:plugin,hooks}{supersedes:case 905}
> ```

### Case 912.2 — The install builds the environment before it copies the settings

> **given:**
> `estimate-guppi-package-is-ready-after-the-install`: its Criterion, `purpose` and `method` are set anew.
> **＋** `rule-guppi-package`: the target of that Estimate.
> **＋** `rule-plugin-install`: the rule of the install skill.
> **＋** `plugin/skills/install/SKILL.md`: the skill that `rule-plugin-install` renders.
> **＋** `uv run --project .guppi guppi ship --allow-draft <folder>`: the command that writes the clean version.
> **＋** `/plugin marketplace add <folder>` and `/plugin install guppi@guppi-marketplace`: the commands by which the person installs the plugin.
> **＋** `/guppi:install`: the command by which the person runs the skill.
> **＋** `.claude/settings.json` and `.guppi/.venv/`: the settings file of the copy and the Python environment that `uv sync` builds.
> **＋** `/hi`: the skill to which the install sends the person at its end.

> **when:**
> The person writes the clean version into a local folder by `uv run --project .guppi guppi ship --allow-draft <folder>`, adds that folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` in an empty project open in Claude Code, as `rule-plugin-install` sets it.

> **then:**
> Before it writes anything, `/guppi:install` runs `uv --version`.
> **＋** It copies each file of the install but `.claude/settings.json`, and then runs `uv sync --project .guppi` in the project, which builds the Python environment `.guppi/.venv/`.
> **＋** Once `uv sync` passes, it copies `.claude/settings.json`, and then tells the person to reopen Claude Code and type `/hi`.
> **＋** The hooks of the project find that environment built at the first `/hi`.
> **－** Where `uv --version` passes, it asks nothing about `uv`.

> **tasks:**
> - [ ] update `estimate-guppi-package-is-ready-after-the-install`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether /guppi:install runs uv --version before it writes anything and, where it passes, asks nothing about uv, copies every file but .claude/settings.json, builds the Python environment .guppi/.venv/ by uv sync, and copies .claude/settings.json only then, before it sends the person to /hi"
>     method: "by hand, after the librarian's run of the session that sets this Criterion, with a tag prod-x.y.z in the history of HEAD: the agent writes the clean version into a local folder by uv run --project .guppi guppi ship --allow-draft; then, at a stop of Work Mode, the person adds that folder as a catalogue, installs the plugin guppi from it and, in an empty project on the machine with uv, types /guppi:install, reopens Claude Code there and types /hi; the person's answer on the output of the install, the order of its steps, the files of the project and its .guppi/.venv/, read against the Criterion; the copy and the project may be those of the reading of estimate-plugin-install-runs-no-hook-before-uv-sync"
>     ```
>   - change: `the Criterion replaced whole — the install copies every file but .claude/settings.json before uv sync, and that file after uv sync passes`
> - [ ] read `estimate-guppi-package-is-ready-after-the-install`

> **ratification:**
> ```
> - decision[case 912.2][update][estimate-guppi-package-is-ready-after-the-install]{ref:rule-guppi-package}
> ```
