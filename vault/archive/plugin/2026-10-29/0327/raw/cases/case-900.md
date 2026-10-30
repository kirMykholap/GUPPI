## Case 900 — The install readings are taken up from the backlog

> **context:**
> Five install checks stand `pending` and put off in the backlog. Each needs a person to install GUPPI by hand, from a clean copy written by `guppi ship --allow-draft`, into an empty project. `decision-case-862` put off four of them: `estimate-git-context-offers-git-init`, `estimate-guppi-package-is-ready-after-the-install`, `estimate-plugin-install-offers-to-install-uv` and `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails`. `decision-case-885` put off `estimate-clean-branch-writes-the-session-files`. The events that the methods wait for have come. A tag `prod-x.y.z` stands in the history of HEAD, since `git tag --merged HEAD` prints `prod-0.2.0`, `prod-1` and `prod-2`. The librarian's runs that the methods name are done. So the readings can be taken in the Work Mode of this session. The person chose one Case for the five, one sub-case per Estimate. Each sub-case retires the defer of its Estimate by an `update` that names the page and carries one `{supersedes}` mark for each Case in its `deferred_by`, as `case-schema.md` sets it for a taken-up defer. `decided_on_its_page` of `.guppi/guppi/prespec.py`, which the check of this file and `/pre-spec` both call, counts only a decision line whose own slug is the page. The `ref` of a line does not count. `clear_deferred_by` of `.guppi/guppi/generate.py` drops a defer only from the pages that the superseding Case names. So `estimate-close-commits` and `estimate-spec-write-writes-a-defer` keep their defer by Case 885 and stay in the backlog, which the person chose. The pages `rule-clean-branch` and `rule-guppi-package` stand in the backlog on their own defers, and this Case leaves them there.
> Each sub-case is checked by its own Estimate. The `when` and `then` of each sub-case are the Criterion of that Estimate word for word. The `update` sets no `status` and no Criterion, so the Criterion and the `pending` status stand until the reading. By the person's choice, the readings run at one `stop:` task of Work Mode, in Case 900.2. Before it, the agent runs `test_ship.py -k skeleton` in the repository, since those tests build their own tree in a temporary folder and the clean copy holds no `test_ship.py`. It writes one fresh clean copy for the three `--check` commands that `estimate-clean-branch-writes-the-session-files` names, and a second fresh copy, in which no command runs, as the catalogue of the installs. Step 2 of `plugin/skills/install/SKILL.md` copies each file of the plugin but those under `.claude-plugin/`, `skills/` and `.git/`, so a Python environment that the `--check` commands may leave in their copy would reach the projects. It would then hide whether `uv sync` built `.guppi/.venv/`, or whether it failed offline. `rule-clean-branch` says that the clean version does not hold `.guppi/.venv/`. At the stop, the person makes three installs from the second copy. The first goes into a folder with no git on a machine with `uv`, for the checks of Cases 900.1, 900.2 and 900.3. The second is started from a terminal whose PATH holds no folder of `uv`, for Case 900.4. The third runs with `UV_OFFLINE=1` and an empty `UV_CACHE_DIR`, for Case 900.5. `rule-where-to-stop` makes a reading that only the person can take no stop, unless a task opens with `stop:`. The reading lines are taken from the person's report and the files of each folder. Frontier line A1 is the question of `estimate-guppi-package-is-ready-after-the-install`, and the reading of Case 900.3 answers it. `estimate-plugin-install-writes-guppi-into-an-empty-project` and `estimate-sprint-plugin-installs-as-a-plugin` may be read at the same installs, and they are not part of this Case.
> The frame showed a clash with Case 898.1 of this session. `ships` of `.guppi/guppi/ship.py` writes an Estimate into the clean copy when it stands `passed` and the copy writes its target. `rule-git-context` and `rule-guppi-package` carry `core: true`. So `estimate-git-context-offers-git-init` and `estimate-guppi-package-is-ready-after-the-install` reach the copy once they pass. Their methods build the copy by `uv run --project .guppi guppi ship --allow-draft`. `rule-clean-branch` says that an installed project gets no command `ship`. The method of the second one also points to `estimate-plugin-install-writes-guppi-into-an-empty-project`, whose target `rule-plugin-install` carries no `core`, so the copy does not hold it. The Criterion that Case 898.1 sets for `estimate-clean-branch-ships-neutral-texts` fails such a `method`. It passes a sentence that states its condition, such as where the module of the command `ship` stands. By the person's choice, Cases 900.1 and 900.3 set those two methods anew to state that condition, and the second one drops the pointer. Their steps stay the same. Each new method still opens with `by hand, after <event>:`, which `waits_for_an_event` of `.guppi/guppi/lint.py` accepts. It holds no `first … after the render`. `estimate-clean-branch-ships-neutral-texts` checks the two methods at its next reading, and its Criterion stands. The When of `estimate-guppi-package-is-ready-after-the-install` still names `guppi ship`. Under Case 898.1, that reading lists a Criterion sentence of a shipped Estimate for a later Case, and the sentence fails nothing. `estimate-clean-branch-writes-the-session-files`, `estimate-plugin-install-offers-to-install-uv` and `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails` target pages without `core`, so they never ship, and their methods stand.
> A Grep of `guppi-package-is-ready-after-the-install|git-context-offers-git-init` over `vault/wiki/` without `brief.md`, `log.md` and `backlog.md` printed `rule-git-context.md`, `rule-guppi-package.md` and `estimate-clean-branch-writes-the-session-files.md`. The two rules list the Estimates in `estimates`. The third names the reading of `estimate-git-context-offers-git-init` in its method. No hit states the method text that changes. A Grep of `wiki_root\(REPO|read_vault\(.*REPO|REPO / "vault"|ship\.ship\(REPO` over `.guppi/tests/` printed `test_ship.py`, `test_generate.py`, `test_guppi_package.py` and `test_schemas.py`. `test_generate.py` and `test_schemas.py` read only the `schema.yaml` files. `test_no_live_page_names_the_old_command_or_path_where_a_reword_changes_it` of `test_guppi_package.py` looks for `uv run guppi`, `uv run pytest` and the paths `guppi/` and `tests/`, and the new methods keep the commands and the paths of the old ones. The live build test of `test_ship.py` asserts no pointer on a page under `vault/wiki/estimates/`, and the new methods hold no case id.
> The check of this file noted that some `then` lines of Case 900.5 share words with lines of Cases 900.3 and 900.4. They stand. Each sub-case copies the Criterion of its own Estimate word for word, and the lines speak of different moments: a failed `uv sync`, a missing `uv` and an install that passes.

