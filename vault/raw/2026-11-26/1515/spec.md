<!-- approved 17:01:52 · session 86f6e9ab -->

# Session 1515 — Plan Mode of 2026-11-26

## Case 1069 — The box and the closer of a Frontier line change in one edit

> **context:**
> The agent closes a line of a session's `frontier.md` by its box and its closer together, such as `- [x] C3 — … · brief · case 7`. The `PreToolUse` hook `uv run --project .guppi guppi frontierguard` of `rule-frontier-hook` works out the text that an `Edit`, `Write` or `MultiEdit` of that file would leave, and refuses the call when a line keeps the box `[ ]` beside a closer (case 1012). It reads no shell call, and it lets a closed box with no closer pass. In session 1336 the agent added the closer of C4 by an Edit, the hook refused it, and the agent ticked the box alone by `sed -i` through Bash; the line stood `[x]` with no closer until a later Edit, as `lesson-frontier-line-closed-in-two-changes-through-bash` records, and the synthesis set `insight-orchestration-frontier-closer-leaves-the-box-open` `open` again. The person chose that the hook refuse every Bash or PowerShell command whose text names `frontier.md`, reads too, and that it also refuse an edit that leaves a closed box `[x]` or `[-]` with no closer, so that neither half of a line changes alone.
>
> The rule that governs both is `rule-frontier-hook`, and `rule-one-judgment-one-implementation` governs the new judgment of a closed box. I read whole `run`, `is_frontier` and `refusal` of `.guppi/guppi/frontierguard.py`, `open_box_closers`, `open_case_items` and `check_frontier` of `.guppi/guppi/prespec.py`, and `text_after` of `.guppi/guppi/ratified.py`. Today the only judgment of a closed box line with no closer is inline in `check_frontier`: a box `[x]` or `[-]` whose last segment after ` · ` does not match `CLOSERS`, a line with no ` · ` included, under any heading; the hook calls only `open_box_closers`. So Case 1069.2 moves that judgment into one function of `prespec.py` that both import, and no second copy exists. A Grep of `CLOSERS|FRONTIER_LINE` over `.guppi/guppi/` printed `casecheck.py`, `frontierguard.py`, `generate.py` and `prespec.py`; `open_backlog_lines` of `casecheck.py` and `frontier_marks` of `generate.py` read the box and the source and make no judgment of a closer. A Grep of `frontier\.md|FRONTIER\b` over `.guppi/guppi/` printed `backlog.py`, `casecheck.py`, `frontierguard.py`, `generate.py`, `onward.py`, `prespec.py` and `recall.py`; none judges a shell command, so the judgment of a command that names the file is new and lives in `frontierguard.py` alone. The shell check stays in that module and under `rule-frontier-hook` rather than in `bashguard.py`, a choice of form, since the rule is about the Frontier and one module then holds both refusals; the hooks `uv run --project .guppi guppi bashguard` and `uv run --project .guppi guppi powershellguard`, which run on the same calls, are not changed. The name is matched in any letter case, since on Windows `Frontier.md` opens the same file.
>
> No fixed command of the harness names the file. A commit message the agent writes is another matter: at Retro, where `.claude/skills/retro/SKILL.md` says to commit the work and then the session folder, or anywhere else, a `git commit -m` whose message names `frontier.md` is refused, as the person accepted with option (a), and the agent names the Frontier in words. The refusal reason says so, a line of the `then` of Case 1069.1, so the agent learns it at the one call it costs. No Render of a commit step changes, since none sets the words of a commit message: the step of the retro skill says only to commit, and `rule-retro-commit` sets only that the tree is committed before `/handoff`. A text the agent has to remember did not stop the split of a line before, so the reason is where the rule stands. In this session the hook is registered on the shell only at the librarian's render, so the commits of this session's Retro are not refused. A Grep of `frontier\.md` over `.claude/` printed lines of `agents/librarian-guppi.md`, `settings.json`, `skills/carry/SKILL.md`, `skills/hi/SKILL.md`, `skills/pr-review/SKILL.md`, `skills/retro/SKILL.md`, `skills/sprint-close/SKILL.md` and `skills/work/SKILL.md`, none a command, and a Grep of `git add|git commit|git mv|git rm` over `.claude/` printed `agents/librarian-guppi.md`, `skills/box/SKILL.md`, `skills/handoff/SKILL.md` and `skills/merge-main/SKILL.md`, none naming the file. The Frontier that `/hi` writes holds closed lines only with a closer, so Case 1069.2 refuses none of its writes.
>
> The Criterion of `estimate-frontier-hook-refuses-an-open-box-with-a-closer`, which passed and is no one-off, says that another tool exits 0, which Case 1069.1 makes false, and speaks of the box beside a closer, which Case 1069.2 widens; Case 1069.2 replaces it whole and sets its `purpose` anew, and Case 1069.1 creates its own Estimate, a choice of form. The docstring of `frontierguard.py` says that a box written by a shell call still shows at `/pre-spec`; Case 1069.1 changes it. Adding the hook to the Bash and PowerShell entries is an `update` of `rule-hook-registry`, as its Purpose sets for a hook added to the rule whose check it runs. A Grep of `bashguard` in the mode of paths over `{vault/wiki,.claude,.guppi/guppi}/**` printed 12 files; `.claude/settings.json` and `rule-hook-registry` list the hooks of the event and change, `cli.py` lists every hook command and holds `frontierguard` already, and the rest name the Bash guard alone. A Grep of `frontierguard` in the mode of paths over `{vault/wiki,.claude,.guppi}/**` printed 16 files; `entity-sprint-plugin` and `estimate-sprint-close-settles-unread-estimates` name a one-off Estimate of a build, `insight-ship-live-code-writes-a-case-number-outside-a-bracket` a pointer once left in the docstring, and the docstrings of `prespec.py` and `ratified.py` stay true. That Insight, and the test `test_the_live_code_holds_no_pointer_outside_a_bracket` of `.guppi/tests/test_ship.py`, which judges the live code by `ship.live_code`, are why each code task writes a pointer to a case only in a bracket at the end of its sentence. A Grep of `settings\.json` over `.guppi/tests/` printed `test_ratified.py`, `test_ship.py`, `test_guppi_package.py`, `test_render.py` and `test_guard.py`; only `settings_commands` of `test_guppi_package.py` reads the live file, and the new entries keep the command form its tests ask for. Case 1069.1 sets the Insight `actioned`, its `addressed_by` the decision of 1069.1. The session holds no ledger yet, so no lesson mark is due, and the lesson of session 1336 gets none, since its fix is ratified in another session.
>
> The new Criterion of that Estimate rewords four of its old lines on purpose: the reason now names an item with its closer only where the box is open, the event log is named by words, the passing tools leave out `Bash` and `PowerShell`, and `prespec.py` changes in its code while its findings stay. Two lines of the two sub-cases share their words, the line of the event log and the line of what exits 0, since each sub-case is a refusal of its own that writes the same log line and passes its own other calls. Of the files the check named, I read `estimate-prespec-checks-the-frontier`, whose Criterion on a closed line with no closer stands, since its findings stay; `estimate-hook-registry-rendered`, `estimate-settings` and `estimate-powershell-guard-refuses-a-here-string-piped-into-an-interpreter`, whose lines on the render and on the registration of the PowerShell guard stay true with one more hook on the same entry; `estimate-hi-writes-frontier`, whose closers stand; and the lines of `rule-prespec` on closers, all History. `rule-plan-mode` names `rule-frontier-hook` only in its `children`. `lesson-hooks-matching-hooks-of-one-event-run-in-parallel` stands, since the new hook and the guard beside it on the same entry read the payload alone and wait on no output of each other. The other files the check named speak of `.claude/settings.json`, of `prespec.py` or of `guppi prespec` for other things, and I did not read them. The check also named the files of Cases 1070 and 1071: Case 1070 names `rule-frontier-hook`, and Case 1071 names `prespec.py`. On the second pass I read both finished files whole, `vault/raw/2026-11-26/1515/cases/case-1070.md` and `vault/raw/2026-11-26/1515/cases/case-1071.md`. Case 1070 names `rule-frontier-hook`, `rule-hook-registry` and this Case's hook on shell calls only in its context, and it changes none of them. Its renders of `.claude/settings.json` at a setup take the Render of `rule-hook-registry` as it stands, so they carry the two new entries once this Case lands. Case 1071.2 changes `check_form`, `judge` and the docstrings of `prespec.py` for a new finding on a `method`. Case 1069.2 changes `check_frontier` and adds one function there, so the two touch different functions and no finding of one changes the other. Case 1071.1 sets that an Estimate off a sprint page reads no transcript of a session in a `method` that a Case creates or keeps under a new Criterion. Both Estimates of this Case read `uv run --project .guppi guppi test`, with no reading by hand, so the rule and the check of Case 1071 leave them alone. No line of either file rests on what this Case makes false, and this Case changes nothing on their account.

> **problem:**
> The hook that keeps the box and the closer of a Frontier line together reads only edits, so a shell command can tick a box alone, and an edit can do the same, and the line stands half closed.

> **recommend:**
> - **Which shell calls on frontier.md the guard refuses**
>   - Recommended: (a) refuse every Bash or PowerShell command that names `frontier.md`, reads too, before it runs.
>   - Answer: agreed, (a).
> - **Whether an edit that ticks the box alone is refused too**
>   - Recommended: (a) refuse a closed box with no closer as well, by one function that the check of `/pre-spec` and the hook share.
>   - Answer: agreed, (a).

### Case 1069.1 — A shell command that names the Frontier is refused

> **given:**
> `.guppi/guppi/frontierguard.py`: the hook, which now reads shell calls too.
> **＋** `.guppi/tests/test_frontierguard.py`: the tests of the hook.
> **＋** `rule-frontier-hook`: the rule of the hook.
> **＋** `estimate-frontier-hook-refuses-a-shell-command-on-the-frontier`: the new check of the shell refusal.
> **＋** `rule-hook-registry`: the registrations of `.claude/settings.json`.
> **＋** `.claude/settings.json`: the hooks of each event, rendered.
> **＋** `.guppi/guppi/prespec.py`: the check of the Frontier at `/pre-spec`.
> **＋** `insight-orchestration-frontier-closer-leaves-the-box-open`: the Insight this Case actions.

> **when:**
> The agent calls `Bash` or `PowerShell`, and the `PreToolUse` hook `uv run --project .guppi guppi frontierguard` of `.guppi/guppi/frontierguard.py` reads `tool_input.command` of the payload.
> **＋** Or `.guppi/tests/test_frontierguard.py` runs the hook over a made-up payload of `Bash` or `PowerShell`.

> **then:**
> When the command names `frontier.md`, in any letter case, the hook exits 2, and the call does not run.
> **＋** The reason on stderr says that `frontier.md` changes only by an `Edit` of the whole line or by a `Write`, and is read by `Read` or `Grep`, never through a shell command.
> **＋** The same reason says that a commit message names the Frontier in words, since a `git commit` whose message names `frontier.md` is refused too.
> **＋** Before the refusal one line goes to the day's event log, since a blocked call has no `PostToolUse`.
> **－** A command that does not name `frontier.md` exits 0, and a payload the hook cannot read exits 0 with one line on stderr; the hook never raises.
> **－** A script that a command runs by its path and that writes `frontier.md` is not seen; the check of the Frontier in `.guppi/guppi/prespec.py` still reports a line it leaves wrong.

```then
create:
- slug: estimate-frontier-hook-refuses-a-shell-command-on-the-frontier
  ref: rule-frontier-hook
  kind: QA
  purpose: Whether a Bash or PowerShell call whose command names frontier.md is refused before it runs, with a reason that says how the file is changed and read, and every other shell call passes
  method: uv run --project .guppi guppi test, which runs .guppi/tests/test_frontierguard.py
  tags:
  - hooks
  - harness
  - session
update:
- slug: rule-frontier-hook
  replace:
  - old: before it runs, and its mechanism stands in the docstring of
    new: before it runs. The same hook refuses before it runs a `Bash` or `PowerShell` call whose command names `frontier.md`, since a box ticked alone through Bash got past the check of an edit (as set in case 1069.1). Its mechanism stands in the docstring of
  change: the hook refuses a Bash or PowerShell command that names frontier.md
- slug: rule-hook-registry
  replace:
  - old: 'guppi bashguard", "timeout": 30 } ] },'
    new: 'guppi bashguard", "timeout": 30 }, { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi frontierguard", "timeout": 30 } ] },'
  - old: 'guppi powershellguard", "timeout": 30 } ] },'
    new: 'guppi powershellguard", "timeout": 30 }, { "type": "command", "command": "uv run --project \"${CLAUDE_PROJECT_DIR}/.guppi\" guppi frontierguard", "timeout": 30 } ] },'
  change: guppi frontierguard registered on PreToolUse of Bash and of PowerShell
- slug: insight-orchestration-frontier-closer-leaves-the-box-open
  set:
    status: actioned
    addressed_by: decision-case-1069.1
  change: 'actioned: the hook refuses a shell command that names frontier.md, and an edit that leaves a closed box with no closer (case 1069)'
```

