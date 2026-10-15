## Case 818 — The plugin guppi installs GUPPI into a project

> **context:**
> The branch `prod` holds the clean version of GUPPI that `guppi ship` builds: GUPPI's code, the harness `.claude/` and `CLAUDE.md`, already rendered, and each page with `core: true`. Case 819 of this session moves the code into a folder of its own, `.guppi/`. Case 816 makes that branch a catalogue, `guppi-marketplace`, and the clean version a plugin, `guppi`. But Claude Code loads the skills of a plugin from a folder `skills/` at its root, and the clean version keeps its skills under `.claude/skills/`. So an install of the plugin gives the person nothing to run, and an empty project gets no file of GUPPI. The person chose the plugin as an installer, model B. The plugin carries one skill of its own, `install`, typed as `/guppi:install`. That skill copies the files of the plugin, as `guppi ship` built them, into the project open in Claude Code, and runs no `guppi` command. The first `/hi` of the project then renders the harness from the project's own rule pages, by its line `guppi render --sync`. Until the open item on what a new project gets (C9) is decided, the skill copies every file of the plugin but its own: those under `.claude-plugin/`, `skills/` and `.git/`. A later Case on that item narrows the set. After Case 819, the copied files hold GUPPI's code under `.guppi/` and no `pyproject.toml` or `uv.lock` at the root, so a project's own `pyproject.toml` no longer stops the install; a file under `.guppi/` that already stands does stop it. Case 819.4 adds two steps to the skill: it checks `uv` before it writes, and it runs `uv sync` in `.guppi/` after the copy. Case 819.4 writes the Purpose and the Render of `rule-plugin-install` whole. The texts this Case creates for that page are its first form, written to agree with Case 819.4 but for those two steps. The `then` of Case 818.1 leaves `uv` and the Python environment to Case 819.4, and its check that each copied file stands and its last message come before and after the `uv sync` step of Case 819.4, so the two orders agree. In a project where one of those files already stands, the skill lists the files, writes nothing and stops. Merges and updates are left to later items. The skills of a project keep their bare names, such as `/hi`; only the skill of the plugin carries the prefix of the plugin. A new rule, `rule-plugin-install`, holds the text of the skill in its Render, written to `plugin/skills/install/SKILL.md`. It has no `core: true`, so a project that installs GUPPI does not hold it. `guppi ship` copies that file to `skills/install/SKILL.md` of the clean version (Case 818.1). The Criterion of `estimate-sprint-plugin-installs-as-a-plugin` expects `/hi` to run right after the plugin installs, which is no longer true under model B, so Case 818.2 replaces it. In the plugin-structure skill of the official `plugin-dev` plugin in the local plugin cache, `case-guppi` read that a skill file may name `${CLAUDE_PLUGIN_ROOT}` as the path of the plugin, and in its skill-development skill that `name` is required in the frontmatter of a skill. That the skill is called as `/guppi:install` is what the main agent read in the Claude Code docs; `case-guppi` did not read it at its source, and the reading of Case 818.1 tests it. The vault query found no page on the install of the plugin. Near pages are `rule-clean-branch`, which builds the clean version, and `rule-morph`, the install Case at the first `/hi`, which Case 817 of this batch owns. A Glob `vault/**/*plugin-install*` printed `vault/wiki/estimates/estimate-sprint-plugin-installs-as-a-plugin.md` alone, so both new slugs are free. The tags `harness`, `plugin` and `render` exist in `vault/wiki/tags.md`. A Grep `install` (case-insensitive) over `vault/wiki/rules/` printed `rule-clean-branch.md`, `rule-guppi-config.md`, `rule-github-repository.md`, `rule-morph.md` and `rule-permissions.md`. A Grep of the same pattern over `.claude/` printed nothing. `rule-clean-branch` changes here. `rule-guppi-config` leaves the questions of an install to `rule-morph`. `rule-github-repository` says that an install does not carry the settings of the repository on GitHub. `rule-permissions` leaves the name of the transcripts folder of another install to `rule-morph`. Each of these stays true. `rule-morph` sets what the first `/hi` does after the install, and this Case does not touch that moment. Case 817 sets that its own skill is not named `install`, so a project never holds both `/install` and `/guppi:install`. Until Case 817 lands, the copied `.claude/settings.json` names the transcripts folder of this repository. Today `guppi ship` leaves out `vault/wiki/sprint.md`, `vault/wiki/backlog.md` and `vault/wiki/brief.md`, which the `@` lines of `/hi` name. Case 821.3 ships them as skeletons, so the first `/hi` of a new project starts `/sprint-open`. Case 821.7 stops `guppi ship <folder>` while a page with `core: true` stands `draft`, so the workflow writes nothing to `prod` while `rule-skill-hi`, `rule-work-mode` and `entity-sprint` stand `draft`, likely until after the close of the sprint `plugin`. So the person chose that the sprint reads the install from a local copy that `guppi ship --allow-draft` writes, before the close (Case 818.2). That local folder holds `.claude-plugin/marketplace.json` of Case 816, the catalogue `guppi-marketplace` whose plugin `guppi` stands at `./`. The person adds it by `/plugin marketplace add <folder>` and installs by `/plugin install guppi@guppi-marketplace`. `case-guppi` read the form `/plugin install <plugin>@<catalogue>` in the README of the official catalogue in the local plugin cache, and `/plugin marketplace add` with a catalogue on GitHub in the README of its plugin `claude-security`. That a local folder is accepted as a catalogue, and that a plugin at a relative path loads in place, is what the main agent read in the Claude Code docs. `case-guppi` did not read it at its source, and the reading of Case 818.2 tests it. The reading of Case 818.1 is taken on the install from `prod` itself, so its `method` waits for the first run of `.github/workflows/prod.yml` that writes `prod`. Case 819.3 replaces the Criterion of `estimate-clean-branch-writes-a-clean-copy` with the code under `.guppi/`. Its line that `guppi ship` writes no file that a page without `core: true` renders in full names the path that the page governs, `plugin/skills/install/SKILL.md`, which the clean version does not hold. Its `--check` line covers each file that `guppi ship` would write outside `vault/`, `skills/install/SKILL.md` included. The copy to `skills/` is promised by the new Estimate of Case 818.1, so it is not signed twice. The other Estimates of `rule-clean-branch` speak of pointers in pages and code, which this Case does not change, and `estimate-clean-branch-installs-as-a-plugin` of Case 816 leaves the skills of the plugin out of its promise. A Grep `estimate-sprint-plugin-installs-as-a-plugin` over `vault/wiki/` printed `brief.md`, `log.md` and `entities/entity-sprint-plugin.md`. The entity names the Estimate in its `estimates` field, and its Purpose still holds. A Grep `project_root\(\)|REPO\b|ROOT = |Path\(__file__\)` over `tests/` printed `test_lint.py`, `test_schemas.py`, `test_generate.py`, `test_materialize.py`, `test_orchestration.py` and `test_case_schema.py`. Those files read the `schema.yaml` of a category, `case-schema.md`, `case-example.md`, `orchestration.md` and the `Makefile`, and this Case changes none of those. The new rule takes `rule-harness`, the map of the harness tools, as its parent, as `rule-render-harness` does. The pair of Case 818.1 on `rule-clean-branch` and the first pair of Case 816.1 touch the same sentence of its Purpose, and the two fit. Case 818.1 puts a sentence before the words `It gives each page`, which Case 816.1 does not change. Case 816.1 adds sentences after the words `the pages it writes.`, which Case 818.1 does not change. So each `old` hits the page once, whichever pair runs first. Read side by side, the two new texts agree: `skills/` of the clean version comes from `plugin/skills/`, and the clean version holds no folder `plugin/`. The Criterion of `estimate-sprint-plugin-installs-as-a-plugin` is replaced whole. Its one `When` line, someone installs the clean branch as a plugin into an empty project, opens Claude Code there and types `/hi`, becomes the three `when` lines of Case 818.2: the local copy, the install from it with `/guppi:install`, and the reopening of Claude Code before `/hi`. The task on `guppi/ship.py` adds a copy and no new judgment of a text: it judges the copied skill by `judged`, as it judges each other file. Case 819.3 changes other sentences of `rule-clean-branch`: the list of what `guppi ship` writes, and what it leaves out. Its new texts do not touch the words that the two pairs of Case 818.1 anchor on. The new texts of Case 818.1 name no `guppi/` and no `tests/` outside `.guppi/`, so the path pairs of the `reword` of Case 819.1 leave them as they are. The `when` of Case 818.1 names `uv run guppi ship`, which Case 819.1's `reword` turns into the form with `--project .guppi`, since the decision lines of Case 818 come before it in the ledger. The `method` of its Estimate and the texts of Case 818.2 already name the form with `--project .guppi` and `.guppi/tests/`, which the pairs of that `reword` do not hit. Case 821.3 adds a sentence to `rule-clean-branch` before the words `It gives each page`, where Case 818.1 adds its own, and both pairs keep those words. It also replaces the last sentence of the Purpose that Case 819.4 writes for `rule-plugin-install`. Case 818.1 writes that sentence too, in its first form of the page, which Case 819.4 replaces whole. So no words of Case 818 that Cases 819.4 and 821.3 leave alone change here. Cases 820.5 and 821.4 add sentences to the same paragraph of `rule-clean-branch` as the second pair of Case 818.1. Case 820.5 adds its sentence after the words `a Case rewords that text at its source.`, and Case 821.4 adds its sentence after the end of the sentence of Case 820.5. The second pair of Case 818.1 changes only the dashed list of the `--check` sentence, from `— the code, the harness` to `of the project —`, which comes later in that paragraph. Case 820.7 rewords `make lint` across the pages, and the words `and make lint runs it` that follow that list stand outside the `old` of the pair. So each `old` hits the page once in any order. Read side by side, the texts agree: `--check` judges the code, the harness, the root files and `plugin/skills/` in place. It skips `.guppi/guppi/ship.py`, which the clean version does not hold. Case 821.5 adds `.github/workflows/checks.yml` in a sentence of its own. The Work Mode of Case 819 moves the tests, and the task of Case 818.1 on the tests of `guppi ship` goes to that file wherever it then stands.

