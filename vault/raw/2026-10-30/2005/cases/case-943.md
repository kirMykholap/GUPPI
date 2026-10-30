## Case 943 — Work Mode stops for the install by hand into five projects, and the agent writes the copy in two checks

> **context:**
> Four Estimates wait on an install by hand from a clean copy: `estimate-plugin-install-sets-aside-the-files-of-the-project`, `estimate-plugin-install-writes-guppi-into-an-empty-project` and `estimate-plugin-install-runs-no-hook-before-uv-sync`, of `rule-plugin-install`, and `estimate-guppi-package-is-ready-after-the-install`, of `rule-guppi-package`. Each `method` writes the clean version by `uv run --project .guppi guppi ship --allow-draft`, adds it as a catalogue by `/plugin marketplace add`, installs it by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` in a test project. The method of `estimate-guppi-package-is-ready-after-the-install` says that the person does this at a stop of Work Mode and that its copy and project may be those of `estimate-plugin-install-runs-no-hook-before-uv-sync`. Their event has come: the brief reports the librarian's run of session 1713 and that `git tag --merged HEAD` prints `prod-0.2.0`. The methods name five projects. The first is an empty project, for the copy, the hooks before `uv sync`, and the reopen and `/hi`. The second is an empty project with Claude Code started with `UV_OFFLINE=1` and `UV_CACHE_DIR` set to an empty folder. The third holds a `CLAUDE.md`, a `.claude/settings.json` with a hook and a `.gitattributes` of its own. The fourth is such a project, offline. The fifth holds a file of its own under `vault/`. `where-to-stop.md` lets Work Mode stop for the person only on its conditions, and the fourth condition is a task of the Spec whose text opens with `stop:`.
>
> I read `run`, `drafts` and `version` of `.guppi/guppi/ship.py` whole. A build into a folder that is not empty writes nothing. With `--allow-draft`, the lines on the draft pages with `core: true` are printed and set no exit code, and the copy is written when a tag `prod-x.y.z` stands in the history of HEAD. The person chose to take all four readings in this session, with the copy written by the agent, one stop, and the readings after the person's word. The Claude Code page https://code.claude.com/docs/en/plugin-marketplaces says that one user cannot have two marketplaces with the same name, and that `claude plugin marketplace remove <name>` removes the marketplace and uninstalls its plugins. So the steps first remove a `guppi-marketplace` left by an earlier install.
>
> This Case replaces Case 941, which was ratified with the stop alone and the four Criteria kept. A finding of `/pre-spec` showed that two Criteria say that the person writes the copy, while the agent writes it. In `estimate-plugin-install-writes-guppi-into-an-empty-project` this is a `＋` line of its When, and in `estimate-guppi-package-is-ready-after-the-install` it is its When; the `method` of the second already says that the agent writes it. The person chose to replace both Criteria whole, with the agent as the one who writes the copy and the rest as it stands, and to build Case 941 again under a new number with sub-cases. The rule that governs this is the form of a promise in `case-schema.md`: a promise changes only by a Criterion replaced whole. So Cases 943.2 and 943.3 replace each Criterion whole and set each Estimate `pending`. Each `method` waited for the librarian's run of the session that sets its Criterion; once this session sets it, that wait would move past this session. So each `method` is set anew, with the reading at Retro of this session, as the person chose. Each `purpose` speaks of what the install does, not of who writes the copy, so it stands. `.claude/skills/work/SKILL.md` leaves to Retro the reading of an Estimate that this session creates or updates. So these two are read at Retro, against the Spec that holds their new Criteria. The two other Estimates are still read in Work Mode after the last task. Case 943.1 names the two rules by an `update` with only `change`. I read `names_a_part` and `lift_criterion` of `.guppi/guppi/materialize.py`: an `update` of a rule is no Estimate entry, so nothing is lifted and no status is set.
>
> `estimate-where-to-stop-stops-only-on-its-conditions` stands `passed`. It already promises that the agent stops before a task that opens with `stop:` and runs it after the person's word, so its Criterion stands. The Criteria of `estimate-plugin-install-sets-aside-the-files-of-the-project` and `estimate-plugin-install-runs-no-hook-before-uv-sync` do not say who writes the copy, so they stand. `estimate-sprint-plugin-installs-as-a-plugin` also reads an install into an empty project with `/hi`. Its target is the live sprint page, and `.claude/skills/hi/SKILL.md` makes such an Estimate wait for the Retro of the session that finishes the work of the sprint. Item C1 of the clean branch is still open, so that Estimate stays out. I read the finished file of Case 939 whole. It runs `guppi ship --allow-draft --review` at Retro into an empty temporary folder of its own, so the two builds share no folder. It also replaces the sentence of `rule-clean-branch` on the uses of `--allow-draft`, and its new sentence still names the install by hand from that folder, which is what this Case does. This Case names `rule-clean-branch` only as the rule of the clean version and changes none of its text, so the two Cases need no change against each other. The ledger of this session holds no `error` lesson, so no line carries `{addresses:...}`.

> **problem:**
> Four install readings are due, and each needs the person to install by hand. No task of the Spec makes Work Mode stop for that, so without one the run goes on to Retro and the readings go to the handoff unread. Two of their Criteria also say that the person writes the clean copy, while the agent writes it.

> **recommend:**
> - **Which pages does the Case name?**
>   - Recommended: (a) the two rules the checks belong to, by an `update` with only `change`.
>   - Answer: agreed, (a).
> - **Who makes the five test projects?**
>   - Recommended: (a) the agent, before the stop.
>   - Answer: agreed, (a).
> - **Which check closes the Case?**
>   - Recommended: (a) the four install checks, their wording kept.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: a finding of `/pre-spec` — two Criteria say that the person writes the clean copy; the person agreed that the Case replaces both whole, with the agent as the one who writes it, and that Retro reads both against the Spec.
>   - Taken: Cases 943.2 and 943.3 replace those Criteria whole and set each `method` anew for Retro.
> - **Where do the two rewritten checks go?**
>   - Recommended: (a) Case 941 built again under a new number, with sub-cases.
>   - Answer: agreed, (a).

### Case 943.1 — Work Mode stops for the install by hand into five projects

> **given:**
> `rule-plugin-install`: the install the readings check; an `update` with only `change`.
> **＋** `rule-guppi-package`: the rule of the Python environment after the install; an `update` with only `change`.
> **＋** `.guppi/guppi/ship.py`: `guppi ship --allow-draft`, which writes the clean version.
> **＋** `plugin/skills/install/SKILL.md`: the skill `/guppi:install` that the person types.
> **＋** `rule-where-to-stop`: sets the stop before a task that opens with `stop:`.
> **＋** `.claude/skills/work/SKILL.md`: takes the readings after the last task.
> **＋** `estimate-guppi-package-is-ready-after-the-install`: the reading by the person's answer.

> **when:**
> In Work Mode of the session, the agent writes the clean version by `uv run --project .guppi guppi ship --allow-draft <folder>` of `.guppi/guppi/ship.py` into a new empty folder outside the repository, makes the five test projects outside the repository, and reaches the `stop:` task of this Case.

> **then:**
> Before the stop, each test project holds only the files that its method names, and the agent records what each holds.
> **＋** The agent stops as `rule-where-to-stop` sets it, and its reply gives the person the steps for each project: the folder, how to start Claude Code there, offline where the method says so, the commands of the catalogue, the install and `/guppi:install`, and what to run after.
> **＋** Where a catalogue `guppi-marketplace` already stands from an earlier install, the first step removes it by `claude plugin marketplace remove guppi-marketplace`.
> **＋** The reply puts the question of `estimate-guppi-package-is-ready-after-the-install` on the first empty project, after the person reopens Claude Code there and opens a working session.
> **＋** After the person's word, the run goes on, and the readings that `.claude/skills/work/SKILL.md` sets read the transcripts and the files of the projects against the Criteria of the Estimates of `rule-plugin-install` and `rule-guppi-package`.
> **－** The agent adds no catalogue, installs no plugin and types no `/guppi:install` itself, and deletes no folder outside the repository.
> **－** No text of `rule-plugin-install` or `rule-guppi-package` changes.

> **tasks:**
> - [ ] update `rule-plugin-install`
>   - change: `the install by hand of its readings taken at a stop of Work Mode of session 2005`
> - [ ] update `rule-guppi-package`
>   - change: `the install by hand of its reading taken at a stop of Work Mode of session 2005`
> - [ ] `uv run --project .guppi guppi ship --allow-draft <folder>` into a new empty folder outside the repository.
> - [ ] The five test projects made outside the repository, the files of each as its method names them, and what each holds recorded.
> - [ ] stop: in Work Mode, the person installs the clean copy into the five projects by the steps the agent gives, and answers the question of `estimate-guppi-package-is-ready-after-the-install`.

> **ratification:**
> ```
> - decision[case 943.1][update][rule-plugin-install]{ref:rule-plugin-install}{supersedes:case 941}
> - decision[case 943.1][update][rule-guppi-package]{ref:rule-guppi-package}{supersedes:case 941}
> ```

### Case 943.2 — The check of the copy into an empty project names the agent as the one who writes the copy

> **given:**
> `estimate-plugin-install-writes-guppi-into-an-empty-project`: its Criterion is replaced whole and its `method` set anew.
> **＋** `.guppi/guppi/ship.py`: `uv run --project .guppi guppi ship --allow-draft <folder>` and `uv run --project .guppi guppi ship --check`.
> **＋** `plugin/skills/install/SKILL.md`: the skill `/guppi:install`, which `guppi ship` writes to `skills/install/SKILL.md` of the clean version.
> **＋** `rule-plugin-install`: sets the install, which leaves out the files of the plugin under `.claude-plugin/`, `skills/` and `.git/`.
> **＋** `vault/`: the vault of the project, whose pages under `vault/wiki/` the install copies.
> **＋** `.claude/settings.json` and `.claude/skills/`: the settings and the skills of the harness that the install copies.
> **＋** `rule-clean-branch`: sets the clean version.
> **＋** `/plugin marketplace add <folder>` and `/plugin install guppi@guppi-marketplace`: the commands of Claude Code that add the catalogue and install the plugin.
> **＋** `/hi`: the command that the last message of the install names.

> **when:**
> `uv run --project .guppi guppi ship --allow-draft <folder>` builds the clean version, as `rule-clean-branch` sets it, and `uv run --project .guppi guppi ship --check` judges the working tree.
> **＋** The agent writes the clean version into a local folder by `uv run --project .guppi guppi ship --allow-draft <folder>`; the person adds that folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` in the project open in Claude Code, as `rule-plugin-install` sets it.

