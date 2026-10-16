<!-- approved 05:15:57 · session e7c349c1 -->

# Session 0342 — the sprint plugin: /hi outside a git repository and the install of GUPPI

## Case 851 — /hi offers git init in a folder that is no git repository

> **context:**
> When the person types `/hi`, the skill file runs two git commands as `!` lines before the agent's first turn: `git branch --show-current` for `Branch:` and `git status --short` for `Status:`. Claude Code stops the whole skill when one of those commands fails, so in a folder that is no git repository `/hi` ends on `fatal: not a git repository` and the agent never gets a turn. In session 0104 this stopped the first `/hi` after `/guppi:install` in an empty folder; after `git init`, a second `/hi` started `/sprint-open` (`lesson-hi-fails-outside-a-git-repository`, the Result of `estimate-clean-branch-writes-the-session-files`). The hooks on `/hi` need no git: `dirty` of `.guppi/guppi/gate.py` gives an empty text when git fails, and `.guppi/guppi/shellwrite.py` catches the error of git. The person chose that one GUPPI command, `uv run --project .guppi guppi gitstate`, takes the place of the two git lines and always exits 0. In a folder with no repository it prints a line that says so, and the agent asks whether it runs `git init -b main`. On a yes it runs it and ends `/hi`, and the person types `/hi` again; on a no it ends `/hi` too. Either way the `/hi` that saw no repository starts no `/sprint-open` and writes no Frontier. `-b main` names the first branch `main`, since `/sprint-open` takes any other branch for the branch of a closed sprint and plans a push of it. The pre-spec finding on atomicity split what the command prints, checked by a test in Case 851.3, from what the agent asks, checked by hand in Case 851.1.
>
> In a repository the command prints the branch under `Branch:` as git did, and the `/hi` that prints the `none` line ends before any skill reads that line. So step 4 of `rule-skill-sprint-open`, step 1 of `rule-skill-merge-main` and `estimate-skill-sprint-open-merges-the-closed-sprint-branch` read a real branch name, `main` after a `git init -b main`, and stand. The Criterion of `estimate-git-context-current`, which speaks of `Branch:` with the current branch and `Status:` with `git status --short` in this repository, stands for the same reason. The `allowed-tools` of `rule-skill-hi` names the two git commands, and the Criterion of `estimate-hi-no-read-calls` names them too, so Case 851.2 replaces that Criterion. It carries both of its promises in new words: the line of the context names the output of `guppi gitstate` under `Branch:` in place of two git lines, and the line of `allowed-tools` names `guppi gitstate` in place of the two git commands. `git init -b main` writes `.git/` in Plan Mode before any Case is ratified. `rule-default-mode` keeps a session from writing anything before a Case is ratified, so Case 851.1 adds to its Purpose the one exception the person chose. `rule-permissions` allows the agent its own working files only, and `git init -b main` stays out of `allowed-tools`, so Claude Code asks the person to allow it and that rule stands. The Criterion of `estimate-default-mode` asks only that the Purpose of `rule-default-mode` say why nothing is written before a Case, which it still says, so it stands.
>
> `estimate-morph-sets-up-the-project-at-the-first-hi` (pending, on the draft `rule-morph`, whose setup Case is not built) puts the setup Case before the opening Case of `/sprint-open` and before the Frontier, and takes the name of the main branch and the remote from git. The git step of this Case comes first: the setup needs a repository, and the `/hi` that runs `git init` ends before any Case. `estimate-sprint-plugin-installs-as-a-plugin` (pending) promises that `/hi` opens a working session in an empty project after `/guppi:install`; in a folder with no git that now happens at the `/hi` after the person's `git init -b main`. For the related item C7, Case 855 defers `estimate-clean-branch-writes-the-session-files`.
>
> The Case leaves out the following:
> - `/guppi:install`, which still runs no git command (`rule-plugin-install`).
> - A machine without git: there the command prints the same line, and the `git init` that the person allows fails where the person sees it.
> - `/work` and `/box`, whose skills also run `git branch --show-current` but run only after a `/hi`.
> - The owner check of `/sprint-open` by `gh`, which a new repository with no remote does not pass.
> - The setting for the name of the main branch, which the person left to the setup Case of `rule-morph`. That page lists the code that takes the main branch to be `main` among the settings that the setup Case fixes.
>
> Rule `rule-one-judgment-one-implementation` in `CLAUDE.md`: a Grep `\["git"` over `.guppi/guppi/` printed `box.py`, `gate.py`, `ship.py` and `shellwrite.py`. `git` of `box.py` and `dirty` of `gate.py` give an empty text when git fails, so they cannot tell a missing repository from an empty answer. No function there judges whether a folder is a git repository, so the new command holds the one copy of that judgment. A Grep `git branch --show-current|git status --short|Branch:` over `.claude/` printed `.claude/skills/work/SKILL.md`, `.claude/skills/hi/SKILL.md`, `.claude/skills/merge-main/SKILL.md`, `.claude/skills/sprint-open/SKILL.md` and `.claude/skills/box/SKILL.md`. The hits in `work`, `box`, `merge-main` and `sprint-open` stand for the reasons above, and `hi` is the rendered file that this Case changes. `.guppi/tests/test_guppi_package.py` reads each file under `.claude/` live for the old forms of commands. The new line uses `uv run --project .guppi guppi`, so it passes that test. The brackets `(as set in case 851)` and `(as set in case 851.1)` in the new text of `rule-git-context` and `rule-default-mode`, pages with `core: true`, each stand at the end of their sentence, so `guppi ship` removes each one whole.

