<!-- approved 07:15:12 · session 44ee5004 -->

# Session 1907 — sprint plugin

## Case 816 — The clean branch is a plugin and its catalogue

> **context:**
> Claude Code installs a plugin from a catalogue. The catalogue, `.claude-plugin/marketplace.json`, names its owner and lists each plugin with the place of its files. The manifest, `.claude-plugin/plugin.json`, names the plugin and gives its version. The name of the plugin is the prefix of its own commands. Today the workflow `.github/workflows/prod.yml` writes the clean version that `guppi ship` builds to the branch `prod`, but the clean version holds neither file, so Claude Code cannot add `prod` as a catalogue or install from it. A Glob `**/{plugin.json,marketplace.json}` over the repository printed nothing. The person chose the following. A folder `plugin/` of this repository holds both files with no version, and `guppi ship` copies them into `.claude-plugin/` of the clean version and adds the version, so no branch of this repository is a plugin. The catalogue `guppi-marketplace` of the owner `kirMykholap` lists the one plugin `guppi`, whose source is the root of `prod`. The version comes from the tags, which now take three parts, `prod-x.y.z`, the first being `prod-0.2.0`. A run with no such tag in its history stops and writes nothing. CI runs `claude plugin validate` on the clean folder before it commits, and `tests/test_ship.py` checks the two files in `make test`. A new Estimate on `rule-clean-branch` checks the install (Case 816.1). The Criterion of `estimate-sprint-plugin-ci-writes-a-clean-branch`, whose example tag `prod-1` would no longer write `prod`, is replaced whole (Case 816.2). What `case-guppi` could not read at its source stays a claim for a run to test. The main agent read the command `claude plugin validate`, its warning on a root `CLAUDE.md` and the install commands in the Claude Code docs. Whether `fetch-depth: 0` of `actions/checkout` fetches the tags was not read either. The plugin-structure reference of the official `plugin-dev` plugin in the local plugin cache marks a two-part version as not semantic, which is why the tags take three parts. This Case does not make the plugin an installer. The clean version keeps its skills under `.claude/skills/`, which a plugin does not load, and which skills a plugin carries, how `guppi` runs in a project and what a new project gets are the Frontier items C6, C7 and C9. `estimate-sprint-plugin-installs-as-a-plugin` stands: its `/hi` line waits on C6, and its install line is the install this Case reads, read again there. A Grep `git tag|describe|semver|prod-|\bversion\b` over `guppi/` printed `guppi/lint.py`, `guppi/backlog.py`, `guppi/generate.py`, `guppi/pages.py` and `guppi/ship.py`, and no hit judges a tag or a version. So the form of a version tag is judged once, in `guppi/ship.py`, and the `prod-*` filter of the workflow only starts a run. A Grep `rule-clean-branch|guppi ship` over `vault/wiki/`, `log.md` and `brief.md` left out, printed 23 files. Of those, `estimate-clean-branch-writes-a-clean-copy` lists files that `guppi ship` writes and still holds, since it does not say only those, and its `method` runs `tests/test_ship.py`, whose sample tree gets a tag. `estimate-clean-branch-pages-hold-pointers-only-in-brackets` and `estimate-clean-branch-code-holds-pointers-only-in-brackets` are `passed`. Their readings build a folder in this repository, which holds the tags the owner pushes, and a build before the first tag `prod-0.2.0` exits 1 here. `estimate-lint-runs-every-step` stands, since `guppi ship --check` reads no tag. `entity-sprint-plugin` names `prod-2` in its line of the milestone The clean branch under `## Milestones`, as the push that remained for that milestone; that push and its run have taken place, and the line speaks of nothing this Case changes. `entity-guppi-repository` and `rule-github-repository` say who writes `prod`, which does not change. This Case is built again after Case 821, ratified in this session. Under Case 821.7, `guppi ship` writes nothing and exits 1 while a page with `core: true` stands `draft`, and the workflow never passes `--allow-draft`; `rule-skill-hi`, `rule-work-mode` and `entity-sprint` stay `draft` with `core`, so a run on `prod-0.2.0` writes nothing to `prod`. At `/pre-spec` the person chose that an Estimate that would wait for a run that writes `prod` is read instead from a local copy that `guppi ship --allow-draft <folder>` writes, as Case 818.2 reads the install, so that the pages with `core: true` can become `built` before `prod` is written; `prod` is built once every such page is `built`. So `estimate-clean-branch-installs-as-a-plugin` reads `claude plugin validate` and the install on such a local copy before the close of `plugin`, with that folder as the catalogue, and reads the step of the workflow from its text; Case 816.1 no longer holds the push of the tag. The person chose that `estimate-sprint-plugin-ci-writes-a-clean-branch` keeps the promise of a written `prod`, with a line that the run writes nothing while such a page stands, which points to `estimate-clean-branch-refuses-a-draft-core-page` of Case 821.7 rather than signing that promise again. The tests of `guppi ship` check the version now, the run on GitHub is read after a run that writes `prod`, and the person decides its status at the close of `plugin` when no such run comes before it. A copy with `--allow-draft`, which Cases 818.2 and 821 read, also needs a tag `prod-x.y.z` in the history, so Case 816.2 holds the task that places `prod-0.2.0` after the Work Mode. Under Case 821.2 a string of a test file is a sample, so the line of that Criterion on references says that a sample is no reference. The pairs of this Case keep the words that Cases 818.1, 821.1 and 821.7 anchor on: `the pages it writes.`, `which the clean version does not hold (case 816).` and `` `guppi ship --check` reads no tag (case 816). ``. The first pair of Case 816.1 changes the same sentence of the Purpose of `rule-clean-branch` as Cases 818.1 and 821.3. Those two put their sentences before the words `It gives each page`, and Case 816.1 adds its sentences after the words `the pages it writes.` at the end of that sentence, so no pair touches the words of another. Read side by side, the new texts agree: `.claude-plugin/` and `skills/` of the clean version both come from `plugin/`, which the clean version does not hold, and the skeletons of Case 821.3 are no file of `plugin/`. Two lines of the old Criterion of `estimate-sprint-plugin-ci-writes-a-clean-branch` stand changed, not dropped. The line on references gains that a sample is no reference, and the line on a run whose `uv run guppi ship` exits 1 gains the draft page as a case of it. The Work Mode of Case 819 moves `guppi/ship.py` and `tests/test_ship.py` under `.guppi/`, and the tasks of this Case go to those files wherever they then stand.

> **problem:**
> The branch `prod` holds the clean version, but Claude Code cannot add it as a catalogue or install a plugin from it, and nothing checks in CI that it is a valid plugin.

> **recommend:**
> - **Where the two files come from**
>   - Recommended: (c) a template folder `plugin/` on `main` holds both files with no version; `guppi ship` copies them into `.claude-plugin/` and adds the version.
>   - Answer: (c).
> - **Where the catalogue points**
>   - Recommended: (a) both files on `prod`; the source of the plugin entry is the branch itself, `./`.
>   - Answer: (a).
> - **Whether the plugin has a version**
>   - Recommended: (a) no `version`.
>   - Answer: set the current version to 0.2 and take the version from the tag, written as x.y or with more levels where needed.
> - **The names**
>   - Recommended: (a) plugin `guppi`, catalogue `guppi`, owner `kirMykholap`.
>   - Answer: (b) plugin `guppi`, catalogue `guppi-marketplace`.
> - **How CI checks the files**
>   - Recommended: (c) both: `claude plugin validate` on the clean folder in `prod.yml` before the commit, and our own test in `make test`.
>   - Answer: (c).
> - **What checks that this is done**
>   - Recommended: (a) a new Estimate on `rule-clean-branch`: after a tag push the CI plugin check passes and `prod` is written; by hand, in an empty project, adding the catalogue and installing `guppi` end with no error.
>   - Answer: agreed, (a).
> - **Which page records it**
>   - Recommended: (a) update `rule-clean-branch`.
>   - Answer: agreed, (a).
> - **The form of the version**
>   - Recommended: (b) tags `prod-x.y` or deeper; the manifest fills in the missing parts up to three.
>   - Answer: take three parts at once: the tag itself is `prod-x.y.z`.
> - **The version of a run without a version tag**
>   - Recommended: (a) the version is the newest `prod-x.y.z` tag in the history of the built commit; whole-number tags are ignored; with no such tag `guppi ship` stops and nothing reaches `prod`.
>   - Answer: (a).
> - **The sprint's CI Estimate after the tag change**
>   - Recommended: (a) this Case replaces that Criterion with the same promise for a three-part tag and adds that `guppi ship` stops when no such tag stands in the history.
>   - Answer: agreed, (a).
> - **What the sprint's CI Estimate reads while the build refuses draft pages**
>   - Recommended: (a) keep the promise of a written `prod`, and add that the run writes nothing while a draft page with `core: true` stands; the tests check the version now, the run is read after the first run that writes `prod`, and the person decides its status at the close when none comes.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: build the Case again after Case 821, under which a run of `prod.yml` writes nothing while `rule-skill-hi`, `rule-work-mode` and `entity-sprint` stand `draft` with `core: true`.
>   - Taken: the `method` of `estimate-clean-branch-installs-as-a-plugin` waits for the first run that writes `prod`; the push of the tag moves to Case 816.2 as the placing of `prod-0.2.0` after the Work Mode; the Criterion of `estimate-sprint-plugin-ci-writes-a-clean-branch` says that a sample is no reference and that the run writes nothing while such a page stands, and its `method` reads the tests now and the run after the first one that writes `prod`.
> - **Change**
>   - Asked: at `/pre-spec`, the person chose that every Estimate that waits for a run that writes `prod` is read from a local copy that `guppi ship --allow-draft <folder>` writes, and that `prod` is built once every page with `core: true` is `built`; the word "first" stands only for an event that has never happened.
>   - Taken: `estimate-clean-branch-installs-as-a-plugin` reads `claude plugin validate` and the install on a local copy built with `--allow-draft`, that folder being the catalogue, before the close of `plugin`, and reads the CI step from the text of the workflow; the `method` of `estimate-sprint-plugin-ci-writes-a-clean-branch` waits for a run that writes `prod`, not the first one, as ratified.

### Case 816.1 — The clean version holds the manifest and the catalogue

> **given:**
> `rule-clean-branch`: the rule of `guppi ship` and of the workflow that writes `prod`.
> **＋** `estimate-clean-branch-installs-as-a-plugin`: the new check that the clean branch installs as a plugin.
> **＋** `plugin/plugin.json` and `plugin/marketplace.json`: the templates of the manifest and the catalogue.
> **＋** `.claude-plugin/`, `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`: the folder and the two files that the clean version holds.
> **＋** `guppi/ship.py`: the code of `guppi ship`.
> **＋** `.github/workflows/prod.yml`: the workflow that writes `prod`.
> **＋** `tests/test_ship.py`: the tests of `guppi ship`.
> **＋** `vault/raw/2026-10-15/0553/cases/case-821.md`: the Case of this session that adds the option `--allow-draft` of `guppi ship`.

> **when:**
> `uv run guppi ship <folder>`, or `uv run guppi ship --allow-draft <folder>` into a local folder, builds the clean version, as `rule-clean-branch` sets it, and `claude plugin validate` runs on that folder.
> **＋** In an empty project, someone adds that folder to Claude Code as a catalogue and installs the plugin `guppi` from it.

> **then:**
> `uv run guppi ship <folder>` writes `.claude-plugin/plugin.json` into the clean version, copied from `plugin/plugin.json`, with the `name` `guppi`, a description, the author `kirMykholap` and the repository of the project on GitHub.
> **＋** It writes `.claude-plugin/marketplace.json`, copied from `plugin/marketplace.json`, with the `name` `guppi-marketplace`, the owner `kirMykholap` and one entry, the plugin `guppi`, whose source is the root of the branch.
> **＋** `claude plugin validate` passes on that folder.
> **＋** Before a run of `.github/workflows/prod.yml` commits, it runs `claude plugin validate` on the clean folder.
> **＋** The catalogue adds to Claude Code, and the plugin `guppi` installs from it, with no error.
> **－** A run whose `claude plugin validate` fails fails and writes nothing to `prod`.
> **－** The clean version holds no folder `plugin/`, and this repository holds no folder `.claude-plugin/`.
> **－** Which skills the installed plugin `guppi` loads is no part of this promise.

```then
create:
- slug: estimate-clean-branch-installs-as-a-plugin
  ref: rule-clean-branch
  kind: QA
  purpose: Whether the clean version holds the manifest of the plugin guppi and the catalogue guppi-marketplace, passes claude plugin validate, which CI runs before prod is written, and installs as a plugin with no error
  method: 'uv run pytest tests/test_ship.py; by hand, after the Work Mode of this change: uv run guppi ship --allow-draft into an empty local folder, claude plugin validate run on that folder, the two files of its .claude-plugin/ and the step of .github/workflows/prod.yml that runs claude plugin validate, and in an empty project an add of that folder as a catalogue and an install of guppi from it, read against the Criterion'
  tags:
  - ci
  - plugin
update:
- slug: rule-clean-branch
  replace:
  - old: and keeps in its link fields only the pages it writes.
    new: 'and keeps in its link fields only the pages it writes. It also writes the folder `.claude-plugin/`, which makes the clean version a Claude Code plugin and the catalogue that lists it: `plugin.json`, the manifest of the plugin `guppi`, and `marketplace.json`, the catalogue `guppi-marketplace` of the owner `kirMykholap`, whose one entry is the plugin `guppi` at the root of the branch, `./`. It copies both from the folder `plugin/` of this repository, which no branch of this repository loads as a plugin and which the clean version does not hold (case 816).'
  - old: and writes none when nothing changed or when the command exits 1.
    new: and writes none when nothing changed or when the command exits 1. Before it commits, it installs Claude Code and runs `claude plugin validate` on the clean folder, and writes nothing when that check fails (case 816).
  set:
    implementation_ref:
    - guppi/ship.py
    - tests/test_ship.py
    - .github/workflows/prod.yml
    - plugin/plugin.json
    - plugin/marketplace.json
  change: the clean version holds the manifest of the plugin guppi and the catalogue guppi-marketplace, copied from plugin/, and CI runs claude plugin validate before it commits
```

```tasks
- [x] create `estimate-clean-branch-installs-as-a-plugin`
- [x] update `rule-clean-branch`
- [x] `plugin/plugin.json`: the template of the manifest with no `version`: `name` `guppi`, the `description` `A Claude Code harness governed by ratified decisions, and the Obsidian vault it compiles into`, `author` `{"name": "kirMykholap"}`, `repository` `https://github.com/kirMykholap/GUPPI`.
- [x] `plugin/marketplace.json`: the template of the catalogue: `name` `guppi-marketplace`, `owner` `{"name": "kirMykholap"}`, `plugins` with one entry, `name` `guppi`, `source` `./` and the same description.
- [x] `guppi/ship.py`: `guppi ship <folder>` copies `plugin/plugin.json` and `plugin/marketplace.json` into `.claude-plugin/` of the clean version and writes no file of `plugin/`; the docstring names both files.
- [x] `.github/workflows/prod.yml`: a step between the build and the commit installs Claude Code and runs `claude plugin validate "$RUNNER_TEMP/clean"`, so that a failed check fails the run before anything is pushed; the comment at the top names that step.
- [x] `tests/test_ship.py`: the sample tree holds `plugin/plugin.json` and `plugin/marketplace.json`; the file set of `test_it_writes_the_code_the_harness_and_the_core_pages_only` takes `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` and no file of `plugin/`; a test reads both written files and checks the keys and the values that the `then` of this Case names.
- [x] read `estimate-clean-branch-installs-as-a-plugin`
```

### Case 816.2 — The version of the plugin comes from a tag prod-x.y.z

> **given:**
> `estimate-sprint-plugin-ci-writes-a-clean-branch`: its Criterion is replaced whole.
> **＋** `rule-clean-branch`: the rule of `guppi ship` and of the workflow that writes `prod`.
> **＋** `guppi/ship.py`: the code of `guppi ship`, which reads the tags and writes `.claude-plugin/plugin.json`.
> **＋** `.github/workflows/prod.yml`: the workflow that writes `prod`.
> **＋** `tests/test_ship.py`: the tests of `guppi ship`.
> **＋** `estimate-clean-branch-refuses-a-draft-core-page` and `vault/raw/2026-10-15/0553/cases/case-821.md`: the check that no clean version is built while a page with `core: true` is `draft`, and the Case of this session that creates it and makes a string of a test a sample.
> **＋** `prod-0.2.0`: the first tag of a version.

> **when:**
> In a session of the sprint `plugin` before its close, the owner pushes a tag `prod-x.y.z`, such as `prod-0.2.0`, on a commit of the branch `plugin` to the repository of the project on GitHub, and the workflow `.github/workflows/prod.yml` runs on that commit.
> **＋** `uv run guppi ship <folder>` runs on a commit with no tag `prod-x.y.z` in its history.

> **then:**
> The run writes the clean version that `uv run guppi ship` builds to the branch `prod`, as one new commit on top of its last commit, or as its first commit when `prod` does not stand yet, whose message names the commit it was built from.
> **＋** The run pushes to `prod` with the deploy key whose private half is the secret `PROD_DEPLOY_KEY`, which the bypass list of the ruleset on `prod` lets through.
> **＋** `prod` holds each page with `core: true` and no other page.
> **＋** No text of the clean version holds a reference to a case or a decision, a link to a page that the clean version leaves out, or a mention of a session of this repository; a sample, as `rule-clean-branch` sets it, such as a string of a test, is no reference.
> **＋** The clean version holds no data of the sessions of this repository, such as its Frontier and its sprint.
> **＋** The `version` of `.claude-plugin/plugin.json` on `prod` is the number of the highest tag `prod-x.y.z` in the history of the commit it was built from, such as `0.2.0` for `prod-0.2.0`, and a tag of another form, such as `prod-2`, gives no version.
> **＋** The `on:` block of `.github/workflows/prod.yml` starts the same run on a push to `main`.
> **－** `uv run guppi ship <folder>` with no tag `prod-x.y.z` in that history exits 1 and writes nothing, and `uv run guppi ship --check` reads no tag.
> **－** A run whose `uv run guppi ship` exits 1 fails and writes nothing to `prod`, as it does while a page with `core: true` stands `draft`, which `estimate-clean-branch-refuses-a-draft-core-page` checks.
> **－** A run whose clean version equals the last commit of `prod` adds no commit.

```then
update:
- slug: estimate-sprint-plugin-ci-writes-a-clean-branch
  set:
    status: pending
    purpose: Whether CI writes a clean version of the project to a branch of its own, with no case reference and no session data and with the version of its tag prod-x.y.z, and fails when one remains or when no such tag stands in its history
    method: 'uv run pytest tests/test_ship.py for the version of the highest tag, a tag of another form and a commit with no such tag; by hand, after a run of .github/workflows/prod.yml on a tag prod-x.y.z of a commit of plugin that writes prod, before the close of the sprint plugin: its push with the deploy key of the secret PROD_DEPLOY_KEY, the branch prod it wrote, the version in .claude-plugin/plugin.json of prod and the on: block of .github/workflows/prod.yml read against the Criterion; the person''s answer at the close of plugin when no such run comes before it'
  change: the Criterion replaced whole — the run on a tag prod-x.y.z writes prod with the version of that tag, and guppi ship exits 1 with no such tag in the history
- slug: rule-clean-branch
  replace:
  - old: and on each push of a tag `prod-*`, such as `prod-1`, on a commit of another branch.
    new: and on each push of a tag `prod-*` on a commit of another branch. `guppi ship <folder>` gives `.claude-plugin/plugin.json` the version of the highest tag `prod-x.y.z` in the history of the commit it builds, such as `0.2.0` for the tag `prod-0.2.0`; a tag of another form, such as `prod-2`, gives no version, and when no tag `prod-x.y.z` stands in that history `guppi ship <folder>` exits 1 and writes nothing, so the run writes nothing to `prod`; `guppi ship --check` reads no tag (case 816).
  change: the version of the plugin is the highest tag prod-x.y.z in the history, and guppi ship exits 1 with no such tag
```

```tasks
- [x] update `estimate-sprint-plugin-ci-writes-a-clean-branch`
- [x] update `rule-clean-branch`
- [x] `guppi/ship.py`: `guppi ship <folder>` reads the tags `prod-x.y.z` in the history of the commit of the working tree, writes the number of the highest as the `version` of `.claude-plugin/plugin.json`, and exits 1 with a line and nothing written when there is none; the judgment of the form of the tag lives in this module alone; `--check` reads no tag; the docstring says so.
- [x] `tests/test_ship.py`: the sample tree carries a tag `prod-x.y.z` in its history, so the tests that build a folder pass; tests that the highest of two such tags is the version, that a tag such as `prod-2` gives no version, that a tree with no such tag exits 1 and writes nothing, and that `--check` passes on such a tree.
- [ ] stop: after the Work Mode, the owner places the tag `prod-0.2.0` on the last commit of `plugin` and pushes it; the run it starts writes nothing to `prod` while a page with `core: true` stands `draft`, and a copy built with `--allow-draft` finds its version.
- [ ] read `estimate-sprint-plugin-ci-writes-a-clean-branch`
```

## Case 817 — The install Case comes at the first /hi after /guppi:install

> **context:**
> `rule-morph` sets up a new project. At the first `/hi` of a project, one install Case shows the values that the install step finds in git and the values it asks for, and the person ratifies it; the render then writes the settings. The page says that `/hi` puts that Case first while the settings hold no answers of the install, and that no settings file changes outside that Case. Under the installer model of Case 818, the plugin `guppi` carries one skill, `/guppi:install`, which copies the files of the clean version into the project, the settings among them, and the person then reopens Claude Code and types `/hi`, which renders by `guppi render --sync`. So the settings are never empty: the copied `guppi.toml` holds the languages of this repository, and the copied `.claude/settings.json` names the folder of this repository's saved transcripts. The test of the page never fires, and its sentence on the settings files is false. The person chose the following. The install Case stays at the first `/hi`, now after `/guppi:install` and a reopening of Claude Code, since the one rule of `rule-ratification` says that nothing changes without a ratified Decision, and only that order keeps the settings a ratified decision. A key of `guppi.toml`, rendered by `rule-guppi-config`, marks the install as done: the install Case sets it, the clean version holds it unset, and `/hi` puts the install Case first while it is not set. The person agreed, on Case 818, that the install step is no skill named `install`, so that a project never holds both `/install` and `/guppi:install`. This session changes the text of `rule-morph` and the Criterion of its one Estimate only. The page stays `draft`. A later session builds the key, the skill, its step in `/hi` and the change of `guppi ship` that ships the key unset. So `rule-guppi-config`, `rule-clean-branch`, `guppi/config.py` and `guppi/ship.py` do not change here, and Cases 816 and 818, which change `rule-clean-branch`, need no change. `parse` of `guppi/config.py` checks only the keys `documentation_lang` and `chat_lang`, so a later key does not break it. The Purpose of `rule-guppi-config` names those two keys and stays true until that later Case. Whether `/hi` opens a session in a new project at all is the promise of `estimate-sprint-plugin-installs-as-a-plugin`, whose Criterion Case 818.2 replaced: Case 819.1 moves the code under `.guppi/`, so the clean version holds no `pyproject.toml` at its root, and Case 821.3 makes `guppi ship` write `vault/wiki/sprint.md`, `backlog.md` and `brief.md` as skeletons. Two other Cases of this session leave values to the install Case. Case 820.2 adds the keys `test` and `style` to `guppi.toml` and leaves the questions of an install, those two commands among them, to `rule-morph`. Case 821.4 has `guppi ship` write a blank description of the project into `rule-claude-md` and `CLAUDE.md`, which the install Case of `rule-morph` replaces. The person decided, at the pre-spec of this session, that `rule-guppi-config` ships with this repository's values, `test` and `style` included, and that the install Case sets the project's own. So the new text of `rule-morph` and the new Criterion name the description of the project and the commands of `test` and `style` among the values that the install step asks for, and `CLAUDE.md` from `rule-claude-md` among the files that the render writes. The person also decided there that `rule-morph` keeps `core: true`, so the `core: null` of Case 821.7 on `rule-morph` is undone in that Case, and this Case sets no `core`. The milestone line of `rule-morph` on `entity-sprint-plugin` stays open, since the install step is not built, and this Case rewords it to what remains. The bootstrap writes the files before any Case. The new text names that as the one exception to the rule that no settings file changes outside the install Case: the copy and the render of `/hi` take the values as the clean version holds them, and they change no value. A Grep `rule-morph|estimate-morph` over `vault/wiki/`, with `log.md` and `brief.md` left out, printed `sprint.md`, `backlog.md`, `entities/entity-sprint-plugin.md`, `rules/rule-guppi-config.md`, `rules/rule-permissions.md`, `rules/rule-morph.md` and `estimates/estimate-morph-sets-up-the-project-at-the-first-hi.md`. `sprint.md` is written from `entity-sprint-plugin` by `guppi sprint`. The Backlog line on the category set stays true. `rule-guppi-config` leaves the questions of an install to `rule-morph`, which still holds. `rule-permissions` leaves the folder name of another install to `rule-morph`, which still holds. The Criterion of `estimate-morph-sets-up-the-project-at-the-first-hi` is replaced whole, with its `purpose` and `method`. Five of its lines change: the trigger line, on settings that hold no answers, becomes the line on `/guppi:install` and the key of `guppi.toml`; the line on the values it asks for gains the keys `test` and `style` and the description of the project; the line on the render of Work Mode gains `CLAUDE.md` and the key; the exception that no settings file changes before the install Case gains the copy and the render of `/hi`; and the exception on a project whose settings hold the answers now names the key. Its other lines stand word for word.

> **problem:**
> Under the installer model, `/guppi:install` writes the settings of this repository into the project before any `/hi`. So `rule-morph` has no test of a project that is not set up yet, and its rule that no settings file changes outside the install Case is false.

> **recommend:**
> - **Where the person gives the settings of a new project**
>   - Recommended: (a) the install Case at the first `/hi`, after the bootstrap of `/guppi:install`.
>   - Answer: agreed, (a).
> - **How much of the install step this session builds**
>   - Recommended: (a) this session changes the page and its Estimate only; a later session builds the skill and the check in `/hi`.
>   - Answer: agreed, (a).
> - **How `/hi` tells that the project has not been set up yet**
>   - Recommended: (a) `/hi` compares the transcripts folder that the read rules name with the one the project's path gives.
>   - Answer: (b) a new key in `guppi.toml` that the install Case sets and the clean version holds unset.
> - **What checks that this is done**
>   - Recommended: (a) replace the Criterion of `estimate-morph-sets-up-the-project-at-the-first-hi` whole.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at the pre-spec, name the description of the project and the keys `test` and `style` among the values of the install Case, and `CLAUDE.md` among the files it renders; keep the milestone line of `rule-morph` on `entity-sprint-plugin` open with what remains; fix the sentence of `context` on what the copy holds.
>   - Taken: the new text of `rule-morph`, the new Criterion and `context` name them, and an `update` of `entity-sprint-plugin` rewords its milestone line.

> **given:**
> `rule-morph`: the rule of the install step at the first `/hi`.
> **＋** `estimate-morph-sets-up-the-project-at-the-first-hi`: its Criterion is replaced whole.
> **＋** `rule-plugin-install`, `vault/raw/2026-10-15/0553/cases/case-818.md`, `vault/raw/2026-10-15/0553/cases/case-820.md` and `vault/raw/2026-10-15/0553/cases/case-821.md`: the rule of `/guppi:install`, which copies GUPPI into the project, and the Cases of this session that create it, add the keys `test` and `style` and blank the description of the project.
> **＋** `entity-sprint-plugin`: the sprint page whose milestone The plugin names `rule-morph` and whose `## Backlog` keeps the category set as data.
> **＋** `rule-guppi-config`, `guppi.toml`, `rule-claude-md` and `CLAUDE.md`: the settings file, the file that holds the description of the project, and the rules that render them.
> **＋** `rule-permissions`: the rule of the read rules of the saved transcripts under `~/.claude/projects`.
> **＋** `rule-skill-hi` and `raw/<date>/<hi HHMM>/frontier.md`: the rule of `/hi` and the Frontier it writes.
> **＋** `rule-ratification`: the one rule, that nothing changes without a ratified Decision.