> **problem:**
> An install of the plugin `guppi` gives a project no skill to run and no file of GUPPI, so GUPPI cannot be installed into a new project.

> **recommend:**
> - **What `/guppi:install` puts into the project**
>   - Recommended: (a) copy the ready files from the plugin's own copy; the first `/hi` renders.
>   - Answer: agreed, (a).
> - **How far this Case reaches while two questions stay open**
>   - Recommended: (a) copy everything but the plugin's own files for now; a later Case narrows the set.
>   - Answer: agreed, (a).
> - **A project that is not empty**
>   - Recommended: (a) list the files that already stand, write nothing and stop.
>   - Answer: agreed, (a).
> - **Skill names**
>   - Recommended: (a) bare names in every project; only the plugin's skill is `/guppi:install`.
>   - Answer: agreed, (a).
> - **Which page governs the install skill**
>   - Recommended: (a) a new rule `rule-plugin-install` with no `core: true`, whose Render `guppi ship` copies to `skills/install/SKILL.md`.
>   - Answer: agreed, (a).
> - **What checks that this is done**
>   - Recommended: (a) a new Estimate on the install, and the Criterion of the sprint Estimate replaced.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: build the Case again to agree with Case 819, which moves GUPPI's code, its `pyproject.toml` and its `uv.lock` into `.guppi/` and adds the `uv` steps to the install.
>   - Taken: the install copies the code under `.guppi/` and no `pyproject.toml` at the root, so a file under `.guppi/` that already stands stops it and a project's own `pyproject.toml` does not. The first text of `rule-plugin-install` names `.guppi/`, and `uv` and the Python environment are left to Case 819.4.
> - **Change**
>   - Asked: build the Case again to agree with Case 821, which stops `guppi ship` while a page with `core: true` is `draft` and adds `--allow-draft` for a local copy.
>   - Taken: the sprint Estimate of Case 818.2 reads an install from a local copy that `guppi ship --allow-draft` writes, added by `/plugin marketplace add` and installed by `/plugin install guppi@guppi-marketplace`, before the close. The `method` of the Estimate of Case 818.1 waits for the first run that writes `prod`.

