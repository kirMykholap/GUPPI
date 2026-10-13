## Case 794 — The history on GitHub starts at the harness, and only style and test block a merge

> **context:**
> Case 787.1 set up the repository `GUPPI` on GitHub. In Work Mode the workflow `.github/workflows/checks.yml` and the scan of the history were done, and the push waits at its stop. Two of its choices changed before the push. First, the history goes up whole today. The reflog of `main` shows that the tag `vault-v1` marks the commit `afb1b914`, the clone from `c:/PROJECTS/job hunt ai`, and that its child `8b34941a` is the commit "chore: the product leaves, and the repository becomes the harness and the vault". Every commit before it belongs to the former product. The person chose to cut the history there: `8b34941a` becomes the first commit, and each later commit keeps its files and message with a new id. Second, Case 787.1 makes the three jobs of the workflow block a merge into `main`. `make lint` exits non-zero at the Baseline of this session in `work.md`, and the glossary row of Lint says that its red is a signal, not a gate. So with lint required, no pull request from outside could merge. The person chose that only `style` and `test` block a merge, and that `lint` runs and shows its result. This Case is Case 787.1 built again under a new number, since a ratified Case is not taken back in Work Mode. Its decision line carries `{supersedes:case 787.1}`. Case 787.2 stands as it is. Its sentence that `origin` had been the product repository this vault was split from stays true. The text of 787.1 is carried but for the lines below. The Purpose of `rule-github-repository` says that the history on GitHub starts at the cut, and that only `style` and `test` block a merge. The Criterion of `estimate-sprint-plugin-pull-requests-reviewed-on-github` is replaced whole again. Its line on the three checks now names `style` and `test`, and a new `－` line says that a red `lint` blocks no merge. Its `purpose` and `method` do not name which checks block, so they are set as Case 787.1 set them. The tasks gain the cut, a check by hand before the push, a change of `README.md`, and the removal of the backup after the push. A local backup branch holds the old history while the cut is made and checked, so a cut that went wrong can be undone and needs no stop. After the push is checked, the backup branch and the tag `vault-v1` are removed and git clears the old commits. git cannot undo that, so it is a stop by the third condition of `rule-where-to-stop`. The history of the product stays in the owner's local product repository: a Glob found `c:/PROJECTS/job hunt ai/.git/HEAD`. Pages that quote a commit id stay as records, by the person's answer. A Grep `\b(commit|commits|run of|at|of) [0-9a-f]{7,40}\b` over `vault/wiki/` printed 27 occurrences across 25 files. After the cut those ids open nowhere, and their text stays as it is. A Grep `rev-parse|merge-base|rev-list|filter-repo|filter-branch` over the repository outside `vault/` printed nothing, so no code reads a stored commit id. A Grep `(?i)whole history|job hunt|split (out|from)` over the repository outside `vault/raw/` and `vault/archive/` printed `README.md` and `vault/wiki/rules/rule-git-context.md`. The sentence of `README.md` that the project was split out with the whole history becomes false at the push, so a task changes it. The hit in `rule-git-context` is the sentence that Case 787.2 changes, and it stays true. A Grep `README|sprint-plugin|github-repository|checks\.yml` over `tests/` printed `tests/test_prespec.py` and `tests/test_lint.py`. Both build their pages under a temporary folder or hold the name as a string, so no test reads a file this Case changes. The cut itself is checked by hand in Work Mode before the push, since a fault found after the push cannot be undone. The Estimate checks the pull request, as the person chose.

> **problem:**
> Case 787.1 would push the whole history, the former product's commits included. It would also make `lint` block every merge into `main`, though lint is red at the Baseline and is only a signal.

