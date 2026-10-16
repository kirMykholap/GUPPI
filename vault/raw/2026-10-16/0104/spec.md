<!-- approved 02:12:18 · session b9e432eb -->

# Session 0104

## Case 840 — The example of a path pair names no path of GUPPI

> **context:**
> When a Case renames a word or a path everywhere, `guppi generate` runs a `reword` over every live rule, entity and Estimate. Case 819.1 moved the tests of GUPPI from `tests/` to `.guppi/tests/` this way. `.guppi/tests/test_guppi_package.py`, the test of `estimate-guppi-package-runs-from-its-own-folder`, fails when a live page still names a bare `tests/` in a part that a `reword` changes, and it finds it by `reword_pattern` and `Vault.reword_text` of `.guppi/guppi/generate.py`. Case 819.2 wrote `tests/` as the example of a path pair into the Purpose of `rule-page-generation` and into the Criterion of `estimate-generate-rewords`, after the `reword` in ledger order. So the test is red, and the Estimate was read `failed` at line 5 of the ledger of session 1959 and put off by case 837. The brief of the librarian of session 1959 (`vault/wiki/brief.md`, `## Readings at the close`) reports the last run: `uv run --project .guppi guppi test`: 1 failed, 1714 passed, 6 skipped, 1 deselected (exit 1); the failure is `test_guppi_package.py::test_no_live_page_names_the_old_command_or_path_where_a_reword_changes_it[tests/]`. The Result of the Estimate names the same two pages as the only hits. The person chose a neutral example, `docs/` → `site/docs/`. That pair names no path of GUPPI, so the test cannot match it, and it keeps the same matching: `docs/intro.md` changes, and `site/docs/` and `cart/docs/` stay as they are.
>
> The rule that governs the change is the one `case-schema.md` sets: a part inside a Criterion is refused, and a promise changes only by a Criterion replaced whole (case 378.4). So Case 840.1 replaces the Criterion of `estimate-generate-rewords` whole. The behaviour stays the same and only the example changes, and the Estimate goes back to `pending`. The check of the Case file sends one note for each line of the old Criterion that the new one does not carry; the line with the `tests/` example is such a line, and it changes on purpose. Its `method` loses the part by hand: that part waits for the librarian's run that applied the `reword` of `rule-guppi-package`, which ran in session 1959, and its outcome stands in the Result. `.guppi/tests/test_generate.py` checks the matching of a path pair with `tests/` (`test_reword_pattern_reads_a_path_pair_from_the_start_of_a_path` among others). The new example is the same matching on another folder, so no new test is added. No code changes. The docstrings of `.guppi/guppi/generate.py` keep `tests/` as their example, since the test reads only the live pages. Of the other Estimates of `rule-page-generation`, none speaks of the example, and they stand. The defer of case 793 on `rule-page-generation` is about a form of `update` that removes a section; this Case does not settle it, and it stands.
>
> The pages change at the librarian's run of this session, not before. A reading of `test_guppi_package.py` at this session's Retro would still be red. So Case 840.2 sets `estimate-guppi-package-runs-from-its-own-folder` `pending` with its Criterion unchanged, takes up the defer of case 837, and gives it a `method` that waits for that librarian's run. This settles Frontier item C3 as well. No `create` stands in the Case, so no query of the vault for a free slug was run.

> **problem:**
> Two live pages use the path `tests/` as the example of a path pair of `reword`, and the Criterion of `estimate-guppi-package-runs-from-its-own-folder` forbids such a path on a live page. Its test stays red, and the Estimate stays `failed` and put off.

> **recommend:**
> - **How do we settle the clash between the example and the test?**
>   - Recommended: (a) change the example to a neutral folder, such as `docs/` → `site/docs/`, in both pages; the Criterion of `estimate-generate-rewords` replaced whole and set `pending`.
>   - Answer: agreed, (a).
> - **Does this Case also re-read the failed Estimate (item C3)?**
>   - Recommended: (a) yes, as a second part of this Case: the Estimate set `pending` with its Criterion unchanged, the defer taken up, and a `method` that waits for the librarian's run of the session that changes the example.
>   - Answer: agreed, (a).
> - **What does the reading of `estimate-generate-rewords` run once its Criterion is replaced?**
>   - Recommended: (a) keep only the test, `pytest .guppi/tests/test_generate.py`, read at this session's Retro.
>   - Answer: agreed, (a).

### Case 840.1 — The example of a path pair is a neutral folder

> **given:**
> `estimate-generate-rewords`: its Criterion is replaced whole, and its `method` is set anew.
> **＋** `rule-page-generation`: the rule of `guppi generate`, whose Purpose names the example of a path pair.
> **＋** `.guppi/guppi/generate.py`: `guppi generate` and the matching of a `reword` pair.
> **＋** `.guppi/guppi/prespec.py`: the preview of `uv run --project .guppi guppi prespec --check`.
> **＋** `.guppi/tests/test_generate.py`: the test of the reading.
> **＋** `.guppi/tests/test_guppi_package.py`: the test that finds a path of GUPPI outside `.guppi/` on a live page.
> **＋** `vault/wiki/`: the live pages that a `reword` changes, beside `vault/archive/` and `vault/raw/`, which it never touches.
> **＋** `docs/`: the example folder of a path pair, with `site/docs/`, `docs/intro.md`, `site/docs/intro.md` and `cart/docs/`, paths of no real project.

> **when:**
> `guppi generate` applies an `update` entry whose item carries `reword`, a list of `{old, new}` pairs.

> **then:**
> A pair whose `old` does not end with `/` is replaced as a whole word, with no letter, digit, `_` or `-` right before or after it.
> **＋** A pair whose `old` ends with `/`, such as `docs/`, is replaced as the start of a path: where no letter, digit, `_`, `-`, `.` or `/` stands right before it, whatever follows it, so the pair `docs/` → `site/docs/` turns `docs/intro.md` into `site/docs/intro.md` and leaves `site/docs/` and `cart/docs/` as they are.
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
  - old: A pair whose `old` ends with `/`, such as `tests/`, is the start of a path
    new: A pair whose `old` ends with `/`, such as `docs/`, is the start of a path
  change: the example of a path pair is docs/, a folder that names no path of GUPPI
- slug: estimate-generate-rewords
  set:
    status: pending
    method: uv run --project .guppi pytest .guppi/tests/test_generate.py on a temp vault whose pages hold paths in their text and their link fields
  change: the Criterion replaced whole — the example of a path pair is docs/ → site/docs/; the method keeps the test alone