> **when:**
> In a project where the person installed the plugin `guppi` and typed `/guppi:install`, as `rule-plugin-install` sets it, and whose `guppi.toml` does not mark the install step of `rule-morph` as done, the person reopens Claude Code and types `/hi`.

> **then:**
> `/hi` opens the session as `rule-skill-hi` sets it, and puts the install Case first, before the items of `raw/<date>/<hi HHMM>/frontier.md`.
> **＋** The install step takes the name of the main branch and the git remote from git, and the name of the project's folder of saved transcripts under `~/.claude/projects` from the path of the project.
> **＋** It asks the person only for the values it cannot find, such as `documentation_lang`, `chat_lang`, the commands of the keys `test` and `style` of `guppi.toml`, and the description of the project.
> **＋** Every value stands in that one install Case, which the person ratifies or corrects.
> **＋** The Work Mode of the same session writes the settings by the render of the rule pages that hold them, such as `guppi.toml` from `rule-guppi-config`, the description of the project in `CLAUDE.md` from `rule-claude-md` and the read rules of the saved transcripts from `rule-permissions`, and `guppi.toml` then marks the install as done.
> **－** Between `/guppi:install` and the ratified install Case, no settings file changes but by the copy of `/guppi:install` and the render that `/hi` runs.
> **－** The install step is no skill named `install`.
> **－** The install step does not ask for the category set: the project takes the development set, as `entity-sprint-plugin` keeps the category set as data in its `## Backlog`.
> **－** The install step reads no code of the project and creates no page for it.
> **－** A project whose `guppi.toml` marks the install as done gets no install Case at `/hi`.

```then
update:
- slug: rule-morph
  set:
    purpose: 'Prevents a new install of GUPPI from running on the settings of another machine or project: at the first /hi after /guppi:install, while guppi.toml does not mark the install as done, one install Case that the person ratifies sets them'
  sections:
    Purpose: |-
      Prevents a new install of GUPPI from running on the settings of another machine or project: at the first `/hi` after `/guppi:install`, while `guppi.toml` does not mark the install as done, one install Case that the person ratifies sets them. The plugin `guppi` installs GUPPI by its skill `/guppi:install`, which copies the files of the clean version into the project, the settings among them, as `rule-plugin-install` sets it. Until the install Case, those settings name another project: `guppi.toml` holds the languages and the commands of the keys `test` and `style` of this repository, `CLAUDE.md` holds a blank description of the project, the read rules of [[rule-permissions]] name the folder of this repository's saved transcripts under `~/.claude/projects`, and the code takes the main branch to be `main` (as set in case 693).

      A key of `guppi.toml`, which [[rule-guppi-config]] renders, marks the install as done: the install Case sets it, and the clean version holds it unset. The install step is a skill of the project whose name is not `install`, so that a project never holds both `/install` and `/guppi:install`. After `/guppi:install`, the person reopens Claude Code in the project and types `/hi`. `/hi` opens the session as always and, while `guppi.toml` does not mark the install as done, puts the install Case first, before the Frontier: a Case lives only inside a session that `/hi` opened. The skill takes the name of the main branch and the git remote from git, and the name of the project's folder of saved transcripts from the path of the project, and asks the person only for the rest, such as the language of the repository and of the chat, the commands of the keys `test` and `style` of `guppi.toml`, and the description of the project. Every value stands in that one Case; the person ratifies or corrects it, and the Work Mode of the same session writes the settings by the render of the rule pages that hold them, such as [[rule-guppi-config]] for `guppi.toml`, [[rule-claude-md]] for the description of the project in `CLAUDE.md` and [[rule-permissions]] for the read rules, and so sets the key. No settings file changes outside that Case but by the copy of `/guppi:install` and the render that `/hi` runs, which take the values as the clean version holds them ([[rule-ratification]]).

      The install step does not set the category set: every project takes the development set — entity, rule, estimate — and the category set as data waits as a line of the `## Backlog` of [[entity-sprint-plugin]]. It reads no code of the project and creates no page for it: the pages of a project with code of its own grow one Case at a time. The key, the skill, its step in `/hi` and the clean version that holds the key unset are built in the milestone The plugin of [[entity-sprint-plugin]] (as set in cases 802 and 817).
  change: the install Case comes at the first /hi after /guppi:install, while a key of guppi.toml does not mark the install as done; the install step is no skill named install
- slug: estimate-morph-sets-up-the-project-at-the-first-hi
  set:
    status: pending
    purpose: Whether the first /hi after /guppi:install, in a project whose guppi.toml does not mark the install as done, puts one install Case first with the values it finds and the values the person gives, and whether the settings change only by the copy, the render of /hi and the render after that Case is ratified
    method: 'by hand, after the session whose Work Mode builds the install skill of rule-morph and its step in /hi: in an empty project, the plugin guppi installed, /guppi:install typed, Claude Code reopened and /hi typed; the transcript of that session and the files its Work Mode writes read against the Criterion, recorded in the estimate line'
  change: the Criterion replaced whole — the install Case comes at the first /hi after /guppi:install, while guppi.toml does not mark the install as done
- slug: entity-sprint-plugin
  replace:
  - old: '- [[rule-morph]] — the install step that the first `/hi` of a new install runs'
    new: '- [[rule-morph]] — the install step that the first `/hi` after `/guppi:install` runs; what remains: the install skill, its step in `/hi`, the key of `guppi.toml` that marks the install as done, and the clean version that ships that key unset'
  change: the milestone line of rule-morph names what remains of the install step
```

```tasks
- [x] update `rule-morph`
- [x] update `estimate-morph-sets-up-the-project-at-the-first-hi`
- [x] update `entity-sprint-plugin`
- [x] `uv run guppi sprint`
- [ ] read `estimate-morph-sets-up-the-project-at-the-first-hi`
```

## Case 818 — The plugin guppi installs GUPPI into a project

> **context:**
> The branch `prod` holds the clean version of GUPPI that `guppi ship` builds: GUPPI's code, the harness `.claude/` and `CLAUDE.md`, already rendered, and each page with `core: true`. Case 819 of this session moves the code into a folder of its own, `.guppi/`. Case 816 makes that branch a catalogue, `guppi-marketplace`, and the clean version a plugin, `guppi`. But Claude Code loads the skills of a plugin from a folder `skills/` at its root, and the clean version keeps its skills under `.claude/skills/`. So an install of the plugin gives the person nothing to run, and an empty project gets no file of GUPPI. The person chose the plugin as an installer, model B. The plugin carries one skill of its own, `install`, typed as `/guppi:install`. That skill copies the files of the plugin, as `guppi ship` built them, into the project open in Claude Code, and runs no `guppi` command. The first `/hi` of the project then renders the harness from the project's own rule pages, by its line `guppi render --sync`. Until the open item on what a new project gets (C9) is decided, the skill copies every file of the plugin but its own: those under `.claude-plugin/`, `skills/` and `.git/`. A later Case on that item narrows the set. After Case 819, the copied files hold GUPPI's code under `.guppi/` and no `pyproject.toml` or `uv.lock` at the root, so a project's own `pyproject.toml` no longer stops the install; a file under `.guppi/` that already stands does stop it. Case 819.4 adds two steps to the skill: it checks `uv` before it writes, and it runs `uv sync` in `.guppi/` after the copy. Case 819.4 writes the Purpose and the Render of `rule-plugin-install` whole. The texts this Case creates for that page are its first form, written to agree with Case 819.4 but for those two steps. The `then` of Case 818.1 leaves `uv` and the Python environment to Case 819.4, and its check that each copied file stands and its last message come before and after the `uv sync` step of Case 819.4, so the two orders agree. In a project where one of those files already stands, the skill lists the files, writes nothing and stops. Merges and updates are left to later items. The skills of a project keep their bare names, such as `/hi`; only the skill of the plugin carries the prefix of the plugin. A new rule, `rule-plugin-install`, holds the text of the skill in its Render, written to `plugin/skills/install/SKILL.md`. It has no `core: true`, so a project that installs GUPPI does not hold it. `guppi ship` copies that file to `skills/install/SKILL.md` of the clean version (Case 818.1). The Criterion of `estimate-sprint-plugin-installs-as-a-plugin` expects `/hi` to run right after the plugin installs, which is no longer true under model B, so Case 818.2 replaces it. In the plugin-structure skill of the official `plugin-dev` plugin in the local plugin cache, `case-guppi` read that a skill file may name `${CLAUDE_PLUGIN_ROOT}` as the path of the plugin, and in its skill-development skill that `name` is required in the frontmatter of a skill. That the skill is called as `/guppi:install` is what the main agent read in the Claude Code docs; `case-guppi` did not read it at its source, and the reading of Case 818.1 tests it. The vault query found no page on the install of the plugin. Near pages are `rule-clean-branch`, which builds the clean version, and `rule-morph`, the install Case at the first `/hi`, which Case 817 of this batch owns. A Glob `vault/**/*plugin-install*` printed `vault/wiki/estimates/estimate-sprint-plugin-installs-as-a-plugin.md` alone, so both new slugs are free. The tags `harness`, `plugin` and `render` exist in `vault/wiki/tags.md`. A Grep `install` (case-insensitive) over `vault/wiki/rules/` printed `rule-clean-branch.md`, `rule-guppi-config.md`, `rule-github-repository.md`, `rule-morph.md` and `rule-permissions.md`. A Grep of the same pattern over `.claude/` printed nothing. `rule-clean-branch` changes here. `rule-guppi-config` leaves the questions of an install to `rule-morph`. `rule-github-repository` says that an install does not carry the settings of the repository on GitHub. `rule-permissions` leaves the name of the transcripts folder of another install to `rule-morph`. Each of these stays true. `rule-morph` sets what the first `/hi` does after the install, and this Case does not touch that moment. Case 817 sets that its own skill is not named `install`, so a project never holds both `/install` and `/guppi:install`. Until Case 817 lands, the copied `.claude/settings.json` names the transcripts folder of this repository. Today `guppi ship` leaves out `vault/wiki/sprint.md`, `vault/wiki/backlog.md` and `vault/wiki/brief.md`, which the `@` lines of `/hi` name. Case 821.3 ships them as skeletons, so the first `/hi` of a new project starts `/sprint-open`. Case 821.7 stops `guppi ship <folder>` while a page with `core: true` stands `draft`, so the workflow writes nothing to `prod` while `rule-skill-hi`, `rule-work-mode` and `entity-sprint` stand `draft`, likely until after the close of the sprint `plugin`. So the person chose that the sprint reads the install from a local copy that `guppi ship --allow-draft` writes, before the close (Case 818.2). That local folder holds `.claude-plugin/marketplace.json` of Case 816, the catalogue `guppi-marketplace` whose plugin `guppi` stands at `./`. The person adds it by `/plugin marketplace add <folder>` and installs by `/plugin install guppi@guppi-marketplace`. `case-guppi` read the form `/plugin install <plugin>@<catalogue>` in the README of the official catalogue in the local plugin cache, and `/plugin marketplace add` with a catalogue on GitHub in the README of its plugin `claude-security`. That a local folder is accepted as a catalogue, and that a plugin at a relative path loads in place, is what the main agent read in the Claude Code docs. `case-guppi` did not read it at its source, and the reading of Case 818.2 tests it. At `/pre-spec` the person chose that every Estimate that waited for a run that writes `prod` reads a local copy that `guppi ship --allow-draft` writes, so the pages with `core: true` can become `built` without `prod`. So the reading of Case 818.1 takes the same local install as Case 818.2. Its `method` waits for no run of `.github/workflows/prod.yml`, as `rule-estimates-schema` asks of the word first, which stands only for an event that has never happened. Case 819.3 replaces the Criterion of `estimate-clean-branch-writes-a-clean-copy` with the code under `.guppi/`. Its line that `guppi ship` writes no file that a page without `core: true` renders in full names the path that the page governs, `plugin/skills/install/SKILL.md`, which the clean version does not hold. Its `--check` line covers each file that `guppi ship` would write outside `vault/`, `skills/install/SKILL.md` included. The copy to `skills/` is promised by the new Estimate of Case 818.1, so it is not signed twice. The other Estimates of `rule-clean-branch` speak of pointers in pages and code, which this Case does not change, and `estimate-clean-branch-installs-as-a-plugin` of Case 816 leaves the skills of the plugin out of its promise. A Grep `estimate-sprint-plugin-installs-as-a-plugin` over `vault/wiki/` printed `brief.md`, `log.md` and `entities/entity-sprint-plugin.md`. The entity names the Estimate in its `estimates` field, and its Purpose still holds. A Grep `project_root\(\)|REPO\b|ROOT = |Path\(__file__\)` over `tests/` printed `test_lint.py`, `test_schemas.py`, `test_generate.py`, `test_materialize.py`, `test_orchestration.py` and `test_case_schema.py`. Those files read the `schema.yaml` of a category, `case-schema.md`, `case-example.md`, `orchestration.md` and the `Makefile`, and this Case changes none of those. The new rule takes `rule-harness`, the map of the harness tools, as its parent, as `rule-render-harness` does. The pair of Case 818.1 on `rule-clean-branch` puts its sentence before the words `It gives each page`, which it keeps. Case 816.1 adds its sentences after the words `the pages it writes.` of the same sentence, and Case 822.3 puts its own sentence on the skeletons before `It gives each page` too and keeps those words, so each `old` hits the page once in any order. Read side by side, the texts agree: `skills/` of the clean version comes from `plugin/skills/`, and the clean version holds no folder `plugin/`. The Criterion of `estimate-sprint-plugin-installs-as-a-plugin` is replaced whole. Its one `When` line, someone installs the clean branch as a plugin into an empty project, opens Claude Code there and types `/hi`, becomes the three `when` lines of Case 818.2: the local copy, the install from it with `/guppi:install`, and the reopening of Claude Code before `/hi`. The task on `guppi/ship.py` adds a copy and no new judgment of a text: it judges the copied skill by `judged`, as it judges each other file. Case 819.3 changes other sentences of `rule-clean-branch`: the list of what `guppi ship` writes, and what it leaves out. The new texts of Case 818.1 name no `guppi/` and no `tests/` outside `.guppi/`, so the path pairs of the `reword` of Case 819.1 leave them as they are. The `when` of Case 818.1 names `uv run guppi ship`, which Case 819.1's `reword` turns into the form with `--project .guppi`, since the decision lines of Case 818 come before it in the ledger. The `method` of its Estimate and the texts of Case 818.2 already name the form with `--project .guppi` and `.guppi/tests/`, which the pairs of that `reword` do not hit. Case 822.3 replaces the last sentence of the Purpose that Case 819.4 writes for `rule-plugin-install`. Case 818.1 writes that sentence too, in its first form of the page, which Case 819.4 replaces whole. So no words of Case 818 that Cases 819.4 and 822.3 leave alone change here. Case 822 replaces Case 821 under a new number, with the same promises and slugs: its sub-cases 822.3, 822.4, 822.6 and 822.8 are 821.3, 821.4, 821.5 and 821.7 of the sentences above, and `rule-morph` keeps `core`. Its file was read whole for this build. Cases 820.5, 820.7 and 822.4 change the paragraph of `rule-clean-branch` that holds the sentence on `guppi ship --check`. So Case 818.1 leaves that sentence alone, and its own sentence says that `--check` judges the files under `plugin/skills/` in place, as Case 822.6 does for `.github/workflows/checks.yml`. The Work Mode of Case 819 moves the tests, and the task of Case 818.1 on the tests of `guppi ship` goes to that file wherever it then stands.

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
> - **Change**
>   - Asked: at `/pre-spec`, read every Estimate that waited for a run that writes `prod` from a local copy that `guppi ship --allow-draft` writes, since a run that writes `prod` has already happened and the word first in a `method` stands only for an event that never happened.
>   - Taken: the `when` of Case 818.1 and the `method` of its Estimate read the install from that local copy, by the same commands as Case 818.2, with no run of `.github/workflows/prod.yml` and no word first.

### Case 818.1 — /guppi:install copies GUPPI into an empty project

> **given:**
> `rule-plugin-install`: the new rule of the skill of the plugin.
> **＋** `estimate-plugin-install-writes-guppi-into-an-empty-project`: the new check of the install.
> **＋** `plugin/skills/install/SKILL.md` and `skills/install/SKILL.md`: the skill `/guppi:install` as the Render writes it in this repository, and as the clean version holds it.
> **＋** `.claude-plugin/`, `skills/` and `.git/`: the plugin's own files, which the install does not copy.
> **＋** `CLAUDE.md`, `.claude/settings.json`, `.claude/skills/` with `/hi`, `.guppi/` and `vault/wiki/`: files of the plugin that the install copies.
> **＋** `rule-clean-branch`: the rule of `guppi ship`.
> **＋** `vault/raw/2026-10-15/0553/cases/case-816.md`, `vault/raw/2026-10-15/0553/cases/case-819.md` and `vault/raw/2026-10-15/0553/cases/case-822.md`: the Cases of this session that make the clean version a plugin, move the code into `.guppi/`, set what a new project gets, and change `rule-clean-branch` and `rule-plugin-install`.
> **＋** `guppi/ship.py` and `tests/test_ship.py`: the code of `guppi ship` and its tests.
> **＋** `uv run --project .guppi guppi ship --allow-draft <folder>`, `/plugin marketplace add <folder>` and `/plugin install guppi@guppi-marketplace`: the local copy of the clean version, and the commands of Claude Code that add it as a catalogue and install the plugin from it.

> **when:**
> `uv run guppi ship <folder>` builds the clean version, as `rule-clean-branch` sets it, and `uv run guppi ship --check` judges the working tree.
> **＋** The person writes the clean version into a local folder by `uv run --project .guppi guppi ship --allow-draft <folder>`, adds that folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` in the project open in Claude Code, as `rule-plugin-install` sets it.

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

```then
create:
- slug: rule-plugin-install
  type: rule
  ref: rule-harness
  kind: Leaf
  purpose: Prevents a project that installs the plugin guppi from getting a part of GUPPI, or from losing a file of its own to it
  enforcement: render
  governs: plugin/skills/install/SKILL.md
  render_mode: full
  tags:
  - harness
  - plugin
  - render
  sections:
    Purpose: 'Prevents a project that installs the plugin `guppi` from getting a part of GUPPI, or from losing a file of its own to it. The plugin, which the catalogue `guppi-marketplace` on the branch `prod` lists, is an installer. It carries one skill of its own, `install`, which the person types as `/guppi:install` in the project to install into. `guppi ship` copies the skill from `plugin/skills/install/SKILL.md`, which the Render of this page writes, to `skills/install/SKILL.md` of the clean version ([[rule-clean-branch]]). The skill copies into the project each file of the plugin but its own files, those under `.claude-plugin/`, `skills/` and `.git/`. Those files are the code of GUPPI in `.guppi/`, the harness `.claude/` and `CLAUDE.md`, the files at the root and the pages with `core: true`, as `guppi ship` built them. It writes nothing when one of those files already stands in the project, and it runs no `guppi` and no `git` command. The project then runs on its own copy: its first `/hi` renders the harness from its own rule pages, and [[rule-morph]] sets its settings there. The skills of the project keep their bare names, such as `/hi`; only the skill of the plugin carries the prefix of the plugin (case 818). This page has no `core: true`, so a project that installs GUPPI does not hold it. Which files a new project gets waits for a Case of its own.'
    Render: |-
      <!-- rule-plugin-install -->
      ---
      name: install
      description: "Install GUPPI into the project open in this session: copy its files from this plugin, then the person reopens Claude Code and types /hi. Run it when the person types /guppi:install."
      disable-model-invocation: true
      ---

      Install GUPPI into the project of this session, the folder that Claude Code was opened in. The files come from this plugin, at `${CLAUDE_PLUGIN_ROOT}`. Write nothing into that folder of the plugin.

      1. List each file under `${CLAUDE_PLUGIN_ROOT}`, but the files under `.claude-plugin/`, `skills/` and `.git/`. These are the files to install, each at the same path in the project.
      2. Check which of those paths already stand in the project. When one or more stand, list them, say that the install writes nothing into a project that already holds one of its files, and stop. Write nothing.
      3. Otherwise copy each file to its path in the project, with the folders it needs. Change no other file. Run no `guppi` command and no `git` command.
      4. Check that each file now stands in the project. When one is missing, name it and stop.
      5. Say that GUPPI is installed, and that the person reopens Claude Code in this project and types `/hi`.
      <!-- /rule-plugin-install -->
- slug: estimate-plugin-install-writes-guppi-into-an-empty-project
  ref: rule-plugin-install
  kind: QA
  purpose: Whether guppi ship puts the skill install into the clean version, and whether /guppi:install copies every file of the plugin but its own into a project that holds none of them, and writes nothing into one that holds one
  method: 'uv run --project .guppi pytest .guppi/tests/test_ship.py -k plugin_skill; by hand, after the Work Mode of this change: the clean version written into a local folder by uv run --project .guppi guppi ship --allow-draft; in an empty project, that folder added as a catalogue by /plugin marketplace add, guppi installed by /plugin install guppi@guppi-marketplace, /guppi:install typed and the files of the project read against those of the plugin; in a second empty project with a file CLAUDE.md of its own, /guppi:install typed and its output and the files of that project read against the Criterion'
  tags:
  - plugin
  - harness
update:
- slug: rule-clean-branch
  replace:
  - old: 'It gives each page `origin: guppi`, `sprint: guppi`,'
    new: 'It writes each file under `plugin/skills/` of this repository to the same path under `skills/` of the clean version, where Claude Code finds the skills of a plugin, and judges and cleans it like each other file it writes, and `guppi ship --check` judges each file under `plugin/skills/` in place; the one such file is `plugin/skills/install/SKILL.md`, which the Render of [[rule-plugin-install]] writes (case 818). It gives each page `origin: guppi`, `sprint: guppi`,'
  change: guppi ship writes the skill of the plugin from plugin/skills/ to skills/ of the clean version, and --check judges it in place
```

```tasks
- [x] create `rule-plugin-install`
- [x] create `estimate-plugin-install-writes-guppi-into-an-empty-project`
- [x] update `rule-clean-branch`
- [x] `guppi/ship.py`: `guppi ship <folder>` writes each file under `plugin/skills/` to the same path under `skills/` of the clean version, judged and cleaned by `judged` like each other file, and writes no file of `plugin/skills/` at its own path; `--check` judges each file under `plugin/skills/` in place; the docstring says so.
- [x] `tests/test_ship.py`: the sample tree holds `plugin/skills/install/SKILL.md` with a pointer in a bracket of its own; the file set of `test_it_writes_the_code_the_harness_and_the_core_pages_only` takes `skills/install/SKILL.md` and no file under `plugin/skills/`; a test checks that the written skill has lost that bracket; a test checks that `--check` prints a line for a pointer outside a bracket in `plugin/skills/install/SKILL.md`; the names of these tests hold `plugin_skill`.
- [x] `uv run guppi render`: `plugin/skills/install/SKILL.md`
- [x] read `estimate-plugin-install-writes-guppi-into-an-empty-project`
```

### Case 818.2 — The sprint reads the install through /guppi:install