> **problem:**
> In a folder that is no git repository, `/hi` stops on a git error before the agent's first turn. It neither tells the person that GUPPI needs a git repository nor offers to make one, so a new install never opens its first sprint.

> **recommend:**
> - **What should `/hi` do in a folder that is no git repository?**
>   - Recommended: (b) offer to run `git init -b main`, run it on the person's yes and go on to open the first sprint in the same session.
>   - Answer: agreed, (b).
> - **What should happen when no repository gets made?**
>   - Recommended: (a) stop after the note: no `/sprint-open` and no Frontier, and the person types `/hi` again after `git init -b main`.
>   - Answer: agreed, (a).
> - **How should the branch and status lines stop failing?**
>   - Recommended: (a) one GUPPI command, `uv run --project .guppi guppi gitstate`, that prints the branch and the status, or a line that the folder is no git repository, and always exits 0, with a test.
>   - Answer: agreed, (a).
> - **Should `/guppi:install` change too?**
>   - Recommended: (a) only `/hi`; the install keeps running no git command.
>   - Answer: agreed, (a).
> - **How should we check that this works?**
>   - Recommended: (a) a new Estimate on `rule-git-context`, read by a test of the new command and once by hand in an empty folder with GUPPI and no git.
>   - Answer: agreed, (a).
> - **Where should the name of the main branch be set?**
>   - Recommended: (a) leave it to the setup Case of `rule-morph`; this Case uses `git init -b main`.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at pre-spec, the person agreed that on the yes the agent runs `git init -b main` and stops, telling the person that the repository is made and to type `/hi` again, so that the new `/hi` prints `main` under `Branch:` and `/sprint-open` and `/merge-main` read a real branch; no going on in the same turn.
>   - Taken: on the yes the agent runs `git init -b main`, says that the repository is made and ends `/hi`; the person types `/hi` again.
> - **Change**
>   - Asked: at pre-spec, the person agreed that `git init -b main` stays out of `allowed-tools`, so that Claude Code asks the person to allow it. `rule-default-mode` gets one exception: `git init -b main` at `/hi` on the person's yes is the one write before a Case. The sentence that plan mode does not stop the command is dropped.
>   - Taken: `allowed-tools` names `guppi gitstate` alone in place of the two git commands; Case 851.1 adds the exception to the Purpose of `rule-default-mode`; the Render of `rule-git-context` says nothing of plan mode.

### Case 851.1 — /hi asks to run git init outside a git repository and ends

> **given:**
> `rule-git-context`: the Render of the `Branch:` line of `/hi` and the step outside a repository.
> **＋** `rule-skill-hi`: the skill `/hi`, its `allowed-tools` and its step that starts `/sprint-open`.
> **＋** `rule-default-mode`: no write before a ratified Case, with its one exception.
> **＋** `rule-skill-sprint-open`: its hook on `/hi` asks for `/sprint-open` before the Frontier.
> **＋** `.claude/skills/hi/SKILL.md`: the skill file rendered from `rule-skill-hi`.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier that `/hi` writes.
> **＋** `estimate-git-context-offers-git-init`: the new check of this behaviour.

> **when:**
> The person types `/hi` of `.claude/skills/hi/SKILL.md` in a project folder, and its `Branch:` line, which runs `uv run --project .guppi guppi gitstate` of `rule-git-context`, reads `none: this folder is no git repository`.

> **then:**
> Before `/sprint-open` and before the Frontier, the agent says that GUPPI works only in a git repository and asks the person whether it runs `git init -b main`.
> **＋** On the person's yes, the agent runs `git init -b main`, which Claude Code asks the person to allow, says that the repository is made, and tells the person to type `/hi` again.
> **＋** The next `/hi` prints `main` under `Branch:` and goes on as `rule-skill-hi` sets it, `/sprint-open` first when the hook of `rule-skill-sprint-open` asks for it.
> **＋** On the person's no, the agent tells the person to type `/hi` again after `git init -b main`.
> **－** After either answer, that `/hi` starts no `/sprint-open` and writes no `raw/<date>/<hi HHMM>/frontier.md`.
> **－** `git init -b main` is the one write before a ratified Case that `rule-default-mode` allows, and `allowed-tools` of `.claude/skills/hi/SKILL.md` does not name it.