```

```tasks
- [x] update `rule-page-generation`
- [x] update `estimate-generate-rewords`
- [x] read `estimate-generate-rewords`
```

### Case 840.2 — The package Estimate is read again after the new example lands

> **given:**
> `estimate-guppi-package-runs-from-its-own-folder`: set `pending`, its Criterion kept, its `method` set anew.
> **＋** `rule-guppi-package`: the rule that the Estimate checks.
> **＋** `decision-case-837`: the decision that put the Estimate off.
> **＋** `.guppi/tests/test_guppi_package.py`: the test of the reading.
> **＋** `.claude/settings.json`: the hooks of a session of the repository of GUPPI.
> **＋** `vault/wiki/`: the live pages that the test reads.

> **when:**
> In the repository of GUPPI, after the move of the code and the render of the harness, a session of Claude Code opens and its hooks, skills and agents run the code of GUPPI, and `uv run --project .guppi pytest` runs the tests of `.guppi/tests/`.

> **then:**
> No live rule, entity or Estimate names a command that runs the code of GUPPI or its tests through `uv run` without `--project .guppi` outside History and Result, and none names a path of that code or those tests outside `.guppi/`.
> **－** The Decision pages, the lessons and the Insights keep the old command and the old paths, since they are records.

```then
update:
- slug: estimate-guppi-package-runs-from-its-own-folder
  set:
    status: pending
    method: 'by hand, after the librarian''s run of the session that changes the example of a path pair in rule-page-generation: uv run --project .guppi pytest .guppi/tests/test_guppi_package.py, then a session opened in this repository, /hi typed there, and the output of its hooks read against the Criterion'
  sections:
    Criterion: |-
      When:
      In the repository of GUPPI, after the move of the code and the render of the harness, a session of Claude Code opens and its hooks, skills and agents run the code of GUPPI, and `uv run --project .guppi pytest` runs the tests of `.guppi/tests/`.
      **＋** `uv run --project .guppi guppi ship <folder>` builds the clean version, as `rule-clean-branch` sets it.

      Then:
      The package `guppi`, its `pyproject.toml`, its lock file `uv.lock`, its tests and a `.gitignore` that holds `.venv/` stand under `.guppi/`, and `.guppi/pyproject.toml` declares pytest and ruff for the tests.
      **＋** Each hook of `.claude/settings.json`, and each command of a skill, an agent, the `Makefile` and `.github/workflows/prod.yml` that runs the code of GUPPI or its tests, runs it through `uv run --project .guppi`, and no hook prints an error.
      **＋** No live rule, entity or Estimate names a command that runs the code of GUPPI or its tests through `uv run` without `--project .guppi` outside History and Result, and none names a path of that code or those tests outside `.guppi/`.
      **＋** `.guppi/tests/test_guppi_package.py` fails on such a command in a file of `.claude/`, the `Makefile`, `.github/workflows/` or a live rule, entity or Estimate, and on such a path in such a page, found by the matching of `reword` of `guppi generate`.
      **＋** Each module that finds its own refusals in the transcript by the command of its hook finds them under the command with `--project .guppi` and under the command without it.
      **＋** The Bash and PowerShell guards judge `uv run --project .guppi python` as they judge `uv run python`, and `guppi lint` takes a test path under `.guppi/tests/` in a `method` as it takes one in the folder of tests of the project's own code.
      **＋** The clean version holds no `pyproject.toml` and no `uv.lock` at its root.
      **－** The repository of GUPPI keeps at its root, until a Case of a later session removes them, the `pyproject.toml` and `uv.lock` of a development project that takes the package from `.guppi/`, so a command without `--project .guppi` still runs at its root and no hook of a running session fails.
      **－** The Decision pages, the lessons and the Insights keep the old command and the old paths, since they are records.
      **－** The examples of a project of the person's own in `rule-case-example`, `rule-estimates-schema` and `rule-rules-schema` keep a path of tests of that project, with no `.guppi/`.
  change: read again after the example of a path pair changes in rule-page-generation and estimate-generate-rewords; the Criterion stands, the method waits for the librarian's run that writes the new example
```

```tasks
- [x] update `estimate-guppi-package-runs-from-its-own-folder`
- [ ] read `estimate-guppi-package-runs-from-its-own-folder`
```

## Case 841 — The tag prod-0.2.0 stands on plugin before the readings of the batch

> **context:**
> `guppi ship` builds the clean version of GUPPI only when the history of HEAD holds a tag `prod-x.y.z`, which gives `.claude-plugin/plugin.json` its version; `VERSION_TAG` of `.guppi/guppi/ship.py` is the one judgment of that form, and `prod-2` gives no version. The repository holds the tags `prod-1` and `prod-2` only, as `.git/refs/tags/` shows and no packed tag adds, so each build exits 1, the local build with `--allow-draft` too, and the brief reports that `guppi ship --allow-draft` exits 1 with no tag `prod-x.y.z`. That blocks the readings of the other Cases of this batch (842 to 846). A push of such a tag starts `.github/workflows/prod.yml`, whose `on:` block takes each tag `prod-*`; its build runs without `--allow-draft`, and while a page with `core: true` stands `draft` `guppi ship` exits 1 before it reads a tag, so the run writes nothing to `prod`. The brief's Flags list seven such pages from the last `guppi check`: `entity-sprint`, `rule-guppi-package`, `rule-harness`, `rule-morph`, `rule-ratification`, `rule-skill-hi` and `rule-work-mode`. The person chose a local tag `prod-0.2.0` on the last commit of `plugin` as the first task of Work Mode, and the push as a `stop:` task, since `rule-where-to-stop` makes a push to a remote a stop. `/pre-spec` found that Work Mode runs the tasks in the order of the Spec, as `.claude/skills/work/SKILL.md` sets it, so a push in this Case would run before the readings by hand of Cases 843 to 846, while Case 843 reads before the push. The person agreed to move the `stop:` task of the push out of this Case to run after the install readings; it stands in Case 850, so this Case keeps the local tag alone. The tag also opens the reading of `estimate-clean-branch-ships-neutral-texts`, whose `method` waits for a tag `prod-x.y.z` in the history of HEAD and for the librarian's run of the session that set that `method`, which the brief says was the run of session 1959. No Case of the plan names it, and this Case does not change it: the Retro of this session reads it by its `method`, a `guppi ship --allow-draft` into an empty folder, by the agent alone. This Case takes up the unticked `stop:` task at line 165 of `vault/raw/2026-10-15/0553/spec.md`, which named the same tag. The promise stays with `estimate-sprint-plugin-ci-writes-a-clean-branch`: its Criterion already covers the run on a tag `prod-x.y.z` and the run that writes nothing when `guppi ship` exits 1, and its `method` waits for a run that writes `prod` before the close of `plugin`, or the person's answer at that close. So its Criterion, `purpose` and `method` stand, the `update` carries only `change`, and Retro leaves it `pending`. The seven draft pages stay out of this Case: each becomes `built` by its own Estimates. A Grep `prod-2|prod-0\.2\.0` over `vault/wiki/`, with `log.md` and `brief.md` left out, printed `sprint.md`, `entities/entity-sprint-plugin.md`, `rules/rule-clean-branch.md` and `estimates/estimate-sprint-plugin-ci-writes-a-clean-branch.md`. In `rule-clean-branch` and the Estimate, `prod-2` stands as the example of a tag of another form and `prod-0.2.0` as an example of a version, and both stay true. The milestone line of `entity-sprint-plugin`, which `guppi sprint` copies into `sprint.md`, still names a tag `prod-2`; Case 847 of this batch rewords it, so this Case leaves it.

> **problem:**
> No tag `prod-x.y.z` stands in the history of `plugin`, so no clean version is built, locally or by CI. The question is which tag is placed, when and where, and where its push stands while the draft pages with `core: true` still stop the build of `prod`.

> **recommend:**
> - **Which name does the tag take?**
>   - Recommended: (a) `prod-0.2.0`, the name the open task and `rule-clean-branch` already use.
>   - Answer: agreed, (a).
> - **When and on which commit is the tag placed?**
>   - Recommended: (a) the first task of Work Mode, on the last commit of `plugin` at that moment, local only.
>   - Answer: agreed, (a).
> - **What does the push of the tag do in this session?**
>   - Recommended: (a) a `stop:` task in this Work Mode: the tag is pushed on the person's word; the run fails on the draft pages and writes nothing to `prod`, and the Estimate stays `pending`.
>   - Answer: agreed, (a).
> - **Which Estimate checks this Case?**
>   - Recommended: (a) `estimate-sprint-plugin-ci-writes-a-clean-branch` stands as it is.
>   - Answer: agreed, (a).
> - **Are the seven draft pages with `core: true` part of this Case?**
>   - Recommended: (a) left out: this Case sets only the tag and its push.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec`, move the `stop:` task of the push out of this Case into Case 847, since Work Mode runs the tasks in the order of the Spec and Case 843 reads before the push; and name `estimate-clean-branch-ships-neutral-texts`, whose reading the tag opens.
>   - Taken: the push left this Case and stands in Case 850, a new Case after the install readings; this Case keeps the local tag as the first task of Work Mode, and `context` names the Estimate that the Retro of this session reads by its `method`.

