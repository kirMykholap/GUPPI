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

> **tasks:**
> - [ ] update `rule-clean-branch`
>   - old: `which the clean version does not hold (case 816).`
>   - new: `` which the clean version does not hold (case 816). It also writes each `passed` Estimate whose target page it writes, with `core: true` written into its copy and a `## Result` of one line, the date of its last reading and that it passed in the repository of GUPPI; no Estimate of this repository carries `core`, an Estimate that is `pending` or `failed` stays here until its reading passes, and one whose `method` names a target of the `Makefile` stays here until a Case moves it to pytest (case 822). ``
>   - change: `guppi ship writes each passed Estimate of a page it writes, with core: true and a Result of one line, but one whose method names a make target`
> - [ ] update `rule-estimates-schema`
>   - old: `` optional; `true`. The page ships in the clean version of GUPPI that `guppi ship` writes for the branch `prod`; a page without it stays in this repository only. Set by a Case, never by hand (case 804). ``
>   - new: `` optional; `true`. It stands only in the clean version of GUPPI that `guppi ship` writes: `guppi ship` writes it into the copy of each `passed` Estimate whose target page carries `core: true` and whose `method` names no `make` target, and lint reads it there; no Estimate of the repository that builds that version carries it (cases 804, 822). ``
>   - change: `the field core of an Estimate is written by guppi ship into the copy of each passed Estimate of a shipped page`
> - [ ] update `entity-sprint-plugin`
>   - change: `the question put off by decision-case-805 is decided by case 822: the passed Estimates of the shipped pages ship, and the tests ship`
> - [ ] create `estimate-clean-branch-ships-the-passed-estimates`
>   - ref: `rule-clean-branch`
>   - kind: `QA`
>   - purpose: `Whether guppi ship writes each passed Estimate of a page it writes, with core: true and a Result of one line, and no Estimate that is pending or failed, whose target it does not write, or whose method names a make target`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_ship.py -k estimate`
>   - tags: `[ci, plugin]`
> - [ ] `.guppi/guppi/ship.py`: `plan` takes each Estimate whose `status` is `passed`, whose target, read by `slug_of` of `.guppi/guppi/pages.py`, is a page with `core: true` that it writes, and whose `method` holds no match of `MAKE_TARGET` of `.guppi/guppi/lint.py`, imported; `shipped_page` writes `core: true` into such an Estimate and its `## Result` as one line, the date of `checked` and that it passed in the repository of GUPPI; the docstring says so.
> - [ ] `.guppi/tests/test_ship.py`: the sample tree holds a `passed`, a `pending` and a `failed` Estimate of a page with `core: true`, a `passed` one whose `method` names `make test-x`, and a `passed` Estimate of a page without it; the copy holds the first alone, with `core: true`, `origin: guppi` and a Result of one line, and the `estimates` of its target list it alone; `guppi lint` over the copy gives no finding on its `origin`; the names of these tests hold `estimate`.
> - [ ] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`
> - [ ] read `estimate-clean-branch-ships-the-passed-estimates`

> **ratification:**
> ```
> - decision[case 822.1][update][rule-clean-branch]{ref:rule-clean-branch}{supersedes:case 821}{supersedes:case 821.1}{supersedes:case 821.2}{supersedes:case 821.3}{supersedes:case 821.4}{supersedes:case 821.5}{supersedes:case 821.6}{supersedes:case 821.7}
> - decision[case 822.1][update][rule-estimates-schema]{ref:rule-estimates-schema}
> - decision[case 822.1][update][entity-sprint-plugin]{ref:entity-sprint-plugin}{supersedes:case 805}
> - decision[case 822.1][create][estimate-clean-branch-ships-the-passed-estimates]{ref:rule-clean-branch}{tags:ci,plugin}
> ```

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

> **tasks:**
> - [ ] update `rule-clean-branch`
>   - old: `` but not its tests `.guppi/tests/` or its Python environment `.guppi/.venv/`; ``
>   - new: `` with its tests `.guppi/tests/` but `.guppi/tests/test_ship.py`, the tests of the command `ship`, and not its Python environment `.guppi/.venv/`; ``
>   - old: `and it judges no code outside them.`
>   - new: `` and it judges no code outside them. In a test file under `.guppi/tests/` it cleans and judges only the comments and the docstrings: each other string is a sample, as a code span of a page is, so a case id in the data of a test is neither removed nor judged (case 822). ``
>   - change: `guppi ship writes the tests but those of ship, and in a test file it cleans and judges only the comments and the docstrings`
> - [ ] create `estimate-clean-branch-ships-the-tests`
>   - ref: `rule-clean-branch`
>   - kind: `QA`
>   - purpose: `Whether guppi ship writes the tests but those of the command ship, cleans and judges only their comments and docstrings, keeps their other strings as samples, and whether the tests pass in the clean version`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_ship.py -k tests; by hand, after the librarian's run of this change: uv run --project .guppi guppi ship --allow-draft into an empty temporary folder, then uv run --project .guppi pytest .guppi/tests in that folder, read against the Criterion`
>   - tags: `[plugin, tests]`
> - [ ] `.guppi/guppi/pointers.py`: beside `masked`, one function sets aside as samples the strings of a Python file that are not docstrings, read by `tokenize`; `outside` and the cleaning take it for a file under `.guppi/tests/`; the docstring says so.
> - [ ] `.guppi/guppi/ship.py`: the copy and `--check` take the files under `.guppi/tests/` but `.guppi/tests/test_ship.py`, and judge and clean them through that function; the docstring says so.
> - [ ] `.guppi/tests/`: each pointer outside a bracket in a comment or a docstring stands in a bracket of its own at the end of its sentence, and each bare case number there gets the word `case`, so that `guppi ship --check` prints no line on them; a test that needs the `Makefile`, `.github/workflows/prod.yml` or the module `guppi.ship` is skipped where it is missing.
> - [ ] `.guppi/tests/test_ship.py`: the sample tree holds a test file with a pointer in a bracket in a comment, a sample ledger line and a bracket with a pointer in a string, and a file `.guppi/tests/test_ship.py`; the copy holds the first without the bracket of the comment and with both strings unchanged, and no `.guppi/tests/test_ship.py`; `--check` prints a line for a pointer outside a bracket in a comment of a test and none for one in a string; the names of these tests hold `tests`.
> - [ ] read `estimate-clean-branch-ships-the-tests`