```then
create:
- slug: estimate-git-context-offers-git-init
  ref: rule-git-context
  kind: QA
  purpose: Whether /hi in a folder that is no git repository asks to run git init -b main, runs it on the person's yes and ends, ends on a no, and opens no sprint and writes no Frontier either way
  method: 'by hand, after the librarian''s run: in an empty folder that is no git repository, GUPPI installed by /guppi:install from a copy that uv run --project .guppi guppi ship --allow-draft wrote into a local folder, Claude Code opened there, /hi typed and answered no, /hi typed again and answered yes, then /hi typed a third time, and the replies, the context of each /hi, the session folders and git branch --show-current read against the Criterion'
  tags:
  - session
  - harness
  - git
update:
- slug: rule-git-context
  replace:
  - old: |-
      Branch: !`git branch --show-current`
      Status: !`git status --short`
    new: |-
      Branch: !`uv run --project .guppi guppi gitstate`

      When the line `Branch:` above reads `none: this folder is no git repository`, take this step first, before `/sprint-open` and before the Frontier (as set in case 851.1). Say that GUPPI works only in a git repository, and ask the person whether you run `git init -b main`, which names the first branch `main`. On the person's yes, run `git init -b main` with the Bash tool, say that the repository is made, and tell the person to type `/hi` again. On a no, tell the person to type `/hi` again after `git init -b main`. After either answer, start no `/sprint-open`, write no Frontier, and end the reply.
  - old: '`/hi` runs no `git pull`'
    new: '`uv run --project .guppi guppi gitstate` of `.guppi/guppi/gitstate.py` prints the branch, then `Status:` and the status, or, in a folder that is no git repository, one line that says so, and it exits 0 in each case, since Claude Code stops the whole skill on a `!` command that fails: two git commands stood on these lines until a first `/hi` in an empty project stopped on a git error (as set in case 851). `/hi` runs no `git pull`'
  set:
    implementation_ref:
    - .guppi/guppi/gitstate.py
    - .guppi/tests/test_gitstate.py
  change: the branch and the status come from guppi gitstate, and outside a git repository /hi asks to run git init -b main and ends
- slug: rule-skill-hi
  replace:
  - old: Bash(git branch --show-current), Bash(git status --short)
    new: Bash(uv run --project .guppi guppi gitstate)
  - old: 'start `/sprint-open` first, as the hook on `/hi` says:'
    new: 'start `/sprint-open` first, unless the step of `rule-git-context` above ends the reply, as the hook on `/hi` says:'
  - old: '`allowed-tools` names the four `!` commands of the skill:'
    new: '`allowed-tools` names the three `!` commands of the skill, and not `git init -b main`, which the agent runs in a folder that is no git repository only on the person''s yes and with the person''s leave in Claude Code, as `rule-git-context` sets it:'
  change: allowed-tools names guppi gitstate in place of the two git commands, and /sprint-open waits for the git step
- slug: rule-default-mode
  replace:
  - old: own and not a line of the registry (case 85.4).
    new: 'own and not a line of the registry (case 85.4). One write comes before a Case: at `/hi` in a folder that is no git repository, the agent runs `git init -b main` on the person''s yes, which writes `.git/`, since a session of GUPPI needs a git repository, as `rule-git-context` sets it (as set in case 851.1).'
  change: 'one exception: git init -b main at /hi on the person''s yes'
```

```tasks
- [x] update `rule-git-context`
- [x] update `rule-skill-hi`
- [x] update `rule-default-mode`
- [x] create `estimate-git-context-offers-git-init`
- [x] `uv run --project .guppi guppi render`: `.claude/skills/hi/SKILL.md`
- [ ] read `estimate-git-context-offers-git-init`
```

### Case 851.2 — /hi loads the branch and status with no read call

> **given:**
> `estimate-hi-no-read-calls`: its Criterion is replaced whole.
> **＋** `rule-skill-hi`: the skill `/hi` and its `allowed-tools`.
> **＋** `rule-git-context`: the line `Branch:` of `/hi`, which runs `guppi gitstate`.
> **＋** `rule-internal-context`: the files `/hi` loads.
> **＋** `rule-ledger-tail`: the line `Tail:` of `/hi`.
> **＋** `.claude/skills/hi/SKILL.md`: the skill file rendered from `rule-skill-hi`.

> **when:**
> The person invokes `/hi`, and Claude Code expands `.claude/skills/hi/SKILL.md` before the agent's first turn.

> **then:**
> The context of the first turn holds the output of each block of the skill, in the order of the children of `rule-skill-hi`: the text of the files `rule-internal-context` loads, the line `Render:` and the output of `uv run --project .guppi guppi gitstate` under the line `Branch:` of `rule-git-context`, and the line `Tail:` of `rule-ledger-tail`.
> **＋** The `allowed-tools` of the skill names `uv run --project .guppi guppi render --sync`, `uv run --project .guppi guppi gitstate` and `uv run --project .guppi guppi tail`, and neither `git pull`, `git init` nor `gh`.
> **－** The agent makes no read-tool call to get any of them.

```then
update:
- slug: estimate-hi-no-read-calls
  set:
    status: pending
    method: 'by hand, after the librarian''s run of the session that sets this Criterion: at the first /hi after it, the first turn''s context and the tool calls before it read in the transcript, and the allowed-tools of .claude/skills/hi/SKILL.md, written into the estimate line'
  change: the Criterion replaced whole — allowed-tools names guppi gitstate in place of the two git commands
```

```tasks
- [x] update `estimate-hi-no-read-calls`
- [x] read `estimate-hi-no-read-calls`
```

### Case 851.3 — guppi gitstate prints the state of git or one line outside a repository

> **given:**
> `.guppi/guppi/gitstate.py`: the new command `guppi gitstate`.
> **＋** `.guppi/guppi/cli.py`: the table of commands.
> **＋** `.guppi/tests/test_gitstate.py`: the test of the new command.
> **＋** `.claude/skills/hi/SKILL.md`: the skill file whose `Branch:` line runs the command.
> **＋** `rule-git-context`: the rule whose Render runs the command.
> **＋** `estimate-git-context-gitstate-exits-zero`: the new check of the command.

> **when:**
> `uv run --project .guppi guppi gitstate` of `.guppi/guppi/gitstate.py` runs in a folder, from the `Branch:` line of `.claude/skills/hi/SKILL.md`, from a test or by hand.