> **given:**
> `estimate-sprint-plugin-ci-writes-a-clean-branch`: the Estimate of the run on a tag, its Criterion kept.
> **＋** `rule-clean-branch`: the rule of `guppi ship` and of the workflow that writes `prod`.
> **＋** `.guppi/guppi/ship.py`: `guppi ship`, which reads the tags `prod-x.y.z` in the history of HEAD.
> **＋** `.claude-plugin/plugin.json`: the manifest of the clean version, whose `version` comes from the tag.
> **＋** `vault/raw/2026-10-15/0553/spec.md`: the Spec whose `stop:` task on the tag this Case takes up.
> **＋** `vault/raw/2026-10-16/0104/cases/case-850.md`: the Case after the install readings, which holds the `stop:` task of the push of the tag.

> **when:**
> In Work Mode of this session, as its first task, the owner places the tag `prod-0.2.0` on the last commit of the branch `plugin`, and `uv run --project .guppi guppi ship --allow-draft <folder>` runs on that commit or a later one.

> **then:**
> `uv run --project .guppi guppi ship --allow-draft <folder>` writes the clean version, with `0.2.0` as the `version` of `.claude-plugin/plugin.json`.
> **－** The tag stays local in this Case: its push to GitHub is the `stop:` task of `vault/raw/2026-10-16/0104/cases/case-850.md`.
> **－** The pages with `core: true` that stand `draft` do not change.

```then
update:
- slug: estimate-sprint-plugin-ci-writes-a-clean-branch
  change: 'the tag prod-0.2.0 placed on plugin, local; its push is a stop: task of case 850; the Criterion stands, and the reading waits for a run that writes prod'
```

```tasks
- [x] update `estimate-sprint-plugin-ci-writes-a-clean-branch`
- [x] `git tag prod-0.2.0` on the last commit of `plugin`, as the first task of Work Mode, before the readings of the other Cases of this batch; local only.
- [x] by hand: `git tag --list prod-* --merged HEAD` prints `prod-0.2.0`, and `uv run --project .guppi guppi ship --allow-draft <folder>` into an empty folder writes `.claude-plugin/plugin.json` with `version` `0.2.0`.
```

## Case 842 — The plugin install check waits for a version tag

> **context:**
> `estimate-clean-branch-installs-as-a-plugin` checks that `guppi ship` writes the manifest of the plugin `guppi` and the catalogue `guppi-marketplace` into the clean version, that `claude plugin validate` passes on it, that `.github/workflows/prod.yml` runs that check before it writes `prod`, and that the plugin installs into an empty project. Its by-hand part builds the clean version with `guppi ship --allow-draft`. `.guppi/guppi/ship.py` takes the version from the highest tag `prod-x.y.z` in the history of HEAD, and with no such tag it prints `ship: no tag prod-x.y.z in the history of HEAD; nothing written` and exits 1. The brief of the librarian of session 1959 (`vault/wiki/brief.md`, `## Readings due`) says `git tag` holds `prod-1` and `prod-2` only. So the Retro of session 1739 marked the Estimate `failed` unread, and case 831 put it off. Its `method` waits for an event that has passed, the Work Mode of case 816.1, and does not name the tag.
>
> The tag is the work of Case 841 of this batch, the Frontier item C1. Its case file did not yet stand when this Case was built, so this Case names no tag of its own and waits for any tag `prod-x.y.z` in the history of HEAD. The person chose to set the Estimate `pending`, write its Criterion back unchanged and give it a `method` whose by-hand part opens with `by hand, after a tag prod-x.y.z stands in the history of HEAD:`. By `case-schema.md` (case 781), and by `waits_for_an_event` of `.guppi/guppi/lint.py`, such a part waits for its event, so Retro leaves the Estimate `pending` until the tag stands and marks it failed for no missing tag. The person also chose to do the install step: the agent runs the test, the build, `claude plugin validate` and the reading of the files, and the person adds the folder as a catalogue and installs `guppi` from it in an empty project, as the other install checks of the sprint do. The rule that governs a promise is `case-schema.md`: a promise changes only by a Criterion replaced whole (case 378.4). The Criterion stands: each of its lines still states what `rule-clean-branch` sets, and the failure was the missing tag, not the promise. So the Estimate itself checks this Case, and no new Estimate is made.
>
> The Case takes up the defer of case 831 on this page by `{supersedes:case 831}`. Case 831 also put off `estimate-plugin-install-writes-guppi-into-an-empty-project` and `estimate-guppi-package-is-ready-after-the-install`; those are the items of Cases 843 and 846, and this Case does not settle them. A Grep for `estimate-clean-branch-installs-as-a-plugin` over the repository, `vault/raw/` left out, printed `vault/wiki/brief.md`, `vault/wiki/backlog.md`, `vault/wiki/rules/rule-clean-branch.md` and `vault/wiki/log.md`; the hit in `rule-clean-branch` is its `estimates` field and a History line, and neither changes. A Grep for `installs-as-a-plugin|after the Work Mode of this change` over `.guppi/` printed nothing, so no test reads this page live. The brief (`## Flags`) reports `guppi check` at exit 1 with `unread: failed` on the 4 failed Estimates, this one among them; with the Estimate `pending`, that line goes after the librarian's run. No `create` stands in the Case, so no query of the vault for a free slug was run.