> **given:**
> `estimate-sprint-plugin-installs-as-a-plugin`: its Criterion is replaced whole.
> **＋** `rule-plugin-install`: the rule of `/guppi:install`.
> **＋** `rule-clean-branch`: the rule of `guppi ship` and of its option `--allow-draft`.
> **＋** `vault/raw/2026-10-15/0553/cases/case-816.md` and `vault/raw/2026-10-15/0553/cases/case-822.md`: the Cases of this session that make the clean version a plugin with its catalogue `guppi-marketplace`, and add `--allow-draft`.
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

```then
update:
- slug: estimate-sprint-plugin-installs-as-a-plugin
  set:
    status: pending
    purpose: Whether the clean version, written into a local folder by guppi ship --allow-draft, installs as a Claude Code plugin into an empty project, /guppi:install copies GUPPI there, and /hi runs there
    method: 'by hand, in a session of the sprint plugin before its close: the clean version written into a local folder by uv run --project .guppi guppi ship --allow-draft, that folder added as a catalogue in an empty project by /plugin marketplace add, guppi installed from it by /plugin install guppi@guppi-marketplace, /guppi:install typed, Claude Code reopened there and /hi typed, read against the Criterion'
  change: the Criterion replaced whole — the install is read from a local copy that guppi ship --allow-draft writes, and /guppi:install copies GUPPI into the empty project before /hi runs there
```

```tasks
- [x] update `estimate-sprint-plugin-installs-as-a-plugin`
- [ ] read `estimate-sprint-plugin-installs-as-a-plugin`
```

## Case 819 — The code of GUPPI stands in .guppi/ and every caller runs it there

> **context:**
> Every hook of `.claude/settings.json`, every skill and agent that calls the code, the `Makefile` and the workflow `.github/workflows/prod.yml` run GUPPI's code through `uv run` at the root of the project. That works only where GUPPI's `pyproject.toml` stands at the root, so Case 818 copies `guppi/`, `pyproject.toml` and `uv.lock` to the root of a user's project as a stopgap until this item. A Python project that has its own `pyproject.toml` cannot take that copy. The person chose a folder of its own: the package `guppi`, its `pyproject.toml`, its `uv.lock` and its tests move into `.guppi/`, and every caller runs them as `uv run --project .guppi guppi …` and `uv run --project .guppi pytest`. This repository moves its own code there too, so the command has one form here and in a user's project. A Grep `__file__` over `guppi/` printed nothing, and `project_root` of `guppi/event.py` takes the project from `CLAUDE_PROJECT_DIR` or the working folder, so the code reads the project's vault from wherever it stands. For now the root keeps a small development project that takes the package from `.guppi/`, so that a session whose hooks still name the old command keeps working between the move and the render; the person chose to remove it later, by a Case of a later session (Case 819.1). A `.guppi/.gitignore` keeps the environment `.guppi/.venv/` out of git. The tests move into `.guppi/tests/`. This Case ships none of them, since `guppi ship` cleans the whole text of a Python file, strings included. A Grep `[Cc]ases? \d|decision-case-\d|[Ss]ession \d{4}` over `tests/` printed 1725 places in 35 files, mostly sample data. Case 821.2 of this session ships them with only their comments and docstrings cleaned, their other strings kept as samples. Case 821 also ships the passed Estimates, the session files as skeletons and `.github/workflows/checks.yml`. So the Criterion that Case 819.3 writes for `estimate-clean-branch-writes-a-clean-copy` points to the Estimates of Cases 821.1, 821.2, 821.3 and 821.5 for those files, and its line on the brackets it removes leaves out the strings of a test file. Case 821.2 anchors on the words of Case 819.3 on `rule-clean-branch`, ``but not its tests `.guppi/tests/` or its Python environment `.guppi/.venv/`;``, and replaces them, so Case 819.3 keeps those words as they stand. The check of this file applies the pairs of the other Cases first, so it finds the `reword` of Case 819.1 in the sentence that Case 821.2 adds to `rule-clean-branch` on a test file under `.guppi/tests/`. In the ledger the decision lines of Case 819 come before those of Case 821, so `guppi generate` applies this `reword` first and the sentence of Case 821.2 lands after it, untouched. Under the matching of Case 819.2, a path that a `.` or a `/` comes before is not touched anyway. Case 822 replaces Case 821 under a new number, with the same promises and slugs, and its file in `vault/raw/2026-10-15/0553/cases/` was read whole for this build: Cases 821.1, 821.2, 821.3, 821.5 and 821.7 named in this `context` are its Cases 822.1, 822.2, 822.3, 822.6 and 822.8. The sentences of the pages where a pair of Case 819.1 meets a word that Case 820 or Case 822 writes were read again with both case files, and each reads true with both changes. In the sentence that Case 822.2 adds to `rule-clean-branch` on a test file under `.guppi/tests/`, the path stands after a `/`, so under the matching of Case 819.2 the pair `tests/` leaves it alone; and the decision lines of Case 819 come first in the ledger, so that sentence lands after the `reword` in any case. The two new texts fit. The sentence of `rule-clean-branch` on test files under `.guppi/tests/` is written by Case 821.2 and Case 822.2, and the `reword` of this Case leaves it as written, since a `.guppi/tests/` path stands after a `.`. Two lines of the old Criterion of `estimate-clean-branch-writes-a-clean-copy` are changed on purpose. The line on brackets now leaves out the strings of a test file. The line on what is not written now lets in the passed Estimates and points to Cases 821.3 and 821.5 for `.github/` and the session files. Both changes follow what Case 821 ships. The person chose that every text names the new command, the pages and their Criteria included. A Grep `uv run guppi` over `vault/wiki/`, `log.md` and `brief.md` left out, printed 352 places in 204 files. One `reword` changes them as a phrase, on the new page `rule-guppi-package`, whose Purpose holds each `new`. A `reword` replaces text in place in `purpose`, `method` and every section but History and Result, the Criterion included, and sets no Estimate `pending`, so no reading is retired: each Estimate still promises the same thing under the new name of the command. Lessons, Insights and Decision pages keep the old words as records. The paths change too, from `guppi/` and `tests/` to `.guppi/guppi/` and `.guppi/tests/`, in the text and in the link fields `implementation_ref`, `governs` and `code_ref`, which `guppi lint` checks for existence. Today `reword_pattern` of `guppi/generate.py` matches only a whole word, so `tests/` never matches inside `tests/test_ship.py`, and `reword_text` changes only `purpose`, `method` and sections. Case 819.2 teaches it path prefixes. The same function serves the preview of `/pre-spec`, so both sides keep one judgment, and `rename` passes only slugs, which never end with `/`. The new code is live at the librarian's run of the session whose Work Mode builds it, which is the run that applies the pairs. The check of this file and `/pre-spec` in this session run the old matching. Under it, the pairs `guppi/` and `tests/` still hit, where a backtick or a space follows them, so no pair stands without a hit. No anchor of this Case depends on a path that only the new matching changes: the pairs of Case 819.3 anchor on `.guppi/guppi/`, which the old matching also writes in place of `` `guppi/` ``, and the new texts of Cases 819.2 to 819.4 are written in the new forms and come after the `reword` in the ledger. The check of this file previews the `reword` over Decision pages and lessons too, such as `decision-case-807` and `lesson-caseid-run-to-check-an-id-held-a-new-one`; `guppi generate` changes only rules, entities and Estimates, so those hits stand as records. A path prefix would also turn the examples of a user's own project into GUPPI's paths. A Grep `test_cart_view|test_new_client|test_pricing_sync` over the repository, `vault/raw/` and `vault/archive/` left out, printed `vault/wiki/case-example.md`, `vault/wiki/rules/rule-case-example.md`, `vault/wiki/rules/rule-estimates-schema.md`, `vault/wiki/rules/rule-rules-schema.md`, `vault/wiki/rules/schema.yaml` and `vault/wiki/estimates/schema.yaml`. So Case 819.1 rewrites those examples before the `reword` runs, into paths that no pair touches, and states the method forms of `rule-estimates-schema` for both kinds of test folder. The new rule carries `core: true`, since the layout holds in every project. It takes the field by a `set` of its `update`, since a value of a `create` lands as a string and `is_core` of `guppi/pages.py` accepts only the boolean. Until its Estimate passes, the rule stands `draft`, so by Case 821.7 `guppi ship` writes no `prod` while it stands, and a copy for an install by hand is built with `--allow-draft`; its test ships with the other tests as Case 821.2 sets it. The words of the new texts avoid the old command and the old paths, since the `reword` would rewrite them. `lint.py` takes a test path by `TEST_PATH`, which would read `tests/test_ship.py` out of `.guppi/tests/test_ship.py` and look for it at the root; Case 819.1 makes it take both folders, and the texts of the code that `estimate-lint-checks-the-method` and `estimate-prespec-catches-a-method-without-a-form` quote follow the `reword` of their Criteria, so both stand. `interpreter` of `guppi/bashguard.py` skips each option after `uv run`, so under the new form it would read `.guppi` as the program and pass `uv run --project .guppi python` fed a heredoc; Case 819.1 makes it skip the value of `--project`, so `estimate-bash-guard` stands. A Grep `uv run guppi|uv run pytest|uv run ruff|uv run python` over the repository, `vault/` left out, printed 126 places in 35 files: `.claude/settings.json`, `.claude/agents/librarian-guppi.md`, eight skills, `Makefile`, `.github/workflows/prod.yml`, eight modules of `guppi/` and fifteen test files. `ledger.py`, `onward.py`, `ratified.py` and `casecheck.py` find their own refusals in the transcript by the text of their hook's command; they take both forms, the old one for a session that still runs the hooks it read at its start, and a test asserts that each new form stands in `.claude/settings.json`, as `rule-one-judgment-one-implementation` asks of two sides that cannot share code. The ticker of render lines, `command_line` of `guppi/render.py`, matches `guppi render` anywhere in the first code span and takes both forms as it stands; `OFF_FORM_LINE` of `guppi/prespec.py` would miss a line of the new form, so it takes both. A Grep `project_root\(\)|REPO\b|ROOT = |Path\(__file__\)` over `tests/` printed `test_generate.py`, `test_case_schema.py`, `test_orchestration.py`, `test_schemas.py`, `test_lint.py` and `test_materialize.py`, which read `case-schema.md`, `case-example.md`, `orchestration.md`, the `schema.yaml` files and the `Makefile` by a path counted from the test file; under `.guppi/tests/` each counts one step more. `test_lint.py` lists the steps of `make lint` as the fake `uv` records them, so they take `--project .guppi`. `test_case_schema.py` runs the check over the example Case, whose new method still names `make test-cart`, so `estimate-case-example-passes-the-check` stands. Whether Claude Code runs a hook in the project's folder after a Bash command changed folder was not read; the relative path `.guppi` rests on it, and the reading of Case 819.1 tests it. That `uv sync` installs the group dev, and that uv fetches Python 3.12 itself, were not read at a source; the readings of Cases 819.1 and 819.4 test them. Between the Work Mode that moves the code and the librarian's run, `.claude/settings.json` and the pages still hold the old command, so the new test is red; that red is a note for the handoff by `rule-retro`, and the root development project keeps each hook working. `estimate-clean-branch-writes-a-clean-copy` lists `pyproject.toml` and `uv.lock` among the files `guppi ship` writes, which becomes false, so Case 819.3 replaces its Criterion. `estimate-generate-rewords` says every pair is a whole word, which becomes false, so Case 819.2 replaces its Criterion rather than adding a second Estimate beside a false one. Case 816 changes `rule-clean-branch` in other sentences, and its pairs and those of Case 818.1 apply before this Case's `reword`; the pairs of Case 819.3 are written on the text that the `reword` leaves. Case 818.1 creates `rule-plugin-install`; Case 819.4 writes its Purpose and Render whole, keeping each sentence of Case 818 that still holds. Case 818.1 must change: its `then` and `given` name `guppi/` and `pyproject.toml` among the files the install copies, and after this Case the clean version holds `.guppi/` and no `pyproject.toml` at its root; the `reword` turns `guppi/` in its Criterion into `.guppi/guppi/` and leaves `pyproject.toml`, which a Case may not change inside a Criterion. Its lines should name `.guppi/` in place of `guppi/` and `pyproject.toml`, and the person agreed that Case 818 is built again. Its rebuild should leave the `uv` check and the `uv sync` step to Case 819.4, which writes the Purpose and the Render of `rule-plugin-install` whole after the `create` of Case 818. The check of those two steps stands on `rule-guppi-package`, as `estimate-guppi-package-is-ready-after-the-install`, since the check of this file finds no live page `rule-plugin-install` to put it on. Case 817 changes no text this Case touches. `estimate-clean-branch-code-holds-pointers-only-in-brackets` stands, since this repository keeps a root `pyproject.toml`. `estimate-hook-registry-rendered` stands, since it promises only that the file equals the Render. Case 820 of this session drops `make`: `guppi check`, `guppi test` and `guppi style` run the checks, a thin `Makefile` stays in this repository for now, the clean version writes no `Makefile` and no `.guppi/guppi/ship.py`, and the judgment of a pointer moves into `.guppi/guppi/pointers.py`. So Case 819.3 lists no `Makefile` among the files `guppi ship` writes, and for the module of `ship` it points to `estimate-clean-branch-ships-no-ship-command` of Case 820.5, which makes that promise. This Case changes only the commands inside the `Makefile`. The `reword` of Case 820.7 replaces `make lint`, `make test` and `make style`, and the pairs of this Case replace `uv run guppi`, `uv run pytest`, `guppi/` and `tests/`. No `old` of one set stands inside an `old` or a `new` of the other, and the pairs of this Case come first in the ledger, so where both hit one sentence each changes its own words. The check of this file names such sentences in `estimate-backlog-checks-the-file`, `estimate-carry-over-writes`, `estimate-clean-branch-code-holds-pointers-only-in-brackets`, `estimate-documentation-completes`, `estimate-spec-box-runs-a-conserved-spec`, `estimate-where-to-stop-stops-only-on-its-conditions`, `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-guppi-tests-green`, `estimate-prespec-catches-a-method-without-a-form` and `decision-case-807`. Read side by side, each reads true with both changes: a target of make becomes a command of `guppi`, and a command or a path of the code takes `--project .guppi` or `.guppi/`. For example, the `When` of `estimate-guppi-tests-green` becomes `uv run --project .guppi guppi test` running `uv run --project .guppi pytest -q` over `.guppi/tests/`. In `estimate-prespec-catches-a-method-without-a-form`, Case 820.4 replaces the Criterion whole after both rewords. The Decision page `decision-case-807` is a record that `guppi generate` leaves alone. Case 820 changes other sentences of `rule-clean-branch`, `rule-estimates-schema`, `rule-lint` and `rule-guppi-config` than this Case does: on `rule-clean-branch` it adds a sentence after words this Case leaves alone; on `rule-estimates-schema` it changes the sentence on the form of a MOC, which this Case leaves alone; and it writes the Purpose of `rule-lint` and `rule-guppi-config` whole, in the new paths, after the `reword` of this Case.

> **problem:**
> GUPPI's code runs only where its `pyproject.toml` stands at the root of the project, so a user's project must take files at its root that it does not own, and a project with its own `pyproject.toml` cannot take GUPPI at all.

> **recommend:**
> - **Where the code that the hooks run lives**
>   - Recommended: (a) the project's own copy at its root, for this sprint.
>   - Answer: (d) a copy in its own folder `.guppi/`, called as `uv run --project .guppi guppi …`; this repository moves its own code there too.
> - **What the install does when `uv` is missing**
>   - Recommended: (a) the install checks for `uv` first.
>   - Answer: not answered; replaced by the question on what the install does about `uv` and the Python environment.
> - **What the install does about `uv` and the Python environment**
>   - Recommended: (a) check `uv`, then build the environment by `uv sync` after the copy.
>   - Answer: agreed, (a).
> - **What stays at the root of this repository**
>   - Recommended: (a) a development project stays at the root.
>   - Answer: (a) as a step in between, then (b), nothing at the root.
> - **Which texts change to the new command**
>   - Recommended: (a) the texts that run.
>   - Answer: (b) every text; the Estimates that go back to pending are read later by one Case of their own.
> - **Where GUPPI's own tests live**
>   - Recommended: (a) they stay at the root and do not ship.
>   - Answer: not answered; the person asked why not (b) and why one script cannot rewrite the paths; replaced by the question on where the tests live and whether they ship.
> - **Where GUPPI's own tests live, and whether they ship**
>   - Recommended: (b) move them into `.guppi/tests/` now, and leave how they ship to item C9.
>   - Answer: agreed, (b).
> - **Git and the Python environment of `.guppi/`**
>   - Recommended: (a) a `.gitignore` of its own inside `.guppi/`.
>   - Answer: agreed, (a).
> - **What checks that this is done**
>   - Recommended: (a) a new Estimate for each half, plus the sprint Estimate.
>   - Answer: agreed, (a).
> - **When the root development project goes**
>   - Recommended: (a) a Case of a later session removes it.
>   - Answer: agreed, (a).
> - **How the pages take the new command**
>   - Recommended: (a) one `reword` of the command.
>   - Answer: agreed, (a).
> - **Which page holds where GUPPI's code lives**
>   - Recommended: (a) a new rule, `rule-guppi-package`.
>   - Answer: agreed, (a).
> - **How the paths of the code and the tests change in the pages**
>   - Recommended: (a) `reword` learns path prefixes.
>   - Answer: agreed, (a).
> - **Which page carries the check of the `uv` step of the install**
>   - Recommended: (a) the check stands on `rule-guppi-package`.
>   - Answer: agreed, (a); Case 818 is built again too.
> - **Change**
>   - Asked: the person agreed to build this Case again after Case 820, which drops `make` and ships no command `ship`.
>   - Taken: Case 819.3 no longer lists the `Makefile` among the files that `guppi ship` writes, in its new text of `rule-clean-branch`, its `then` and its task on `ROOT_FILES`; its `then` points to `estimate-clean-branch-ships-no-ship-command` for the module of `ship`; the Purpose of `rule-guppi-package` names the `Makefile` as the one this repository keeps for now.
> - **Change**
>   - Asked: the person agreed to build this Case again after Case 821, which ships the tests, the passed Estimates, the session files and `.github/workflows/checks.yml`, and builds no `prod` while a page with `core: true` is `draft`.
>   - Taken: the Criterion of Case 819.3 drops its lines on the tests, `.github/` and the session files and points to the Estimates of Cases 821.1, 821.2, 821.3 and 821.5; its line on brackets leaves out the strings of a test file; its task on `guppi/ship.py` leaves the tests to Case 821.2; the method of `estimate-guppi-package-is-ready-after-the-install` waits for the first run that writes `prod`; the test of Case 819.1 builds with `--allow-draft`.
> - **Change**
>   - Asked: at `/pre-spec`, the person chose that each Estimate that waits for a run that writes `prod` is read from a local copy that `guppi ship --allow-draft` writes after the librarian's run of this change; and the findings of `ask-guppi` on this Case are fixed.
>   - Taken: the method of `estimate-guppi-package-is-ready-after-the-install` reads such a local copy. `rule-guppi-package` takes `core: true` by a `set` of its `update`, so the field lands as a boolean that `is_core` of `guppi/pages.py` accepts. Its texts, and the Criterion of Case 819.1, name the repository of GUPPI in place of this repository. Two more pairs on `rule-estimates-schema` keep its example command and its sentence on a test path off the `reword`. The task on `TEST_PATH` reads a test path whole from its start. The Criterion of Case 819.3 says that what it writes of the tests, the environment and the module of `ship` is what Cases 820 and 821 set. A pair of Case 819.2 makes the Purpose of `rule-page-generation` name rules, entities and Estimates as what a `reword` changes.

### Case 819.1 — The code stands in .guppi/ and every caller runs it there

> **given:**
> `rule-guppi-package`: the new rule of where the code of GUPPI stands and how it is called.
> **＋** `estimate-guppi-package-runs-from-its-own-folder`: the new check of that rule.
> **＋** `guppi/`, `tests/`, `pyproject.toml`, `uv.lock`, `.guppi/`, `.guppi/pyproject.toml`, `.guppi/uv.lock`, `.guppi/.gitignore`, `.guppi/tests/`, `.guppi/tests/test_guppi_package.py` and `.venv/`: the code, its tests, its settings and its Python environment, before and after the move.
> **＋** `rule-hook-registry`, `.claude/settings.json`, the skills and agents under `.claude/`, `Makefile` and `.github/workflows/prod.yml`: the callers of the code.
> **＋** `guppi/ledger.py`, `guppi/onward.py`, `guppi/ratified.py`, `guppi/casecheck.py`, `guppi/prespec.py`, `guppi/lint.py`, `guppi/bashguard.py` and `guppi/generate.py`: the modules that judge the command or a path, or carry the `reword`.
> **＋** `rule-case-example`, `rule-estimates-schema` and `rule-rules-schema`: the examples of a project of the person's own, kept out of the `reword`.
> **＋** `rule-clean-branch` and `guppi/ship.py`: the rule and the code of the clean version.

> **when:**
> In the repository of GUPPI, after the move of the code and the render of the harness, a session of Claude Code opens and its hooks, skills and agents run the code of GUPPI, and `uv run --project .guppi pytest` runs the tests of `.guppi/tests/`.
> **＋** `uv run --project .guppi guppi ship <folder>` builds the clean version, as `rule-clean-branch` sets it.

> **then:**
> The package `guppi`, its `pyproject.toml`, its lock file `uv.lock`, its tests and a `.gitignore` that holds `.venv/` stand under `.guppi/`, and `.guppi/pyproject.toml` declares pytest and ruff for the tests.
> **＋** Each hook of `.claude/settings.json`, and each command of a skill, an agent, the `Makefile` and `.github/workflows/prod.yml` that runs the code of GUPPI or its tests, runs it through `uv run --project .guppi`, and no hook prints an error.
> **＋** No live rule, entity or Estimate names a command that runs the code of GUPPI or its tests through `uv run` without `--project .guppi` outside History and Result, and none names a path of that code or those tests outside `.guppi/`.
> **＋** `.guppi/tests/test_guppi_package.py` fails on such a command in a file of `.claude/`, the `Makefile`, `.github/workflows/` or a live rule, entity or Estimate, and on such a path in such a page, found by the matching of `reword` of `guppi generate`.
> **＋** Each module that finds its own refusals in the transcript by the command of its hook finds them under the command with `--project .guppi` and under the command without it.
> **＋** The Bash and PowerShell guards judge `uv run --project .guppi python` as they judge `uv run python`, and `guppi lint` takes a test path under `.guppi/tests/` in a `method` as it takes one in the folder of tests of the project's own code.
> **＋** The clean version holds no `pyproject.toml` and no `uv.lock` at its root.
> **－** The repository of GUPPI keeps at its root, until a Case of a later session removes them, the `pyproject.toml` and `uv.lock` of a development project that takes the package from `.guppi/`, so a command without `--project .guppi` still runs at its root and no hook of a running session fails.
> **－** The Decision pages, the lessons and the Insights keep the old command and the old paths, since they are records.
> **－** The examples of a project of the person's own in `rule-case-example`, `rule-estimates-schema` and `rule-rules-schema` keep a path of tests of that project, with no `.guppi/`.

```then
create:
- slug: rule-guppi-package
  type: rule
  ref: rule-harness
  kind: Leaf
  purpose: Prevents a project with GUPPI from depending on files at its root that it does not own, or on a command that runs only in the repository of GUPPI
  enforcement: check
  implementation_ref:
  - .guppi/pyproject.toml
  - .guppi/tests/test_guppi_package.py
  tags:
  - harness
  - plugin
  sections:
    Purpose: Prevents a project with GUPPI from depending on files at its root that it does not own, or on a command that runs only in the repository of GUPPI. The code of GUPPI, the package `guppi`, stands in `.guppi/guppi/`, with its `.guppi/pyproject.toml`, its lock file `.guppi/uv.lock`, its tests in `.guppi/tests/` and a `.guppi/.gitignore` that keeps its Python environment `.guppi/.venv/` out of git. Each caller runs the code as `uv run --project .guppi guppi …` — the hooks of `.claude/settings.json`, the skills, the agents and the `Makefile` that the repository of GUPPI keeps for now — and the tests as `uv run --project .guppi pytest`. `.guppi/pyproject.toml` declares the version of Python, the one runtime dependency PyYAML, and pytest and ruff for the tests. The code finds the project by the folder that Claude Code was opened in, so it reads the vault of the project from there. The test `.guppi/tests/test_guppi_package.py` fails on a command that runs the code or the tests through `uv run` without `--project .guppi`, in a file of `.claude/`, the `Makefile`, `.github/workflows/` or a live rule, entity or Estimate, and on a path of the code or the tests outside `.guppi/` in such a page, found by the matching of `reword` of `guppi generate`. The repository of GUPPI keeps at its root, for now, the `pyproject.toml` and `uv.lock` of a development project that takes the package from `.guppi/`, so that a session whose hooks still name the command without `--project .guppi` keeps working; `guppi ship` does not write them, and a later Case removes them (as set in case 819).
- slug: estimate-guppi-package-runs-from-its-own-folder
  ref: rule-guppi-package
  kind: QA
  purpose: Whether the code, the settings, the lock and the tests of GUPPI stand under .guppi/, every hook, skill, agent, Makefile line and page runs them through uv run --project .guppi, the modules and the guards take that form, and the clean version holds no pyproject.toml at its root
  method: 'uv run --project .guppi pytest .guppi/tests/test_guppi_package.py; by hand, after the librarian''s run of the session whose Work Mode moves the code: a session opened in this repository, /hi typed there, and the output of its hooks read against the Criterion'
  tags:
  - harness
  - plugin
update:
- slug: rule-case-example
  replace:
  - old: 'method: `make test-cart, which runs uv run pytest tests/test_cart_view.py -k render_time`'
    new: 'method: `make test-cart, which runs pytest cart/tests/test_view.py -k render_time`'
  - old: 'method: make test-cart, which runs uv run pytest tests/test_cart_view.py -k render_time'
    new: 'method: make test-cart, which runs pytest cart/tests/test_view.py -k render_time'
  change: the example Estimate names a test path of the example project that the reword of rule-guppi-package does not touch
- slug: rule-estimates-schema
  replace:
  - old: a path under `tests/`; or the words `by hand`
    new: a path under `.guppi/tests/` or under the folder of tests of the project's own code; or the words `by hand`
  - old: 'method: pytest tests/discounts/test_new_client.py'
    new: 'method: pytest discounts/tests/test_new_client.py'
  - old: '`pytest tests/discounts/test_new_client.py`: 3 passed.'
    new: '`pytest discounts/tests/test_new_client.py`: 3 passed.'
  - old: '`make test-x`, `pytest tests/test_x.py`'
    new: '`make test-x`, `pytest app/tests/test_x.py`'
  - old: 'Naming a form is not enough by itself: a path under `tests/` must exist'
    new: 'Naming a form is not enough by itself: a test path must exist'
  change: a method names a test path under .guppi/tests/ or in the tests of the project's own code; the example names a path that the reword of rule-guppi-package does not touch
- slug: rule-rules-schema
  replace:
  - old: 'implementation_ref: [ruff.toml, tests/lint/test_pricing_sync.py]'
    new: 'implementation_ref: [ruff.toml, lint/tests/test_pricing_sync.py]'
  change: the example names a test path that the reword of rule-guppi-package does not touch
- slug: rule-guppi-package
  reword:
  - old: uv run guppi
    new: uv run --project .guppi guppi
  - old: uv run pytest
    new: uv run --project .guppi pytest
  - old: guppi/
    new: .guppi/guppi/
  - old: tests/
    new: .guppi/tests/
  set:
    core: true
  change: every live rule, entity and Estimate names the command, the code and the tests of GUPPI under .guppi/, and the page ships
```