```tasks
- [x] update `rule-frontier-hook`
- [x] update `rule-hook-registry`
- [x] create `estimate-frontier-hook-refuses-a-shell-command-on-the-frontier`
- [x] update `insight-orchestration-frontier-closer-leaves-the-box-open`
- [x] `.guppi/guppi/frontierguard.py`: on `Bash` and `PowerShell` the hook reads `tool_input.command` and refuses a command that names `frontier.md` in any letter case, by exit 2 with the reason of the `then` on stderr and one line in the day's event log first; its docstring says so, and its sentence that a box written by a shell call still shows at `/pre-spec` says instead that a script run by its path is not seen and that `/pre-spec` still reports what it leaves; a pointer to a case stands only in a bracket at the end of its sentence.
- [x] `.guppi/tests/test_frontierguard.py`: a Bash `sed -i` on a session `frontier.md`, a PowerShell `Set-Content` on it, a `cat` of it, a `git commit -m` whose message names `frontier.md` and a command that names `FRONTIER.MD` are refused with the reason, its words on a commit message included, and one line in the event log; a Bash and a PowerShell command that name no `frontier.md` pass.
- [x] `uv run --project .guppi guppi render`: `.claude/settings.json`
- [x] read `estimate-frontier-hook-refuses-a-shell-command-on-the-frontier`
```

### Case 1069.2 — An edit that leaves a closed box with no closer is refused

> **given:**
> `.guppi/guppi/frontierguard.py`: the hook, which now refuses a closed box with no closer too.
> **＋** `.guppi/guppi/prespec.py`: the judgments of a Frontier line and the check of the Frontier.
> **＋** `.guppi/guppi/ratified.py`: the one computation of the text a call would leave.
> **＋** `.guppi/tests/test_frontierguard.py`: the tests of the hook.
> **＋** `rule-frontier-hook`: the rule of the hook.
> **＋** `estimate-frontier-hook-refuses-an-open-box-with-a-closer`: its Criterion is replaced whole.
> **＋** `vault/raw/<date>/<HHMM>/frontier.md`: the Frontier of a session, the file the hook judges.

> **when:**
> The agent calls `Edit`, `Write` or `MultiEdit` on a file `vault/raw/<date>/<HHMM>/frontier.md`, and the `PreToolUse` hook `uv run --project .guppi guppi frontierguard` of `.guppi/guppi/frontierguard.py` reads the payload.
> **＋** Or `.guppi/tests/test_frontierguard.py` runs the hook over a made-up payload and a made-up `frontier.md`.

> **then:**
> The hook works out the whole text the call would leave: the `content` of a `Write`, or the file with each `old_string` replaced by its `new_string` in order, once or at each match with `replace_all`, by the one function that `builder_write` of `.guppi/guppi/ratified.py` uses too.
> **＋** When a box line of that text, under any heading, keeps the box `[ ]` while its last segment after ` · ` is a closer by `CLOSERS` of `.guppi/guppi/prespec.py`, the hook exits 2, and the call does not run.
> **＋** When a box line of that text, under any heading, has the box `[x]` or `[-]` while its last segment after ` · ` is no closer by `CLOSERS`, a line with no ` · ` included, the hook exits 2 too, and the call does not run.
> **＋** The hook takes that second judgment from the one function of `.guppi/guppi/prespec.py` by which its check of the Frontier reports a line closed without a closer.
> **＋** The reason on stderr names each such item, with its closer where the box is open, and says that the box and the closer are written in one edit of the whole line, `[x]` for an item ended and `[-]` for an item put off.
> **＋** Before the refusal one line goes to the day's event log, since a blocked call has no `PostToolUse`.
> **－** A text whose open lines carry no closer and whose closed lines each carry one exits 0, and so do a file other than such a `frontier.md` and a tool other than `Edit`, `Write`, `MultiEdit`, `Bash` and `PowerShell`.
> **－** An old string missing or found more than once without `replace_all`, a file to edit that does not exist, and a payload the hook cannot read exit 0, the last with one line on stderr; the hook never raises.
> **－** The findings of the check of the Frontier in `.guppi/guppi/prespec.py`, and their order, stay as they are.

```then
update:
- slug: rule-frontier-hook
  set:
    purpose: Prevents a line of the Frontier from keeping its open box beside a closer, or its closed box [x] or [-] with no closer, so that the box and the closer of a line change in one edit
  replace:
  - old: Prevents a line of the Frontier from keeping its open box beside a closer, so that the line reads as open though the agent closed it.
    new: Prevents a line of the Frontier from keeping its open box beside a closer, or its closed box [x] or [-] with no closer, so that the box and the closer of a line change in one edit.
  change: the hook refuses a closed box with no closer too
- slug: estimate-frontier-hook-refuses-an-open-box-with-a-closer
  set:
    status: pending
    purpose: Whether an Edit, Write or MultiEdit of the frontier.md of a session folder that would leave a line with the box [ ] beside a closer, or with a closed box and no closer, is refused before it runs, with a reason that names each item, and every other such call passes
  change: the Criterion replaced whole — a closed box with no closer is refused too
```

```tasks
- [x] update `rule-frontier-hook`
- [x] update `estimate-frontier-hook-refuses-an-open-box-with-a-closer`
- [x] `.guppi/guppi/prespec.py`: one function names the item of each box line of a Frontier, under any heading, whose box is `[x]` or `[-]` and whose last segment after ` · ` is no closer by `CLOSERS`, a line with no ` · ` included; `check_frontier` reports its finding `is closed without case N, work, defer, kept or defer case N` by that same judgment, its findings and their order unchanged; the docstrings say that the hook imports it, a pointer to a case only in a bracket at the end of its sentence.
- [x] `.guppi/guppi/frontierguard.py`: the hook refuses a text that leaves such a line, by that function of `prespec.py`, with the reason of the `then`; its docstring says so, a pointer to a case only in a bracket at the end of its sentence.
- [x] `.guppi/tests/test_frontierguard.py`: an Edit that ticks the box of an open line alone, a Write that leaves `[-]` with no closer and a line closed with no ` · ` are refused, each item named in the reason; the tests that stand pass as they are.
- [x] read `estimate-frontier-hook-refuses-an-open-box-with-a-closer`
```

## Case 1070 — A project sets the name of its main branch at the setup, and the code and the skills read it

