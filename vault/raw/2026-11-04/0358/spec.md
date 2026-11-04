<!-- approved 05:47:06 · session 76379bf1 -->

# Session 0358 — the sprint plugin

## Case 1025 — The root ignore file counts for a new file

> **context:**
> When a Case adds a file that is no page, `rule-case-build` tells `case-guppi` to read each `.gitignore` in a folder that holds the new file, since git may leave the file out. The words do not say how far up the folders go. The one-time check `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` read the build of Case 1012, which added `.guppi/guppi/frontierguard.py` and `.guppi/tests/test_frontierguard.py`. By its own Result, that build read `.guppi/.gitignore` and not the root `.gitignore`, and the agent of session 1825 passed the check on its own judgment that the root is no folder that holds the files. The person judged otherwise: the root holds every file of the repository, git applies its `.gitignore` to every file under it, and the build already counted `.guppi/`, two levels up. Case 1025.1 sets the one-time check `failed` by the person's decision. Its Criterion is written back unchanged. A reading of the root `.gitignore` in this build found that no pattern matches either file, so nothing was lost; `git check-ignore` was not run here. Case 1025.2 makes the rule say that the folders go up to the root in each of its three folder clauses, and replaces the Criterion of `estimate-case-build-reads-the-readers-of-a-new-files-folder` with the same words. Its `purpose` and its `method` are set anew: the `method` read `.claude/agents/case-guppi.md`, which changes only at the render of the librarian's run, so it now reads the new Render in the Spec at Retro, in the form that other Estimates of `rule-case-build` use. The governing rule is `rule-case-build`. Of the Estimates that `rule-case-build` lists, only `estimate-case-build-reads-the-readers-of-a-new-files-folder` has a `purpose` that speaks of ignore files. At the finding 1.4 of `/pre-spec`, the person chose that all three folder clauses of that paragraph go up to the root: the path search, the ignore files and the readers. In round 3 the person chose that the path search stops below the root, since the root has no path to search for; the ignore files and the readers take the root in. Two readers that take every file of the root stand today: the line `* text=auto eol=lf` of `.gitattributes`, and the key `style` of `guppi.toml`, which runs `ruff check .` and `ruff format --check .`; both were read for this Case. The new clause of the readers names neither one, since a builder reads them for its own new file. `entity-sprint-plugin` stands: its Purpose says that an Estimate of the page that has not passed by the close goes to the archive with the page, its status kept. `judge_estimates` and `settled` of `.guppi/guppi/sprint_close.py`, read whole, take a `failed` Estimate of the sprint page as settled at the close. The Milestones of that page say that the clean branch is blocked by a page with `core: true` whose Estimate is `failed`, and `entity-sprint-plugin` carries no `core: true`. The new Criterion does not carry the lines on the path search, the ignore files and the readers of a folder that holds the new file: its lines on each folder up to the root replace them, as the person chose. `estimate-prespec-finds-a-reader-of-a-new-files-folder` stands: its Criterion asks whether the `context` names each search and reading that `.claude/agents/case-guppi.md` sets, so it follows the new sentence with no change of its words. Of the other files that the note of the check listed as naming `rule-case-build`, `case-guppi.md` or `case-guppi`, none speaks of ignore files by its purpose line or its path, and the Grep below finds no other text on them. A Grep for `` ignore files? of git|\.gitignore` in a folder|\.gitignore` and each reader `` over `{vault/wiki,.claude,.guppi/guppi}/**` from the root printed `.claude/agents/case-guppi.md`, `vault/wiki/estimates/estimate-case-build-reads-the-readers-of-a-new-files-folder.md`, `vault/wiki/estimates/estimate-sprint-plugin-frontierguard-build-read-its-folders-readers.md` and `vault/wiki/rules/rule-case-build.md`, each one in the Case. A Grep of `.guppi/tests/` for `case-guppi\.md|rule-case-build` printed `test_casecheck.py`, which asserts only the agent name that `carried_names` takes from the path, and `test_guppi_package.py`, whose docstring names the rule; neither reads the changed sentence. A Grep of the session's ledger for `lesson\[error\]|\{addresses:` printed nothing, so no lesson is marked.

> **problem:**
> The rule does not say whether the root folder counts among the folders that hold a new file. A one-time check passed on the agent's own judgment that it does not, and the person judges that it does.

> **recommend:**
> - **Does the root `.gitignore` count as an ignore file of a folder that holds the new files**
>   - Recommended: (a) yes, the root counts; the check did not hold, and the Estimate is set `failed` by the person's decision.
>   - Answer: agreed, (a).
> - **Does the rule say that the root counts**
>   - Recommended: (a) yes; the rule names every folder from the folder of the new file up to the root, and the Criterion of the lasting check is replaced with the same words.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at the finding 1.4 of `/pre-spec`, the person chose that the path search and the readers clause go up to the root as well, the root included, and not the ignore files alone.
>   - Taken: Case 1025.2 replaces all three folder clauses of `rule-case-build` and the lines of its Criterion on them.
> - **What the path search does at the root**
>   - Recommended: (a) the path search stops below the root, since the root has no path; the ignore files and the readers take the root in.
>   - Answer: agreed, (a).

### Case 1025.1 — The one-time check of the build of Case 1012 failed

> **given:**
> `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers`: the one-time check of the build, set `failed`.
> **＋** `vault/archive/plugin/2026-11-02/2155/raw/cases/case-1012.md`: the case file of the build it judges.
> **＋** `.gitignore`: the root ignore file that the build did not read.
> **＋** `rule-case-build`: the rule whose words the check judges.

> **when:**
> The person judges `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` against the build of `vault/archive/plugin/2026-11-02/2155/raw/cases/case-1012.md`.

> **then:**
> `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` stands `failed` by the person's decision.
> **＋** Its Result says that the root `.gitignore` is an ignore file of a folder that holds the new files, and that the build did not read it.
> **＋** Its Result says that no pattern of the root `.gitignore` matches either new file.
> **－** Its Criterion does not change.