> **recommend:**
> - **Change**
>   - Asked: the person, in Work Mode, chose to cut the history at `8b34941a` before the first push, so that the commits after it keep their content with new ids, and to make only `style` and `test` required on `main`, with `lint` shown but not blocking.
>   - Taken: Case 787.1 is built again as Case 794 with `{supersedes:case 787.1}`. The Purpose of `rule-github-repository`, the Criterion of `estimate-sprint-plugin-pull-requests-reviewed-on-github` and the tasks change as `context` says.
> - **Where should the old history stay on this computer?**
>   - Recommended: (b) a local backup branch only while the cut is made and checked; after the push and its check, the backup branch and the tag `vault-v1` are removed, and git clears the old commits.
>   - Answer: agreed, (b).
> - **What happens to the commit ids that pages already quote?**
>   - Recommended: (a) they stay as records; the texts do not change.
>   - Answer: agreed, (a).
> - **Does this Case change the README sentence about the history?**
>   - Recommended: (a) this Case changes the sentence before the push: the public history starts at the commit that removed the product, and the earlier history stays only in the owner's local copy.
>   - Answer: agreed, (a).
> - **How is the cut checked?**
>   - Recommended: (a) a check by hand in Work Mode just before the push: the first commit has no parent and holds the files of the commit that removed the product, the last commit of `plugin` holds the same files as before the cut, and a search of the new history for the key and the token finds nothing; the check page of the sprint keeps only the pull request.
>   - Answer: agreed, (a).

> **given:**
> `rule-github-repository`: the new rule of the repository on GitHub, its history, its rulesets and its CI.
> **＋** `.github/workflows/checks.yml`: the workflow whose jobs `style`, `test` and `lint` run the checks.
> **＋** `estimate-sprint-plugin-pull-requests-reviewed-on-github`: its Criterion is replaced whole.
> **＋** `entity-sprint-plugin`: the sprint whose milestone asks for the repository.
> **＋** `Makefile`: the targets `test`, `lint` and `style` that the workflow runs.
> **＋** `README.md`: its sentence on the history of the project.
> **＋** `rule-where-to-stop`: the push, the login and the removal of the old history wait for the person's word.

> **when:**
> In a session of the sprint `plugin` before its close, someone opens a pull request against the branch `main` of the repository `GUPPI` on GitHub, which `rule-github-repository` describes, from an account other than the owner's, such as a second account that the owner made for the test.

