## Case 846 — The install check reads a local copy of the clean version

> **context:**
> `/guppi:install` first runs `uv --version` and stops, writing nothing, when the tool `uv` is missing. After the copy it runs `uv sync --project .guppi`, which builds the Python environment `.guppi/.venv/` before the skill sends the person to `/hi`. `estimate-guppi-package-is-ready-after-the-install` checks this, and no one has read it yet. Its reading needs a local copy, and `guppi ship --allow-draft` writes one only when a tag `prod-x.y.z` stands in the history of HEAD. `version` and `VERSION_TAG` of `.guppi/guppi/ship.py` take `prod-2` for no version, so with the tags `prod-1` and `prod-2` the command exits 1 with `ship: no tag prod-x.y.z in the history of HEAD; nothing written`. Case 831 put the Estimate off for that reason. Case 832 put it off because its `when` installs from the catalogue of the branch `prod` while its `method` reads a local copy. The decision page of case 832 gives the problem: no Case of that session makes the `when` agree with the `method`. In this batch, Case 841 owns the task that sets the tag, and this Case reads the Estimate after it.
>
> The schema sets the rule: a promise changes only when its Criterion is replaced whole (case 378.4). So this Case replaces the Criterion. Its `when` now names the local copy, written the way the `when` of `estimate-plugin-install-writes-guppi-into-an-empty-project` writes it, and its `then` keeps each line of the old Criterion word for word. The check of the Case file sends a note on the old `when` line, which this Case changes on purpose. The `method` is set anew. It waits for the tag, makes `uv` missing on the same machine by a terminal whose `PATH` holds no folder of `uv`, and makes `uv sync` fail in a third empty project opened offline with an empty cache, so the line on a failed `uv sync` is read as behaviour. The copy and the empty project with `uv` may be the same as those of the reading of `estimate-plugin-install-writes-guppi-into-an-empty-project`. `vault/wiki/where-to-stop.md` says that a reading only the person can take is no stop unless a task opens with `stop:`, so this Case holds the one `stop:` task for every install by hand of the batch, before the push of the tag `prod-0.2.0` that Case 841 sets, and the `method` names the person's answer. Cases 843 and 845 need their own `stop:` tasks of the install removed and a pointer to this one, and the `stop:` task of the push moves from Case 841 to the new Case 850, after this stop, while Case 847 stands as it is; Case 843 holds no reading task of its own before the push, so the `stop:` task here reads its two projects against its Criterion; the person agreed to these changes at `/pre-spec`. The `purpose` states no part that changes, so it stands. The decision line carries `{supersedes:case 831}` and `{supersedes:case 832}`, the two Cases in the `deferred_by` of the page. Case 831 also put off two other Estimates. Its mark here clears only this page, since `generate` clears a defer only from the pages the superseding Case names. A Grep for `catalogue of the branch` over `vault/wiki/` printed one file, `estimates/estimate-guppi-package-is-ready-after-the-install.md`, which is the page this Case changes. A Grep for `guppi-package-is-ready` over the repository, `vault/raw/` left out, printed `vault/wiki/brief.md`, `vault/wiki/backlog.md`, `vault/wiki/log.md` and `vault/wiki/rules/rule-guppi-package.md`. No test under `.guppi/tests/` reads the page. `rule-guppi-package` lists the Estimate in `estimates`, and that list stays true. No code changes, and no `create` stands in the Case, so no query of the vault for a free slug was run.

> **problem:**
> The check of the install has never been read. Its `when` installs from the branch `prod`, which no build has written, while its `method` reads a local copy. That copy needs a tag `prod-x.y.z`, which does not stand yet.

> **recommend:**
> - **Which install does the check describe?**
>   - Recommended: (a) the local copy: the `when` names the folder that `guppi ship --allow-draft` writes, added as a catalogue, and the result lines stay. The Criterion is replaced whole and set `pending`.
>   - Answer: agreed, (a).
> - **How does the reading make `uv` look missing?**
>   - Recommended: (a) the same machine: Claude Code started from a terminal whose `PATH` holds no folder of `uv`.
>   - Answer: agreed, (a).
> - **Does the reading make `uv sync` fail on purpose?**
>   - Recommended: (a) yes: a third empty project, with Claude Code started from a terminal with `UV_OFFLINE=1` and `UV_CACHE_DIR` set to an empty folder.
>   - Answer: agreed, (a).
> - **Does this reading share its install with the other install checks?**
>   - Recommended: (a) yes: the local copy and the empty project with `uv` may be the same as those of the other install readings of the batch.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: a finding of `/pre-spec`: the readings by hand need steps that only the person can take, and the Case named neither the person's answer nor a `stop:` task. The person agreed to one `stop:` task in this Case for every install by hand of the batch, after the agent builds the copy and runs its own parts, with the four projects in one go, and to a `method` that names the person's answer.
>   - Taken: the `method` names the agent's part and the person's answer; a task by hand writes the copy after the tag; one `stop:` task, before the push of the tag, holds the four projects of Cases 843, 845 and 846; `given` names `rule-where-to-stop`.
> - **Change**
>   - Asked: at `/pre-spec`, the push of the tag stands in the new Case 850, not in Case 847; and the `stop:` task also reads the output of `/guppi:install` and the files of the project with `uv` and of the project with its own `CLAUDE.md` against the Criterion of `estimate-plugin-install-writes-guppi-into-an-empty-project`, since Case 843 no longer holds a reading task before the push.
>   - Taken: the `stop:` task names the push of Case 850 and reads those two projects against that Criterion, right after the installs; `context` names Case 850.