> **context:**
> GUPPI takes the main branch of every project to be `main`. The word stands in the code and in the text of each skill that ships. The check of a conserved Spec, `guppi box --check` of `.guppi/guppi/box.py`, refuses to run on the branch `main` by a constant, `SHARED_NEVER = "main"`. The skills that open and close a sprint run `gh pr create --base main`, `git merge --ff-only origin/main` and `gh api repos/{owner}/{repo}/commits/main`, and `/work` and `where-to-stop.md` stop Work Mode on `main`. In a project whose main branch is `master`, these commands fail or point at the wrong branch, and Work Mode and `/box` run on the shared branch. The setup Case does not ask the name on purpose: the `## Purpose` of `rule-morph` says that the code takes the main branch to be `main` in every project and the setup does not change it (case 1017.4), and the line of this item waits in the `## Backlog` of `entity-sprint-plugin`.
>
> The person chose a key `main_branch` in `guppi.toml`, which the render fills into the Renders as it fills the languages, and which the code reads through one function; the setup Case proposes the name from the branch that `/hi` printed under `Branch:` and shows it for correction; and only the texts that ship take the name. So Case 1070.1 adds the key and its readers, Case 1070.2 has `/box` read it, Case 1070.3 has the setup Case set it, Case 1070.4 puts `{{main_branch}}` into the Renders of the skills that ship, Case 1070.5 does the same for the librarian, the pages that say who writes the vault and the glossary, Case 1070.6 words the `purpose` of three shipped Estimates of those skills for any project, and Case 1070.7 reads the whole in one new install whose main branch is `master`. The split is a choice of form, by the rule of atomicity: each part fails and is fixed apart.
>
> The render already has the form: `fill_placeholders` of `.guppi/guppi/render.py` puts in the name of a language where a Render writes `{{documentation_lang}}` or `{{chat_lang}}`, by `parse` of `.guppi/guppi/config.py` over the Render of `rule-guppi-config`, and stops the run on an unknown placeholder, a missing key or an unknown code. Case 1070.1 lets it put the value of `main_branch` in as it stands. On a missing key the two readers part on purpose: the render stops, as `estimate-guppi-config-fills-the-languages` promises for a missing key, since a project gets the key and the placeholders in one render; the code gives `main`, as `setup_pending` takes a missing `setup_done` as done, so a `guppi.toml` written before this Case keeps working. The value itself is judged by one new function of `config.py` that both sides import (`rule-one-judgment-one-implementation`). Today no side judges a branch name: a Grep of `.guppi/guppi/` for `def .*branch|BRANCH|branch_name` printed nothing, `box.py` compares with its constant and `fill_placeholders` knows only the language keys, read whole for this claim with `parse`, `read_settings`, `commands_of`, `setup_pending` of `config.py`, and `check` and `git` of `box.py`. The Criterion of `estimate-guppi-config-fills-the-languages` stands: it speaks of the two language placeholders, and a placeholder that is no key still stops the run.
>
> The setup proposes the name from `Branch:`, which prints `git branch --show-current` by `state` of `.guppi/guppi/gitstate.py`, read whole. The documentation of git, https://git-scm.com/docs/git-branch, says of `--show-current` that it prints the name of the current branch and nothing in detached `HEAD` state, so the setup proposes `main` where the line names no branch. In a folder with no git repository `/hi` ends its reply before `/setup`, as the Render of `rule-git-context` sets it. Case 1070.3 replaces the Criterion of `estimate-morph-sets-up-the-project-at-the-first-hi` whole, since its line that the setup asks no name of the main branch turns false. The `/pre-spec` check found that a Then of behaviour cannot be seen in a reading of the Spec, so the new Criterion, `purpose` and `method` read only what the `## Render` of `rule-skill-setup` and the `## Purpose` of `rule-morph` say, in the Spec at Retro, or after it the Render of `rule-skill-setup` in `.claude/skills/setup/SKILL.md`, rendered from it; the behaviour, the install in a project made by `git init -b master` among it, moves to the one-off Estimate of Case 1070.7, which waits for the librarian's run of this session, since a copy that `guppi ship --allow-draft` writes before that run holds the old text of `/setup`. `estimate-morph-takes-in-the-set-aside-files` and `estimate-skill-setup-starts-at-hi` speak of the files set aside and of the hook on `/hi`, and stand. The Criterion of `estimate-spec-box-refuses-a-stale-spec` names a run from `main`, so Case 1070.2 replaces it whole and rewords its `purpose`; its `method`, `test_box.py`, stands.
>
> A Grep of `vault/wiki/` for ``origin/main|`main`|--base main|commits/main|into main|merge-main|main branch|\bmain <hash>|on main\b`` printed 186 matches in 42 files. The Renders that ship and name the main branch are those of `rule-git-context`, `rule-skill-sprint-open`, `rule-skill-sprint-close`, `rule-work-mode`, `rule-where-to-stop` and `rule-documentation`; each has `core: true`. The `## Purpose` of `rule-git-context`, `rule-work-mode`, `rule-spec-box`, `rule-page-generation` and `rule-vault-layout` and the rows Librarian and Work Mode of `entity-glossary` name `main` in prose, and each pair turns it into words. The other hits stand. `rule-skill-merge-main`, `rule-skill-pr-review`, `rule-clean-branch`, `rule-github-repository`, `entity-guppi-repository` and their Estimates have no `core: true` and stay in the repository of GUPPI, whose main branch is `main`, as the person chose. So do `estimate-sprint-plugin-ci-writes-a-clean-branch` and `estimate-sprint-plugin-pull-requests-reviewed-on-github`, which read the branch `main` of the repository of GUPPI on GitHub. `rule-plan-mode` names `rule-skill-merge-main` among its children, `insight-case-build-recommends-without-reading-the-governing-rule` tells of a session of GUPPI, and the `main` of `rule-lessons-schema` stands in an example lesson of GUPPI. The hits in `log.md`, `brief.md` and `backlog.md` are not read. `rule-skill-setup` says it asks no name, and Case 1070.3 changes that. The Criteria of `estimate-skill-sprint-open-merges-the-closed-sprint-branch`, `estimate-skill-sprint-close-leads-the-closing-session`, `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-where-to-stop-stops-only-on-its-conditions`, `estimate-git-context-offers-git-init` and `estimate-git-context-gitstate-exits-zero` name `main`, and they stand: in this repository the key holds `main`, so each rendered file reads as before, and the Criteria are read here. `estimate-clean-branch-ships-neutral-texts` sets that no `purpose` of a shipped Estimate holds only in the repository of GUPPI, and that its reader lists each sentence of a shipped Criterion that does, for a later Case; so Case 1070.6 words the `purpose` of the three of these Estimates that name `main` there, and their Criteria wait for that list. The `/pre-spec` check found that the `method` of `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` names a run on main and the branch main and reads a transcript; the Criterion of `estimate-clean-branch-ships-neutral-texts` says that no sentence of the `method` of a shipped Estimate holds only in the repository of GUPPI, so Case 1070.6 gives it a new `method` that names no branch and waits for no moment of a past session. Case 1071.1 lets no new `method` of an Estimate whose target is not a sprint page read a transcript, and has the lasting one read a test, a command or the text of a page in the Spec at Retro or in the file rendered from it; so that `method` runs `uv run --project .guppi guppi render --check` and reads `.claude/skills/work/SKILL.md` against each line of the Criterion, as the old `method` already did for the lines a session lacked. Its status stays `passed`, since its Criterion stands and its reading of 2026-11-23 read the run in its transcript once; no one-off Estimate takes that reading again, as nothing in that run changes, and the new paragraph of `/work` on the setup Case is read in a run by the one-off Estimate of Case 1070.7. That Estimate already checks Case 1070.6, and its Criterion stands, since it promises exactly this of every shipped `purpose` and `method`. The `purpose` of `estimate-git-context-offers-git-init` holds in any project, since the clean version ships `main` and the step it names comes before the setup, and the `purpose` of the other two names no branch. The two Estimates that Cases 1070.2 and 1070.3 set `pending` do not ship until a reading passes, as `estimate-clean-branch-ships-the-passed-estimates` promises for a shipped Estimate, and their pages keep a History line that set them `built`, so the build of the clean version is not blocked.
>
> In code, a Grep of `.guppi/` for `show-current|branch ==|== "main|SHARED_NEVER|origin/` printed `box.py` (the constant), `gitstate.py` (its docstring) and `test_box.py` (a test on the branch `migration`). The docstring of `gitstate.py` changes under Case 1070.4. `.github/workflows/checks.yml` names no branch but `prod`. A Grep of `.claude/` for `main branch|origin/main` printed `.claude/skills/setup/SKILL.md`, `.claude/skills/sprint-open/SKILL.md` and `.claude/skills/merge-main/SKILL.md`; the first two change by their pages, and `/merge-main` stays. The new key and the placeholder add members to two lists. A Grep for `setup_done` in the mode of paths, over `{vault/wiki,.claude,.guppi/guppi}/**` from the root, printed 21 files. The texts among them that list the keys of `guppi.toml` are `config.py`, `rule-guppi-config`, `rule-skill-setup` and the Criterion of `estimate-morph-sets-up-the-project-at-the-first-hi`, and each enters a sub-case; the rest name `setup_done` alone. A Grep for `chat_lang\}\}` the same way printed 10 files. The texts that list the placeholders are `render.py`, `rule-guppi-config` and the Criterion of `estimate-guppi-config-fills-the-languages`, which speaks of the languages and stands; the others use a placeholder.
>
> Tests that read a live file: a Grep of `.guppi/tests/` for `REPO\s*/|parents\[2\]|ROOT\s*=|project_root\(\)` printed `test_case_schema.py`, `test_generate.py`, `test_guppi_package.py`, `test_lint.py`, `test_materialize.py`, `test_orchestration.py`, `test_schemas.py` and `test_ship.py`. Of them, `test_guppi_package.py` reads the hook commands of the frontmatter of `librarian-guppi.md`, which no pair changes, and `test_ship.py` builds the clean version from the working tree; `ship.py` imports neither `render` nor `box`, and the copy runs the new tests over made-up folders. A Grep of `.guppi/` for `guppi\.render|from guppi import .*render|from guppi\.render|guppi\.box|from guppi import .*box` printed `glossary.py`, `prespec.py`, `spec.py`, `sprint.py`, `sprint_close.py`, `test_backlog.py`, `test_box.py`, `test_render.py` and `test_ship.py`; they import `tick_command_lines`, `command_line`, `conserved_spec_named` or the modules for made-up trees, and none reaches `fill_placeholders` or `check` over a live file. The code runs from the working tree in Work Mode and the pages land at the librarian's run: until then no Render holds `{{main_branch}}` and `guppi.toml` holds no key, so the render reads nothing new and `box.py` reads `main`, and no reader needs an old form. The session's ledger holds no `error` lesson.
>
> Of the files the check named, I read these. `estimate-clean-branch-ships-the-setup-not-done` keeps every other line of the Render of `rule-guppi-config` in the copy, so the line `main_branch = "main"` ships and its Criterion stands. `.claude/skills/setup/SKILL.md` is the text of `rule-skill-setup` that Case 1070.3 changes. `vault/wiki/where-to-stop.md` is the text of `rule-where-to-stop`. `.claude/skills/box/SKILL.md` names the shared branch only by `<shared branch>`, and `estimate-spec-box-runs-a-conserved-spec` does not name `main`; both stand. `test_box.py` asserts the reason of a run from `main` word for word, so the task of `box.py` keeps those words. `test_gitstate.py` makes its repository by `git init -b main` and reads no docstring. `test_config.py` holds the tests that the new ones join. `estimate-clean-branch-code-holds-pointers-only-in-brackets` is why each code task writes a pointer only in a bracket. `case-1069.md` changes `rule-frontier-hook`, `rule-hook-registry` and a hook on shell calls, and this Case changes none of them. `estimate-render-harness-reproduces` speaks of the render as a whole, and the fill of the placeholders is the promise of the two Estimates of `rule-guppi-config`. The new Criterion of `estimate-spec-box-refuses-a-stale-spec` drops its line on a branch `main` on purpose, since the line that names the main branch of `guppi.toml` takes its place. Some `then` lines of Cases 1070.1, 1070.2, 1070.4 and 1070.5 share words, since each names the same key or the same placeholder; each is a promise of its own on its own reader or text. `estimate-sprint-plugin-close-steps-run-from-the-line` names `estimate-skill-sprint-close-leads-the-closing-session` only as the holder of the steps of `/sprint-close`, which a new `purpose` does not change, and it stands. The `then` of Case 1070.6 shares words with those of Cases 1070.3, 1070.4 and 1070.5, since each says that a text names the main branch in words; each speaks of other texts. The `then` of Case 1070.7 shares words with those of Cases 1070.1 to 1070.5 on purpose: it is the one-off reading of their behaviour in one new install, which Case 1071.1 keeps off the rule pages, and the lasting promises stay with the Estimates of those sub-cases. The other files the check named import `config.py`, `render.py` or `box.py` for other functions, or name `guppi render`, `guppi box` or `guppi gitstate` for other things, and I did not read them.
>
> Cases 1069 and 1071 were built again at the same time after `/pre-spec`, and on this pass I read both finished files whole. Case 1071.1 removes the line of its own item from the `## Backlog` of `entity-sprint-plugin` by a fenced `old` that is that line alone and an empty `new`; the line of this item stands just before it. Case 1070.3 removes the line of this item in the same form, its `old` that line alone, and adds the item under `## Closed` after the line of case 794. The two `old` texts are two different lines and share no character, so both pairs apply in either order. Case 1071.1 also sets that an Estimate whose target is not a sprint page reads no transcript of a session in its `method`, for each Estimate that a Case creates or gives a new `method` or a new Criterion, and that the lasting Estimate of such a promise reads a test, a command, or the text of a page in the Spec at Retro or in the file rendered from it. So the new `method` of `estimate-morph-sets-up-the-project-at-the-first-hi` reads the two pages in the Spec at Retro, or after it `.claude/skills/setup/SKILL.md`, rendered from `rule-skill-setup`; the new `method` of `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` runs the render check and reads `.claude/skills/work/SKILL.md`; and Case 1070.7 creates a one-off Estimate of `entity-sprint-plugin` with `once: true` that reads a new install in its transcript. The other Estimates this Case creates or changes run tests, read files rendered from their pages or change a `purpose` alone. Case 1071.1 names `/merge-main` only where the project holds it, so the task of the docstring of `gitstate.py` in Case 1070.4 names it the same way. Case 1069 changes `rule-frontier-hook`, `rule-hook-registry`, `frontierguard.py` and `prespec.py`; this Case changes none of them, and the render of `.claude/settings.json` at a setup takes the Render of `rule-hook-registry` as it stands. No line of either file rests on what this Case makes false.

> **problem:**
> A project whose main branch is not `main` cannot keep GUPPI's rules on branches: the skills open pull requests into a branch that does not exist, and Work Mode and `/box` run on the shared branch. No setting holds the name, and the setup Case does not ask for one.

> **recommend:**
> - **Where the name is kept and how the texts read it**
>   - Recommended: (a) a setting `main_branch` in `guppi.toml`, `main` in the copy that ships; the render puts its value where a Render writes `{{main_branch}}`, and the code reads it by one function of the settings module, `main` when the file or the setting is missing.
>   - Answer: agreed, (a).
> - **How the setup finds the name**
>   - Recommended: (a) proposed from the branch that `/hi` printed under `Branch:`, shown for the person to correct, with no question.
>   - Answer: agreed, (a).
> - **Which texts take the name in place of `main`**
>   - Recommended: (a) only the texts that ship; `/merge-main`, `/pr-review` and the other pages of the repository of GUPPI keep `main`.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: on the findings of `/pre-spec`, the person chose that `/sprint-open` and `/work`, in the session of the setup Case, take the name of the main branch from the ratified setup Case and not from the placeholder, the name going into the prompt of the opening Case as the branch of `Branch:` does; the other findings asked that `/setup` write that branch into its prompt and render each file that names the main branch, that the Criterion of the setup Estimate read only text, and that the `method` of the Estimate of `/work` name the main branch in words.
>   - Taken: Cases 1070.4 and 1070.7 take the name from the setup Case and read that run; Case 1070.3 writes the branch into the prompt, renders those files and reads only the texts of the setup; Case 1070.6 gives that `method` words and no transcript.

### Case 1070.1 — The key main_branch of guppi.toml, filled by the render and read by the code

> **given:**
> `estimate-guppi-config-fills-the-main-branch`: the new check of the key and its two readers.
> **＋** `rule-guppi-config`: the page whose Render is `guppi.toml`, which gains the key.
> **＋** `.guppi/guppi/config.py`: the settings module, which gains the key, its judgment and its reader.
> **＋** `.guppi/guppi/render.py`: the render, whose placeholders take the key.
> **＋** `.guppi/tests/test_config.py`: the tests of the reader.
> **＋** `.guppi/tests/test_render.py`: the tests of the placeholder.

> **when:**
> `guppi render` builds the governed files from the `## Render` of the render pages, or a script of `.guppi/guppi/` asks `main_branch` of `.guppi/guppi/config.py` for the name of the main branch of the project.

> **then:**
> Each `{{main_branch}}` in the `## Render` of a render page becomes, in the file it governs, the value of the key `main_branch` that the `## Render` of `rule-guppi-config` sets, as it stands.
> **＋** The page keeps the placeholder, so the next render after a changed name writes the new name.
> **＋** `main_branch` of `.guppi/guppi/config.py` gives the value of the key `main_branch` of `guppi.toml` at the root of the project, and `main` where the file is missing, does not parse or holds no such key.
> **＋** The render and `main_branch` judge the value by one function of `.guppi/guppi/config.py`: a value that is not a string, is empty or holds a space is an error that names its source and the key.
> **＋** A `{{main_branch}}` while the `## Render` of `rule-guppi-config` holds no key `main_branch`, or a value that function refuses, stops the run: nothing is written, the page and the key go to stderr, `guppi render` exits 1, and `guppi render --sync` exits 0 with the same line.
> **＋** The `## Render` of `rule-guppi-config` holds `main_branch = "main"`, and `guppi.toml` holds it after the render.
> **－** A run in which no `## Render` holds a placeholder reads no `rule-guppi-config` and needs none.
> **－** The render reads the name from the `## Render` of `rule-guppi-config`, never from `guppi.toml`, which is its own output.

