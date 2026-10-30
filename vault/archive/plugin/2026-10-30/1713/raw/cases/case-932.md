## Case 932 — An existing project sets its own files aside to install GUPPI

> **context:**
> `/guppi:install` copies the files of GUPPI into the project open in Claude Code. Today, step 3 of its skill, `plugin/skills/install/SKILL.md`, lists each file of the install that already stands in the project, writes nothing and stops. So a project with its own `CLAUDE.md` or `.claude/settings.json` cannot install GUPPI at all. Case 911 put this off with the words that it lets GUPPI install into an existing project that holds its own settings, hooks and `CLAUDE.md`. A plain copy over those files is no answer. `CLAUDE.md` and `.claude/settings.json` are rendered whole from the rule pages `rule-claude-md` and `rule-settings`, so any extra text of the project there is lost at the first render. `rule-claude-md` keeps any line nobody ratified out of the system prompt, and `rule-hook-registry` keeps any hook from being registered by hand. The settings documentation of Claude Code (https://code.claude.com/docs/en/settings) names one shared project file, `.claude/settings.json`, and a personal `.claude/settings.local.json` that stays out of git, so the settings of a project cannot move to a second shared file. The memory documentation (https://code.claude.com/docs/en/memory) says that a `CLAUDE.md` in a subfolder loads on demand when Claude works with files there, so the set-aside files take `.set-aside` on their names, which no file of Claude Code carries.
> The person chose that the install sets the clashing files aside and that the setup Case of `rule-morph` takes them in at the first `/hi`. Case 932.1 changes the install, and Case 932.2 changes the setup Case. The setup step of `rule-morph` is not built yet. As the Purpose of `rule-clean-branch` sets it, `guppi ship` writes nothing while a page with `core: true` stands `draft`, and `rule-morph` is such a page. So no project gets this install from the branch `prod` before the setup step is built, and the person chose no temporary step for installs by hand. The take-in also covers `.gitattributes` and `.github/workflows/checks.yml`. A Grep for `^governs:.*(\.gitattributes|checks\.yml)` over `vault/wiki/` printed nothing, and a Grep for `^(code_ref|implementation_ref|governs):.*(gitattributes|checks\.yml|\.github)` over `vault/wiki/` printed `rules/rule-clean-branch.md` and `rules/rule-github-repository.md`, whose `implementation_ref` lists `.github/workflows/checks.yml` as code. No page renders those two files, so a task of the setup Case writes a kept part into them.
> Of the Estimates of `rule-plugin-install`, two promise the refusal in a `－` line: `estimate-plugin-install-writes-guppi-into-an-empty-project` and `estimate-plugin-install-runs-no-hook-before-uv-sync`. Cases 932.3 and 932.4 replace each Criterion whole without that line, and add a `－` line that a file of the project at a path of the install is no part of its promise; the person chose two parts, and the check of the case file asked that these two Criteria stand in sub-cases of their own, since each is a promise of its own. The purpose of the first names the refusal, and its method reads a second project with a `CLAUDE.md` of its own, so both are set anew. Its When and Then name `guppi ship --allow-draft <folder>`, since `rule-clean-branch` sets it that `guppi ship <folder>` writes nothing while a page with `core: true` stands `draft`, and its method names the tag `prod-x.y.z` that `guppi ship <folder>` needs, as that rule sets it; both were findings of `/pre-spec`. The purpose and method of the second speak of empty projects and stand. `estimate-plugin-install-offers-to-install-uv` and `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails` speak of an empty project, where nothing is set aside, and stand. The new Estimate of Case 932.1 checks the undo for a project with files set aside. In `estimate-morph-sets-up-the-project-at-the-first-hi`, the purpose and the `－` line say that the settings change only by the copy of `/guppi:install` and the render, and the setting aside of the project's `.claude/settings.json` is a move, not a copy; a finding of `/pre-spec` named it, so Case 932.5 replaces its Criterion whole with the setting aside beside the copy and sets its purpose anew, and its method, which waits for the build of the setup step, stands. Its line that the setup step reads no code of the project stands too, since the set-aside files are instructions and settings, not the code of the project. In the Purpose of `rule-morph`, the sentence that no settings file changes but by the copy of `/guppi:install` and the render would be made false by the setting aside, so Case 932.2 rewords it. A Grep for `guppi:install` over `vault/wiki/` printed `log.md`, `brief.md`, `sprint.md`, `entities/entity-sprint-plugin.md`, `lessons/lesson-hi-fails-outside-a-git-repository.md`, `lessons/lesson-plugin-install-hooks-of-the-copy-run-at-once.md`, `estimates/estimate-clean-branch-writes-the-session-files.md`, `rules/rule-plugin-install.md`, `rules/rule-morph.md`, `estimates/estimate-git-context-offers-git-init.md`, `estimates/estimate-guppi-package-is-ready-after-the-install.md`, `estimates/estimate-morph-sets-up-the-project-at-the-first-hi.md`, `estimates/estimate-sprint-plugin-installs-as-a-plugin.md` and the four Estimates of `rule-plugin-install`. Beside the pages this Case changes, the Estimates there speak of an empty project and stand; the two lessons record past events and were not read. The line of `entity-sprint-plugin` lists what remains of `rule-morph`, the setup skill among it, and stands. A Grep for `plugin/skills/install|rule-plugin-install|rule-morph|estimate-plugin-install|estimate-morph` over `.guppi/tests/` printed `test_ship.py`, whose hit is a sample string of an error, so no test reads these texts live. A Grep for `guppi-set-aside` over the repository outside `vault/raw/` printed nothing, so no step reads that folder yet. The new slugs are free: a Glob for each over `vault/wiki/**` printed nothing. Case 932.1 carries `{supersedes:case 911}`, the one defer of `rule-plugin-install`. The ledger of the session holds no `error` lesson.

> **problem:**
> `/guppi:install` refuses a project that already holds its own `CLAUDE.md`, `.claude/settings.json` or another file of the install, so GUPPI cannot install into an existing project. Its files cannot simply be joined to GUPPI's, since the render writes those files whole from ratified pages.

> **recommend:**
> - **What the install does in a project that already holds its own files**
>   - Recommended: (c) the install sets the clashing files aside, and the person brings back what they need by ordinary Cases later.
>   - Answer: (b) the install sets the files aside, and the setup Case at the first `/hi` shows what they hold, for the person to keep or drop each part. The person first chose (c), asked how the process would go, and then changed the answer to (b).
> - **How the first `/hi` learns of the set-aside folder**
>   - Recommended: (b) the install writes one line about the folder into the brief it copies.
>   - Answer: not answered; the round that asked it was never shown to the person, since the person changed the answer to the first question, and **Where a kept part of a set-aside file lands** and **What happens until the setup step is built** replaced it.
> - **Which clashing files the install sets aside**
>   - Recommended: (c) `CLAUDE.md`, the files under `.claude/`, `.gitattributes` and `.github/workflows/checks.yml`; a clash under `vault/` or `.guppi/` still stops the install.
>   - Answer: agreed, (c).
> - **Where the set-aside files go**
>   - Recommended: (b) the folder `guppi-set-aside/` at the root, each file under its old path with `.set-aside` added to its name.
>   - Answer: agreed, (b).
> - **When the project's own `.claude/settings.json` is set aside**
>   - Recommended: (a) just before GUPPI's copy, after `uv sync` passes.
>   - Answer: agreed, (a).
> - **Where a kept part of a set-aside file lands**
>   - Recommended: (a) into the pages of GUPPI that already write that file; the setup Case creates no page.
>   - Answer: agreed, (a).
> - **What happens to the set-aside folder after the setup Case**
>   - Recommended: (a) a task of the setup Case deletes it in the Work Mode of the same session.
>   - Answer: agreed, (a).
> - **What happens until the setup step is built**
>   - Recommended: (a) nothing extra, since the published version waits for the setup step anyway.
>   - Answer: agreed, (a).
> - **How the Case is checked**
>   - Recommended: (a) two parts, each with a new check, and the refusal lines of the two checks of the install rewritten.
>   - Answer: agreed, (a).
> - **Where a kept part lands when no page writes its file**
>   - Recommended: (a) the setup Case holds a task that writes the kept part into GUPPI's copy of that file, run in the Work Mode of the same session.
>   - Answer: (a).

### Case 932.1 — The install sets aside the files of the project that clash

> **given:**
> `rule-plugin-install`: its Purpose and its Render set what the install does with a file of the project at a path of the install.
> **＋** `plugin/skills/install/SKILL.md`: the skill `/guppi:install`, which the Render writes.
> **＋** `estimate-plugin-install-sets-aside-the-files-of-the-project`: the new check of the setting aside.
> **＋** `.claude/`: the folder whose files of the project the install sets aside.
> **＋** `.claude/settings.json`: the settings file, which the install sets aside only after `uv sync` passes.
> **＋** `.github/workflows/checks.yml`: a file of the project that the install sets aside.
> **＋** `guppi-set-aside/`: the folder that holds the set-aside files.
> **＋** `/hi`: the first session after the install, where the person keeps or drops the set-aside files.

> **when:**
> The person types `/guppi:install` of `plugin/skills/install/SKILL.md` in a project open in Claude Code, where `uv --version` passes, that holds a `CLAUDE.md`, a `.claude/settings.json` and a `.gitattributes` of its own and no other file of the install.

> **then:**
> Before it copies, the agent moves each file of the project at a path of the install that is `CLAUDE.md`, a file under `.claude/` but `.claude/settings.json`, `.gitattributes` or `.github/workflows/checks.yml` into `guppi-set-aside/`, under its old path with `.set-aside` added to its name.
> **＋** It moves the `.claude/settings.json` of the project into `guppi-set-aside/` the same way only after `uv sync` passes, just before it copies the `.claude/settings.json` of GUPPI.
> **＋** Its last message lists each file it set aside with its path under `guppi-set-aside/`, and says that none of them loads or runs until the person keeps or drops it at the first `/hi`.
> **＋** When `uv sync` fails, it deletes what it copied, moves each file it set aside back to its old path and deletes `guppi-set-aside/`, so that the project holds only what it held before.
> **－** It changes no text of a file it sets aside, and sets aside no file at a path that the install does not write.
> **－** In a project that holds a file of the install at any other path, or that already holds `guppi-set-aside/`, it lists them, writes and moves nothing, and stops.
> **－** It writes nothing into the folder of the plugin, and runs no `guppi` command and no `git` command.

> **tasks:**
> - [ ] update `rule-plugin-install`
>   - old: `` It writes nothing when one of those files already stands in the project, and it runs no `guppi` and no `git` command. ``
>   - new: `` Where the project already holds a file at one of those paths that is `CLAUDE.md`, a file under `.claude/`, `.gitattributes` or `.github/workflows/checks.yml`, it moves that file of the project, its text unchanged, to the same path under the folder `guppi-set-aside/`, with `.set-aside` added to its name, such as `guppi-set-aside/CLAUDE.md.set-aside`, so that Claude Code loads and runs none of it. It writes and moves nothing when the project holds a file of the install at any other path, such as under `vault/` or `.guppi/`, or already holds `guppi-set-aside/` (as set in case 932.1). It runs no `guppi` and no `git` command. ``
>   - old: `` and none runs after a failed `uv sync` (as set in case 912). ``
>   - new: `` and none runs after a failed `uv sync` (as set in case 912). It sets aside a `.claude/settings.json` of the project only then, just before it copies the one of GUPPI, so that the hooks of the project run until then and a failed `uv sync` leaves that file in place (as set in case 932.1). ``
>   - old: `` When `uv sync` fails, the skill shows its output, deletes each file it copied and each folder it made, ``
>   - new: `` When `uv sync` fails, the skill shows its output, deletes each file it copied and each folder it made, moves each file it set aside back to its old path and deletes `guppi-set-aside/`, ``
>   - old: `and [[rule-morph]] sets its settings there.`
>   - new: `and [[rule-morph]] sets its settings there. The last message of the install lists each file it set aside, and the setup Case of that first /hi shows what each holds, for the person to keep or drop each part (as set in case 932.1).`
>   - old: `3. Check which of those paths already stand in the project. When one or more stand, list them, say that the install writes nothing into a project that already holds one of its files, and stop. Write nothing.`
>   - new: `` 3. Check which of those paths already stand in the project, and whether the folder `guppi-set-aside/` stands there. When that folder stands, or when one of those paths is not `CLAUDE.md`, a file under `.claude/`, `.gitattributes` or `.github/workflows/checks.yml`, such as a path under `vault/` or `.guppi/`, list them, say that the install writes nothing into a project that already holds them, and stop. Write and move nothing. ``
>   - old: `` 4. Otherwise copy each file to its path in the project, with the folders it needs, but `.claude/settings.json`, which step 7 copies once `uv sync` passes, so that no hook of the project runs before then. ``
>   - new: `` 4. Otherwise set aside each of those paths that stands in the project, but `.claude/settings.json`: move the file of the project, its text unchanged, to the same path under `guppi-set-aside/`, with `.set-aside` added to its name, such as `guppi-set-aside/CLAUDE.md.set-aside`. Then copy each file to its path in the project, with the folders it needs, but `.claude/settings.json`, which step 7 copies once `uv sync` passes, so that no hook of GUPPI runs before then. ``
>   - old: `` included, so that the project holds only what it held before. Delete nothing else. ``
>   - new: `` included, move each file you set aside in step 4 back to its old path, and delete `guppi-set-aside/`, so that the project holds only what it held before. Delete nothing else. ``
>   - old: `` 7. Copy `.claude/settings.json` from `${CLAUDE_PLUGIN_ROOT}` to its path in the project, and check that it stands. ``
>   - new: `` 7. When the project holds a `.claude/settings.json` of its own, move it, its text unchanged, to `guppi-set-aside/.claude/settings.json.set-aside`. Then copy `.claude/settings.json` from `${CLAUDE_PLUGIN_ROOT}` to its path in the project, and check that it stands. ``
>   - old: `` 8. Say that GUPPI is installed, and that the person reopens Claude Code in this project and types `/hi`. ``
>   - new: `` 8. Say that GUPPI is installed, and that the person reopens Claude Code in this project and types `/hi`. When step 4 or step 7 set aside files, list each of them with its path under `guppi-set-aside/`, and say that the setup Case of the first `/hi` shows what each holds, for the person to keep or drop each part, and that until then none of them loads or runs. ``
>   - change: `taken up: the install sets aside a CLAUDE.md, a file under .claude/, a .gitattributes or a .github/workflows/checks.yml of the project in guppi-set-aside/, the settings file only after uv sync passes, and stops only on a clash elsewhere`
> - [ ] `uv run --project .guppi guppi render`: `plugin/skills/install/SKILL.md`
> - [ ] create `estimate-plugin-install-sets-aside-the-files-of-the-project`
>   - ref: `rule-plugin-install`
>   - kind: `QA`
>   - purpose: `Whether /guppi:install moves each file of the project at a path of the install that is CLAUDE.md, a file under .claude/, .gitattributes or .github/workflows/checks.yml into guppi-set-aside/ with .set-aside added, the settings file only after uv sync passes, lists them in its last message, puts them back when uv sync fails, and stops on a clash at any other path`
>   - method: `by hand, after the librarian's run of the session that sets this Criterion, with a tag prod-x.y.z in the history of HEAD: the clean version written into a local folder by uv run --project .guppi guppi ship --allow-draft, that folder added as a catalogue by /plugin marketplace add and guppi installed from it by /plugin install guppi@guppi-marketplace; in a project that holds a CLAUDE.md, a .claude/settings.json with a hook and a .gitattributes of its own, /guppi:install typed; in a second such project with Claude Code started from a terminal with UV_OFFLINE=1 and UV_CACHE_DIR set to an empty folder, /guppi:install typed; in a third project with a file under vault/ of its own, /guppi:install typed; the transcripts and the files of the three projects before and after read against the Criterion`
>   - tags: `[plugin, harness]`
> - [ ] read `estimate-plugin-install-sets-aside-the-files-of-the-project`

> **ratification:**
> ```
> - decision[case 932.1][update][rule-plugin-install]{ref:rule-plugin-install}{supersedes:case 911}
> - decision[case 932.1][create][estimate-plugin-install-sets-aside-the-files-of-the-project]{ref:rule-plugin-install}{tags:plugin,harness}
> ```

### Case 932.2 — The setup Case takes in the set-aside files

> **given:**
> `rule-morph`: its Purpose sets how the setup Case of the first `/hi` takes in the set-aside files.
> **＋** `estimate-morph-takes-in-the-set-aside-files`: the new check of the take-in.
> **＋** `rule-plugin-install`: the rule of the install.
> **＋** `/guppi:install`: the skill that sets the files of the project aside in `guppi-set-aside/`.
> **＋** `rule-claude-md`: the page that writes `CLAUDE.md`, an example of a page that writes a set-aside file.
> **＋** `guppi.toml`: its key marks the setup as done.
> **＋** `.gitattributes`: a file that no page writes.
> **＋** `.github/workflows/checks.yml`: a file that no page writes.

> **when:**
> In a project where `/guppi:install`, as `rule-plugin-install` sets it, set aside files of the project under `guppi-set-aside/`, and whose `guppi.toml` does not mark the setup of `rule-morph` as done, the person reopens Claude Code and types `/hi`.

> **then:**
> The setup Case of `rule-morph` shows what each file under `guppi-set-aside/` holds, by its old path.
> **＋** In that one setup Case, the person keeps or drops each part of each file, such as an instruction, a hook or a permission.
> **＋** A kept part goes into the page that writes its file, such as `rule-claude-md` for an instruction of `CLAUDE.md`, and the render of the Work Mode of that session writes it into the file.
> **＋** For a file that no page writes, such as `.gitattributes` or `.github/workflows/checks.yml`, a task of the setup Case writes the kept part into that file, and the Work Mode of the same session runs it.
> **＋** A task of the setup Case deletes `guppi-set-aside/` in that Work Mode.
> **－** A dropped part reaches no file of the project.
> **－** The setup Case creates no page for a kept part.

> **tasks:**
> - [ ] update `rule-morph`
>   - old: `` but by the copy of `/guppi:install` and the render that `/hi` runs ``
>   - new: `` but by the copy and the setting aside of `/guppi:install` and the render that `/hi` runs ``
>   - old: `as the clean version holds them ([[rule-ratification]]).`
>   - new: `` as the clean version holds them ([[rule-ratification]]). Where `/guppi:install` set aside files of the project in the folder `guppi-set-aside/`, the setup Case also shows what each of them holds, by its old path, and the person keeps or drops each part of it, such as an instruction, a hook or a permission. A kept part goes into the page of GUPPI that writes its file, such as [[rule-claude-md]] for an instruction of `CLAUDE.md`, [[rule-hook-registry]] for a hook and [[rule-permissions]] for a permission, and the render writes it into the file; for a file that no page writes, such as `.gitattributes` or `.github/workflows/checks.yml`, a task of the setup Case writes the kept part into that file. A dropped part reaches no file, the setup Case creates no page for a kept part, and a task of it deletes `guppi-set-aside/` in the Work Mode of the same session (as set in case 932.2). ``
>   - change: `the setup Case shows what the files that /guppi:install set aside hold; the person keeps or drops each part, a kept part goes into the page that writes its file or, where none does, into the file by a task, and guppi-set-aside/ is deleted`
> - [ ] create `estimate-morph-takes-in-the-set-aside-files`
>   - ref: `rule-morph`
>   - kind: `QA`
>   - purpose: `Whether the setup Case of the first /hi shows what each file that /guppi:install set aside holds, lets the person keep or drop each part, puts a kept part into the page that writes its file or, where none does, into the file by a task, creates no page and deletes guppi-set-aside/`
>   - method: `by hand, after the session whose Work Mode builds the setup skill of rule-morph and its step in /hi: in a project that holds a CLAUDE.md, a .claude/settings.json with a hook and a .gitattributes of its own, with a tag prod-x.y.z in the history of HEAD, the plugin guppi installed from a local copy written by uv run --project .guppi guppi ship --allow-draft, /guppi:install typed, Claude Code reopened and /hi typed, one part of each set-aside file kept and one dropped in the setup Case; the transcript of that session, its ledger and the files its Work Mode writes read against the Criterion, recorded in the estimate line`
>   - tags: `[session, harness, plugin]`
> - [ ] read `estimate-morph-takes-in-the-set-aside-files`

> **ratification:**
> ```
> - decision[case 932.2][update][rule-morph]{ref:rule-morph}
> - decision[case 932.2][create][estimate-morph-takes-in-the-set-aside-files]{ref:rule-morph}{tags:session,harness,plugin}
> ```

### Case 932.3 — The check of an install into an empty project promises no refusal

> **given:**
> `estimate-plugin-install-writes-guppi-into-an-empty-project`: its Criterion is replaced whole by the text under `sections`.
> **＋** `/guppi:install`: the skill whose refusal of a project that holds a file of the install ends.

> **when:**
> Someone reads the Criterion of `estimate-plugin-install-writes-guppi-into-an-empty-project` to judge `/guppi:install`.

> **then:**
> Its reading still judges the clean version and the copy of `/guppi:install` into an empty project.
> **－** Its reading needs no second project with a `CLAUDE.md` of its own.

> **tasks:**
> - [ ] update `estimate-plugin-install-writes-guppi-into-an-empty-project`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether guppi ship puts the skill install into the clean version, and whether /guppi:install copies every file of the plugin but its own into a project that holds none of them"
>     method: "uv run --project .guppi pytest .guppi/tests/test_ship.py -k plugin_skill; by hand, after the librarian's run of the session that sets this Criterion, with a tag prod-x.y.z in the history of HEAD: the clean version written into a local folder by uv run --project .guppi guppi ship --allow-draft; in an empty project, that folder added as a catalogue by /plugin marketplace add, guppi installed by /plugin install guppi@guppi-marketplace, /guppi:install typed and the files of the project read against those of the plugin and against the Criterion"
>     ```
>   - sections.Criterion:
>     ```
>     When:
>     `uv run --project .guppi guppi ship --allow-draft <folder>` builds the clean version, as `rule-clean-branch` sets it, and `uv run --project .guppi guppi ship --check` judges the working tree.
>     **＋** The person writes the clean version into a local folder by `uv run --project .guppi guppi ship --allow-draft <folder>`, adds that folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` in the project open in Claude Code, as `rule-plugin-install` sets it.
>
>     Then:
>     `uv run --project .guppi guppi ship --allow-draft <folder>` writes `plugin/skills/install/SKILL.md` to `skills/install/SKILL.md` of the clean version and cleans it like each other file it writes, and the clean version holds no file under `plugin/skills/`.
>     **＋** `uv run --project .guppi guppi ship --check` judges `plugin/skills/install/SKILL.md` in place, as it judges each other file outside `vault/`.
>     **＋** The installed plugin offers the skill `install`, which the person types as `/guppi:install`.
>     **＋** In a project that holds none of the files it would write, `/guppi:install` copies each file of the plugin to the same path in the project, but those under `.claude-plugin/`, `skills/` and `.git/`, such as `CLAUDE.md`, `.claude/settings.json`, the code under `.guppi/` and the pages under `vault/wiki/`.
>     **＋** It checks that each copied file stands, and its last message tells the person to reopen Claude Code in the project and type `/hi`.
>     **－** It writes nothing into the folder of the plugin, and runs no `guppi` command and no `git` command.
>     **－** The skills it copies under `.claude/skills/` keep their bare names, such as `hi`.
>     **－** Which files a new project needs, what the install does about `uv` and the Python environment under `.guppi/`, and what it does with a file of the project that stands at one of its paths are no part of this promise.
>     ```
>   - change: `the Criterion replaced whole — the refusal of a project that holds a file of the install leaves it, since the install now sets such files aside`
> - [ ] read `estimate-plugin-install-writes-guppi-into-an-empty-project`

> **ratification:**
> ```
> - decision[case 932.3][update][estimate-plugin-install-writes-guppi-into-an-empty-project]{ref:rule-plugin-install}
> ```

### Case 932.4 — The check of the settings file before `uv sync` promises no refusal

> **given:**
> `estimate-plugin-install-runs-no-hook-before-uv-sync`: its Criterion is replaced whole by the text under `sections`.
> **＋** `/guppi:install`: the skill whose refusal of a project that holds a file of the install ends.

> **when:**
> Someone reads the Criterion of `estimate-plugin-install-runs-no-hook-before-uv-sync` to judge `/guppi:install`.

> **then:**
> Its reading still judges, in an empty project, that no hook runs before `uv sync` passes or after it fails.
> **－** Its Criterion keeps no line on a refusal by `/guppi:install`.

> **tasks:**
> - [ ] update `estimate-plugin-install-runs-no-hook-before-uv-sync`
>   - set: `{status: pending}`
>   - sections.Criterion:
>     ```
>     When:
>     The person types `/guppi:install` of `plugin/skills/install/SKILL.md` in an empty project open in Claude Code, where `uv --version` passes.
>
>     Then:
>     Until `uv sync --project .guppi` passes, the project holds no `.claude/settings.json`, so no hook of the copy runs.
>     **＋** No hook of the copy has made `.guppi/.venv/` by the time `uv sync` runs.
>     **＋** When `uv sync` fails, the project never holds `.claude/settings.json`, and no later command of that session shows a hook error.
>     **－** What the install does with a file of the project that stands at one of its paths is no part of this promise.
>     ```
>   - change: `the Criterion replaced whole — the refusal of a project that holds a file of the install leaves it, since the install now sets such files aside`
> - [ ] read `estimate-plugin-install-runs-no-hook-before-uv-sync`

> **ratification:**
> ```
> - decision[case 932.4][update][estimate-plugin-install-runs-no-hook-before-uv-sync]{ref:rule-plugin-install}
> ```

### Case 932.5 — The check of the setup Case counts the setting aside among the changes of the install

> **given:**
> `estimate-morph-sets-up-the-project-at-the-first-hi`: its purpose and its Criterion, replaced whole by the text under `sections`, name the setting aside beside the copy.
> **＋** `/guppi:install`: the skill that copies the files of GUPPI and sets aside those of the project.

> **when:**
> Someone reads `estimate-morph-sets-up-the-project-at-the-first-hi` to judge which changes of the settings files come before the setup Case.

> **then:**
> Its purpose and its Criterion count the files that `/guppi:install` sets aside, beside the files it copies, among the changes that come before the setup Case.
> **－** Its promise on the setup Case itself does not change.

> **tasks:**
> - [ ] update `estimate-morph-sets-up-the-project-at-the-first-hi`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether the first /hi after /guppi:install, in a project whose guppi.toml does not mark the setup as done, puts one setup Case first, before the opening of the first sprint, with the values it finds and the values the person gives, and whether the settings change only by the copy and the setting aside of /guppi:install, the render of /hi and the render after that Case is ratified"
>     ```
>   - sections.Criterion:
>     ```
>     When:
>     In a project where the person installed the plugin `guppi` and typed `/guppi:install`, as `rule-plugin-install` sets it, and whose `guppi.toml` does not mark the setup of `rule-morph` as done, the person reopens Claude Code and types `/hi`.
>
>     Then:
>     `/hi` opens the session as `rule-skill-hi` sets it, and puts the setup Case first, before the opening Case of `rule-skill-sprint-open` and before the Frontier.
>     **＋** Once the person ratifies the setup Case, `/hi` starts `/sprint-open` in the same session, and the ledger hook of `rule-ledger-write` writes the decision lines of the setup Case though no sprint is open.
>     **＋** The setup step takes the name of the main branch and the git remote from git, and the name of the project's folder of saved transcripts under `~/.claude/projects` from the path of the project.
>     **＋** It asks the person only for the values it cannot find, such as `documentation_lang`, `chat_lang`, the commands of the keys `test` and `style` of `guppi.toml`, and the description of the project.
>     **＋** Every value stands in that one setup Case, which the person ratifies or corrects.
>     **＋** The Work Mode of the same session writes the settings by the render of the rule pages that hold them, such as `guppi.toml` from `rule-guppi-config`, the description of the project in `CLAUDE.md` from `rule-claude-md` and the read rules of the saved transcripts from `rule-permissions`, and `guppi.toml` then marks the setup as done.
>     **－** `/guppi:install` is no Case, and the person ratifies nothing at it.
>     **－** Between `/guppi:install` and the ratified setup Case, no settings file changes but by the copy and the setting aside of `/guppi:install` and the render that `/hi` runs.
>     **－** The setup step is no skill named `install`.
>     **－** The setup step does not ask for the category set: the project takes the development set, as `entity-sprint-plugin` keeps the category set as data in its `## Backlog`.
>     **－** The setup step reads no code of the project and creates no page for it.
>     **－** A project whose `guppi.toml` marks the setup as done gets no setup Case at `/hi`.
>     ```
>   - change: `the Criterion replaced whole — the files that /guppi:install sets aside count beside its copy among the changes before the setup Case`
> - [ ] read `estimate-morph-sets-up-the-project-at-the-first-hi`

> **ratification:**
> ```
> - decision[case 932.5][update][estimate-morph-sets-up-the-project-at-the-first-hi]{ref:rule-morph}
> ```
