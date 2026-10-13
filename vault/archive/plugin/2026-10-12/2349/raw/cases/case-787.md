## Case 787 — The repository on GitHub takes pull requests into main

> **context:**
> The milestone The sprint turn and GitHub of `entity-sprint-plugin` asks for the repository on GitHub, set up so that a pull request from another person is easy to review. Today nothing of it exists: `.git/config` holds no `[remote]` section, and a Glob `.github/**` printed nothing. The person wants a public repository. Only the owner pushes. Every pull request goes into `main`, and `prod` is a branch that only the owner and later the CI write. No page governs a CI file or the settings of a GitHub repository. The ask-guppi query found these facts. The index lines of `vault/wiki/rules/` and `vault/wiki/entities/` hold no rule or entity on GitHub, CI or a remote. The lessons hold one near hit: `lesson-obsidian-cli-needs-the-running-app` names CI only as a place where that CLI cannot run. The insights hold none. A Glob `vault/**/rule-github*.md` printed only `vault/archive/migration/2026-09-30/0138/rules/rule-github-issues.md`, so `rule-github-repository` is free. The tags `github`, `ci` and `git` exist in `tags.md`. Case 787.1 creates `rule-github-repository` for the rulesets, the CI workflow and the approval of outside runs. Its list of Estimates stays empty for now. Until the sprint closes, `estimate-sprint-plugin-pull-requests-reviewed-on-github` checks the setup, and a later Case gives the rule a lasting Estimate. The Criterion of that sprint Estimate expects a pull request against `plugin` and a merge into `plugin` (case 766). The person now sends every pull request into `main`, so Case 787.1 replaces the Criterion whole and sets its `purpose` anew. None of its old lines is carried on purpose. The trigger now names `main`, not `plugin`. The line on the checks of CI becomes the line that names the workflow and its three checks. The merge into `plugin` becomes a merge into `main` that only the owner can do. The exception that `main` takes the pull request with `plugin` at the close becomes the test pull request closed without a merge. Its `method` stands, since it does not name the branch. Case 789 leaves that Criterion to this Case. This Case closes the Frontier line of the sprint item, so 787.1 also updates `entity-sprint-plugin`. The milestone The sprint turn and GitHub leaves `## Milestones` and is named under `## Closed` with this Case, as case 321 closed a Slice of `entity-sprint-migration`. The item is a plain line, a note, which `rule-sprint` keeps open until a Case cuts it into items or removes it. It is not cut into an item that names `rule-github-repository`, since an item ticks only when its page is `built`, and the cascade of `guppi/generate.py` leaves a page with no Estimate as it stands. The change of the sprint page and of the Estimate's purpose makes `sprint.md` stale, so 787.1 runs `uv run guppi sprint`. The remote makes two texts false. `rule-git-context` says the repository has no remote since case 528. The Criterion of `estimate-git-context-current` says that `git remote` prints no remote. A Grep `(?i)no remote|prints no remote|has no remote` over `vault/wiki/` and `.claude/` printed `vault/wiki/log.md`, `vault/wiki/rules/rule-git-context.md` and `vault/wiki/estimates/estimate-git-context-current.md`; `log.md` is not read. Case 787.2 changes both texts, and `/hi` still runs no `git pull`. One old line of that Criterion is not carried on purpose: the line that `git remote` prints no remote becomes the line that it prints `origin`. Its other lines stand as they were. Only a `/hi` gives the context that the Criterion reads, and the `/hi` of this session ran before the push. So 787.2 sets the `method` anew to wait for the first `/hi` after the first push to GitHub, a part that opens with `by hand, after` and names its event, as case 781 allows. `rule-rules-schema` says that a Leaf which still carries `## How it works` drops the section at its next touch, the mechanism living in the docstring of its code or in its Render. `rule-git-context` renders commands into `.claude/skills/hi/SKILL.md` and has no code with a docstring. The section stays here all the same, and 787.2 changes only its sentence on the remote by a `replace` pair; the Purpose stands as it is. No form of an `update` removes a section today: `body` in `guppi/generate.py` writes a section set to empty text as its heading alone. `rule-vault-layout` says that no file of `wiki/` is written by hand, so no task removes the section by hand either. By the person's answer, the form of an `update` that drops a section is put off to the backlog by a defer of `rule-page-generation`. A later Case moves the facts of the section into the Purpose and drops the section in one step, once that form exists. The new sentence says how the local `main` and a sprint branch take the work of GitHub. The local `main` follows `origin/main` by `git fetch origin` and `git merge --ff-only origin/main` in the opening Case of a sprint, which Case 789.1 sets. A sprint branch takes `main` by the merge Case of `/merge-main`, which Case 790 sets. Before anything goes public, the history is scanned. A Grep `(?i)users[\\/]+kir` over the repository printed 10 files: this case file and 9 under `vault/archive/migration/`, for example a handoff that names a plan file under `C:\Users\kir\.claude\plans\`. This Case pushes `main` and `plugin` only. By the person's answer to the report of `/pre-spec`, a session pushes nothing during a sprint. The owner pushes a sprint branch by hand when the owner wants, by `! git push`. CI runs on a sprint branch after that push, and a new sprint branch goes up at the owner's first push. The push of the closed branch in the opening Case of the next sprint is a step of Case 789.1. The owner's own pull request there waits for green checks before its merge, which is Case 789.1's too, and the bypass of the owner on `main` stays. `estimate-sprint-plugin-ci-writes-a-clean-branch` waits for a commit that lands on `plugin` on GitHub before the close. Under this Case that commit lands by the owner's push, and its Criterion stands. What `prod` holds, and whether the clean version leaves out `.github/` and `rule-github-repository`, is the item The clean branch of `entity-sprint-plugin`, which also adds the CI to the bypass list of `prod`. A Grep `git-context|pull-requests-reviewed|sprint-plugin|\.github|git remote` over `tests/` printed `tests/test_guard.py`, `tests/test_prespec.py` and `tests/test_lint.py`. Each builds its pages under a temporary folder or holds the name as a string, so none reads a live file this Case changes.

> **problem:**
> The project has no repository on GitHub, so nobody else can propose work and no check runs on a proposal. The vault still promises a pull request into `plugin`, and it states that the repository has no remote.

> **recommend:**
> - **Which page describes the GitHub setup**
>   - Recommended: (a) a new rule page `rule-github-repository`, its Estimates empty for now, the sprint Estimate checks the setup until the sprint closes.
>   - Answer: agreed, (a).
> - **What the ruleset on `main` enforces**
>   - Recommended: (a) no deletion, no force push, every change by a pull request, the CI checks must pass before a merge; no approving review; the owner on the bypass list.
>   - Answer: agreed, (a).
> - **What the ruleset on `prod` enforces now**
>   - Recommended: (a) a ruleset now that blocks creation, updates, deletion and force pushes, only the owner bypasses it; the CI writer is added by the later item The clean branch.
>   - Answer: agreed, (a).
> - **What CI runs, on which machine and when**
>   - Recommended: (a) `make test`, `make lint` and `make style` on `windows-latest`, on every pull request by `pull_request` and on every push to `main` and a sprint branch; all three required; a first-time contributor's run waits for approval.
>   - Answer: agreed, (a).
> - **What the test pull request must prove**
>   - Recommended: (a) against `main`, the checks shown, reviewed by the owner with the merge open to the owner, the second account cannot push to `main` or `prod`, then closed without a merge.
>   - Answer: agreed, (a).
> - **What happens to the claim that the repository has no remote**
>   - Recommended: (a) the remote is stated, and `/hi` still runs no pull.
>   - Answer: agreed, (a).
> - **How the history is checked before it goes public**
>   - Recommended: (a) a scan of the whole history for local paths, email addresses, keys and tokens, then a stop for the person's word before the push; a path that names only the user folder stays.
>   - Answer: agreed, (a).
> - **The repository's name and the branches pushed first**
>   - Recommended: (a) `GUPPI`, public, on the owner's account, `main` and `plugin` pushed first.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the person agreed to the fixes of the report of `/pre-spec`. A session pushes nothing during a sprint: the owner pushes a sprint branch by hand, CI runs after that push, and a new branch goes up at the owner's first push. The Case closes the sprint item on the sprint page. The text of `rule-git-context` names how the local `main` and a sprint branch take the work of GitHub. Its `## How it works` leaves as the schema of a rule sets it. The check of the session start waits for the first `/hi` after the push.
>   - Taken: in 787.1 the Purpose of `rule-github-repository` says who pushes and when. An `update` of `entity-sprint-plugin` moves the milestone The sprint turn and GitHub to `## Closed`. In 787.2 the facts of `## How it works` move into the Purpose of `rule-git-context`, which names the opening Case of a sprint and `/merge-main`. A one-off task removes the section. The `method` of `estimate-git-context-current` waits for the first `/hi` after the first push, and its trigger is `/hi` alone.
> - **How the section `## How it works` leaves `rule-git-context`**
>   - Recommended: (c) a new form of `update` that removes a section, set by a Case of its own, which this Case then uses.
>   - Answer: agreed, (c); that Case is Case 792 of this session.
> - **Change**
>   - Asked: the main agent's reading, which the person's answer above settles: no task removes the section by hand, since `rule-vault-layout` says that no file of `wiki/` is written by hand. The section leaves through the `update` itself, in the form that Case 792 sets.
>   - Taken: in 787.2 the one-off task is gone. The `update` of `rule-git-context` drops `## How it works` by the key `drop`.
> - **When the section `## How it works` leaves `rule-git-context`**
>   - Recommended: (b) this session changes only the sentence on the remote inside `## How it works`; a later Case moves the facts into the Purpose and drops the section in one step, once a form of `update` that drops a section exists.
>   - Answer: agreed, (b); the Case on that form was put off to the backlog by a defer of `rule-page-generation`.