> **then:**
> The workflow `.github/workflows/checks.yml` runs `make test`, `make lint` and `make style` of the `Makefile` on `windows-latest` on the pull request, and shows each result on it.
> **＋** A run of a first-time contributor waits until the owner approves it.
> **＋** The owner reviews the pull request on GitHub, and only the owner can merge it.
> **＋** A merge into `main` waits until the jobs `style` and `test` pass, except for the owner, who is on the bypass list of the ruleset on `main`.
> **＋** The other account cannot push to `main` or to `prod`, and a pull request against `prod` cannot be merged.
> **－** A red result of the job `lint` does not block a merge into `main`.
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
>     Prevents a pull request from reaching `main` unchecked, and an account other than the owner's from writing to `main` or `prod`. The repository of the project is the public repository `GUPPI` on GitHub, on the owner's account, and `origin` points to it. Its history starts at the commit that removed the former product from the repository and made it the harness and the vault. The commits of that product before it are not on GitHub, and no copy of them is kept in this repository (case 794). A ruleset on `main` blocks its deletion and a force push, takes a change only by a pull request, and lets a pull request merge only after the jobs `style` and `test` of `.github/workflows/checks.yml` pass. The job `lint` runs too and shows its result on the pull request, but it blocks no merge, since the red of lint is a signal, not a gate ([[rule-lint]]). The owner is on the bypass list of the ruleset, so the owner's own push and merge still work. No approving review is required, since GitHub lets no one approve their own pull request. A ruleset on the name `prod` blocks the creation, the update and the deletion of the branch and a force push. Only the owner bypasses it, so a pull request into `prod` cannot be merged. The item The clean branch of [[entity-sprint-plugin]] adds the CI that writes `prod` to that bypass list. The workflow runs `make test`, `make lint` and `make style` on `windows-latest`, where the suite is known to run. It runs on each pull request by the event `pull_request`, never `pull_request_target`, so the code of a pull request reaches no secret. It also runs on each push to a branch other than `prod`. A run of a first-time contributor waits for the owner's approval. Only the owner pushes, by hand when the owner wants, by `! git push`. A session pushes nothing during a sprint, and a new sprint branch goes up at the owner's first push, after which the workflow runs on it. The owner's own pull request into `main` waits for `style` and `test` too, and the owner's bypass stays for a push the owner makes by hand. The rulesets and the approval are settings of the repository on GitHub, not files: a clone, a fork or an install of GUPPI does not carry them.
>     ```
> - [ ] `.github/workflows/checks.yml`: on `pull_request` and on `push` to every branch but `prod`, on `windows-latest`, three jobs `style`, `test` and `lint`, each sets up uv and runs its `make` target.
> - [ ] stop: the person runs `gh auth login` in the shell, since the login asks questions only the person can answer.
> - [ ] The whole history searched before the push: `git log -p --all` for local paths, email addresses, keys and tokens, and `git log --all --format=%ae` for the author addresses; the findings shown to the person.
> - [ ] The history cut: a local backup branch at the old tip of `plugin`, then `main` and `plugin` written again so that the commit of `8b34941a`, "chore: the product leaves, and the repository becomes the harness and the vault", is their first commit with no parent, and each later commit keeps its files, its message and its author with a new id.
> - [ ] `README.md`: the sentence that the project was split out of the `job hunt ai` repository with the whole history, at the tag `vault-v1` there, says instead that it was split out of that repository on 2026-09-07, that its history starts at the commit that removed the product, and that the earlier history of the product stays in the owner's local copy of that repository and is not public.
> - [ ] by hand, before the push: the first commit of the new `main` and `plugin` has no parent and holds the files of `8b34941a`; the last commit of the new `plugin` holds the same files as the old tip in the backup branch; `git log -p` of the new `main` and `plugin` holds none of the keys and tokens that the scan of the history found; the result shown to the person.
> - [ ] stop: after the person's word on that check, `gh repo create GUPPI --public --source . --remote origin`, then `git push -u origin main plugin`.
> - [ ] The settings of the repository by `gh api`: the ruleset on `main` with the jobs `style` and `test` as required checks and `lint` not required, the ruleset on `prod` and the approval of the runs of first-time contributors, as the Purpose of `rule-github-repository` sets them.
> - [ ] stop: after the person's word, once the first commit of `main` and `plugin` on GitHub is read as the cut commit, the backup branch and the tag `vault-v1` are deleted, and `git reflog expire --expire=now --all` and `git gc --prune=now` clear the old commits from this repository.
> - [ ] update `estimate-sprint-plugin-pull-requests-reviewed-on-github`
>   - set: `{status: pending, purpose: "Whether a pull request from another account, a second account of the owner included, runs the checks of CI on GitHub and can be reviewed and merged into the branch main by the owner alone"}`
>   - change: `the Criterion replaced whole — the pull request goes against main, only style and test block a merge, only the owner merges, the test pull request is closed without a merge`
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
>   - sections.Closed: `- The sprint turn and GitHub: the repository on GitHub set up so that a pull request from another person is easy to review (case 794)`
>   - change: `the milestone The sprint turn and GitHub closed — out of Milestones, named in Closed (case 794)`
> - [ ] `uv run guppi sprint`
> - [ ] read `estimate-sprint-plugin-pull-requests-reviewed-on-github`

> **ratification:**
> ```
> - decision[case 794][create][rule-github-repository]{supersedes:case 787.1}{tags:github,ci,git}
> - decision[case 794][update][estimate-sprint-plugin-pull-requests-reviewed-on-github]{ref:entity-sprint-plugin}
> - decision[case 794][update][entity-sprint-plugin]{ref:entity-sprint-plugin}
> ```