### Case 818.1 — /guppi:install copies GUPPI into an empty project

> **given:**
> `rule-plugin-install`: the new rule of the skill of the plugin.
> **＋** `estimate-plugin-install-writes-guppi-into-an-empty-project`: the new check of the install.
> **＋** `plugin/skills/install/SKILL.md` and `skills/install/SKILL.md`: the skill `/guppi:install` as the Render writes it in this repository, and as the clean version holds it.
> **＋** `.claude-plugin/`, `skills/` and `.git/`: the plugin's own files, which the install does not copy.
> **＋** `CLAUDE.md`, `.claude/settings.json`, `.claude/skills/` with `/hi`, `.guppi/` and `vault/wiki/`: files of the plugin that the install copies.
> **＋** `rule-clean-branch`: the rule of `guppi ship`.
> **＋** `vault/raw/2026-10-14/1907/cases/case-816.md`, `vault/raw/2026-10-14/1907/cases/case-819.md` and `vault/raw/2026-10-14/1907/cases/case-821.md`: the Cases of this session that make the clean version a plugin, move the code into `.guppi/`, set what a new project gets, and change `rule-clean-branch` and `rule-plugin-install`.
> **＋** `guppi/ship.py`: the code of `guppi ship`.
> **＋** `tests/test_ship.py`: the tests of `guppi ship`.