### Case 787.1 — A pull request into main is checked and reviewed on GitHub

> **given:**
> `rule-github-repository`: the new rule of the repository on GitHub, its rulesets and its CI.
> **＋** `.github/workflows/checks.yml`: the new workflow that runs the checks.
> **＋** `estimate-sprint-plugin-pull-requests-reviewed-on-github`: its Criterion is replaced whole.
> **＋** `entity-sprint-plugin`: the sprint whose milestone asks for the repository.
> **＋** `Makefile`: the targets `test`, `lint` and `style` that the workflow runs.
> **＋** `rule-where-to-stop`: the push and the login wait for the person's word.

> **when:**
> In a session of the sprint `plugin` before its close, someone opens a pull request against the branch `main` of the repository `GUPPI` on GitHub, which `rule-github-repository` describes, from an account other than the owner's, such as a second account that the owner made for the test.

> **then:**
> The workflow `.github/workflows/checks.yml` runs `make test`, `make lint` and `make style` of the `Makefile` on `windows-latest` on the pull request, and shows each result on it.
> **＋** A run of a first-time contributor waits until the owner approves it.
> **＋** The owner reviews the pull request on GitHub, and only the owner can merge it.
> **＋** A merge into `main` waits until the three checks pass, except for the owner, who is on the bypass list of the ruleset on `main`.
> **＋** The other account cannot push to `main` or to `prod`, and a pull request against `prod` cannot be merged.
> **－** The workflow does not run on the event `pull_request_target`, so the code of the pull request reaches no secret of the repository.
> **－** The test pull request is closed without a merge, so `main` takes no commit before `plugin` closes.