```tasks
- [x] create `rule-guppi-package`
- [x] create `estimate-guppi-package-runs-from-its-own-folder`
- [x] update `rule-case-example`
- [x] update `rule-estimates-schema`
- [x] update `rule-rules-schema`
- [x] update `rule-guppi-package`
- [x] Move, in an order where a command without `--project .guppi` still answers at the root after each step: `guppi/` to `.guppi/guppi/`, `tests/` to `.guppi/tests/`, the package's `pyproject.toml` and `uv.lock` to `.guppi/`, with pytest and ruff and their settings in `.guppi/pyproject.toml`; a new `.guppi/.gitignore` that holds `.venv/`; the root `pyproject.toml` and `uv.lock` rewritten as a development project that takes `guppi` from `.guppi/` as an editable path and holds pytest and ruff with the settings of the tests.
- [x] `.guppi/tests/test_guppi_package.py`: the layout of `.guppi/`; no `uv run guppi` and no `uv run pytest` by `reword_pattern` of `guppi/generate.py` in the files of `.claude/`, the `Makefile` and `.github/workflows/`, and none of those and no path that the pairs `guppi/` and `tests/` would change in the parts of a live rule, entity or Estimate that `reword_text` changes; each `COMMAND` of `ledger.py`, `onward.py`, `ratified.py` and `casecheck.py`, in the new form, stands in `.claude/settings.json`; a clean version built into a temporary folder, with `--allow-draft` where it builds from this repository, holds no `pyproject.toml` and no `uv.lock` at its root.
- [x] `.guppi/tests/`: each path counted from the test file in `test_generate.py`, `test_case_schema.py`, `test_orchestration.py`, `test_schemas.py`, `test_lint.py` and `test_materialize.py` takes one step more; `LINT_STEPS` of `test_lint.py` take `--project .guppi`; each test that names the command or a path of the code or the tests names it as the code does.
- [x] `guppi/ledger.py`, `guppi/onward.py`, `guppi/ratified.py` and `guppi/casecheck.py`: each `COMMAND` holds the command with `--project .guppi`, and the search for the module's own refusals takes the command without it too, until a Case of a later session removes the old form.
- [x] `guppi/prespec.py`: `OFF_FORM_LINE` takes a render or sprint line of the form with `--project .guppi` as it takes one without it.
- [x] `guppi/lint.py`: `TEST_PATH` reads a test path whole from its start, where no letter, digit, `_`, `-`, `.` or `/` stands before it, so `.guppi/tests/test_x.py`, `tests/test_x.py` and `discounts/tests/test_x.py` are each one path and none is read from the middle of another; lint checks each such path for existence from the root of the project.
- [x] `guppi/bashguard.py`: `interpreter` skips the value of `--project` after `uv run`, so `uv run --project .guppi python` fed a script on stdin is judged as `uv run python` is; a test in `test_bashguard.py` and one in `test_powershellguard.py`.
- [x] `guppi/`: each docstring, comment and message that names the command, the code or the tests of GUPPI names them as the pages name them after the `reword`.
- [x] `Makefile`: each `uv run` line takes `--project .guppi`.
- [x] `.github/workflows/prod.yml`: the build runs `uv run --project .guppi guppi ship "$RUNNER_TEMP/clean"`.
- [x] `uv run guppi render`: `.claude/settings.json`
- [x] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [x] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [x] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [x] `uv run guppi render`: `.claude/skills/box/SKILL.md`
- [x] `uv run guppi render`: `.claude/skills/sprint-close/SKILL.md`
- [x] `uv run guppi render`: `.claude/skills/merge-main/SKILL.md`
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [x] `uv run guppi render`: `.claude/skills/work/SKILL.md`
- [x] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
- [x] `uv run guppi render`: `.claude/skills/carry/SKILL.md`
- [x] `uv run guppi render`: `vault/wiki/where-to-stop.md`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] `uv run guppi render`: `vault/wiki/case-example.md`
- [x] `uv run guppi render`: `vault/wiki/ratification.md`
- [x] `uv run guppi render`: `vault/wiki/orchestration.md`
- [x] `uv run guppi render`: `vault/wiki/rules/schema.yaml`
- [x] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`
- [ ] read `estimate-guppi-package-runs-from-its-own-folder`
```

### Case 819.2 — A reword pair that ends with / changes the start of a path

> **given:**
> `rule-page-generation`: the rule of `guppi generate` and its `reword`.
> **＋** `estimate-generate-rewords`: its Criterion is replaced whole.
> **＋** `guppi/generate.py`: `reword_pattern`, `reword_text` and `reword_pairs`.
> **＋** `guppi/prespec.py`: the preview of the pairs, which imports `reword_pattern` and `reword_text`.
> **＋** `tests/test_generate.py`: the tests of `guppi generate`.
> **＋** `tests/`, `tests/test_ship.py`, `.guppi/tests/`, `.guppi/tests/test_ship.py` and `cart/tests/`: the paths of the example of a pair that ends with `/`.
> **＋** `vault/wiki/`, `vault/archive/` and `vault/raw/`: the live pages a `reword` changes, and the folders it leaves alone.

> **when:**
> `guppi generate` applies an `update` entry whose item carries `reword`, a list of `{old, new}` pairs.

> **then:**
> A pair whose `old` does not end with `/` is replaced as a whole word, with no letter, digit, `_` or `-` right before or after it.
> **＋** A pair whose `old` ends with `/`, such as `tests/`, is replaced as the start of a path: where no letter, digit, `_`, `-`, `.` or `/` stands right before it, whatever follows it, so the pair `tests/` → `.guppi/tests/` turns `tests/test_ship.py` into `.guppi/tests/test_ship.py` and leaves `.guppi/tests/` and `cart/tests/` as they are.
> **＋** The replace runs on every live page of the folders `rules`, `entities` and `estimates` of `vault/wiki/`, in every section but History and Result and in the fields `purpose` and `method`, and a pair whose `old` ends with `/` runs in the fields `implementation_ref`, `governs` and `code_ref` too.
> **＋** Each page touched gets one History line `reworded: old → new · [[decision-case-N]]`, and stdout has one line per page with the count.
> **＋** The other keys of the item — `set`, `replace`, `sections`, `change` — apply to the page itself as before; an item that carries `reword` alone is content and applies.
> **＋** `uv run --project .guppi guppi prespec --check` previews each pair by the same matching as `guppi generate`.
> **－** A pair with no hit on any live page fails the entry with the reason, and so does a pair whose `new` is absent from the text of the page of the item: its `purpose`, `governs`, `implementation_ref`, Purpose and Render, compared without regard to case. Nothing is applied.
> **－** The Decision pages, the lessons and the Insights, `vault/archive/`, `vault/raw/`, `log.md`, `brief.md` and `sprint.md` are not touched; the status of no Estimate changes.

```then
update:
- slug: rule-page-generation
  replace:
  - old: and in `purpose` and `method`, of every live page of `wiki/`, one History line per page touched
    new: and in `purpose` and `method`, of every live rule, entity and Estimate of `wiki/`, one History line per page touched
  - old: a slug goes through `rename`, not `reword` (case 274.1).
    new: 'a slug goes through `rename`, not `reword` (case 274.1). A pair whose `old` ends with `/`, such as `tests/`, is the start of a path: it matches wherever no letter, digit, `_`, `-`, `.` or `/` stands right before it, whatever follows it, and it is replaced in the link fields `implementation_ref`, `governs` and `code_ref` too (as set in case 819).'
  change: a reword pair whose old ends with / matches the start of a path and changes the link fields too
- slug: estimate-generate-rewords
  set:
    status: pending
    purpose: An update item with reword replaces its pairs as whole words, or a pair whose old ends with / as the start of a path in the link fields too, on every live page but History and Result, one History line each, and fails on a pair with no hit or a new the owner does not carry
    method: 'uv run --project .guppi pytest .guppi/tests/test_generate.py on a temp vault whose pages hold paths in their text and their link fields; by hand, after the librarian''s run that applies the reword of rule-guppi-package: the pages it touched and its stdout read against the Criterion'
  change: the Criterion replaced whole — a pair whose old ends with / matches the start of a path, in the link fields too
```

```tasks
- [x] update `rule-page-generation`
- [x] update `estimate-generate-rewords`
- [x] `guppi/generate.py`: `reword_pattern` matches an `old` that ends with `/` as the start of a path, and stays the one matching of `reword`, `rename` and the preview of `/pre-spec`; `reword_text` changes `implementation_ref`, `governs` and `code_ref` for such a pair; the docstring says so.
- [x] `tests/test_generate.py`: a pair `tests/` on a temp vault turns `tests/test_x.py` into `.guppi/tests/test_x.py` in a section, in `method` and in `implementation_ref`, and leaves `.guppi/tests/` and `cart/tests/` alone; a pair that does not end with `/` still matches a whole word only.
- [ ] read `estimate-generate-rewords`
```

### Case 819.3 — guppi ship writes the code under .guppi/

> **given:**
> `rule-clean-branch`: the rule of `guppi ship`.
> **＋** `estimate-clean-branch-writes-a-clean-copy`: its Criterion is replaced whole.
> **＋** `vault/raw/2026-10-14/1907/cases/case-816.md` and `vault/raw/2026-10-14/1907/cases/case-818.md`: the Cases of this session that change other sentences of `rule-clean-branch`.
> **＋** `guppi/ship.py`: `ROOT_FILES`, `TREES`, `SKIPPED_NAMES` and `NOT_CLEANED`.
> **＋** `tests/test_ship.py`: the tests of `guppi ship`.
> **＋** `.guppi/`, `.guppi/tests/`, `.guppi/.venv/`, `.guppi/uv.lock`, `.claude/` and `.github/`: folders and files that the clean version holds or leaves out.
> **＋** `vault/wiki/`, `vault/wiki/tags.md`, `vault/wiki/case-example.md`, `vault/archive/` and `vault/raw/`: the pages and files of the vault that the clean version holds or leaves out.
> **＋** `rule-case-example` and `decision-case-N`: the page whose Render holds the example Case, and the form of the id of a Decision page.
> **＋** `estimate-clean-branch-ships-no-ship-command` and `vault/raw/2026-10-14/1907/cases/case-820.md`: the check that the clean version holds no module of the command `ship`, and the Case of this session that creates it and leaves the `Makefile` out of the clean version.
> **＋** `estimate-clean-branch-ships-the-tests`, `estimate-clean-branch-ships-the-passed-estimates`, `estimate-clean-branch-ships-the-checks-workflow`, `estimate-clean-branch-writes-the-session-files` and `vault/raw/2026-10-15/0553/cases/case-822.md`: the checks of what else the clean version holds, and the Case of this session that creates them.

> **when:**
> `uv run --project .guppi guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.
> **＋** Or `uv run --project .guppi guppi ship --review <folder>` does the same.
> **＋** Or `uv run --project .guppi guppi ship --check` judges the working tree and writes no folder.

> **then:**
> It writes `.guppi/` — what it writes of its tests, its Python environment and the module of the command `ship` is what `estimate-clean-branch-ships-the-tests` and `estimate-clean-branch-ships-no-ship-command` set — then `.claude/`, `CLAUDE.md`, `.gitattributes`, the `schema.yaml` of each category, `vault/wiki/tags.md`, each page under `vault/wiki/` with `core: true`, and each file rendered from such a page.
> **＋** In each file it writes, it removes whole each bracket that holds a pointer — a reference to a case, an id `decision-case-N` or a mention of a session by its id — with every word in it and the space before it, and each `[[decision-case-N]]` link, but in a string of a test file, as `estimate-clean-branch-ships-the-tests` sets it; a bracket that holds no pointer stays as it is.
> **＋** It writes each other `[[…]]` link of a Markdown file to a page or a file it does not write as the slug in a code span.
> **＋** Each page it writes carries `origin: guppi`, `sprint: guppi`, the date of the run in `created` and a `## History` of one line that says the page shipped with GUPPI, and its link fields keep only the pages it writes.
> **＋** It exits 1, and prints the file and the line, for each pointer that stands outside such a bracket, each id of a list of sessions included.
> **＋** In a comment or a docstring of a Python file it writes, it exits 1, and prints the file and the line, for each bracket that holds only case numbers, joined by a comma, a semicolon, `and` or a dash, such as `(274.1)` or `(513, 544.7)`.
> **＋** It does the same for each comment or docstring that opens with one or more case numbers joined the same way, followed by a colon, such as `# 169.1:`, `"""75.2:` or `# 387.4, 445.4:`, and for each comment whose whole text is one or more case numbers joined the same way, such as `# 786` or `# 387.4, 445.4`.
> **＋** It exits 1 when a file it writes holds a section between the markers of a page without `core: true`.
> **＋** With `--review` it also prints the file, the line and the bracket for each bracket it removes that holds words beside its pointers, and those lines set no exit code.
> **＋** With `--check` it judges each file it would write outside `vault/` — the code under `.guppi/`, `.claude/` and the files at the root of the project — but `.guppi/uv.lock`, which it does not clean, as it would write it, prints the same lines for it, exits 1 on any, and writes nothing.
> **－** It writes no page without `core: true` but the Estimates that `estimate-clean-branch-ships-the-passed-estimates` sets, nothing of `vault/raw/` or `vault/archive/`, and no `guppi.toml`; what it writes of `.github/` and in place of the session files is what `estimate-clean-branch-ships-the-checks-workflow` and `estimate-clean-branch-writes-the-session-files` set.
> **－** It writes no cache folder of Python, pytest or ruff, and `--check` does not judge one.
> **－** It writes no file that a page without `core: true` renders in full.
> **－** A case id inside a code span of a Markdown file, or after `[case ` or `#case-`, is the form of a line, not a reference.
> **－** A case id inside a fenced block of a Markdown file, inside a code span of the text of a `schema.yaml`, or after `:case `, is the form of a sample or of a line: it is neither removed nor printed; in `vault/wiki/case-example.md` and the Render of `rule-case-example` only the fenced blocks, the example Case among them, are set aside so, and the text around them is judged and cleaned like the text of any other page.
> **－** It removes no bare case number: the copy holds it as written.
> **－** It judges no code of a Python file outside its comments and docstrings for a bare case number, such as `match.group(1)`, and a number or a list of numbers that opens a comment with words and no colon after it, such as `# 3, 4 tries`, is no finding.

```then
update:
- slug: rule-clean-branch
  replace:
  - old: 'into an empty folder: `.guppi/guppi/`, `.claude/`, `CLAUDE.md`, `Makefile`, `pyproject.toml`, `uv.lock`, `.gitattributes`,'
    new: 'into an empty folder: `.guppi/`, which holds the package `guppi` with its `pyproject.toml`, `uv.lock` and `.gitignore`, but not its tests `.guppi/tests/` or its Python environment `.guppi/.venv/`; `.claude/`, `CLAUDE.md`, `.gitattributes`,'
  - old: but `sprint.md`, `backlog.md` and `guppi.toml`, which belong to this project.
    new: but `sprint.md`, `backlog.md` and `guppi.toml`, which belong to this project, and the `pyproject.toml` and `uv.lock` at the root of this repository, which [[rule-guppi-package]] keeps for the development of GUPPI.
  change: guppi ship writes the code under .guppi/ without its tests and its environment, and no pyproject.toml or uv.lock at the root
- slug: estimate-clean-branch-writes-a-clean-copy
  set:
    status: pending
    purpose: 'Whether guppi ship writes the code under .guppi/ without its cache folders, the harness and the pages with core: true, removes whole each bracket that holds a pointer, writes a link to a page it leaves out as its slug, writes the shipped values, exits 1 on a pointer outside such a bracket and on a bare case number in a comment or a docstring of a Python file, lists the brackets with words under --review, and judges in place under --check each file outside vault/ that it writes'
    method: uv run --project .guppi pytest .guppi/tests/test_ship.py
  change: the Criterion replaced whole — the code ships under .guppi/, and the root pyproject.toml and uv.lock do not ship
```

```tasks
- [x] update `rule-clean-branch`
- [x] update `estimate-clean-branch-writes-a-clean-copy`
- [x] `guppi/ship.py`: `ROOT_FILES` holds `CLAUDE.md` and `.gitattributes`; the tree `.guppi` replaces `guppi` in `TREES`; `.guppi/.venv/` and the cache folders of Python, pytest and ruff are skipped by the copy and by `--check`, and the tests under `.guppi/tests/` go as Case 822.2 sets; `.guppi/uv.lock` is not cleaned; the docstring says so.
- [x] `tests/test_ship.py`: the sample tree holds `.guppi/guppi/`, `.guppi/pyproject.toml`, `.guppi/uv.lock`, `.guppi/.gitignore`, a file under `.guppi/.venv/`, a cache folder of pytest under `.guppi/`, and a root `pyproject.toml`; the file set of `test_it_writes_the_code_the_harness_and_the_core_pages_only` takes the first four and no file of `.guppi/.venv/`, of the cache folder or the root `pyproject.toml`; the tests under `.guppi/tests/` are judged as Case 822.2 sets.
- [x] read `estimate-clean-branch-writes-a-clean-copy`
```

### Case 819.4 — /guppi:install checks uv and builds the environment

> **given:**
> `rule-plugin-install`: the rule of the skill `/guppi:install`.
> **＋** `estimate-guppi-package-is-ready-after-the-install`: the new check of the two steps.
> **＋** `plugin/skills/install/SKILL.md`: the skill as the Render writes it.
> **＋** `vault/raw/2026-10-14/1907/cases/case-818.md`: the Case of this session that creates `rule-plugin-install`.
> **＋** `rule-guppi-package` and `.guppi/.venv/`: the rule of the folder of the code, and the Python environment that `uv sync` builds there.
> **＋** `/hi`: the skill that opens a working session in the project.

> **when:**
> The person installs the plugin `guppi` from the catalogue of the branch `prod` and types `/guppi:install` in an empty project open in Claude Code, as `rule-plugin-install` sets it.

> **then:**
> Before it writes anything, `/guppi:install` runs `uv --version`.
> **＋** After it copies the files, it runs `uv sync --project .guppi` in the project, which builds the Python environment `.guppi/.venv/` before it tells the person to reopen Claude Code and type `/hi`.
> **＋** The hooks of the project find that environment built at the first `/hi`.
> **－** When `uv --version` fails, it says that GUPPI needs the tool `uv`, and that the person installs it and types `/guppi:install` again, writes nothing and stops.
> **－** When `uv sync --project .guppi` fails, it shows its output and stops, and does not tell the person to type `/hi`.

```then
create:
- slug: estimate-guppi-package-is-ready-after-the-install
  ref: rule-guppi-package
  kind: QA
  purpose: Whether /guppi:install stops and writes nothing when uv is missing, and builds the Python environment .guppi/.venv/ by uv sync after the copy, before it sends the person to /hi
  method: 'by hand, after the librarian''s run of the session whose Work Mode builds this change: a local copy that uv run --project .guppi guppi ship --allow-draft writes into an empty folder, the plugin guppi installed from it; in an empty project on a machine whose search path holds no uv, /guppi:install typed and its output and the files of the project read; in an empty project on a machine with uv, /guppi:install typed, .guppi/.venv/ read and Claude Code reopened there, read against the Criterion'
  tags:
  - plugin
  - harness
update:
- slug: rule-plugin-install
  sections:
    Purpose: 'Prevents a project that installs the plugin `guppi` from getting a part of GUPPI, or from losing a file of its own to it. The plugin, which the catalogue `guppi-marketplace` on the branch `prod` lists, is an installer. It carries one skill of its own, `install`, which the person types as `/guppi:install` in the project to install into. `guppi ship` copies the skill from `plugin/skills/install/SKILL.md`, which the Render of this page writes, to `skills/install/SKILL.md` of the clean version ([[rule-clean-branch]]). The skill first runs `uv --version`; when the tool `uv` is missing, it says that GUPPI needs it and writes nothing. It copies into the project each file of the plugin but its own files, those under `.claude-plugin/`, `skills/` and `.git/`. Those files are the code of GUPPI in `.guppi/`, the harness `.claude/` and `CLAUDE.md`, the files at the root and the pages with `core: true`, as `guppi ship` built them. It writes nothing when one of those files already stands in the project, and it runs no `guppi` and no `git` command. After the copy it runs `uv sync --project .guppi`, which builds the Python environment `.guppi/.venv/`, so that the first hook of the project does not wait for it ([[rule-guppi-package]], case 819). The project then runs on its own copy: its first `/hi` renders the harness from its own rule pages, and [[rule-morph]] sets its settings there. The skills of the project keep their bare names, such as `/hi`; only the skill of the plugin carries the prefix of the plugin (case 818). This page has no `core: true`, so a project that installs GUPPI does not hold it. Which files a new project gets waits for a Case of its own.'
    Render: |-
      <!-- rule-plugin-install -->
      ---
      name: install
      description: "Install GUPPI into the project open in this session: check uv, copy its files from this plugin and build its Python environment, then the person reopens Claude Code and types /hi. Run it when the person types /guppi:install."
      disable-model-invocation: true
      ---

      Install GUPPI into the project of this session, the folder that Claude Code was opened in. The files come from this plugin, at `${CLAUDE_PLUGIN_ROOT}`. Write nothing into that folder of the plugin.

      1. Run `uv --version`. When it fails, say that GUPPI needs the tool `uv`, which installs Python and runs the code of GUPPI, and that the person installs `uv` and types `/guppi:install` again, and stop. Write nothing.
      2. List each file under `${CLAUDE_PLUGIN_ROOT}`, but the files under `.claude-plugin/`, `skills/` and `.git/`. These are the files to install, each at the same path in the project.
      3. Check which of those paths already stand in the project. When one or more stand, list them, say that the install writes nothing into a project that already holds one of its files, and stop. Write nothing.
      4. Otherwise copy each file to its path in the project, with the folders it needs. Change no other file. Run no `guppi` command and no `git` command.
      5. Check that each file now stands in the project. When one is missing, name it and stop.
      6. Run `uv sync --project .guppi` in the project, which builds the Python environment of GUPPI in `.guppi/.venv/`. When it fails, show its output and stop.
      7. Say that GUPPI is installed, and that the person reopens Claude Code in this project and types `/hi`.
      <!-- /rule-plugin-install -->
  change: /guppi:install checks uv before it writes and builds the Python environment by uv sync after the copy
```

```tasks
- [x] update `rule-plugin-install`
- [x] create `estimate-guppi-package-is-ready-after-the-install`
- [x] `uv run guppi render`: `plugin/skills/install/SKILL.md`
- [ ] read `estimate-guppi-package-is-ready-after-the-install`
```

## Case 820 — GUPPI runs its checks without make