> **when:**
> `uv run guppi ship <folder>` builds the clean version, as `rule-clean-branch` sets it, and `uv run guppi ship --check` judges the working tree.
> **＋** The person installs the plugin `guppi` from the catalogue of the branch `prod` and types `/guppi:install` in the project open in Claude Code, as `rule-plugin-install` sets it.

> **then:**
> `uv run guppi ship <folder>` writes `plugin/skills/install/SKILL.md` to `skills/install/SKILL.md` of the clean version and cleans it like each other file it writes, and the clean version holds no file under `plugin/skills/`.
> **＋** `uv run guppi ship --check` judges `plugin/skills/install/SKILL.md` in place, as it judges each other file outside `vault/`.
> **＋** The installed plugin offers the skill `install`, which the person types as `/guppi:install`.
> **＋** In a project that holds none of the files it would write, `/guppi:install` copies each file of the plugin to the same path in the project, but those under `.claude-plugin/`, `skills/` and `.git/`, such as `CLAUDE.md`, `.claude/settings.json`, the code under `.guppi/` and the pages under `vault/wiki/`.
> **＋** It checks that each copied file stands, and its last message tells the person to reopen Claude Code in the project and type `/hi`.
> **－** In a project where one or more of those files already stand, it lists them, writes nothing and stops.
> **－** It writes nothing into the folder of the plugin, and runs no `guppi` command and no `git` command.
> **－** The skills it copies under `.claude/skills/` keep their bare names, such as `hi`.
> **－** Which files a new project needs, and what the install does about `uv` and the Python environment under `.guppi/`, are no part of this promise.