```then
create:
- slug: estimate-guppi-config-fills-the-main-branch
  ref: rule-guppi-config
  kind: QA
  purpose: Whether the render puts the value of the key main_branch of the Render of rule-guppi-config in place of each {{main_branch}}, the code reads it from guppi.toml with main where it is missing, and both judge the value by one function
  method: 'uv run --project .guppi pytest .guppi/tests/test_config.py -k main_branch and uv run --project .guppi pytest .guppi/tests/test_render.py -k main_branch; by hand, after the librarian''s run of the session that sets this method: guppi.toml read for main_branch = "main" and the output of uv run --project .guppi guppi render --check, recorded in the estimate line'
  tags:
  - harness
  - render
  - git
update:
- slug: rule-guppi-config
  replace:
  - old: setup_done = true
    new: |-
      main_branch = "main"
      setup_done = true
  - old: The questions asked at setup, these two commands among them, belong to the setup Case of a project
    new: 'The key `main_branch` names the main branch of the project: the render puts its value where another Render writes `{{main_branch}}`, and a Render with that placeholder stops the run while this Render holds no such key, as for a language; the code reads it from `guppi.toml` by `main_branch` of `.guppi/guppi/config.py`, which gives `main` where the file or the key is missing; one function of that module judges the value for both; this Render holds `main`, the clean version ships it, and the setup Case of a project writes the name of its own main branch (as set in case 1070.1). The questions asked at setup, these two commands among them, belong to the setup Case of a project'
  change: the key main_branch names the main branch; the render fills {{main_branch}} and the code reads it, main where guppi.toml holds no key
```

```tasks
- [x] update `rule-guppi-config`
- [x] create `estimate-guppi-config-fills-the-main-branch`
- [x] `.guppi/guppi/config.py`: `BRANCH_KEY = "main_branch"` and `DEFAULT_BRANCH = "main"`; one function that judges the value of the key in a parsed text — the value, none where the key is missing, a `ConfigError` that names the source and the key for a value that is not a string, is empty or holds a space; `main_branch(project_dir)`, which gives `DEFAULT_BRANCH` for a missing file, a text that does not parse or a missing key; the docstring names the key, its judgment and its reader, a pointer to a case only in a bracket at the end of its sentence.
- [x] `.guppi/guppi/render.py`: `fill_placeholders` takes `main_branch` beside the language keys and puts in the value that the judgment of `config.py` gives over the Render of `rule-guppi-config`, a missing key or a refused value a `RenderError` that names the page and the key; the docstring names the placeholder, a pointer to a case only in a bracket at the end of its sentence.
- [x] `.guppi/tests/test_config.py`: tests whose names hold `main_branch`: the value of a written `guppi.toml`; `main` for a missing file, a text that does not parse and a missing key; an error for a value that is a number, empty or holds a space.
- [x] `.guppi/tests/test_render.py`: tests whose names hold `main_branch`: a Render with `{{main_branch}}` takes `trunk` from the Render of `rule-guppi-config`, the page keeps the placeholder, a changed value reaches the file at the next render, `guppi.toml` does not set it, and a missing key or a value with a space writes nothing and names the key.
- [x] `uv run --project .guppi guppi render`: `guppi.toml`
- [ ] read `estimate-guppi-config-fills-the-main-branch`
```

### Case 1070.2 — The box check refuses the main branch that guppi.toml names

> **given:**
> `estimate-spec-box-refuses-a-stale-spec`: its Criterion is replaced whole.
> **＋** `rule-spec-box`: the page of `/box`, whose Purpose names the shared branch.
> **＋** `.guppi/guppi/box.py`: the check, which reads the name in place of its constant.
> **＋** `.guppi/guppi/config.py`: the reader of the name that the check imports.
> **＋** `.guppi/guppi/materialize.py`: the mark of a conserved Spec and the parser of its items.
> **＋** `.guppi/guppi/caseid.py`: the reading of a Case id.
> **＋** `vault/raw/<date>/<HHMM>/` and `spec/<date>-<HHMM>`: the folder of a conserved Spec and its branch.
> **＋** `.guppi/tests/test_box.py`: the tests of the check.

> **when:**
> Someone runs `uv run --project .guppi guppi box --check <folder> --session <id>`, where `<folder>` is a folder `vault/raw/<date>/<HHMM>/` and `<id>` is the session id of a `hi` line.

> **then:**
> It prints one line for each reason the Spec cannot run now, and exits 1 when it prints any; with no reason it prints nothing and exits 0.
> **＋** A folder that `is_carried_over` of `.guppi/guppi/materialize.py` does not judge marked is one reason, and so is a folder for which no branch `spec/<date>-<HHMM>` exists.
> **＋** A current branch that is the main branch, the name that `main_branch` of `.guppi/guppi/config.py` reads from `guppi.toml`, `main` where `guppi.toml` holds no key, is one reason: the shared branch is never the main branch.
> **＋** A value of the key `main_branch` of `guppi.toml` that `.guppi/guppi/config.py` refuses is one reason, naming the file and the key.
> **＋** A decision line other than a `defer` in the ledger of the session's folder is one reason, naming its Case.
> **＋** A live page named by an `update`, `delete` or `defer` item of the folder's `spec.md` is one reason when a line of its History names the Decision page of a later Case, read by `.guppi/guppi/caseid.py`: a plain id whose whole part is higher than that of every Case of that Spec with a plain id, when the Spec holds one; an id of a sprint whose number is higher than that of every Case of that Spec of the same sprint; or an id of a sprint of which the Spec holds no Case, on a History line dated on or after the date of the folder. The line names the page and that Decision page.
> **＋** A slug that a `create` item of that Spec names and a live page carries is one reason, naming the slug.
> **－** The check writes nothing, switches no branch, and opens no page beyond those the Spec names.

```then
update:
- slug: rule-spec-box
  replace:
  - old: the shared branch is never `main`.
    new: the shared branch is never the main branch that `guppi.toml` names.
  change: the shared branch is never the main branch that guppi.toml names
- slug: estimate-spec-box-refuses-a-stale-spec
  set:
    status: pending
    purpose: Whether guppi box --check refuses a conserved Spec whose folder lacks carry.md or its branch, a run from the main branch that guppi.toml names or a value of that key the settings refuse, a session that ratified a Case of its own, a page of the Spec changed by a later Case, and a page the Spec creates that now stands — and passes any other
  change: the Criterion replaced whole — the check refuses the main branch that guppi.toml names, main where it names none
```

```tasks
- [x] update `rule-spec-box`
- [x] update `estimate-spec-box-refuses-a-stale-spec`
- [x] `.guppi/guppi/box.py`: `SHARED_NEVER` gives way to `main_branch` of `.guppi/guppi/config.py`, read once per check; the reason keeps its words with that name in place of `main`, `box: the current branch is <name> — the shared branch never is`, so the test of a run from `main` passes as it stands; a `ConfigError` of it is one reason line; the docstring names the main branch that `guppi.toml` names, a pointer to a case only in a bracket at the end of its sentence.
- [x] `.guppi/tests/test_box.py`: a test whose `guppi.toml` holds `main_branch = "trunk"`: on the branch `trunk` the check prints the reason, on a branch `main` it prints none of that kind; a test whose value holds a space prints one reason that names the key.
- [x] read `estimate-spec-box-refuses-a-stale-spec`
```

### Case 1070.3 — The setup Case proposes the name of the main branch from the branch /hi printed

> **given:**
> `estimate-morph-sets-up-the-project-at-the-first-hi` and `estimate-sprint-plugin-setup-takes-a-main-branch-other-than-main`: the check whose Criterion is replaced whole, and the one-off check of a new install that Case 1070.7 creates.
> **＋** `rule-morph`: the setup and the order of a new project.
> **＋** `rule-skill-setup` and `.claude/skills/setup/SKILL.md`: the skill `/setup`, which writes the prompt of the setup Case, and the file rendered from it.
> **＋** `rule-plugin-install`, `/guppi:install`, `/hi` and `/sprint-open`: the install before the setup, the command that starts it and the skill that follows it.
> **＋** `.guppi/`, `vault/`, `.claude/` and `guppi-set-aside/`: the folders of GUPPI and of the files set aside, which the look for code of the project leaves out.
> **＋** `rule-ledger-write`: the ledger hook that writes the lines of the setup Case.
> **＋** `rule-guppi-config`: the page whose Render the setup Case updates.
> **＋** `entity-sprint-plugin`: the sprint page whose Backlog holds this item.

> **when:**
> Someone reads the `## Render` of `rule-skill-setup` and the `## Purpose` of `rule-morph`, in the Spec at the Retro of the session that ratified this Criterion, or after it the Render of `rule-skill-setup` in `.claude/skills/setup/SKILL.md`, rendered from it, and the `## Purpose` of `rule-morph` in the Spec of the last session that changed it.

> **then:**
> The two texts say that, after `/guppi:install` of `rule-plugin-install`, the first `/hi` in a project whose `guppi.toml` holds `setup_done = false` starts `/setup`, which puts the setup Case of `rule-morph` first, before the opening Case of the first sprint and before the Frontier.
> **＋** They say that step 2 of `/setup` writes the branch that `/hi` printed under `Branch:` into the prompt of the setup Case.
> **＋** They say that the setup Case takes the name of the project's folder of saved transcripts from the path of the project, and the name of its main branch from that branch, `main` where that line names no branch, and shows each for the person to correct.
> **＋** They say that it asks the person for the language of the repository, the language of the chat and the description of the project, and that, where the file paths of the project show a file of a programming language outside `.guppi/`, `vault/`, `.claude/` and `guppi-set-aside/`, one plain question asks how the project's own tests and style check run beside GUPPI's, whose commands stay first in the keys `test` and `style`.
> **＋** They say that the `update` of `rule-guppi-config` of the setup Case holds `main_branch` with the name of the main branch, and that the ledger hook of `rule-ledger-write` writes its decision lines though no sprint is open.
> **＋** They say that the setup Case holds a render line for each file its updates write and for each file whose `## Render` names the main branch by the placeholder of the key `main_branch`, and that the librarian's run of that session renders them.
> **＋** They say that the reply that acknowledges the setup Case shows no Frontier and ends with the open question on what the first sprint is to build, and that `/sprint-open` starts in the same session with the person's answer.
> **－** They say that `/guppi:install` is no Case and that the person ratifies nothing at it.
> **－** They say that the setup Case asks for no category set and no git remote, asks no question on the main branch, reads no code of the project and creates no page.
> **－** They say that, where the file paths show no such file, it asks nothing on tests or style, and that its question names no key of `guppi.toml`.
> **－** The reading does not run the setup: a new install is read by the one-off Estimate `estimate-sprint-plugin-setup-takes-a-main-branch-other-than-main`.

