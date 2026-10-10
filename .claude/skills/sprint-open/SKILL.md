---
name: sprint-open
description: "Open the next sprint. Run it when the hook on /hi says that no sprint is open, or when the person types /sprint-open."
---

No sprint is open: the first heading of `vault/wiki/sprint.md` marks the last sprint closed. This session opens the next one. The ledger hook refuses each decision line but a `defer` until a `create` of a page `entity-sprint-<id>` stands, so the opening Case is the first Case the session ratifies.

1. Assemble no Frontier yet: the opening Case comes first, and no other item of the session is taken up before the person ratifies it (case 769.1).
2. Dispatch `case-guppi` at once for the line `open the next sprint` of the brief, as `vault/wiki/orchestration.md` sets it, and write into the prompt of the call that the opening Case asks the person, in its rounds:
   - the id of the sprint, which names the page `entity-sprint-<id>`;
   - its goal in one sentence, the `purpose` and the `## Purpose` of the page;
   - its Definition of done, one Estimate per condition, which the page lists in `estimates`;
   - the first milestone and its items, under `## Milestones`;
   - whether to take any item of `vault/wiki/backlog.md` into the sprint: the Case says how many items the file holds, and goes through no item the person does not name.
3. Write into the same prompt that the opening Case writes, as the last item of the last milestone of the page, the line ``- the close of `<id>` — `/sprint-close`, a session of its own``, so that the session that closes the sprint starts `/sprint-close` from it.
4. Write into the same prompt the branch that `/hi` printed under `Branch:`. When it is not `main`, the closed sprint ran on it, and the opening Case holds as its first task lines `git switch main`, `git merge --ff-only <branch>`, `git switch -c <id>` and `git branch -d <branch>`, `<id>` the id of the new sprint. The Spec holds the opening Case first, so Work Mode runs them before any other task: `main` takes the work of the closed sprint by a fast-forward, and the rest of Work Mode runs on the branch `<id>`. A refusal of the merge or of the deletion is a stop on the sixth condition of `vault/wiki/where-to-stop.md`. When the branch is `main`, the opening Case holds no merge, branch or deletion task: Work Mode stops on `main`, and goes on after the person makes the branch `<id>` and moves to it. The opening Case puts no question on the merge or the branch to the person (case 775.1).
5. The skill decides none of the answers: `case-guppi` puts each to the person, and the person ratifies the opening Case as any other. Before the reply that acknowledges it, assemble and write the Frontier as `/hi` sets it, the items of the first milestone of the opening Case among its Cases; that reply shows it, as `vault/wiki/orchestration.md` sets that reply (case 769.4).