> **context:**
> GUPPI runs its checks through `make`, a system program that reads the `Makefile`: `make test` runs GUPPI's own tests, `make style` runs the style checker ruff, and `make lint` runs six vault checks in a row. `make` is no Python package, so it cannot come in GUPPI's Python environment; Windows has none by default, and the `Makefile` also looks for the shell of Git for Windows. So a person who installs GUPPI cannot run the checks that Work Mode, Retro and the librarian run. The person chose to drop `make` everywhere. `guppi check` runs the vault checks (Case 820.1). `guppi test` and `guppi style` run the commands that two new keys of `guppi.toml` set, each a list of commands run with no shell, here `uv run --project .guppi pytest -q` and the two ruff commands; in a user's project the install Case of `rule-morph` will ask for them in a later session, and until then, as the person chose, a new project takes the commands of the Render of `rule-guppi-config`, which ships, so its `guppi test` runs the tests of GUPPI; where `guppi.toml` or the key is missing, the command says so and exits 1 (Case 820.2). Whether the module `guppi.ship` stands is one function, `ship_stands` of `guppi/pages.py`, which `guppi check`, the list of commands and the check of a draft page that Case 821.7 adds to `guppi lint` import. The new texts of the shipped pages `rule-guppi-config` and `rule-harness` name the repository of GUPPI by that name, so they hold in any project, as Case 821.6 asks. Cases 818.1 and 819.1 create `rule-plugin-install` and `rule-guppi-package` under `rule-harness`, whose Purpose counts and lists the rules that run in no pipeline, and `estimate-harness-pipeline` promises that list; Case 820.9 adds both rules to the list and replaces that Criterion, with the new command of the vault checks. `parse` of `guppi/config.py` checks only the two language keys, so the new keys do not stop the render. The person also chose that a project that installs GUPPI gets no command `ship`, which only builds the clean version of this repository. `guppi/prespec.py` imports its judgment of a pointer, `outside`, from `guppi/ship.py`, so that judgment and the functions it calls move into a module of their own, `guppi/pointers.py`, which both sides import, and `guppi check` skips `guppi ship --check` where the module is missing (Cases 820.5 and 820.6). A Grep `ship` over `guppi/`, `ship.py` left out, printed `guppi/cli.py`, `guppi/prespec.py` and `guppi/pages.py`; the hit in `pages.py` is a docstring, so no other module needs `ship.py`. A Grep `guppi\.ship|ship\.` over `tests/` printed `tests/test_ship.py` and `tests/test_prespec.py`; the second asserts that `prespec.outside` is `ship.outside`, and Case 820.6 makes it assert the same of `pointers.outside`. Each group rule page, a MOC, has an Estimate whose method names a make target of its pipeline, such as `make test-harness`. The person chose the form of a pytest command with the test files of the pipeline. Today `names_a_moc_form` of `guppi/lint.py` refuses that form on a MOC, and `prespec.judge`, which the check of this file runs, calls it; so this Case teaches `guppi lint` and `/pre-spec` the new form beside the make target (Cases 820.3 and 820.4), and a Case of a later session moves the group Estimates and the example of `rule-case-example` to it and removes the make form, the group targets and the `Makefile`. The person chose that the three new commands are forms of a method too: after the replace below, the method of `estimate-guppi-tests-green` names `guppi test` and no other form. A Grep `names_a_moc_form|names_a_form` over `guppi/` printed `guppi/lint.py` and `guppi/prespec.py`: the forms stay one predicate each in `lint.py`, which `prespec.py` imports, so the change adds no second copy, as `rule-one-judgment-one-implementation` asks. No code but the `Makefile` runs the steps of the vault checks, and `guppi/config.py` stays the one reader of `guppi.toml`. The `Makefile` stays for now, since the rendered `/work` and `/retro` load the old commands until the librarian's render, which runs after Retro. Its target `lint` calls `guppi check`, which is code and runs as soon as Work Mode writes it; its targets `test` and `style` keep their own commands, since `guppi test` reads a key that `guppi.toml` gets only at that render (Case 820.7). The person will conserve this Spec with `/carry`, so its Work Mode, Retro and render run in a later session. At the last close the brief reports `make test`: 1620 passed, 6 skipped, and `make lint`: 0 lines, exit 0. Every live rule, entity and Estimate takes the new commands by one `reword` per command, which sets no Estimate `pending`, as the `reword` of Case 819 does. `reword_pairs` of `guppi/generate.py` needs the `new` of a pair in the text of its owner and runs before the other keys of its own item, and `/pre-spec` refuses two items of one target in one Case or sub-case; so the `reword` stands in Case 820.7, on `rule-lint` and `rule-guppi-config`, whose new Purposes Cases 820.1 and 820.2 write first. No other new text of this Case holds an old command, since the `reword` would rewrite it. A Grep `make (test|lint|style)\b[^-]` over the repository, `vault/raw/` and `vault/archive/` left out, printed 215 places in 85 files. The pair is a whole word, so `make test-harness` and `make test-cart` stay. Each match on a live rule, entity or Estimate reads true with the new command but the Criterion of `estimate-harness-make-runs-in-both-shells`, which names the old commands as targets of the `Makefile`; the person chose to replace it in words the `reword` leaves alone (Case 820.7). The Criterion of `estimate-sprint-plugin-pull-requests-reviewed-on-github` says that CI runs the three old commands of the `Makefile`, which after the `reword` would name the new commands as targets of the `Makefile`; it stays `pending` and Case 820.8 replaces it with the same promise and the commands that CI runs, each other line word for word. `estimate-skill-sprint-close-migration-merged-into-main` passed on a run of the old test command, which ran the same pytest that `guppi test` runs here, so its Criterion reads true under the new name. The `reword` also previews over Decision pages, lessons and Insights, such as `decision-case-807` and `lesson-obsidian-cli-needs-the-running-app`; `guppi generate` changes only rules, entities and Estimates, so those stand as records. Where the `reword` of Case 819.1 and this one hit the same sentence of an Estimate, each changes its own words, a command of the code against a target of make, so the two compose. Case 819.1 changes the first sentence of the field `method` of the Render of `rule-estimates-schema`, the list of the four forms, so the pair of Case 820.3 leaves that sentence alone and adds the three commands in a sentence of their own before the sentence on the form of a MOC, which no other Case of the session changes. Before that pair, the field `method` goes on to say that a path must exist and a make target must stand in the `Makefile`, which still holds, since the three commands need no file of their own. In `entity-glossary`, the `reword` changes the row of Lint, which then says that `guppi check` runs `guppi lint` after the render, sprint, backlog and glossary checks, and the row of Work Mode, whose baseline then holds `guppi test` and `guppi check`; both read true. The pair of Case 820.5 on `rule-clean-branch` adds a sentence before the sentence on `guppi ship --check` that Case 818.1 changes, and neither touches the words of the other. Lessons, Insights, Decision pages, `log.md` and `brief.md` keep the old words as records. `rule-documentation` names the `Makefile` among the files of the scripts, which stays true while it stands. The Criteria of `estimate-lint-runs-every-step`, `estimate-lint-checks-the-method` and `estimate-prespec-catches-a-method-without-a-form` are replaced whole, with their `purpose` and `method` where these state the old promise. The Criterion of `estimate-prespec-hook-reports-a-pointer-outside-a-bracket` says that the judgment is imported from `guppi/ship.py`, so Case 820.6 replaces it. Each line of the four replaced Criteria that the check of this file notes as not carried stands in the new Criterion with the new command, the new paths or the new forms. Case 820.7 adds no Estimate for the `reword` and for `.github/workflows/checks.yml`: the lines on the texts and the CI jobs in the Criteria of Cases 820.1 and 820.2 check them. `estimate-harness-pipeline` and `estimate-guppi-tests-green` stand, since after the `reword` they promise the same under the new command. `estimate-guppi-config-fills-the-languages` stands, since its Criterion speaks of the render of the languages, which the new keys do not change. `estimate-clean-branch-code-holds-pointers-only-in-brackets` stands: it names the `Makefile` among the files on which `guppi ship --check` prints no line, which holds when the clean version no longer holds that file. CI runs the new commands; a push between the Work Mode and the librarian's run would see the job `test` red, since `guppi.toml` gets its keys at that run. A Grep `__file__|project_root\(\)|ROOT|REPO` over `tests/` printed `test_case_schema.py`, `test_orchestration.py`, `test_schemas.py`, `test_lint.py`, `test_materialize.py` and `test_generate.py`. `test_lint.py` runs the target `lint` of the live `Makefile` and lists the six steps, so Case 820.7 makes it expect `guppi check` alone. `test_case_schema.py` runs the check over the example Case, whose method names `make test-cart`, a form both sides still take. The others read the lists of the `schema.yaml` files, and Case 820.3 changes only the prose of the `method` field of the estimates schema. Case 819, built again in this session, lists no `Makefile` among the files that `guppi ship` writes, in its new text of `rule-clean-branch`, its `then` and its task on `ROOT_FILES`, and for `ship.py` its `then` points to `estimate-clean-branch-ships-no-ship-command`, which makes that promise here. Case 821.4 anchors on the end of the sentence that Case 820.5 adds to `rule-clean-branch`, and Case 821.2 ships the tests but `.guppi/tests/test_ship.py`, so the tests of the command `ship` that Case 820.5 adds stay out of the clean version with that file. Case 820.5 adds its sentence of `rule-clean-branch` after words that Cases 816, 818 and 819 leave alone. Cases 816, 817 and 818 change no text this Case touches; `rule-morph`, which Case 817 changes, names the languages as values the install Case asks for, and stays true with the two new keys.

> **problem:**
> GUPPI runs its tests, its style check and its vault checks through `make`, which a project that installs GUPPI may not have and cannot get from GUPPI's Python environment, and it gives every such project a command `ship` that only this repository can use.

> **recommend:**
> - **What runs the vault checks in place of `make lint`**
>   - Recommended: (a) a new command `guppi check` that runs the same steps in the same order, each one even after a red step, red if any is.
>   - Answer: agreed, (a).
> - **Whether `guppi check` judges GUPPI's clean version in every project**
>   - Recommended: (b) only where the folder `plugin/` stands.
>   - Answer: (c) the user does not get `ship`: the clean version holds no `guppi/ship.py`, the judgment of a pointer moves into a module that `/pre-spec` and `guppi ship` both import, the list of commands has no `ship` when its module is missing, and `guppi check` skips that step then.
> - **What runs the tests in place of `make test`**
>   - Recommended: (a) `guppi test` runs a command set in `guppi.toml`.
>   - Answer: agreed, (a).
> - **What runs the style check in place of `make style`**
>   - Recommended: (a) `guppi style` runs a second command set in `guppi.toml`.
>   - Answer: agreed, (a).
> - **What a group rule's Estimate names in place of a make target**
>   - Recommended: (a) the method lists the test files.
>   - Answer: agreed, (a).
> - **When the `Makefile` leaves this repository**
>   - Recommended: (a) a thin `Makefile` stays here until a Case of a later session removes it, and the clean version stops writing it now.
>   - Answer: agreed, (a).
> - **How the pages and the harness take the new commands**
>   - Recommended: (a) one `reword` per command, and real changes only where make itself is the promise.
>   - Answer: agreed, (a).
> - **When the group Estimates switch to the list of test files**
>   - Recommended: (a) this Case teaches the checks the new form, and a Case of a later session moves the Estimates.
>   - Answer: agreed, (a).
> - **Whether a method may name `guppi test`, `guppi check` or `guppi style`**
>   - Recommended: (a) the three new commands count as a form.
>   - Answer: agreed, (a).
> - **What `guppi test` and `guppi style` do where `guppi.toml` sets no command**
>   - Recommended: (a) say so and exit non-zero.
>   - Answer: agreed, (a).
> - **The form of the two settings in `guppi.toml`**
>   - Recommended: (a) two keys, `test` and `style`, each a list of commands run in order.
>   - Answer: agreed, (a).
> - **What checks that this is done**
>   - Recommended: (a) new Estimates where nothing checks the change, and the replaced Criteria where one does.
>   - Answer: agreed, (a).
> - **What the thin `Makefile` runs for `test` and `style` until the next session**
>   - Recommended: (a) `lint` calls `guppi check`; `test` and `style` keep their own commands.
>   - Answer: agreed, (a).
> - **The check of the `Makefile` under both shells**
>   - Recommended: (a) replace its Criterion, naming the targets in words that the replace leaves alone.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: by the findings of `/pre-spec`, the person chose that `rule-guppi-config` ships with the commands of the repository of GUPPI until the install Case of `rule-morph` sets a project's own, and that the wording, not the shipping, changes; the shipped texts hold in any project; the two new children of `rule-harness` join its list; one function judges whether the module of `ship` stands; and the line on the texts gets a reading after the librarian's run.
>   - Taken: the Purpose of `rule-guppi-config` says that a new project runs the tests of GUPPI until the install Case sets its own; the sentence of `rule-harness` names the repository of GUPPI and the clean version; Case 820.9 adds both rules to the list of `rule-harness` and replaces the Criterion of `estimate-harness-pipeline`; `ship_stands` of `guppi/pages.py` serves `guppi check`, the list of commands and `guppi lint`; the methods of the Estimates of Cases 820.1 and 820.2 read the texts by hand after the librarian's run.

### Case 820.1 — guppi check runs the vault checks

> **given:**
> `rule-lint`: the rule of `guppi lint` and of the command that runs the vault checks.
> **＋** `estimate-lint-runs-every-step`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/check.py`, `.guppi/guppi/cli.py` and `.guppi/tests/test_check.py`: the new command `guppi check`, the list of commands of `guppi`, and the tests of the new command.
> **＋** `.guppi/guppi/ship.py`: the module of the command `ship`, which a project that installed GUPPI does not hold.
> **＋** `.claude/agents/librarian-guppi.md`, `.claude/skills/work/SKILL.md` and `.github/workflows/checks.yml`: the librarian's run, the Baseline of `/work` and the CI job that run the vault checks.
> **＋** `.claude/`: the harness files that name the command of the vault checks.

> **when:**
> Someone runs `uv run --project .guppi guppi check` in a project: by hand, in the Baseline of `/work`, in the librarian's run of `.claude/agents/librarian-guppi.md`, or in the job `lint` of `.github/workflows/checks.yml`.
> **＋** Or `.guppi/tests/test_check.py` runs it in a temporary project whose steps record each call: once with the step `guppi backlog --check` failing, once with every step exiting 0, and once with no module `.guppi/guppi/ship.py`.

> **then:**
> It runs `guppi render --check`, `guppi sprint --check`, `guppi backlog --check`, `guppi glossary --check`, `guppi lint` and `guppi ship --check`, in that order, whether an earlier step exited 0 or not.
> **＋** Each step prints its own lines as it does when it runs alone, so a red step hides no finding of a later step.
> **＋** It exits non-zero when any step exits non-zero, and 0 only when every step exits 0.
> **＋** No live rule, entity or Estimate outside History and Result, and no file of `.claude/`, names make with the target `lint` as the way to run the vault checks.
> **－** Where the module `.guppi/guppi/ship.py` is missing, as in a project that installed GUPPI, it runs the other five steps and prints one line that it skips `guppi ship --check`, and that skip sets no exit code.
> **－** No step reads the stdin of its caller, and it writes nothing to the tree.

```then
update:
- slug: rule-lint
  set:
    implementation_ref:
    - .guppi/guppi/lint.py
    - .guppi/guppi/check.py
    - .guppi/tests/test_lint.py
    - .guppi/tests/test_check.py
  sections:
    Purpose: |-
      Prevents a page that breaks its schema, points at nothing, claims a status its
      Estimates do not support, or waits for a reading nobody took from sitting in the vault
      unnoticed. Pages are written by the generator;
      both drift, and nothing else reads the whole graph at once. Red is a signal, not a
      gate: a `pending` Estimate is red until its reading, but for one whose `method` waits for a later moment — an event it names, a later session, a session of a sprint, the session that closes one, the librarian or `/hi` — since the brief lists it under Readings due and puts it under Work once its moment comes, and a `failed` one is red until it is read again (cases 182, 799); a placeholder is red with the count of its defers (case 186.3).
      `uv run --project .guppi guppi check` runs it after `guppi render --check`, `guppi sprint --check`, `guppi backlog --check` and `guppi glossary --check`, and runs `guppi ship --check` after it, which finds a pointer outside its bracket in each file outside `vault/` that the clean version holds (case 807.2). Where the command `ship` is missing, as in a project that installed GUPPI, it prints one line that it skips that step and runs the other five (case 820). All six only report, so no step writes to the tree (cases 147.7, 227). It runs every step even when one of them is red, so a red step hides no finding of a later one, and it exits non-zero when any step is red (case 587). It needs no tool but `uv`, so a project runs it on any machine (case 820). `parent: rule-harness` names the
      MOC of the harness tools: lint runs with the renderer, in no phase of the session. The
      classes and their order live in the docstring of `.guppi/guppi/lint.py`.
  change: guppi check runs the six vault checks, and skips guppi ship --check where the command ship is missing
- slug: estimate-lint-runs-every-step
  set:
    status: pending
    purpose: Whether guppi check runs every step, guppi ship --check last, when an earlier one is red, prints the lines of each, exits non-zero when any step is red, and skips guppi ship --check where the command ship is missing
    method: 'uv run --project .guppi pytest .guppi/tests/test_check.py; by hand, after the librarian''s run that applies the reword of this change: a Grep of make with the target lint over the live rules, entities and Estimates and over .claude/, read against the Criterion'
  change: the Criterion replaced whole — guppi check runs the vault checks in place of the target lint of the Makefile
```

```tasks
- [x] update `rule-lint`
- [x] update `estimate-lint-runs-every-step`
- [x] `.guppi/guppi/check.py`: `run` runs the six steps in order, each even after a red one, each with its own output and no stdin, exits non-zero when any is red, and skips `guppi ship --check` with one line when `ship_stands` of `.guppi/guppi/pages.py` answers that the module `guppi.ship` is missing; the docstring says so and names `rule-lint`.
- [x] `.guppi/guppi/pages.py`: `ship_stands`, the one judgment of whether the module `guppi.ship` stands, which `guppi check`, the list of commands of `.guppi/guppi/cli.py` and the check of a draft page of `guppi lint` import; the docstring names them.
- [x] `.guppi/guppi/cli.py`: the command `check` in `COMMANDS`.
- [x] `.guppi/tests/test_check.py`: the order of the steps, every step after a red `guppi backlog --check`, the exit code with one red step and with none, no stdin read, the tree unchanged, and the skip of `guppi ship --check` with its one line when the module is missing.
- [ ] read `estimate-lint-runs-every-step`
```

### Case 820.2 — guppi test and guppi style run the commands of guppi.toml

> **given:**
> `rule-guppi-config`: the rule of `guppi.toml`, which now also sets the commands of the tests and of the style check.
> **＋** `estimate-guppi-config-runs-the-test-and-style-commands`: the new check of the two commands.
> **＋** `guppi.toml`: the settings file, rendered from the Render of `rule-guppi-config`.
> **＋** `.guppi/guppi/commands.py`, `.guppi/guppi/config.py`, `.guppi/guppi/cli.py` and `.guppi/tests/test_commands.py`: the two new commands, the reader of `guppi.toml`, the list of commands of `guppi`, and the tests of the new commands.
> **＋** `.claude/skills/work/SKILL.md`, `.claude/skills/retro/SKILL.md` and `.github/workflows/checks.yml`: the Baseline of `/work`, Retro and the CI jobs that run the tests and the style check.
> **＋** `.claude/`: the harness files that name the commands of the tests and of the style check.
> **＋** `rule-morph`: the install Case that sets the settings of a new project.

> **when:**
> Someone runs `uv run --project .guppi guppi test` or `uv run --project .guppi guppi style` in a project, as `rule-guppi-config` sets it: by hand, in the Baseline of `/work`, in Retro, or in the jobs `test` and `style` of `.github/workflows/checks.yml`.

> **then:**
> It reads the list of commands of the key `test`, or of the key `style`, from `guppi.toml` at the root of the project.
> **＋** It runs each command of the list in order, in the folder of the project and with no shell between, each one even after a red one.
> **＋** The output of each command reaches the person whole, and no command gets the stdin of `guppi test` or `guppi style`.
> **＋** A single red command makes the run red; the run is green only when all the listed commands pass.
> **＋** In this repository, the key `test` holds `uv run --project .guppi pytest -q`, and the key `style` holds `uv run --project .guppi ruff check .` and `uv run --project .guppi ruff format --check .`.
> **＋** The rules, entities and Estimates of the vault and the harness files of `.claude/` call the tests and the style check by these two commands, and never by make.
> **－** When `guppi.toml` is missing or holds no such key, it prints one line that names the file and the key, runs nothing and exits 1.
> **－** The render reads `documentation_lang` and `chat_lang` as before, and a key `test` or `style` does not stop it.

```then
create:
- slug: estimate-guppi-config-runs-the-test-and-style-commands
  ref: rule-guppi-config
  kind: QA
  purpose: Whether guppi test and guppi style run the commands that the keys test and style of guppi.toml list, in order and each after a red one, exit non-zero when any is red, and exit 1 with one line when the file or the key is missing
  method: 'uv run --project .guppi pytest .guppi/tests/test_commands.py; by hand, after the librarian''s run that renders guppi.toml with the keys test and style: uv run --project .guppi guppi test and uv run --project .guppi guppi style in this repository, and a Grep of make with the targets test and style over the live rules, entities and Estimates and over .claude/, read against the Criterion'
  tags:
  - harness
  - tests
update:
- slug: rule-guppi-config
  set:
    implementation_ref:
    - .guppi/guppi/config.py
    - .guppi/guppi/commands.py
    - .guppi/tests/test_config.py
    - .guppi/tests/test_commands.py
  sections:
    Purpose: |-
      Prevents a setting of guppi from being written by hand into the texts that use it, or changed outside a ratified decision. This page's Render is `guppi.toml`, guppi's one settings file: a change is an `update` of the Render, and the governed-files hook refuses a hand edit of the file. It sets the language of the repository, `documentation_lang`, and the language of the chat with the owner, `chat_lang`, as codes; `.guppi/guppi/config.py` holds the table of each code's name and script. The render reads the codes from this Render and puts the name where another Render writes `{{documentation_lang}}` or `{{chat_lang}}`; the checks, such as the pre-spec finding, read `guppi.toml`.

      It also sets how the project tests its code and checks its style: the key `test` and the key `style`, each a list of commands. `uv run --project .guppi guppi test` runs the commands of `test`, and `uv run --project .guppi guppi style` the commands of `style`, which `.guppi/guppi/commands.py` reads from `guppi.toml` through `.guppi/guppi/config.py`. Each runs its commands in order, in the folder of the project and with no shell between, runs each one even after a red one, lets each print its own lines, and exits non-zero when any of them does. When `guppi.toml` or the key is missing, it prints one line that names the file and the key, runs nothing and exits 1. The Render holds the commands of the repository of GUPPI, and a project that installs GUPPI takes them as they stand, so its `guppi test` runs the tests of GUPPI until the install Case of `rule-morph` sets the project's own commands. Work Mode, Retro and the CI of the project run these two commands, so a project needs no tool but `uv` (case 820). The questions asked at install, these two commands among them, stay with `rule-morph` (cases 476.1, 802); the category set as data waits as a line of the `## Backlog` of `entity-sprint-plugin` (case 802).
    Render: |-
      <!-- rule-guppi-config -->
      # guppi settings, rendered from vault/wiki/rules/rule-guppi-config.md
      documentation_lang = "en"
      chat_lang = "ru"
      test = ["uv run --project .guppi pytest -q"]
      style = ["uv run --project .guppi ruff check .", "uv run --project .guppi ruff format --check ."]
      <!-- /rule-guppi-config -->
  change: guppi.toml sets the commands of the tests and of the style check, which guppi test and guppi style run
```

```tasks
- [x] update `rule-guppi-config`
- [x] create `estimate-guppi-config-runs-the-test-and-style-commands`
- [x] `.guppi/guppi/config.py`: one function reads the list of commands of a key of `guppi.toml`, and names the file and the key when either is missing; `parse` still checks only the two language keys; the docstring says so.
- [x] `.guppi/guppi/commands.py`: `guppi test` and `guppi style` read their key through `.guppi/guppi/config.py`, split each command into its words and run it in the folder of the project with no shell and no stdin, each after a red one, and exit non-zero when any is red, or exit 1 with one line when the file or the key is missing; the docstring names `rule-guppi-config`.
- [x] `.guppi/guppi/cli.py`: the commands `test` and `style` in `COMMANDS`.
- [x] `.guppi/tests/test_commands.py`: the order of the commands, every command after a red one, the exit code with one red command and with none, no stdin read, no shell, and the one line with exit 1 for a missing `guppi.toml` and for a missing key.
- [x] `uv run guppi render`: `guppi.toml`
- [ ] read `estimate-guppi-config-runs-the-test-and-style-commands`
```

### Case 820.3 — guppi lint takes the new forms of a method

> **given:**
> `rule-estimates-schema`: the schema of an Estimate, whose field `method` names the forms that lint classifies.
> **＋** `estimate-lint-checks-the-method`: its Criterion is replaced whole.
> **＋** `vault/wiki/estimates/schema.yaml`: the Render of `rule-estimates-schema`, which `guppi lint` reads.
> **＋** `.guppi/guppi/lint.py`: `names_a_form`, `names_a_moc_form`, `sibling_names_a_target` and `check_method`.
> **＋** `.guppi/tests/test_lint.py`: the tests of the method check.
> **＋** `Makefile`: the targets of the pipelines of the MOCs, which this repository keeps for now.
> **＋** `estimate-claude-md-rendered`: the Estimate that gets no `method` finding.

> **when:**
> `uv run --project .guppi guppi lint` reads the `method` field of each live Estimate.

> **then:**
> For an Estimate of a Leaf, a test file that exists, the word `pytest`, a `make <target>` of the `Makefile`, one of the commands `guppi test`, `guppi check` and `guppi style`, or `by hand` passes; else the finding "method: names no test file, pytest, guppi command or make target and is not a reading".
> **＋** A named test file that does not exist, or a `make <target>` that the `Makefile` does not hold, is a finding.
> **＋** For an Estimate of a MOC, a `make <target>` of the `Makefile` passes whatever stands beside it, and so does the word `pytest` with one or more test files, each of which exists.
> **＋** For an Estimate of a MOC, `by hand` without either passes when every counted Estimate of the children is a reading or a sibling Estimate names either; else a finding.
> **＋** On a MOC with `render_mode: full`, the Estimates of a child with `enforcement: render` are not counted.
> **＋** `estimate-claude-md-rendered` gets no `method` finding.
> **－** On a MOC, the word `pytest` with no test file, a test file with no `pytest`, and a command `guppi test`, `guppi check` or `guppi style` alone are each a finding.
> **－** On a MOC with `render_mode: full`, the Estimates of a child without `enforcement: render` are counted.
> **－** On a MOC without `render_mode: full`, the Estimates of every child are counted, a child with `enforcement: render` included.
> **－** A `## Method` section is not read as the `method` of a page.