> **problem:**
> The plugin install check is `failed` and put off. It was never read, because no tag `prod-x.y.z` stood. Its `method` does not say that it waits for that tag, and it does not say who installs the plugin.

> **recommend:**
> - **How does the plugin-install check come back to a reading?**
>   - Recommended: (a) set it `pending`, keep its promise word for word, and make the by-hand part of its `method` wait for a tag `prod-x.y.z` in the history of HEAD; the defer is taken up.
>   - Answer: agreed, (a).
> - **Who installs the plugin into an empty project?**
>   - Recommended: (a) the person installs by `/plugin marketplace add <folder>` and `/plugin install guppi@guppi-marketplace` in an empty project in Claude Code; the agent runs the test, the build, `claude plugin validate` and the reading of the files.
>   - Answer: agreed, (a).

> **given:**
> `estimate-clean-branch-installs-as-a-plugin`: set `pending`, its Criterion kept, its `method` set anew.
> **＋** `rule-clean-branch`: the rule that the Estimate checks.
> **＋** `decision-case-831`: the decision that put the Estimate off.
> **＋** `.guppi/guppi/ship.py`: the command `guppi ship` and its option `--allow-draft`.
> **＋** `.guppi/tests/test_ship.py`: the tests of the command `ship`.
> **＋** `plugin/plugin.json` and `plugin/marketplace.json`: the sources of the manifest and of the catalogue.
> **＋** `.github/workflows/prod.yml`: the workflow that writes `prod`.
> **＋** `.claude-plugin/`: the folder of the clean version that holds `.claude-plugin/plugin.json`, the manifest, and `.claude-plugin/marketplace.json`, the catalogue.

> **when:**
> `uv run --project .guppi guppi ship <folder>`, or `uv run --project .guppi guppi ship --allow-draft <folder>` into a local folder, builds the clean version, as `rule-clean-branch` sets it, and `claude plugin validate` runs on that folder.
> **＋** In an empty project, someone adds that folder to Claude Code as a catalogue and installs the plugin `guppi` from it.

> **then:**
> `uv run --project .guppi guppi ship <folder>` writes `.claude-plugin/plugin.json` into the clean version, copied from `plugin/plugin.json`, with the `name` `guppi`, a description, the author `kirMykholap` and the repository of the project on GitHub.
> **＋** It writes `.claude-plugin/marketplace.json`, copied from `plugin/marketplace.json`, with the `name` `guppi-marketplace`, the owner `kirMykholap` and one entry, the plugin `guppi`, whose source is the root of the branch.
> **＋** `claude plugin validate` passes on that folder.
> **＋** Before a run of `.github/workflows/prod.yml` commits, it runs `claude plugin validate` on the clean folder.
> **＋** The catalogue adds to Claude Code, and the plugin `guppi` installs from it, with no error.
> **－** A run whose `claude plugin validate` fails fails and writes nothing to `prod`.
> **－** The clean version holds no folder `plugin/`, and this repository holds no folder `.claude-plugin/`.
> **－** Which skills the installed plugin `guppi` loads is no part of this promise.

```then
update:
- slug: estimate-clean-branch-installs-as-a-plugin
  set:
    status: pending
    method: 'uv run --project .guppi pytest .guppi/tests/test_ship.py; by hand, after a tag prod-x.y.z stands in the history of HEAD: uv run --project .guppi guppi ship --allow-draft into an empty local folder, claude plugin validate run on that folder, the two files of its .claude-plugin/ and the step of .github/workflows/prod.yml that runs claude plugin validate read against the Criterion, then the person''s answer after the person adds that folder as a catalogue by /plugin marketplace add <folder> and installs guppi by /plugin install guppi@guppi-marketplace in an empty project open in Claude Code'
  sections:
    Criterion: |-
      When:
      `uv run --project .guppi guppi ship <folder>`, or `uv run --project .guppi guppi ship --allow-draft <folder>` into a local folder, builds the clean version, as `rule-clean-branch` sets it, and `claude plugin validate` runs on that folder.
      **＋** In an empty project, someone adds that folder to Claude Code as a catalogue and installs the plugin `guppi` from it.

      Then:
      `uv run --project .guppi guppi ship <folder>` writes `.claude-plugin/plugin.json` into the clean version, copied from `plugin/plugin.json`, with the `name` `guppi`, a description, the author `kirMykholap` and the repository of the project on GitHub.
      **＋** It writes `.claude-plugin/marketplace.json`, copied from `plugin/marketplace.json`, with the `name` `guppi-marketplace`, the owner `kirMykholap` and one entry, the plugin `guppi`, whose source is the root of the branch.
      **＋** `claude plugin validate` passes on that folder.
      **＋** Before a run of `.github/workflows/prod.yml` commits, it runs `claude plugin validate` on the clean folder.
      **＋** The catalogue adds to Claude Code, and the plugin `guppi` installs from it, with no error.
      **－** A run whose `claude plugin validate` fails fails and writes nothing to `prod`.
      **－** The clean version holds no folder `plugin/`, and this repository holds no folder `.claude-plugin/`.
      **－** Which skills the installed plugin `guppi` loads is no part of this promise.
  change: read again once a tag prod-x.y.z stands; the Criterion stands, the method waits for the tag and names the person's install
```

```tasks
- [x] update `estimate-clean-branch-installs-as-a-plugin`
- [ ] read `estimate-clean-branch-installs-as-a-plugin`
```

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

```then
update:
- slug: estimate-plugin-install-writes-guppi-into-an-empty-project
  set:
    status: pending
  change: set to pending with its Criterion unchanged, for a reading once a tag prod-x.y.z stands
```

```tasks
- [x] update `estimate-plugin-install-writes-guppi-into-an-empty-project`
- [x] `uv run --project .guppi pytest .guppi/tests/test_ship.py -k plugin_skill`
- [x] read `estimate-plugin-install-writes-guppi-into-an-empty-project`
```

## Case 844 — The tests of the clean version are read after a version tag