> **tasks:**
> - [ ] create `rule-github-repository`
>   - type: `rule`
>   - kind: `Leaf`
>   - purpose: `Prevents a pull request from reaching main unchecked, and an account other than the owner's from writing to main or prod`
>   - enforcement: `check`
>   - implementation_ref: `[.github/workflows/checks.yml]`
>   - tags: `[github, ci, git]`
>   - sections.Purpose:
>     ```
>     Prevents a pull request from reaching `main` unchecked, and an account other than the owner's from writing to `main` or `prod`. The repository of the project is the public repository `GUPPI` on GitHub, on the owner's account, and `origin` points to it. A ruleset on `main` blocks its deletion and a force push, takes a change only by a pull request, and lets a pull request merge only after the checks of `.github/workflows/checks.yml` pass. The owner is on its bypass list, so the owner's own push and merge still work. No approving review is required, since GitHub lets no one approve their own pull request. A ruleset on the name `prod` blocks the creation, the update and the deletion of the branch and a force push. Only the owner bypasses it, so a pull request into `prod` cannot be merged. The item The clean branch of [[entity-sprint-plugin]] adds the CI that writes `prod` to that bypass list. The workflow runs `make test`, `make lint` and `make style` on `windows-latest`, where the suite is known to run. It runs on each pull request by the event `pull_request`, never `pull_request_target`, so the code of a pull request reaches no secret. It also runs on each push to a branch other than `prod`. A run of a first-time contributor waits for the owner's approval. Only the owner pushes, by hand when the owner wants, by `! git push`. A session pushes nothing during a sprint, and a new sprint branch goes up at the owner's first push, after which the workflow runs on it. The owner's own pull request into `main` waits for its checks too, and the owner's bypass stays for a push the owner makes by hand. The rulesets and the approval are settings of the repository on GitHub, not files: a clone, a fork or an install of GUPPI does not carry them.
>     ```
> - [ ] `.github/workflows/checks.yml`: on `pull_request` and on `push` to every branch but `prod`, on `windows-latest`, three jobs `style`, `test` and `lint`, each sets up uv and runs its `make` target.
> - [ ] stop: the person runs `gh auth login` in the shell, since the login asks questions only the person can answer.
> - [ ] The whole history searched before the push: `git log -p --all` for local paths, email addresses, keys and tokens, and `git log --all --format=%ae` for the author addresses; the findings shown to the person.
> - [ ] stop: after the person's word on the findings, `gh repo create GUPPI --public --source . --remote origin`, then `git push -u origin main plugin`.
> - [ ] The settings of the repository by `gh api`: the ruleset on `main`, the ruleset on `prod` and the approval of the runs of first-time contributors, as the Purpose of `rule-github-repository` sets them.
> - [ ] update `estimate-sprint-plugin-pull-requests-reviewed-on-github`
>   - set: `{status: pending, purpose: "Whether a pull request from another account, a second account of the owner included, runs the checks of CI on GitHub and can be reviewed and merged into the branch main by the owner alone"}`
>   - change: `the Criterion replaced whole — the pull request goes against main, only the owner merges, the test pull request is closed without a merge`
> - [ ] update `entity-sprint-plugin`
>   - old:
>     ```
>     ### The sprint turn and GitHub
>
>     - the repository on GitHub set up so that a pull request from another person is easy to review
>
>     ### The clean branch
>     ```
>   - new: `### The clean branch`
>   - sections.Closed: `- The sprint turn and GitHub: the repository on GitHub set up so that a pull request from another person is easy to review (case 787)`
>   - change: `the milestone The sprint turn and GitHub closed — out of Milestones, named in Closed (case 787)`
> - [ ] `uv run guppi sprint`
> - [ ] read `estimate-sprint-plugin-pull-requests-reviewed-on-github`