```then
update:
- slug: estimate-sprint-plugin-frontierguard-build-read-its-folders-readers
  set:
    status: failed
    checked: 2026-11-04
  sections:
    Criterion: |-
      When:
      The agent transcript `~/.claude/projects/c--PROJECTS-GUPPI/c818d971-be31-4157-ab5d-802bd511827f/subagents/agent-aaf1016f261a07c9b.jsonl` of the `case-guppi` that built the Case adding `.guppi/guppi/frontierguard.py` and `.guppi/tests/test_frontierguard.py`, and its case file `vault/archive/plugin/2026-11-02/2155/raw/cases/case-1012.md`, are read once against this Criterion.

      Then:
      That build searched `.guppi/guppi/`, `.claude/` and `vault/wiki/rules/` for the path of each folder that holds `.guppi/guppi/frontierguard.py` or `.guppi/tests/test_frontierguard.py`.
      **＋** It searched `.guppi/guppi/` and `.guppi/tests/` for the calls that walk a folder, such as `os.walk`, `rglob`, `glob` and `iterdir`.
      **＋** It read each ignore file of git in a folder that holds those files.
      **＋** It read each reader that takes every file of such a folder.
      **＋** Each reader that those files make wrong entered the Case of `vault/archive/plugin/2026-11-02/2155/raw/cases/case-1012.md`, or its `context` names it and says why it stands.
      **＋** That `context` names each of those searches, with its pattern, its paths and each file it printed or the count it printed, and each ignore file of git and each reader it read, with whether those files make it wrong.
    Result: |-
      2026-11-04, the person's decision, case 1025.1: the root folder holds both new files and git applies the root .gitignore to every file under it, so the root .gitignore is an ignore file of a folder that holds them, and the build did not read it; a reading of its lines in session 0358 found no pattern that matches either file.

      2026-11-03, Work Mode of session 1825, ~/.claude/projects/c--PROJECTS-GUPPI/c818d971-be31-4157-ab5d-802bd511827f/subagents/agent-aaf1016f261a07c9b.jsonl (606 lines, 2 matches of Build Case 1012) listed by its tool calls, and vault/archive/plugin/2026-11-02/2155/raw/cases/case-1012.md read: the build ran Greps of \.guppi/guppi and \.guppi/tests over {.guppi/guppi,.claude,vault/wiki/rules}/** (counts 81 and 52) and of the bare names guppi/ and tests/ (47 and 38), Greps of os\.walk|rglob\(|\.glob\(|iterdir\( over .guppi/guppi and .guppi/tests (29 files), read .guppi/.gitignore, ship.py and casecheck.py (tree_files, named_files), and its context (lines 8 and 10) names each search with its pattern, paths and count, each reader with why it stands; .guppi/guppi/ and .guppi/tests/ hold no .gitignore, and the root .gitignore was not read, judged here as no folder that holds the new files, git check-ignore printing neither file
  change: 'failed by the person''s decision: the root .gitignore is an ignore file of a folder that holds the new files, and the build did not read it'
```

```tasks
- [ ] update `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers`
```

### Case 1025.2 — The rule names each folder up to the root

> **given:**
> `rule-case-build`: the Render sentence on the searches and readings a build makes for the folders of a new file.
> **＋** `.claude/agents/case-guppi.md`: the file rendered from `rule-case-build`.
> **＋** `estimate-case-build-reads-the-readers-of-a-new-files-folder`: its Criterion is replaced whole.
> **＋** `vault/wiki/`: the vault, whose Rule pages the build searches and whose pages need no such search.
> **＋** `.guppi/guppi/`: the code the build searches for the paths and for the calls that walk a folder.
> **＋** `.guppi/tests/`: the tests the build searches for the calls that walk a folder.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case with a task that adds a file that is no page of `vault/wiki/`, and is about to answer with its summary.

> **then:**
> It searches `.guppi/guppi/`, `.claude/` and the Rule pages of `vault/wiki/` for the path and the bare name of each folder from the folder of the new file up to the root of the repository.
> **＋** It searches `.guppi/guppi/` and `.guppi/tests/` for the calls that walk a folder, such as `os.walk`, `rglob`, `glob` and `iterdir`.
> **＋** It reads each ignore file of git in each folder from the folder of the new file up to the root of the repository, the root included.
> **＋** It reads each reader that takes every file of a folder from the folder of the new file up to the root of the repository, the root included.
> **＋** Each reader that the new file makes wrong enters the Case, or the `context` of the Case names it and says why it stands.
> **＋** The `context` of the Case names each of those searches, with its pattern, its paths and each file it printed or the count it printed, and each ignore file of git and each reader it read, with whether the new file makes it wrong.
> **－** The root of the repository, which has no path, gets no search for its path.
> **－** A page that a `create` adds under `vault/wiki/` starts no such search.

```then
update:
- slug: rule-case-build
  replace:
  - old: for the path of each folder that holds it, the bare name of the folder too,
    new: for the path of each folder from the folder of the new file up to the root of the repository, the root left out since it has no path, the bare name of the folder too,
  - old: and read each `.gitignore` in a folder that holds it, since
    new: and read each `.gitignore` in each folder from the folder of the new file up to the root of the repository, the root included, since
  - old: read each reader that takes every file of a folder that holds the new file, such as a walk that copies every file of a folder;
    new: read each reader that takes every file of a folder from the folder of the new file up to the root of the repository, the root included, such as a walk that copies every file of a folder;
  change: case-guppi searches and reads for each folder from the folder of a new file up to the root of the repository, the root left out of the path search
- slug: estimate-case-build-reads-the-readers-of-a-new-files-folder
  set:
    status: pending
    purpose: Whether case-guppi, when a task of its Case adds a file that is no page, searches for the paths of the folders from its own up to the root of the repository but for the root, and for the calls that walk a folder, reads the ignore file of git and each reader that takes every file of a folder in each folder from its own up to the root, the root included, enters each one the new file makes wrong in the Case or names it in context, and names in context each of those searches and readings
    method: by hand, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec read against the Criterion, recorded in the estimate line
  change: the Criterion replaced whole — the searches and readings for the folders of a new file go up to the root of the repository, the root left out of the path search
```

```tasks
- [ ] update `rule-case-build`
- [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [ ] update `estimate-case-build-reads-the-readers-of-a-new-files-folder`
- [ ] read `estimate-case-build-reads-the-readers-of-a-new-files-folder`
```

## Case 1026 — The install readings of the setup are taken in this session