```then
update:
- slug: rule-estimates-schema
  replace:
  - old: On the Estimate of a MOC the form is a `make <target>` of the Makefile alone — there `pytest` or a path by itself earns a finding, and `by hand` passes only when every child's Estimate is a reading or a sibling Estimate of the MOC names such a target;
    new: Besides these four forms, the Estimate of a Leaf may name one of the commands `guppi test`, `guppi check` and `guppi style`, which run the tests, the vault checks and the style check of the project. On the Estimate of a MOC the form is a `make <target>` of the Makefile, or the word `pytest` with the test files of its pipeline, each of which must exist — there `pytest` without a test file, a path without `pytest`, or one of the commands of the project alone earns a finding, and `by hand` passes only when every child's Estimate is a reading or a sibling Estimate of the MOC names such a form;
  change: a method may name guppi test, guppi check or guppi style, and the Estimate of a MOC may name pytest with the test files of its pipeline
- slug: estimate-lint-checks-the-method
  set:
    status: pending
  change: the Criterion replaced whole — the commands guppi test, guppi check and guppi style are forms, and on a MOC pytest with test files that exist passes
```

```tasks
- [x] update `rule-estimates-schema`
- [x] update `estimate-lint-checks-the-method`
- [x] `.guppi/guppi/lint.py`: `names_a_form` takes the commands `guppi test`, `guppi check` and `guppi style`; `names_a_moc_form` takes the word `pytest` with one or more test paths; `check_method` checks on a MOC that each such path exists, and `sibling_names_a_target` takes a sibling that names such a form; the finding names the new forms; the docstrings say so.
- [x] `.guppi/tests/test_lint.py`: on a Leaf each of the three commands passes; on a MOC `pytest` with test files that exist passes, a missing one is a finding, and `pytest` alone, a path alone and a command alone are findings; a sibling with `pytest` and test files lets `by hand` pass; the tests of a `make <target>` stand.
- [x] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`
- [x] read `estimate-lint-checks-the-method`
```

### Case 820.4 — /pre-spec takes the new forms of a method

> **given:**
> `estimate-prespec-catches-a-method-without-a-form`: its Criterion is replaced whole.
> **＋** `rule-prespec`: the rule of `/pre-spec`, the target of that Estimate.
> **＋** `.guppi/guppi/prespec.py`: `NO_FORM`, `MOC_NO_FORM` and the method check of the plan.
> **＋** `.guppi/guppi/lint.py`: `names_a_form` and `names_a_moc_form`, which `/pre-spec` imports, and `check_method`.
> **＋** `.guppi/tests/test_prespec.py`: the tests of `/pre-spec`.
> **＋** `Makefile`: the targets of the pipelines that a MOC's `method` may name.

> **when:**
> `uv run --project .guppi guppi prespec --check <plan> --session <id>` reads the items of the plan's `then` blocks before the Spec is approved.

> **then:**
> A `create` of an Estimate, or an `update` carrying `set: {method: …}`, whose `method` names none of the forms lint classifies (a `make <target>`, the word `pytest`, a test path, one of the commands `guppi test`, `guppi check` and `guppi style`, or the words `by hand`) gives one line `case N: <create|update> <slug>: method names no form`, which goes on to name those forms.
> **＋** A `create` of an Estimate with no `method` at all gives the same finding.
> **＋** When the target of the Estimate is a MOC as the plan leaves it — the live page, or a `create` or an `update` of the plan that writes `kind: MOC` — a `method` that names neither a `make <target>`, nor the word `pytest` with a test path, nor `by hand` gives one line `case N: <create|update> <slug>: method of a MOC's Estimate names no make target or test files and is not a reading`, in place of the line of no form.
> **＋** The predicate is one, lifted out of `.guppi/guppi/lint.py`; `/pre-spec` writes no second one.
> **＋** The form of a MOC's `method` is one predicate too, in `.guppi/guppi/lint.py`, which `check_method` of `guppi lint` calls as well.
> **－** Existence is not checked in the plan: the test file is written in Work Mode, and lint checks it later.
> **－** Whether the `Makefile` holds the `make <target>` that a MOC's `method` names is left to lint.
> **－** Whether every counted Estimate of the MOC's children is a reading, or a sibling Estimate names a form of a MOC, is left to lint.
> **－** An `update` of an Estimate that writes no `method` gives no line of the form of a MOC's `method`.

```then
update:
- slug: estimate-prespec-catches-a-method-without-a-form
  set:
    status: pending
    purpose: Whether pre-spec refuses an Estimate whose method names none of the forms lint classifies, or, on a MOC, neither a make target, nor pytest with a test path, nor by hand
    method: uv run --project .guppi pytest .guppi/tests/test_prespec.py on a temp plan — a create with a prose method, a create with no method, each of the five forms clean, and on a MOC a test path alone, pytest alone and guppi test alone as findings, a make target, pytest with a test path and by hand clean
  change: the Criterion replaced whole — the commands guppi test, guppi check and guppi style are forms, and on a MOC pytest with a test path is one
```

```tasks
- [x] update `estimate-prespec-catches-a-method-without-a-form`
- [x] `.guppi/guppi/prespec.py`: `NO_FORM` and `MOC_NO_FORM` name the new forms; the method check of the plan calls `names_a_form` and `names_a_moc_form` of `.guppi/guppi/lint.py` as before; the docstring says so.
- [x] `.guppi/tests/test_prespec.py`: each of the five forms clean on a Leaf; on a MOC `pytest` with a test path clean, and a test path alone, `pytest` alone and `guppi test` alone each the line of a MOC; the lines name the new forms.
- [x] read `estimate-prespec-catches-a-method-without-a-form`
```

### Case 820.5 — The clean version holds no command ship

> **given:**
> `rule-clean-branch`: the rule of `guppi ship`.
> **＋** `estimate-clean-branch-ships-no-ship-command`: the new check that the clean version holds no command `ship`.
> **＋** `.guppi/guppi/ship.py`, `.guppi/guppi/pointers.py` and `.guppi/guppi/cli.py`: the command `ship`, the new module of the judgment of a pointer, and the list of commands of `guppi`.
> **＋** `.guppi/tests/test_ship.py`: the tests of `guppi ship`.
> **＋** `vault/raw/2026-10-15/0553/cases/case-816.md`, `vault/raw/2026-10-15/0553/cases/case-818.md` and `vault/raw/2026-10-15/0553/cases/case-819.md`: the Cases of this session that change other sentences of `rule-clean-branch`.

> **when:**
> `uv run --project .guppi guppi ship <folder>` builds the clean version of this repository into an empty folder, as `rule-clean-branch` sets it.
> **＋** Then `guppi` runs from the code of that folder, with no argument and with the argument `ship`.

> **then:**
> The clean version holds `.guppi/guppi/pointers.py` and no `.guppi/guppi/ship.py`.
> **＋** Run from the code of the clean version, `guppi` lists no command `ship`, and `guppi ship` prints that the command is unknown and exits 2.
> **＋** `guppi ship` removes and refuses a pointer by the functions of `.guppi/guppi/pointers.py`, and holds no copy of them.
> **－** `guppi ship --check` does not judge `.guppi/guppi/ship.py`, which the clean version does not hold.
> **－** In this repository, `guppi` lists the command `ship`, and `guppi ship` runs as `rule-clean-branch` sets it.

```then
create:
- slug: estimate-clean-branch-ships-no-ship-command
  ref: rule-clean-branch
  kind: QA
  purpose: Whether the clean version holds the module of the judgment of a pointer and no module of the command ship, so that guppi there lists no command ship, while guppi ship of this repository judges by that module
  method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k ship_command
  tags:
  - plugin
  - ci
update:
- slug: rule-clean-branch
  replace:
  - old: a Case rewords that text at its source.
    new: a Case rewords that text at its source. It does not write `.guppi/guppi/ship.py`, so a project that installs GUPPI, which builds no clean version, gets no command `ship`, and `guppi check` skips its step `guppi ship --check` there; the judgment of a pointer outside its bracket, which `guppi ship` and `/pre-spec` share, lives in `.guppi/guppi/pointers.py`, which it writes (case 820).
  change: the clean version holds no guppi/ship.py, and the judgment of a pointer lives in guppi/pointers.py
```

```tasks
- [x] update `rule-clean-branch`
- [x] create `estimate-clean-branch-ships-no-ship-command`
- [x] `.guppi/guppi/pointers.py`: `outside` and the functions and patterns it calls, moved from `.guppi/guppi/ship.py` unchanged; the docstring names it the one judgment of a pointer, which `guppi ship` and `/pre-spec` import.
- [x] `.guppi/guppi/ship.py`: imports the judgment of a pointer from `.guppi/guppi/pointers.py` and keeps no copy of it; the copy and `--check` skip `.guppi/guppi/ship.py`; the docstring says so.
- [x] `.guppi/guppi/cli.py`: `COMMANDS` holds `ship` only when `ship_stands` of `.guppi/guppi/pages.py` answers that the module `guppi.ship` stands.
- [x] `.guppi/tests/test_ship.py`: a clean version built into a temporary folder holds `.guppi/guppi/pointers.py` and no `.guppi/guppi/ship.py`; the code of that folder lists no command `ship`, and `guppi ship` there exits 2 with its line; `--check` prints no line for `.guppi/guppi/ship.py`; the names of these tests hold `ship_command`.
- [x] read `estimate-clean-branch-ships-no-ship-command`
```

### Case 820.6 — /pre-spec judges a pointer by the module it shares with guppi ship

> **given:**
> `estimate-prespec-hook-reports-a-pointer-outside-a-bracket`: its Criterion is replaced whole.
> **＋** `rule-prespec-hook`: the rule of the hook at `ExitPlanMode`, the target of that Estimate.
> **＋** `.guppi/guppi/prespec.py` and `.guppi/guppi/pointers.py`: `/pre-spec`, and the module whose judgment of a pointer it imports.
> **＋** `.guppi/tests/test_prespec.py`: the test that asserts that both sides share one judgment.
> **＋** `decision-case-N`: the form of the id of a Decision page.

> **when:**
> `uv run --project .guppi guppi prespec --check <plan>` checks the plan of a session, or the hook of `rule-prespec-hook` runs the same judgment when the agent calls `ExitPlanMode`.

> **then:**
> It prints a finding for each pointer — a reference to a case, an id `decision-case-N` or a mention of a session by its id — that stands outside a bracket of its own in the `new` of a `replace` pair, the text of a `sections` value or the `purpose` of an item for a page that carries `core: true`, on the live page or as the plan leaves it.
> **＋** The finding names the Case, the page and the pointer.
> **＋** It judges each text by `outside` of `.guppi/guppi/pointers.py`, imported, the judgment that `guppi ship` runs over the files it writes.
> **－** A pointer inside such a bracket, a code span or a fenced block is no finding.
> **－** An item for a page without `core: true`, the `change` line of an item, and the `context`, `problem` and `recommend` of a Case are not judged.

```then
update:
- slug: estimate-prespec-hook-reports-a-pointer-outside-a-bracket
  set:
    status: pending
  change: the Criterion replaced whole — the judgment of a pointer is imported from guppi/pointers.py
```

```tasks
- [x] update `estimate-prespec-hook-reports-a-pointer-outside-a-bracket`
- [x] `.guppi/guppi/prespec.py`: imports `outside` from `.guppi/guppi/pointers.py`; the docstrings name that module.
- [x] `.guppi/tests/test_prespec.py`: the test that asserted `prespec.outside is ship.outside` asserts `prespec.outside is pointers.outside`.
- [x] read `estimate-prespec-hook-reports-a-pointer-outside-a-bracket`
```

### Case 820.7 — The Makefile stays for now and every text names the new commands

> **given:**
> `rule-harness`: the MOC of the harness tools, whose Purpose names the `Makefile` that stays for now.
> **＋** `estimate-harness-make-runs-in-both-shells`: its Criterion is replaced whole.
> **＋** `Makefile` and `.guppi/tests/test_lint.py`: the targets that this repository keeps until a later Case removes the file, and the test that runs its target `lint`.
> **＋** `rule-lint` and `rule-guppi-config`: the owners of the replace of the old commands over every live rule, entity and Estimate.
> **＋** `.github/workflows/checks.yml` and `rule-github-repository`: the CI jobs and their rule.
> **＋** `.claude/`, `vault/wiki/where-to-stop.md`, `vault/wiki/case-schema.md` and `vault/wiki/glossary.md`: the rendered files whose pages the replace changes.
> **＋** `.guppi/guppi/`: the docstrings that name the old commands.
> **＋** `C:/ProgramData/chocolatey/bin/make.exe`, `/dev/null` and `/usr/bin/sh`: the make of Windows that reads the `Makefile`, the stdin of each recipe, and the shell of the `Makefile` outside Windows.

> **when:**
> On Windows, someone runs make with each of the targets `help`, `style`, `test` and `lint` of the `Makefile` from PowerShell and from Git Bash. `C:/ProgramData/chocolatey/bin/make.exe` reads the `Makefile`.
> **＋** Or `.guppi/tests/test_lint.py` runs make with the target `lint` of the `Makefile` in a temporary folder, with a fake `uv` first on the search path that records each call.

> **then:**
> Make runs each recipe under a POSIX `sh`, with stdin read from `/dev/null`, and each target gives the same exit code from PowerShell as from Git Bash.
> **＋** The target `lint` runs `uv run --project .guppi guppi check` and nothing else.
> **＋** The target `test` runs pytest over the tests of `.guppi/tests/`, and the target `style` runs ruff, both as they did before this change.
> **＋** The targets of the pipelines of the MOCs stand as before.
> **＋** When make finds no POSIX `sh` on Windows, it stops before any recipe runs, with one message that names the missing shell and the places it searched.
> **－** Make never runs a recipe of the `Makefile` under `cmd.exe`.
> **－** Running a target changes no file of the working tree.
> **－** Outside Windows, the `SHELL` of the `Makefile` stays `/usr/bin/sh`.

```then
update:
- slug: rule-harness
  replace:
  - old: (cases 59.6, 59.8, 127, 145.1, 304, 315, 392.3, 420.1, 476.1, 640, 710.1, 796).
    new: '(cases 59.6, 59.8, 127, 145.1, 304, 315, 392.3, 420.1, 476.1, 640, 710.1, 796). The repository of GUPPI keeps for its own work, for now, a `Makefile`: its target `lint` runs `uv run --project .guppi guppi check`, its target `test` runs pytest, its target `style` runs ruff, and one target runs the tests of each pipeline of a MOC, each under a POSIX shell on Windows too; the clean version of GUPPI holds no `Makefile`, and a later Case removes it (case 820).'
  change: 'the Makefile stays for now: its target lint runs guppi check, and its other targets stand'
- slug: estimate-harness-make-runs-in-both-shells
  set:
    status: pending
    purpose: Whether the Makefile that this repository keeps for now runs its targets help, style, test and lint under a POSIX sh from PowerShell as from Git Bash, its target lint runs guppi check alone, and it stops with a message when no sh is found
    method: 'uv run --project .guppi pytest .guppi/tests/test_lint.py -k makefile; by hand, after the Work Mode that builds this change: make with the targets help, style, test and lint from PowerShell and from Git Bash on Windows, read against the Criterion'
  change: the Criterion replaced whole — the Makefile stays for now, and its target lint runs guppi check
- slug: rule-lint
  reword:
  - old: make lint
    new: uv run --project .guppi guppi check
  change: every live rule, entity and Estimate names guppi check in place of the target lint of the Makefile
- slug: rule-guppi-config
  reword:
  - old: make test
    new: uv run --project .guppi guppi test
  - old: make style
    new: uv run --project .guppi guppi style
  change: every live rule, entity and Estimate names guppi test and guppi style in place of the targets test and style of the Makefile
```

```tasks
- [x] update `rule-harness`
- [x] update `estimate-harness-make-runs-in-both-shells`
- [x] update `rule-lint`
- [x] update `rule-guppi-config`
- [x] `Makefile`: the target `lint` runs `uv run --project .guppi guppi check` alone; the targets `help`, `test`, `style` and those of the pipelines keep their recipes; the comment at the top says that the file stays until a later Case removes it, that `guppi check`, `guppi test` and `guppi style` are the commands of the checks, and that the clean version does not hold it.
- [x] `.guppi/tests/test_lint.py`: the test of the target `lint` of the `Makefile` records one call, `run --project .guppi guppi check`, and its name holds `makefile`; the tests of the steps move to `.guppi/tests/test_check.py`.
- [x] `.github/workflows/checks.yml`: the jobs `style`, `test` and `lint` run `uv run --project .guppi guppi style`, `uv run --project .guppi guppi test` and `uv run --project .guppi guppi check`, with no step that installs make; the comment at the top says so.
- [x] `.guppi/guppi/`: each docstring, comment and message that names the old commands names `guppi check`, `guppi test` or `guppi style`.
- [x] `uv run guppi render`: `.claude/skills/work/SKILL.md`
- [x] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
- [x] `uv run guppi render`: `.claude/skills/handoff/SKILL.md`
- [x] `uv run guppi render`: `.claude/skills/carry/SKILL.md`
- [x] `uv run guppi render`: `.claude/skills/box/SKILL.md`
- [x] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [x] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [x] `uv run guppi render`: `vault/wiki/where-to-stop.md`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] `uv run guppi glossary`
- [x] read `estimate-harness-make-runs-in-both-shells`
```

### Case 820.8 — The sprint's check of a pull request names the commands that CI runs

> **given:**
> `estimate-sprint-plugin-pull-requests-reviewed-on-github`: its Criterion is replaced whole.
> **＋** `entity-sprint-plugin`: the sprint page, the target of that Estimate.
> **＋** `.github/workflows/checks.yml` and `rule-github-repository`: the CI jobs and their rule.
> **＋** `GUPPI`, `main`, `prod` and `plugin`: the repository on GitHub and its branches.

> **when:**
> In a session of the sprint `plugin` before its close, someone opens a pull request against the branch `main` of the repository `GUPPI` on GitHub, which `rule-github-repository` describes, from an account other than the owner's, such as a second account that the owner made for the test.

> **then:**
> The workflow `.github/workflows/checks.yml` runs its jobs `test`, `lint` and `style` on `windows-latest` on the pull request, by `uv run --project .guppi guppi test`, `uv run --project .guppi guppi check` and `uv run --project .guppi guppi style`, and shows each result on it.
> **＋** A run of a first-time contributor waits until the owner approves it.
> **＋** The owner reviews the pull request on GitHub, and only the owner can merge it.
> **＋** A merge into `main` waits until the jobs `style` and `test` pass, except for the owner, who is on the bypass list of the ruleset on `main`.
> **＋** The other account cannot push to `main` or to `prod`, and a pull request against `prod` cannot be merged.
> **－** A red result of the job `lint` does not block a merge into `main`.
> **－** The workflow does not run on the event `pull_request_target`, so the code of the pull request reaches no secret of the repository.
> **－** The test pull request is closed without a merge, so `main` takes no commit before `plugin` closes.

```then
update:
- slug: estimate-sprint-plugin-pull-requests-reviewed-on-github
  set:
    status: pending
  change: the Criterion replaced whole — the jobs of CI run guppi test, guppi check and guppi style in place of the targets of the Makefile
```

```tasks
- [x] update `estimate-sprint-plugin-pull-requests-reviewed-on-github`
- [ ] read `estimate-sprint-plugin-pull-requests-reviewed-on-github`
```

### Case 820.9 — rule-harness names its new children that run in no pipeline

> **given:**
> `rule-harness`: the MOC of the harness tools, whose Purpose lists the rules that belong to it and run in no pipeline.
> **＋** `estimate-harness-pipeline`: its Criterion is replaced whole.
> **＋** `rule-guppi-package` and `rule-plugin-install`: the children that Cases 818.1 and 819.1 create under `rule-harness`.
> **＋** `vault/raw/2026-10-15/0553/cases/case-818.md` and `vault/raw/2026-10-15/0553/cases/case-819.md`: the Cases of this session that create them.
> **＋** `rule-sprint`, `rule-backlog`, `settings.json`, `CLAUDE.md`, `guppi.toml` and `.claude/rules/`: the checks and the files that the Purpose names.

> **when:**
> `uv run --project .guppi guppi check` and `make test-harness` run, and someone reads the Purpose of `rule-harness`.

> **then:**
> The Purpose says that three rules belong to no phase of the session: the renderer, the page `settings.json` is assembled from, and lint. With them, the checks of `rule-sprint` and `rule-backlog` run in `uv run --project .guppi guppi check`, in this order: the harness files against their pages, the sprint file against its page, the backlog file against its sources, the glossary file against its page, then the pages.
> **＋** The Purpose names the rules that belong to it and run in no pipeline: the folder of the code of GUPPI and the command that runs it, the skill of the plugin that installs GUPPI into a project, the settings file `guppi.toml`, the schemas of the pages, the layout of the vault, the hook that refuses a hand edit of a rendered file, the hook that refuses a heredoc with a backslash, a file write or an interpreter it feeds, the hook that refuses a PowerShell here-string piped into an interpreter, the hook that repairs or names a file a shell call left with CRLF line endings, a byte-order mark or bytes that are not UTF-8, the page `CLAUDE.md` is rendered from, the pinned clock of the tests, the hook that shows the size of the context, the hooks that read a page of the vault without its History, and the file under `.claude/rules/` that keeps the text of Decision pages out of a search.
> **＋** `make test-harness` is green. The steps of `uv run --project .guppi guppi check` before `guppi lint` (`render --check`, `sprint --check`, `backlog --check` and `glossary --check`) exit 0 with no output on the committed tree. `guppi lint` is read by its own Estimates.

```then
update:
- slug: rule-harness
  replace:
  - old: 'Twelve more belong here and run in no pipeline: the settings file of guppi, `guppi.toml`,'
    new: 'Fourteen more belong here and run in no pipeline: the folder of the code of GUPPI and the command that runs it, the skill of the plugin that installs GUPPI into a project, the settings file of guppi, `guppi.toml`,'
  change: the Purpose names the folder of the code of GUPPI and the skill of the plugin among the rules that run in no pipeline
- slug: estimate-harness-pipeline
  set:
    status: pending
  change: the Criterion replaced whole — the rules in no pipeline include the folder of the code and the skill of the plugin, and the vault checks run by guppi check
```

```tasks
- [x] update `rule-harness`
- [x] update `estimate-harness-pipeline`
- [x] read `estimate-harness-pipeline`
```

## Case 822 — A new project gets the Estimates, the tests, the session files and the CI of GUPPI