> **problem:**
> Five install checks wait in the backlog, though the events their methods wait for have come. No Case sets when their readings are taken. Two of them would also reach the clean copy with a method that cannot run in an installed project.

> **recommend:**
> - **What the methods of the two Estimates that ship once passed say**
>   - Recommended: (a) reword the two methods now, so that each states that it runs in a repository that holds the command `ship`, and the second drops its pointer to the Estimate that is not shipped; the steps, the Criterion and the `pending` status stand.
>   - Answer: agreed, (a).
> - **How the install readings run in Work Mode**
>   - Recommended: (a) one `stop:` task: the agent runs `test_ship.py -k skeleton` in the repository and the three `--check` commands over a fresh clean copy written for them alone, and writes a second fresh copy, in which no command runs, as the catalogue; then the person makes the three installs from that catalogue and reports, and the five readings are recorded.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: after the findings of `/pre-spec`, the person agreed that the item on how the install readings run should match the tasks of Case 900.2.
>   - Taken: the item now says that the skeleton tests run in the repository, that the `--check` commands run over a copy of their own, and that the installs take a second copy as the catalogue; the decision lines stand as they were.

### Case 900.1 — /hi outside a git repository offers git init

> **given:**
> `estimate-git-context-offers-git-init`: its defer is retired and its `method` is set anew.
> **＋** `rule-git-context`: the git step of `/hi`.
> **＋** `.claude/skills/hi/SKILL.md`: the skill that opens a session.
> **＋** `rule-skill-hi`: sets `/hi`.
> **＋** `rule-skill-sprint-open`: its hook asks for `/sprint-open`.
> **＋** `rule-default-mode`: sets the writes allowed before a ratified Case.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of a session.