> **ratification:**
> ```
> - decision[case 822.2][update][rule-clean-branch]{ref:rule-clean-branch}
> - decision[case 822.2][create][estimate-clean-branch-ships-the-tests]{ref:rule-clean-branch}{tags:plugin,tests}
> ```

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

> **tasks:**
> - [ ] update `rule-clean-branch`
>   - old: `` It gives each page `origin: guppi`, `sprint: guppi`, ``
>   - new: `` In place of the session files of this project it writes skeletons, so the first `/hi` of a project that installs GUPPI finds each file it loads: `vault/wiki/sprint.md` in the closed form of the sprint `guppi`, so that `/hi` starts `/sprint-open`; `vault/wiki/backlog.md` and `vault/wiki/glossary.md` as `guppi backlog` and `guppi glossary` write them over the clean version; a `vault/wiki/brief.md` whose Next session opens its Cases with the line that opens the next sprint; and a `vault/wiki/log.md` that holds its heading alone (case 822). It gives each page `origin: guppi`, `sprint: guppi`, ``
>   - change: `guppi ship writes sprint.md, backlog.md, brief.md, glossary.md and log.md as skeletons`
> - [ ] update `rule-plugin-install`
>   - old: `Which files a new project gets waits for a Case of its own.`
>   - new: `` What a new project gets beside the pages with `core: true` — the tests, the session files as skeletons and the CI of its checks — is set in [[rule-clean-branch]] (case 822). ``
>   - change: `what a new project gets is set in rule-clean-branch`
> - [ ] create `estimate-clean-branch-writes-the-session-files`
>   - ref: `rule-clean-branch`
>   - kind: `QA`
>   - purpose: `Whether guppi ship writes sprint.md in the closed form of the sprint guppi, backlog.md and glossary.md by their writers, a brief.md that opens the next sprint and a log.md with its heading alone, so that the checks of those files pass and the first /hi of a new project starts /sprint-open`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_ship.py -k skeleton; by hand, after the librarian's run of this change: in an empty project, guppi installed from a copy that uv run --project .guppi guppi ship --allow-draft wrote into a local folder, /guppi:install typed, Claude Code reopened and /hi typed, read against the Criterion`
>   - tags: `[plugin, ci]`
> - [ ] `.guppi/guppi/ship.py`: the copy writes `vault/wiki/sprint.md` by `closed_form` of `.guppi/guppi/sprint.py` for `guppi`, `vault/wiki/backlog.md` and `vault/wiki/glossary.md` by `render` of `.guppi/guppi/backlog.py` and of `.guppi/guppi/glossary.py` over the clean folder, and `vault/wiki/brief.md` and `vault/wiki/log.md` from two fixed texts in this module; no copy of a judgment of those writers stands here; the docstring says so.
> - [ ] `.guppi/tests/test_ship.py`: the copy of the sample tree holds the five files; `sprint.md` equals `closed_form("guppi")`; `guppi sprint --check`, `guppi backlog --check` and `guppi glossary --check` over the copy print nothing and exit 0; `brief.md` opens its Cases with the line of the next sprint; the names of these tests hold `skeleton`.
> - [ ] read `estimate-clean-branch-writes-the-session-files`