> **given:**
> `estimate-guppi-package-is-ready-after-the-install`: its Criterion is replaced whole, and its `method` is set anew.
> **＋** `rule-guppi-package`: the rule that the Estimate checks.
> **＋** `rule-plugin-install` and `plugin/skills/install/SKILL.md`: the rule of the skill `/guppi:install`, and the skill as its Render writes it.
> **＋** `rule-where-to-stop`: the rule of a task that opens with `stop:`.
> **＋** `.guppi/guppi/ship.py`: `guppi ship`, which writes the clean version into a folder.
> **＋** `/plugin marketplace add <folder>` and `/plugin install guppi@guppi-marketplace`: the commands of Claude Code that add a catalogue and install a plugin from it.
> **＋** `.guppi/.venv/`: the Python environment that `uv sync` builds.
> **＋** `/hi`: the skill that opens a working session in the project.

> **when:**
> The person writes the clean version into a local folder by `uv run --project .guppi guppi ship --allow-draft <folder>`, adds that folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` in an empty project open in Claude Code, as `rule-plugin-install` sets it.

> **then:**
> Before it writes anything, `/guppi:install` runs `uv --version`.
> **＋** After it copies the files, it runs `uv sync --project .guppi` in the project, which builds the Python environment `.guppi/.venv/` before it tells the person to reopen Claude Code and type `/hi`.
> **＋** The hooks of the project find that environment built at the first `/hi`.
> **－** When `uv --version` fails, it says that GUPPI needs the tool `uv`, and that the person installs it and types `/guppi:install` again, writes nothing and stops.
> **－** When `uv sync --project .guppi` fails, it shows its output and stops, and does not tell the person to type `/hi`.

> **tasks:**
> - [ ] update `estimate-guppi-package-is-ready-after-the-install`
>   - set:
>     ```
>     status: pending
>     method: "by hand, after a tag prod-x.y.z stands in the history of HEAD: the agent writes the clean version into a local folder by uv run --project .guppi guppi ship --allow-draft; then, at a stop of Work Mode, the person adds that folder as a catalogue, installs the plugin guppi from it and, in an empty project on the machine with uv, types /guppi:install, reopens Claude Code there and types /hi; in an empty project with Claude Code started from a terminal whose PATH holds no folder of uv, types /guppi:install; in an empty project with Claude Code started from a terminal with UV_OFFLINE=1 and UV_CACHE_DIR set to an empty folder, types /guppi:install; the person's answer on the output of each install, the files of each project and .guppi/.venv/ of the project with uv, read against the Criterion; the copy and the project with uv may be those of the reading of estimate-plugin-install-writes-guppi-into-an-empty-project at the same commit"
>     ```
>   - change: `the Criterion replaced whole — the install comes from a local copy that guppi ship --allow-draft writes, not from the branch prod; the method makes uv missing by the PATH of a terminal, makes uv sync fail offline and reads the person's answer`
> - [ ] By hand, after the task of Case 841 that sets the tag `prod-0.2.0`: `uv run --project .guppi guppi ship --allow-draft <folder>` into an empty local folder outside the repository, and the parts of the readings of Cases 843 and 845 that the agent runs.
> - [ ] stop: before the push of the tag `prod-0.2.0` by the `stop:` task of Case 850, the one stop for every install by hand of this batch; the person adds that folder by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and, in one go, works in four empty projects: in the project on the machine with `uv`, types `/guppi:install`, reopens Claude Code there and types `/hi` (for Cases 843, 845 and 846); in a project with a `CLAUDE.md` of its own, types `/guppi:install` (for Case 843); in a project with Claude Code started from a terminal whose `PATH` holds no folder of `uv`, types `/guppi:install` (for Case 846); in a project with Claude Code started from a terminal with `UV_OFFLINE=1` and `UV_CACHE_DIR` set to an empty folder, types `/guppi:install` (for Case 846); then the person tells what each project showed; right after the installs, the output of `/guppi:install` and the files of the project with `uv` and of the project with a `CLAUDE.md` of its own are read against the Criterion of `estimate-plugin-install-writes-guppi-into-an-empty-project`, and the projects of Case 846 against the Criterion of `estimate-guppi-package-is-ready-after-the-install`.
> - [ ] read `estimate-guppi-package-is-ready-after-the-install`

> **ratification:**
> ```
> - decision[case 846][update][estimate-guppi-package-is-ready-after-the-install]{ref:rule-guppi-package}{supersedes:case 831}{supersedes:case 832}
> ```