```then
update:
- slug: rule-morph
  replace:
  - old: The code takes the main branch to be `main` in every project, and the setup does not change it (as set in case 1017.4).
    new: The setup Case sets the name of the main branch of the project in `guppi.toml`, which the code and the skills read (as set in case 1070.3).
  - old: 'The skill takes the name of the project''s folder of saved transcripts from the path of the project, and asks the person only for the rest:'
    new: 'The skill takes the name of the project''s folder of saved transcripts from the path of the project, and the name of its main branch from the branch that `/hi` prints under `Branch:`, `main` where that line names no branch, shows each for the person to correct, and asks the person only for the rest:'
  change: the setup Case proposes the name of the main branch from the branch /hi printed and sets it in guppi.toml
- slug: rule-skill-setup
  replace:
  - old: 'not the time of the folder —, and write into the prompt of the call that the setup Case:'
    new: 'not the time of the folder —, and write into the prompt of the call the branch that `/hi` printed under `Branch:`, and that the setup Case:'
  - old: takes the name of the folder of the saved transcripts of this project under `~/.claude/projects` from the path of the project, and shows it for the person to correct;
    new: takes the name of the folder of the saved transcripts of this project under `~/.claude/projects` from the path of the project, and the name of its main branch from the branch of `Branch:` that the prompt names, `main` where that line names no branch, and shows each for the person to correct, with no question on it;
  - old: holds an `update` of `rule-guppi-config` whose Render holds the languages, the commands the person gave after GUPPI's commands, which leave neither key, and `setup_done = true`,
    new: holds an `update` of `rule-guppi-config` whose Render holds the languages, the commands the person gave after GUPPI's commands, which leave neither key, `main_branch` with the name of the main branch, and `setup_done = true`,
  - old: with a render line for each file they write;
    new: with a render line for each file they write and for each file whose Render names the main branch by the placeholder of the key `main_branch`, since a new name reaches such a file only at its render;
  - old: asks for no category set, no name of the main branch and no git remote,
    new: asks for no category set and no git remote,
  - old: renders `guppi.toml`, `CLAUDE.md` and `.claude/settings.json` from them;
    new: renders `guppi.toml`, `CLAUDE.md`, `.claude/settings.json` and each file whose Render names the main branch by the placeholder of the key `main_branch` from them;
  change: the branch /hi printed goes into the prompt of the setup Case, which takes the name of the main branch from it, shows it for correction, writes it into the key main_branch and renders each file that names the main branch by its placeholder
- slug: estimate-morph-sets-up-the-project-at-the-first-hi
  set:
    status: pending
    purpose: Whether the Render of rule-skill-setup and the Purpose of rule-morph say that the first /hi after /guppi:install, in a project whose guppi.toml holds setup_done = false, puts one setup Case first, with the values it finds — the folder of saved transcripts and the main branch from the branch /hi printed, which goes into its prompt — and the values the person gives, and that the librarian's run of that session renders the settings and each file that names the main branch by the key main_branch
    method: 'by hand, at the Retro of the session that sets this Criterion: the new Render of rule-skill-setup and the new Purpose of rule-morph in the Spec read against the Criterion, and after it the Render of rule-skill-setup in .claude/skills/setup/SKILL.md, rendered from it, recorded in the estimate line'
  change: the Criterion replaced whole — the texts of the setup say that the setup Case proposes the name of the main branch from the branch /hi printed and writes it into guppi.toml; purpose and method read those texts in the Spec at Retro, and the install moves to a one-off Estimate of the sprint page
- slug: entity-sprint-plugin
  replace:
  - old: '- The name of the main branch: a project whose main branch is not main sets its name at the setup, and the code and the skills read it; taken out of rule-morph (case 1017.4)'
    new: ''
  - old: '- The sprint turn and GitHub: the repository on GitHub set up so that a pull request from another person is easy to review (case 794)'
    new: |-
      - The sprint turn and GitHub: the repository on GitHub set up so that a pull request from another person is easy to review (case 794)
      - The name of the main branch: a project whose main branch is not main sets its name at the setup, and the code and the skills read it (case 1070)
  change: the item of the name of the main branch leaves the Backlog for Closed
```

```tasks
- [x] update `rule-morph`
- [x] update `rule-skill-setup`
- [x] update `estimate-morph-sets-up-the-project-at-the-first-hi`
- [x] update `entity-sprint-plugin`
- [x] `uv run --project .guppi guppi render`: `.claude/skills/setup/SKILL.md`
- [x] `uv run --project .guppi guppi sprint`
- [x] read `estimate-morph-sets-up-the-project-at-the-first-hi`
```

### Case 1070.4 — The skills that ship name the main branch by its setting

> **given:**
> `estimate-sprint-plugin-skills-name-the-main-branch-by-its-setting`: the new one-off check of the texts.
> **＋** `rule-guppi-config` and `rule-morph`: the page whose Render sets the key `main_branch`, and the setup Case whose `update` of that page sets the name before the render writes it.
> **＋** `rule-git-context`: the step of `/hi` in a folder with no git repository.
> **＋** `rule-skill-sprint-open`: the skill that merges the closed sprint and makes the branch of the next.
> **＋** `rule-skill-sprint-close`: the skill that refuses a branch that does not hold the main branch.
> **＋** `rule-work-mode`: the skill `/work`, which does not start on the main branch.
> **＋** `rule-where-to-stop`: the stops of the run, one on the main branch.
> **＋** `.guppi/guppi/gitstate.py`: the code of `Branch:`, whose docstring names the main branch.

> **when:**
> After the librarian's run of the session that ratified this check, someone reads the `## Render` and the `## Purpose` of `rule-git-context`, `rule-skill-sprint-open`, `rule-skill-sprint-close`, `rule-work-mode` and `rule-where-to-stop`, and the files that `guppi render` writes from them.

> **then:**
> Each place where those Renders name the main branch of the project, in prose or in a `git` or `gh` command, writes `{{main_branch}}`.
> **＋** The file each of them governs writes there the value of `main_branch` that the `## Render` of `rule-guppi-config` sets, and `uv run --project .guppi guppi render --check` exits 0.
> **＋** Step 4 of the Render of `rule-skill-sprint-open` says that, in a session that ratified the setup Case of `rule-morph`, the main branch of that step is the name that the `update` of `rule-guppi-config` of that Case sets, and that the step writes that name into the prompt of the opening Case beside the branch of `Branch:`.
> **＋** The paragraph of the Render of `rule-work-mode` on the branch and the fifth condition of `rule-where-to-stop` say that, where the Spec holds the setup Case of `rule-morph`, the main branch is the name that its `update` of `rule-guppi-config` sets.
> **＋** The `## Purpose` of `rule-git-context` and of `rule-work-mode` names the main branch in words, not as `main`.
> **－** The `gh` placeholders `{owner}` and `{repo}` of `rule-skill-sprint-close` stay as they are.

```then
create:
- slug: estimate-sprint-plugin-skills-name-the-main-branch-by-its-setting
  ref: entity-sprint-plugin
  kind: QA
  purpose: Whether the Renders of the skills that ship name the main branch by {{main_branch}}, or, in the session of a ratified setup Case, by the name that Case sets, which /sprint-open writes into the prompt of the opening Case, their files by the name that rule-guppi-config sets, and the Purposes of rule-git-context and rule-work-mode by words
  method: 'by hand, after the librarian''s run of the session that sets this method: a Grep of the pages and the files the Criterion names for main and for {{main_branch}}, and the output of uv run --project .guppi guppi render --check, read against the Criterion, recorded in the estimate line'
  once: true
  tags:
  - sprint
  - git
  - harness
update:
- slug: rule-git-context
  replace:
  - old: tell the person to type `! git init -b main`, which names the first branch `main`
    new: tell the person to type `! git init -b {{main_branch}}`, which names the first branch `{{main_branch}}`
  - old: On `main` or a working branch
    new: On the main branch or a working branch
  change: the step in a folder with no git repository names the main branch by {{main_branch}}
- slug: rule-skill-sprint-open
  replace:
  - old: the merge of `main` into `<id>`
    new: the merge of `{{main_branch}}` into `<id>`
  - old: 4. Write into the same prompt the branch that `/hi` printed under `Branch:`, and whether
    new: 4. The main branch of this project is `{{main_branch}}`, but in a session that ratified the setup Case of `rule-morph` it is the name that the `update` of `rule-guppi-config` of that Case sets, since `guppi.toml` and this skill take that name only at the librarian's run of the session; where this step names `{{main_branch}}`, it means the main branch so found. Write into the same prompt that name, the branch that `/hi` printed under `Branch:`, and whether
  - old: When the branch is not `main`, the closed sprint ran on it
    new: When the branch is not `{{main_branch}}`, the closed sprint ran on it
  - old: '`gh pr create --base main --fill`, `gh pr checks <branch> --watch`'
    new: '`gh pr create --base {{main_branch}} --fill`, `gh pr checks <branch> --watch`'
  - old: open its pull request into `main`, wait
    new: open its pull request into `{{main_branch}}`, wait
  - old: '`git switch main`, `git merge --ff-only origin/main`, `git switch -c <id>` and `git branch -d <branch>`, so that the local `main` follows `origin/main`;'
    new: '`git switch {{main_branch}}`, `git merge --ff-only origin/{{main_branch}}`, `git switch -c <id>` and `git branch -d <branch>`, so that the local `{{main_branch}}` follows `origin/{{main_branch}}`;'
  - old: shows no open pull request, `gh pr create --base main --fill`
    new: shows no open pull request, `gh pr create --base {{main_branch}} --fill`
  - old: 'The opening Case does not merge `main` into the closed branch: `/sprint-close` closes no sprint whose branch does not hold `main`, so `main` was merged into it before the close'
    new: 'The opening Case does not merge `{{main_branch}}` into the closed branch: `/sprint-close` closes no sprint whose branch does not hold `{{main_branch}}`, so `{{main_branch}}` was merged into it before the close'
  - old: When the branch is `main`, the opening Case holds as its first task line
    new: When the branch is `{{main_branch}}`, the opening Case holds as its first task line
  change: the merge and branch tasks of the opening Case name the main branch by {{main_branch}}, or, in the session of the setup Case, by the name that Case sets, which goes into the prompt of the opening Case
- slug: rule-skill-sprint-close
  replace:
  - old: '`gh api repos/{owner}/{repo}/commits/main --jq .sha` prints `<hash>`, the commit of `main` on GitHub. When `git merge-base --is-ancestor <hash> HEAD` exits other than 0, the branch does not hold `main`,'
    new: '`gh api repos/{owner}/{repo}/commits/{{main_branch}} --jq .sha` prints `<hash>`, the commit of `{{main_branch}}` on GitHub. When `git merge-base --is-ancestor <hash> HEAD` exits other than 0, the branch does not hold `{{main_branch}}`,'
  - old: tell the person to bring the branch up to `main` first
    new: tell the person to bring the branch up to `{{main_branch}}` first
  - old: 'the merge of the sprint''s branch into `main`:'
    new: 'the merge of the sprint''s branch into `{{main_branch}}`:'
  change: the check of the branch before the close names the main branch by {{main_branch}}
- slug: rule-work-mode
  replace:
  - old: If the branch is `main` and the Spec holds
    new: The main branch is `{{main_branch}}`, but where the Spec holds the setup Case of `rule-morph`, it is the name that the `update` of `rule-guppi-config` of that Case sets, since this skill takes that name only at the librarian's run of the session; where this paragraph names `{{main_branch}}`, it means the main branch so found. If the branch is `{{main_branch}}` and the Spec holds
  - old: 'With any other Spec on `main`, stop and say so: Work Mode does not start on `main`.'
    new: 'With any other Spec on `{{main_branch}}`, stop and say so: Work Mode does not start on `{{main_branch}}`.'
  - old: It stops on `main`, but for the branch task
    new: It stops on the main branch that `guppi.toml` names, or, where the Spec holds the setup Case, on the name that Case sets, but for the branch task
  change: Work Mode stops on the main branch that guppi.toml names, by {{main_branch}}, or on the name that the setup Case of the Spec sets
- slug: rule-where-to-stop
  replace:
  - old: '5. The branch is `main`:'
    new: '5. The branch is the main branch, `{{main_branch}}`, or, where the Spec holds the setup Case of `rule-morph`, the name that its `update` of `rule-guppi-config` sets:'
  change: the stop on the main branch names it by {{main_branch}}, or by the name that the setup Case of the Spec sets
```