> **ratification:**
> ```
> - decision[case 822.3][update][rule-clean-branch]{ref:rule-clean-branch}
> - decision[case 822.3][update][rule-plugin-install]{ref:rule-plugin-install}
> - decision[case 822.3][create][estimate-clean-branch-writes-the-session-files]{ref:rule-clean-branch}{tags:plugin,ci}
> ```

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

> **tasks:**
> - [ ] update `rule-clean-branch`
>   - old: `` It writes any other `[[…]]` link to a page or a file it does not write as the slug in a code span. ``
>   - new: `` It writes any other `[[…]]` link to a page or a file it does not write as the slug in a code span. In the Render of `rule-claude-md` and in `CLAUDE.md` that it writes, it puts the heading `# Project` and the line `Project description: not set yet.` between the lines `<!-- project-description -->` and `<!-- /project-description -->`, in place of the heading and the description of GUPPI, which the install Case of `rule-morph` replaces with the description of the project (case 822). ``
>   - change: `guppi ship writes a blank description of the project into rule-claude-md and CLAUDE.md`
> - [ ] create `estimate-clean-branch-ships-a-blank-project-description`
>   - ref: `rule-clean-branch`
>   - kind: `QA`
>   - purpose: `Whether guppi ship writes, between the marker lines of the description in rule-claude-md and CLAUDE.md, a heading and a line that says the description is not set yet, and leaves every other line and the render check of the copy as they are`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_ship.py -k description`
>   - tags: `[plugin, render]`
> - [ ] `.guppi/guppi/ship.py`: one function writes the heading `# Project`, a blank line and `Project description: not set yet.` between `<!-- project-description -->` and `<!-- /project-description -->` in the Render of `rule-claude-md` and in `CLAUDE.md` that the copy holds; the docstring says so.
> - [ ] `.guppi/tests/test_ship.py`: the sample tree holds a `rule-claude-md` with `core: true` and its `CLAUDE.md`, both with the block; the copy holds the placeholder in both, every other line unchanged, and `guppi render --check` over the copy exits 0; the names of these tests hold `description`.
> - [ ] read `estimate-clean-branch-ships-a-blank-project-description`

> **ratification:**
> ```
> - decision[case 822.4][update][rule-clean-branch]{ref:rule-clean-branch}
> - decision[case 822.4][create][estimate-clean-branch-ships-a-blank-project-description]{ref:rule-clean-branch}{tags:plugin,render}
> ```

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

