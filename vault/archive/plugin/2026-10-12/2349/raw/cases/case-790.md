## Case 790 — A sprint branch takes in main by one merge Case before its close

> **context:**
> Each branch already has its own documentation, since `vault/` is tracked in git and every branch carries its own copy of it. The person plans a public repository: others run a sprint on their own branch and open a pull request of the whole branch into `main`. When two branches change one page, git stops on a conflict. A rule page that both branches updated conflicts at least in its History, since each side adds a line at its end. Nothing says today how such a conflict is settled, and the rules leave no way to settle it: `rule-vault-layout` says that no file of `wiki/` is written by hand, and `rule-page-generation` says that the script is the only writer to `wiki/`. Case 789 of this session sets that the author of a branch settles its conflicts and that the owner takes a pull request into `main` by `/pr-review`. The person chose the following. The close of a sprint archives what it archives today. `estimate-sprint-close-archives-the-decisions` and `estimate-sprint-close-archives-done-insights-and-lone-lessons` check that, and their Criteria stand. They keep live a Decision page that a live page names in `deferred_by` or `addressed_by`, an open Insight with its lessons, and a `knowledge` lesson, so open debt crosses into `main` with the branch. The author runs a new skill, `/merge-main`, in a session of its own, after the work of the sprint and before `/sprint-close`. The merge Case is the one Case of that session. Files that a command writes are written again rather than joined. `log.md` and `tags.md` keep the lines of both sides. Every other conflicted file takes a joined text that the person signs in the merge Case, and Work Mode writes that text into the file without the librarian. The merge Case is recorded as any Case: its decision lines add a History line to the live sprint page and to each joined page, and set `pending` each Estimate whose Criterion speaks of a joined text. A merge with no conflict still has a merge Case, since `rule-default-mode` keeps a session from writing anything before a Case is ratified. The merge runs before the close because, once a sprint is closed, `guppi ledger` refuses each decision line but a `defer` until a new sprint page stands, as `estimate-sprint-close-next-session-opens-the-sprint` says. That Criterion stands, and the close then settles each Estimate that the merge set `pending`. The tests run again in the full test run of `/work` over the merged code, and CI runs on the pull request. The pull request follows the close. For the owner's sprint, the opening Case of the next sprint pushes the branch, opens the pull request and merges it, which Case 789 of this session sets. Another person runs `git push` and `gh pr create` after the close, and the owner reviews it by `/pr-review`.
>
> The vault query, run on the rules and entities, found no page that merges `main` into a branch. `rule-skill-sprint-open` is near: it merges the closed branch into `main`, and Case 789.1 changes it. `rule-spec-box` is near too: it brings a Spec branch up to the shared branch by a fast-forward, and stands. The rules that bear here are `rule-ratification`, `rule-default-mode`, `rule-vault-layout` and `rule-page-generation`. The tags `git`, `workflow`, `sprint` and `harness` fit. A Glob `vault/**/*merge-main*` printed nothing, so `rule-skill-merge-main` and `estimate-skill-merge-main-joins-a-conflicted-page` are free. The new rule takes `rule-plan-mode` as its `ref`, as `rule-skill-pr-review` of Case 789.2 does.
>
> A Grep `only writer|No file of` over `vault/wiki/`, with `log.md` and `brief.md` left out, printed `glossary.md`, `entity-glossary.md`, `rule-page-generation.md`, `rule-vault-layout.md` and `rule-documentation.md`. Over `.claude/` it printed `.claude/agents/librarian-guppi.md`. Each hit says that the script or the librarian is the only writer to `vault/wiki/`, or that no file of it is written by hand. The merge Case makes each of them false, so this Case names the exception in each of them. `rule-documentation` renders `.claude/agents/librarian-guppi.md`, and `entity-glossary` renders `glossary.md`. Case 786.1 also changes the Purpose of `rule-page-generation` and a row of `entity-glossary`, in other sentences: an exception for a `defer`, and the Types row. Each new text reads beside theirs with no contradiction. The `## Terms` table of `entity-glossary` was read whole. The pair of this Case changes only the Librarian row, and the pair of Case 786.1 changes only the Types row of the same table. The new Types row speaks of what a `defer` writes, and the new Librarian row speaks of who writes the joined text of a conflicted page, so the two rows fit. The Ratification row says that nothing in the vault or the code changes without a sign-off, which stays true, since the person signs each joined text in the merge Case. The Vault, Working files and Documentation rows say nothing of who writes a page, and stand. A change to a Purpose or a Render touches no Estimate (case 378.5). `estimate-vault-layout-holds` speaks of `layout` findings of lint, which stay true, and stands. `rule-skill-sprint-close` says that its closing Case holds no merge of the branch into `main`, which stays true. It also refuses a close in a session whose ledger holds another decision line, which is why the merge has a session of its own. A Grep `(ROOT|REPO)\s*/\s*"(vault|\.claude)"` over `tests/` printed `tests/test_case_schema.py`, `tests/test_generate.py`, `tests/test_orchestration.py` and `tests/test_schemas.py`. They read `case-schema.md`, `case-example.md`, `orchestration.md` and the files `schema.yaml`, which this Case does not change. The Case adds no code: `/merge-main` is instructions, checked by hand after the first real merge that leaves a conflicted page.
>
> Findings of `/pre-spec`. A merge Case may set several Estimates `pending`. Each `update` that sets one counts as a new Criterion, so two of them in one Case are two promises. The glossary row of an Estimate says its Criterion is the `when` and `then` of one Case. So the merge Case sets each such Estimate `pending` by a sub-case of its own, whose `when` and `then` are that Criterion as the page holds it. A path that `git checkout --theirs` takes stays unmerged until `git add`, so the merge Case runs `git add` on each conflicted path before its commit. Git keeps both sides of `log.md` and `tags.md` by a `merge=union` line in `.gitattributes`, the merge driver that git has built in. No rule page governs `.gitattributes`: a Grep `gitattributes` over `vault/wiki/` printed only `rule-shell-write-check.md`, which names the file and does not render it. The exception texts name these two files beside the joined text. `rule-default-mode` keeps a session from writing anything before a Case is ratified, and a `git fetch` writes into `.git/`. So before the merge Case `/merge-main` only reads. It takes the commit of `main` and the files `main` changed by `gh api`, and the files the branch changed by `git`. The fetch, the merge and all that needs them run in Work Mode. Without a merge before the Case, the merge Case cannot know which files git will leave in conflict. So it holds a joined text for each file that both sides changed, and Work Mode writes that text whether or not git left the file in conflict. Case 789.3 now names the tasks of a merge Case of `/merge-main` in the sixth condition of `rule-where-to-stop`. A refused `git` command there is a stop, and so is a file left in conflict that the merge Case does not settle. This Case leaves that condition and its Criterion to Case 789.3. Case 789.2 finds the merge Case by the message of its merge commit, `merge: main <hash> into <branch> — case N`, which this Case sets. That `/sprint-close` refuses while the branch does not hold `origin/main` is Case 791. Case 789.1 has `/sprint-open` write a `/merge-main` line before the close line.
>
> Not done. When `main` takes another pull request after the merge and before the pull request of this branch is merged, GitHub shows a conflict. The sprint is closed by then, so `/merge-main` cannot run again, and no rule covers that case yet. No code checks that the merge Case is the one Case of its session.