> **when:**
> The person types `/hi` of `.claude/skills/hi/SKILL.md` in a project folder, and its `Branch:` line, which runs `uv run --project .guppi guppi gitstate` of `rule-git-context`, reads `none: this folder is no git repository`.

> **then:**
> Before `/sprint-open` and before the Frontier, the agent says that GUPPI works only in a git repository and asks the person whether it runs `git init -b main`.
> **＋** On the person's yes, the agent runs `git init -b main`, which Claude Code asks the person to allow, says that the repository is made, and tells the person to type `/hi` again.
> **＋** The next `/hi` prints `main` under `Branch:` and goes on as `rule-skill-hi` sets it, `/sprint-open` first when the hook of `rule-skill-sprint-open` asks for it.
> **＋** On the person's no, the agent tells the person to type `/hi` again after `git init -b main`.
> **－** After either answer, that `/hi` starts no `/sprint-open` and writes no `raw/<date>/<hi HHMM>/frontier.md`.
> **－** `git init -b main` is the one write before a ratified Case that `rule-default-mode` allows, and `allowed-tools` of `.claude/skills/hi/SKILL.md` does not name it.

> **tasks:**
> - [ ] update `estimate-git-context-offers-git-init`
>   - set:
>     ```
>     method: "by hand, after the librarian's run, in a repository that holds the module of the command ship: in an empty folder that is no git repository, GUPPI installed by /guppi:install from a copy that uv run --project .guppi guppi ship --allow-draft wrote into a local folder, Claude Code opened there, /hi typed and answered no, /hi typed again and answered yes, then /hi typed a third time, and the replies, the context of each /hi, the session folders and git branch --show-current read against the Criterion"
>     ```
>   - change: `the defer retired, the reading taken at the install stop of Work Mode; the method states that it runs where the command ship stands`
> - [ ] read `estimate-git-context-offers-git-init`

> **ratification:**
> ```
> - decision[case 900.1][update][estimate-git-context-offers-git-init]{ref:rule-git-context}{supersedes:case 862}
> ```

### Case 900.2 — The clean copy writes the session files

> **given:**
> `estimate-clean-branch-writes-the-session-files`: its defer is retired.
> **＋** `rule-clean-branch`: the command `guppi ship`, which writes the clean version.
> **＋** `.guppi/guppi/sprint.py`: its `closed_form` writes a closed sprint page.
> **＋** `vault/wiki/sprint.md`, `vault/wiki/backlog.md`, `vault/wiki/glossary.md`, `vault/wiki/brief.md` and `vault/wiki/log.md`: the session files the copy writes as skeletons.
> **＋** `rule-git-context`: the git step of `/hi`.
> **＋** `/sprint-open`: the skill that opens a sprint.
> **＋** `.guppi/tests/test_ship.py`: the tests of the command `ship`.
> **＋** `plugin/skills/install/SKILL.md`: the skill `/guppi:install` of the plugin `guppi`.

> **when:**
> `uv run --project .guppi guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.
> **＋** Or, in an empty project, the person installs the plugin `guppi` from such a copy, types `/guppi:install`, reopens Claude Code there and types `/hi`, and types `/hi` again after the git step of `rule-git-context` where the folder is no git repository.

> **then:**
> It writes `vault/wiki/sprint.md` as `closed_form` of `.guppi/guppi/sprint.py` writes it for the sprint `guppi`, so its first `## ` heading carries the mark of a closed sprint.
> **＋** It writes `vault/wiki/backlog.md` and `vault/wiki/glossary.md` as `guppi backlog` and `guppi glossary` write them over the clean version, by their own code.
> **＋** It writes a `vault/wiki/brief.md` whose `Cases` of its `## Next session` open with the line `open the next sprint — no sprint is open since the close of guppi`, and a `vault/wiki/log.md` that holds its heading and the paragraph under it alone.
> **＋** Over the clean version, `guppi sprint --check`, `guppi backlog --check` and `guppi glossary --check` print nothing and exit 0.
> **＋** In that project, the first `/hi` whose `Branch:` line, the output of `uv run --project .guppi guppi gitstate`, names a branch starts `/sprint-open` before the Frontier.
> **－** A `/hi` whose `Branch:` line reads `none: this folder is no git repository` is no part of this promise.
> **－** It writes no `sprint.md`, `backlog.md`, `brief.md`, `glossary.md` or `log.md` of the project it builds from.