> **context:**
> This Case replaces Case 821, which is built again under a new number because its sub-case on draft pages no longer takes `core` off `rule-morph`, and a decision line of Case 821 named that page. Its decision lines carry a mark for Case 821 and for each of its sub-cases. `guppi ship` builds the clean version of GUPPI that a project installs: the code, the harness, the root files and each page with `core: true`. Today it leaves out every Estimate, since no Estimate carries `core`, so each shipped rule lists none. It leaves out the tests, the session files that `/hi` loads, `sprint.md`, `backlog.md`, `brief.md`, `glossary.md` and `log.md`, and the CI. It also ships texts that hold only in this repository, such as `entity-guppi` and the description at the head of `CLAUDE.md`. The person chose the following. An Estimate ships when its target page ships and it stands `passed`; `guppi ship` judges that from the target and writes `core: true` into the copy, and the `## Result` of the copy is one line, the date of the last reading and that it passed, since most Results here name a session, a commit or a case outside a bracket (Case 822.1). At `/pre-spec` the person added that, for now, an Estimate whose `method` names a `make` target does not ship, since the copy holds no `Makefile` and `guppi lint` would report it in every new project; such an Estimate ships once a Case of a later session moves its `method` to pytest. The copy judges a make target by `MAKE_TARGET` of `guppi/lint.py`, imported. Case 822.1 also takes up `decision-case-805`, which put off on `entity-sprint-plugin` whether the clean version ships the Estimates of its rules with the tests; this Case decides both. A Grep `^20\d\d-\d\d-\d\d.*([Cc]ases? \d|decision-case-\d|[Ss]essions? \d{4})` over `vault/wiki/estimates/` printed 184 lines in 183 files, and a Grep `^method:.*([Cc]ases? \d|decision-case-\d|[Ss]essions? \d{4})` over the same folder printed 14 files. A pointer that stays outside a bracket in a `method` or a Criterion stops the build, and a Case of a later session moves it into a bracket at its source. The tests ship. In a test file `guppi ship` cleans and judges only the comments and the docstrings, and each other string is a sample, so the sample ledger lines of the tests stay as data (Case 822.2). A Grep `[Cc]ases? \d|decision-case-\d|[Ss]ession \d{4}` over `tests/` printed 1725 lines in 35 files. The session files ship as skeletons that the writers of those files would write over the copy, `sprint.md` in the closed form of the sprint `guppi`, so the first `/hi` starts `/sprint-open` (Case 822.3). The description of the project in the Render of `rule-claude-md` stands between marker lines of its own (Case 822.5). The copy holds there a line that says it is not set yet, which the install Case of `rule-morph` replaces in a later session (Case 822.4). The Criterion of `estimate-claude-md-rendered` quotes `CLAUDE.md` as one paragraph after `# GUPPI`, which the marker lines make false, so Case 822.5 replaces it. `.github/workflows/checks.yml` ships, and no other file of `.github/` (Case 822.6). `entity-guppi`, `rule-language` and `rule-case-build` lose the sentences that hold only here, and a reading of the copy looks for the rest of the shipped text, since the person chose that the rest is found by a check and rewritten by a later Case (Case 822.7). For the rules, the entities and `CLAUDE.md` the reading passes only when it finds no such sentence. For the `purpose`, `method` and Criterion of each shipped Estimate, it lists each such sentence for a later Case, and the list does not fail it, as the person chose at `/pre-spec`: Case 822.1 ships Estimates such as `estimate-guppi-config-fills-the-languages`, whose `method` names English and Russian as the languages of `CLAUDE.md`. `rule-guppi-config` ships with the values of this repository, as the person chose at `/pre-spec`, so its Render stays out of that reading. `render --sync` at the first `/hi` writes `guppi.toml` from it until the install Case, as Case 817 says. Then the person set a rule: a page with `core: true` may not be `draft`. While one stands, `guppi ship` writes nothing and exits 1 (Case 822.8), and `guppi lint` reports it where the module of `ship` stands (Case 822.9), both by one function. An option `--allow-draft` writes a local copy for an install by hand and lists those pages, and the workflow that writes `prod` never passes it. At `/pre-spec` the person chose that every Estimate that waits for a run that writes `prod` is read from such a local copy, so a page can become `built` before `prod` is written. The lint finding is of the class `status`, so the Criterion of `estimate-lint-checks-the-statuses`, which says that a page without Estimates is not judged, is replaced (Case 822.9). A Grep `^status: draft` over `vault/wiki/` printed `entity-sprint-plugin`, `rule-work-mode`, `rule-skill-hi`, `entity-sprint`, `entity-guppi-repository`, `rule-github-repository`, `rule-skill-pr-review`, `rule-skill-merge-main` and `rule-morph`; six of them carry `core: true`. Case 822.8 takes `core` off `rule-skill-merge-main` and `rule-skill-pr-review`, each to come back by a Case once it is `built`. `rule-morph` keeps `core`, as the person chose at `/pre-spec`, since its Estimate reads the install step in a copy that a page without `core` never reaches. `entity-sprint` carries no Estimate, so the cascade never builds it; the person did not name what its Estimate checks, so a Case of a later session gives it one. Besides those, the librarian's run that applies this Spec sets `draft` each page with `core: true` whose Estimate a Case of this session creates or sets `pending`, among them `rule-guppi-package`, `rule-guppi-config`, `rule-page-generation`, `rule-lint` and `rule-claude-md`. So `guppi ship <folder>` exits 1 and `guppi lint` prints one line for each such page here until its reading passes, a red signal by `rule-lint`. A Grep `merge-main|pr-review|rule-morph` over `.claude/` printed `.claude/skills/sprint-close/SKILL.md`, `.claude/skills/sprint-open/SKILL.md`, `.claude/skills/merge-main/SKILL.md`, `.claude/skills/pr-review/SKILL.md` and `.claude/agents/librarian-guppi.md`. The shipped skills and the librarian name `/merge-main` and `/pr-review`, which the copy no longer holds until those pages come back; that stands as the cost the person took. `vault/raw/` and `vault/archive/` do not ship: the hooks create the raw folder of a day, and `archived_slugs` of `guppi/lint.py` takes a missing archive as empty. A Grep `^core: true` over `vault/wiki/` printed 85 files. A Grep `^target: "\[\[(rule-clean-branch|rule-github-repository|entity-guppi-repository|entity-sprint-plugin)\]\]"` over `vault/wiki/estimates/` printed 8 files, the Estimates whose target does not ship. A Grep `is_core|SHIPPED` over `guppi/` printed `guppi/ship.py`, `guppi/prespec.py`, `guppi/lint.py` and `guppi/pages.py`. `is_core` of `guppi/pages.py` is the one judgment of the field, and lint accepts `origin: guppi` only on a page it accepts, which is why the copy of an Estimate carries `core: true`. A Grep `"draft"|find_spec|guppi\.ship` over `guppi/` printed `guppi/prespec.py`, `guppi/generate.py` and `guppi/lint.py`; no code judges a draft page with `core`, so the new function adds no second copy. Case 820 judges whether the module of `ship` stands in `guppi check` and in the list of commands. The one function of that judgment is `ship_stands` of `.guppi/guppi/pages.py`, which `check.py`, `cli.py` and `lint.py` import, beside `is_draft_core`, the one judgment of a draft page with `core: true`. The case file of Case 820 in this folder already names `ship_stands` of `.guppi/guppi/pages.py` in its tasks, so Case 820 needs no change. `/pre-spec` judges new text only on a page that carries `core: true`, which no Estimate here does; a pointer in the new Criterion of a shipped Estimate is then found by the build, as the person chose. A Grep `this repository|the repository of GUPPI|kirMykholap|this project` over `vault/wiki/rules/` printed `schema.yaml`, `rule-clean-branch.md`, `rule-rules-schema.md`, `rule-permissions.md`, `rule-language.md`, `rule-estimates-schema.md`, `rule-entities-schema.md`, `rule-where-to-stop.md`, `rule-github-repository.md` and `rule-morph.md`, and over `vault/wiki/entities/` printed `schema.yaml`, `entity-guppi-repository.md` and `entity-guppi.md`. `rule-clean-branch`, `rule-github-repository` and `entity-guppi-repository` do not ship. `rule-morph` ships once `built`, in the text that Case 817 writes whole; the reading of Case 822.7 lists what of it holds only here. The sentences of `rule-where-to-stop` and `rule-permissions` hold in any project, since there this repository is that project. The field `core` of the rules and the entities schemas says that a page without it stays in this repository, which holds in a project that builds no clean version; the field of the estimates schema changes in Case 822.1. A Grep `Russian` over `vault/wiki/` printed 15 files: `orchestration.md`, `case-schema.md`, `log.md`, `tags.md`, `rule-language.md`, `rule-claude-md.md`, `rule-case-protocol.md`, `rule-case-build.md` and seven Estimates. `orchestration.md` takes the name from the render of `{{chat_lang}}`. The hits in `rule-case-protocol.md` and `rule-claude-md.md` stand in History. The alias column of `tags.md` and of `case-schema.md` sets a form, the Russian aliases of a tag, which is a behaviour and no neutral wording; the reading of Case 822.7 lists it for a later Case. A Grep `CLAUDE\.md|rule-claude-md|entity-guppi\b|rule-language|checks\.yml|estimates/schema|rule-case-build` over `tests/` printed `test_ship.py`, `test_prespec.py`, `test_generate.py`, `test_materialize.py`, `test_render.py`, `test_glossary.py` and `test_guard.py`; each hit is a comment, a string or a file written under a temporary folder. `test_schemas.py` reads the lists of the live `schema.yaml`, and `core: [true]` stays in the values of the estimates schema. At the last close the brief reports `make test`: 1620 passed, 6 skipped, and `make lint`: 0 lines, exit 0. Under Case 822.2 `guppi ship --check` judges the comments of the tests, so it prints lines until the Work Mode moves each pointer of a comment into a bracket, which its task does. `estimate-clean-branch-code-holds-pointers-only-in-brackets` stands, since its Criterion names the code, the `Makefile` and the root files, not the tests. `estimate-clean-branch-pages-hold-pointers-only-in-brackets` stands, since it speaks of the pages with `core: true`, and no Estimate here carries the field; a later reading of either builds with `--allow-draft` while a draft page with `core` stands. The readings of Cases 822.2, 822.3 and 822.7 wait for the librarian's run of this change, since the texts, the rendered skill of the plugin and the renamed commands land there. The case files of Cases 816, 818 and 819 in this folder were built again after Case 821, and they were read for this build. Case 816.1 builds with `--allow-draft`, and Case 816.2 says that a sample is no reference and names the guard of Case 822.8 under its old number. Cases 816.2 and 818.1 read the install from a local copy that `guppi ship --allow-draft` writes, and Case 819.3 drops its lines on the tests, `.github/` and the session files. Those Cases name the sub-cases of Case 821, which this Case keeps under the same promises and slugs. The `method` of `estimate-guppi-package-is-ready-after-the-install` of Case 819.4 already reads an install from a local copy that `guppi ship --allow-draft` writes, so Case 819 needs no change; the case files of Cases 816 and 819 were read whole for this build. In the sentence of Case 820.5 that the pair of Case 822.4 keeps, the path `.guppi/guppi/ship.py` stands after a `.`, so the `reword` pair `guppi/` of Case 819.1, under the matching of Case 819.2, leaves it as written, and that `reword` comes before Case 820.5 in the ledger in any case. Case 817 needs no change. The Criterion of `estimate-claude-md-rendered` is carried line by line but its first `Then` line, which now quotes the marker lines and two paragraphs. The Criterion of `estimate-lint-checks-the-statuses` is carried line by line too, with three changes: its `When` names the command in the form that the `reword` of Case 819.1 gives it, its first `Then` line says that a page without Estimates is not judged for those two findings, and a line on a draft page with `core: true` is added. The pairs on `rule-clean-branch` were read side by side with the new texts of Cases 816.1, 816.2, 818.1, 819.1, 819.3, 820.5 and 820.7, which change the same paragraphs. Each pair of this Case anchors on words that one of those Cases writes or leaves alone, keeps those words, and adds a sentence after them, or before them in Case 822.3. The pairs come after those Cases in the ledger, so each `old` hits the page once. The Purpose of `rule-clean-branch` was read whole for this build, and so were the pairs on it in the case files of Cases 816, 818, 819 and 820 of this folder. In Case 822.1 the pair adds a sentence after the last sentence of Case 816.1, which ends with the words `which the clean version does not hold (case 816).`. In Case 822.2 the pair changes the words `but not its tests` of the list that Case 819.3 writes, and Case 819.1 changes only the paths of that list by its `reword`, which comes first. In Case 822.4 the pair adds its sentence after the live sentence `It writes any other [[…]] link to a page or a file it does not write as the slug in a code span.` of the second paragraph, which it keeps word for word. No pair of Cases 816, 818, 819, 820 and 821 in their case files of this folder, read whole for this build, writes into that sentence: the pairs of Cases 819.1 and 820.7 rename paths and commands it does not hold, and Cases 821.2 and 822.2 add their sentences before it, after the words `and it judges no code outside them.`. In Case 822.8 the pair adds a sentence after the sentence of Case 816.2 on the version of the plugin. For this build the sub-cases 819.1 to 819.3, 818.1 and 820.5 were read again in their case files of this folder. The `reword` of Case 819.1 applies before the texts of Cases 819.3, 820.5 and this Case are written, so it changes none of the words these pairs anchor on. Case 819.3 now writes `.guppi/` with the words `but not its tests`, which Case 822.2 changes, and its Criterion points to the Estimates of this Case for the tests. In Case 822.3 the pair anchors on the words `It gives each page`, which close the new text of Case 818.1; Case 816.1 adds its sentences after the words `the pages it writes.` of the same sentence, so neither pair touches the words of the other. The pair on `rule-lint` anchors on the end of the sentence that names `parent: rule-harness`, which the live Purpose and the Purpose that Case 820.1 writes both hold whole; the new sentence reads true beside the sentence of Case 820.1 on the six steps of `guppi check`. The pair on `rule-plugin-install` anchors on the Purpose that Case 819.4 writes. `entity-guppi` carries `deferred_by` from `decision-case-616`, which puts off the future shape of GUPPI; this Case does not take that question up, and the defer stays.

> **problem:**
> A project that installs GUPPI gets its rules without their Estimates, no tests, none of the files that its first `/hi` loads, no CI, and texts that describe GUPPI's own repository as its project, and nothing stops a build of `prod` that holds a rule that is not done.

> **recommend:**
> - **How the copy knows that an Estimate ships**
>   - Recommended: (a) judged from the target: `guppi ship` takes each Estimate whose target ships and writes `core: true` into its copy.
>   - Answer: agreed, (a).
> - **Which Estimates ship, by their status**
>   - Recommended: (a) only those with a result, `passed` and `failed`.
>   - Answer: only `passed` Estimates ship; a `failed` one may not ship, nor a `pending` one.
> - **What a shipped Estimate says where it names a case or a session**
>   - Recommended: (a) one line in place of the Result; a pointer left outside a bracket stops the build and a later Case moves it.
>   - Answer: agreed, (a).
> - **What happens to the case numbers in the tests**
>   - Recommended: (b) comments and docstrings cleaned, strings kept as samples.
>   - Answer: agreed, (b).
> - **What the skeletons hold, and whether the first /hi opens a sprint**
>   - Recommended: (a) skeletons that lead to a new sprint, each as its own writer writes it over the copy.
>   - Answer: agreed, (a).
> - **How CLAUDE.md gets the project's own description**
>   - Recommended: (a) a marked block that the copy swaps.
>   - Answer: agreed, (a).
> - **How far the neutral rewrite goes in this Case**
>   - Recommended: (a) the pages a search finds now, the rest after a check.
>   - Answer: agreed, (a).
> - **What checks that this is done**
>   - Recommended: (a) new Estimates for each part, and the other Case drops its lines that this Case makes false.
>   - Answer: agreed, (a).
> - **What a draft rule takes into the copy**
>   - Recommended: (a) a draft rule ships with no Estimate.
>   - Answer: none of the options: a page with `core: true` may not be `draft`; a check must catch it, and the fix is to take `core` off, so the page does not ship, or to bring the page to `built`. Replaced by the question on where the guard sits.
> - **Where the guard against a draft core page sits, and what happens to the six drafts now**
>   - Recommended: (a) lint now, the build later.
>   - Answer: `guppi ship` refuses to build `prod` while such a page stands, and `guppi lint` reminds of it too; the six are settled by the question on how they are settled.
> - **Where lint reports a draft core page**
>   - Recommended: (a) only where the command `ship` stands.
>   - Answer: agreed, (a).
> - **How the six drafts are settled, and what the sprint reads before the close**
>   - Recommended: (b) `core` off `rule-skill-merge-main`, `rule-skill-pr-review` and `rule-morph`, a Case gives `entity-sprint` an Estimate, and an option of `guppi ship` writes a local copy for the sprint's install check before the close.
>   - Answer: agreed, (b).
> - **Change**
>   - Asked: at `/pre-spec`, every Estimate that waits for a run that writes `prod` is read from a local copy that `guppi ship --allow-draft` writes, and `rule-morph` keeps `core: true`, while `rule-skill-merge-main` and `rule-skill-pr-review` still lose it.
>   - Taken: Case 822.8 takes `core` off two pages and not `rule-morph`; Cases 816, 818 and 819 already read the local copy; the Case is built again under a new number.
> - **Change**
>   - Asked: at `/pre-spec`, `rule-guppi-config` ships with the values of this repository.
>   - Taken: the reading of Case 822.7 leaves the Render of `rule-guppi-config` out.
> - **Change**
>   - Asked: at `/pre-spec`, for now the copy does not ship a `passed` Estimate whose `method` names a `make` target, until a later Case moves it to pytest.
>   - Taken: Case 822.1 leaves such an Estimate out, judged by `MAKE_TARGET` of `guppi/lint.py`.
> - **Change**
>   - Asked: the findings of `/pre-spec`: a pointer outside a bracket in the pair on `rule-language`, the scope of the neutral reading, the Criteria of `estimate-lint-checks-the-statuses` and `estimate-claude-md-rendered`, the defer of `decision-case-805`, the count of the draft pages, the name of the function that tells whether the module of `ship` stands, and the moment of three readings.
>   - Taken: the pair on `rule-language` takes the bracket whole; the reading of Case 822.7 holds the rules, the entities and `CLAUDE.md` to no sentence that holds only here, and for the shipped Estimates it lists such sentences for a later Case and passes when the list is made; the reading covers each shipped text but History and samples; Cases 822.5 and 822.9 replace the two Criteria; Case 822.1 takes up the defer; the context names the draft pages by kind; `ship_stands` of `.guppi/guppi/pages.py` is named; the three readings wait for the librarian's run.

### Case 822.1 — The clean version holds each passed Estimate of a page it ships

> **given:**
> `rule-clean-branch`: the rule of `guppi ship`.
> **＋** `estimate-clean-branch-ships-the-passed-estimates`: the new check of the Estimates in the clean version.
> **＋** `rule-estimates-schema` and `vault/wiki/estimates/schema.yaml`: the schema of an Estimate, whose field `core` changes, and its Render.
> **＋** `entity-sprint-plugin` and `decision-case-805`: the sprint page, and the defer on it of whether the Estimates ship with the tests.
> **＋** `.guppi/guppi/ship.py`, `.guppi/guppi/pages.py` and `.guppi/guppi/lint.py`: the code of the copy, the judgment of `core`, and lint, which holds `MAKE_TARGET` and reads `origin: guppi`.
> **＋** `Makefile`: the file of make targets, which the clean version does not hold.
> **＋** `.guppi/tests/test_ship.py`: the tests of `guppi ship`.

> **when:**
> `uv run --project .guppi guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.

> **then:**
> It writes each Estimate whose status is `passed` and whose target is a page it writes, with `core: true`, `origin: guppi`, `sprint: guppi` and a `## History` of one line.
> **＋** The `## Result` of each Estimate it writes is one line: the date of its `checked` and that it passed in the repository of GUPPI.
> **＋** Each Estimate it writes keeps its `status`, `checked`, `purpose`, `method` and `## Criterion`, cleaned as the text of each page it writes.
> **＋** The field `estimates` of each page it writes lists the Estimates it writes and no other.
> **＋** `uv run --project .guppi guppi lint` over the clean version gives no finding on the `origin` or the `core` of an Estimate it writes.
> **－** It writes no Estimate that is `pending` or `failed`, none whose target page it does not write, and none whose `method` names a target of the `Makefile`, by `MAKE_TARGET` of `.guppi/guppi/lint.py`.
> **－** No Estimate of the project it builds from carries `core`.
> **－** A pointer outside a bracket in the `## Criterion`, the `purpose` or the `method` of an Estimate it writes makes it exit 1, as a pointer in any page does.

```then
create:
- slug: estimate-clean-branch-ships-the-passed-estimates
  ref: rule-clean-branch
  kind: QA
  purpose: 'Whether guppi ship writes each passed Estimate of a page it writes, with core: true and a Result of one line, and no Estimate that is pending or failed, whose target it does not write, or whose method names a make target'
  method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k estimate
  tags:
  - ci
  - plugin
update:
- slug: rule-clean-branch
  replace:
  - old: which the clean version does not hold (case 816).
    new: 'which the clean version does not hold (case 816). It also writes each `passed` Estimate whose target page it writes, with `core: true` written into its copy and a `## Result` of one line, the date of its last reading and that it passed in the repository of GUPPI; no Estimate of this repository carries `core`, an Estimate that is `pending` or `failed` stays here until its reading passes, and one whose `method` names a target of the `Makefile` stays here until a Case moves it to pytest (case 822).'
  change: 'guppi ship writes each passed Estimate of a page it writes, with core: true and a Result of one line, but one whose method names a make target'
- slug: rule-estimates-schema
  replace:
  - old: optional; `true`. The page ships in the clean version of GUPPI that `guppi ship` writes for the branch `prod`; a page without it stays in this repository only. Set by a Case, never by hand (case 804).
    new: 'optional; `true`. It stands only in the clean version of GUPPI that `guppi ship` writes: `guppi ship` writes it into the copy of each `passed` Estimate whose target page carries `core: true` and whose `method` names no `make` target, and lint reads it there; no Estimate of the repository that builds that version carries it (cases 804, 822).'
  change: the field core of an Estimate is written by guppi ship into the copy of each passed Estimate of a shipped page
- slug: entity-sprint-plugin
  change: 'the question put off by decision-case-805 is decided by case 822: the passed Estimates of the shipped pages ship, and the tests ship'
```

```tasks
- [x] update `rule-clean-branch`
- [x] update `rule-estimates-schema`
- [x] update `entity-sprint-plugin`
- [x] create `estimate-clean-branch-ships-the-passed-estimates`
- [x] `.guppi/guppi/ship.py`: `plan` takes each Estimate whose `status` is `passed`, whose target, read by `slug_of` of `.guppi/guppi/pages.py`, is a page with `core: true` that it writes, and whose `method` holds no match of `MAKE_TARGET` of `.guppi/guppi/lint.py`, imported; `shipped_page` writes `core: true` into such an Estimate and its `## Result` as one line, the date of `checked` and that it passed in the repository of GUPPI; the docstring says so.
- [x] `.guppi/tests/test_ship.py`: the sample tree holds a `passed`, a `pending` and a `failed` Estimate of a page with `core: true`, a `passed` one whose `method` names `make test-x`, and a `passed` Estimate of a page without it; the copy holds the first alone, with `core: true`, `origin: guppi` and a Result of one line, and the `estimates` of its target list it alone; `guppi lint` over the copy gives no finding on its `origin`; the names of these tests hold `estimate`.
- [x] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`
- [x] read `estimate-clean-branch-ships-the-passed-estimates`
```

### Case 822.2 — The clean version holds the tests with their sample data

> **given:**
> `rule-clean-branch`: the rule of `guppi ship`.
> **＋** `estimate-clean-branch-ships-the-tests`: the new check of the tests in the clean version.
> **＋** `.guppi/tests/` and `.guppi/tests/test_ship.py`: the tests of GUPPI, and the tests of the command `ship`.
> **＋** `.guppi/.venv/`: the Python environment that the clean version does not hold.
> **＋** `uv run --project .guppi pytest .guppi/tests`: the run of the tests.
> **＋** `.guppi/guppi/ship.py` and `.guppi/guppi/pointers.py`: the copy, and the one judgment of a pointer and of a sample.

> **when:**
> `uv run --project .guppi guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.
> **＋** Or `uv run --project .guppi guppi ship --check` judges the working tree and writes no folder.
> **＋** Then `uv run --project .guppi pytest .guppi/tests` runs in that folder.

> **then:**
> It writes each file under `.guppi/tests/` but `.guppi/tests/test_ship.py`.
> **＋** In a Python file under `.guppi/tests/`, it removes a bracket that holds a pointer only from the comments and the docstrings, and it judges only them for a pointer outside a bracket and for a bare case number.
> **＋** Each other string of such a file is a sample: a case id there, such as `[case 10]` or `(case 320)` in the data of a test, is neither removed nor judged.
> **＋** `--check` judges each file under `.guppi/tests/` in place, in the same way.
> **＋** In the clean version, `uv run --project .guppi pytest .guppi/tests` passes, and a test that needs a file or a module that the clean version does not hold is skipped.
> **－** The Python environment `.guppi/.venv/` stays out of the copy.
> **－** In a Python file outside `.guppi/tests/`, it judges the whole text as before.

```then
create:
- slug: estimate-clean-branch-ships-the-tests
  ref: rule-clean-branch
  kind: QA
  purpose: Whether guppi ship writes the tests but those of the command ship, cleans and judges only their comments and docstrings, keeps their other strings as samples, and whether the tests pass in the clean version
  method: 'uv run --project .guppi pytest .guppi/tests/test_ship.py -k tests; by hand, after the librarian''s run of this change: uv run --project .guppi guppi ship --allow-draft into an empty temporary folder, then uv run --project .guppi pytest .guppi/tests in that folder, read against the Criterion'
  tags:
  - plugin
  - tests
update:
- slug: rule-clean-branch
  replace:
  - old: but not its tests `.guppi/tests/` or its Python environment `.guppi/.venv/`;
    new: with its tests `.guppi/tests/` but `.guppi/tests/test_ship.py`, the tests of the command `ship`, and not its Python environment `.guppi/.venv/`;
  - old: and it judges no code outside them.
    new: 'and it judges no code outside them. In a test file under `.guppi/tests/` it cleans and judges only the comments and the docstrings: each other string is a sample, as a code span of a page is, so a case id in the data of a test is neither removed nor judged (case 822).'
  change: guppi ship writes the tests but those of ship, and in a test file it cleans and judges only the comments and the docstrings
```

```tasks
- [x] update `rule-clean-branch`
- [x] create `estimate-clean-branch-ships-the-tests`
- [x] `.guppi/guppi/pointers.py`: beside `masked`, one function sets aside as samples the strings of a Python file that are not docstrings, read by `tokenize`; `outside` and the cleaning take it for a file under `.guppi/tests/`; the docstring says so.
- [x] `.guppi/guppi/ship.py`: the copy and `--check` take the files under `.guppi/tests/` but `.guppi/tests/test_ship.py`, and judge and clean them through that function; the docstring says so.
- [x] `.guppi/tests/`: each pointer outside a bracket in a comment or a docstring stands in a bracket of its own at the end of its sentence, and each bare case number there gets the word `case`, so that `guppi ship --check` prints no line on them; a test that needs the `Makefile`, `.github/workflows/prod.yml` or the module `guppi.ship` is skipped where it is missing.
- [x] `.guppi/tests/test_ship.py`: the sample tree holds a test file with a pointer in a bracket in a comment, a sample ledger line and a bracket with a pointer in a string, and a file `.guppi/tests/test_ship.py`; the copy holds the first without the bracket of the comment and with both strings unchanged, and no `.guppi/tests/test_ship.py`; `--check` prints a line for a pointer outside a bracket in a comment of a test and none for one in a string; the names of these tests hold `tests`.
- [ ] read `estimate-clean-branch-ships-the-tests`
```

### Case 822.3 — The clean version holds the session files as skeletons

> **given:**
> `rule-clean-branch`: the rule of `guppi ship`.
> **＋** `estimate-clean-branch-writes-the-session-files`: the new check of the skeletons.
> **＋** `vault/wiki/sprint.md`, `vault/wiki/backlog.md`, `vault/wiki/brief.md`, `vault/wiki/glossary.md` and `vault/wiki/log.md`: the files that `/hi` loads or that the hooks append to.
> **＋** `.guppi/guppi/ship.py`, `.guppi/guppi/sprint.py`, `.guppi/guppi/backlog.py` and `.guppi/guppi/glossary.py`: the copy, and the writers of `sprint.md`, `backlog.md` and `glossary.md`.
> **＋** `rule-plugin-install` and `/guppi:install`: the rule and the skill that copy GUPPI into a project.
> **＋** `/hi` and `/sprint-open`: the skills that open a session and a sprint.
> **＋** `.guppi/tests/test_ship.py`: the tests of `guppi ship`.

> **when:**
> `uv run --project .guppi guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.
> **＋** Or, in an empty project, the person installs the plugin `guppi` from such a copy, types `/guppi:install`, reopens Claude Code there and types `/hi`.