> **problem:**
> A sprint branch and `main` that changed one page conflict in git, and no rule says who settles the conflict, where, or how the settled text is signed. The rules on `vault/wiki/` leave no way to write a joined text: only the script writes a page.

> **recommend:**
> - **What should the close of a sprint send to the archive?**
>   - Recommended: (a) keep the close as it is: closed records go to the archive, and open debt crosses into `main` with the branch.
>   - Answer: agreed, (a).
> - **How are files written by a command settled at the merge?**
>   - Recommended: (a) write them again by their commands after the merge, and keep the lines of both sides in `log.md` and `tags.md`.
>   - Answer: agreed, (a).
> - **Who settles a conflict in a page that both branches changed, and where?**
>   - Recommended: (a) the contributor, before the pull request: they merge `main` into their branch and settle each conflicted page by a Case of their own session.
>   - Answer: agreed, (a), after the person asked how two branches meet step by step and read the answer.
> - **What happens to a check that passed on the branch but may no longer hold after the merge?**
>   - Recommended: (a) the tests run again, and the Case that settles a page sets `pending` each check of that page that speaks of the changed text.
>   - Answer: agreed, (a).
> - **Which text does a conflicted page take when the merge is committed?**
>   - Recommended: (a) the text of `main`; a Case of the branch's author then makes the branch's change again on top of it.
>   - Answer: not answered; the person questioned the approach. Replaced by "Should conflicts be settled in a separate merge mode, where the joined text is written straight into the page?"
> - **What carries out the steps of the merge, and how is that checked?**
>   - Recommended: (a) a new command, tested on a made-up repository.
>   - Answer: not answered. Replaced by "How is it checked that `/merge-main` works?"
> - **When are the settling Cases built, given that the pull request has to wait for them?**
>   - Recommended: (a) the next session builds them, and the pull request waits until then.
>   - Answer: not answered. Replaced by "Where does the merge mode run?"
> - **Should conflicts be settled in a separate merge mode, where the joined text is written straight into the page?**
>   - Recommended: (a) a separate merge mode: the person signs a joined text for each conflicted page, and the agent writes it into the page, a written exception to the rule that no file of `wiki/` is written by hand.
>   - Answer: agreed, (a).
> - **Where does the merge mode run?**
>   - Recommended: (a) a session of its own, started by a skill such as `/merge-main`, before the pull request; the opening Case of the next sprint no longer merges `main`.
>   - Answer: agreed, (a).
> - **What record does the merge mode leave of what the person signed?**
>   - Recommended: (a) one Case per merge, its joined texts written in its file, and the merge commit naming it.
>   - Answer: agreed, (a).
> - **How is it checked that `/merge-main` works?**
>   - Recommended: (a) a reading by hand after the first real `/merge-main` that hits a conflicted page; the skill is instructions only.
>   - Answer: agreed, (a).
> - **What does `/merge-main` do when nothing conflicts?**
>   - Recommended: (a) merge, commit and open the pull request, with no Case.
>   - Answer: agreed, (a). Replaced later by "Does a merge with no conflict still need a Case?"
> - **When does `/merge-main` run: before or after the close of the sprint?**
>   - Recommended: (a) before the close, in a session of its own, while the sprint is still open.
>   - Answer: agreed, (a).
> - **Does a merge with no conflict still need a Case?**
>   - Recommended: (a) yes, a short merge Case whose one decision line adds a History line to the live sprint page.
>   - Answer: agreed, (a).
> - **Who pushes the branch and opens the pull request after the close?**
>   - Recommended: (a) for the owner, the opening Case of the next sprint; for a contributor, `git push` and `gh pr create` by hand after the close.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the person agreed to each fix that `/pre-spec` proposed. The merge Case sets each Estimate `pending` in a form that the check accepts. It runs `git add` before its commit. Git keeps both sides of `log.md` and `tags.md`, and the exception texts name it. The `context` says why `git fetch` in Plan Mode stands, and how this Case fits Case 789.3. `/sprint-close` refuses while `main` is not taken in.
>   - Taken: in the Render of `rule-skill-merge-main`, each such Estimate is set `pending` by a sub-case of the merge Case whose `when` and `then` are its Criterion, and a task runs `git add` on each conflicted path. A task adds `merge=union` lines for `vault/wiki/log.md` and `vault/wiki/tags.md` to `.gitattributes`. The four exception texts and the `then` name the two files. The `context` was fixed. The refusal of `/sprint-close` is a new Case, 791, since it is a second promise.
> - **Change**
>   - Asked: the person agreed that `/merge-main` writes nothing into `.git` before the merge Case is ratified. The fetch, the merge and all that needs them run in Work Mode, Plan Mode only reads, and the `context` no longer points to Case 789.2 for this.
>   - Taken: before the Case, the Render reads the commit of `main` and the files that `main` changed by `gh api`, and the files that the branch changed by `git`. It runs no `git fetch` and no `git merge-tree`. The merge Case holds a joined text for each file that both sides changed. Its first tasks run `git fetch origin` and the merge. The `then`, the `given` and the `context` say the same.