> **tasks:**
> - [ ] create `rule-plugin-install`
>   - type: `rule`
>   - ref: `rule-harness`
>   - kind: `Leaf`
>   - purpose: `Prevents a project that installs the plugin guppi from getting a part of GUPPI, or from losing a file of its own to it`
>   - enforcement: `render`
>   - governs: `plugin/skills/install/SKILL.md`
>   - render_mode: `full`
>   - tags: `[harness, plugin, render]`
>   - sections.Purpose:
>     ```
>     Prevents a project that installs the plugin `guppi` from getting a part of GUPPI, or from losing a file of its own to it. The plugin, which the catalogue `guppi-marketplace` on the branch `prod` lists, is an installer. It carries one skill of its own, `install`, which the person types as `/guppi:install` in the project to install into. `guppi ship` copies the skill from `plugin/skills/install/SKILL.md`, which the Render of this page writes, to `skills/install/SKILL.md` of the clean version ([[rule-clean-branch]]). The skill copies into the project each file of the plugin but its own files, those under `.claude-plugin/`, `skills/` and `.git/`. Those files are the code of GUPPI in `.guppi/`, the harness `.claude/` and `CLAUDE.md`, the files at the root and the pages with `core: true`, as `guppi ship` built them. It writes nothing when one of those files already stands in the project, and it runs no `guppi` and no `git` command. The project then runs on its own copy: its first `/hi` renders the harness from its own rule pages, and [[rule-morph]] sets its settings there. The skills of the project keep their bare names, such as `/hi`; only the skill of the plugin carries the prefix of the plugin (case 818). This page has no `core: true`, so a project that installs GUPPI does not hold it. Which files a new project gets waits for a Case of its own.
>     ```
>   - sections.Render:
>     ````
>     <!-- rule-plugin-install -->
>     ---
>     name: install
>     description: "Install GUPPI into the project open in this session: copy its files from this plugin, then the person reopens Claude Code and types /hi. Run it when the person types /guppi:install."
>     disable-model-invocation: true
>     ---
> 
>     Install GUPPI into the project of this session, the folder that Claude Code was opened in. The files come from this plugin, at `${CLAUDE_PLUGIN_ROOT}`. Write nothing into that folder of the plugin.
> 
>     1. List each file under `${CLAUDE_PLUGIN_ROOT}`, but the files under `.claude-plugin/`, `skills/` and `.git/`. These are the files to install, each at the same path in the project.
>     2. Check which of those paths already stand in the project. When one or more stand, list them, say that the install writes nothing into a project that already holds one of its files, and stop. Write nothing.
>     3. Otherwise copy each file to its path in the project, with the folders it needs. Change no other file. Run no `guppi` command and no `git` command.
>     4. Check that each file now stands in the project. When one is missing, name it and stop.
>     5. Say that GUPPI is installed, and that the person reopens Claude Code in this project and types `/hi`.
>     <!-- /rule-plugin-install -->
>     ````
> - [ ] create `estimate-plugin-install-writes-guppi-into-an-empty-project`
>   - ref: `rule-plugin-install`
>   - kind: `QA`
>   - purpose: `Whether guppi ship puts the skill install into the clean version, and whether /guppi:install copies every file of the plugin but its own into a project that holds none of them, and writes nothing into one that holds one`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_ship.py -k plugin_skill; by hand, after the first run of .github/workflows/prod.yml that writes prod: in an empty project, the catalogue of prod added, guppi installed, /guppi:install typed and the files of the project read against those of the plugin; in a second empty project with a file CLAUDE.md of its own, /guppi:install typed and its output and the files of that project read against the Criterion`
>   - tags: `[plugin, harness]`
> - [ ] update `rule-clean-branch`
>   - old: `` It gives each page `origin: guppi`, `sprint: guppi`, ``
>   - new: `` It writes each file under `plugin/skills/` of this repository to the same path under `skills/` of the clean version, where Claude Code finds the skills of a plugin, and judges and cleans it like each other file it writes; the one such file is `plugin/skills/install/SKILL.md`, which the Render of [[rule-plugin-install]] writes (case 818). It gives each page `origin: guppi`, `sprint: guppi`, ``
>   - old: `` `guppi ship --check` judges in place each file outside `vault/` that the clean version holds — the code, the harness and the files at the root of the project — ``
>   - new: `` `guppi ship --check` judges in place each file outside `vault/` that the clean version holds — the code, the harness, the files at the root of the project and the files under `plugin/skills/` — ``
>   - change: `guppi ship writes the skill of the plugin from plugin/skills/ to skills/ of the clean version, and --check judges it in place`
> - [ ] `guppi/ship.py`: `guppi ship <folder>` writes each file under `plugin/skills/` to the same path under `skills/` of the clean version, judged and cleaned by `judged` like each other file, and writes no file of `plugin/skills/` at its own path; `--check` judges each file under `plugin/skills/` in place; the docstring says so.
> - [ ] `tests/test_ship.py`: the sample tree holds `plugin/skills/install/SKILL.md` with a pointer in a bracket of its own; the file set of `test_it_writes_the_code_the_harness_and_the_core_pages_only` takes `skills/install/SKILL.md` and no file under `plugin/skills/`; a test checks that the written skill has lost that bracket; a test checks that `--check` prints a line for a pointer outside a bracket in `plugin/skills/install/SKILL.md`; the names of these tests hold `plugin_skill`.
> - [ ] `uv run guppi render`: `plugin/skills/install/SKILL.md`
> - [ ] read `estimate-plugin-install-writes-guppi-into-an-empty-project`

> **ratification:**
> ```
> - decision[case 818.1][create][rule-plugin-install]{ref:rule-harness}{tags:harness,plugin,render}
> - decision[case 818.1][create][estimate-plugin-install-writes-guppi-into-an-empty-project]{ref:rule-plugin-install}{tags:plugin,harness}
> - decision[case 818.1][update][rule-clean-branch]{ref:rule-clean-branch}
> ```

### Case 818.2 — The sprint reads the install through /guppi:install

> **given:**
> `estimate-sprint-plugin-installs-as-a-plugin`: its Criterion is replaced whole.
> **＋** `rule-plugin-install`: the rule of `/guppi:install`.
> **＋** `rule-clean-branch`: the rule of `guppi ship` and of its option `--allow-draft`.
> **＋** `vault/raw/2026-10-14/1907/cases/case-816.md` and `vault/raw/2026-10-14/1907/cases/case-821.md`: the Cases of this session that make the clean version a plugin with its catalogue `guppi-marketplace`, and add `--allow-draft`.
> **＋** `/plugin marketplace add <folder>` and `/plugin install guppi@guppi-marketplace`: the commands of Claude Code that add a catalogue and install a plugin from it.
> **＋** `.claude/skills/hi/SKILL.md`: the skill `/hi` that opens a working session.

> **when:**
> In a session of the sprint `plugin` before its close, someone writes the clean version into a local folder by `uv run --project .guppi guppi ship --allow-draft <folder>`, as `rule-clean-branch` sets it.
> **＋** In an empty project, that person adds the folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and types `/guppi:install`, as `rule-plugin-install` sets it.
> **＋** That person then reopens Claude Code in the project and types `/hi`.

> **then:**
> The catalogue adds with no error.
> **＋** The plugin installs with no error.
> **＋** `/guppi:install` copies GUPPI into the project with no error.
> **＋** `/hi` opens a working session in that project.

> **tasks:**
> - [ ] update `estimate-sprint-plugin-installs-as-a-plugin`
>   - set:
>     ```
>     status: pending
>     purpose: Whether the clean version, written into a local folder by guppi ship --allow-draft, installs as a Claude Code plugin into an empty project, /guppi:install copies GUPPI there, and /hi runs there
>     method: "by hand, in a session of the sprint plugin before its close: the clean version written into a local folder by uv run --project .guppi guppi ship --allow-draft, that folder added as a catalogue in an empty project by /plugin marketplace add, guppi installed from it by /plugin install guppi@guppi-marketplace, /guppi:install typed, Claude Code reopened there and /hi typed, read against the Criterion"
>     ```
>   - change: `the Criterion replaced whole — the install is read from a local copy that guppi ship --allow-draft writes, and /guppi:install copies GUPPI into the empty project before /hi runs there`
> - [ ] read `estimate-sprint-plugin-installs-as-a-plugin`

> **ratification:**
> ```
> - decision[case 818.2][update][estimate-sprint-plugin-installs-as-a-plugin]{ref:entity-sprint-plugin}
> ```
