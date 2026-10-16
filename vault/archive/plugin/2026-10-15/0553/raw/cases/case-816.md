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

> **tasks:**
> - [ ] create `estimate-clean-branch-installs-as-a-plugin`
>   - ref: `rule-clean-branch`
>   - kind: `QA`
>   - purpose: `Whether the clean version holds the manifest of the plugin guppi and the catalogue guppi-marketplace, passes claude plugin validate, which CI runs before prod is written, and installs as a plugin with no error`
>   - method: `uv run pytest tests/test_ship.py; by hand, after the Work Mode of this change: uv run guppi ship --allow-draft into an empty local folder, claude plugin validate run on that folder, the two files of its .claude-plugin/ and the step of .github/workflows/prod.yml that runs claude plugin validate, and in an empty project an add of that folder as a catalogue and an install of guppi from it, read against the Criterion`
>   - tags: `[ci, plugin]`
> - [ ] update `rule-clean-branch`
>   - old: `and keeps in its link fields only the pages it writes.`
>   - new: `` and keeps in its link fields only the pages it writes. It also writes the folder `.claude-plugin/`, which makes the clean version a Claude Code plugin and the catalogue that lists it: `plugin.json`, the manifest of the plugin `guppi`, and `marketplace.json`, the catalogue `guppi-marketplace` of the owner `kirMykholap`, whose one entry is the plugin `guppi` at the root of the branch, `./`. It copies both from the folder `plugin/` of this repository, which no branch of this repository loads as a plugin and which the clean version does not hold (case 816). ``
>   - old: `and writes none when nothing changed or when the command exits 1.`
>   - new: `` and writes none when nothing changed or when the command exits 1. Before it commits, it installs Claude Code and runs `claude plugin validate` on the clean folder, and writes nothing when that check fails (case 816). ``
>   - set:
>     ```
>     implementation_ref: [guppi/ship.py, tests/test_ship.py, .github/workflows/prod.yml, plugin/plugin.json, plugin/marketplace.json]
>     ```
>   - change: `the clean version holds the manifest of the plugin guppi and the catalogue guppi-marketplace, copied from plugin/, and CI runs claude plugin validate before it commits`
> - [ ] `plugin/plugin.json`: the template of the manifest with no `version`: `name` `guppi`, the `description` `A Claude Code harness governed by ratified decisions, and the Obsidian vault it compiles into`, `author` `{"name": "kirMykholap"}`, `repository` `https://github.com/kirMykholap/GUPPI`.
> - [ ] `plugin/marketplace.json`: the template of the catalogue: `name` `guppi-marketplace`, `owner` `{"name": "kirMykholap"}`, `plugins` with one entry, `name` `guppi`, `source` `./` and the same description.
> - [ ] `guppi/ship.py`: `guppi ship <folder>` copies `plugin/plugin.json` and `plugin/marketplace.json` into `.claude-plugin/` of the clean version and writes no file of `plugin/`; the docstring names both files.
> - [ ] `.github/workflows/prod.yml`: a step between the build and the commit installs Claude Code and runs `claude plugin validate "$RUNNER_TEMP/clean"`, so that a failed check fails the run before anything is pushed; the comment at the top names that step.
> - [ ] `tests/test_ship.py`: the sample tree holds `plugin/plugin.json` and `plugin/marketplace.json`; the file set of `test_it_writes_the_code_the_harness_and_the_core_pages_only` takes `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` and no file of `plugin/`; a test reads both written files and checks the keys and the values that the `then` of this Case names.
> - [ ] read `estimate-clean-branch-installs-as-a-plugin`

> **ratification:**
> ```
> - decision[case 816.1][create][estimate-clean-branch-installs-as-a-plugin]{ref:rule-clean-branch}{tags:ci,plugin}
> - decision[case 816.1][update][rule-clean-branch]{ref:rule-clean-branch}
> ```

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

> **tasks:**
> - [ ] update `estimate-sprint-plugin-ci-writes-a-clean-branch`
>   - set:
>     ```
>     status: pending
>     purpose: Whether CI writes a clean version of the project to a branch of its own, with no case reference and no session data and with the version of its tag prod-x.y.z, and fails when one remains or when no such tag stands in its history
>     method: "uv run pytest tests/test_ship.py for the version of the highest tag, a tag of another form and a commit with no such tag; by hand, after a run of .github/workflows/prod.yml on a tag prod-x.y.z of a commit of plugin that writes prod, before the close of the sprint plugin: its push with the deploy key of the secret PROD_DEPLOY_KEY, the branch prod it wrote, the version in .claude-plugin/plugin.json of prod and the on: block of .github/workflows/prod.yml read against the Criterion; the person's answer at the close of plugin when no such run comes before it"
>     ```
>   - change: `the Criterion replaced whole — the run on a tag prod-x.y.z writes prod with the version of that tag, and guppi ship exits 1 with no such tag in the history`
> - [ ] update `rule-clean-branch`
>   - old: `` and on each push of a tag `prod-*`, such as `prod-1`, on a commit of another branch. ``
>   - new: `` and on each push of a tag `prod-*` on a commit of another branch. `guppi ship <folder>` gives `.claude-plugin/plugin.json` the version of the highest tag `prod-x.y.z` in the history of the commit it builds, such as `0.2.0` for the tag `prod-0.2.0`; a tag of another form, such as `prod-2`, gives no version, and when no tag `prod-x.y.z` stands in that history `guppi ship <folder>` exits 1 and writes nothing, so the run writes nothing to `prod`; `guppi ship --check` reads no tag (case 816). ``
>   - change: `the version of the plugin is the highest tag prod-x.y.z in the history, and guppi ship exits 1 with no such tag`
> - [ ] `guppi/ship.py`: `guppi ship <folder>` reads the tags `prod-x.y.z` in the history of the commit of the working tree, writes the number of the highest as the `version` of `.claude-plugin/plugin.json`, and exits 1 with a line and nothing written when there is none; the judgment of the form of the tag lives in this module alone; `--check` reads no tag; the docstring says so.
> - [ ] `tests/test_ship.py`: the sample tree carries a tag `prod-x.y.z` in its history, so the tests that build a folder pass; tests that the highest of two such tags is the version, that a tag such as `prod-2` gives no version, that a tree with no such tag exits 1 and writes nothing, and that `--check` passes on such a tree.
> - [ ] stop: after the Work Mode, the owner places the tag `prod-0.2.0` on the last commit of `plugin` and pushes it; the run it starts writes nothing to `prod` while a page with `core: true` stands `draft`, and a copy built with `--allow-draft` finds its version.
> - [ ] read `estimate-sprint-plugin-ci-writes-a-clean-branch`

> **ratification:**
> ```
> - decision[case 816.2][update][estimate-sprint-plugin-ci-writes-a-clean-branch]{ref:entity-sprint-plugin}
> - decision[case 816.2][update][rule-clean-branch]{ref:rule-clean-branch}
> ```
