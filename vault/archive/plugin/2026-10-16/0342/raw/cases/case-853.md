## Case 853 — /guppi:install undoes its copy when uv sync fails

> **context:**
> `/guppi:install` copies the files of GUPPI into an empty project and then runs `uv sync --project .guppi`, which downloads the Python packages and builds `.guppi/.venv/`. Step 6 of its skill says only that when `uv sync` fails, the agent shows the output and stops. In `C:\PROJECTS\test-uv-offline` of session 0104, `uv sync` failed on `ruff==0.16.1` of the `dev` group, and the agent's last sentence still told the person to run `uv sync`, reopen Claude Code and type `/hi`. `.guppi/.venv/` was left unbuilt (handoff of session 0104). The project kept every copied file, and a second `/guppi:install` would refuse it at step 3, because its files already stand. The person said this was bad, and this session recorded `estimate-guppi-package-is-ready-after-the-install` as failed. The person chose that on a failed `uv sync` the agent shows the output, deletes every file it copied and every folder it made, says that the install did not finish, and tells the person to type `/guppi:install` again, with no word on `/hi`. The deletion keeps the Purpose of `rule-plugin-install`, the rule that governs this change: a project loses no file of its own, since the install deletes only what it wrote into a project that held none of those files. The person chose that `uv sync` keeps the `dev` group. A project runs `pytest` and `ruff` through `guppi test` and `guppi style`, as `guppi.toml` sets them, and Work Mode, Retro and the CI of the project run them. From the agent's knowledge of `uv`, which was not read here, `uv run` would install the missing group at the first hook anyway, and with no network and an empty cache `uv` cannot download PyYAML or Python either. The person chose a new Estimate on `rule-plugin-install` for this failure path. Case 852.2 replaced the Criterion of `estimate-guppi-package-is-ready-after-the-install` with a `－` line on a failed `uv sync`. To keep this promise from being signed twice, Case 852 is built again: that line and the offline project leave that Criterion and its `method`, and point to `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails`. The person agreed to that rebuild. Case 852.1 changes the Purpose sentence on a missing `uv`, the description, step 1 and step 7 of `rule-plugin-install`. This Case changes step 6 and adds one sentence after the sentence on `uv sync` in the Purpose, which Case 852.1 does not touch, so the `old` of each pair matches the page as Case 852.1 leaves it. The check of this file notes that the step 6 pair touches a sentence that Case 852.1 changes too. That sentence runs across the end of step 6 and the start of step 7, which the check reads as one sentence. The `old` of this Case ends at the end of step 6, and the `old` of Case 852.1 starts at step 7, so neither pair matches text the other changes. The two new texts were read side by side. The new step 7 of Case 852.1, with its new terminal once step 1 installed `uv`, runs only after a successful step 6. Its new step 1 writes nothing before `uv --version` passes. Both fit the new step 6, which stops before step 7 on a failed `uv sync`. Each sentence of `rule-plugin-install` that states the end of the install was read. In the description, the person reopens Claude Code and types `/hi`. In step 7 and in Case 852.1's new step 7, the install says the person types `/hi`. These stand, since they describe a successful install, which step 6 now leaves before step 7 on a failure. The sentence of step 4, change no other file, stands, since the agent deletes only files it wrote. The Criterion of `estimate-plugin-install-writes-guppi-into-an-empty-project` says that the last message tells the person to type `/hi`. It stands, since its last `－` line puts what the install does about the Python environment outside that promise. A Grep `uv sync` over `vault/wiki/` printed `brief.md`, `log.md`, `rule-plugin-install.md` and `estimate-guppi-package-is-ready-after-the-install.md`, and over `.claude/` printed nothing. The rebuild of Case 852 handles the hit in the Estimate. A Grep `skills/install|rule-plugin-install|"install"` over `.guppi/tests/` printed `test_ship.py` alone. Its tests write their own skill file into a temporary folder and do not read the live skill. `guppi ship --check` refuses a reference to a case in `plugin/skills/install/SKILL.md`, so the new step 6 holds none. The pointer in the new Purpose sentence stands, since the page has no `core: true`. A Glob `vault/**/*undoes*` printed nothing, so the new slug is free. The Case adds no code that judges a text.

> **problem:**
> When `uv sync` fails, `/guppi:install` leaves a half-installed project that a second `/guppi:install` refuses, and the agent still sends the person on to `/hi`.