> **tasks:**
> - [ ] update `estimate-clean-branch-writes-the-session-files`
>   - change: `the defer retired, the reading taken at the install stop of Work Mode`
> - [ ] by hand: `uv run --project .guppi pytest .guppi/tests/test_ship.py -k skeleton` in the repository; then `uv run --project .guppi guppi ship --allow-draft <folder>` into an empty temporary folder used only for the checks, and `uv run --project .guppi guppi sprint --check`, `uv run --project .guppi guppi backlog --check` and `uv run --project .guppi guppi glossary --check` run in that folder; each output kept for the readings of Case 900.
> - [ ] by hand: `uv run --project .guppi guppi ship --allow-draft <folder>` into a second empty temporary folder, the catalogue of the installs, in which no command runs, so that it holds no `.guppi/.venv/`.
> - [ ] stop: the person adds that second folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace`, and makes three installs by `/guppi:install`, each into its own empty folder: one with no git on a machine with `uv`, with Claude Code reopened, `/hi` answered no, `/hi` answered yes and `/hi` typed a third time; one with Claude Code started from a terminal whose PATH holds no folder of `uv`, with the offer answered no, then `/guppi:install` typed again and the offer answered yes, and `uv --version` run in a new terminal; one with Claude Code started from a terminal with `UV_OFFLINE=1` and `UV_CACHE_DIR` set to an empty folder; the person reports the replies and whether Claude Code asked, and the agent reads the files and folders of each project, for the readings of Case 900.
> - [ ] read `estimate-clean-branch-writes-the-session-files`

> **ratification:**
> ```
> - decision[case 900.2][update][estimate-clean-branch-writes-the-session-files]{ref:rule-clean-branch}{supersedes:case 885}
> ```

### Case 900.3 — The Python environment is ready after the install

> **given:**
> `estimate-guppi-package-is-ready-after-the-install`: its defer is retired and its `method` is set anew.
> **＋** `rule-guppi-package`: the package `guppi` in `.guppi/` and its Python environment `.guppi/.venv/`.
> **＋** `rule-plugin-install`: the skill `/guppi:install` and its catalogue.
> **＋** `rule-clean-branch`: the command `guppi ship`, which writes the clean version.
> **＋** `/plugin marketplace add <folder>`: the command of Claude Code that adds a catalogue.
> **＋** `/plugin install guppi@guppi-marketplace`: the command of Claude Code that installs the plugin.
> **＋** `/hi`: the skill that opens a session.

> **when:**
> The person writes the clean version into a local folder by `uv run --project .guppi guppi ship --allow-draft <folder>`, adds that folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` in an empty project open in Claude Code, as `rule-plugin-install` sets it.

> **then:**
> Before it writes anything, `/guppi:install` runs `uv --version`.
> **＋** After it copies the files, it runs `uv sync --project .guppi` in the project, which builds the Python environment `.guppi/.venv/` before it tells the person to reopen Claude Code and type `/hi`.
> **＋** The hooks of the project find that environment built at the first `/hi`.
> **－** Where `uv --version` passes, it asks nothing about `uv`.

> **tasks:**
> - [ ] update `estimate-guppi-package-is-ready-after-the-install`
>   - set:
>     ```
>     method: "by hand, after a tag prod-x.y.z stands in the history of HEAD, in a repository that holds the module of the command ship: the agent writes the clean version into a local folder by uv run --project .guppi guppi ship --allow-draft; then, at a stop of Work Mode, the person adds that folder as a catalogue, installs the plugin guppi from it and, in an empty project on the machine with uv, types /guppi:install, reopens Claude Code there and types /hi; the person's answer on the output of the install, the files of the project and its .guppi/.venv/, read against the Criterion; the copy and the project may be those of another install reading at the same commit"
>     ```
>   - change: `the defer retired, the reading taken at the install stop of Work Mode; the method states that it runs where the command ship stands and names no Estimate the clean version leaves out`
> - [ ] read `estimate-guppi-package-is-ready-after-the-install`