> **given:**
> `rule-skill-merge-main`: the new rule whose Render is the skill `/merge-main`.
> **＋** `.claude/skills/merge-main/SKILL.md`: the file rendered from it.
> **＋** `estimate-skill-merge-main-joins-a-conflicted-page`: the new check of the merge.
> **＋** `raw/<date>/<hi HHMM>/merge.md` and `raw/<date>/<hi HHMM>/spec.md`: the output of `git` that `case-guppi` reads, and the Spec whose tasks Work Mode runs.
> **＋** `rule-page-generation`, `rule-vault-layout`, `rule-documentation` and `entity-glossary`, with `.claude/agents/librarian-guppi.md` and `vault/wiki/glossary.md` rendered from the last two: the texts that name the only writer to `vault/wiki/`.
> **＋** `vault/wiki/sprint.md`, `vault/wiki/backlog.md`, `vault/wiki/brief.md`, `vault/wiki/log.md`, `vault/wiki/tags.md`, `.gitattributes`, and `uv run guppi render`, `uv run guppi glossary`, `uv run guppi sprint` and `uv run guppi backlog`: the files written by a command or that only gain lines, the file that tells git to keep both sides of the latter, and the commands that write them.
> **＋** `entity-sprint-<id>`, `origin/main`, `gh api` and `git fetch origin`: the live sprint page that the merge Case updates, the `main` of GitHub that the branch takes in, the read of it before the Case, and the fetch of it in Work Mode.
> **＋** `.claude/skills/sprint-close/SKILL.md` and `.claude/skills/pr-review/SKILL.md`: the close that follows the merge, and the review of a pull request of another person.

