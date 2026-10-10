## Case 753 — The finished close rule leaves the closing milestone

> **context:**
> Slice 5 of `entity-sprint-migration`, the last milestone of the sprint, holds two items: `rule-sprint-close` and the close line of `migration`. `guppi sprint` ticks an item when each page it names stands `built`, `passed` or `archived`. The cascade sets a rule `built` only when each of its live Estimates stands `passed`, and nothing archives `rule-sprint-close` before the close. Six Estimates of `rule-sprint-close` stand `passed`. Three stand `pending`: `estimate-sprint-close-runs-in-the-librarian-run`, `estimate-sprint-close-takes-the-readings-in-groups` and `estimate-sprint-close-next-session-opens-the-sprint`. Each one waits for the closing session or the session after it. So the item cannot be ticked before the close, and each `/hi` takes it again as a Frontier line from the current milestone (`rule-skill-hi`). The person wants it settled in this session, so that the next session closes the sprint by `/sprint-close` with the close line as the only sprint item. This Case removes the item from Slice 5. `rule-sprint-close` stays `draft`. The closing Case settles its three pending Estimates, by a reading, `--carry` or `--archive-unread`, as `rule-skill-sprint-close` sets it. The close line stays the last item of the last milestone, as `rule-skill-sprint-open` writes it. A Grep for `Slice 5` over `vault/wiki/`, `guppi/`, `tests/` and `.claude/` printed `vault/wiki/brief.md`, `vault/wiki/backlog.md`, `vault/wiki/sprint.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-morph.md`, `vault/wiki/entities/entity-sprint-migration.md`, `tests/test_sprint.py`, `vault/wiki/estimates/estimate-hi-writes-frontier.md` and `vault/wiki/estimates/estimate-sprint-items-move-only-by-a-case.md`. `brief.md` and `log.md` were not read. `sprint.md` is rendered from the sprint page by the task line below. `backlog.md` and `rule-morph.md` name Slice 5 in the purpose of `rule-morph` as an old place of that item, which this Case does not touch. `tests/test_sprint.py` builds its own sprint page under a temporary folder and reads no live file. The Results of the two Estimates record past readings, and a record stands. The Criterion of `estimate-sprint-items-move-only-by-a-case` says that a line of the sprint page moves only through an entry of a ratified Case, and this Case is such an entry. `estimate-sprint-renders-the-backlog` checks this change: its Criterion says that `guppi sprint` renders the current milestone whole from the page, and that a line with no wikilink keeps its milestone open. That Criterion speaks of the render in general and not of this item, so it stands. No Estimate of `entity-sprint-migration` speaks of the milestones, so none is touched. One of them limits the choice that this Case leaves to the closing Case: `estimate-sprint-migration-lint-clean`. Its Criterion forgives an `unread` line in `make lint` before the closing librarian's run only on an Estimate of the sprint page, or on an Estimate whose `method` names a moment at or after that run and that the close line names by `--carry`. `estimate-sprint-close-runs-in-the-librarian-run` and `estimate-sprint-close-next-session-opens-the-sprint` have such a moment. If the closing Case archives either of them unread, that Criterion is not met. The choice stays with the closing Case, as the person decided, and that Criterion stands as the limit the closing Case reads.

> **problem:**
> The milestone item `rule-sprint-close` cannot be ticked before the sprint closes, because its last three Estimates can only be read at the close or after it. So it comes back at every `/hi`, and the closing session must put it off again.

> **recommend:**
> - **What closing C1 does to the sprint page**
>   - Recommended: (a) take the item out of Slice 5; the rule's content is finished, and the closing Case handles its waiting checks like any other unread check.
>   - Answer: agreed with the recommendation, (a).
> - **Who decides what happens to the three waiting checks**
>   - Recommended: (a) leave it to the closing Case, which sorts the checks into groups and picks carry or archive-unread for each one.
>   - Answer: agreed with the recommendation, (a).

> **given:**
> `entity-sprint-migration`: the sprint page whose Slice 5 loses the item.
> **＋** `vault/wiki/sprint.md`: the file `guppi sprint` renders from the sprint page.
> **＋** `rule-sprint-close`: the rule the removed item names.
> **＋** `/hi`: the skill that opens the next session and writes its Frontier.
> **＋** `rule-skill-hi`: takes the items of the current milestone as Frontier lines.
> **＋** `rule-skill-sprint-close`: the closing session settles each pending Estimate.

> **when:**
> The librarian applies the update of `entity-sprint-migration` and runs `uv run guppi sprint`; the next session opens with `/hi` and reads `vault/wiki/sprint.md`.

> **then:**
> Slice 5 of `entity-sprint-migration` and of `vault/wiki/sprint.md` holds the close line of `migration` alone.
> **＋** The `/hi` of the next session takes the close line as the only Frontier line from the sprint, as `rule-skill-hi` sets it.
> **－** `rule-sprint-close` keeps its status, and each of its Estimates keeps its status until the closing session settles it, as `rule-skill-sprint-close` sets it.

> **tasks:**
> - [ ] update `entity-sprint-migration`
>   - old: `` - [[rule-sprint-close]] — what the close of a sprint moves to the archive and what it keeps (cases 612.1, 627) - the close of `migration` ``
>   - new: `` - the close of `migration` ``
>   - change: `Slice 5 holds the close line alone: rule-sprint-close left the milestone, its pending Estimates settled by the closing Case (case 753)`
> - [ ] `uv run guppi sprint`

> **ratification:**
> ```
> - decision[case 753][update][entity-sprint-migration]{ref:entity-sprint-migration}
> ```