> **then:**
> In a git repository, it prints the current branch, then a line `Status:` and the lines of `git status --short` under it, and exits 0.
> **＋** In a folder that is no git repository, it prints the one line `none: this folder is no git repository` and exits 0.
> **－** It writes nothing in the folder.

```then
create:
- slug: estimate-git-context-gitstate-exits-zero
  ref: rule-git-context
  kind: QA
  purpose: Whether guppi gitstate prints the branch and the status in a git repository, and one line in a folder that is no git repository, and exits 0 in each case
  method: uv run --project .guppi pytest .guppi/tests/test_gitstate.py
  tags:
  - session
  - harness
  - git
```

```tasks
- [x] `.guppi/guppi/gitstate.py`: the command `guppi gitstate`, which runs `git rev-parse --is-inside-work-tree` in the project folder; when it prints `true`, the command prints the output of `git branch --show-current`, then the line `Status:` and the lines of `git status --short`; otherwise, a failed or missing git included, the one line `none: this folder is no git repository`; exit 0 in each case.
- [x] `.guppi/guppi/cli.py`: `gitstate` in `COMMANDS`.
- [x] `.guppi/tests/test_gitstate.py`: the command in a temporary folder with no git repository above it prints the one line and exits 0; after `git init -b main` in that folder it prints `main`, the line `Status:` and a line for an untracked file, and exits 0.
- [x] create `estimate-git-context-gitstate-exits-zero`
- [x] read `estimate-git-context-gitstate-exits-zero`
```

## Case 852 — /guppi:install offers to install uv when it is missing

> **context:**
> `/guppi:install` is the one skill of the plugin `guppi`. Its first step runs `uv --version`. When that fails, it says that GUPPI needs the tool `uv`, tells the person to install it and type `/guppi:install` again, stops and writes nothing. In `C:\PROJECTS\test-no-uv` it did just that, and the person said they would prefer the agent itself to offer to install `uv`; this session recorded `estimate-guppi-package-is-ready-after-the-install` as failed on that answer and on the offline install. The person chose that the agent asks whether it installs `uv` by the standalone installer of `uv` and runs it on a yes. After the installer, the agent runs `uv --version` again. When that passes, the install goes on in the same session, and its last message tells the person to start Claude Code from a new terminal, so that the hooks of the project find `uv`. When it fails, because this session of Claude Code does not see the new `uv`, the agent sends the person to a new terminal and a new `/guppi:install`. On a no, the agent shows the command and stops, writing nothing. The two installer commands in the new step come from the agent's knowledge: `case-guppi` could not read the installation page of `uv` from here. The person agreed that Work Mode reads that page before the render, so Case 852.1 holds a task that compares the commands with the page and stops on a difference, as condition 1 of `rule-where-to-stop` sets it. The rule is `rule-plugin-install`. Its Purpose holds one sentence on a missing `uv`, which Case 852.1 replaces, and its Render holds step 1, which Case 852.1 replaces, and step 7, to which Case 852.1 adds the new terminal. Its one Estimate, `estimate-plugin-install-writes-guppi-into-an-empty-project`, stands: its Criterion leaves out what the install does about `uv`, and its sentence that the last message tells the person to reopen Claude Code and type `/hi` stays true. The offer is a promise that can fail apart from the build of the environment, so Case 852.1 creates `estimate-plugin-install-offers-to-install-uv`, a slug that a Glob `vault/**/*install-uv*` did not print. Case 852.2 replaces the Criterion, `purpose` and `method` of `estimate-guppi-package-is-ready-after-the-install` without the missing-`uv` line and the project with no `uv`, so they no longer state the old stop. The new Criterion keeps the `When` line, the line that `uv --version` runs before any write, the line on `uv sync` after the copy and the line on the hooks word for word. It adds a `－` line that the install asks nothing about `uv` where `uv --version` passes, since the reading of this Estimate runs on the machine with `uv`, and the reading of `estimate-plugin-install-offers-to-install-uv` runs only where `uv` is missing. The line on a failed `uv --version` is dropped, since Case 852.1 sets that path anew and its Estimate checks it. At the person's word, Case 852.2 also drops the line on a failed `uv sync` and the offline project from that Estimate, so it keeps only the build of `.guppi/.venv/`. Case 853 of this session, the related item C4, sets what the install does when `uv sync` fails and creates its own Estimate on `rule-plugin-install` for it. That Case changes step 6 of the Render of `rule-plugin-install`, and Case 852.1 changes the description, step 1, step 7 and the Purpose sentence on a missing `uv`. Its case file, `vault/raw/2026-10-16/0342/cases/case-853.md`, was read whole and stands in the `given` of Case 852.1. The check of this file notes that the step 7 pair of Case 852.1 touches a sentence that Case 853 changes too. The check reads the end of the new step 6 of Case 853, which ends with a sentence that tells the agent not to send the person to `uv sync`, a reopen of Claude Code or `/hi`, and the start of step 7 as one sentence. The `old` of Case 852.1 starts at step 7, and the `old` of Case 853 ends at the end of step 6, so neither pair matches text the other changes. The two new texts were read side by side, and they fit. The new step 6 of Case 853 stops on a failed `uv sync` before step 7, and its ban on `/hi` binds only that failure. The new step 7 of Case 852.1 runs only after a successful step 6, and it adds the new terminal only when step 1 installed `uv`. The new Purpose sentence of Case 853 follows the sentence on `uv sync`, and Case 852.1 changes only the sentence on a missing `uv`. `guppi ship --check`, run by `uv run --project .guppi guppi check`, refuses a reference to a case in `plugin/skills/install/SKILL.md`, as `test_check_judges_the_plugin_skill_in_place` of `.guppi/tests/test_ship.py` shows, so the new Render text holds no pointer to a case; the pointer in the new Purpose sentence stands, since the page has no `core: true` and `guppi ship` does not write it. A Grep `rule-plugin-install|guppi:install` over the repository, outside `vault/raw/`, `vault/archive/`, `log.md` and `brief.md`, printed `vault/wiki/sprint.md`, `entity-sprint-plugin.md`, `plugin/skills/install/SKILL.md`, `estimate-clean-branch-writes-the-session-files.md`, `estimate-guppi-package-is-ready-after-the-install.md`, `estimate-morph-sets-up-the-project-at-the-first-hi.md`, `estimate-plugin-install-writes-guppi-into-an-empty-project.md`, `lesson-hi-fails-outside-a-git-repository.md`, `rule-clean-branch.md`, `estimate-sprint-plugin-installs-as-a-plugin.md`, `rule-harness.md`, `rule-plugin-install.md` and `rule-morph.md`, and no file under `.claude/`. The sentence of `rule-morph` that `/guppi:install` decides nothing and is no Case stands, since the person's yes to install a tool ratifies nothing in the vault. Its sentence, and the line of `estimate-morph-sets-up-the-project-at-the-first-hi`, that no settings file changes before the setup Case but by the copy and the render also stand, since the installer of `uv` writes no file of the project. The `method` of `estimate-clean-branch-writes-the-session-files` names the project with `uv` of the reading of `estimate-guppi-package-is-ready-after-the-install`, which Case 852.2 keeps. The other hits name the install without the step this Case changes. Case 851 sets the first `/hi` after the install and keeps the promise that the install runs no git command; this Case runs no git command and does not touch `/hi`. The Case adds no code that judges a text.

