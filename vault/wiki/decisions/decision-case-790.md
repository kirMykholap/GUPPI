---
type: decision
case: "790"
status: current
create: ["[[rule-skill-merge-main]]", "[[estimate-skill-merge-main-joins-a-conflicted-page]]"]
update: ["[[rule-page-generation]]", "[[rule-vault-layout]]", "[[rule-documentation]]", "[[entity-glossary]]"]
origin: raw/2026-10-12/2349/ledger.md#case-790
sprint: plugin
created: 2026-10-12
tags: [git, workflow, sprint, harness, ledger, session, librarian, render]
---

## Problem

A sprint branch and `main` that changed one page conflict in git, and no rule says who settles the conflict, where, or how the settled text is signed. The rules on `vault/wiki/` leave no way to write a joined text: only the script writes a page.

## Recommend

- **What should the close of a sprint send to the archive?**
  - Recommended: (a) keep the close as it is: closed records go to the archive, and open debt crosses into `main` with the branch.
  - Answer: agreed, (a).
- **How are files written by a command settled at the merge?**
  - Recommended: (a) write them again by their commands after the merge, and keep the lines of both sides in `log.md` and `tags.md`.
  - Answer: agreed, (a).
- **Who settles a conflict in a page that both branches changed, and where?**
  - Recommended: (a) the contributor, before the pull request: they merge `main` into their branch and settle each conflicted page by a Case of their own session.
  - Answer: agreed, (a), after the person asked how two branches meet step by step and read the answer.
- **What happens to a check that passed on the branch but may no longer hold after the merge?**
  - Recommended: (a) the tests run again, and the Case that settles a page sets `pending` each check of that page that speaks of the changed text.
  - Answer: agreed, (a).
- **Which text does a conflicted page take when the merge is committed?**
  - Recommended: (a) the text of `main`; a Case of the branch's author then makes the branch's change again on top of it.
  - Answer: not answered; the person questioned the approach. Replaced by "Should conflicts be settled in a separate merge mode, where the joined text is written straight into the page?"
- **What carries out the steps of the merge, and how is that checked?**
  - Recommended: (a) a new command, tested on a made-up repository.
  - Answer: not answered. Replaced by "How is it checked that `/merge-main` works?"
- **When are the settling Cases built, given that the pull request has to wait for them?**
  - Recommended: (a) the next session builds them, and the pull request waits until then.
  - Answer: not answered. Replaced by "Where does the merge mode run?"
- **Should conflicts be settled in a separate merge mode, where the joined text is written straight into the page?**
  - Recommended: (a) a separate merge mode: the person signs a joined text for each conflicted page, and the agent writes it into the page, a written exception to the rule that no file of `wiki/` is written by hand.
  - Answer: agreed, (a).
- **Where does the merge mode run?**
  - Recommended: (a) a session of its own, started by a skill such as `/merge-main`, before the pull request; the opening Case of the next sprint no longer merges `main`.
  - Answer: agreed, (a).
- **What record does the merge mode leave of what the person signed?**
  - Recommended: (a) one Case per merge, its joined texts written in its file, and the merge commit naming it.
  - Answer: agreed, (a).
- **How is it checked that `/merge-main` works?**
  - Recommended: (a) a reading by hand after the first real `/merge-main` that hits a conflicted page; the skill is instructions only.
  - Answer: agreed, (a).
- **What does `/merge-main` do when nothing conflicts?**
  - Recommended: (a) merge, commit and open the pull request, with no Case.
  - Answer: agreed, (a). Replaced later by "Does a merge with no conflict still need a Case?"
- **When does `/merge-main` run: before or after the close of the sprint?**
  - Recommended: (a) before the close, in a session of its own, while the sprint is still open.
  - Answer: agreed, (a).
- **Does a merge with no conflict still need a Case?**
  - Recommended: (a) yes, a short merge Case whose one decision line adds a History line to the live sprint page.
  - Answer: agreed, (a).
- **Who pushes the branch and opens the pull request after the close?**
  - Recommended: (a) for the owner, the opening Case of the next sprint; for a contributor, `git push` and `gh pr create` by hand after the close.
  - Answer: agreed, (a).
- **Change**
  - Asked: the person agreed to each fix that `/pre-spec` proposed. The merge Case sets each Estimate `pending` in a form that the check accepts. It runs `git add` before its commit. Git keeps both sides of `log.md` and `tags.md`, and the exception texts name it. The `context` says why `git fetch` in Plan Mode stands, and how this Case fits Case 789.3. `/sprint-close` refuses while `main` is not taken in.
  - Taken: in the Render of `rule-skill-merge-main`, each such Estimate is set `pending` by a sub-case of the merge Case whose `when` and `then` are its Criterion, and a task runs `git add` on each conflicted path. A task adds `merge=union` lines for `vault/wiki/log.md` and `vault/wiki/tags.md` to `.gitattributes`. The four exception texts and the `then` name the two files. The `context` was fixed. The refusal of `/sprint-close` is a new Case, 791, since it is a second promise.
- **Change**
  - Asked: the person agreed that `/merge-main` writes nothing into `.git` before the merge Case is ratified. The fetch, the merge and all that needs them run in Work Mode, Plan Mode only reads, and the `context` no longer points to Case 789.2 for this.
  - Taken: before the Case, the Render reads the commit of `main` and the files that `main` changed by `gh api`, and the files that the branch changed by `git`. It runs no `git fetch` and no `git merge-tree`. The merge Case holds a joined text for each file that both sides changed. Its first tasks run `git fetch origin` and the merge. The `then`, the `given` and the `context` say the same.

## History

- 2026-10-13 created · raw/2026-10-12/2349/ledger.md#case-790