> **recommend:**
> - **What should `/guppi:install` do when `uv sync` fails?**
>   - Recommended: (a) undo the copy: show the output of `uv sync`, delete every file it copied and every folder it made, `.guppi/` with its `.venv/` included, say that the install did not finish, tell the person to type `/guppi:install` again, and never mention `/hi`.
>   - Answer: agreed, (a).
> - **Should the install's `uv sync` also install `pytest` and `ruff`?**
>   - Recommended: (a) keep the `dev` group in the install; leaving it out only moves the download to the first hook.
>   - Answer: agreed, (a).
> - **How should we check that a failed `uv sync` undoes the install?**
>   - Recommended: (a) a new Estimate on `rule-plugin-install` for the failure path, read by hand in an empty project offline with an empty cache of `uv`; Case 852 is built again so that the check of the Python environment drops its line on a failed `uv sync` and its offline project.
>   - Answer: agreed, (a).

> **given:**
> `rule-plugin-install`: the skill `/guppi:install`, its Purpose and its Render.
> **＋** `plugin/skills/install/SKILL.md`: the skill file rendered from `rule-plugin-install`.
> **＋** `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails`: the new check of this behaviour.
> **＋** `.guppi/.venv/`: the Python environment that `uv sync --project .guppi` builds.
> **＋** `/hi`: the skill the person types after a successful install.
> **＋** `vault/raw/2026-10-16/0342/cases/case-852.md`: the Case of this session that changes the same page and the check of the Python environment.

> **when:**
> The person types `/guppi:install` of `plugin/skills/install/SKILL.md` in an empty project open in Claude Code, where `uv --version` passes, and `uv sync --project .guppi` fails after the copy, such as with no network and an empty cache of `uv`.

> **then:**
> The agent shows the output of `uv sync --project .guppi`.
> **＋** It deletes each file it copied into the project and each folder it made there, `.guppi/` with `.guppi/.venv/` included, so that the project holds only what it held before `/guppi:install`.
> **＋** It says that the install did not finish and that the project stands as before, and that the person types `/guppi:install` again once the cause that the output shows is fixed, and stops.
> **－** It does not tell the person to run `uv sync`, to reopen Claude Code or to type `/hi`.
> **－** It deletes no file or folder that stood in the project before `/guppi:install`, and nothing in the folder of the plugin.

> **tasks:**
> - [ ] update `rule-plugin-install`
>   - old: `so that the first hook of the project does not wait for it ([[rule-guppi-package]], case 819).`
>   - new: `` so that the first hook of the project does not wait for it ([[rule-guppi-package]], case 819). When `uv sync` fails, the skill shows its output, deletes each file it copied and each folder it made, says that the install did not finish and that the person types `/guppi:install` again, and does not send the person to `/hi` (case 853). ``
>   - old: `` 6. Run `uv sync --project .guppi` in the project, which builds the Python environment of GUPPI in `.guppi/.venv/`. When it fails, show its output and stop. ``
>   - new: `` 6. Run `uv sync --project .guppi` in the project, which builds the Python environment of GUPPI in `.guppi/.venv/`. When it fails, show its output, then delete each file you copied in step 4 and each folder you made for them, `.guppi/` with its `.venv/` included, so that the project holds only what it held before. Delete nothing else. Say that the install did not finish and that the project stands as before, and that the person types `/guppi:install` again once the cause that the output shows is fixed, and stop. Do not tell the person to run `uv sync`, to reopen Claude Code or to type `/hi`. ``
>   - change: `when uv sync fails, /guppi:install deletes what it copied, says the install did not finish and sends the person to /guppi:install, not to /hi`
> - [ ] create `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails`
>   - ref: `rule-plugin-install`
>   - kind: `QA`
>   - purpose: `Whether /guppi:install, when uv sync fails after the copy, shows its output, deletes every file and folder it wrote into the project, and sends the person to /guppi:install again, not to /hi`
>   - method: `by hand, after the librarian's run of the session that sets this Criterion, with a tag prod-x.y.z in the history of HEAD: the clean version written into a local folder by uv run --project .guppi guppi ship --allow-draft, that folder added as a catalogue by /plugin marketplace add and guppi installed from it by /plugin install guppi@guppi-marketplace; in an empty project with Claude Code started from a terminal with UV_OFFLINE=1 and UV_CACHE_DIR set to an empty folder, where uv --version passes, /guppi:install typed; its reply and the files and folders of the project before and after read against the Criterion`
>   - tags: `[plugin, harness]`
> - [ ] `uv run --project .guppi guppi render`: `plugin/skills/install/SKILL.md`
> - [ ] read `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails`

> **ratification:**
> ```
> - decision[case 853][update][rule-plugin-install]{ref:rule-plugin-install}
> - decision[case 853][create][estimate-plugin-install-undoes-the-copy-when-uv-sync-fails]{ref:rule-plugin-install}{tags:plugin,harness}
> ```
