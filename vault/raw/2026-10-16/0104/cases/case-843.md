## Case 843 — The install by hand reads the plugin install again

> **context:**
> `estimate-plugin-install-writes-guppi-into-an-empty-project` checks two things. First, that `guppi ship` writes the skill `install` into the clean version. Second, that `/guppi:install` copies GUPPI into an empty project and writes nothing into a project that already holds one of its files. Its `method` runs `test_ship.py -k plugin_skill`, and then, by hand, a local copy from `guppi ship --allow-draft`, an add of that copy as a catalogue, an install of the plugin and `/guppi:install` in two empty projects, the second with a `CLAUDE.md` of its own. The part by hand never ran: `run` in `.guppi/guppi/ship.py` returns 1 before it writes when `version` finds no tag `prod-x.y.z` merged into HEAD, and prints `ship: no tag prod-x.y.z in the history of HEAD; nothing written`. The context of `decision-case-831` quotes that line from the `/hi` of session 1959, and `git tag -l` printed only `prod-1` and `prod-2` this session. The Retro of session 1739 set the page `failed` unread, and case 831 deferred it. Case 841 of this session sets the tag `prod-0.2.0` locally as the first task of Work Mode. Work Mode runs the tasks in the order the Spec holds them, so the push of the tag to GitHub is the `stop:` task of Case 850, `git push origin prod-0.2.0`, after the one `stop:` task of Case 846. Case 846 holds the one `stop:` task in which the person does every install by hand: the shared empty project with `uv`, the second empty project with a `CLAUDE.md` of its own that this Case reads, and the projects that Case 846 alone reads. Cases 845 and 846 read the same local copy and the same shared empty project. The `method` of the page stands: it names the steps by hand, not the Case that runs them, and the `stop:` task of Case 846 runs those steps. A task of this Case that read the two projects would stand in the Spec before that `stop:` task, and so would run before the install; so this Case holds no task by hand, and Case 846 needs its `stop:` task to read, right after the installs, the output of `/guppi:install` and the files of the shared empty project and of the second project against the Criterion of `estimate-plugin-install-writes-guppi-into-an-empty-project`, before the push of Case 850.
>
> The Criterion of the page still matches the skill: steps 2 to 5 of `plugin/skills/install/SKILL.md`, which equals the Render of `rule-plugin-install`, list and copy each file but those under `.claude-plugin/`, `skills/` and `.git/`, stop on a file that stands, and check the copy. Its steps on `uv` fall under the last exception line of the Criterion and are the promise of `estimate-guppi-package-is-ready-after-the-install`, which Case 846 reads. The rule that governs the change is the passage of `case-schema.md` on an `update` of an Estimate: it carries `set: {status: pending}` and `change`, and the scripts replace the Criterion with the Case's `when` and `then`. So this Case's `when` and `then` are the Criterion of the page word for word, and the promise stays as it was signed in case 818.1; `purpose` and `method` state that same promise and stand. As `case-schema.md` sets it for a deferred decision taken up, the decision line carries `{supersedes:case 831}`, and `generate` clears that defer from this page alone; Cases 842 and 846 take up the other two pages of case 831.
>
> The `## Readings at the close` of `vault/wiki/brief.md` reports `uv run --project .guppi guppi test`: 1 failed, 1714 passed, 6 skipped, 1 deselected, the failure in `test_guppi_package.py`; its `## Readings due` says `guppi test` ran `.guppi/tests/test_ship.py` with no failure. A Grep of `estimate-plugin-install-writes-guppi-into-an-empty-project` over `vault/wiki/` printed `brief.md`, `backlog.md`, `log.md` and `rules/rule-plugin-install.md`; the line of `rule-plugin-install` lists the Estimate and stays true, and the line of `backlog.md` is written again by `guppi backlog` at the librarian's run. The same Grep over `.claude/` printed nothing. The live test `test_no_live_page_names_the_old_command_or_path_where_a_reword_changes_it` of `.guppi/tests/test_guppi_package.py` reads each live page; this Case leaves the body of the page as it stands, so that test answers on it as before.

> **problem:**
> The promise of the plugin install was never read, since no local copy could be built with no tag `prod-x.y.z`; once Case 841 sets the tag, the page must come back to `pending` and be read by its `method`.

