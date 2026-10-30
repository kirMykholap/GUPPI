## Case 941 — Work Mode stops for the install by hand into five projects

> **context:**
> Four Estimates wait on an install by hand from a clean copy: `estimate-plugin-install-sets-aside-the-files-of-the-project`, `estimate-plugin-install-writes-guppi-into-an-empty-project` and `estimate-plugin-install-runs-no-hook-before-uv-sync`, of `rule-plugin-install`, and `estimate-guppi-package-is-ready-after-the-install`, of `rule-guppi-package`. Each `method` writes the clean version by `uv run --project .guppi guppi ship --allow-draft`, adds it as a catalogue by `/plugin marketplace add`, installs it by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` in a test project. The method of `estimate-guppi-package-is-ready-after-the-install` says that the person does this at a stop of Work Mode and that its copy and project may be those of `estimate-plugin-install-runs-no-hook-before-uv-sync`. Their event has come: the brief reports the librarian's run of session 1713 and that `git tag --merged HEAD` prints `prod-0.2.0`. The methods name five projects. The first is an empty project, for the copy, the hooks before `uv sync`, and the reopen and `/hi`. The second is an empty project with Claude Code started with `UV_OFFLINE=1` and `UV_CACHE_DIR` set to an empty folder. The third holds a `CLAUDE.md`, a `.claude/settings.json` with a hook and a `.gitattributes` of its own. The fourth is such a project, offline. The fifth holds a file of its own under `vault/`. `where-to-stop.md` lets Work Mode stop for the person only on its conditions, and the fourth condition is a task of the Spec whose text opens with `stop:`. A Grep of `stop:` over `vault/raw/2026-10-30/2005/cases/` printed `vault/raw/2026-10-30/2005/cases/case-941.md` alone, the file of this Case, so no other Case of this session holds such a task.
>
> I read `run`, `drafts` and `version` of `.guppi/guppi/ship.py` whole. A build into a folder that is not empty writes nothing. With `--allow-draft`, the lines on the draft pages with `core: true` are printed and set no exit code, and the copy is written when a tag `prod-x.y.z` stands in the history of HEAD. The person chose to take all four readings in this session, with the copy written by the agent, one stop, and the readings after the person's word. The decision lines name the two rules by an `update` with only `change`. `.claude/skills/work/SKILL.md` leaves to Retro the reading of an Estimate that this session creates or updates; so the four Estimates stay out of the decision lines, and the three Work readings run in Work Mode after the last task, in the order of `frontier.md`. I read `names_a_part` and `lift_criterion` of `.guppi/guppi/materialize.py`: an `update` of a rule is no Estimate entry, so nothing is lifted and no status is set. No text of either rule changes, so no rendered file and no test that reads one live changes.
>
> The person chose the four Estimates as the check of this Case. Their Criteria stand, since this Case changes neither the install nor its rules. `estimate-where-to-stop-stops-only-on-its-conditions`, `passed`, already promises that the agent stops before a task that opens with `stop:` and runs it after the person's word, and its Criterion stands. The Claude Code page https://code.claude.com/docs/en/plugin-marketplaces says that one user cannot have two marketplaces with the same name, and that `claude plugin marketplace remove <name>` removes the marketplace and uninstalls its plugins. So the steps first remove a `guppi-marketplace` left by an earlier install. `estimate-sprint-plugin-installs-as-a-plugin` also reads an install into an empty project with `/hi`. Its target is the live sprint page, and `.claude/skills/hi/SKILL.md` makes such an Estimate wait for the Retro of the session that finishes the work of the sprint. Item C1 of the clean branch is still open, so that Estimate stays out. Case 939 runs `guppi ship --allow-draft --review` at Retro into an empty folder of its own, so the two builds share no folder. The ledger of this session holds no `error` lesson, so no line carries `{addresses:...}`.

> **problem:**
> Four install readings are due, and each needs the person to install by hand. No task of the Spec makes Work Mode stop for that, so without one the run goes on to Retro and the readings go to the handoff unread.

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

> **given:**
> `rule-plugin-install`: the install the Work readings check; an `update` with only `change`.
> **＋** `rule-guppi-package`: the rule of the Python environment after the install; an `update` with only `change`.
> **＋** `.guppi/guppi/ship.py`: `guppi ship --allow-draft`, which writes the clean version.
> **＋** `plugin/skills/install/SKILL.md`: the skill `/guppi:install` that the person types.
> **＋** `rule-where-to-stop`: sets the stop before a task that opens with `stop:`.
> **＋** `.claude/skills/work/SKILL.md`: takes the Work readings after the last task.
> **＋** `estimate-guppi-package-is-ready-after-the-install`: the reading by the person's answer.

> **when:**
> In Work Mode of the session, the agent writes the clean version by `uv run --project .guppi guppi ship --allow-draft <folder>` of `.guppi/guppi/ship.py` into a new empty folder outside the repository, makes the five test projects outside the repository, and reaches the `stop:` task of this Case.

> **then:**
> Before the stop, each test project holds only the files that its method names, and the agent records what each holds.
> **＋** The agent stops as `rule-where-to-stop` sets it, and its reply gives the person the steps for each project: the folder, how to start Claude Code there, offline where the method says so, the commands of the catalogue, the install and `/guppi:install`, and what to run after.
> **＋** Where a catalogue `guppi-marketplace` already stands from an earlier install, the first step removes it by `claude plugin marketplace remove guppi-marketplace`.
> **＋** The reply puts the question of `estimate-guppi-package-is-ready-after-the-install` on the first empty project, after the person reopens Claude Code there and opens a working session.
> **＋** After the person's word, the run goes on, and the Work readings of `.claude/skills/work/SKILL.md` read the transcripts and the files of the projects against the Criteria of the Estimates of `rule-plugin-install`.
> **－** The agent adds no catalogue, installs no plugin and types no `/guppi:install` itself, and deletes no folder outside the repository.
> **－** No text of `rule-plugin-install` or `rule-guppi-package` changes, and no Estimate of either changes its Criterion or its status by this Case.

> **tasks:**
> - [ ] update `rule-plugin-install`
>   - change: `the install by hand of its Work readings taken at a stop of Work Mode of session 2005`
> - [ ] update `rule-guppi-package`
>   - change: `the install by hand of its reading taken at a stop of Work Mode of session 2005`
> - [ ] `uv run --project .guppi guppi ship --allow-draft <folder>` into a new empty folder outside the repository.
> - [ ] The five test projects made outside the repository, the files of each as its method names them, and what each holds recorded.
> - [ ] stop: in Work Mode, the person installs the clean copy into the five projects by the steps the agent gives, and answers the question of `estimate-guppi-package-is-ready-after-the-install`.

> **ratification:**
> ```
> - decision[case 941][update][rule-plugin-install]{ref:rule-plugin-install}
> - decision[case 941][update][rule-guppi-package]{ref:rule-guppi-package}
> ```