> **when:**
> The person types `/merge-main` on `UserPromptSubmit` in Plan Mode, or the main agent calls it on `PreToolUse Skill`, in a session on the branch of an open sprint, `.claude/skills/merge-main/SKILL.md` rendered from `rule-skill-merge-main`; Work Mode then runs the tasks of `raw/<date>/<hi HHMM>/spec.md`.

> **then:**
> Writing nothing into the tree or into `.git` and running no `git fetch`, the main agent reads by `gh api` the commit of `main` on GitHub and the files that `main` changed since the last commit of `main` that the branch holds, and by `git` the files that the branch changed. It writes that output and the text on both sides of each file that both sides changed into `raw/<date>/<hi HHMM>/merge.md`, and dispatches `case-guppi` for the merge Case with that path.
> **＋** The merge Case is the one Case of the session; its tasks run `git fetch origin`, merge the commit of `main` that the session read into the branch, and commit the merge with a message that names the Case.
> **＋** Each conflicted file that a command writes takes the text of `main` and is written again by `uv run guppi render`, `uv run guppi glossary`, `uv run guppi sprint` or `uv run guppi backlog`, and `vault/wiki/brief.md` by the librarian; git keeps the lines of both sides of `vault/wiki/log.md` and `vault/wiki/tags.md` by their `merge=union` lines in `.gitattributes`.
> **＋** For each other file that both sides changed, the merge Case shows its text on the branch and on `main` and holds the joined text that the person signs or corrects; Work Mode writes that text into the file, and runs `git add` on each such path before the commit.
> **＋** Its decision lines update the live sprint page `entity-sprint-<id>` with only a `change` that names the merge, and each joined page under `vault/wiki/` with only a `change`; each Estimate whose Criterion speaks of a joined text is set `pending` by a sub-case of its own, whose `when` and `then` are that Criterion; the librarian writes no other text of a joined page.
> **＋** `rule-page-generation`, `rule-vault-layout`, `rule-documentation`, `entity-glossary`, `.claude/agents/librarian-guppi.md` and `vault/wiki/glossary.md` name that joined text, and the lines of `log.md` and `tags.md` that git joins, as what a merge of `main` writes into `vault/wiki/` besides the script.
> **＋** `.claude/skills/merge-main/SKILL.md` says that the pull request into `main` follows `/sprint-close` of `.claude/skills/sprint-close/SKILL.md`, and that another person runs `git push` and `gh pr create --base main` after the close, for the owner to review by `/pr-review` of `.claude/skills/pr-review/SKILL.md`.
> **－** With no file that both sides changed, the update of the sprint page is the one decision line of the merge Case.
> **－** When the branch is `main`, when the first heading of `vault/wiki/sprint.md` marks the last sprint closed, or when the branch already holds `origin/main`, no Case is built and nothing is merged; the main agent tells the person why.
> **－** The merge Case archives nothing: what goes to the archive is what `/sprint-close` of `.claude/skills/sprint-close/SKILL.md` moves.