> **recommend:**
> - **How does the Estimate come back for a new reading?**
>   - Recommended: (a) set it to pending, with the same Criterion; one `update` also takes back the defer.
>   - Answer: agreed, (a).
> - **Does this reading share one install by hand with Cases 845 and 846?**
>   - Recommended: (a) one copy and one first project for all three; this Case adds only the second project with its own `CLAUDE.md`.
>   - Answer: agreed, (a).
> - **Does the reading run before the tag is pushed to GitHub?**
>   - Recommended: (a) before the push, so that a failed install can still stop the push.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: Work Mode runs the tasks in Spec order, so a push in Case 841 would run before this reading; the person agreed that one `stop:` task of Case 846 holds every install by hand, this Case's second project included, and that the push moves to Case 850.
>   - Taken: the `stop:` task of this Case is gone; the reading of the two projects against this Criterion moves into the `stop:` task of Case 846, which stands before the push of Case 850.

> **given:**
> `estimate-plugin-install-writes-guppi-into-an-empty-project`: set to `pending` with its Criterion as it stands.
> **＋** `rule-plugin-install`: the rule of the skill `install`, the target of the Estimate.
> **＋** `plugin/skills/install/SKILL.md`: the skill `install` that the Render of `rule-plugin-install` writes.
> **＋** `rule-clean-branch`: the rule of the clean version that `guppi ship` builds.
> **＋** `.guppi/guppi/ship.py`: the build of the clean version, which reads the tag.
> **＋** `.guppi/tests/test_ship.py`: the tests of the build, with those of the skill `install`.
> **＋** `/plugin marketplace add <folder>`: the command of Claude Code that adds the local copy as a catalogue.
> **＋** `/plugin install guppi@guppi-marketplace`: the command of Claude Code that installs the plugin from that catalogue.
> **＋** `/guppi:install`: the skill `install` as the person types it.
> **＋** `/hi`: the skill that opens a session in the new project.
> **＋** `vault/`: the folder of the vault, whose files `guppi ship --check` does not judge in place.
> **＋** `vault/wiki/`: the folder of the pages that the install copies.
> **＋** `.claude-plugin/`: the folder of the plugin's own manifest, which the install does not copy.
> **＋** `.git/`: the folder of git, which the install does not copy.
> **＋** `.claude/settings.json`: the settings of the harness, one of the files the install copies.
> **＋** `.claude/skills/`: the folder of the skills the install copies.

> **when:**
> `uv run --project .guppi guppi ship <folder>` builds the clean version, as `rule-clean-branch` sets it, and `uv run --project .guppi guppi ship --check` judges the working tree.
> **＋** The person writes the clean version into a local folder by `uv run --project .guppi guppi ship --allow-draft <folder>`, adds that folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` in the project open in Claude Code, as `rule-plugin-install` sets it.

> **then:**
> `uv run --project .guppi guppi ship <folder>` writes `plugin/skills/install/SKILL.md` to `skills/install/SKILL.md` of the clean version and cleans it like each other file it writes, and the clean version holds no file under `plugin/skills/`.
> **＋** `uv run --project .guppi guppi ship --check` judges `plugin/skills/install/SKILL.md` in place, as it judges each other file outside `vault/`.
> **＋** The installed plugin offers the skill `install`, which the person types as `/guppi:install`.
> **＋** In a project that holds none of the files it would write, `/guppi:install` copies each file of the plugin to the same path in the project, but those under `.claude-plugin/`, `skills/` and `.git/`, such as `CLAUDE.md`, `.claude/settings.json`, the code under `.guppi/` and the pages under `vault/wiki/`.
> **＋** It checks that each copied file stands, and its last message tells the person to reopen Claude Code in the project and type `/hi`.
> **－** In a project where one or more of those files already stand, it lists them, writes nothing and stops.
> **－** It writes nothing into the folder of the plugin, and runs no `guppi` command and no `git` command.
> **－** The skills it copies under `.claude/skills/` keep their bare names, such as `hi`.
> **－** Which files a new project needs, and what the install does about `uv` and the Python environment under `.guppi/`, are no part of this promise.

> **tasks:**
> - [ ] update `estimate-plugin-install-writes-guppi-into-an-empty-project`
>   - set: `{status: pending}`
>   - change: `set to pending with its Criterion unchanged, for a reading once a tag prod-x.y.z stands`
> - [ ] `uv run --project .guppi pytest .guppi/tests/test_ship.py -k plugin_skill`
> - [ ] read `estimate-plugin-install-writes-guppi-into-an-empty-project`

> **ratification:**
> ```
> - decision[case 843][update][estimate-plugin-install-writes-guppi-into-an-empty-project]{ref:rule-plugin-install}{supersedes:case 831}
> ```