```tasks
- [x] update `rule-git-context`
- [x] update `rule-skill-sprint-open`
- [x] update `rule-skill-sprint-close`
- [x] update `rule-work-mode`
- [x] update `rule-where-to-stop`
- [x] create `estimate-sprint-plugin-skills-name-the-main-branch-by-its-setting`
- [x] `.guppi/guppi/gitstate.py`: the docstring says that the local main branch follows its branch on `origin` in the opening Case of a sprint, by `git fetch origin` and `git merge --ff-only`, the name being the one `guppi.toml` sets; the sentence on `/merge-main` says that, where the project holds that skill, a sprint branch takes the main branch by its merge Case; the second paragraph, which `parser` takes as the description of the command, stays as it is, and a pointer to a case stands only in a bracket at the end of its sentence.
- [x] `uv run --project .guppi guppi render`: `.claude/skills/hi/SKILL.md`
- [x] `uv run --project .guppi guppi render`: `.claude/skills/sprint-open/SKILL.md`
- [x] `uv run --project .guppi guppi render`: `.claude/skills/sprint-close/SKILL.md`
- [x] `uv run --project .guppi guppi render`: `.claude/skills/work/SKILL.md`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/where-to-stop.md`
- [x] `uv run --project .guppi guppi sprint`
- [ ] read `estimate-sprint-plugin-skills-name-the-main-branch-by-its-setting`
```

### Case 1070.5 — The librarian, the pages on who writes the vault and the glossary name the main branch by its setting or in words

> **given:**
> `estimate-sprint-plugin-vault-writer-texts-name-the-main-branch`: the new one-off check of the texts.
> **＋** `rule-guppi-config`: the page whose Render sets the key `main_branch`.
> **＋** `rule-documentation`: the librarian's agent file, which names what a merge into a branch writes.
> **＋** `rule-page-generation`: the script that writes the vault, with the same exception.
> **＋** `rule-vault-layout`: the layout of the vault, with the same exception.
> **＋** `entity-glossary`: the terms, whose rows Librarian and Work Mode name the main branch.
> **＋** `.claude/agents/librarian-guppi.md` and `vault/wiki/glossary.md`: the files rendered from `rule-documentation` and from `entity-glossary`.

> **when:**
> After the librarian's run of the session that ratified this check, someone reads the `## Render` of `rule-documentation`, the `## Purpose` of `rule-page-generation` and `rule-vault-layout`, the rows Librarian and Work Mode of `entity-glossary`, and the files `.claude/agents/librarian-guppi.md` and `vault/wiki/glossary.md`.

> **then:**
> The `## Render` of `rule-documentation` names the main branch as `{{main_branch}}` where it says what a merge into a branch writes, and `.claude/agents/librarian-guppi.md` writes there the value of `main_branch` that the `## Render` of `rule-guppi-config` sets.
> **＋** The `## Purpose` of `rule-page-generation` and of `rule-vault-layout` names the main branch in words, not as `main`, where it says what a merge into a branch writes.
> **＋** The rows Librarian and Work Mode of `entity-glossary` and of `vault/wiki/glossary.md` name the main branch in words, not as `main`.

```then
create:
- slug: estimate-sprint-plugin-vault-writer-texts-name-the-main-branch
  ref: entity-sprint-plugin
  kind: QA
  purpose: Whether the librarian's agent file names the main branch by {{main_branch}}, and the Purposes of rule-page-generation and rule-vault-layout and the rows Librarian and Work Mode of the glossary by words
  method: 'by hand, after the librarian''s run of the session that sets this method: a Grep of the pages and the files the Criterion names for main and for {{main_branch}}, read against the Criterion, recorded in the estimate line'
  once: true
  tags:
  - sprint
  - git
  - harness
update:
- slug: rule-documentation
  replace:
  - old: but for what a merge of `main` into a branch writes
    new: but for what a merge of `{{main_branch}}` into a branch writes
  change: the librarian's exception names the main branch by {{main_branch}}
- slug: rule-page-generation
  replace:
  - old: 'a merge of `main` into a branch writes: the joined text of a page that both a branch and `main` changed'
    new: 'a merge of the main branch into a branch writes: the joined text of a page that both a branch and the main branch changed'
  change: the exception of a merge names the main branch in words
- slug: rule-vault-layout
  replace:
  - old: 'a merge of `main` into a branch writes: the joined text of a page that both a branch and `main` changed'
    new: 'a merge of the main branch into a branch writes: the joined text of a page that both a branch and the main branch changed'
  change: the exception of a merge names the main branch in words
- slug: entity-glossary
  replace:
  - old: for what a merge of `main` into a branch writes
    new: for what a merge of the main branch into a branch writes
  - old: 'on a branch other than `main`:'
    new: 'on a branch other than the main branch that `guppi.toml` names:'
  change: the rows Librarian and Work Mode name the main branch in words
```

```tasks
- [x] update `rule-documentation`
- [x] update `rule-page-generation`
- [x] update `rule-vault-layout`
- [x] update `entity-glossary`
- [x] create `estimate-sprint-plugin-vault-writer-texts-name-the-main-branch`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/librarian-guppi.md`
- [x] `uv run --project .guppi guppi glossary`
- [x] `uv run --project .guppi guppi sprint`
- [ ] read `estimate-sprint-plugin-vault-writer-texts-name-the-main-branch`
```

### Case 1070.6 — The purposes of the shipped Estimates of the sprint skills and of /work name the main branch in words

> **given:**
> `estimate-skill-sprint-close-leads-the-closing-session`: the check of `/sprint-close`, whose `purpose` names `origin/main`.
> **＋** `estimate-skill-sprint-open-merges-the-closed-sprint-branch`: the check of the merge tasks of `/sprint-open`, whose `purpose` names `main`.
> **＋** `rule-work-mode` and `.claude/skills/work/SKILL.md`: the page of `/work` and the skill rendered from it, which the new `method` reads.
> **＋** `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`: the check of `/work`, whose `purpose` names `main`.
> **＋** `estimate-clean-branch-ships-neutral-texts`: the check that no `purpose` of a shipped Estimate holds only in the repository of GUPPI.

> **when:**
> Someone reads the `purpose` of `estimate-skill-sprint-close-leads-the-closing-session`, `estimate-skill-sprint-open-merges-the-closed-sprint-branch` and `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, and the `method` of the last.

> **then:**
> Each `purpose` names the main branch of the project in words, not as `main` or `origin/main`.
> **＋** The `method` of `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` names no branch, waits for no moment of a past session and reads no transcript of a session: it runs `uv run --project .guppi guppi render --check` and reads the skill rendered from `rule-work-mode` against each line of the Criterion.
> **－** Their `## Criterion` and their status stay as they are.

```then
update:
- slug: estimate-skill-sprint-close-leads-the-closing-session
  set:
    purpose: Whether /sprint-close refuses on a branch that does not hold the main branch of origin and in a session that ratified another Case, puts off the other Cases lines, sorts the readings and has the closing Case built with the close line, while orchestration.md no longer holds the steps of the closing session
  change: the purpose names the main branch in words
- slug: estimate-skill-sprint-open-merges-the-closed-sprint-branch
  set:
    purpose: Whether /sprint-open has the opening Case write the close line last, with the /merge-main line just before it only where the project holds that skill, push the closed sprint's branch and open its pull request into the main branch after the person's word, merge it with a merge commit after its checks pass when the person is the owner, and move the work to a branch named by the new sprint, as the first tasks of Work Mode, with a stop on a refusal, and on the main branch make that branch by one first task with no stop
  change: the purpose names the main branch in words
- slug: estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline
  set:
    purpose: Whether /work loads while guppi check or guppi test finds something, stops on the main branch but for the branch task of the opening Case of a sprint, which it runs first, writes the baseline of uv run --project .guppi guppi test and uv run --project .guppi guppi check into work.md before the first change — the exit code of each as the last line of its preamble line names it — and keeps it on a resume, runs the tasks of the Spec of the session or of the folder /box gives it in order with their ticks but leaves a guppi sprint-close line to the librarian, names that folder under Conserved Spec and deletes its carry.md, marks an expected red under Expected red, runs the check of the plan before the first task of a Case ratified in Work Mode, stops on its finding and ticks a task of that Case whose work already stands, and after the last task runs uv run --project .guppi guppi test in full and holds each failing test against the baseline, fixing a new one within ratified work
    method: 'by hand: uv run --project .guppi guppi render --check, and .claude/skills/work/SKILL.md, rendered from rule-work-mode, read against each line of the Criterion, recorded in the estimate line'
  change: the purpose names the main branch in words, and the method names no branch and reads the render check and the rendered skill, no transcript of a session
```

```tasks
- [x] update `estimate-skill-sprint-close-leads-the-closing-session`
- [x] update `estimate-skill-sprint-open-merges-the-closed-sprint-branch`
- [x] update `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
```

### Case 1070.7 — A new install whose main branch is master takes that name at its setup

> **given:**
> `estimate-sprint-plugin-setup-takes-a-main-branch-other-than-main`: the new one-off check of a new install.
> **＋** `entity-sprint-plugin`: the live sprint page, the target of the one-off check.
> **＋** `rule-morph`: the setup Case of a new project.
> **＋** `rule-skill-setup`: the skill `/setup`, which builds that Case.
> **＋** `rule-guppi-config`: the page whose Render sets the key `main_branch`.
> **＋** `/guppi:install` and `/hi`: the install and the command that starts the setup.
> **＋** `.claude/skills/sprint-open/SKILL.md`, `.claude/skills/sprint-close/SKILL.md`, `.claude/skills/work/SKILL.md` and `vault/wiki/where-to-stop.md`: the rendered texts that name the main branch.

> **when:**
> In a git project made by `git init -b master`, the person installs the plugin `guppi` from a copy that `uv run --project .guppi guppi ship --allow-draft` wrote after the librarian's run of the session that ratified this check, types `/guppi:install`, reopens Claude Code, types `/hi`, and takes that session to its librarian's run.

> **then:**
> The setup Case of `rule-morph`, which `/setup` of `rule-skill-setup` builds, shows `master` as the name of the main branch for the person to correct, and asks no question on it.
> **＋** Its `update` of `rule-guppi-config` holds `main_branch = "master"`, and it holds a render line for each of the four files below.
> **＋** In that session, the opening Case of the first sprint takes `master` as the main branch: its first task line runs `git switch -c <id>`, with no push and no pull request, and Work Mode runs that line first and the rest of the Spec on the branch `<id>`.
> **＋** After that librarian's run, `guppi.toml` holds `main_branch = "master"`, and `.claude/skills/sprint-open/SKILL.md`, `.claude/skills/sprint-close/SKILL.md`, `.claude/skills/work/SKILL.md` and `vault/wiki/where-to-stop.md` name `master` in each place where the copy names `main` as the main branch.

```then
create:
- slug: estimate-sprint-plugin-setup-takes-a-main-branch-other-than-main
  ref: entity-sprint-plugin
  kind: QA
  purpose: Whether a new install in a git project made by git init -b master has its setup Case show master as the main branch for correction, its opening Case and Work Mode take master as the main branch in the same session, and its librarian's run write main_branch = "master" into guppi.toml and master into the rendered skills that name the main branch
  method: 'by hand, after the librarian''s run of the session that sets this method: the plugin guppi installed from a copy that uv run --project .guppi guppi ship --allow-draft wrote into a local folder, in a git project made by git init -b master, /guppi:install typed, Claude Code reopened, /hi typed and that session taken to its librarian''s run, the transcript of that session under ~/.claude/projects, its ledger and the files written in it read against the Criterion, recorded in the estimate line'
  once: true
  tags:
  - sprint
  - git
  - plugin