> **problem:**
> When `uv` is missing, `/guppi:install` only says so and stops. The person must find out how to install `uv` alone, though the agent could offer to install it.

> **recommend:**
> - **What should `/guppi:install` do when `uv` is missing?**
>   - Recommended: (a) offer to install it: ask, run the install command on a yes, and on a no show the command, say to type `/guppi:install` again after installing `uv`, and stop with nothing written.
>   - Answer: agreed, (a).
> - **Which command should install `uv`?**
>   - Recommended: (a) the official standalone installer for the system, a PowerShell command on Windows and a shell command on macOS and Linux; Work Mode reads the installation page of `uv` and checks the exact commands.
>   - Answer: agreed, (a).
> - **What should happen right after `uv` is installed?**
>   - Recommended: (a) run `uv --version` again; when it passes, go on with the install in the same session, its last message saying to start Claude Code from a new terminal; when it fails, say to open a new terminal, start Claude Code there and type `/guppi:install` again, and stop with nothing written.
>   - Answer: agreed, (a).
> - **How should we check that this works?**
>   - Recommended: (a) a new Estimate on `rule-plugin-install`, read by hand in an empty project with Claude Code started from a terminal that does not find `uv`, once answering no and once yes; and the Criterion of `estimate-guppi-package-is-ready-after-the-install` replaced without the missing-`uv` line.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: through Case 853, drop from the new Criterion of `estimate-guppi-package-is-ready-after-the-install` the line on a failed `uv sync` and the offline project, since Case 853 checks that failure with its own Estimate.
>   - Taken: Case 852.2 drops that line, and its `purpose` and `method` drop the failure and the offline project.

### Case 852.1 — /guppi:install asks to install uv when it is missing

> **given:**
> `rule-plugin-install`: the skill `/guppi:install` and its Render.
> **＋** `plugin/skills/install/SKILL.md`: the skill file rendered from `rule-plugin-install`.
> **＋** `estimate-plugin-install-offers-to-install-uv`: the new check of this behaviour.
> **＋** `https://docs.astral.sh/uv/getting-started/installation/`: the installation page of `uv`, with its standalone installer.
> **＋** `rule-where-to-stop`: its condition 1 stops Work Mode when a command differs from that page.
> **＋** `/hi`: the skill the person types after the install.
> **＋** `vault/raw/2026-10-16/0342/cases/case-853.md`: the Case of this session that changes step 6 and the Purpose of the same page.

> **when:**
> The person types `/guppi:install` of `plugin/skills/install/SKILL.md` in an empty project open in Claude Code, where `uv --version` fails.

> **then:**
> Before it writes anything, the agent says that GUPPI needs the tool `uv` and asks the person whether it installs `uv` now by the standalone installer of `uv` for the system: a PowerShell command on Windows, a shell command on macOS and Linux.
> **＋** On the person's no, it shows that command, says that the person installs `uv` with it and types `/guppi:install` again, and stops.
> **＋** On the person's yes, it runs that command, and then `uv --version` again.
> **＋** When `uv --version` then passes, it goes on with the install in the same session, and its last message tells the person to start Claude Code in the project from a new terminal and type `/hi`.
> **＋** When `uv --version` still fails, it says that this session of Claude Code does not find the new `uv`, and that the person opens a new terminal, starts Claude Code there and types `/guppi:install` again, and stops.
> **－** When the installer fails or Claude Code does not run it, the agent shows its output and the command, says that the person installs `uv` with it and types `/guppi:install` again, and stops.
> **－** It writes nothing into the project before `uv --version` passes.