> **context:**
> The setup of `rule-morph` is built: the first `/hi` after `/guppi:install` starts `/setup` of `rule-skill-setup`, which puts one setup Case before the opening of the first sprint (case 1017). What remains is the readings by hand of its Estimates, which need a person to install the plugin from a copy that `guppi ship --allow-draft` writes into a new project, in a second Claude Code window that the agent cannot open. No session has made that install. Earlier in this session the person ratified Cases 1022, 1023 and 1024, which put off three of those readings; their defers stand only as lines of this session's ledger and would reach the pages and `backlog.md` only at the librarian's run. The person then asked why the work is only put off, and picked this item: one session prepares the copy and three folders, and the person installs into each. By the person's choice this Case takes five readings at one `stop:` task of Work Mode, one sub-case per Estimate, since each reading can fail alone and needs its own fix (`rule-atomicity`): `estimate-morph-sets-up-the-project-at-the-first-hi`, `estimate-morph-takes-in-the-set-aside-files`, `estimate-git-context-offers-git-init`, `estimate-sprint-plugin-installs-as-a-plugin` and `estimate-orchestration-acknowledging-reply`. The precedent is Case 900 of session 0327, which took five install readings from the backlog the same way.
> The readings are not all short. The Criterion of `estimate-morph-sets-up-the-project-at-the-first-hi` reads the settings that the librarian's run of the new project's session writes, so in the empty git project the person takes that session through the setup Case, the opening of its first sprint, Work Mode and the librarian's run; the Criterion of `estimate-morph-takes-in-the-set-aside-files` reads the render at the librarian's run of its session too. In the folder with no git the person answers no, then yes, then types `/hi` a third time, as the method of `estimate-git-context-offers-git-init` sets it. The empty git project also serves `estimate-sprint-plugin-installs-as-a-plugin`, whose Criterion asks for an empty project, and the second part of the method of `estimate-orchestration-acknowledging-reply`, which waits for a setup Case ratified in a new install. Its first part waits for replies written after the render of the sentence that lets a heading keep a term of the harness in English; `vault/wiki/orchestration.md` holds that sentence on its line 82, and this session's ledger holds decision lines of Cases ratified alone and of two Cases ratified at one time, so the replies that acknowledge them stand in this session's transcript.
> By the person's choice the put-offs of Cases 1022, 1023 and 1024 are retired: a reading taken today cannot also stand put off. Each sub-case names its Estimate by an `update` with only `change` and carries one `{supersedes:case N}` mark for the Case that put it off, as `case-schema.md` sets it for a taken-up defer, so Cases 1022, 1023 and 1024 leave the Spec of this session. `estimate-orchestration-acknowledging-reply` carries `deferred_by: ["[[decision-case-1014]]"]`, so Case 1026.5 carries `{supersedes:case 1014}`. `estimate-plugin-install-sets-aside-the-files-of-the-project` stays put off by Case 949: its method needs two more projects, one started with uv offline, and the person chose not to add them.
> Each sub-case is checked by its own Estimate, and its `when` and `then` are the Criterion of that Estimate word for word. The `update` sets no `status` and no Criterion, so by `case-schema.md` the Criterion and the `pending` status stand until the reading, which the main agent records as an estimate line from the person's report and the files of each folder. A reading that fails stands `failed`, and a Case of a later session fixes its cause.
> The copy comes from `run` of `.guppi/guppi/ship.py`, read with `parser`: it refuses a folder that is not empty, prints the line of each draft page with `core: true` and goes on with `--allow-draft`, and stops with the line `ship: no tag prod-x.y.z in the history of HEAD; nothing written` when `version` finds no such tag. A Glob of `.git/refs/tags/prod-*` printed `prod-1`, `prod-2`, `prod-0.2.0` and `prod-0.3.0`; `VERSION_TAG` of `.guppi/guppi/ship.py` matches only the form `prod-x.y.z`, so `prod-1` and `prod-2` give no version, and whether `prod-0.2.0` and `prod-0.3.0` stand in the history of HEAD was not checked here, and the task of the copy shows it. Work Mode waits at the `stop:` task for the person's word, as `rule-where-to-stop` sets it.
> The milestone line of `rule-morph` on `entity-sprint-plugin` says that `rule-morph` and `rule-skill-setup` stay `draft` until the readings; `rule-skill-setup` is `built` already, so that part is false. By the person's choice it stands: how the readings end is known only after Work Mode, and the whole line then needs new words, which a later Case writes once. This Case changes no other text of `entity-sprint-plugin`, which Case 1021 put off; Case 1025 of this session touches that page only through its Estimate.
> A Grep of `.guppi/tests/` for `morph-sets-up-the-project|morph-takes-in-the-set-aside|git-context-offers-git-init|sprint-plugin-installs-as-a-plugin|orchestration-acknowledging-reply\b` printed nothing, so no test reads these pages by slug. A Grep of the session's ledger for `lesson\[error\]|\{addresses:` printed nothing, so no lesson is marked.
> The check of this file listed the files that name the changed Estimates, and each stands, since this Case adds only a History line to each Estimate. `rule-git-context` and `rule-orchestration` list them in `estimates` and in History. The Criteria of `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` and `estimate-orchestration-shows-the-frontier-after-a-closed-line` point to the order and the form that `estimate-orchestration-acknowledging-reply` checks, and that Criterion stands. The `method` of `estimate-clean-branch-writes-the-session-files` lets its reading share the copy and the folder of the reading of `estimate-git-context-offers-git-init` at the same commit; this Case does not take that reading. `backlog.md` is written by `guppi backlog` from the pages, so it follows the retired put-offs at the librarian's run. The check also noted that some `then` lines of Cases 1026.4 and 1026.5 share words with lines of Case 1026.1; they stand, since each sub-case copies the Criterion of its own Estimate word for word.

> **problem:**
> The readings of the setup of `rule-morph` and of the install wait for an install by hand that no session has made, and the person chose to take them in this session rather than put them off.

> **recommend:**
> - **What happens to the three put-offs ratified earlier today**
>   - Recommended: (a) retire them in this Case: each decision line that names one of those Estimates carries a mark that retires its put-off.
>   - Answer: agreed, (a); the person accepted every recommendation of the round.
> - **Which checks do the installs take**
>   - Recommended: (b) the four readings, plus the reading of the reply that acknowledges the setup Case, whose put-off is retired too.
>   - Answer: agreed, (b).
> - **How does the pause in Work Mode for the person's installs run**
>   - Recommended: (a) the agent writes a fresh copy and makes the three folders and their files, then one pause at which the person installs into each folder and works there, and the agent reads the transcripts and the files.
>   - Answer: agreed, (a).
> - **Does the milestone line of `rule-morph` change now**
>   - Recommended: (a) leave it; the `context` says why, and a later Case rewrites the line once the readings end.
>   - Answer: agreed, (a).

### Case 1026.1 — The setup at the first /hi is read at the install stop

> **given:**
> `estimate-morph-sets-up-the-project-at-the-first-hi`: its put-off is retired and its reading is taken.
> **＋** `rule-morph`: the setup Case at the first `/hi`.
> **＋** `rule-skill-setup`: the skill `/setup` that builds the setup Case.
> **＋** `rule-plugin-install`: the skill `/guppi:install`.
> **＋** `rule-ledger-write`: the ledger hook.
> **＋** `guppi.toml`: the settings file that holds `setup_done`.
> **＋** `.guppi/guppi/ship.py`: the command that writes the clean copy.
> **＋** `rule-where-to-stop`: the stop before a task that opens with `stop:`.
> **＋** `/sprint-open`: the skill that opens the first sprint after the setup Case.

> **when:**
> In a project where the person installed the plugin `guppi` and typed `/guppi:install`, as `rule-plugin-install` sets it, and whose `guppi.toml` holds `setup_done = false`, the person reopens Claude Code and types `/hi`.

> **then:**
> `/hi` opens the session and starts `/setup` of `rule-skill-setup`, which puts the setup Case of `rule-morph` first, before the opening Case of the first sprint and before the Frontier.
> **＋** The setup Case takes the name of the project's folder of saved transcripts from the path of the project.
> **＋** It asks the person only for the values it cannot find: the language of the repository, the language of the chat, the commands of the keys `test` and `style` of `guppi.toml` and the description of the project.
> **＋** Every value stands in that one setup Case, which the person ratifies or corrects, and the ledger hook of `rule-ledger-write` writes its decision lines though no sprint is open.
> **＋** The reply that acknowledges the setup Case shows no Frontier and ends with the open question on what the first sprint is to build, and on the person's answer `/sprint-open` starts in the same session with that answer.
> **＋** The librarian's run of that session writes the settings by the render of the rule pages that hold them, `guppi.toml`, the description of the project in `CLAUDE.md` and the read rules of the saved transcripts, and `guppi.toml` then holds `setup_done = true`.
> **－** `/guppi:install` is no Case, and the person ratifies nothing at it.
> **－** Between `/guppi:install` and that librarian's run, no settings file changes but by the copy and the setting aside of `/guppi:install` and the render that `/hi` runs.
> **－** The setup step asks for no category set, no name of the main branch and no git remote, reads no code of the project and creates no page for it.
> **－** A project whose `guppi.toml` does not hold `setup_done = false` gets no setup Case at `/hi`.