> **then:**
> It writes `vault/wiki/sprint.md` as `closed_form` of `.guppi/guppi/sprint.py` writes it for the sprint `guppi`, so its first `## ` heading carries the mark of a closed sprint.
> **＋** It writes `vault/wiki/backlog.md` and `vault/wiki/glossary.md` as `guppi backlog` and `guppi glossary` write them over the clean version, by their own code.
> **＋** It writes a `vault/wiki/brief.md` whose `Cases` of its `## Next session` open with the line `open the next sprint — no sprint is open since the close of guppi`, and a `vault/wiki/log.md` that holds its heading and the paragraph under it alone.
> **＋** Over the clean version, `guppi sprint --check`, `guppi backlog --check` and `guppi glossary --check` print nothing and exit 0.
> **＋** In that project, the first `/hi` starts `/sprint-open` before the Frontier.
> **－** It writes no `sprint.md`, `backlog.md`, `brief.md`, `glossary.md` or `log.md` of the project it builds from.

```then
create:
- slug: estimate-clean-branch-writes-the-session-files
  ref: rule-clean-branch
  kind: QA
  purpose: Whether guppi ship writes sprint.md in the closed form of the sprint guppi, backlog.md and glossary.md by their writers, a brief.md that opens the next sprint and a log.md with its heading alone, so that the checks of those files pass and the first /hi of a new project starts /sprint-open
  method: 'uv run --project .guppi pytest .guppi/tests/test_ship.py -k skeleton; by hand, after the librarian''s run of this change: in an empty project, guppi installed from a copy that uv run --project .guppi guppi ship --allow-draft wrote into a local folder, /guppi:install typed, Claude Code reopened and /hi typed, read against the Criterion'
  tags:
  - plugin
  - ci
update:
- slug: rule-clean-branch
  replace:
  - old: 'It gives each page `origin: guppi`, `sprint: guppi`,'
    new: 'In place of the session files of this project it writes skeletons, so the first `/hi` of a project that installs GUPPI finds each file it loads: `vault/wiki/sprint.md` in the closed form of the sprint `guppi`, so that `/hi` starts `/sprint-open`; `vault/wiki/backlog.md` and `vault/wiki/glossary.md` as `guppi backlog` and `guppi glossary` write them over the clean version; a `vault/wiki/brief.md` whose Next session opens its Cases with the line that opens the next sprint; and a `vault/wiki/log.md` that holds its heading alone (case 822). It gives each page `origin: guppi`, `sprint: guppi`,'
  change: guppi ship writes sprint.md, backlog.md, brief.md, glossary.md and log.md as skeletons
- slug: rule-plugin-install
  replace:
  - old: Which files a new project gets waits for a Case of its own.
    new: 'What a new project gets beside the pages with `core: true` — the tests, the session files as skeletons and the CI of its checks — is set in [[rule-clean-branch]] (case 822).'
  change: what a new project gets is set in rule-clean-branch
```

```tasks
- [x] update `rule-clean-branch`
- [x] update `rule-plugin-install`
- [x] create `estimate-clean-branch-writes-the-session-files`
- [x] `.guppi/guppi/ship.py`: the copy writes `vault/wiki/sprint.md` by `closed_form` of `.guppi/guppi/sprint.py` for `guppi`, `vault/wiki/backlog.md` and `vault/wiki/glossary.md` by `render` of `.guppi/guppi/backlog.py` and of `.guppi/guppi/glossary.py` over the clean folder, and `vault/wiki/brief.md` and `vault/wiki/log.md` from two fixed texts in this module; no copy of a judgment of those writers stands here; the docstring says so.
- [x] `.guppi/tests/test_ship.py`: the copy of the sample tree holds the five files; `sprint.md` equals `closed_form("guppi")`; `guppi sprint --check`, `guppi backlog --check` and `guppi glossary --check` over the copy print nothing and exit 0; `brief.md` opens its Cases with the line of the next sprint; the names of these tests hold `skeleton`.
- [ ] read `estimate-clean-branch-writes-the-session-files`
```

### Case 822.5 — CLAUDE.md holds the description of the project between marker lines

> **given:**
> `rule-claude-md` and `CLAUDE.md`: the page whose Render is `CLAUDE.md`, and the file.
> **＋** `<!-- project-description -->` and `<!-- /project-description -->`: the marker lines of the description of the project.
> **＋** `estimate-claude-md-rendered`: its Criterion is replaced whole.
> **＋** `rule-language`, `rule-agent-writing`, `rule-one-judgment-one-implementation` and `rule-governed-files-hook`: the children of `rule-claude-md`, and the hook that refuses a hand edit.
> **＋** `vault/wiki/ratification.md`: the file that holds the one rule.

> **when:**
> `guppi render` writes `CLAUDE.md` from `rule-claude-md` and its children, and a session or a subagent starts and loads the file.

> **then:**
> `CLAUDE.md` is: the line `<!-- project-description -->`; `# GUPPI`; the paragraph "A Claude Code harness governed by ratified decisions, and the Obsidian vault it compiles into."; the line `<!-- /project-description -->`; the paragraph "The vault is vault/; its terms are vault/wiki/glossary.md. A working session opens with /hi.", whose words the file holds with the folder, the path and the skill in code spans; then the text of `rule-language`, `rule-agent-writing` and `rule-one-judgment-one-implementation` in their markers.
> **＋** `render --check` after the render exits 0, and the hook of `rule-governed-files-hook` refuses a hand edit of the file.
> **＋** Every session and every subagent loads this text.
> **－** No `@` import, no "What is loaded here", no paragraph on `index.md`, no "Migration mode", no "Commands", no one rule and no sentence on memory — the one rule is in `vault/wiki/ratification.md`; the `children` of `rule-claude-md` are `rule-language`, `rule-agent-writing` and `rule-one-judgment-one-implementation`.

```then
update:
- slug: rule-claude-md
  replace:
  - old: (cases 272, 273.3, 288.3, 595).
    new: '(cases 272, 273.3, 288.3, 595). The heading and the description of the project stand between the lines `<!-- project-description -->` and `<!-- /project-description -->`: in the clean version of GUPPI a heading and a line that says the description is not set yet stand there, until the install Case of a project writes its own description (case 822).'
  sections:
    Render: |-
      <!-- rule-claude-md -->
      <!-- project-description -->
      # GUPPI

      A Claude Code harness governed by ratified decisions, and the Obsidian vault it compiles into.
      <!-- /project-description -->

      The vault is `vault/`; its terms are `vault/wiki/glossary.md`. A working session opens with `/hi`.

      <!-- rule-language -->

      <!-- rule-agent-writing -->

      <!-- rule-one-judgment-one-implementation -->
      <!-- /rule-claude-md -->
  change: the heading and the description of the project stand between marker lines of their own
- slug: estimate-claude-md-rendered
  set:
    status: pending
    method: 'by hand, after the librarian''s run of this change: uv run --project .guppi guppi render --check, and CLAUDE.md as the file holds it and as the session of that run loads it, read against the Criterion'
  change: the Criterion replaced whole — the heading and the description stand between marker lines of their own
```

```tasks
- [x] update `rule-claude-md`
- [x] update `estimate-claude-md-rendered`
- [x] `uv run guppi render`: `CLAUDE.md`
- [ ] read `estimate-claude-md-rendered`
```

### Case 822.6 — The clean version holds the CI of the checks

> **given:**
> `rule-clean-branch`: the rule of `guppi ship` and of the workflow that writes `prod`.
> **＋** `estimate-clean-branch-ships-the-checks-workflow`: the new check of the CI in the clean version.
> **＋** `.github/`, `.github/workflows/checks.yml` and `.github/workflows/prod.yml`: the CI of the checks, and the workflow that writes `prod`.
> **＋** `vault/raw/2026-10-15/0553/cases/case-820.md`: the Case of this session that makes the jobs of `.github/workflows/checks.yml` run `guppi test`, `guppi check` and `guppi style`.
> **＋** `.guppi/guppi/ship.py` and `.guppi/tests/test_ship.py`: the copy and its tests.

> **when:**
> `uv run --project .guppi guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.
> **＋** Or `uv run --project .guppi guppi ship --check` judges the working tree and writes no folder.

> **then:**
> It writes `.github/workflows/checks.yml`, judged and cleaned like each other file it writes.
> **＋** `--check` judges `.github/workflows/checks.yml` in place.
> **＋** The comment of `.github/workflows/checks.yml` names no page that the clean version does not hold.
> **－** It writes no other file of `.github/`, `.github/workflows/prod.yml` included.

```then
create:
- slug: estimate-clean-branch-ships-the-checks-workflow
  ref: rule-clean-branch
  kind: QA
  purpose: Whether guppi ship writes .github/workflows/checks.yml, judged and cleaned, and no other file of .github/, and whether --check judges it in place
  method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k checks_workflow
  tags:
  - ci
  - plugin
update:
- slug: rule-clean-branch
  replace:
  - old: neither carries `core`, and `.github/` is not part of the clean version (case 804).
    new: neither carries `core`. Of `.github/` the clean version holds only `.github/workflows/checks.yml`, the CI that runs the tests, the vault checks and the style check of a project, judged and cleaned like each other file it writes, and `guppi ship --check` judges it in place (cases 804, 822).
  change: the clean version holds .github/workflows/checks.yml and no other file of .github/
```

```tasks
- [x] update `rule-clean-branch`
- [x] create `estimate-clean-branch-ships-the-checks-workflow`
- [x] `.guppi/guppi/ship.py`: the copy and `--check` take `.github/workflows/checks.yml` and no other file of `.github/`; the docstring says so.
- [x] `.github/workflows/checks.yml`: the comment at the top names no page that the clean version does not hold, such as `rule-github-repository`, and no `Makefile`.
- [x] `.guppi/tests/test_ship.py`: the sample tree holds `.github/workflows/checks.yml` with a pointer in a bracket of its comment and `.github/workflows/prod.yml`; the copy holds the first without the bracket and not the second; `--check` prints a line for a pointer outside a bracket in it; the names of these tests hold `checks_workflow`.
- [x] read `estimate-clean-branch-ships-the-checks-workflow`
```

### Case 822.7 — The shipped texts hold in any project

> **given:**
> `entity-guppi`: the page of GUPPI as a whole.
> **＋** `rule-language` and `rule-case-build`: shipped pages whose Purpose names the languages of this repository.
> **＋** `entity-guppi-repository`: the page of the repository of GUPPI on GitHub, which does not ship.
> **＋** `rule-guppi-config`: the page of the settings, whose Render ships with the values of this repository.
> **＋** `estimate-clean-branch-ships-neutral-texts`: the new reading of the texts of the clean version.
> **＋** `rule-clean-branch`: the rule of `guppi ship`, the target of that reading.

> **when:**
> Someone reads the pages and the files of the clean version that `uv run --project .guppi guppi ship --allow-draft <folder>`, as `rule-clean-branch` sets it, writes into an empty folder.

> **then:**
> `entity-guppi` describes GUPPI as a harness and a vault, and not as the thing that the project builds.
> **＋** `rule-language` and `rule-case-build` name the language of the repository and the language of the chat by their role, not as English and Russian.
> **＋** No other sentence of the rules, the entities and `CLAUDE.md` of the clean version holds only in the repository of GUPPI, such as one that takes its repository on GitHub or its languages for those of the project.
> **＋** The reader lists, in the estimate line, each sentence of the `purpose`, the `method` and the `## Criterion` of each shipped Estimate that holds only in the repository of GUPPI, for a Case of a later session to rewrite.
> **－** A sentence of a shipped Estimate on that list does not fail this promise.
> **－** The History of a page, a sample in a code span or a fenced block, and the values of the Render of `rule-guppi-config` are no part of this promise.

```then
create:
- slug: estimate-clean-branch-ships-neutral-texts
  ref: rule-clean-branch
  kind: QA
  purpose: Whether the rules, the entities and CLAUDE.md of the clean version describe GUPPI and the languages in words that hold in any project and hold no other sentence true only in the repository of GUPPI, and which sentences of the shipped Estimates hold only there
  method: 'by hand, after the librarian''s run of this change: uv run --project .guppi guppi ship --allow-draft into an empty temporary folder, and the pages and the files it wrote read against the Criterion, each sentence that holds only in the repository of GUPPI listed in the estimate line'
  tags:
  - plugin
  - ci
update:
- slug: entity-guppi
  set:
    purpose: GUPPI — a Claude Code harness governed by ratified decisions, and the vault it keeps; its parts the sprint and the glossary, and in the repository of GUPPI also that repository on GitHub
  sections:
    Purpose: 'GUPPI: a Claude Code harness governed by ratified decisions, and the Obsidian vault it compiles into. Its parts are the sprint as a kind (`entity-sprint`) and the glossary (`entity-glossary`), the things of the vault that are content, not rules. In the repository of GUPPI itself, a third part is that repository on GitHub, `entity-guppi-repository`, whose rules are its own; the clean version of GUPPI does not hold that page (as set in case 795.1). `rule-harness` is its guard: the tools of the harness kept equal to the pages that describe them. In a project that uses GUPPI, this page stands beside the root of the product and keeps GUPPI''s own machinery apart from it (as set in case 306.2).'
  change: GUPPI is described as a harness and a vault, true in any project that uses it
- slug: rule-language
  replace:
  - old: rendered into `guppi.toml` — English and Russian in this project (case 476.4; until case 272 the rule was a section of the Render of `rule-claude-md`, a standing condition with no page and no Estimate).
    new: rendered into `guppi.toml` as codes, such as `en` and `ru` (case 476.4; until case 272 the rule was a section of the Render of `rule-claude-md`, a standing condition with no page and no Estimate).
  - old: A Case is discussed in Russian and read in English, whole,
    new: A Case is discussed in the chat language and read in the documentation language, whole,
  change: the Purpose names the two languages by their role
- slug: rule-case-build
  replace:
  - old: with a short Russian text ([[rule-orchestration]])
    new: with a short text in the chat language ([[rule-orchestration]])
  change: the Purpose names the language of the chat by its role
```

```tasks
- [x] update `entity-guppi`
- [x] update `rule-language`
- [x] update `rule-case-build`
- [x] create `estimate-clean-branch-ships-neutral-texts`
- [ ] read `estimate-clean-branch-ships-neutral-texts`
```

### Case 822.8 — No clean version is built while a page with core: true is draft

> **given:**
> `rule-clean-branch`: the rule of `guppi ship`.
> **＋** `estimate-clean-branch-refuses-a-draft-core-page`: the new check of the guard of the build.
> **＋** `rule-skill-merge-main` and `rule-skill-pr-review`: the draft pages that lose `core: true` until they are `built`.
> **＋** `.guppi/guppi/ship.py` and `.guppi/guppi/pages.py`: the copy, and `is_draft_core`, the one judgment of a draft page with `core: true`.
> **＋** `.guppi/tests/test_ship.py`: the tests of `guppi ship`.
> **＋** `.github/workflows/prod.yml` and `prod`: the workflow and the branch it writes.

> **when:**
> `uv run --project .guppi guppi ship <folder>` or `uv run --project .guppi guppi ship --review <folder>`, as `rule-clean-branch` sets it, builds the clean version into an empty folder, with or without the option `--allow-draft`.

> **then:**
> While a rule or an entity with `core: true` stands `draft`, `guppi ship` prints one line for each such page, writes nothing and exits 1.
> **＋** With `--allow-draft`, it writes the clean version into the folder all the same and prints those lines, which set no exit code.
> **＋** `.github/workflows/prod.yml` never passes `--allow-draft`, so it writes nothing to `prod` while such a page stands.
> **＋** The build tells a draft page with `core: true` by `is_draft_core` of `.guppi/guppi/pages.py`, imported.
> **＋** `rule-skill-merge-main` and `rule-skill-pr-review` carry no `core`, so the clean version holds neither them nor the files they render.
> **－** `uv run --project .guppi guppi ship --check` does not judge the status of a page.

```then
create:
- slug: estimate-clean-branch-refuses-a-draft-core-page
  ref: rule-clean-branch
  kind: QA
  purpose: 'Whether guppi ship writes nothing and exits 1 while a page with core: true is draft, and writes the copy with --allow-draft, judging such a page by is_draft_core'
  method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k draft_core
  tags:
  - ci
  - plugin
update:
- slug: rule-clean-branch
  replace:
  - old: '`guppi ship --check` reads no tag (case 816).'
    new: '`guppi ship --check` reads no tag (case 816). While a rule or an entity with `core: true` stands `draft`, `guppi ship <folder>` prints one line for each such page, writes nothing and exits 1, so the workflow writes nothing to `prod`; with the option `--allow-draft` it writes the clean version into the folder all the same and prints those lines, which set no exit code, for an install by hand from that folder, which is where a check that needs an install reads it, and the workflow never passes that option. `guppi ship --check` does not judge the status of a page, and `guppi lint` reports each such page where the module of the command `ship` stands; both judge it by `is_draft_core` of `.guppi/guppi/pages.py`. A draft page that a new project can go without loses `core` until it is `built` (case 822).'
  change: 'guppi ship builds no clean version while a page with core: true is draft, but into a folder with --allow-draft'
- slug: rule-skill-merge-main
  set:
    core: null
  change: core taken off while the page is draft; a Case gives it back once it is built
- slug: rule-skill-pr-review
  set:
    core: null
  change: core taken off while the page is draft; a Case gives it back once it is built
```

```tasks
- [x] update `rule-clean-branch`
- [x] update `rule-skill-merge-main`
- [x] update `rule-skill-pr-review`
- [x] create `estimate-clean-branch-refuses-a-draft-core-page`
- [x] `.guppi/guppi/pages.py`: `is_draft_core` judges a rule or an entity with `core: true` whose `status` is `draft`, and `ship_stands` judges whether the module `guppi.ship` can be found; the docstrings name `guppi ship`, `guppi lint`, `guppi check` and the list of commands, which import them.
- [x] `.guppi/guppi/ship.py`: before it writes, the build prints `ship: <page>: a page with core: true that is draft` for each page that `is_draft_core` accepts, writes nothing and exits 1; with `--allow-draft` it writes the copy and prints those lines with no exit code; `--check` does not judge the status; the docstring says so.
- [x] `.guppi/tests/test_ship.py`: a sample tree with a draft page with `core: true` exits 1 with its line and writes nothing; with `--allow-draft` it writes the copy and exits 0; `--check` prints no line on it; the names of these tests hold `draft_core`.
- [x] read `estimate-clean-branch-refuses-a-draft-core-page`
```

### Case 822.9 — Lint reports a draft page with core: true where the command ship stands

> **given:**
> `rule-lint`: the rule of `guppi lint`.
> **＋** `estimate-lint-checks-the-statuses`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/lint.py` and `.guppi/guppi/pages.py`: lint, and `is_draft_core` and `ship_stands`, which it imports.
> **＋** `.guppi/guppi/check.py` and `.guppi/guppi/cli.py`: `guppi check` and the list of commands, which judge by `ship_stands` too.
> **＋** `.guppi/tests/test_lint.py`: the tests of lint.
> **＋** `vault/wiki/` and `/hi`: the live pages that lint reads, and the moment a `method` may wait for.
> **＋** `vault/raw/2026-10-15/0553/cases/case-820.md`: the Case of this session that writes `check.py` and the list of commands.

> **when:**
> `uv run --project .guppi guppi lint` reads the `status` of the live pages under `vault/wiki/` and the `method` of each Estimate.

> **then:**
> `status`: a `built` entity or rule with an Estimate not `passed`, a `draft` one with every Estimate `passed`; a page without Estimates is not judged for these two.
> **＋** `status`: where `ship_stands` of `.guppi/guppi/pages.py` finds the module of the command `ship`, each entity or rule that `is_draft_core` accepts, with Estimates or without, one finding each.
> **＋** `status`: an Estimate `passed` or `failed` without `## Result`; an Estimate whose `target` is not an entity or a rule, or does not list it in `estimates`.
> **＋** `unread`: every Estimate `failed`, and every Estimate `pending` whose `method` does not wait for a later moment, one finding each, `unread: <status>`.
> **＋** A `method` waits for a later moment when a part of it between two `;` opens with `after`, or with `by hand, after`, and names its event before a colon, or names a later session, the next session, a session after another, a session of a sprint, the session that closes one, the librarian or `/hi`.
> **＋** `deferred`: a placeholder — a rule or entity with `deferred_by` and none of `kind`, `estimates`, `tags` — earns one finding `deferred: <N> times since case <M>` in place of its `schema` findings on those fields and of `orphan`; a page with `deferred_by` whose fields are in place earns none.
> **－** `guppi lint` in a project that installed GUPPI reports none of these pages, since `ship_stands` answers no there.
> **－** A `pending` Estimate whose `method` waits for a later moment earns no `unread` finding.
> **－** A `failed` Estimate earns its `unread` finding whatever its `method` says.

```then
update:
- slug: rule-lint
  replace:
  - old: lint runs with the renderer, in no phase of the session.
    new: 'lint runs with the renderer, in no phase of the session. Where the module of the command `ship` stands, as in the repository that builds the clean version of GUPPI, `guppi lint` also reports each rule or entity with `core: true` that is `draft`, since `guppi ship` builds no clean version while one stands; a project that installed GUPPI gets no such line (case 822).'
  change: 'lint reports a draft page with core: true where the module of ship stands'
- slug: estimate-lint-checks-the-statuses
  set:
    status: pending
    purpose: A status its Estimates do not support, a draft page with core true where the command ship stands, a failed Estimate, a pending Estimate whose reading does not wait for a later moment, and a placeholder are findings of lint
    method: uv run --project .guppi pytest .guppi/tests/test_lint.py
  change: 'the Criterion replaced whole — a draft page with core: true is a status finding where the module of ship stands'
```

```tasks
- [x] update `rule-lint`
- [x] update `estimate-lint-checks-the-statuses`
- [x] `.guppi/guppi/lint.py`: a finding of the class `status` for each page that `is_draft_core` accepts, only where `ship_stands` finds the module, both of `.guppi/guppi/pages.py`, imported; the docstring says so.
- [x] `.guppi/guppi/check.py` and `.guppi/guppi/cli.py`: each judges whether the module of `ship` stands by `ship_stands` of `.guppi/guppi/pages.py`, imported, and holds no copy of it.
- [x] `.guppi/tests/test_lint.py`: a draft page with `core: true` and no Estimate gives the finding where the module `guppi.ship` stands and none where it is missing; a test asserts that `lint`, `check` and `cli` call the same `ship_stands`, and that `lint` and `ship` call the same `is_draft_core`; the names of these tests hold `draft_core`.
- [x] read `estimate-lint-checks-the-statuses`
```

### Case 822.4 — The clean version holds no description of GUPPI as its project

> **given:**
> `rule-claude-md` and `CLAUDE.md`: the page whose Render is `CLAUDE.md`, and the file.
> **＋** `<!-- project-description -->` and `<!-- /project-description -->`: the marker lines of the description of the project.
> **＋** `rule-clean-branch`: the rule of `guppi ship`.
> **＋** `estimate-clean-branch-ships-a-blank-project-description`: the new check of the description in the clean version.
> **＋** `.guppi/guppi/ship.py` and `.guppi/tests/test_ship.py`: the copy and its tests.

> **when:**
> `uv run --project .guppi guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.

> **then:**
> In the Render of `rule-claude-md` and in `CLAUDE.md` that it writes, the lines between `<!-- project-description -->` and `<!-- /project-description -->` are the heading `# Project`, a blank line and the line `Project description: not set yet.`, and nothing else.
> **＋** Every other line of that Render and of that `CLAUDE.md` stays as the project it builds from holds it.
> **＋** `uv run --project .guppi guppi render --check` over the clean version names no file that differs.
> **－** In the project it builds from, `rule-claude-md` and `CLAUDE.md` keep the heading and the description of that project.

```then
create:
- slug: estimate-clean-branch-ships-a-blank-project-description
  ref: rule-clean-branch
  kind: QA
  purpose: Whether guppi ship writes, between the marker lines of the description in rule-claude-md and CLAUDE.md, a heading and a line that says the description is not set yet, and leaves every other line and the render check of the copy as they are
  method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k description
  tags:
  - plugin
  - render
update:
- slug: rule-clean-branch
  replace:
  - old: It writes any other `[[…]]` link to a page or a file it does not write as the slug in a code span.
    new: 'It writes any other `[[…]]` link to a page or a file it does not write as the slug in a code span. In the Render of `rule-claude-md` and in `CLAUDE.md` that it writes, it puts the heading `# Project` and the line `Project description: not set yet.` between the lines `<!-- project-description -->` and `<!-- /project-description -->`, in place of the heading and the description of GUPPI, which the install Case of `rule-morph` replaces with the description of the project (case 822).'
  change: guppi ship writes a blank description of the project into rule-claude-md and CLAUDE.md
```

```tasks
- [x] update `rule-clean-branch`
- [x] create `estimate-clean-branch-ships-a-blank-project-description`
- [x] `.guppi/guppi/ship.py`: one function writes the heading `# Project`, a blank line and `Project description: not set yet.` between `<!-- project-description -->` and `<!-- /project-description -->` in the Render of `rule-claude-md` and in `CLAUDE.md` that the copy holds; the docstring says so.
- [x] `.guppi/tests/test_ship.py`: the sample tree holds a `rule-claude-md` with `core: true` and its `CLAUDE.md`, both with the block; the copy holds the placeholder in both, every other line unchanged, and `guppi render --check` over the copy exits 0; the names of these tests hold `description`.
- [x] read `estimate-clean-branch-ships-a-blank-project-description`
```