> **then:**
> `uv run --project .guppi guppi ship --allow-draft <folder>` writes `plugin/skills/install/SKILL.md` to `skills/install/SKILL.md` of the clean version and cleans it like each other file it writes, and the clean version holds no file under `plugin/skills/`.
> **＋** `uv run --project .guppi guppi ship --check` judges `plugin/skills/install/SKILL.md` in place, as it judges each other file outside `vault/`.
> **＋** The installed plugin offers the skill `install`, which the person types as `/guppi:install`.
> **＋** In a project that holds none of the files it would write, `/guppi:install` copies each file of the plugin to the same path in the project, but those under `.claude-plugin/`, `skills/` and `.git/`, such as `CLAUDE.md`, `.claude/settings.json`, the code under `.guppi/` and the pages under `vault/wiki/`.
> **＋** It checks that each copied file stands, and its last message tells the person to reopen Claude Code in the project and type `/hi`.
> **－** It writes nothing into the folder of the plugin, and runs no `guppi` command and no `git` command.
> **－** The skills it copies under `.claude/skills/` keep their bare names, such as `hi`.
> **－** Which files a new project needs, what the install does about `uv` and the Python environment under `.guppi/`, and what it does with a file of the project that stands at one of its paths are no part of this promise.

> **tasks:**
> - [ ] update `estimate-plugin-install-writes-guppi-into-an-empty-project`
>   - set:
>     ```
>     status: pending
>     method: "uv run --project .guppi pytest .guppi/tests/test_ship.py -k plugin_skill; by hand, at Retro of the session that sets this Criterion, with a tag prod-x.y.z in the history of HEAD: the clean version written by the agent in Work Mode into a local folder by uv run --project .guppi guppi ship --allow-draft; at a stop of Work Mode, in an empty project, the person adds that folder as a catalogue by /plugin marketplace add, installs guppi by /plugin install guppi@guppi-marketplace and types /guppi:install; the files of the project read against those of the plugin and against the Criterion"
>     ```
>   - change: `the Criterion replaced whole — the agent writes the clean copy; the reading at Retro of the session that sets it`
> - [ ] read `estimate-plugin-install-writes-guppi-into-an-empty-project`