> **context:**
> `estimate-clean-branch-ships-the-tests` checks that `guppi ship` writes the tests of GUPPI into the clean version, cleans only their comments and docstrings, and that they pass there. The first part of its `method`, `pytest .guppi/tests/test_ship.py -k tests`, ran inside `guppi test`. The brief of the librarian of session 1959 (`vault/wiki/brief.md`, Readings due) reports that `guppi test` ran `.guppi/tests/test_ship.py` with no failure, with its `live` test deselected, and that this run ran no `guppi ship`. The part by hand builds the clean version with `guppi ship --allow-draft` into an empty folder and runs `pytest .guppi/tests` there. No reading of that part was ever taken. That build cannot run today. `run` of `.guppi/guppi/ship.py` takes the version from `version`, which lists the tags `prod-*` merged into HEAD and matches them with `VERSION_TAG`. With no tag `prod-x.y.z`, it prints `ship: no tag prod-x.y.z in the history of HEAD; nothing written`. `rule-clean-branch` states the same in its Purpose. The `method` of the Estimate does not say this. It waits only for the librarian's run of its change, which has already run, so the page looked ready to read. The brief therefore proposed to defer it into `backlog.md`.
>
> The person chose to take the reading in this session instead, in one batch with the other items that wait for a version tag. Case 841 of this session owns the task that sets that tag. The rule that governs the change is the one `case-schema.md` and `rule-retro` set for a `method`: a part that opens with `by hand, after` names its event before a colon. Retro leaves the Estimate `pending` until that event comes, and reads it in the session in which the event came (case 781). So the `method` names the tag as its event. A `method` change alone would leave the page unread by the Retro of this session, since `rule-retro` does not read an Estimate whose `update` names one part alone. So the Case sets the page `pending` and its Criterion is replaced by the same text, as Case 840.2 did. The Criterion stands as it was, since the behaviour it checks does not change. The ledger hook (`refused_readings` of `.guppi/guppi/ledger.py`) refuses an `estimate` line of a slug that a decision line of this session updates until Retro opens. So the reading is taken at Retro, after the tag task of Case 841, and not in Work Mode. If no tag stands then, the page stays `pending` and is not set `failed`.
>
> The reading builds its own empty temporary folder. It does not share the folder of the plugin install of Case 842, so the `.venv` and the caches that `pytest` writes there never reach a folder that a plugin is installed from. A Grep for `estimate-clean-branch-ships-the-tests` over `vault/wiki/` printed `brief.md`, `log.md`, `rules/rule-clean-branch.md` and `estimates/estimate-clean-branch-writes-a-clean-copy.md`. Over `.claude/` it printed nothing. The rule lists the Estimate in `estimates`. The Criterion of `estimate-clean-branch-writes-a-clean-copy` points to it for what the copy writes of the tests. Both stay true, since the Criterion does not change. `test_no_live_page_names_the_old_command_or_path_where_a_reword_changes_it` of `.guppi/tests/test_guppi_package.py` reads the `method` of each live Estimate. The new `method` names `.guppi/tests` and `uv run --project .guppi` as the old one does, so the test finds no hit there. No `create` stands in the Case, so no query of the vault for a free slug was run.

> **problem:**
> The part by hand of the reading of `estimate-clean-branch-ships-the-tests` needs a tag `prod-x.y.z` in the history of HEAD, and none stands. Its `method` waits only for an event that has already come, so the page looks ready to read when it is not, and a Retro would set it `failed` again for the same reason.

> **recommend:**
> - **What does this Case change on the Estimate?**
>   - Recommended: (a) the `method` waits until a tag `prod-x.y.z` stands in the history of HEAD; the Criterion stays and is written back unchanged; the page stays `pending`, and Retro reads it in this session after the tag is set.
>   - Answer: agreed, (a).
> - **Does this reading share its build folder with the plugin-install reading of item C4?**
>   - Recommended: (a) each reading builds its own folder; this one builds into its own empty temporary folder, as its `method` says.
>   - Answer: agreed, (a).

> **given:**
> `estimate-clean-branch-ships-the-tests`: set `pending`, its Criterion kept, its `method` set anew.
> **＋** `rule-clean-branch`: the rule of `guppi ship`, which the Estimate checks.
> **＋** `rule-retro`: the rule of the reading of an Estimate whose `method` waits for an event.
> **＋** `.guppi/guppi/ship.py`: the copy, the judgment of the comments, the docstrings and the samples, and the version from the tag.
> **＋** `.guppi/tests/` and `.guppi/tests/test_ship.py`: the tests of GUPPI, and the tests of the command `ship`.
> **＋** `.guppi/.venv/`: the Python environment that the clean version does not hold.
> **＋** `uv run --project .guppi pytest .guppi/tests`: the run of the tests.

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
update:
- slug: estimate-clean-branch-ships-the-tests
  set:
    status: pending
    method: 'uv run --project .guppi pytest .guppi/tests/test_ship.py -k tests; by hand, after a tag prod-x.y.z stands in the history of HEAD: uv run --project .guppi guppi ship --allow-draft into an empty temporary folder of its own, then uv run --project .guppi pytest .guppi/tests in that folder, read against the Criterion'
  change: the method waits for a tag prod-x.y.z in the history of HEAD, which guppi ship needs; the Criterion stands