```then
update:
- slug: estimate-morph-sets-up-the-project-at-the-first-hi
  change: the put-off retired before it was applied; the reading taken at the install stop of Work Mode
```

```tasks
- [ ] update `estimate-morph-sets-up-the-project-at-the-first-hi`
- [x] by hand: `uv run --project .guppi guppi ship --allow-draft <folder>` into an empty temporary folder outside the repository, the catalogue of the installs, in which no command runs.
- [x] by hand: three new folders outside the repository: the first an empty folder with `git init -b main` run in it; the second a folder with `git init -b main` run in it that holds a `CLAUDE.md`, a `.claude/settings.json` with a hook and a `.gitattributes` of its own; the third an empty folder with no git.
- [x] stop: the person adds the catalogue by `/plugin marketplace add <folder>` and installs the plugin by `/plugin install guppi@guppi-marketplace`, then in each of the three folders types `/guppi:install`, reopens Claude Code and types `/hi`: in the first folder the person takes that session through the setup Case, the opening of its first sprint, Work Mode and the librarian's run; in the second the person keeps one part and drops one part of each set-aside file in the setup Case and takes that session to its librarian's run; in the third the person answers no, types `/hi` again and answers yes, then types `/hi` a third time; the person reports, and the agent reads the transcripts under `~/.claude/projects`, the ledgers and the files of each folder, for the readings of Case 1026.
- [ ] read `estimate-morph-sets-up-the-project-at-the-first-hi`
```

### Case 1026.2 — The set-aside files are read at the install stop

> **given:**
> `estimate-morph-takes-in-the-set-aside-files`: its put-off is retired and its reading is taken.
> **＋** `rule-morph`: the setup Case at the first `/hi`.
> **＋** `rule-skill-setup`: the skill `/setup` that builds the setup Case.
> **＋** `rule-plugin-install`: the skill `/guppi:install`, which sets files aside.
> **＋** `guppi-set-aside/`: the folder of the files set aside.
> **＋** `guppi.toml`: the settings file that holds `setup_done`.

> **when:**
> In a project where `/guppi:install`, as `rule-plugin-install` sets it, set aside files of the project under `guppi-set-aside/`, and whose `guppi.toml` holds `setup_done = false`, the person reopens Claude Code and types `/hi`.

> **then:**
> The setup Case of `rule-morph` that `/setup` of `rule-skill-setup` builds shows what each file under `guppi-set-aside/` holds, by its old path.
> **＋** In that one setup Case, the person keeps or drops each part of each file, such as an instruction, a hook or a permission.
> **＋** A kept part goes into the page that writes its file, and the render at the librarian's run of that session writes it into the file.
> **＋** For a file that no page writes, a task of the setup Case writes the kept part into that file, and the Work Mode of the same session runs it.
> **＋** A task of the setup Case deletes `guppi-set-aside/` in that Work Mode.
> **－** A dropped part reaches no file of the project.
> **－** The setup Case creates no page for a kept part.

```then
update:
- slug: estimate-morph-takes-in-the-set-aside-files
  change: the put-off retired before it was applied; the reading taken at the install stop of Work Mode
```

```tasks
- [ ] update `estimate-morph-takes-in-the-set-aside-files`
- [ ] read `estimate-morph-takes-in-the-set-aside-files`
```

### Case 1026.3 — The git init offer is read at the install stop

> **given:**
> `estimate-git-context-offers-git-init`: its put-off is retired and its reading is taken.
> **＋** `rule-git-context`: the git step of `/hi`.
> **＋** `.claude/skills/hi/SKILL.md`: the skill that opens a session.
> **＋** `rule-skill-hi`: sets `/hi`.
> **＋** `rule-skill-sprint-open`: its hook asks for `/sprint-open`.
> **＋** `rule-default-mode`: sets the writes allowed before a ratified Case.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of a session.
> **＋** `/setup`: the skill of the setup Case, started first in a project whose setup is not done.

> **when:**
> The person types `/hi` of `.claude/skills/hi/SKILL.md` in a project folder, and its `Branch:` line, which runs `uv run --project .guppi guppi gitstate` of `rule-git-context`, reads `none: this folder is no git repository`.

> **then:**
> Before `/sprint-open` and before the Frontier, the agent says that GUPPI works only in a git repository and asks the person whether it runs `git init -b main`.
> **＋** On the person's yes, the agent runs `git init -b main`, which Claude Code asks the person to allow, says that the repository is made, and tells the person to type `/hi` again.
> **＋** The next `/hi` prints `main` under `Branch:` and goes on as `rule-skill-hi` sets it: `/setup` first when the hook on `/hi` says that the setup of the project is not done, and `/sprint-open` when the hook of `rule-skill-sprint-open` asks for it.
> **＋** On the person's no, the agent tells the person to type `/hi` again after `git init -b main`.
> **－** After either answer, that `/hi` starts no `/sprint-open` and writes no `raw/<date>/<hi HHMM>/frontier.md`.
> **－** `git init -b main` is the one write before a ratified Case that `rule-default-mode` allows, and `allowed-tools` of `.claude/skills/hi/SKILL.md` does not name it.

```then
update:
- slug: estimate-git-context-offers-git-init
  change: the put-off retired before it was applied; the reading taken at the install stop of Work Mode
```

```tasks
- [ ] update `estimate-git-context-offers-git-init`
- [ ] read `estimate-git-context-offers-git-init`
```

### Case 1026.4 — The install of the plugin is read at the install stop

> **given:**
> `estimate-sprint-plugin-installs-as-a-plugin`: its reading is taken.
> **＋** `entity-sprint-plugin`: the sprint page, its target.
> **＋** `rule-clean-branch`: the clean version that `guppi ship` writes.
> **＋** `rule-plugin-install`: the skill `/guppi:install`.
> **＋** `/plugin marketplace add <folder>`: the command of Claude Code that adds the copy as a catalogue.
> **＋** `/plugin install guppi@guppi-marketplace`: the command of Claude Code that installs the plugin.
> **＋** `/hi`: the skill that opens a session in the project.

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
  change: the reading taken at the install stop of Work Mode, in the empty git project