```then
create:
- slug: estimate-plugin-install-offers-to-install-uv
  ref: rule-plugin-install
  kind: QA
  purpose: Whether /guppi:install, where uv is missing, asks to install uv by its standalone installer, stops with nothing written on a no, and on a yes goes on once uv --version passes or sends the person to a new terminal
  method: 'by hand, after the librarian''s run of the session that sets this Criterion, with a tag prod-x.y.z in the history of HEAD: the clean version written into a local folder by uv run --project .guppi guppi ship --allow-draft, that folder added as a catalogue by /plugin marketplace add and guppi installed from it by /plugin install guppi@guppi-marketplace; in an empty project with Claude Code started from a terminal whose PATH holds no folder of uv, /guppi:install typed and the offer answered no, then /guppi:install typed again and the offer answered yes; the replies, the files of the project and uv --version in a new terminal read against the Criterion'
  tags:
  - plugin
  - harness
update:
- slug: rule-plugin-install
  replace:
  - old: The skill first runs `uv --version`; when the tool `uv` is missing, it says that GUPPI needs it and writes nothing.
    new: The skill first runs `uv --version`; when the tool `uv` is missing, it says that GUPPI needs it and asks the person whether it installs `uv` by the standalone installer of `uv`, runs that installer on a yes and `uv --version` again, and writes nothing into the project until `uv --version` passes; on a no, a failed installer or a `uv` that this session of Claude Code does not find yet, it stops and tells the person what to do (case 852.1).
  - old: check uv, copy its files from this plugin
    new: check uv and offer to install it when it is missing, copy its files from this plugin
  - old: 1. Run `uv --version`. When it fails, say that GUPPI needs the tool `uv`, which installs Python and runs the code of GUPPI, and that the person installs `uv` and types `/guppi:install` again, and stop. Write nothing.
    new: |-
      1. Run `uv --version`. When it passes, go on with step 2. When it fails, say that GUPPI needs the tool `uv`, which installs Python and runs the code of GUPPI, and ask the person whether you install `uv` now by its standalone installer. On Windows its command is `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`; on macOS and Linux it is `curl -LsSf https://astral.sh/uv/install.sh | sh`. Write nothing into the project until `uv --version` passes.
         - On a no, show the command for this system, say that the person installs `uv` with it and types `/guppi:install` again, and stop.
         - On a yes, run the command for this system. When it fails, or Claude Code does not run it, show its output and the command, say that the person installs `uv` with it and types `/guppi:install` again, and stop.
         - Then run `uv --version` again. When it passes, go on with step 2. When it fails, say that this session of Claude Code does not find the new `uv` yet, and that the person opens a new terminal, starts Claude Code there in this project and types `/guppi:install` again, and stop.
  - old: 7. Say that GUPPI is installed, and that the person reopens Claude Code in this project and types `/hi`.
    new: 7. Say that GUPPI is installed, and that the person reopens Claude Code in this project and types `/hi`. When step 1 installed `uv`, say that the person starts Claude Code from a new terminal, so that the hooks of the project find `uv`.
  change: when uv is missing, /guppi:install asks to install it by the standalone installer of uv and goes on once uv --version passes
```

```tasks
- [x] update `rule-plugin-install`
- [x] Read the standalone installer commands of `https://docs.astral.sh/uv/getting-started/installation/` against the two commands of the new step 1 of `rule-plugin-install` in the Spec; a command that differs is a fork by condition 1 of `rule-where-to-stop`.
- [x] create `estimate-plugin-install-offers-to-install-uv`
- [x] `uv run --project .guppi guppi render`: `plugin/skills/install/SKILL.md`
- [ ] read `estimate-plugin-install-offers-to-install-uv`
```

### Case 852.2 — The check of the Python environment leaves the missing uv out

> **given:**
> `estimate-guppi-package-is-ready-after-the-install`: its Criterion, `purpose` and `method` are replaced.
> **＋** `rule-guppi-package`: the target of that Estimate.
> **＋** `rule-plugin-install`: the skill `/guppi:install`.
> **＋** `/plugin marketplace add <folder>`: the command of Claude Code that adds the copy as a catalogue.
> **＋** `/plugin install guppi@guppi-marketplace`: the command of Claude Code that installs the plugin.
> **＋** `.guppi/.venv/`: the Python environment of GUPPI in the project.
> **＋** `/hi`: the skill the person types after the install.

> **when:**
> The person writes the clean version into a local folder by `uv run --project .guppi guppi ship --allow-draft <folder>`, adds that folder as a catalogue by `/plugin marketplace add <folder>`, installs the plugin by `/plugin install guppi@guppi-marketplace` and types `/guppi:install` in an empty project open in Claude Code, as `rule-plugin-install` sets it.

> **then:**
> Before it writes anything, `/guppi:install` runs `uv --version`.
> **＋** After it copies the files, it runs `uv sync --project .guppi` in the project, which builds the Python environment `.guppi/.venv/` before it tells the person to reopen Claude Code and type `/hi`.
> **＋** The hooks of the project find that environment built at the first `/hi`.
> **－** Where `uv --version` passes, it asks nothing about `uv`.

```then
update:
- slug: estimate-guppi-package-is-ready-after-the-install
  set:
    status: pending
    purpose: Whether /guppi:install runs uv --version before it writes anything and, where it passes, asks nothing about uv and builds the Python environment .guppi/.venv/ by uv sync after the copy before it sends the person to /hi
    method: 'by hand, after a tag prod-x.y.z stands in the history of HEAD: the agent writes the clean version into a local folder by uv run --project .guppi guppi ship --allow-draft; then, at a stop of Work Mode, the person adds that folder as a catalogue, installs the plugin guppi from it and, in an empty project on the machine with uv, types /guppi:install, reopens Claude Code there and types /hi; the person''s answer on the output of the install, the files of the project and its .guppi/.venv/, read against the Criterion; the copy and the project may be those of the reading of estimate-plugin-install-writes-guppi-into-an-empty-project at the same commit'
  change: the Criterion replaced whole — the missing uv is left to estimate-plugin-install-offers-to-install-uv and the failed uv sync to the Estimate of case 853, and the method drops the project with no uv and the offline project