> **ratification:**
> ```
> - decision[case 943.2][update][estimate-plugin-install-writes-guppi-into-an-empty-project]{ref:rule-plugin-install}{supersedes:case 941}
> ```

### Case 943.3 — The check of the package after the install names the agent as the one who writes the copy

> **given:**
> `estimate-guppi-package-is-ready-after-the-install`: its Criterion is replaced whole and its `method` set anew.
> **＋** `rule-guppi-package`: the rule of the Python environment `.guppi/.venv/`.
> **＋** `.guppi/guppi/ship.py`: `uv run --project .guppi guppi ship --allow-draft <folder>`, which writes the clean version.
> **＋** `plugin/skills/install/SKILL.md`: the skill `/guppi:install`, which runs `uv --version` and `uv sync --project .guppi`.
> **＋** `rule-plugin-install`: sets the install.
> **＋** `/plugin marketplace add <folder>` and `/plugin install guppi@guppi-marketplace`: the commands of Claude Code that add the catalogue and install the plugin.
> **＋** `.claude/settings.json`: the file that holds the hooks of the project.
> **＋** `/hi`: the command that the install sends the person to.

> **when:**
> In the repository of GUPPI, the agent writes the clean version into a local folder by `uv run --project .guppi guppi ship --allow-draft <folder>`; the person adds that folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` in an empty project open in Claude Code, as `rule-plugin-install` sets it.

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
>     method: "by hand, at Retro of the session that sets this Criterion, with a tag prod-x.y.z in the history of HEAD: in the repository of GUPPI, the agent writes the clean version into a local folder by uv run --project .guppi guppi ship --allow-draft in Work Mode; then, at a stop of Work Mode, the person adds that folder as a catalogue, installs the plugin guppi from it and, in an empty project on the machine with uv, types /guppi:install, reopens Claude Code there and types /hi; the person's answer on the output of the install, the order of its steps, the files of the project and its .guppi/.venv/, read against the Criterion; the copy and the project may be those of the reading of estimate-plugin-install-runs-no-hook-before-uv-sync"
>     ```
>   - change: `the Criterion replaced whole — the agent writes the clean copy; the reading at Retro of the session that sets it`
> - [ ] read `estimate-guppi-package-is-ready-after-the-install`

> **ratification:**
> ```
> - decision[case 943.3][update][estimate-guppi-package-is-ready-after-the-install]{ref:rule-guppi-package}{supersedes:case 941}
> ```