> **ratification:**
> ```
> - decision[case 787.1][create][rule-github-repository]{tags:github,ci,git}
> - decision[case 787.1][update][estimate-sprint-plugin-pull-requests-reviewed-on-github]{ref:entity-sprint-plugin}
> - decision[case 787.1][update][entity-sprint-plugin]{ref:entity-sprint-plugin}
> ```

### Case 787.2 — The session start knows the remote and still pulls nothing

> **given:**
> `rule-git-context`: the rule of the git lines of `/hi`, which states the remote.
> **＋** `estimate-git-context-current`: its Criterion is replaced whole.
> **＋** `.claude/skills/hi/SKILL.md`: the skill whose commands the Criterion runs.

> **when:**
> The person invokes `/hi`, and `.claude/skills/hi/SKILL.md` runs the commands of `rule-git-context`.

> **then:**
> The context holds `Render:` with the output of `uv run guppi render --sync` (a diff for each governed file that differed and was written, or nothing), then `Branch:` with the current branch and `Status:` with `git status --short`.
> **＋** `git remote -v` prints `origin` with the URL of the repository `GUPPI` on GitHub.
> **－** The skill runs no `git pull`, and the context holds no `Pull:` line.

> **tasks:**
> - [ ] update `rule-git-context`
>   - old: `` The repository has no remote since case 528: `origin` was the product repository this vault was split from and `migration` had no upstream, so the pull that stood first in this block failed at every session start. `/hi` runs no `git pull`; a Case that adds a remote writes its pull line and its rule again. ``
>   - new: `` From case 528 to case 787 the repository had no remote: `origin` had been the product repository this vault was split from and `migration` had no upstream, so the pull that stood first in this block failed at every session start. Since case 787 `origin` is the public repository `GUPPI` on GitHub, and `/hi` still runs no `git pull`. The local `main` follows `origin/main` in the opening Case of a sprint, by `git fetch origin` and `git merge --ff-only origin/main` (case 789.1), and a sprint branch takes `main` by the merge Case of `/merge-main` (case 790). ``
>   - change: `the remote is the repository GUPPI on GitHub; /hi still runs no git pull`
> - [ ] update `estimate-git-context-current`
>   - set: `{status: pending, method: "by hand, after the first /hi that follows the first push to GitHub: the first turn's context, the output of git remote -v and .claude/skills/hi/SKILL.md read against the Criterion, written into the estimate line"}`
>   - change: `the Criterion replaced whole — git remote prints origin, the repository GUPPI on GitHub; /hi still runs no git pull`
> - [ ] read `estimate-git-context-current`

> **ratification:**
> ```
> - decision[case 787.2][update][rule-git-context]{ref:rule-git-context}
> - decision[case 787.2][update][estimate-git-context-current]{ref:rule-git-context}
> ```