```

```tasks
- [x] update `estimate-guppi-package-is-ready-after-the-install`
- [ ] read `estimate-guppi-package-is-ready-after-the-install`
```

## Case 853 — /guppi:install undoes its copy when uv sync fails

> **context:**
> `/guppi:install` copies the files of GUPPI into an empty project and then runs `uv sync --project .guppi`, which downloads the Python packages and builds `.guppi/.venv/`. Step 6 of its skill says only that when `uv sync` fails, the agent shows the output and stops. In `C:\PROJECTS\test-uv-offline` of session 0104, `uv sync` failed on `ruff==0.16.1` of the `dev` group, and the agent's last sentence still told the person to run `uv sync`, reopen Claude Code and type `/hi`. `.guppi/.venv/` was left unbuilt (handoff of session 0104). The project kept every copied file, and a second `/guppi:install` would refuse it at step 3, because its files already stand. The person said this was bad, and this session recorded `estimate-guppi-package-is-ready-after-the-install` as failed. The person chose that on a failed `uv sync` the agent shows the output, deletes every file it copied and every folder it made, says that the install did not finish, and tells the person to type `/guppi:install` again, with no word on `/hi`. The deletion keeps the Purpose of `rule-plugin-install`, the rule that governs this change: a project loses no file of its own, since the install deletes only what it wrote into a project that held none of those files. The person chose that `uv sync` keeps the `dev` group. A project runs `pytest` and `ruff` through `guppi test` and `guppi style`, as `guppi.toml` sets them, and Work Mode, Retro and the CI of the project run them. From the agent's knowledge of `uv`, which was not read here, `uv run` would install the missing group at the first hook anyway, and with no network and an empty cache `uv` cannot download PyYAML or Python either. The person chose a new Estimate on `rule-plugin-install` for this failure path. Case 852.2 replaced the Criterion of `estimate-guppi-package-is-ready-after-the-install` with a `－` line on a failed `uv sync`. To keep this promise from being signed twice, Case 852 is built again: that line and the offline project leave that Criterion and its `method`, and point to `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails`. The person agreed to that rebuild. Case 852.1 changes the Purpose sentence on a missing `uv`, the description, step 1 and step 7 of `rule-plugin-install`. This Case changes step 6 and adds one sentence after the sentence on `uv sync` in the Purpose, which Case 852.1 does not touch, so the `old` of each pair matches the page as Case 852.1 leaves it. The check of this file notes that the step 6 pair touches a sentence that Case 852.1 changes too. That sentence runs across the end of step 6 and the start of step 7, which the check reads as one sentence. The `old` of this Case ends at the end of step 6, and the `old` of Case 852.1 starts at step 7, so neither pair matches text the other changes. The two new texts were read side by side. The new step 7 of Case 852.1, with its new terminal once step 1 installed `uv`, runs only after a successful step 6. Its new step 1 writes nothing before `uv --version` passes. Both fit the new step 6, which stops before step 7 on a failed `uv sync`. Each sentence of `rule-plugin-install` that states the end of the install was read. In the description, the person reopens Claude Code and types `/hi`. In step 7 and in Case 852.1's new step 7, the install says the person types `/hi`. These stand, since they describe a successful install, which step 6 now leaves before step 7 on a failure. The sentence of step 4, change no other file, stands, since the agent deletes only files it wrote. The Criterion of `estimate-plugin-install-writes-guppi-into-an-empty-project` says that the last message tells the person to type `/hi`. It stands, since its last `－` line puts what the install does about the Python environment outside that promise. A Grep `uv sync` over `vault/wiki/` printed `brief.md`, `log.md`, `rule-plugin-install.md` and `estimate-guppi-package-is-ready-after-the-install.md`, and over `.claude/` printed nothing. The rebuild of Case 852 handles the hit in the Estimate. A Grep `skills/install|rule-plugin-install|"install"` over `.guppi/tests/` printed `test_ship.py` alone. Its tests write their own skill file into a temporary folder and do not read the live skill. `guppi ship --check` refuses a reference to a case in `plugin/skills/install/SKILL.md`, so the new step 6 holds none. The pointer in the new Purpose sentence stands, since the page has no `core: true`. A Glob `vault/**/*undoes*` printed nothing, so the new slug is free. The Case adds no code that judges a text.

> **problem:**
> When `uv sync` fails, `/guppi:install` leaves a half-installed project that a second `/guppi:install` refuses, and the agent still sends the person on to `/hi`.

> **recommend:**
> - **What should `/guppi:install` do when `uv sync` fails?**
>   - Recommended: (a) undo the copy: show the output of `uv sync`, delete every file it copied and every folder it made, `.guppi/` with its `.venv/` included, say that the install did not finish, tell the person to type `/guppi:install` again, and never mention `/hi`.
>   - Answer: agreed, (a).
> - **Should the install's `uv sync` also install `pytest` and `ruff`?**
>   - Recommended: (a) keep the `dev` group in the install; leaving it out only moves the download to the first hook.
>   - Answer: agreed, (a).
> - **How should we check that a failed `uv sync` undoes the install?**
>   - Recommended: (a) a new Estimate on `rule-plugin-install` for the failure path, read by hand in an empty project offline with an empty cache of `uv`; Case 852 is built again so that the check of the Python environment drops its line on a failed `uv sync` and its offline project.
>   - Answer: agreed, (a).

> **given:**
> `rule-plugin-install`: the skill `/guppi:install`, its Purpose and its Render.
> **＋** `plugin/skills/install/SKILL.md`: the skill file rendered from `rule-plugin-install`.
> **＋** `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails`: the new check of this behaviour.
> **＋** `.guppi/.venv/`: the Python environment that `uv sync --project .guppi` builds.
> **＋** `/hi`: the skill the person types after a successful install.
> **＋** `vault/raw/2026-10-16/0342/cases/case-852.md`: the Case of this session that changes the same page and the check of the Python environment.

> **when:**
> The person types `/guppi:install` of `plugin/skills/install/SKILL.md` in an empty project open in Claude Code, where `uv --version` passes, and `uv sync --project .guppi` fails after the copy, such as with no network and an empty cache of `uv`.

> **then:**
> The agent shows the output of `uv sync --project .guppi`.
> **＋** It deletes each file it copied into the project and each folder it made there, `.guppi/` with `.guppi/.venv/` included, so that the project holds only what it held before `/guppi:install`.
> **＋** It says that the install did not finish and that the project stands as before, and that the person types `/guppi:install` again once the cause that the output shows is fixed, and stops.
> **－** It does not tell the person to run `uv sync`, to reopen Claude Code or to type `/hi`.
> **－** It deletes no file or folder that stood in the project before `/guppi:install`, and nothing in the folder of the plugin.

```then
create:
- slug: estimate-plugin-install-undoes-the-copy-when-uv-sync-fails
  ref: rule-plugin-install
  kind: QA
  purpose: Whether /guppi:install, when uv sync fails after the copy, shows its output, deletes every file and folder it wrote into the project, and sends the person to /guppi:install again, not to /hi
  method: 'by hand, after the librarian''s run of the session that sets this Criterion, with a tag prod-x.y.z in the history of HEAD: the clean version written into a local folder by uv run --project .guppi guppi ship --allow-draft, that folder added as a catalogue by /plugin marketplace add and guppi installed from it by /plugin install guppi@guppi-marketplace; in an empty project with Claude Code started from a terminal with UV_OFFLINE=1 and UV_CACHE_DIR set to an empty folder, where uv --version passes, /guppi:install typed; its reply and the files and folders of the project before and after read against the Criterion'
  tags:
  - plugin
  - harness