```

```tasks
- [x] create `estimate-sprint-plugin-setup-takes-a-main-branch-other-than-main`
- [x] `uv run --project .guppi guppi sprint`
- [ ] read `estimate-sprint-plugin-setup-takes-a-main-branch-other-than-main`
```

## Case 1071 — A check that reads a transcript is split into a lasting check and a one-off check

> **context:**
> An Estimate says how a promise of a rule is checked, and its `method` names the reading. Many lasting Estimates on rule pages read the transcript of a session under `~/.claude/projects/`, to see what an agent did. A Grep `^method:.*(transcript|\.jsonl|~/.claude/projects)` over `vault/wiki/estimates/` printed 59 files, a few of them tests over made-up transcripts. Such a reading waits for its event and often fails, since an agent does not always do what its text says. The ledger of session 1336, `vault/raw/2026-11-26/1336/ledger.md`, records `estimate-orchestration-dispatches-case-guppi-at-a-level` and `estimate-case-build-settles-form-by-itself` as `failed` on the transcript of session 2003. While an Estimate stands `failed`, its rule page with `core: true` stops the clean build: `is_draft_core` of `.guppi/guppi/pages.py`, which `drafts` of `.guppi/guppi/ship.py` calls, accepts a `draft` page with `core: true` that was never built or that has a failed Estimate. Cases 1019.2 and 1019.3 split one such Estimate into a lasting one that reads the Render and a one-off one of `entity-sprint-plugin`, and Case 1019.4 put the general question on the `## Backlog` of that page.
>
> The person chose three things. First, the split becomes the rule for each Estimate that a Case creates, gives a new `method` or gives a new Criterion; the Estimates that stand keep their readings until then. Second, the text of `rule-case-protocol` and `rule-estimates-schema` says it, and `guppi prespec --check` reports a break. Third, a Criterion written back word for word is no new Criterion; the merge Case of `.claude/skills/merge-main/SKILL.md` writes one back so as to set an Estimate `pending`, so `/merge-main` keeps its steps. Case 1071.1 sets the text and Case 1071.2 the check. That split is a choice of form, since the two can fail apart and need different fixes (`rule-atomicity`).
>
> In the Render of `rule-case-protocol`, the paragraph on a `create` of an Estimate holds the sentences that say where a reading stands. The `method` holds only what runs in the Case's own session, or a reading that waits for an event it names. A reading by hand names where its evidence is saved, a transcript among the places. An Estimate of a sprint page may wait for a later session of its sprint. A one-off Estimate targets the live sprint page. None of them becomes false, since a one-off Estimate still reads a transcript, so the new sentences stand after the last of them. The description of `method` in the Render of `rule-estimates-schema` says the same of the evidence and gains the same sentences. The description of `once` names a transcript among the states that a one-off Estimate checks. Both pages carry `core: true`, so each pointer stands in a bracket at the end of its sentence. The line of `entity-sprint-plugin` leaves `## Backlog` by one pair whose `old` is that line alone and whose `new` is empty. Case 1070 of this session takes up the item of the line above it, the name of the main branch, so this pair touches no other line of the page. The new Estimate of Case 1071.1 sits on `rule-case-protocol`, whose Render `case-guppi` reads whole. Its `method` reads the Spec at Retro and no transcript, so it keeps the rule it sets. That Estimate is the check of the text, a choice of form: `estimate-estimates-schema-method-names-its-evidence` checks where a reading saves its evidence, another promise, which the new text leaves true, so it stands. `estimate-case-protocol-loaded` promises the render only (case 378.5). `estimate-case-protocol-case-form` speaks of the sections of a built Case. `estimate-estimates-schema-checked` speaks of the lists that lint reads, which do not change. So these stand. On the sprint page, `estimate-sprint-plugin-passed-one-off-estimate-is-not-read-again`, which is `pending`, speaks of the sentences of case 1063.1 and of another Backlog line, which this Case leaves as they are, so it stands.
>
> A Grep `transcript.*method|method.*transcript` over `vault/wiki/rules/`, `vault/wiki/entities/` and `.claude/` printed `.claude/skills/hi/SKILL.md`, `rule-orchestration.md`, `entity-sprint-plugin.md`, `rule-estimates-schema.md`, `rule-case-protocol.md` and `rule-skill-hi.md`. `rule-skill-hi` and its skill let `/hi` read the transcript that a `method` names. That stays true for a one-off Estimate and for the Estimates that stand. Line 39 of `rule-orchestration` names the `method` of an Estimate among the texts a check reads, for the Cases that a dispatch names as related, and its transcript is the one of a subagent, in which the main agent reads a fact before it states it, so it stands. The glossary rows `Estimate` and `Estimate fields` name `method` with no rule on where a reading stands, so they stand.
>
> For Case 1071.2 I read the part of `check_form` that judges the Estimate items, and whole `estimate_target`, `kept_method_waits`, `kept_method`, `new_criterion`, `criterion_line` and `judge` of `.guppi/guppi/prespec.py`, with the opening of `criterion_notes`; `is_reading`, `tied_to_a_one_off_moment`, `waits_for_an_event`, `names_its_event_inside_a_part` and `waits_for_another_session` of `.guppi/guppi/lint.py`; and `is_sprint_page` of `.guppi/guppi/ledger.py`. `check_form` reports a `method` of a `create` or a `set: {method: …}` that waits for another session off a sprint page, and `kept_method_waits` reports a kept one, both by `waits_for_another_session`, which the lint run does not call. A Grep `waits_for_another_session` over `.guppi/guppi/` printed the definition in `lint.py` and the calls in `prespec.py` alone. The new judgment follows that model. A Grep `compile\(.*transcript|transcript.*compile\(|["']transcript|claude/projects`, case ignored, over `.guppi/guppi/` printed lines of `agents.py` and `ledger.py`, which read a transcript as input and judge no `method`. So no code judges a transcript reading today, and the one new function in `lint.py` is the one judgment, imported by `prespec.py` (`rule-one-judgment-one-implementation`). A Grep `written back|Criterion unchanged|same Criterion|criterion_line\(` over `.guppi/guppi/` printed `prespec.py` alone: `criterion_notes` reads each line by `criterion_line`, and no function judges whether a Criterion is written back unchanged. So the new comparison reads the new Criterion by `new_criterion` and each line by `criterion_line`, the readings that `criterion_notes` uses. `check_form` takes no Cases, and `new_criterion` needs them, so the check of a kept `method` runs from `judge`, which holds them. `judge` is also what the `SubagentStop` check of `.guppi/guppi/casecheck.py` runs over a case file, at line 1484, so a Case file of `case-guppi` gets the same line. A Grep `waits for another session|waits_for_another_session` over `{vault/wiki,.claude,.guppi/guppi}/**`, in the mode of paths, printed 6 files. The module docstring of `prespec.py` and the docstring of `check_form` list the findings on a `method` and gain the new one. `lint.py` holds the predicate, whose docstring names its caller. `estimate-prespec-hook-reports-a-method-that-waits-for-another-session`, `estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session` and `estimate-prespec-hook-reports-a-wait-off-its-form` each promise a finding or a note on a wait, which the new line leaves as it is. `lesson-prespec-method-predicate-misses-a-sprint-session` records a past miss of the wait predicate. So these stand, and the new finding gets its own Estimate on `rule-prespec-hook`, whose `implementation_ref` names `prespec.py`.
>
> A Grep `method.{0,200}(transcript|claude/projects)` over `.guppi/tests/` printed nothing, so no test plan holds a `method` that the new check would report. `.guppi/tests/test_case_schema.py` runs `casecheck.check_answer` over the live `vault/wiki/case-example.md`. Its `create` names `make test-cart`, and `seed` of that test writes the page of its `update` with a `method` that runs `pytest`, so neither holds a reading by hand and the new check gives it no line. `test_schemas.py` and `test_generate.py` read the lists of the live `schema.yaml` files, and `test_case_schema.py` and `test_orchestration.py` copy those files into a test vault; the new text changes no list and stays inside the block of its field. A Grep `case-schema|rule-case-protocol|rule-estimates-schema|entity-sprint-plugin` over `.guppi/tests/` printed `test_prespec.py`, `test_casecheck.py`, `test_lint.py`, `test_generate.py`, `test_render.py`, `test_recall.py`, `test_pages.py`, `test_guard.py` and `test_glossary.py`, each with the name as a string or a page of a temporary vault, so no test reads the live `case-schema.md` or the live pages this Case changes. The check runs as the code stands when it runs, so the `/pre-spec` of this session, before Work Mode, does not have it. Case 1069 creates an Estimate whose `method` runs `guppi test`, with no reading by hand. The ledger of this session holds no `error` lesson.
>
> The check of this file named what follows. The items of the `## Backlog` of `entity-sprint-plugin` stand as one list with no full stop, so the check takes the list as one sentence; I read the page around it, lines 30 to 43. The pair removes the line of this item alone and keeps every other item. The check notes that Case 1070 changes the same list. Cases 1069 and 1070 were built again after `/pre-spec`, and on this pass I read both finished files whole, `vault/raw/2026-11-26/1515/cases/case-1069.md` and `vault/raw/2026-11-26/1515/cases/case-1070.md`. Case 1070.3 removes the line of the name of the main branch by a fenced `old` that is that line alone and an empty `new`, the form of my pair, and adds that item under `## Closed` after the line of case 794. My `old` is the line after it, and the two `old` texts are two different lines that share no character, so both pairs apply in either order; the `## Closed` section is not touched by this Case. Case 1070 keeps the rule of Case 1071.1. The new `method` of `estimate-morph-sets-up-the-project-at-the-first-hi` reads by hand the Render of `rule-skill-setup` and the Purpose of `rule-morph` in the Spec at Retro, and after it `.claude/skills/setup/SKILL.md`, rendered from it. The new `method` of `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` runs `uv run --project .guppi guppi render --check` and reads `.claude/skills/work/SKILL.md`. The new `method` of `estimate-guppi-config-fills-the-main-branch` runs tests and reads `guppi.toml` and the output of the render check. The new text lets a lasting `method` read the text of any page in the Spec at Retro, or the file rendered from it, not only the Render of its own rule, so these three readings fit it, and the check of Case 1071.2 judges only a part by hand that names a transcript or `~/.claude/projects/`, so it gives none of them a line. The install in a new project moves to the one-off Estimate of Case 1070.7 on `entity-sprint-plugin`, which reads its transcript, and its other one-off Estimates of Cases 1070.4 and 1070.5 sit on that sprint page too. `estimate-spec-box-refuses-a-stale-spec`, whose Criterion Case 1070.2 replaces, keeps `uv run --project .guppi pytest .guppi/tests/test_box.py`, as its live page holds it, and the two Estimates of Case 1070.6 that change a `purpose` alone get no new `method` and no new Criterion. The task of the docstring of `gitstate.py` in Case 1070.4 names `/merge-main` only where the project holds that skill, as the new text of `rule-case-protocol` does. In Case 1069, `estimate-frontier-hook-refuses-a-shell-command-on-the-frontier` runs `uv run --project .guppi guppi test`, and `estimate-frontier-hook-refuses-an-open-box-with-a-closer`, whose Criterion Case 1069.2 replaces, keeps `uv run --project .guppi guppi test, which runs .guppi/tests/test_frontierguard.py`, as its live page holds it, so neither reads a transcript. Case 1069.2 changes `check_frontier` of `prespec.py` and adds one function there, and Case 1071.2 changes `check_form`, `judge` and the docstrings of the same module for a finding on a `method`, so the two touch different functions. No line of either file rests on something this Case makes false, and this Case changes nothing on their account. The then lines of Case 1071.2 share words with those of Case 1071.1 on purpose: Case 1071.1 sets the rule in the text, and Case 1071.2 sets the check that reports a break of it. The check also listed files that name a page or a file that this Case changes. I read `estimate-sprint-plugin-passed-one-off-estimate-is-not-read-again`: its Criterion speaks of the passed one-off Estimate and of another Backlog line, and the new text of `once` keeps the sentence that it is not read again. `estimate-lint-reports-a-method-tied-to-a-one-off-moment` speaks of the finding of a first moment, which the new line does not replace. `estimate-lint-checks-the-method` speaks of the forms that lint reads, and lint does not call the new function. So each of them stands. The other files, judged by their purpose lines and paths, speak of the form, the render or the lists of these pages and modules, or of other findings of `prespec.py` and `lint.py`, not of where a transcript reading stands, so they stand.

> **problem:**
> A lasting check on a rule page that reads the transcript of a session can wait long and fail often. While it stands failed, it stops the clean build of a page that ships. No rule says where such a reading belongs, and nothing reports a Case that puts one on a rule page.

> **recommend:**
> - **Whether the split becomes a rule**
>   - Recommended: (b) a rule for each new Estimate, and for each Estimate whose Criterion a Case replaces; the Estimates that stand today change only when a Case replaces their Criterion.
>   - Answer: agreed, (b).
> - **What reports a Case that misses the split**
>   - Recommended: (b) the text, and a finding of `guppi prespec --check`, by one new function of `.guppi/guppi/lint.py` that the lint run does not call.
>   - Answer: agreed, (b).
> - **Whether a Criterion set again word for word counts as replaced**
>   - Recommended: (b) not a replacement: a Criterion written back unchanged gives no finding, so `/merge-main` keeps its steps.
>   - Answer: agreed, (b).
> - **Change**
>   - Asked: `/pre-spec` asked that the new text of `rule-case-protocol`, a page with `core: true`, name `/merge-main` only where the project holds `.claude/skills/merge-main/SKILL.md`, and that a lasting `method` may read the text of any page that ships, in the Spec at Retro or in the file rendered from it, not only the Render of its own rule.
>   - Taken: the new sentence of `rule-case-protocol` names `/merge-main` with that condition, and the new text of both pages and the then of Case 1071.1 say that a lasting `method` reads a test, a command, or the text of a page in the Spec at Retro or in the file rendered from it.

### Case 1071.1 — The form of a Case and the schema of an Estimate set the split

