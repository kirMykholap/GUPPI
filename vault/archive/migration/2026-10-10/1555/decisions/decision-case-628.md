---
type: decision
case: "628"
status: archived
children: ["[[decision-case-628.1]]", "[[decision-case-628.2]]", "[[decision-case-628.3]]", "[[decision-case-628.4]]", "[[decision-case-628.5]]", "[[decision-case-628.6]]", "[[decision-case-628.7]]", "[[decision-case-628.8]]", "[[decision-case-628.9]]", "[[decision-case-628.10]]", "[[decision-case-628.11]]", "[[decision-case-628.12]]"]
origin: raw/2026-10-04/1439/ledger.md#case-628
sprint: migration
created: 2026-10-04
tags: [sprint, workflow, librarian, ledger, session, harness, render, hooks, git, tests]
---

## Problem

Nothing says where the close of a sprint runs, who calls it, or how the next sprint opens. Run in the wrong place, the close refuses the readings of its own session. Between the close and a new sprint page, the vault has no live sprint, and the pages written then would belong to a closed sprint. The closed sprint page also takes its Backlog into the archive, and the checks of migration wait for a moment that the close itself removes. The question is where the close runs, how its readings are taken first, how the next session opens the next sprint before anything else, and where the Backlog and the checks of the closed sprint go.

## Recommend

- **Which step of a session runs the close with `--apply`?**
  - Recommended: (a) the librarian's run, right after `guppi generate`, from a task line of the closing session's Spec that holds the command with the person's choices.
  - Answer: agreed.
- **Does the close get a session of its own?**
  - Recommended: (a) a session of its own, whose Plan Mode holds only the closing Case and the Cases that prepare its readings.
  - Answer: agreed.
- **How does the next sprint start?**
  - Recommended: (a) the closing Case creates the next sprint page in the same session.
  - Answer: (b): a Case of the next session creates it.
- **How does the closing session take the pending readings before the close?**
  - Recommended: (a) the rule of the close sets the grouping, with no code: the pending Estimates sorted by the kind of moment their method names, each moment set up in Work Mode, only the rest carried or archived unread.
  - Answer: agreed.
- **Which sprint do the pages written before the next sprint opens belong to?**
  - Recommended: (b) the new sprint's id, taken from the `create` of `entity-sprint-<id>` in the same unit.
  - Answer: agreed.
- **What do `guppi sprint` and `make lint` do between the close and the opening of the next sprint?**
  - Recommended: (a) it stays an error, as the person's answer reads: the brief flags it and the next session's Baseline holds the red.
  - Answer: (a). The person had first said that one session closes the sprint and that all of its decisions belong to that sprint. After that, every test runs, and a check may report that no sprint is open, which is normal. The next session must start by opening a new sprint.
- **What happens to the check of migration that says the close is the sprint page set `built`?**
  - Recommended: (a) replace its Criterion whole now: the line on `built` gives way to the librarian's run of the command, the lines on `make test` and the merge kept.
  - Answer: agreed; later replaced by the person's answer at `/pre-spec` on when the three Estimates of migration are read (see the second **Change**).
- **Where does the grouping of the pending readings stand?**
  - Recommended: (a) in the closing Case: its `context` lists the groups, its `tasks` hold a `by hand` task per moment and a `read` line per Estimate.
  - Answer: agreed.
- **How is this Case split, and what checks each part?**
  - Recommended: (a) three sub-cases, one new check each, all on `rule-sprint-close`: the librarian runs the close; the readings in groups; the next sprint opens first.
  - Answer: agreed.
- **What makes the next session open the new sprint first?**
  - Recommended: (b) the brief and `/hi`, plus a ledger hook that refuses every decision line but a `defer` until a `create` of a sprint page stands.
  - Answer: agreed.
- **How does the close command, with your choices, reach the librarian?**
  - Recommended: (a) keep the task line, and change Work Mode, Retro, `rule-orchestration` and the ticker of `guppi sprint` so that the librarian runs it and the command ticks it.
  - Answer: agreed.
- **How is this Case cut, now that more checks must change?**
  - Recommended: (a) one Case with every sub-case: the three new checks, the migration check and one sub-case per check the change makes false.
  - Answer: agreed.
- **Change**
  - Asked: at `/pre-spec`, on where the `## Backlog` lines of a closed sprint page go, the person said the backlog should pass between sprints, and that the Backlog of the sprint page goes into the general `backlog.md`.
  - Taken: 628.12: `guppi backlog` reads the `## Backlog` of each sprint page, live or under `vault/archive/`; `rule-backlog` and the Criterion of `estimate-backlog-renders` say so, and `## How it works` of `rule-sprint-close` names it.
- **Change**
  - Asked: at `/pre-spec`, on when the three Estimates of migration are read, option (a): in the Work Mode of the closing session, before the librarian's run, their Then naming what holds before the close — `make test` green on the last commit, `make lint` with no finding but the unread of the sprint page's own Estimates, the leftovers gone — the merge into `main` leaving the promise of the closed sprint and becoming the first work of the session that opens the next sprint.
  - Taken: 628.9 to 628.11 replace the When of the three, and the Then of `estimate-sprint-migration-merges` keeps only `make test`; their purposes and methods are set anew; `entity-sprint-migration` gets the merge as a line of its `## Backlog`, its Slice 5 note replaced by the close of migration, and "the branch merged" out of its Purpose.
- **Change**
  - Asked: on Case 627, the person agreed that the change to the sprint page also closes the question put off on it by `decision-case-615`, how much stays for the close of migration, answered by what this session set; the Case that changes the other line of the same milestone carries the same mark.
  - Taken: the decision line of 628.9 on `entity-sprint-migration` carries `{supersedes:case 615}`; the defer is retired and the page leaves `backlog.md`.

## History

- 2026-10-04 created · raw/2026-10-04/1439/ledger.md#case-628
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