update:
- slug: rule-plugin-install
  replace:
  - old: so that the first hook of the project does not wait for it ([[rule-guppi-package]], case 819).
    new: so that the first hook of the project does not wait for it ([[rule-guppi-package]], case 819). When `uv sync` fails, the skill shows its output, deletes each file it copied and each folder it made, says that the install did not finish and that the person types `/guppi:install` again, and does not send the person to `/hi` (case 853).
  - old: 6. Run `uv sync --project .guppi` in the project, which builds the Python environment of GUPPI in `.guppi/.venv/`. When it fails, show its output and stop.
    new: 6. Run `uv sync --project .guppi` in the project, which builds the Python environment of GUPPI in `.guppi/.venv/`. When it fails, show its output, then delete each file you copied in step 4 and each folder you made for them, `.guppi/` with its `.venv/` included, so that the project holds only what it held before. Delete nothing else. Say that the install did not finish and that the project stands as before, and that the person types `/guppi:install` again once the cause that the output shows is fixed, and stop. Do not tell the person to run `uv sync`, to reopen Claude Code or to type `/hi`.
  change: when uv sync fails, /guppi:install deletes what it copied, says the install did not finish and sends the person to /guppi:install, not to /hi
```

```tasks
- [x] update `rule-plugin-install`
- [x] create `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails`
- [x] `uv run --project .guppi guppi render`: `plugin/skills/install/SKILL.md`
- [ ] read `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails`
```

## Deferred

## Case 855 — The reading of the session files put off until Case 851 lands

> **context:**
> At /hi of session 0342 the person put off `estimate-clean-branch-writes-the-session-files`. It failed at the Retro of session 0104 on its last clause alone: the first `/hi` in an empty folder with no git repository stopped on `git branch --show-current`. Case 851 of this session makes `/hi` offer `git init -b main` there and go on to `/sprint-open`, and its context says the Criterion of this Estimate holds with it. The skill file of `/hi` changes only at the render after the librarian's run, so no reading runs in this session.

> **problem:**
> No reading of `estimate-clean-branch-writes-the-session-files` can run in this session, since the fix of Case 851 lands only at the render after the librarian's run.

```then
defer:
  - slug: estimate-clean-branch-writes-the-session-files
    type: estimate
    purpose: "Failed at Retro of session 0104 on the first /hi outside a git repository; its reading waits for the render of Case 851 and an install by hand into an empty folder with no git, beside the readings of Cases 852 and 853; put off at /hi of session 0342"
```