```

```tasks
- [x] update `estimate-clean-branch-ships-the-tests`
- [x] read `estimate-clean-branch-ships-the-tests`
```

## Case 845 — The check of the session files is read after the tag

> **context:**
> `estimate-clean-branch-writes-the-session-files` (case 822.3, pending, target `rule-clean-branch`) promises that `guppi ship` writes `sprint.md`, `backlog.md`, `brief.md`, `glossary.md` and `log.md` of a new project as skeletons that their checks pass, and that the first `/hi` of a project that installs GUPPI from that copy starts `/sprint-open`. Its `method` waits only for the librarian's run of its change, and that run has passed. The real blocker is a tag: `run` of `.guppi/guppi/ship.py` prints "ship: no tag prod-x.y.z in the history of HEAD; nothing written" and exits 1 when `version` finds no tag that `VERSION_TAG` accepts. The brief reports in `## Readings due` on the sibling check `estimate-clean-branch-ships-neutral-texts` that "`git tag` holds `prod-1` and `prod-2` only", and on this check that "This run ran no `guppi ship`". The last step of the reading is by hand: the person installs the copy in an empty project, types `/guppi:install`, reopens Claude Code and types `/hi`.
>
> The brief proposed to defer the check into `backlog.md`. The person chose instead to read it in this session, in one batch with the other items that wait for a tag `prod-x.y.z`. Case 841 of this batch owns the task that sets the tag, and this Case sets no tag of its own. The person chose that the `method` names the tag as the event it waits for (Q1), as case 824 did for `estimate-clean-branch-ships-neutral-texts`. The rule against which each option was judged is the form of a `method` in `case-schema.md`: a part between two `;` that opens with `by hand, after` and names its event before a colon waits for that event, and Retro leaves the Estimate `pending` until that event comes (cases 670.4, 781). The new `method` waits for the tag alone. The clause on the librarian's run of its change is dropped: once this update applies, "its change" would read as the change of this Case, whose librarian's run comes after the Retro of this session, so Retro would leave the page unread (a finding of `/pre-spec`). The first part of the `method`, the tests named `skeleton`, waits for no event. The target carries no `core: true`, so the rule of a pointer in a bracket (case 807.4) does not bind the new text, and it holds no pointer.
>
> An `update` that sets only `method` is an update of one part alone: `names_a_part` of `.guppi/guppi/materialize.py` returns true for an item with no `status` under `set` and no `Criterion` under `sections`, and the Render of `rule-retro` says that such an Estimate "is neither read nor set `failed`". So the update sets `pending`, and the Case's `when` and `then` are the Criterion of the page word for word, so that the scripts write it back unchanged, as Case 844 does for `estimate-clean-branch-ships-the-tests`. The Criterion stands as it was, since the behaviour it checks does not change. The person first chose a `stop:` task of this Case for the install by hand (Q2). At `/pre-spec` the person chose instead one `stop:` task in Case 846 for every install by hand of this batch, the empty project with `uv` where the install, `/guppi:install`, the reopen and `/hi` of this reading run among them. That file did not yet hold that task when this Case was written, so this Case holds no `stop:` task and points to that one. Retro takes the reading from what the person reported at that stop and from the run of `guppi ship --allow-draft`, the `skeleton` tests and the three checks over the copy; if no tag stands then, the page stays `pending`. The brief's `## Readings at the close` reports "`uv run --project .guppi guppi test`: 1 failed, 1714 passed, 6 skipped, 1 deselected (exit 1)"; that failure is in `test_guppi_package.py` on `tests/`, which Case 840 handles, and no test of `skeleton` failed. A Grep of `estimate-clean-branch-writes-the-session-files` over the repository outside `vault/raw/` printed `vault/wiki/brief.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-clean-branch.md` and `vault/wiki/estimates/estimate-clean-branch-writes-a-clean-copy.md`. The hit in `rule-clean-branch` is its list of `estimates`, and the hit in `estimate-clean-branch-writes-a-clean-copy` names what the check sets in place of the session files; neither speaks of the `method`, and both stand. The hits in `brief.md` and `log.md` are not read. `test_no_live_page_names_the_old_command_or_path_where_a_reword_changes_it` of `.guppi/tests/test_guppi_package.py` reads each live page against `OLD_COMMANDS`, `uv run guppi` and `uv run pytest`, and `OLD_PATHS`, `guppi/` and `tests/`. The new `method` names `uv run --project .guppi` and `.guppi/tests/test_ship.py` as the old one does, and adds no other command or path, so it gives that test no hit the old text did not give; the failure on `tests/` is the item of Case 840.

> **problem:**
> The check of the session files names an event that has passed, not the tag without which `guppi ship` writes nothing, and its last step needs the person, so it would stay unread again.

> **recommend:**
> - **Does the line on how the check is read change to name the tag?**
>   - Recommended: (a) the method waits for the tag too.
>   - Answer: agreed, (a).
> - **Who does the install in the empty project, and when?**
>   - Recommended: (a) a stop step in Work Mode after the tag.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: a finding of `/pre-spec`: an `update` that sets only `method` names one part alone, so Retro would neither read the page nor set it `failed`, and the `read` task would be debt.
>   - Taken: the update sets `pending`, and the `when` and `then` are the Criterion of the page word for word, so it is written back unchanged.
> - **Change**
>   - Asked: a finding of `/pre-spec`: the clause on the librarian's run of its change would read as the change of this Case, whose librarian's run comes after this Retro.
>   - Taken: the `method` waits for the tag `prod-x.y.z` alone.
> - **Change**
>   - Asked: the person's answer at `/pre-spec`: one `stop:` task in Case 846 for every install by hand of the batch, the install and `/hi` of this reading among them.
>   - Taken: the `stop:` task and the task by hand of this Case go; Retro reads the page from that one stop and the run over the copy.

> **given:**
> `estimate-clean-branch-writes-the-session-files`: the check of the session files as skeletons, set `pending`, its Criterion kept and its `method` set anew.
> **＋** `rule-clean-branch` and `uv run --project .guppi guppi ship <folder>`: the rule of `guppi ship` and the command, whose module `.guppi/guppi/ship.py` needs a tag `prod-x.y.z`.
> **＋** `vault/wiki/sprint.md`, `vault/wiki/backlog.md`, `vault/wiki/brief.md`, `vault/wiki/glossary.md` and `vault/wiki/log.md`: the session files the copy writes as skeletons.
> **＋** `closed_form` of `.guppi/guppi/sprint.py`, `guppi backlog`, `guppi glossary`, `guppi sprint --check`, `guppi backlog --check` and `guppi glossary --check`: the writers and the checks of those files.
> **＋** The plugin `guppi`, `/guppi:install`, `/hi` and `/sprint-open`: the install and the skills that open a session and a sprint.
> **＋** `.guppi/tests/test_ship.py` and `uv run --project .guppi pytest .guppi/tests/test_ship.py -k skeleton`: the tests of the skeletons, the first part of the `method`.
> **＋** `rule-retro`: the rule of the reading of an Estimate whose `method` waits for an event.
> **＋** `vault/raw/2026-10-16/0104/cases/case-846.md`: the Case that holds the one `stop:` task for the installs by hand of this batch.

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
update:
- slug: estimate-clean-branch-writes-the-session-files
  set:
    status: pending
    method: 'uv run --project .guppi pytest .guppi/tests/test_ship.py -k skeleton; by hand, after a tag prod-x.y.z stands in the history of HEAD: in an empty project, guppi installed from a copy that uv run --project .guppi guppi ship --allow-draft wrote into a local folder, the copy and the empty project with uv being those of the reading of estimate-guppi-package-is-ready-after-the-install where that reading runs at the same commit, /guppi:install typed, Claude Code reopened and /hi typed, and guppi sprint --check, guppi backlog --check and guppi glossary --check run over the copy, read against the Criterion'
  change: the method waits for a tag prod-x.y.z in the history of HEAD, without which guppi ship writes nothing; the Criterion stands
```

```tasks
- [x] update `estimate-clean-branch-writes-the-session-files`
- [x] read `estimate-clean-branch-writes-the-session-files`
```

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

```then
update:
- slug: estimate-guppi-package-is-ready-after-the-install
  set:
    status: pending
    method: 'by hand, after a tag prod-x.y.z stands in the history of HEAD: the agent writes the clean version into a local folder by uv run --project .guppi guppi ship --allow-draft; then, at a stop of Work Mode, the person adds that folder as a catalogue, installs the plugin guppi from it and, in an empty project on the machine with uv, types /guppi:install, reopens Claude Code there and types /hi; in an empty project with Claude Code started from a terminal whose PATH holds no folder of uv, types /guppi:install; in an empty project with Claude Code started from a terminal with UV_OFFLINE=1 and UV_CACHE_DIR set to an empty folder, types /guppi:install; the person''s answer on the output of each install, the files of each project and .guppi/.venv/ of the project with uv, read against the Criterion; the copy and the project with uv may be those of the reading of estimate-plugin-install-writes-guppi-into-an-empty-project at the same commit'
  change: the Criterion replaced whole — the install comes from a local copy that guppi ship --allow-draft writes, not from the branch prod; the method makes uv missing by the PATH of a terminal, makes uv sync fail offline and reads the person's answer
