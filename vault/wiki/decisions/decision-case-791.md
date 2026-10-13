---
type: decision
case: "791"
status: current
update: ["[[rule-skill-sprint-close]]", "[[estimate-skill-sprint-close-leads-the-closing-session]]"]
origin: raw/2026-10-12/2349/ledger.md#case-791
sprint: plugin
created: 2026-10-12
tags: [sprint, workflow, harness]
---

## Problem

A sprint can be closed before its branch takes in `main`. After the close, the merge Case of `/merge-main` can no longer be recorded, so the pull request of the closed sprint can reach `main` with conflicts that nobody settled.

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
  - Recommended: (a) a separate merge mode: the person signs a joined text for each conflicted page, and the agent writes it into the page.
  - Answer: agreed, (a).
- **Where does the merge mode run?**
  - Recommended: (a) a session of its own, started by a skill such as `/merge-main`, before the pull request.
  - Answer: agreed, (a).
- **What record does the merge mode leave of what the person signed?**
  - Recommended: (a) one Case per merge, its joined texts written in its file, and the merge commit naming it.
  - Answer: agreed, (a).
- **How is it checked that `/merge-main` works?**
  - Recommended: (a) a reading by hand after the first real `/merge-main` that hits a conflicted page.
  - Answer: agreed, (a).
- **What does `/merge-main` do when nothing conflicts?**
  - Recommended: (a) merge, commit and open the pull request, with no Case.
  - Answer: agreed, (a). Replaced later by "Does a merge with no conflict still need a Case?"
- **When does `/merge-main` run: before or after the close of the sprint?**
  - Recommended: (a) before the close, in a session of its own, while the sprint is still open; this is the order that this Case makes `/sprint-close` keep.
  - Answer: agreed, (a).
- **Does a merge with no conflict still need a Case?**
  - Recommended: (a) yes, a short merge Case whose one decision line adds a History line to the live sprint page.
  - Answer: agreed, (a).
- **Who pushes the branch and opens the pull request after the close?**
  - Recommended: (a) for the owner, the opening Case of the next sprint; for a contributor, `git push` and `gh pr create` by hand after the close.
  - Answer: agreed, (a).
- **Change**
  - Asked: the person agreed with the finding of `/pre-spec`: `/sprint-close` refuses while `origin/main` is not in the branch, starting with `git merge-base --is-ancestor origin/main HEAD`, and tells the person to run `/merge-main` first.
  - Taken: step 1 of the Render of `rule-skill-sprint-close` runs that check first and stops the skill on it, and the Criterion of `estimate-skill-sprint-close-leads-the-closing-session` is replaced whole with the refusal added.
- **Change**
  - Asked: the person agreed that nothing is written into `.git` before a Case is ratified, as `rule-default-mode` sets it.
  - Taken: the check runs no `git fetch`. It reads the commit of `main` on GitHub by `gh api` and asks `git merge-base --is-ancestor` whether the branch holds that commit. Any exit but 0 is a refusal.

## History

- 2026-10-13 created · raw/2026-10-12/2349/ledger.md#case-791