> **tasks:**
> - [ ] create `rule-skill-merge-main`
>   - ref: `rule-plan-mode`
>   - kind: `Leaf`
>   - purpose: `Prevents a sprint branch from reaching main with a conflict its author did not settle, or with a joined text the person did not sign`
>   - enforcement: `render`
>   - governs: `.claude/skills/merge-main/SKILL.md`
>   - render_mode: `full`
>   - tags: `[git, workflow, sprint, harness]`
>   - sections.Purpose:
>     ```
>     Prevents a sprint branch from reaching `main` with a conflict its author did not settle, or with a joined text the person did not sign. Others clone the project and run a sprint on their own branch, and each branch carries its own copy of `vault/`. When a branch and `main` changed one page, git stops on a conflict, and the author of the branch settles it (case 790). The author runs `/merge-main` in a session of its own, after the work of the sprint and before `/sprint-close`, while the sprint page is live. The ledger then takes the lines of the merge Case, and the close settles each check that the merge Case set `pending`. Files that a command writes are written again rather than joined, and git keeps both sides of `log.md` and `tags.md`, which only gain lines. Every other conflicted file takes a joined text that the person signs in the merge Case and Work Mode writes. These are what a merge of `main` writes into `vault/wiki/` besides the script ([[rule-page-generation]], [[rule-vault-layout]]). The close archives what it archived before ([[rule-sprint-close]]). The pull request follows the close: for the owner's sprint the opening Case of the next sprint opens and merges it ([[rule-skill-sprint-open]]), and the owner reviews the pull request of another person by `/pr-review`.
>     ```
>   - sections.Render:
>     ````
>     <!-- rule-skill-merge-main -->
>     ---
>     name: merge-main
>     description: "Merge main into the branch of the open sprint as one merge Case, before the close of the sprint. Run it when the person types /merge-main."
>     ---
>
>     This session merges `origin/main` into the branch of the open sprint, after the work of the sprint and before `/sprint-close`, so that the pull request of the closed sprint reaches `main` with no conflict. The merge Case is the one Case of this session (case 790).
>
>     1. When `/hi` printed `main` under `Branch:`, or the first heading of `vault/wiki/sprint.md` marks the last sprint closed, build no Case and merge nothing: tell the person that `/merge-main` runs on the branch of an open sprint, before its close.
>     2. Until the merge Case is ratified, only read: write nothing into the tree or into `.git`, so run no `git fetch` (`rule-default-mode`). `gh api repos/{owner}/{repo}/commits/main --jq .sha` prints `<hash>`, the commit of `main` on GitHub. When `git merge-base --is-ancestor <hash> HEAD` exits 0, the branch already holds `main`: build no Case, and tell the person so.
>     3. `git merge-base HEAD origin/main` prints `<base>`, the last commit of `main` that the branch holds. `gh api repos/{owner}/{repo}/compare/<base>...<hash> --jq '.files[].filename'` names each file that `main` changed since, and `git diff --name-only <base> HEAD` each file that the branch changed. Write the output of these commands, as they printed it, into `raw/<date>/<hi HHMM>/merge.md`. Under it, for each file that both lists name and that the terms below do not settle by a command or by git, write its text on this branch by `git show HEAD:<path>` and on `main` by `gh api "repos/{owner}/{repo}/contents/<path>?ref=<hash>" -H "Accept: application/vnd.github.raw"`.
>     4. Dispatch `case-guppi` for the merge Case as `vault/wiki/orchestration.md` sets it, with the path of that file in the prompt and these terms:
>        - its first tasks run `git fetch origin` and `git merge --no-ff --no-commit <hash>`, so that Work Mode merges the commit this session read, and its last task runs `git commit -m "merge: main <hash> into <branch> — case N"`;
>        - each file that a command writes — a file that a live rule page names in `governs`, `vault/wiki/glossary.md`, `vault/wiki/sprint.md`, `vault/wiki/backlog.md` and `vault/wiki/brief.md` — takes the text of `main` by `git checkout --theirs -- <path>` when git leaves it in conflict; the tasks `uv run guppi render`, `uv run guppi glossary`, `uv run guppi sprint` and `uv run guppi backlog` write them again, and the librarian of the session writes `brief.md` again;
>        - `vault/wiki/log.md` and `vault/wiki/tags.md` are joined by git itself, by their `merge=union` lines in `.gitattributes`, which keep the lines of both sides; no task writes them;
>        - for each other file that both sides changed, a page or code, the Case shows its text on the branch and on `main` from `merge.md`, and holds one task that writes the joined text into the file, the text as a sub-point; the person signs or corrects that text, and Work Mode writes it into the file itself, whether or not git left the file in conflict;
>        - after the tasks that settle these files, one task runs `git add` on each of their paths, so that no path stands unmerged before the commit;
>        - its decision lines are an `update` of the live sprint page `entity-sprint-<id>` with only a `change` that names the merge and `<hash>`, and an `update` with only a `change` of each joined page under `vault/wiki/`;
>        - each Estimate whose Criterion speaks of a joined text is set `pending` by a sub-case of its own: its `when` and `then` are that Criterion as the page holds it, and its one decision line is an `update` of the Estimate with `set: {status: pending}`, so that each sub-case holds one promise;
>        - with no file that both sides changed, the `update` of the sprint page is its one decision line;
>        - the merge Case archives nothing: what goes to the archive is what `/sprint-close` moves.
>     5. The person ratifies the merge Case as any other. Work Mode runs its tasks, and the full test run of `/work` runs over the merged code. The librarian writes the Decision page, the History lines and the statuses set `pending`, and no other text of a joined page. The joined texts of the conflicted pages, and the lines of `log.md` and `tags.md` that git joins, are what a merge of `main` writes into `vault/wiki/` besides the script.
>     6. The pull request into `main` follows `/sprint-close`, so that it holds the whole closed sprint. For the owner's sprint, the opening Case of the next sprint opens and merges it, as `.claude/skills/sprint-open/SKILL.md` sets it. Another person runs `git push` and `gh pr create --base main` after the close, and the owner reviews it by `/pr-review`.
>     <!-- /rule-skill-merge-main -->
>     ````
> - [ ] `uv run guppi render`: `.claude/skills/merge-main/SKILL.md`
> - [ ] create `estimate-skill-merge-main-joins-a-conflicted-page`
>   - ref: `rule-skill-merge-main`
>   - kind: `QA`
>   - purpose: `Whether /merge-main merges main into the branch of an open sprint as one merge Case, writes again the files a command writes, keeps both sides of the files that only gain lines, and writes the joined text the person signed into each other conflicted file`
>   - method: `by hand, after the first /merge-main whose merge of main leaves a conflicted page: its merge.md, the merge Case in its case file, its decision lines, the merge commit, the joined pages and the Render of rule-skill-merge-main read against the Criterion`
>   - tags: `[git, workflow, sprint]`
> - [ ] update `rule-page-generation`
>   - old: `` The script is the only writer to `wiki/`. ``
>   - new: `` The script is the only writer to `wiki/`, but for what a merge of `main` by `/merge-main` writes: the joined text of a page that both a branch and `main` changed, which the merge Case signs and Work Mode writes, the script then writing the History line and the status that the Case sets, and the lines of both sides of `log.md` and `tags.md`, which git joins by their `merge=union` lines in `.gitattributes` (case 790). ``
>   - change: `a merge of main by /merge-main writes the joined text of a conflicted page and git joins log.md and tags.md (case 790)`
> - [ ] update `rule-vault-layout`
>   - old: `` No file of `wiki/` is written by hand. ``
>   - new: `` No file of `wiki/` is written by hand, but for what a merge of `main` by `/merge-main` writes: the joined text of a page that both a branch and `main` changed, which the merge Case signs and Work Mode writes into the page, and the lines of both sides of `log.md` and `tags.md`, which git joins by their `merge=union` lines in `.gitattributes` (case 790). ``
>   - change: `a merge of main by /merge-main writes the joined text of a conflicted page and git joins log.md and tags.md (case 790)`
> - [ ] update `rule-documentation`
>   - old: `` You are the only writer to `vault/wiki/`, and you write only through the scripts named below. ``
>   - new: `` You are the only writer to `vault/wiki/` but for what a merge of `main` by `/merge-main` writes — the joined text of a conflicted page, written in Work Mode, and the lines of `log.md` and `tags.md` that git joins (case 790) — and you write only through the scripts named below. ``
>   - change: `the librarian is the only writer to vault/wiki/ but for what a merge of main by /merge-main writes (case 790)`
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] update `entity-glossary`
>   - old: `` Clean context; the only writer to `wiki/`; ``
>   - new: `` Clean context; the only writer to `wiki/` but for what a merge of `main` by `/merge-main` writes: the joined text of a conflicted page, and the lines of `log.md` and `tags.md` that git joins (case 790); ``
>   - change: `Librarian: the only writer to wiki/ but for what a merge of main by /merge-main writes (case 790)`
> - [ ] `uv run guppi glossary`
> - [ ] `.gitattributes`: the lines `vault/wiki/log.md merge=union` and `vault/wiki/tags.md merge=union` after the line `* text=auto eol=lf`, under one comment that names case 790: git keeps the lines of both sides of the two files at a merge.
> - [ ] read `estimate-skill-merge-main-joins-a-conflicted-page`

> **ratification:**
> ```
> - decision[case 790][create][rule-skill-merge-main]{ref:rule-plan-mode}{tags:git,workflow,sprint,harness}
> - decision[case 790][create][estimate-skill-merge-main-joins-a-conflicted-page]{ref:rule-skill-merge-main}{tags:git,workflow,sprint}
> - decision[case 790][update][rule-page-generation]{ref:rule-page-generation}
> - decision[case 790][update][rule-vault-layout]{ref:rule-vault-layout}
> - decision[case 790][update][rule-documentation]{ref:rule-documentation}
> - decision[case 790][update][entity-glossary]{ref:entity-glossary}
> ```