```

```tasks
- [x] update `estimate-guppi-package-is-ready-after-the-install`
- [x] By hand, after the task of Case 841 that sets the tag `prod-0.2.0`: `uv run --project .guppi guppi ship --allow-draft <folder>` into an empty local folder outside the repository, and the parts of the readings of Cases 843 and 845 that the agent runs.
- [x] stop: before the push of the tag `prod-0.2.0` by the `stop:` task of Case 850, the one stop for every install by hand of this batch; the person adds that folder by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and, in one go, works in four empty projects: in the project on the machine with `uv`, types `/guppi:install`, reopens Claude Code there and types `/hi` (for Cases 843, 845 and 846); in a project with a `CLAUDE.md` of its own, types `/guppi:install` (for Case 843); in a project with Claude Code started from a terminal whose `PATH` holds no folder of `uv`, types `/guppi:install` (for Case 846); in a project with Claude Code started from a terminal with `UV_OFFLINE=1` and `UV_CACHE_DIR` set to an empty folder, types `/guppi:install` (for Case 846); then the person tells what each project showed; right after the installs, the output of `/guppi:install` and the files of the project with `uv` and of the project with a `CLAUDE.md` of its own are read against the Criterion of `estimate-plugin-install-writes-guppi-into-an-empty-project`, and the projects of Case 846 against the Criterion of `estimate-guppi-package-is-ready-after-the-install`.
- [ ] read `estimate-guppi-package-is-ready-after-the-install`
```

## Case 847 — The milestone of the clean branch names the tag form that guppi ship reads

> **context:**
> The milestone "The clean branch" of `entity-sprint-plugin` says what work is left before CI writes the clean branch. Its line waits for the fix of `guppi ship` for the example Case, and then for a tag `prod-2`. That fix stands in `.guppi/guppi/ship.py`: its docstring says that the text around the example Case of `case-example.md` is judged like any other (case 815). `.git/refs/tags/prod-2` points at c95e75791a69. But `guppi ship` reads only a tag `prod-x.y.z`: with none in the history of HEAD it prints "ship: no tag prod-x.y.z in the history of HEAD; nothing written" and exits 1 (`.guppi/guppi/ship.py`, line 656), and `rule-clean-branch` says that a tag of another form, such as `prod-2`, gives no version. So the line names a run that cannot pass. Case 830 put this line off, and the page carries it in `deferred_by`; this Case takes it up. The rule of the line is `rule-sprint`: an item is `- [[slug]] — <text>`, ticked by the statuses of the slugs before the first ` — `, and the text after it is free; the new text keeps both slugs before the dash. The new line names only the form `prod-x.y.z`. Case 841 of this session sets the tag `prod-0.2.0` locally in Work Mode and pushes it later by a `stop:` task, so the two Cases agree, and the line does not go stale at the next tag. The line also says that the run writes nothing to `prod` while a page with `core: true` stands `draft`, as `rule-clean-branch` sets it. The brief of the last session lists seven such pages under `## Flags`, and Case 841 leaves them as they are. `entity-sprint-plugin` carries no `core: true`, so the pointer form of case 807.4 does not bind its new text. The Estimate that checks the change is `estimate-sprint-plugin-ci-writes-a-clean-branch`, which the line names. Its Criterion already reads the tag `prod-x.y.z` and says that a tag such as `prod-2` gives no version, so it stands, and no Estimate is set `pending`. A Grep of `prod-2` over `vault/wiki/` (with `log.md` and `brief.md` left out, and `decisions/` left out by the hook) printed `vault/wiki/sprint.md`, `vault/wiki/entities/entity-sprint-plugin.md`, `vault/wiki/rules/rule-clean-branch.md` and `vault/wiki/estimates/estimate-sprint-plugin-ci-writes-a-clean-branch.md`. The same Grep over `.claude/` printed nothing. `vault/wiki/sprint.md` changes by the render. `rule-clean-branch` and the Criterion of the Estimate name `prod-2` only as a form that gives no version, which stays true. The `## Result` of the Estimate reports the past run on `prod-2`, which also stays true. A Grep of `entity-sprint-plugin|sprint\.md` over `.guppi/tests/` printed lines of `test_archive.py`, `test_caseid.py`, `test_casecheck.py`, `test_generate.py`, `test_lint.py`, `test_ship.py`, `test_ledger.py`, `test_recall.py`, `test_cleanup.py`, `test_prespec.py`, `test_sprint.py`, `test_sprint_close.py` and `test_materialize.py`. By the printed lines, each one writes `sprint.md` under a project folder of the test or names the path or the slug as a string. None of them reads the milestone line of the live page.

> **problem:**
> The milestone line of `entity-sprint-plugin` waits for a fix that is already done, and for a tag `prod-2` that `guppi ship` does not read. It does not say that the draft core pages still stop the run.

> **recommend:**
> - **How should the line name the tag?**
>   - Recommended: (a) only the form `prod-x.y.z`, with no number.
>   - Answer: agreed, (a).
> - **What should the line list as the work left?**
>   - Recommended: (a) the tag, the CI run read by its Estimate, and the draft core pages that stop the run.
>   - Answer: agreed, (a).
> - **Which check confirms this change?**
>   - Recommended: (a) the existing `estimate-sprint-plugin-ci-writes-a-clean-branch`, its Criterion unchanged.
>   - Answer: agreed, (a).

> **given:**
> `entity-sprint-plugin`: the sprint page whose milestone line changes.
> **＋** `vault/wiki/sprint.md`: the render of the sprint page.
> **＋** `estimate-sprint-plugin-ci-writes-a-clean-branch`: the Estimate that the line names, which reads the CI run.
> **＋** `rule-sprint`: the form of a milestone item.
> **＋** `rule-clean-branch`: the tag that `guppi ship` reads, and the refusal of a draft core page.

> **when:**
> Someone reads the milestone "The clean branch" of `entity-sprint-plugin`, or its render in `vault/wiki/sprint.md`.

> **then:**
> The line says that the owner pushes `plugin` and a tag of the form `prod-x.y.z` on its last commit, and names no number of a tag.
> **＋** The line says that `estimate-sprint-plugin-ci-writes-a-clean-branch` reads the CI run that the tag starts.
> **＋** The line says that this run writes nothing to `prod` while a page with `core: true` stands `draft`, as `rule-clean-branch` sets it.
> **－** The line does not wait for the fix of `guppi ship` for the example Case.

