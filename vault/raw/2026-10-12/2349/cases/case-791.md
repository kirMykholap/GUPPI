## Case 791 — The close of a sprint waits until its branch holds main

> **context:**
> By Case 790, the author of a sprint branch takes in `main` with `/merge-main`, in a session of its own, before `/sprint-close`. The merge must come first. After the close no sprint page is live, and `guppi ledger` refuses each decision line but a `defer` until a new sprint page stands. So a branch closed before its merge cannot record a merge Case any more. Nothing today checks the order. `/sprint-close`, the Render of `rule-skill-sprint-close`, starts the close in any session whose ledger holds no decision line but a `defer`. `/pre-spec` found this gap in Case 790. The person chose that `/sprint-close` refuses while the branch does not hold `origin/main`, and tells the person to run `/merge-main` first. This is a second promise beside the merge itself, so it is a Case of its own beside Case 790, which stays as it is. Case 789.1 adds the other half: `/sprint-open` writes a `/merge-main` line before the close line of the sprint.
>
> Step 1 of the Render of `rule-skill-sprint-close` already stops the skill in a session whose ledger holds another decision line. The new check comes before it and stops the skill the same way: it closes the close line as put off, tells the person why, and goes no further. The check writes nothing into `.git`, since the skill starts in Plan Mode and `rule-default-mode` keeps a session from writing anything before a Case is ratified. So it runs no `git fetch`. `gh api repos/{owner}/{repo}/commits/main --jq .sha` reads the commit of `main` on GitHub, and `git merge-base --is-ancestor <hash> HEAD` asks whether the branch holds it. Any exit but 0 means that the branch does not hold `main`, an unknown commit included. A failure of `gh api`, such as a missing remote, is shown to the person as printed, and the skill stops too. The Criterion of `estimate-skill-sprint-close-leads-the-closing-session` speaks of what the skill does when it starts, and its line that opens with "Otherwise" would be false on a branch that does not hold `main`, so it is replaced whole. Its other lines are kept word for word. Its `purpose` names the refusals of the skill, and its `method` names the Retro of the session of case 775, so both are set anew in the same `update`. The other Estimate of the rule, `estimate-skill-sprint-close-migration-merged-into-main`, records the one merge of `migration`, a reading already taken, and stands. The Purpose of `rule-skill-sprint-close` says that the skill keeps the close from mixing with other decisions, which stays true. The sentences of `vault/wiki/orchestration.md` on `/sprint-close` name the skill and the moment of a short-form defer, which stay true. No other Case of this session changes `rule-skill-sprint-close` or its Estimates: a Grep `estimate-skill-sprint-close|rule-skill-sprint-close` over `vault/raw/2026-10-12/2349/cases/` printed `case-789.md`, `case-790.md` and `case-791.md`. The last is this Case's own file, and the other two only name the rule.

> **problem:**
> A sprint can be closed before its branch takes in `main`. After the close, the merge Case of `/merge-main` can no longer be recorded, so the pull request of the closed sprint can reach `main` with conflicts that nobody settled.

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
>   - Recommended: (a) a separate merge mode: the person signs a joined text for each conflicted page, and the agent writes it into the page.
>   - Answer: agreed, (a).
> - **Where does the merge mode run?**
>   - Recommended: (a) a session of its own, started by a skill such as `/merge-main`, before the pull request.
>   - Answer: agreed, (a).
> - **What record does the merge mode leave of what the person signed?**
>   - Recommended: (a) one Case per merge, its joined texts written in its file, and the merge commit naming it.
>   - Answer: agreed, (a).
> - **How is it checked that `/merge-main` works?**
>   - Recommended: (a) a reading by hand after the first real `/merge-main` that hits a conflicted page.
>   - Answer: agreed, (a).
> - **What does `/merge-main` do when nothing conflicts?**
>   - Recommended: (a) merge, commit and open the pull request, with no Case.
>   - Answer: agreed, (a). Replaced later by "Does a merge with no conflict still need a Case?"
> - **When does `/merge-main` run: before or after the close of the sprint?**
>   - Recommended: (a) before the close, in a session of its own, while the sprint is still open; this is the order that this Case makes `/sprint-close` keep.
>   - Answer: agreed, (a).
> - **Does a merge with no conflict still need a Case?**
>   - Recommended: (a) yes, a short merge Case whose one decision line adds a History line to the live sprint page.
>   - Answer: agreed, (a).
> - **Who pushes the branch and opens the pull request after the close?**
>   - Recommended: (a) for the owner, the opening Case of the next sprint; for a contributor, `git push` and `gh pr create` by hand after the close.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the person agreed with the finding of `/pre-spec`: `/sprint-close` refuses while `origin/main` is not in the branch, starting with `git merge-base --is-ancestor origin/main HEAD`, and tells the person to run `/merge-main` first.
>   - Taken: step 1 of the Render of `rule-skill-sprint-close` runs that check first and stops the skill on it, and the Criterion of `estimate-skill-sprint-close-leads-the-closing-session` is replaced whole with the refusal added.
> - **Change**
>   - Asked: the person agreed that nothing is written into `.git` before a Case is ratified, as `rule-default-mode` sets it.
>   - Taken: the check runs no `git fetch`. It reads the commit of `main` on GitHub by `gh api` and asks `git merge-base --is-ancestor` whether the branch holds that commit. Any exit but 0 is a refusal.