> **given:**
> `rule-case-protocol`: the rule of the form of a Case, whose Render gains the rule of the split.
> **＋** `vault/wiki/case-schema.md`: the file rendered from `rule-case-protocol`, which `case-guppi` reads whole.
> **＋** `rule-estimates-schema`: the schema of an Estimate, whose fields `method` and `once` gain the rule.
> **＋** `vault/wiki/estimates/schema.yaml`: the file rendered from `rule-estimates-schema`.
> **＋** `entity-sprint-plugin`: the live sprint page, whose `## Backlog` loses the question.
> **＋** `entity-sprint-<id>`: a sprint page, the target of a one-off Estimate.
> **＋** `estimate-case-protocol-splits-a-transcript-reading`: the new check of the text.
> **＋** `.guppi/guppi/prespec.py`: the check of `/pre-spec`, which reports a break, changed by Case 1071.2.

> **when:**
> `case-guppi` reads `vault/wiki/case-schema.md`, rendered from `rule-case-protocol`, to write the `method` of an Estimate, or a reader reads the fields `method` and `once` of `vault/wiki/estimates/schema.yaml`, rendered from `rule-estimates-schema`.
> **＋** A reader opens the `## Backlog` of `entity-sprint-plugin`.

> **then:**
> Both texts say that an Estimate whose target is not a sprint page `entity-sprint-<id>` reads no transcript of a session in its `method`.
> **＋** Both say that a promise whose check reads what an agent did in a transcript takes two Estimates: a lasting one on the page of the promise, whose `method` reads a text that ships — a test, a command, or the text of a page in the Spec at Retro or in the file rendered from it — and a one-off Estimate of the live sprint page with `once: true`, whose `method` reads the transcript.
> **＋** Both say that this binds each Estimate that a Case creates, gives a new `method` or gives a new Criterion, and that `guppi prespec --check` of `.guppi/guppi/prespec.py` reports one that breaks it.
> **＋** The field `once` of `vault/wiki/estimates/schema.yaml` names what an agent did in the transcript of a session among the states that a one-off Estimate checks.
> **＋** The `## Backlog` of `entity-sprint-plugin` no longer asks whether every Estimate that reads a transcript is split.
> **－** An Estimate that stands with a transcript reading keeps it until a Case gives it a new `method` or a new Criterion.
> **－** A Criterion written back word for word to set an Estimate `pending` again is no new Criterion.
> **－** A test over a made-up transcript reads no transcript of a session.

```then
create:
- slug: estimate-case-protocol-splits-a-transcript-reading
  ref: rule-case-protocol
  kind: QA
  purpose: Whether the form of a Case and the schema of an Estimate say that an Estimate off a sprint page reads no transcript, that a promise checked in a transcript takes a lasting Estimate that reads a text that ships and a one-off Estimate of the sprint page, for each Estimate a Case creates, gives a new method or gives a new Criterion, and that pre-spec reports a break
  method: 'by hand, at the Retro of the session that sets this Criterion: the new Render of rule-case-protocol and of rule-estimates-schema and the update of entity-sprint-plugin in the Spec read against the Criterion, recorded in the estimate line'
  tags:
  - harness
  - workflow
update:
- slug: rule-case-protocol
  replace:
  - old: 'lint reports one with `once: true` whose target is not a sprint page (as set in case 969.1).'
    new: 'lint reports one with `once: true` whose target is not a sprint page (as set in case 969.1). An Estimate whose target is not a sprint page reads no transcript of a session in its `method`: a promise whose check reads what an agent did in a transcript takes two Estimates, a lasting one on the page of the promise, whose `method` reads a text that ships — a test, a command, or the text of a page in the Spec at Retro or in the file rendered from it — and a one-off Estimate of the live sprint page with `once: true`, whose `method` reads the transcript (as set in case 1071.1). This binds each Estimate that a Case creates, gives a new `method` or gives a new Criterion: one that stands with such a reading keeps it until then, a Criterion written back word for word to set an Estimate `pending` again, as `/merge-main` writes one where the project holds `.claude/skills/merge-main/SKILL.md`, is no new Criterion, and a test over a made-up transcript reads no transcript of a session; `guppi prespec --check` reports an Estimate that breaks it (as set in case 1071.1).'
  change: 'an Estimate off a sprint page reads no transcript: a promise checked in a transcript takes a lasting Estimate that reads a text that ships and a one-off Estimate of the sprint page'
- slug: rule-estimates-schema
  replace:
  - old: the estimate line names that file; the person's answer is kept by the estimate line itself (as set in case 960.1).
    new: 'the estimate line names that file; the person''s answer is kept by the estimate line itself (as set in case 960.1). An Estimate whose `target` is not a sprint page reads no transcript of a session in its `method`: a promise whose check reads what an agent did in a transcript takes two Estimates, a lasting one on the page of the promise, whose `method` reads a text that ships — a test, a command, or the text of a page in the Spec at Retro or in the file rendered from it — and a one-off Estimate of the live sprint page with `once: true`, whose `method` reads the transcript (as set in case 1071.1). This binds each Estimate that a Case creates, gives a new `method` or gives a new Criterion: one that stands with such a reading keeps it until then, a Criterion written back word for word to set an Estimate `pending` again is no new Criterion, and a test over a made-up transcript reads no transcript of a session; `guppi prespec --check` reports an Estimate that breaks it, by one predicate of `.guppi/guppi/lint.py` that the lint run does not call (as set in case 1071.2).'
  - old: such as the lines of a file after a run, rather than a behaviour that lasts.
    new: such as the lines of a file after a run or what an agent did in the transcript of a session, rather than a behaviour that lasts.
  change: 'the field method: an Estimate off a sprint page reads no transcript, a promise checked in a transcript takes a lasting Estimate and a one-off Estimate; the field once names a transcript among the states it checks'
- slug: entity-sprint-plugin
  replace:
  - old: '- Whether every Estimate whose `method` reads the transcript of a session should be a one-off Estimate of the sprint page with `once: true`, with a lasting Estimate beside it whose `method` reads a file that ships, as `rule-estimates-schema` would then set it; the split made once for `estimate-case-build-reads-the-readers-of-a-new-files-folder` (case 1019.4)'
    new: ''
  change: 'the Backlog question whether every Estimate that reads a transcript is split is decided: it is, for each Estimate a Case creates, gives a new method or gives a new Criterion'
```

```tasks
- [x] update `rule-case-protocol`
- [x] update `rule-estimates-schema`
- [x] update `entity-sprint-plugin`
- [x] create `estimate-case-protocol-splits-a-transcript-reading`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/case-schema.md`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/estimates/schema.yaml`
- [x] read `estimate-case-protocol-splits-a-transcript-reading`
```

### Case 1071.2 — The check of the plan reports a transcript reading off a sprint page

> **given:**
> `.guppi/guppi/lint.py`: the module of the judgments of a `method`, which gains the judgment of a transcript reading.
> **＋** `.guppi/guppi/prespec.py`: the check of `/pre-spec`, which reports such a reading.
> **＋** `.guppi/guppi/ledger.py`: `is_sprint_page`, the one judgment of a sprint page, unchanged.
> **＋** `entity-sprint-<id>`: a sprint page, whose Estimates the check leaves alone.
> **＋** `~/.claude/projects/`: the folder of the saved transcripts, which a reading names.
> **＋** `.guppi/guppi/casecheck.py`: the check of the case file of `case-guppi`, which runs `judge` of `prespec.py`, unchanged.
> **＋** `.guppi/tests/test_lint.py`: the tests of the judgment.
> **＋** `.guppi/tests/test_prespec.py`: the tests of the check.
> **＋** `rule-prespec-hook`: the rule of the check of the plan, the target of the new Estimate.
> **＋** `estimate-prespec-hook-reports-a-method-that-reads-a-transcript`: the new check.

> **when:**
> `uv run --project .guppi guppi prespec --check <plan> --session <id>` of `.guppi/guppi/prespec.py` reads the `method` of a `create` of an Estimate, or of an `update` that carries `set: {method: …}`, in the `then` blocks of the plan file, or the `method` that the live page of an Estimate keeps under an `update` that replaces its Criterion whole.
> **＋** Or the check of `.guppi/guppi/casecheck.py` runs the same `judge` of `.guppi/guppi/prespec.py` over the file of a Case that `case-guppi` wrote.
> **＋** Or `.guppi/tests/test_prespec.py` and `.guppi/tests/test_lint.py` run them over a made-up plan, made-up pages and made-up methods.

> **then:**
> A `method` that the plan writes, with a part between two `;` that holds `by hand` and names the word `transcript` or the folder `~/.claude/projects/`, gives one line `case N: <create|update> <slug>: method reads the transcript of a session off a sprint page — a lasting method reads a text that ships, and a one-off Estimate of the sprint page reads the transcript`.
> **＋** A `method` kept on the live page with such a part gives one line `case N: update <slug>: the method on the page reads the transcript of a session — set a method that reads a text that ships, and read the transcript by a one-off Estimate of the sprint page`.
> **＋** The judgment of such a part is one function of `.guppi/guppi/lint.py`, which `.guppi/guppi/prespec.py` imports.
> **＋** The check of `.guppi/guppi/casecheck.py` sends back a Case file with the same line.
> **－** An Estimate whose target is a sprint page `entity-sprint-<id>`, by `is_sprint_page` of `.guppi/guppi/ledger.py` — the `ref` of a `create`, the `target` that an `update` sets or that the live page holds — gives no such line.
> **－** A kept `method` gives no such line when each line of the new Criterion, read by `new_criterion` and `criterion_line` of `.guppi/guppi/prespec.py`, equals the line in its place of the `## Criterion` of the live page, empty lines aside, as when a Criterion is written back to set the Estimate `pending` again.
> **－** An `update` that sets `passed` or `failed` by the person's decision, or that names a part of the page alone, keeps no `method` and gives no such line.
> **－** A part with no `by hand`, such as a test run over a made-up transcript, gives no such line.
> **－** `uv run --project .guppi guppi lint` of `.guppi/guppi/lint.py` over the live Estimate pages gives no finding by this function.
> **－** The line replaces no other finding of the same `method`, such as the line of a `method` that waits for another session.

```then
create:
- slug: estimate-prespec-hook-reports-a-method-that-reads-a-transcript
  ref: rule-prespec-hook
  kind: QA
  purpose: Whether pre-spec reports a method that the plan writes, or that the live page keeps under a new Criterion, whose reading by hand reads the transcript of a session off a sprint page, by one predicate of .guppi/guppi/lint.py, and leaves alone a sprint page, a Criterion written back unchanged, a part with no by hand and the live pages
  method: uv run --project .guppi pytest .guppi/tests/test_prespec.py .guppi/tests/test_lint.py -k transcript
  tags:
  - harness
  - workflow
```

```tasks
- [x] create `estimate-prespec-hook-reports-a-method-that-reads-a-transcript`
- [x] `.guppi/guppi/lint.py`: one function judges whether a `method` holds a part between two `;` that holds `by hand`, by `is_reading`, and names the word `transcript` or the folder `~/.claude/projects/`; its docstring says that `pre-spec` imports it and that the lint run does not call it, and a pointer to a case stands only in a bracket at the end of its sentence.
- [x] `.guppi/guppi/prespec.py`: a `create` of an Estimate whose `ref` is no sprint page, and an `update` with `set: {method: …}` whose target by `estimate_target` is no sprint page, give the line of the `then` when that function accepts the `method`; an `update` that `kept_method` reads, whose live `target` is no sprint page and whose new Criterion by `new_criterion` differs from the live `## Criterion` line by line by `criterion_line`, empty lines aside, gives the kept line when the function accepts the kept `method`; that check runs from `judge`, which holds the Cases; the module docstring and the docstring of `check_form` list the new findings, a pointer to a case only in a bracket at the end of its sentence.
- [x] `.guppi/tests/test_lint.py`: tests whose names hold `transcript`: a part `by hand, at Retro: the reply read in the transcript of the session` and a part that names `~/.claude/projects/` are accepted; a part `pytest .guppi/tests/test_x.py over a temp agent transcript` and a `method` with no transcript are not; the lint run over a made-up Estimate page with such a `method` gives no finding by the function.
- [x] `.guppi/tests/test_prespec.py`: tests whose names hold `transcript`: a `create` on a rule and an `update` with `set: {method: …}` that read a transcript give the line; the same on `entity-sprint-plugin` gives none; an `update` that replaces the Criterion with new text while its live page keeps a transcript reading gives the kept line, and one whose Case writes back the live Criterion word for word gives none; an `update` that sets `passed` by the person's decision gives none; a `method` that reads a transcript and waits for another session gives both lines; `prespec` imports the function of `lint` itself.
- [x] read `estimate-prespec-hook-reports-a-method-that-reads-a-transcript`
```