```then
update:
- slug: entity-sprint-plugin
  replace:
  - old: 'what remains: once Work Mode commits the fix of `guppi ship` that cleans the text around the example Case (case 815), the owner pushes `plugin` and a tag `prod-2` on its last commit, and the CI run it starts is read by its Estimate'
    new: 'what remains: the owner pushes `plugin` and a tag of the form `prod-x.y.z` on its last commit, and the CI run it starts is read by its Estimate; while a page with `core: true` stands `draft`, that run writes nothing to `prod`'
  change: the milestone The clean branch names the tag form prod-x.y.z and the draft core pages that stop the run; the defer of decision-case-830 taken up
```

```tasks
- [x] update `entity-sprint-plugin`
- [x] `uv run --project .guppi guppi sprint`
```

## Case 850 — The tag prod-0.2.0 is pushed after the install readings, on the person's word

> **context:**
> Work Mode runs the tasks of the Spec in the order the Spec holds them, as `.claude/skills/work/SKILL.md` says. Case 841 placed the `stop:` task that pushes the tag `prod-0.2.0` in its own Case, before the install readings of Cases 843 to 846, so the push would run before them. The person chose to read the install before the push. At `/pre-spec` the person agreed that Case 846 holds one `stop:` task for every install by hand, and that the push follows after it. The push is a behaviour with a promise of its own, and Case 847, which sets the milestone line of `entity-sprint-plugin`, already has a decision line in the ledger of this session. So the push stands in this new Case, beside Case 847 and after it, and Case 847 stays as it is. Its milestone line already says that the owner pushes a tag of the form `prod-x.y.z` and that the run writes nothing to `prod` while a page with `core: true` stands `draft`. The push is the third condition of `rule-where-to-stop`: an action that git in this repository cannot undo, such as a push to a remote. So the task opens with `stop:` and runs on the person's word, as Case 841 set it (its answer to the question on the push). A push of a tag `prod-*` starts `.github/workflows/prod.yml`. Its build runs without `--allow-draft`, so while the draft pages with `core: true` that the brief lists under `## Flags` stand `draft`, the run fails and writes nothing to `prod`. The Estimate that checks the push is `estimate-sprint-plugin-ci-writes-a-clean-branch`. Its Criterion already covers the run on a tag `prod-x.y.z` and a run that writes nothing when `guppi ship` exits 1, and its `method` waits for a run that writes `prod` before the close of `plugin`. So its Criterion, `purpose` and `method` stand, its `update` here carries only `change`, and it stays `pending`; this Case adds no `read` line, since this run cannot write `prod`.

> **problem:**
> The push of the tag would run before the install readings that the person wants first, because Work Mode runs the tasks in the order of the Spec.

> **recommend:**
> - **How should the line name the tag?**
>   - Recommended: (a) only the form `prod-x.y.z`, with no number, in the milestone line that Case 847 sets.
>   - Answer: agreed, (a).
> - **What should the line list as the work left?**
>   - Recommended: (a) the tag, the CI run read by its Estimate, and the draft core pages that stop the run.
>   - Answer: agreed, (a).
> - **Which check confirms this change?**
>   - Recommended: (a) the existing `estimate-sprint-plugin-ci-writes-a-clean-branch`, its Criterion unchanged.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec`, the person agreed that the `stop:` task that pushes `prod-0.2.0` moves out of Case 841 and runs after the one `stop:` task of Case 846 for every install by hand, on the person's word.
>   - Taken: the push stands in this Case, beside Case 847 and after it, since Case 847 already has a decision line; Case 847 stays as it is.

> **given:**
> `estimate-sprint-plugin-ci-writes-a-clean-branch`: the Estimate of the run on a tag, its Criterion kept.
> **＋** `.github/workflows/prod.yml`: the workflow that a push of a tag `prod-*` starts.
> **＋** `rule-clean-branch`: the rule of the workflow that writes `prod`, and its refusal of a draft page with `core: true`.
> **＋** `rule-where-to-stop`: the rule that makes a push to a remote a stop.
> **＋** `.claude/skills/work/SKILL.md`: Work Mode, which runs the tasks in the order of the Spec.

> **when:**
> In Work Mode of this session, after the install readings by hand, on the person's word at a `stop:` task, the owner pushes the tag `prod-0.2.0` to the repository of the project on GitHub, and `.github/workflows/prod.yml` runs on the tagged commit.

> **then:**
> The push of the tag starts the run of `.github/workflows/prod.yml` on the tagged commit.
> **－** While a page with `core: true` stands `draft`, the run fails and writes nothing to `prod`, as `rule-clean-branch` sets it.
> **－** The tag stays local until the person's word, and when the person says no at the stop, the push is left to a Case of a later session.

```then
update:
- slug: estimate-sprint-plugin-ci-writes-a-clean-branch
  change: the push of the tag prod-0.2.0 runs after the install readings, on the person's word; the Criterion stands, and the reading waits for a run that writes prod
```

```tasks
- [x] update `estimate-sprint-plugin-ci-writes-a-clean-branch`
- [x] stop: on the person's word, `git push origin prod-0.2.0`; then `gh run list --workflow prod.yml` and `gh run view` of the run it starts: it fails at the step that builds the clean version, on the draft pages with `core: true`, and `git ls-remote origin prod` shows no new commit; the result goes into the handoff.
```

## Deferred

## Case 848 — The root pytest settings put off

> **context:**
> The person put off the items left open at the close of Plan Mode of session 0104. The root `pyproject.toml` still holds the pytest settings, the marker `live` and `addopts = '-m "not live"'`, beside `.guppi/pyproject.toml`, as the brief of the librarian of session 1959 reports. No Case decides whether the root file keeps them until a Case removes it.

> **problem:**
> No Case of this session decides whether the root `pyproject.toml` keeps the pytest settings beside `.guppi/pyproject.toml`.

```then
defer:
  - slug: rule-guppi-package
    type: rule
    purpose: "Whether the root pyproject.toml keeps the pytest settings beside .guppi/pyproject.toml until the Case that removes it; put off at the close of Plan Mode of session 0104"
```

## Case 849 — The harness pipeline reading put off again

> **context:**
> The person put off the items left open at the close of Plan Mode of session 0104. `estimate-harness-pipeline` failed unread at the Retro of session 1739 and was put off by case 833; its `method` still names no moment after the librarian's run that writes the text it reads, and `guppi check` exits 1 on 14 lines by the brief of session 1959.

> **problem:**
> No Case of this session gives `estimate-harness-pipeline` a reading moment after the librarian's run.

```then
defer:
  - slug: estimate-harness-pipeline
    type: estimate
    purpose: "Failed unread at Retro of session 1739; its method names no moment after the librarian's run that writes the text it reads; put off again at the close of Plan Mode of session 0104"
```