> **given:**
> `rule-skill-sprint-close`: the skill whose Render gets the check at its start.
> **＋** `.claude/skills/sprint-close/SKILL.md`: the file rendered from it.
> **＋** `estimate-skill-sprint-close-leads-the-closing-session`: its Criterion is replaced whole.
> **＋** `main` on GitHub, `gh api repos/{owner}/{repo}/commits/main --jq .sha`, `git merge-base --is-ancestor <hash> HEAD` and `.claude/skills/merge-main/SKILL.md`: the `main` that the branch must hold, the commands that check it, and the skill that takes it in, by Case 790.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`, `frontier.md` and the close line `uv run guppi sprint-close --sprint <id> --apply`: the session's ledger and Frontier, and the line of the closing Case.
> **＋** `vault/wiki/orchestration.md` and `.claude/agents/librarian-guppi.md`: the steps of a session and the librarian that runs the close line.
> **＋** `entity-sprint-migration`: the sprint closed before, whose close line the Criterion reads.
> **＋** `.claude/skills/sprint-open/SKILL.md`: the opening of the next sprint.

> **when:**
> The person takes up on the Frontier the line of the sprint that names `/sprint-close`, and the main agent starts the skill `/sprint-close` of `.claude/skills/sprint-close/SKILL.md`, rendered from `rule-skill-sprint-close`, on `PreToolUse Skill`, or the person types `/sprint-close` on `UserPromptSubmit`.

> **then:**
> Writing nothing into `.git`, the main agent first runs `gh api repos/{owner}/{repo}/commits/main --jq .sha`, which prints `<hash>`, and `git merge-base --is-ancestor <hash> HEAD`. When the second exits other than 0, it closes the close line `[-] … · sprint · defer`, tells the person to run `/merge-main` of `.claude/skills/merge-main/SKILL.md` in a session of its own first, and the skill stops. When `gh api` fails, it shows the output and the skill stops the same way.
> **＋** When the session's ledger holds a decision line other than a `defer`, the main agent closes the close line `[-] … · sprint · defer`, tells the person that the close needs a session of its own, and the skill stops.
> **＋** Otherwise the main agent closes each other open line under `## Cases` of `frontier.md` by the closer of its source put off, the person's pick of the close line standing as the words that ratify each short-form defer, leaves the lines under `## Work` and `## Ask` open, and shows the Frontier.
> **＋** It sorts the Estimates that stand `pending` or `failed` into groups by the kind of moment their `method` names and dispatches `case-guppi` for the closing Case with the groups in the prompt, and the closing Case names the groups in its `context`, holds one `by hand` task per moment that Work Mode sets up and one `read` line per Estimate, and holds the task line `uv run guppi sprint-close --sprint <id> --apply` with the person's choice for each Estimate still unread.
> **＋** Work Mode takes each reading whose moment came and neither runs nor ticks the close line; the librarian runs it, as `.claude/agents/librarian-guppi.md` sets it.
> **＋** `vault/wiki/orchestration.md` holds no paragraph on the closing session, names the two skills in one sentence, and counts the start of `/sprint-close` among the moments of a short-form defer.
> **＋** The close line of `entity-sprint-migration` reads ``- the close of `migration` — `/sprint-close`, a session of its own``, and its `## Backlog` holds no line on the merge.
> **－** Besides the closing Case, the session ratifies only the Cases that prepare its readings.
> **－** The closing Case holds no task line for the merge of the sprint's branch into `main`: the opening Case of the next sprint holds the merge, as `.claude/skills/sprint-open/SKILL.md` sets it.

> **tasks:**
> - [ ] update `rule-skill-sprint-close`
>   - old: `` 1. When the session's `raw/<date>/<hi HHMM>/ledger.md` holds a decision line other than a `defer`, this session cannot close the sprint. ``
>   - new: `` 1. Write nothing into `.git`, so run no `git fetch`: `gh api repos/{owner}/{repo}/commits/main --jq .sha` prints `<hash>`, the commit of `main` on GitHub. When `git merge-base --is-ancestor <hash> HEAD` exits other than 0, the branch does not hold `main`, and this session cannot close the sprint: close the line of the close in `frontier.md` as `[-] … · sprint · defer`, tell the person to run `/merge-main` in a session of its own first, and stop the skill here (case 791). When `gh api` fails, show its output, close the line the same way and stop the skill here. When the session's `raw/<date>/<hi HHMM>/ledger.md` holds a decision line other than a `defer`, this session cannot close the sprint. ``
>   - change: `/sprint-close refuses while the branch does not hold origin/main, and asks for /merge-main first (case 791)`
> - [ ] `uv run guppi render`: `.claude/skills/sprint-close/SKILL.md`
> - [ ] update `estimate-skill-sprint-close-leads-the-closing-session`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether /sprint-close refuses on a branch that does not hold origin/main and in a session that ratified another Case, puts off the other Cases lines, sorts the readings and has the closing Case built with the close line, while orchestration.md no longer holds the steps of the closing session"
>     method: "by hand, at the Retro of the session of case 791, the new Render of rule-skill-sprint-close in its spec.md, vault/wiki/orchestration.md and entity-sprint-migration under vault/archive/migration/ read against the Criterion"
>     ```
>   - change: `the Criterion replaced whole — /sprint-close refuses while the branch does not hold origin/main`
> - [ ] read `estimate-skill-sprint-close-leads-the-closing-session`

> **ratification:**
> ```
> - decision[case 791][update][rule-skill-sprint-close]{ref:rule-skill-sprint-close}
> - decision[case 791][update][estimate-skill-sprint-close-leads-the-closing-session]{ref:rule-skill-sprint-close}
> ```