> **tasks:**
> - [ ] update `rule-claude-md`
>   - old: `(cases 272, 273.3, 288.3, 595).`
>   - new: `` (cases 272, 273.3, 288.3, 595). The heading and the description of the project stand between the lines `<!-- project-description -->` and `<!-- /project-description -->`: in the clean version of GUPPI a heading and a line that says the description is not set yet stand there, until the install Case of a project writes its own description (case 822). ``
>   - sections.Render:
>     ````
>     <!-- rule-claude-md -->
>     <!-- project-description -->
>     # GUPPI
>
>     A Claude Code harness governed by ratified decisions, and the Obsidian vault it compiles into.
>     <!-- /project-description -->
>
>     The vault is `vault/`; its terms are `vault/wiki/glossary.md`. A working session opens with `/hi`.
>
>     <!-- rule-language -->
>
>     <!-- rule-agent-writing -->
>
>     <!-- rule-one-judgment-one-implementation -->
>     <!-- /rule-claude-md -->
>     ````
>   - change: `the heading and the description of the project stand between marker lines of their own`
> - [ ] update `estimate-claude-md-rendered`
>   - set:
>     ```
>     status: pending
>     method: "by hand, after the librarian's run of this change: uv run --project .guppi guppi render --check, and CLAUDE.md as the file holds it and as the session of that run loads it, read against the Criterion"
>     ```
>   - change: `the Criterion replaced whole — the heading and the description stand between marker lines of their own`
> - [ ] `uv run guppi render`: `CLAUDE.md`
> - [ ] read `estimate-claude-md-rendered`

> **ratification:**
> ```
> - decision[case 822.5][update][rule-claude-md]{ref:rule-claude-md}
> - decision[case 822.5][update][estimate-claude-md-rendered]{ref:rule-claude-md}
> ```

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