> **ratification:**
> ```
> - decision[case 900.3][update][estimate-guppi-package-is-ready-after-the-install]{ref:rule-guppi-package}{supersedes:case 862}
> ```

### Case 900.4 — The install offers to install uv

> **given:**
> `estimate-plugin-install-offers-to-install-uv`: its defer is retired.
> **＋** `rule-plugin-install`: renders the skill `/guppi:install`.
> **＋** `plugin/skills/install/SKILL.md`: the skill `/guppi:install` of the plugin `guppi`.
> **＋** `/hi`: the skill that opens a session.

> **when:**
> The person types `/guppi:install` of `plugin/skills/install/SKILL.md` in an empty project open in Claude Code, where `uv --version` fails.

> **then:**
> Before it writes anything, the agent says that GUPPI needs the tool `uv` and asks the person whether it installs `uv` now by the standalone installer of `uv` for the system: a PowerShell command on Windows, a shell command on macOS and Linux.
> **＋** On the person's no, it shows that command, says that the person installs `uv` with it and types `/guppi:install` again, and stops.
> **＋** On the person's yes, it runs that command, and then `uv --version` again.
> **＋** When `uv --version` then passes, it goes on with the install in the same session, and its last message tells the person to start Claude Code in the project from a new terminal and type `/hi`.
> **＋** When `uv --version` still fails, it says that this session of Claude Code does not find the new `uv`, and that the person opens a new terminal, starts Claude Code there and types `/guppi:install` again, and stops.
> **－** When the installer fails or Claude Code does not run it, the agent shows its output and the command, says that the person installs `uv` with it and types `/guppi:install` again, and stops.
> **－** It writes nothing into the project before `uv --version` passes.

> **tasks:**
> - [ ] update `estimate-plugin-install-offers-to-install-uv`
>   - change: `the defer retired, the reading taken at the install stop of Work Mode`
> - [ ] read `estimate-plugin-install-offers-to-install-uv`

> **ratification:**
> ```
> - decision[case 900.4][update][estimate-plugin-install-offers-to-install-uv]{ref:rule-plugin-install}{supersedes:case 862}
> ```

### Case 900.5 — The install undoes the copy when uv sync fails

> **given:**
> `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails`: its defer is retired.
> **＋** `rule-plugin-install`: renders the skill `/guppi:install`.
> **＋** `plugin/skills/install/SKILL.md`: the skill `/guppi:install` of the plugin `guppi`.
> **＋** `.guppi/`: the folder of the code of GUPPI in the project.
> **＋** `.guppi/.venv/`: the Python environment that `uv sync` builds.
> **＋** `/hi`: the skill that opens a session.

> **when:**
> The person types `/guppi:install` of `plugin/skills/install/SKILL.md` in an empty project open in Claude Code, where `uv --version` passes, and `uv sync --project .guppi` fails after the copy, such as with no network and an empty cache of `uv`.

> **then:**
> The agent shows the output of `uv sync --project .guppi`.
> **＋** It deletes each file it copied into the project and each folder it made there, `.guppi/` with `.guppi/.venv/` included, so that the project holds only what it held before `/guppi:install`.
> **＋** It says that the install did not finish and that the project stands as before, and that the person types `/guppi:install` again once the cause that the output shows is fixed, and stops.
> **－** It does not tell the person to run `uv sync`, to reopen Claude Code or to type `/hi`.
> **－** It deletes no file or folder that stood in the project before `/guppi:install`, and nothing in the folder of the plugin.

> **tasks:**
> - [ ] update `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails`
>   - change: `the defer retired, the reading taken at the install stop of Work Mode`
> - [ ] read `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails`

> **ratification:**
> ```
> - decision[case 900.5][update][estimate-plugin-install-undoes-the-copy-when-uv-sync-fails]{ref:rule-plugin-install}{supersedes:case 862}
> ```