```

```tasks
- [ ] update `estimate-sprint-plugin-installs-as-a-plugin`
- [ ] read `estimate-sprint-plugin-installs-as-a-plugin`
```

### Case 1026.5 — The acknowledging reply is read in this session and at the install stop

> **given:**
> `estimate-orchestration-acknowledging-reply`: its put-off is retired and its reading is taken.
> **＋** `rule-orchestration`: sets the reply that acknowledges a ratification.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `rule-ledger-write`: the ledger hook.
> **＋** `rule-morph`: the setup Case.
> **＋** `rule-skill-setup`: the skill `/setup` that builds the setup Case.
> **＋** `rule-prespec-onward`: its hook sends the agent on after `/pre-spec`.
> **＋** `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec`: checks the `STOP:` line before the `LEDGER` block.
> **＋** `estimate-ledger-write-holds-a-decision-line-off-the-stored-case`: checks the decision line that the ledger hook holds.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of a session.

> **when:**
> The person ratifies a Case, ratifies again a Case shown again after its ratification, or ratifies in one answer Cases shown together, and the agent writes the reply that acknowledges it, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The reply has four parts, in this order. First, the `LEDGER` block, before which stands nothing but the `STOP:` line that `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` checks. Second, the heading `## Case N — ratified` and a paragraph `Changes:` that says what changes, in one or two sentences. Third, a paragraph `Notes:` with facts that did not enter the Case, left out when there are none. Last, the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist.
> **＋** Each heading and label of the reply stands in the language of the chat that `CLAUDE.md` sets, but for the terms of the harness it holds: the words of the heading `## Case N — ratified` and of the labels `Changes:` and `Notes:` other than such a term stand in that language, not in the English words by which this Criterion names them.
> **＋** In the checklist the closed lines are folded into one line, and the lines put off stand as `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
> **＋** The open `W` lines are folded into one line that lists their ids, and each other open line stands on its own line with a short title.
> **＋** While a line under `## Cases` is open, the question which item is next ends the reply.
> **＋** When none is open before `/pre-spec`, the question whether to go on to `/pre-spec` ends the reply, in the plain form of the question which item is next. The agent calls `/pre-spec` only after the person says to go on. A reply that answers a question of the person instead ends with the same question again.
> **＋** When none is open after `/pre-spec`, the reply ends with the Frontier and asks nothing, and the hook of `rule-prespec-onward` sends the agent on.
> **＋** One reply acknowledges every Case and sub-case ratified in one answer, a Case with its sub-cases or Cases shown together for one ratification: one `LEDGER` block with all their lines, one heading `## Case N — ratified` that names their ids, one paragraph `Changes:`, one Frontier.
> **＋** The reply that acknowledges a re-ratification carries the `LEDGER` block with the decision lines of each Case ratified again, as at its first ratification.
> **＋** No tool call follows the `LEDGER` block in the same reply.
> **－** The reply that acknowledges the setup Case of `rule-morph`, built by `/setup` of `rule-skill-setup`, holds no Frontier and ends with the open question on what the first sprint is to build, and no tool call follows its `LEDGER` block.
> **－** A term of the harness that a heading or a label holds, such as Case or Frontier, may stay in English, untransliterated as `CLAUDE.md` sets it, and the heading of the Frontier may be that term alone, such as `## Frontier`.
> **－** Slugs, paths, the tag of the `LEDGER` block, the ledger lines and the word `STOP:` that opens a reply keep their own words in any language of the chat; the rest of the `STOP:` line stands in the language of the chat.
> **－** The ledger hook of `rule-ledger-write` does not append a repeated decision line a second time.
> **－** When a `Stop` hook other than the ledger hook of `rule-ledger-write` refuses the reply with exit 2, the agent's answer to the refusal is a reply of its own and may call tools. The `LEDGER` block stands written, but for a decision line the ledger hook holds, as `estimate-ledger-write-holds-a-decision-line-off-the-stored-case` sets it.

```then
update:
- slug: estimate-orchestration-acknowledging-reply
  change: the put-off retired; the reading taken from the acknowledging replies of this session and the reply that acknowledges the setup Case in the empty git project of the install stop
```

```tasks
- [ ] update `estimate-orchestration-acknowledging-reply`
- [ ] read `estimate-orchestration-acknowledging-reply`
```

## Case 1028 — A bare case number in the code is named at the write, and the hook stays out of the clean copy