> **tasks:**
> - [ ] update `rule-clean-branch`
>   - old: `` neither carries `core`, and `.github/` is not part of the clean version (case 804). ``
>   - new: `` neither carries `core`. Of `.github/` the clean version holds only `.github/workflows/checks.yml`, the CI that runs the tests, the vault checks and the style check of a project, judged and cleaned like each other file it writes, and `guppi ship --check` judges it in place (cases 804, 822). ``
>   - change: `the clean version holds .github/workflows/checks.yml and no other file of .github/`
> - [ ] create `estimate-clean-branch-ships-the-checks-workflow`
>   - ref: `rule-clean-branch`
>   - kind: `QA`
>   - purpose: `Whether guppi ship writes .github/workflows/checks.yml, judged and cleaned, and no other file of .github/, and whether --check judges it in place`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_ship.py -k checks_workflow`
>   - tags: `[ci, plugin]`
> - [ ] `.guppi/guppi/ship.py`: the copy and `--check` take `.github/workflows/checks.yml` and no other file of `.github/`; the docstring says so.
> - [ ] `.github/workflows/checks.yml`: the comment at the top names no page that the clean version does not hold, such as `rule-github-repository`, and no `Makefile`.
> - [ ] `.guppi/tests/test_ship.py`: the sample tree holds `.github/workflows/checks.yml` with a pointer in a bracket of its comment and `.github/workflows/prod.yml`; the copy holds the first without the bracket and not the second; `--check` prints a line for a pointer outside a bracket in it; the names of these tests hold `checks_workflow`.
> - [ ] read `estimate-clean-branch-ships-the-checks-workflow`

> **ratification:**
> ```
> - decision[case 822.6][update][rule-clean-branch]{ref:rule-clean-branch}
> - decision[case 822.6][create][estimate-clean-branch-ships-the-checks-workflow]{ref:rule-clean-branch}{tags:ci,plugin}
> ```

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

> **tasks:**
> - [ ] update `entity-guppi`
>   - set:
>     ```
>     purpose: "GUPPI — a Claude Code harness governed by ratified decisions, and the vault it keeps; its parts the sprint and the glossary, and in the repository of GUPPI also that repository on GitHub"
>     ```
>   - sections.Purpose:
>     ```
>     GUPPI: a Claude Code harness governed by ratified decisions, and the Obsidian vault it compiles into. Its parts are the sprint as a kind (`entity-sprint`) and the glossary (`entity-glossary`), the things of the vault that are content, not rules. In the repository of GUPPI itself, a third part is that repository on GitHub, `entity-guppi-repository`, whose rules are its own; the clean version of GUPPI does not hold that page (as set in case 795.1). `rule-harness` is its guard: the tools of the harness kept equal to the pages that describe them. In a project that uses GUPPI, this page stands beside the root of the product and keeps GUPPI's own machinery apart from it (as set in case 306.2).
>     ```
>   - change: `GUPPI is described as a harness and a vault, true in any project that uses it`
> - [ ] update `rule-language`
>   - old: `` rendered into `guppi.toml` — English and Russian in this project (case 476.4; until case 272 the rule was a section of the Render of `rule-claude-md`, a standing condition with no page and no Estimate). ``
>   - new: `` rendered into `guppi.toml` as codes, such as `en` and `ru` (case 476.4; until case 272 the rule was a section of the Render of `rule-claude-md`, a standing condition with no page and no Estimate). ``
>   - old: `A Case is discussed in Russian and read in English, whole,`
>   - new: `A Case is discussed in the chat language and read in the documentation language, whole,`
>   - change: `the Purpose names the two languages by their role`
> - [ ] update `rule-case-build`
>   - old: `with a short Russian text ([[rule-orchestration]])`
>   - new: `with a short text in the chat language ([[rule-orchestration]])`
>   - change: `the Purpose names the language of the chat by its role`
> - [ ] create `estimate-clean-branch-ships-neutral-texts`
>   - ref: `rule-clean-branch`
>   - kind: `QA`
>   - purpose: `Whether the rules, the entities and CLAUDE.md of the clean version describe GUPPI and the languages in words that hold in any project and hold no other sentence true only in the repository of GUPPI, and which sentences of the shipped Estimates hold only there`
>   - method: `by hand, after the librarian's run of this change: uv run --project .guppi guppi ship --allow-draft into an empty temporary folder, and the pages and the files it wrote read against the Criterion, each sentence that holds only in the repository of GUPPI listed in the estimate line`
>   - tags: `[plugin, ci]`
> - [ ] read `estimate-clean-branch-ships-neutral-texts`

> **ratification:**
> ```
> - decision[case 822.7][update][entity-guppi]{ref:entity-guppi}
> - decision[case 822.7][update][rule-language]{ref:rule-language}
> - decision[case 822.7][update][rule-case-build]{ref:rule-case-build}
> - decision[case 822.7][create][estimate-clean-branch-ships-neutral-texts]{ref:rule-clean-branch}{tags:plugin,ci}
> ```

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

