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

> **tasks:**
> - [ ] update `rule-git-context`
>   - old:
>     ```
>     Branch: !`git branch --show-current`
>     Status: !`git status --short`
>     ```
>   - new:
>     ```
>     Branch: !`uv run --project .guppi guppi gitstate`
>
>     When the line `Branch:` above reads `none: this folder is no git repository`, take this step first, before `/sprint-open` and before the Frontier (as set in case 851.1). Say that GUPPI works only in a git repository, and ask the person whether you run `git init -b main`, which names the first branch `main`. On the person's yes, run `git init -b main` with the Bash tool, say that the repository is made, and tell the person to type `/hi` again. On a no, tell the person to type `/hi` again after `git init -b main`. After either answer, start no `/sprint-open`, write no Frontier, and end the reply.
>     ```
>   - old: `` `/hi` runs no `git pull` ``
>   - new: `` `uv run --project .guppi guppi gitstate` of `.guppi/guppi/gitstate.py` prints the branch, then `Status:` and the status, or, in a folder that is no git repository, one line that says so, and it exits 0 in each case, since Claude Code stops the whole skill on a `!` command that fails: two git commands stood on these lines until a first `/hi` in an empty project stopped on a git error (as set in case 851). `/hi` runs no `git pull` ``
>   - set:
>     ```
>     implementation_ref: [.guppi/guppi/gitstate.py, .guppi/tests/test_gitstate.py]
>     ```
>   - change: `the branch and the status come from guppi gitstate, and outside a git repository /hi asks to run git init -b main and ends`
> - [ ] update `rule-skill-hi`
>   - old: `Bash(git branch --show-current), Bash(git status --short)`
>   - new: `Bash(uv run --project .guppi guppi gitstate)`
>   - old: `` start `/sprint-open` first, as the hook on `/hi` says: ``
>   - new: `` start `/sprint-open` first, unless the step of `rule-git-context` above ends the reply, as the hook on `/hi` says: ``
>   - old: `` `allowed-tools` names the four `!` commands of the skill: ``
>   - new: `` `allowed-tools` names the three `!` commands of the skill, and not `git init -b main`, which the agent runs in a folder that is no git repository only on the person's yes and with the person's leave in Claude Code, as `rule-git-context` sets it: ``
>   - change: `allowed-tools names guppi gitstate in place of the two git commands, and /sprint-open waits for the git step`
> - [ ] update `rule-default-mode`
>   - old: `own and not a line of the registry (case 85.4).`
>   - new: `` own and not a line of the registry (case 85.4). One write comes before a Case: at `/hi` in a folder that is no git repository, the agent runs `git init -b main` on the person's yes, which writes `.git/`, since a session of GUPPI needs a git repository, as `rule-git-context` sets it (as set in case 851.1). ``
>   - change: `one exception: git init -b main at /hi on the person's yes`
> - [ ] create `estimate-git-context-offers-git-init`
>   - ref: `rule-git-context`
>   - kind: `QA`
>   - purpose: `Whether /hi in a folder that is no git repository asks to run git init -b main, runs it on the person's yes and ends, ends on a no, and opens no sprint and writes no Frontier either way`
>   - method: `by hand, after the librarian's run: in an empty folder that is no git repository, GUPPI installed by /guppi:install from a copy that uv run --project .guppi guppi ship --allow-draft wrote into a local folder, Claude Code opened there, /hi typed and answered no, /hi typed again and answered yes, then /hi typed a third time, and the replies, the context of each /hi, the session folders and git branch --show-current read against the Criterion`
>   - tags: `[session, harness, git]`
> - [ ] `uv run --project .guppi guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] read `estimate-git-context-offers-git-init`

> **ratification:**
> ```
> - decision[case 851.1][update][rule-git-context]{ref:rule-git-context}
> - decision[case 851.1][update][rule-skill-hi]{ref:rule-skill-hi}
> - decision[case 851.1][update][rule-default-mode]{ref:rule-default-mode}
> - decision[case 851.1][create][estimate-git-context-offers-git-init]{ref:rule-git-context}{tags:session,harness,git}
> ```

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

> **tasks:**
> - [ ] update `estimate-hi-no-read-calls`
>   - set:
>     ```
>     status: pending
>     method: "by hand, after the librarian's run of the session that sets this Criterion: at the first /hi after it, the first turn's context and the tool calls before it read in the transcript, and the allowed-tools of .claude/skills/hi/SKILL.md, written into the estimate line"
>     ```
>   - change: `the Criterion replaced whole — allowed-tools names guppi gitstate in place of the two git commands`
> - [ ] read `estimate-hi-no-read-calls`

> **ratification:**
> ```
> - decision[case 851.2][update][estimate-hi-no-read-calls]{ref:rule-skill-hi}
> ```

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

> **tasks:**
> - [ ] `.guppi/guppi/gitstate.py`: the command `guppi gitstate`, which runs `git rev-parse --is-inside-work-tree` in the project folder; when it prints `true`, the command prints the output of `git branch --show-current`, then the line `Status:` and the lines of `git status --short`; otherwise, a failed or missing git included, the one line `none: this folder is no git repository`; exit 0 in each case.
> - [ ] `.guppi/guppi/cli.py`: `gitstate` in `COMMANDS`.
> - [ ] `.guppi/tests/test_gitstate.py`: the command in a temporary folder with no git repository above it prints the one line and exits 0; after `git init -b main` in that folder it prints `main`, the line `Status:` and a line for an untracked file, and exits 0.
> - [ ] create `estimate-git-context-gitstate-exits-zero`
>   - ref: `rule-git-context`
>   - kind: `QA`
>   - purpose: `Whether guppi gitstate prints the branch and the status in a git repository, and one line in a folder that is no git repository, and exits 0 in each case`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_gitstate.py`
>   - tags: `[session, harness, git]`
> - [ ] read `estimate-git-context-gitstate-exits-zero`

> **ratification:**
> ```
> - decision[case 851.3][create][estimate-git-context-gitstate-exits-zero]{ref:rule-git-context}{tags:session,harness,git}
> ```