> **context:**
> A pointer to a case in a comment or a docstring under `.guppi/` must stand in a bracket of its own at the end of its sentence, such as `(as set in case 12)`, so that `guppi ship` can remove it whole from the clean version. Today the one check of the live code, `test_the_live_code_holds_no_pointer_outside_a_bracket` of `.guppi/tests/test_ship.py`, runs only inside the full `uv run --project .guppi guppi test` at the end of Work Mode. So the agent learns of a bare case number only there and goes back to fix it. The two children of `insight-ship-live-code-writes-a-case-number-outside-a-bracket` record two such cases: a test comment that held a case number alone, and a sample closer in the docstring of `.guppi/guppi/frontierguard.py` that held a real case number where the placeholder `case N` belonged. The person chose a hook after each Edit, Write or MultiEdit of a file under `.guppi/`. It runs the same judgment over that file and tells the agent at once, by a note beside the tool result, and it refuses nothing. It is written into `rule-clean-branch` beside the live code test and checked by a new Estimate.
>
> This Case replaces Case 1027, which held the hook alone. `/pre-spec` found that Case 1027 put the hook's tests into `test_ship.py`, which the clean version leaves out, while `codewrite.py` shipped. The person then chose that the hook does not ship, since it serves only the build of the clean copy. In an installed project it would be a hook that runs on every write and does nothing. Leaving the hook out is a second behaviour that can fail on its own, so the Case now has two sub-cases. The person chose this Case again with two parts. Case 1027 has decision lines in the ledger, and `vault/wiki/case-schema.md` (`## Splitting`) sets a new number for a Case that comes back with sub-cases (case 722.2). So this Case is 1028, and its decision lines carry `{supersedes:case 1027}`. The file of Case 1027 stays as it is.
>
> The judgment stays one. The test's `live_code_lines` walks `ship.tree_files(root, ".guppi")`, skips `ship.LEFT_OUT` and `ship.NOT_CLEANED`, and takes `ship.judged(name, text, set(), set())[1]` for each file. `judged` of `.guppi/guppi/ship.py` returns no line for a file of `NOT_CLEANED`. Otherwise it judges a Markdown file or a `schema.yaml` as a sample file, a Python file under `.guppi/tests/` by its comments and docstrings only, and a `.py` file for bare numbers by `bare_numbers`, through `leftovers` and through `outside` of `.guppi/guppi/pointers.py`. Case 1028.1 moves the per-file part of that test into one function, `live_code(name, text)` of `ship.py`, and both the test and the hook import it. A Grep of `.guppi/guppi/` for `judged\(|live_code` printed `ship.py` alone, where `ship` and `check` call `judged`, so no other module of the package holds a copy. Since the hook does not ship, `codewrite.py` imports `guppi.ship` directly and does not call `ship_stands` of `.guppi/guppi/pages.py`. So the docstring of `ship_stands` and the test of `.guppi/tests/test_lint.py` that checks its importers are left as they are. Those importers are `lint.py`, `check.py` and `cli.py`. `cli.py` adds the command `codewrite` under the same `if ship_stands():` that adds `ship`, so the clean version, which holds neither module, lists neither. The note form follows `shellwrite` of `.guppi/guppi/shellwrite.py`, which prints `{"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": ...}}` and exits 0. The page on hooks, https://code.claude.com/docs/en/hooks, says that the `additionalContext` of a `PostToolUse` hook is inserted next to the tool result. It also says that exit 2 there only shows stderr, since the tool already ran, and that the matcher of `PostToolUse` is the tool name, with `Edit|Write` among its examples. `frontierguard` reads the path as `tool_input.file_path` and resolves a relative one against the project.
>
> The copy takes `.claude/settings.json` byte for byte. `ship` of `ship.py` copies each file of `plan` and then cleans it by `settled`. It takes the Render of each page with `core: true` through `shipped_page`, which already rewrites the Render of `rule-claude-md` by `blank_description` and that of `rule-guppi-config` by `setup_not_done`. So Case 1028.2 adds `.guppi/guppi/codewrite.py` to `LEFT_OUT`. It also removes the exact registration of `guppi codewrite` from the copy of `.claude/settings.json` and from the Render of `rule-hook-registry` in `shipped_page`, so that `guppi render --check` over the copy finds both alike. The person chose to name one exact entry. They then chose that the build exits 1 only where a text still names `guppi codewrite` after the removal. The made-up project of `tree` in `test_ship.py` writes `{}` into `.claude/settings.json`. This repository holds no entry until the librarian's run. A refusal of every text without the entry would have made both red. `plan` leaves out each name of `LEFT_OUT`, so `check` does not judge `codewrite.py` either, as it does not judge `ship.py`.
>
> `rule-hook-registry` says in its Purpose that a hook Rule names `.claude/settings.json` in `implementation_ref`, so `rule-clean-branch` now names it, with `codewrite.py`. It also says that a hook is registered in the same Case that creates the hook's Rule. This hook gets no new Rule, so Case 1028.1 widens that sentence to a Rule the hook is added to. The Purpose of `rule-clean-branch` says that the copy holds the tests but `test_ship.py`, the tests of the command `ship`, and that it does not write `ship.py`. Case 1028.2 adds the hook to both sentences.
>
> The Estimates of `rule-clean-branch` stand as follows. The Criterion of `estimate-clean-branch-tests-judge-the-live-code` stands: the test still walks by `tree_files`, leaves out `LEFT_OUT` and `NOT_CLEANED`, now inside `live_code`, and runs `judged` over each file, and its promise is the full test run. `estimate-clean-branch-ships-the-tests` stands, since the hook's tests stand in `test_ship.py`, which the copy leaves out, and the copy holds no test that needs `codewrite.py`. `estimate-clean-branch-ships-no-ship-command` stands, since it speaks of `ship.py` alone, and the new `estimate-clean-branch-ships-no-code-write-hook` checks `codewrite.py`. `estimate-clean-branch-code-holds-pointers-only-in-brackets` stands as the promise that the new code holds its pointers in brackets. `estimate-hook-registry-rendered` stands, since the render line keeps the live `.claude/settings.json` equal to the Render. The insight is set `actioned` with this decision in `addressed_by`, as `vault/wiki/insights/schema.yaml` sets it for a Case of its own session.
>
> The other `PostToolUse` hooks of `.claude/settings.json` are `guppi event tool` on every tool, `guppi spec` on `ExitPlanMode`, `guppi pageread --after` on `Read` and `guppi shellwrite` on `Bash|PowerShell`. None of them runs on Edit or Write. `lesson-hooks-matching-hooks-of-one-event-run-in-parallel` stands, since `guppi event tool` and the new hook do not read each other's output. A Grep with the glob `{vault/wiki,.claude,.guppi/guppi}/**` from the root for `shellwrite`, a member of the list of hook commands, printed `.claude/settings.json`, `vault/wiki/log.md`, `vault/wiki/rules/rule-hook-registry.md`, `.guppi/guppi/cli.py`, `vault/wiki/estimates/estimate-shell-write-check-repairs-and-reports.md`, `vault/wiki/rules/rule-shell-write-check.md`, `.guppi/guppi/shellwrite.py` and `vault/wiki/lessons/lesson-work-mode-edited-a-source-file-through-the-shell.md`. The texts that list the hook commands are the Render of `rule-hook-registry` and the docstring of `cli.py`, and both enter the Case. A Grep of `.guppi/tests/` for `settings\.json|"shellwrite"|COMMANDS` printed `test_ship.py`, `test_ratified.py`, `test_render.py`, `test_guppi_package.py`, `test_shellwrite.py` and `test_guard.py`. Of these, two tests read the live repository. `test_each_hook_command_stands_in_the_settings_in_the_new_form` of `test_guppi_package.py` reads `.claude/settings.json`, and the new line passes it. `test_the_clean_version_holds_no_pyproject_and_no_lock_at_its_root` builds the copy of this repository and asserts no line of the build, so the removal changes nothing it asserts.
>
> The one new file is `.guppi/guppi/codewrite.py`. A Grep for `guppi/`, which covers `.guppi/guppi/`, `.guppi/` and the bare `guppi/`, printed 33 files of `.guppi/guppi/`. It printed 5 files of `.claude/`: `skills/setup/SKILL.md`, `skills/pre-spec/SKILL.md`, `agents/librarian-guppi.md`, `agents/ask-guppi.md` and `agents/case-guppi.md`. It printed 196 hits in 49 files of `vault/wiki/rules/`. A Grep of `vault/wiki/rules/` and `.claude/` for a rule over each module or file of such a folder, `(each|every) (module|file)[^.]{0,80}guppi/`, printed nothing. A Grep of `.guppi/guppi/` for `os\.walk|rglob|\.glob\(|iterdir` printed 14 files: `ledger.py`, `ship.py`, `prespec.py`, `casecheck.py`, `pages.py`, `lint.py`, `onward.py`, `backlog.py`, `sprint_close.py`, `generate.py`, `materialize.py`, `archive.py`, `cleanup.py` and `caseid.py`. The same Grep of `.guppi/tests/` printed 15 files: `test_ship.py`, `test_check.py`, `test_lint.py`, `test_onward.py`, `test_generate.py`, `test_spec.py`, `test_backlog.py`, `test_materialize.py`, `test_ratified.py`, `test_case_schema.py`, `test_sprint_close.py`, `test_guppi_package.py`, `test_gitstate.py`, `test_orchestration.py` and `test_archive.py`. These are the readers that take every file of the folder:
> - `tree_files` of `ship.py` walks `.guppi/`, and `LEFT_OUT` keeps the new module out of the copy and out of `live_code`;
> - `named_files` of `.guppi/guppi/casecheck.py` searches every file of `.guppi/guppi` for names, which a new module does not make wrong;
> - `test_without_the_module_ship_the_ship_step_is_skipped_with_one_line` of `test_check.py` copies the package without `ship.py`, where `cli.py` imports no `codewrite`, since `ship_stands` answers no;
> - the `style` key of `guppi.toml`, `uv run --project .guppi ruff check .` and `uv run --project .guppi ruff format --check .`, judges the new module like every other Python file.
>
> The other walks of the tests read temporary folders, the vault, `.claude/` or `.github/workflows/`. `.gitignore` and `.guppi/.gitignore` ignore no `.py` file of `.guppi/guppi/`. In `rule-plugin-install`, the install copies `.claude/settings.json` from the clean version, which no longer holds the entry. A Grep of the session ledger for `lesson\[error\]` and for `\{addresses:` printed nothing, so this Case closes no lesson of this session.
>
> The check of the file listed the files that name `rule-clean-branch`, `rule-hook-registry`, `ship.py`, `test_ship.py`, `cli.py`, `.claude/settings.json` or `guppi ship`. These are the ones whose purpose speaks of what the Case changes, and why each stands:
> - `rule-plugin-install` copies `.claude/settings.json` only after `uv sync` passes, as `estimate-plugin-install-runs-no-hook-before-uv-sync` promises, and `lesson-plugin-install-hooks-of-the-copy-run-at-once` names the cause; in an installed project the hook never runs, since the copy holds neither its entry nor its module;
> - `estimate-clean-branch-installs-as-a-plugin` and `estimate-sprint-plugin-installs-as-a-plugin` stand, since removing one element with its leading comma from a list of `PostToolUse` keeps `.claude/settings.json` valid JSON;
> - `estimate-clean-branch-ships-a-blank-project-description` and `estimate-clean-branch-ships-the-setup-not-done` speak of the other rewrites of `shipped_page`, which the new one leaves as they are;
> - `rule-settings`, `estimate-settings` and `rule-harness` say that `.claude/settings.json` is rendered whole from its rules, which stands in this repository, and the copy keeps its Render and its file alike;
> - `rule-morph` and `rule-skill-setup` speak of the settings of a project that installed GUPPI, which simply hold no entry of the hook;
> - in `.guppi/tests/test_check.py` a test copies the whole package without `ship.py`, where `cli.py` adds no `codewrite`, since `ship_stands` answers no;
> - `estimate-prespec-hook-reports-a-pointer-outside-a-bracket` speaks of `/pre-spec` over the new text of a page, another moment.
>
> The other listed files speak of other parts of the clean version, of the install, of the Case check or of other hooks, not of the hook at the write or of the entry the copy removes, and the Case leaves them as they are.