> **tasks:**
> - [ ] update `rule-clean-branch`
>   - old: `` `guppi ship --check` reads no tag (case 816). ``
>   - new: `` `guppi ship --check` reads no tag (case 816). While a rule or an entity with `core: true` stands `draft`, `guppi ship <folder>` prints one line for each such page, writes nothing and exits 1, so the workflow writes nothing to `prod`; with the option `--allow-draft` it writes the clean version into the folder all the same and prints those lines, which set no exit code, for an install by hand from that folder, which is where a check that needs an install reads it, and the workflow never passes that option. `guppi ship --check` does not judge the status of a page, and `guppi lint` reports each such page where the module of the command `ship` stands; both judge it by `is_draft_core` of `.guppi/guppi/pages.py`. A draft page that a new project can go without loses `core` until it is `built` (case 822). ``
>   - change: `guppi ship builds no clean version while a page with core: true is draft, but into a folder with --allow-draft`
> - [ ] update `rule-skill-merge-main`
>   - set:
>     ```
>     core: null
>     ```
>   - change: `core taken off while the page is draft; a Case gives it back once it is built`
> - [ ] update `rule-skill-pr-review`
>   - set:
>     ```
>     core: null
>     ```
>   - change: `core taken off while the page is draft; a Case gives it back once it is built`
> - [ ] create `estimate-clean-branch-refuses-a-draft-core-page`
>   - ref: `rule-clean-branch`
>   - kind: `QA`
>   - purpose: `Whether guppi ship writes nothing and exits 1 while a page with core: true is draft, and writes the copy with --allow-draft, judging such a page by is_draft_core`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_ship.py -k draft_core`
>   - tags: `[ci, plugin]`
> - [ ] `.guppi/guppi/pages.py`: `is_draft_core` judges a rule or an entity with `core: true` whose `status` is `draft`, and `ship_stands` judges whether the module `guppi.ship` can be found; the docstrings name `guppi ship`, `guppi lint`, `guppi check` and the list of commands, which import them.
> - [ ] `.guppi/guppi/ship.py`: before it writes, the build prints `ship: <page>: a page with core: true that is draft` for each page that `is_draft_core` accepts, writes nothing and exits 1; with `--allow-draft` it writes the copy and prints those lines with no exit code; `--check` does not judge the status; the docstring says so.
> - [ ] `.guppi/tests/test_ship.py`: a sample tree with a draft page with `core: true` exits 1 with its line and writes nothing; with `--allow-draft` it writes the copy and exits 0; `--check` prints no line on it; the names of these tests hold `draft_core`.
> - [ ] read `estimate-clean-branch-refuses-a-draft-core-page`

> **ratification:**
> ```
> - decision[case 822.8][update][rule-clean-branch]{ref:rule-clean-branch}
> - decision[case 822.8][update][rule-skill-merge-main]{ref:rule-skill-merge-main}
> - decision[case 822.8][update][rule-skill-pr-review]{ref:rule-skill-pr-review}
> - decision[case 822.8][create][estimate-clean-branch-refuses-a-draft-core-page]{ref:rule-clean-branch}{tags:ci,plugin}
> ```

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

> **tasks:**
> - [ ] update `rule-lint`
>   - old: `lint runs with the renderer, in no phase of the session.`
>   - new: `` lint runs with the renderer, in no phase of the session. Where the module of the command `ship` stands, as in the repository that builds the clean version of GUPPI, `guppi lint` also reports each rule or entity with `core: true` that is `draft`, since `guppi ship` builds no clean version while one stands; a project that installed GUPPI gets no such line (case 822). ``
>   - change: `lint reports a draft page with core: true where the module of ship stands`
> - [ ] update `estimate-lint-checks-the-statuses`
>   - set:
>     ```
>     status: pending
>     purpose: A status its Estimates do not support, a draft page with core true where the command ship stands, a failed Estimate, a pending Estimate whose reading does not wait for a later moment, and a placeholder are findings of lint
>     method: uv run --project .guppi pytest .guppi/tests/test_lint.py
>     ```
>   - change: `the Criterion replaced whole — a draft page with core: true is a status finding where the module of ship stands`
> - [ ] `.guppi/guppi/lint.py`: a finding of the class `status` for each page that `is_draft_core` accepts, only where `ship_stands` finds the module, both of `.guppi/guppi/pages.py`, imported; the docstring says so.
> - [ ] `.guppi/guppi/check.py` and `.guppi/guppi/cli.py`: each judges whether the module of `ship` stands by `ship_stands` of `.guppi/guppi/pages.py`, imported, and holds no copy of it.
> - [ ] `.guppi/tests/test_lint.py`: a draft page with `core: true` and no Estimate gives the finding where the module `guppi.ship` stands and none where it is missing; a test asserts that `lint`, `check` and `cli` call the same `ship_stands`, and that `lint` and `ship` call the same `is_draft_core`; the names of these tests hold `draft_core`.
> - [ ] read `estimate-lint-checks-the-statuses`

> **ratification:**
> ```
> - decision[case 822.9][update][rule-lint]{ref:rule-lint}
> - decision[case 822.9][update][estimate-lint-checks-the-statuses]{ref:rule-lint}
> ```