> **problem:**
> The agent writes a bare case number into a comment or a docstring under `.guppi/`, and nothing tells it so until the full test run at the end of Work Mode, so the fix is a second pass; the hook that tells it serves only the build of the clean copy and must not reach a project that installs GUPPI.

> **recommend:**
> - **What catches a bare case number when it is written**
>   - Recommended: (a) a hook after each write under `.guppi/`.
>   - Answer: (a), the recommendation accepted.
> - **Whether the hook stops the write or speaks after it**
>   - Recommended: (b) a note after the write.
>   - Answer: (b), the recommendation accepted.
> - **Which page holds the hook**
>   - Recommended: (b) a paragraph of `rule-clean-branch`.
>   - Answer: (b), the recommendation accepted.
> - **How the change is checked**
>   - Recommended: (a) a new Estimate on the page of the hook.
>   - Answer: (a), the recommendation accepted.
> - **Where the leaving-out of the hook goes**
>   - Recommended: (a) this Case again, with two parts.
>   - Answer: (a), the recommendation accepted.
> - **How the copy drops the registration**
>   - Recommended: (a) one named entry, removed from both texts.
>   - Answer: (a), the recommendation accepted.
> - **When a text without the entry stops the build**
>   - Recommended: (b) stop only where the hook is named in another form.
>   - Answer: (b), the recommendation accepted.
> - **Change**
>   - Asked: `/pre-spec` asked where the tests of the hook live and whether the hook enters the clean copy, and the person chose that the hook does not ship, its tests staying in `test_ship.py`.
>   - Taken: the hook and its registration stay out of the clean copy, set in Case 1028.2; `.claude/settings.json` joins the `implementation_ref` of `rule-clean-branch`.

### Case 1028.1 — A bare case number in the code is named at the write

> **given:**
> `rule-clean-branch`: the rule of the pointer in a bracket, which gains the hook.
> **＋** `estimate-clean-branch-names-a-pointer-at-the-write`: the new check of the hook.
> **＋** `rule-hook-registry`: the hook list of `.claude/settings.json`, which registers the hook.
> **＋** `insight-ship-live-code-writes-a-case-number-outside-a-bracket`: the insight the Case actions.
> **＋** `.guppi/guppi/codewrite.py`: the new hook module.
> **＋** `.guppi/guppi/ship.py`: the module that holds the judgment of the live code.
> **＋** `.guppi/guppi/cli.py`: the entry point that lists the commands.
> **＋** `.guppi/tests/test_ship.py`: the tests of the live code and of the hook.

> **when:**
> An Edit, Write or MultiEdit call writes a file under `.guppi/` in the repository of GUPPI, and the `PostToolUse` hook `uv run --project .guppi guppi codewrite` of `.guppi/guppi/codewrite.py` runs; or `.guppi/tests/test_ship.py` runs that hook over a payload of such a call in a temporary project.

> **then:**
> The hook reads the file as written and runs over it `live_code` of `.guppi/guppi/ship.py`, the judgment that the live code test of `.guppi/tests/test_ship.py` runs too.
> **＋** For each pointer outside a bracket of its own and each bare case number in a comment or a docstring of the file, it gives the agent a line with the file, the line and what it found, in `hookSpecificOutput.additionalContext` beside the result of the tool.
> **＋** With those lines it gives one line on the fix: a bracket of its own at the end of the sentence, or the sample `case N`.
> **＋** `live_code` leaves out each file of `LEFT_OUT` and `NOT_CLEANED` of `.guppi/guppi/ship.py` and each file outside `.guppi/`, and the live code test of `.guppi/tests/test_ship.py` takes its lines from it.
> **－** A file with no such line, a file outside `.guppi/` and a call of another tool get no line.
> **－** The hook refuses no call and exits 0; a payload or a file it cannot read gives one line on stderr.

```then
create:
- slug: estimate-clean-branch-names-a-pointer-at-the-write
  ref: rule-clean-branch
  kind: QA
  purpose: Whether, after an Edit, Write or MultiEdit of a file under .guppi/ in the repository of GUPPI, the hook guppi codewrite names to the agent each pointer outside its bracket and each bare case number of that file by the judgment of the live code test, and gives no line on a clean file, on a file outside .guppi/ or on a call of another tool
  method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k code_write_names
  tags:
  - ci
  - hooks
  - plugin
update:
- slug: rule-clean-branch
  set:
    implementation_ref:
    - .guppi/guppi/ship.py
    - .guppi/guppi/codewrite.py
    - .guppi/tests/test_ship.py
    - .claude/settings.json
    - .github/workflows/prod.yml
    - plugin/plugin.json
    - plugin/marketplace.json
    - plugin/assets
  replace:
  - old: before the Spec is approved, or, for a Case ratified in Work Mode, before its tasks run (case 807).
    new: before the Spec is approved, or, for a Case ratified in Work Mode, before its tasks run (case 807). After each Edit, Write or MultiEdit of a file under `.guppi/`, the hook `uv run --project .guppi guppi codewrite` of `.guppi/guppi/codewrite.py`, registered on `PostToolUse` by `rule-hook-registry`, runs over that file as written the same judgment, `live_code` of `.guppi/guppi/ship.py`, which the test of the live code takes its lines from, and names each such line and its fix — a bracket of its own, or the sample `case N` — to the agent beside the result of the tool, so that the agent fixes it before the full test run; it refuses no call (as set in case 1028.1).
  change: the hook guppi codewrite names a pointer outside its bracket under .guppi/ at the write
- slug: rule-hook-registry
  replace:
  - old: hook is an `update` of this page in the same Case that creates the hook's Rule.
    new: hook is an `update` of this page in the same Case that creates the hook's Rule, or that adds the hook to the Rule whose check it runs.
  - old: '{ "matcher": "Bash|PowerShell", "hooks": [ { "type": "command", "command": "uv run --project .guppi guppi shellwrite", "timeout": 30 } ] }'
    new: '{ "matcher": "Bash|PowerShell", "hooks": [ { "type": "command", "command": "uv run --project .guppi guppi shellwrite", "timeout": 30 } ] }, { "matcher": "Edit|Write|MultiEdit", "hooks": [ { "type": "command", "command": "uv run --project .guppi guppi codewrite", "timeout": 30 } ] }'
  change: guppi codewrite registered on PostToolUse of Edit, Write and MultiEdit
- slug: insight-ship-live-code-writes-a-case-number-outside-a-bracket
  set:
    status: actioned
    addressed_by: decision-case-1028.1
  change: 'actioned: the hook guppi codewrite names a bare case number at the write'
```

```tasks
- [ ] create `estimate-clean-branch-names-a-pointer-at-the-write`
- [ ] update `rule-clean-branch`
- [ ] update `rule-hook-registry`
- [ ] update `insight-ship-live-code-writes-a-case-number-outside-a-bracket`
- [x] `.guppi/guppi/ship.py`: add `live_code(name, text) -> list[str]`, which returns no line for a file outside `.guppi/` or of `LEFT_OUT` or `NOT_CLEANED`, and otherwise the `ship:` lines of `judged(name, text, set(), set())`.
- [x] `.guppi/guppi/codewrite.py`: the new `PostToolUse` hook; it reads `tool_name` and `tool_input.file_path` of the payload, takes the path relative to the project, imports `live_code` from `guppi.ship`, prints its lines and the line on the fix as one `hookSpecificOutput.additionalContext`, and exits 0; its docstring names `rule-clean-branch`.
- [x] `.guppi/guppi/cli.py`: add `"codewrite"` to `COMMANDS` by `importlib.import_module("guppi.codewrite").run` under the `if ship_stands():` that adds `ship`, and add `codewrite` to the hook commands and to the sentence on `ship` of the docstring.
- [x] `.guppi/tests/test_ship.py`: `live_code_lines` takes the lines of each file from `ship.live_code`; new tests whose names hold `code_write_names` run the hook over a temporary project: a Write of a file under `.guppi/` with a bare case number gets its line and the line on the fix, and a clean file, a file outside `.guppi/` and a call of another tool get no output; `cli.COMMANDS["codewrite"]` is `codewrite.run`.
- [ ] `uv run --project .guppi guppi render`: `.claude/settings.json`
- [ ] read `estimate-clean-branch-names-a-pointer-at-the-write`
```

### Case 1028.2 — The hook stays out of the clean copy

> **given:**
> `rule-clean-branch`: the rule of the clean copy, which leaves the hook out.
> **＋** `estimate-clean-branch-ships-no-code-write-hook`: the new check that the copy holds no hook.
> **＋** `rule-hook-registry`: the page whose Render in the copy loses the entry.
> **＋** `.guppi/guppi/ship.py`: the build of the copy.
> **＋** `.guppi/guppi/codewrite.py`: the hook module the copy leaves out.
> **＋** `.guppi/guppi/cli.py`: the entry point that lists the commands.
> **＋** `.guppi/tests/test_ship.py`: the tests of the build.
> **＋** `.claude/settings.json`: the settings file whose copy loses the entry.

> **when:**
> `uv run --project .guppi guppi ship <folder>` of `.guppi/guppi/ship.py` builds the clean version of the repository of GUPPI into an empty folder; or `.guppi/tests/test_ship.py` runs the build over a temporary project.

> **then:**
> The clean version holds no `.guppi/guppi/codewrite.py`.
> **＋** Its `.claude/settings.json` and the Render of `rule-hook-registry` hold no registration of `guppi codewrite`, and every other line stays as the working tree holds it.
> **＋** `guppi render --check` over the clean version names no file that differs.
> **＋** Run from the code of the clean version, `guppi` lists no command `codewrite`.
> **＋** Where a text still names `guppi codewrite` after the removal of the exact entry, the build prints a line that names the file and exits 1.
> **－** A text that never names `guppi codewrite` passes as it is.
> **－** `guppi ship --check` does not judge `.guppi/guppi/codewrite.py`, which the clean version does not hold.

```then
create:
- slug: estimate-clean-branch-ships-no-code-write-hook
  ref: rule-clean-branch
  kind: QA
  purpose: Whether the clean version holds no .guppi/guppi/codewrite.py and no registration of guppi codewrite in .claude/settings.json or in the Render of rule-hook-registry, lists no command codewrite, passes guppi render --check, and whether the build exits 1 where a text still names guppi codewrite after the removal of the exact entry
  method: uv run --project .guppi pytest .guppi/tests/test_ship.py -k no_code_write_hook
  tags:
  - ci
  - hooks
  - plugin
update:
- slug: rule-clean-branch
  replace:
  - old: with its tests `.guppi/tests/` but `.guppi/tests/test_ship.py`, the tests of the command `ship`,
    new: with its tests `.guppi/tests/` but `.guppi/tests/test_ship.py`, the tests of the command `ship` and of the hook `guppi codewrite`,
  - old: It does not write `.guppi/guppi/ship.py`, so a project that installs GUPPI, which builds no clean version, gets no command `ship`, and `guppi check` skips its step `guppi ship --check` there;
    new: It does not write `.guppi/guppi/ship.py`, so a project that installs GUPPI, which builds no clean version, gets no command `ship`, and `guppi check` skips its step `guppi ship --check` there; it does not write `.guppi/guppi/codewrite.py` either, and it removes the exact registration of the hook `guppi codewrite` from `.claude/settings.json` and from the Render of `rule-hook-registry` that it writes, so a project that installs GUPPI runs no such hook, and it prints a line and exits 1 where either text still names `guppi codewrite` after that removal;
  change: the clean version leaves out the hook guppi codewrite and its registration
```

```tasks
- [ ] create `estimate-clean-branch-ships-no-code-write-hook`
- [ ] update `rule-clean-branch`
- [x] `.guppi/guppi/ship.py`: add `.guppi/guppi/codewrite.py` to `LEFT_OUT`; add the exact registration text of `guppi codewrite`, as the Render of `rule-hook-registry` writes it with its leading comma, and one function that removes it from a text and tells whether `guppi codewrite` still stands there; `ship` applies it to the copy of `.claude/settings.json` and `shipped_page` to the Render of `rule-hook-registry`, and each text that still names the hook gives a `ship:` line; the module docstring names the hook among the files the copy leaves out.
- [x] `.guppi/tests/test_ship.py`: new tests whose names hold `no_code_write_hook`: a temporary project whose `.claude/settings.json` and Render of `rule-hook-registry` hold the entry builds a copy with no `.guppi/guppi/codewrite.py`, no entry in either text and a `guppi render --check` that names no file; a project whose text names `guppi codewrite` in another form gets a `ship:` line and exit 1; a project that never names the hook builds as before; the code of the copy lists no command `codewrite`.
- [ ] read `estimate-clean-branch-ships-no-code-write-hook`
```

## Deferred
