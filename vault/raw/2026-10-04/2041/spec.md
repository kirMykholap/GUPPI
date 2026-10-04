<!-- approved 22:18:09 · session 9fb75985 -->

# Spec — session 2041, 2026-10-04

## Case 632 — The findings on Cases 627–629 closed before the close of migration

> **context:**
> Cases 627, 628 and 629 were ratified in session 1439. They built the close of a sprint and the check of a built Case against the other Cases of its session. Session 1934 took their conserved Spec and ran it unchanged, because a session that takes a conserved Spec builds and ratifies none of its Cases again. The librarian then applied it (commit c04578e2). At the `/pre-spec` of 1934, `ask-guppi` found places where their texts contradict a page, the code or each other, and Estimates that they did not name. The texts stand that way today:
> - `rule-sprint-close` is a Leaf, but it gained a `## How it works`, which `rule-rules-schema` allows only on a MOC. Its Purpose describes the command, not the failure the rule prevents.
> - `rule-cleanup` kept its own section when 627.1 touched it.
> - `entity-sprint`, `rule-sprint` and the Purpose of `entity-sprint-migration` call the sprint page's Estimates its Definition of done, but the close goes ahead without them.
> - `estimate-sprint-migration-lint-clean` fails by design. Lint reports every pending Estimate as `unread`, and some Estimates that Case 628 created or reset can be read only at or after the closing librarian's run. One example is `estimate-sprint-close-runs-in-the-librarian-run`.
> - The Criterion of `estimate-sprint-close-next-session-opens-the-sprint` gives the new sprint id to every page of the opening run. `opened_sprint` of `guppi/materialize.py` gives it only to the pages written from the ledger that creates the sprint page.
> - The session that opens a sprint can never take a conserved Spec, and no text says so. It must ratify the opening `create` first, and `/hi` takes a conserved Spec only while the ledger holds no decision line but a `defer`. The same sentence of `rule-skill-hi` also puts two things first.
> - Step 5 of `rule-documentation` reads the Backlog of the live sprint page only, but `guppi backlog` has read each sprint page, live or archived, since 628.12.
> - The method `-k clash` of `estimate-case-check-sends-back-a-case-number-held-by-another-agent` also selects the tests of 629.1, whose names hold `session_clash`.
> - Four Estimates speak of what those Cases changed, and the Cases did not name them.
>
> The person agreed with every recommendation of the round. The fixes carry no `{supersedes}` mark. The Decision pages of 627–629 stay current, and each sub-case says which of them it corrects (Q1). One Case holds one sub-case per promise (Q2). The answers fall on the sub-cases as follows:
> - 632.1 (Q3): both `## How it works` sections leave. Two parts of the section of `rule-sprint-close` stand in no other file that an agent loads: the session of its own, and the readings sorted into groups. They go into `rule-orchestration`, together with the 628.3 sentence that `guppi sprint` and `make lint` report the missing sprint page until the next sprint opens. The Purpose keeps only the failure the rule prevents.
> - 632.3 (Q4): the three texts say that the Estimates are the Definition of done, read before the close.
> - 632.4 (Q5): the lint bar also passes an `unread` of an Estimate that the close line carries because its moment comes at or after the closing librarian's run.
> - 632.5 (Q6): the texts follow the code on the sprint id.
> - 632.6 and 632.7 (Q7): the opening session takes no conserved Spec. This changes what `/hi` lists. The Cases line of `estimate-hi-writes-frontier` lists each conserved Spec, so its Criterion is replaced too, in 632.6. 632.7 replaces the Criterion of `estimate-hi-takes-a-conserved-spec`, as the answer to Q7 says, and its lines on taking a Spec now hold explicitly for a session that does not open a sprint. The Frontier and the taking of a Spec are two promises, so they are two sub-cases.
> - 632.8 (Q8): the older selector narrows to `-k subagent_clash`.
> - 632.9 (Q9): `estimate-insights-schema-checked` drops its word-for-word claim.
> - 632.10 (Q10): `estimate-orchestration-asks-in-the-grill-me-shape` takes the question that the main agent asks after a clash.
>
> `estimate-work-mode-takes-the-work-readings` stands (Q11). Its step takes each open `W` reading whose moment has come and leaves an Estimate that the session itself changes. The closing Case's `by hand` tasks set up the moments before that step, so its Criterion and the Criterion of `estimate-sprint-close-takes-the-readings-in-groups` agree. Step 5 of `rule-documentation` needed no choice and is 632.2.
>
> The `/pre-spec` of this session found that Case 634.2, in `vault/raw/2026-10-04/2041/cases/case-634.md`, adds one more question that the main agent asks itself: after the `ask-guppi` runs confirm their findings, whether each finding not closed is fixed or left. 632.10 adds that question too, both to the list of `rule-orchestration` and to the When and the purpose of the Criterion it replaces, so that only one Case replaces that Criterion. Its anchor leaves out the sentence of `rule-orchestration` that 634.3 rewords, the one that says the agent dispatches `ask-guppi` once, at pre-spec.
>
> The same check named four Estimates that speak of what a sub-case changes. Each agrees with the change, its Criterion stands, and the `given` of the sub-case names it:
> - `estimate-cleanup-moves` (632.1): its Then states the facts that move into the docstring of `guppi/cleanup.py`;
> - `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest` (632.3): the sprint page's Estimates go to the archive with it;
> - `estimate-generate-writes` (632.5): a page's sprint is the `<id>` in a unit whose ledger creates `entity-sprint-<id>`;
> - `estimate-spec-box-refuses-a-stale-spec` (632.7): `guppi box --check` refuses a session that ratified a Case of its own, and that already guards the session that opens a sprint.
>
> The frame. `guppi generate` applies `sections` as whole replacements and removes no section (`guppi/generate.py`, the `update` branch). So the two sections leave by a one-off task by hand, as the section of `rule-case-check` left in case 589.2 and the section of `rule-ledger-write` in case 592: their History lines read that the section was removed by hand, or left the Leaf. The line of `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` that the skill writes no page of `vault/wiki/` stands, as it stood for those one-off tasks.
>
> The searches this Case rests on:
> - A Grep of ``How it works` of`` over the repository outside `vault/archive/`, `vault/raw/` and `vault/wiki/decisions/` printed `guppi/casecheck.py`, on the section of `rule-case-check`, and `rule-sprint-close.md`, its own Purpose. So no other text points to the section that leaves.
> - A Grep of `session of its own|into groups|kind of moment` over `.claude/`, `vault/wiki/*.md` and `vault/wiki/rules/` printed `sprint.md` (the milestone note of migration), `rule-sprint-close.md` and `log.md`. So the two parts that move into `rule-orchestration` stand in no other rule and no harness file.
> - A Grep of `Definition of done|Done when` over the repository outside `vault/archive/`, `vault/raw/` and `vault/wiki/decisions/` printed 14 files: `brief.md`, `glossary.md`, `sprint.md`, `entity-glossary.md`, `entity-sprint.md`, `entity-sprint-migration.md`, `tests/test_sprint.py`, `guppi/sprint.py`, `vault/wiki/rules/schema.yaml`, `rule-sprint.md`, `rule-rules-schema.md`, `docs/migration/migration-plan.md`, `log.md` and `estimate-sprint-renders-the-backlog.md`. 632.3 changes three of them. The others stand:
>   - `glossary.md`, `entity-glossary.md`, `guppi/sprint.py` and `tests/test_sprint.py` name the Estimates as the Definition of done, which stays true;
>   - `vault/wiki/rules/schema.yaml` and `rule-rules-schema.md` say that it is read;
>   - `sprint.md` and `estimate-sprint-renders-the-backlog.md` speak of the rendered Done when;
>   - `docs/migration/migration-plan.md` is a leftover that the closing Case deletes;
>   - `brief.md` and `log.md` were not read.
> - A Grep of `Backlog.? of the sprint page` over `.claude/`, `vault/wiki/*.md`, `vault/wiki/rules/`, `vault/wiki/estimates/`, `vault/wiki/entities/` and `guppi/` printed three lines:
>   - `vault/wiki/brief.md`, which was not read;
>   - `rule-documentation.md` line 77, step 5;
>   - `.claude/agents/librarian-guppi.md` line 105, its render.
> - A Grep of `-k clash` outside `vault/archive/` and `vault/raw/` printed `brief.md`, `lesson-prespec-one-ask-guppi-run-samples-the-spec.md`, which records the finding and stands, and the Estimate that 632.8 changes.
> - A Grep of `def test_\w*clash\w*` over `tests/` printed 11 tests in `tests/test_casecheck.py`: three that open `test_subagent_clash_` and eight that open `test_subagent_session_clash_`.
> - A Grep of `conserved Spec` over `.claude/`, `vault/wiki/rules/` and `vault/wiki/orchestration.md` printed 19 files. I read the hits of `rule-skill-hi`, `rule-spec-box`, `rule-backlog` and `rule-brief`: only `rule-skill-hi` sets which lines `/hi` writes. I did not read the other 15 files.
>
> No `create` is proposed, so the vault query was not run.
>
> The notes of the hook. Some lines of a replaced Criterion are not carried, on purpose:
> - In 632.4, the When also names the close line of the closing Spec, and the Then line on the one exception gives way to a line on the findings and two exception lines, as Q5 chose.
> - In 632.5, the line on the pages of the opening run gives way to the line on the pages written from the ledger that creates the sprint page, as Q6 chose.
> - In 632.6, the line on where the kinds of `## Cases` come from puts the opening line alone first, and a new `－` line keeps every conserved Spec off the Frontier while that line stands.
> - In 632.7, three lines now name the session they hold for, so that they do not contradict the `－` line of the session that opens a sprint:
>   - the line on taking the Spec names the session that does not open a sprint;
>   - the line on closing its Frontier line names such a session;
>   - the line on Cases not built again names the session that takes the Spec.
> - In 632.9, the old Then is rewritten without its lists. Each list item stands in one line of lint keys, and the word-for-word claim and the old file `schema.md` leave the description line, as Q9 chose.
> - In 632.10, the When gains the question after a clash and the question on a finding not closed.
>
> Several `then` lines share words with a line of a sibling, and each pair speaks of a different promise, so each line stays in its own sub-case:
> - a line of 632.3, on the close, with 632.1, on the missing sprint page;
> - the lines of 632.6, the lines `/hi` writes on the Frontier, with 632.5, the brief and the opening line after a close;
> - the lines of 632.7, the taking of a conserved Spec, with 632.5 and 632.6;
> - a line of 632.10, the shape of the main agent's questions, with 632.7.
>
> Not done:
> - The bar of `estimate-sprint-migration-lint-clean` on stale defers stands as 628.10 kept it. Four stale defers stand today.
> - The `read` lines that 628.2 puts into the closing Case, for Estimates that the Case does not change, stand as 628.2 set them.
> - How `/pre-spec` checks a whole Spec is Case 634.

> **problem:**
> The Cases that built the close of a sprint left texts that contradict the schema of rule pages, the close itself, the code and each other. They also left four Estimates that speak of what those Cases changed. The question is how each contradiction is fixed before the close of migration, and which checks follow.

> **recommend:**
> - **Do the fixes mark the earlier decisions as replaced?**
>   - Recommended: (a) no mark: new sub-cases change the pages, each `context` names the earlier sub-case it corrects, and the earlier decision pages stay current.
>   - Answer: agreed.
> - **How is the Case cut?**
>   - Recommended: (a) one Case, one sub-case per promise, the count set by the other answers.
>   - Answer: agreed.
> - **Where does the description of the close go?**
>   - Recommended: (a) both sections leave: the Purpose of `rule-sprint-close` keeps only the failure it prevents, the two parts with no other home go into `rule-orchestration`, and the section of `rule-cleanup` goes into the docstring of `guppi/cleanup.py`.
>   - Answer: agreed.
> - **What does "Definition of done" mean when the close does not wait for it?**
>   - Recommended: (a) reword the three texts: the Estimates are the Definition of done, read before the close; one not passed goes to the archive with the sprint page, its status kept in the record of the close.
>   - Answer: agreed.
> - **What bar does the lint check of migration keep?**
>   - Recommended: (a) widen the exception to an `unread` of an Estimate whose method names a moment at or after the closing librarian's run and which the close line carries by `--carry`; the Criterion replaced, its purpose and method following.
>   - Answer: agreed.
> - **Which pages of the opening run carry the new sprint id?**
>   - Recommended: (a) the texts follow the code: the pages written from the session that creates the sprint page carry its id.
>   - Answer: agreed.
> - **Can the session that opens the next sprint take a conserved Spec?**
>   - Recommended: (a) no: while the opening line stands, `/hi` lists no conserved Spec, the sentence is reworded so that only the opening line comes first, and the Criterion of `estimate-hi-takes-a-conserved-spec` is replaced.
>   - Answer: agreed.
> - **How does the older clash check stop running the newer tests?**
>   - Recommended: (a) narrow the older method to `-k subagent_clash`.
>   - Answer: agreed.
> - **What does the schema check of Insights claim about its text?**
>   - Recommended: (a) replace the Criterion with no word-for-word claim; pending, read by its test and `make lint`.
>   - Answer: agreed.
> - **Does the check of the main agent's own questions cover the new question?**
>   - Recommended: (a) replace the Criterion, its When naming the question after a clash.
>   - Answer: agreed.
> - **Does the check of the Work readings change for the closing session?**
>   - Recommended: (a) its Criterion stands, and `context` says why.
>   - Answer: agreed.

### Case 632.1 — `## How it works` leaves `rule-sprint-close` and `rule-cleanup`, and the closing session stands in `orchestration.md`

> **given:**
> `rule-sprint-close` — the rule of the close of `entity-sprint-<id>`, a Leaf; its Purpose changes and its `## How it works` leaves (it corrects 627.1 and 628.1)
> **＋** `rule-cleanup` — a Leaf; its `## How it works` leaves (it corrects 627.1)
> **＋** `guppi/cleanup.py` — its docstring takes the facts of that section that it lacks
> **＋** `guppi/sprint_close.py` — its docstring already holds the mechanism of the close and the tick of its line
> **＋** `rule-orchestration` — what the main agent does, rendered into `vault/wiki/orchestration.md`, which `/hi` loads; one paragraph is added
> **＋** `rule-rules-schema` — a Leaf drops `## How it works` at its next touch, and a Purpose states the failure it prevents
> **＋** `estimate-sprint-close-takes-the-readings-in-groups`, `estimate-sprint-close-runs-in-the-librarian-run` and `estimate-cleanup-moves` — they check the closing session and the moves of `guppi cleanup`, its rerun, its exit 1 and its History lines; their Criteria stand
> **＋** `guppi sprint` and `make lint` — they report the missing sprint page after a close

> **when:**
> The main agent plans the session that closes `entity-sprint-<id>`, with `vault/wiki/orchestration.md` rendered from `rule-orchestration` and loaded by `/hi`.
> **＋** Someone reads `rule-sprint-close`, `rule-cleanup` and the docstring of `guppi/cleanup.py`.

> **then:**
> `vault/wiki/orchestration.md` says that the session that closes a sprint is a session of its own, whose Plan Mode holds only the closing Case and the Cases that prepare its readings.
> **＋** It says that before the closing Case the main agent sorts the Estimates that stand `pending` or `failed` into groups by the kind of moment their `method` names, and that only an Estimate still unread after Work Mode is carried or archived unread.
> **＋** It says that `guppi sprint` and `make lint` report the missing sprint page from the close until a Case of the next session creates the next one, and that this is expected.
> **＋** `rule-sprint-close` holds a Purpose that states the failure it prevents, and no `## How it works`.
> **＋** `rule-cleanup` holds no `## How it works`, and the docstring of `guppi/cleanup.py` holds each fact that section held.
> **－** The docstring of `guppi/sprint_close.py` does not change: it already holds the mechanism of the close.

```then
update:
- slug: rule-sprint-close
  sections:
    Purpose: 'Prevents a closed sprint from leaving its finished work among the live pages, so that the vault does not only grow: without a close, the Decision pages, the `actioned` Insights, the `error` lessons that joined no Insight, the sprint page and its Estimates of every past sprint stay among the pages that each search of the vault reads (cases 612, 627.1, 632.1).'
  change: '## How it works left the Leaf: the mechanism in the docstring of guppi/sprint_close.py, the closing session in orchestration.md; the Purpose states the failure it prevents (case 632.1)'
- slug: rule-cleanup
  change: '## How it works left the Leaf, its mechanism in the docstring of guppi/cleanup.py (case 632.1)'
- slug: rule-orchestration
  replace:
  - old: while another Case is built, as `## Showing and signing a Case` sets it (case 598.1).
    new: |-
      while another Case is built, as `## Showing and signing a Case` sets it (case 598.1).

      The session that closes a sprint is a session of its own: its Plan Mode holds only the closing Case and the Cases that prepare its readings, so that all of its decisions belong to the sprint it closes, and the closing Case holds the task line `uv run guppi sprint-close --sprint <id> --apply` with the person's choices, which the librarian runs (`rule-sprint-close`, case 628.1). Before the closing Case, the main agent sorts the Estimates that stand `pending` or `failed` into groups by the kind of moment their `method` names; the closing Case names the groups in its `context` and holds one `by hand` task per moment that Work Mode sets up and one `read` line per Estimate, and only an Estimate still unread after Work Mode is carried or archived unread (case 628.2). From the close until the first Case of the next session creates the next sprint page, `guppi sprint` and `make lint` report the missing sprint page, and that is expected (cases 628.3, 632.1).
  change: the session that closes a sprint — a session of its own, its readings in groups, the missing sprint page expected — moved here from the How it works of rule-sprint-close (case 632.1)
```

```tasks
- [ ] update `rule-sprint-close`
- [ ] update `rule-cleanup`
- [ ] update `rule-orchestration`
- [x] `guppi/cleanup.py`: the docstring gains the facts of the section that it lacks — `sprint` is the first `## <id>` heading of `sprint.md`; the History lines `archived · cleanup` and `restored · cleanup`; a rerun moves nothing and exits 0; a file that cannot be moved, or a name already taken in the archive, is reported on stderr with exit 1, and the other pages still move
- [x] one-off, by hand: the `## How it works` section of `vault/wiki/rules/rule-cleanup.md` is removed, its heading and text, after the docstring of `guppi/cleanup.py` holds each of its facts
- [x] one-off, by hand: the `## How it works` section of `vault/wiki/rules/rule-sprint-close.md` is removed, its heading and text; each of its facts stands in the docstring of `guppi/sprint_close.py`, in the new paragraph of `rule-orchestration`, or in `rule-documentation`, `rule-work-mode`, `rule-retro`, `rule-skill-hi`, `rule-brief`, `rule-ledger-write`, `rule-materialize` or `rule-backlog`
- [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
```

### Case 632.2 — Step 5 of the librarian reads the Backlog of each sprint page

> **given:**
> `rule-documentation` — the frame of `librarian-guppi`, rendered into `.claude/agents/librarian-guppi.md`; step 5 changes (it follows 628.12)
> **＋** `rule-backlog` and `guppi/backlog.py` — `uv run guppi backlog`, which reads the `## Backlog` of each sprint page, live or under `vault/archive/`
> **＋** `vault/wiki/backlog.md` and `vault/archive/` — the file the script writes and where a closed sprint page stands
> **＋** `estimate-backlog-renders` — checks what `guppi backlog` reads; its Criterion stands

> **when:**
> `librarian-guppi` reaches step 5 of `.claude/agents/librarian-guppi.md`, rendered from `rule-documentation`, and runs `uv run guppi backlog`.

> **then:**
> Step 5 says that `uv run guppi backlog` writes `vault/wiki/backlog.md` from the conserved Specs, the pages with `deferred_by`, the open Insights and the `## Backlog` of each sprint page, live or under `vault/archive/`.
> **－** The step does not name the live sprint page as the only source of Backlog lines.

```then
update:
- slug: rule-documentation
  replace:
  - old: the open Insights and the `## Backlog` of the sprint page.
    new: the open Insights and the `## Backlog` of each sprint page, live or under `vault/archive/` (`rule-backlog`, case 632.2).
  change: step 5 reads the Backlog of each sprint page, live or archived (case 632.2)
```

```tasks
- [ ] update `rule-documentation`
- [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
```

### Case 632.3 — The sprint page's Estimates are its Definition of done, read before its close

> **given:**
> `entity-sprint` — the MOC over the sprint pages; one phrase of its Purpose changes
> **＋** `rule-sprint` — the guard of the sprint page; one phrase of its Purpose changes
> **＋** `entity-sprint-migration` — the sprint page; one sentence is added to its Purpose (it corrects 628.9)
> **＋** `rule-sprint-close` — the close, `uv run guppi sprint-close --sprint <id> --apply`, and the record of the close
> **＋** `estimate-sprint-close-settles-unread-estimates` and `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest` — they check that an Estimate of the sprint page is read or archived unread, and goes to the archive with the sprint page; their Criteria stand
> **＋** `vault/wiki/sprint.md` — rendered from the sprint page by `guppi sprint`

> **when:**
> Someone reads `entity-sprint`, `rule-sprint`, `entity-sprint-migration` and `vault/wiki/sprint.md`, and the close `uv run guppi sprint-close --sprint <id> --apply` runs.

> **then:**
> The three pages say that the Estimates of a sprint page are its Definition of done, read before its close.
> **＋** They say that an Estimate of the sprint page that has not passed by the close goes to the archive with the sprint page, and that the record of the close keeps its status.
> **－** No page says that the close waits until every Estimate of the sprint page passes.

```then
update:
- slug: entity-sprint
  replace:
  - old: its Estimates are its Definition of done, its `## Milestones`
    new: its Estimates are its Definition of done, read before its close, and one that has not passed by then goes to the archive with the sprint page, its status kept in the record of the close (`rule-sprint-close`, case 632.3); its `## Milestones`
  change: the Estimates are the Definition of done read before the close; one not passed is archived with the sprint page (case 632.3)
- slug: rule-sprint
  replace:
  - old: whose `estimates` are its Definition of done —
    new: whose `estimates` are its Definition of done, read before its close, one that has not passed by then going to the archive with the sprint page, its status kept in the record of the close (`rule-sprint-close`, case 632.3) —
  change: the Estimates of a sprint page are its Definition of done read before the close (case 632.3)
- slug: entity-sprint-migration
  replace:
  - old: the `file` route out of the scripts.
    new: the `file` route out of the scripts. Each Estimate of this page is read before the close of the sprint; one that has not passed by then goes to the archive with this page, its status kept in the record of the close (`rule-sprint-close`, case 632.3).
  change: each Estimate of the page is read before the close; one not passed is archived with the page (case 632.3)
```

```tasks
- [ ] update `entity-sprint`
- [ ] update `rule-sprint`
- [ ] update `entity-sprint-migration`
- [ ] `uv run guppi sprint`
```

### Case 632.4 — The lint check of migration passes the readings that wait for the close

> **given:**
> `estimate-sprint-migration-lint-clean` — its Criterion replaced whole, its `purpose` and `method` set anew (it corrects 628.10)
> **＋** `entity-sprint-migration` — the sprint page whose Estimates are one exception
> **＋** `rule-sprint-close` — the close line `uv run guppi sprint-close --sprint migration --apply` and its `--carry`
> **＋** `rule-lint` and `make lint` — a `pending` Estimate is an `unread` finding until its reading
> **＋** `vault/raw/<date>/<hi HHMM>/spec.md` — the Spec of the closing session, which holds the close line

> **when:**
> In the Work Mode of the session that closes `entity-sprint-migration`, before the librarian's run, someone reads `make lint` and the close line `uv run guppi sprint-close --sprint migration --apply` of `vault/raw/<date>/<hi HHMM>/spec.md`.

> **then:**
> `make lint` prints no finding in any category, `unmigrated` included — the old Estimate shape is gone, the counter at zero — but the `unread` lines below, and exits 0 when it prints none of them.
> **－** An `unread` line on an Estimate of `entity-sprint-migration` not yet read at that moment fails nothing.
> **－** An `unread` line on an Estimate whose `method` names a moment at or after the librarian's run of the closing session, and that the close line names by `--carry`, fails nothing.

```then
update:
- slug: estimate-sprint-migration-lint-clean
  set:
    status: pending
    purpose: make lint in the Work Mode of the session that closes the sprint, before the librarian's run, shows no finding, unmigrated included, but the unread of the sprint page's own Estimates and of the Estimates read only at or after the closing librarian's run, which the close line carries
    method: 'make lint in the Work Mode of the session that closes the sprint, before the librarian''s run: exit 0, or only unread lines on the Estimates of entity-sprint-migration and on Estimates whose method names a moment at or after that librarian''s run and that the close line names by --carry, each such line named in the estimate line'
  change: the Criterion replaced whole — an unread Estimate that the close line carries because its moment comes at or after the closing librarian's run fails nothing (case 632.4)
```

```tasks
- [ ] update `estimate-sprint-migration-lint-clean`
- [ ] read `estimate-sprint-migration-lint-clean`
```

### Case 632.5 — The new sprint id goes to the pages of the session that creates the sprint page

> **given:**
> `estimate-sprint-close-next-session-opens-the-sprint` — its Criterion replaced whole, its `purpose` and `method` set anew (it corrects 628.3)
> **＋** `rule-sprint-close` — the close of `entity-sprint-<id>`; `entity-sprint-<new id>` is the next sprint page, and `entity-sprint-` is the prefix of any sprint page
> **＋** `rule-materialize`, `guppi/materialize.py` and `tests/test_materialize.py` — `guppi materialize` sets the yaml's `sprint` per session by `opened_sprint`; they stand
> **＋** `estimate-generate-writes` — its line on a page's sprint as the `<id>` in a unit whose ledger creates `entity-sprint-<id>` agrees; its Criterion stands
> **＋** `rule-ledger-write`, `guppi/ledger.py` and `tests/test_ledger.py` — the hook `uv run guppi ledger`, `guppi ledger`
> **＋** `rule-skill-hi` and `rule-brief` — `/hi` and the brief
> **＋** `vault/wiki/brief.md`, `vault/wiki/sprint.md`, `frontier.md` and `vault/raw/<date>/<hi HHMM>/frontier.md` — what the brief and `/hi` write and read
> **＋** `guppi sprint` — writes `vault/wiki/sprint.md`; its error after a close is a flag

> **when:**
> The librarian's run of the session that closes `entity-sprint-<id>` ends with no live sprint page, and the next session opens with `/hi`; someone reads `vault/wiki/brief.md`, that session's `vault/raw/<date>/<hi HHMM>/frontier.md`, the refusals of `uv run guppi ledger` in its transcript, its ledger, and the pages of its librarian's run.
> **＋** Or `tests/test_ledger.py` and `tests/test_materialize.py` run `guppi ledger` and `guppi materialize` over a made-up vault with no live sprint page.

> **then:**
> The first line of the `Cases` of Next session in `vault/wiki/brief.md` is `open the next sprint — no sprint is open since the close of <id>`.
> **＋** `/hi` writes that line first under `## Cases` of `frontier.md`, and takes no item of `vault/wiki/sprint.md`.
> **＋** While no live `entity-sprint-` page stands, `guppi ledger` refuses each decision line of the session but a `defer`, with one stderr line, until the session's ledger or the same reply holds a `create` decision line of an `entity-sprint-` slug.
> **＋** Each page that the librarian's run writes from the ledger of that session, which holds the `create` decision line of `entity-sprint-<new id>`, carries `sprint: <new id>`.
> **－** An `estimate` or `lesson` line is not refused for this reason.
> **－** The error of `guppi sprint` in the closing run is a flag of the brief, not a failure of this promise.

```then
update:
- slug: estimate-sprint-close-next-session-opens-the-sprint
  set:
    status: pending
    purpose: Whether after the close of a sprint the brief puts the opening of the next sprint first, /hi takes no item of sprint.md, the ledger hook refuses every decision line but a defer until a create of a sprint page stands, and the pages written from the ledger of the session that opens it carry its id
    method: 'pytest tests/test_ledger.py -k sprint and tests/test_materialize.py -k sprint; by hand, at the librarian''s run of the session after the close of a sprint: the brief before it, its frontier.md, the refusals of guppi ledger in its transcript, its ledger and the sprint field of the pages written from that ledger'
  change: the Criterion replaced whole — the new sprint id goes to the pages written from the ledger that creates the sprint page, as materialize sets it (case 632.5)
```

```tasks
- [ ] update `estimate-sprint-close-next-session-opens-the-sprint`
- [ ] read `estimate-sprint-close-next-session-opens-the-sprint`
```

### Case 632.6 — `/hi` lists no conserved Spec while the opening of the next sprint stands

> **given:**
> `estimate-hi-writes-frontier` — its Criterion replaced whole (it corrects 628.7)
> **＋** `rule-skill-hi` — the skill `/hi`, rendered into `.claude/skills/hi/SKILL.md`; the sentence on the `## Cases` sources is reworded
> **＋** `vault/wiki/sprint.md`, `vault/wiki/brief.md` and `vault/wiki/backlog.md` — what `/hi` loads; a conserved Spec stands in `backlog.md`
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier it writes
> **＋** `rule-sprint-close` — the gap between the close and the next sprint

> **when:**
> The person invokes `/hi`. The agent assembles the Frontier from `vault/wiki/sprint.md`, `vault/wiki/brief.md`, `vault/wiki/backlog.md` and the output of the skill's commands, and closes its lines in Plan Mode.

> **then:**
> The Frontier is written to `raw/<date>/<hi HHMM>/frontier.md` in the lists `## Cases`, with lines `- [ ] C<n> — <title> · <source>`, `## Work`, with lines `- [ ] W<n> — <title> · <source>`, and `## Ask`, with lines `` - [ ] A<n> — `<slug>` — <question> · brief ``. The title of a line of the current milestone or of the backlog opens with the slug of each of its pages in a code span.
> **＋** The kind comes from the source. Cases: first, when the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, that line; then, on a plan branch, the unfinished plan and each conserved Spec of `vault/wiki/backlog.md`, with the source `backlog`; then the items of the current milestone; the `Cases` list of the brief's Next session; a hand edit shown by `Render:`; a `failed` reading or a lesson of the ledger's Tail; an item the person adds. Work: the `Work` list of the brief's Next session; a dirty tree by `git status`. Ask: the `Ask the person` list of the brief's Next session.
> **＋** The other items of the backlog are not lines. `## Cases` ends with the line `Backlog: N items`, where N is the count in `vault/wiki/backlog.md`. Under a Cases line, an indented line `- near` names by slug each backlog item whose `purpose` is near that line in meaning. The agent judges this from the loaded file, with no `ask-guppi`. An item the person brings onto the Frontier becomes a Cases line with the source `backlog`.
> **＋** A line closes by appending the closer and keeping the source. An item ended closes `[x] … · case N` when decided, or `[x] … · work` when done with no decision. A line of the sprint page left for a later session closes `[-] … · sprint · defer`. An item of the backlog left as it stands closes `[-] … · backlog · kept`. A decision of any other source put off closes `[-] … · defer case N`.
> **＋** An item closed `defer` or `kept` has no short Case and no ledger line. A sprint item never closes `· defer case N`.
> **＋** Only the current milestone gives items. A later milestone and Closed give none, and the sprint page's Backlog reaches the Frontier only through the backlog. A decision line of the Tail is not an item.
> **＋** In the chat the Cases are shown as a checklist. Each line stands as `raw/<date>/<hi HHMM>/frontier.md` holds it, `- [ ] C<n> — <title> · <source>`, with its detail on an indented line under it and the `- near` line under that, and the line `Backlog: N items` comes last. The Work is shown as one block. Only Cases are cut into sub-cases. A `W` that turns out to need a decision closes `· case N`. A `C` that needs none closes `· work`.
> **－** While the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, no conserved Spec and no item of the current milestone is a Cases line, and each conserved Spec stays in `vault/wiki/backlog.md`.
> **－** At `/hi` no Case stands in the chat as a bold line, and no Case has its detail as a paragraph.
> **－** Pre-spec finds an open line under `## Cases`. A `W` or an `A` line stands open until its work is done and closes `· work` where that work is done: at `/hi`, in Work Mode or at Retro. Claude Code's plan mode does not stop the agent from writing `frontier.md`.

```then
update:
- slug: rule-skill-hi
  replace:
  - old: on a plan branch the unfinished plan, and each conserved Spec `backlog.md` names, one line each with the source `backlog`, first; the items of the sprint's current milestone — the first with an open item or with none — and none of a later milestone, of the Backlog or of Closed (case 229.3) — and none at all while the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, which then stands as the first Cases line, before every other (`rule-sprint-close`, case 628.7);
    new: 'first, when the first line of the `Cases` of the brief''s Next session opens with `open the next sprint`, that line (`rule-sprint-close`, case 628.7); then, on a plan branch, the unfinished plan, and each conserved Spec `backlog.md` names, one line each with the source `backlog` — but none while that opening line stands: the session that opens a sprint takes no conserved Spec, which waits in `backlog.md` for the next session (case 632.6); the items of the sprint''s current milestone — the first with an open item or with none — and none of a later milestone, of the Backlog or of Closed (case 229.3), and none at all while that opening line stands (case 628.7);'
  change: the opening of the next sprint alone comes first; no conserved Spec on the Frontier while it stands (case 632.6)
- slug: estimate-hi-writes-frontier
  set:
    status: pending
  change: the Criterion replaced whole — no conserved Spec is a Cases line while the opening of the next sprint stands (case 632.6)
```

```tasks
- [ ] update `rule-skill-hi`
- [ ] update `estimate-hi-writes-frontier`
- [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [ ] read `estimate-hi-writes-frontier`
```

### Case 632.7 — The session that opens a sprint takes no conserved Spec

> **given:**
> `estimate-hi-takes-a-conserved-spec` — its Criterion replaced whole, its `method` set anew
> **＋** `rule-skill-hi` — the skill `/hi`, rendered into `.claude/skills/hi/SKILL.md`; its sentence on the `## Cases` sources is changed by 632.6
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier of the session
> **＋** `vault/wiki/brief.md` and `vault/wiki/backlog.md` — the opening line of the next sprint, and the conserved Specs
> **＋** the plan file of the session, its title line `# Session <hi HHMM> — runs the conserved Spec vault/raw/<date>/<HHMM>/spec.md`, and `vault/raw/<date>/<HHMM>/spec.md` of a conserved Spec
> **＋** `/box` and `/pre-spec` — run the conserved Spec, and check the plan
> **＋** `estimate-spec-box-refuses-a-stale-spec` — `guppi box --check` refuses a session that ratified a Case of its own, which already guards the session that opens a sprint; its Criterion stands

> **when:**
> In a session that `/hi` opened from `.claude/skills/hi/SKILL.md` as rendered from `rule-skill-hi`, the person takes a conserved Spec of `## Cases` of `raw/<date>/<hi HHMM>/frontier.md`.
> **＋** Or `/hi` opens the session after the close of a sprint, while the first line of the `Cases` of Next session in `vault/wiki/brief.md` opens with `open the next sprint`.

> **then:**
> In a session whose `/hi` found no first line `open the next sprint` in the `Cases` of Next session of `vault/wiki/brief.md`, the agent takes the Spec whole, to be run by `/box`, only while the session's ledger holds no decision line other than a `defer`, and after it ratifies no Case but a short-form defer.
> **＋** In such a session it closes the line of that Spec `[x] … · work`.
> **＋** It creates the plan file with one title line, `# Session <hi HHMM> — runs the conserved Spec vault/raw/<date>/<HHMM>/spec.md`, the path that `vault/wiki/backlog.md` names for that Spec.
> **＋** It closes each other open line under `## Cases` as left — `[-] … · backlog · kept`, `[-] … · sprint · defer` or `[-] … · defer case N` — and goes on to `/pre-spec`.
> **＋** A line whose target a `defer` item of that Spec puts off closes `[-] … · defer case N`, N being the Case of that Spec that holds the item, and the session writes no short-form Case and no ledger line for it.
> **－** In the session that opens the next sprint no conserved Spec stands under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md`, and the agent takes none; each stays in `vault/wiki/backlog.md` for a later session.
> **－** No other line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` closes `[x]`.
> **－** No Case of the conserved Spec is built again or ratified again in the session that takes it.
> **－** `.claude/skills/hi/SKILL.md` equals the Render of `rule-skill-hi` and is not edited by hand.

```then
update:
- slug: estimate-hi-takes-a-conserved-spec
  set:
    status: pending
    method: 'uv run guppi render --check; by hand, a session whose person takes a conserved Spec at the Frontier: frontier.md, the title line of the plan file and the session''s ledger read against the Criterion; and the /hi of the session after the close of a sprint: its frontier.md and backlog.md'
  change: the Criterion replaced whole — a session that does not open a sprint takes a conserved Spec as before; the session that opens the next sprint takes none (case 632.7)
```

```tasks
- [ ] update `estimate-hi-takes-a-conserved-spec`
- [ ] read `estimate-hi-takes-a-conserved-spec`
```

### Case 632.8 — The older clash check selects only its own tests

> **given:**
> `estimate-case-check-sends-back-a-case-number-held-by-another-agent` — its `method` set anew; its Criterion stands
> **＋** `uv run pytest tests/test_casecheck.py -k subagent_clash` — the new selector of that method
> **＋** `estimate-case-check-sends-back-a-clash-with-another-case` — its method `-k session_clash` stands (it was set by 629.1)
> **＋** `tests/test_casecheck.py` — the tests named `test_subagent_clash_` and `test_subagent_session_clash_`
> **＋** `rule-case-check` — the check of the answer of `case-guppi`

> **when:**
> Someone takes the reading of `estimate-case-check-sends-back-a-case-number-held-by-another-agent` by its method, `uv run pytest tests/test_casecheck.py -k subagent_clash`.

> **then:**
> pytest runs each test of `tests/test_casecheck.py` whose name holds `subagent_clash`: the tests of a Case number that another agent holds.
> **－** It runs no test whose name holds `session_clash`, the tests of `estimate-case-check-sends-back-a-clash-with-another-case`.

```then
update:
- slug: estimate-case-check-sends-back-a-case-number-held-by-another-agent
  set:
    method: uv run pytest tests/test_casecheck.py -k subagent_clash, then by hand an answer of case-guppi the hook sends back for this reason
  change: the method selects -k subagent_clash, so that the tests of session_clash are not run (case 632.8)
```

```tasks
- [ ] update `estimate-case-check-sends-back-a-case-number-held-by-another-agent`
```

### Case 632.9 — The schema check of Insights drops its word-for-word claim

> **given:**
> `estimate-insights-schema-checked` — its Criterion replaced whole; its `purpose` and `method` stand (it follows 627.2)
> **＋** `rule-insights-schema` — the Render of `vault/wiki/insights/schema.yaml`, whose Threshold and `status` row 627.2 changed
> **＋** `vault/wiki/insights/schema.yaml` and `vault/wiki/insights/` — the file lint reads, and the Insight pages
> **＋** `vault/wiki/insights/schema.md` — the old file, gone
> **＋** `tests/test_schemas.py` — the tests of the schemas

> **when:**
> `uv run guppi render` writes `vault/wiki/insights/schema.yaml` from `rule-insights-schema`, and `uv run guppi lint` reads a page of `vault/wiki/insights/` by the keys of that file.

> **then:**
> `vault/wiki/insights/schema.yaml` equals the Render of `rule-insights-schema`.
> **＋** Lint reads from it: required `type, pattern, status, children, severity, origin, sprint, created, tags`; optional `addressed_by, deferred_by`; values `status: open | actioned | archived`; single `addressed_by`; conditional — `actioned` requires `addressed_by`; `computed: [severity]`; the sections `## Pattern` and `## History` required, `## Proposal` optional.
> **＋** An Insight page with these fields, values and sections has no `schema` finding. A page that lacks a required field, holds a value outside the list, misses a conditional or lacks a required section has one finding per defect.
> **＋** `description` holds the introduction, the Threshold, Reopening and the Slug; `fields` and `sections` describe each name of these lists; `examples` holds the example page.
> **＋** `fields.addressed_by` names one decision, the latest; a list is not its shape.
> **－** `vault/wiki/insights/schema.md` does not exist.

```then
update:
- slug: estimate-insights-schema-checked
  set:
    status: pending
  change: the Criterion replaced whole — the prose stands as data, with no claim that it is word for word the old schema.md (case 632.9)
```

```tasks
- [ ] update `estimate-insights-schema-checked`
- [ ] read `estimate-insights-schema-checked`
```

### Case 632.10 — The question after a clash and the question on a finding not closed take the grill-me shape

> **given:**
> `estimate-orchestration-asks-in-the-grill-me-shape` — its Criterion replaced whole, its `purpose` set anew (it follows 629.1 and 634.2)
> **＋** `rule-orchestration` — what the main agent does, rendered into `vault/wiki/orchestration.md`; its list of the main agent's own questions gains two questions
> **＋** `vault/raw/2026-10-04/2041/cases/case-634.md` — Case 634: 634.2 adds the question whether a finding not closed is fixed or left, and 634.3 rewords another sentence of `rule-orchestration`
> **＋** `rule-prespec` — the loop after the findings, where `ask-guppi` confirms its findings
> **＋** `.claude/skills/grill-me/SKILL.md` — the question shape
> **＋** `rule-spec-capture` — the choice between `/work` and `/carry`
> **＋** `case-guppi`, `ask-guppi`, `/pre-spec`, `/hi`, `/work` and `/carry` — the agents, and the moments of the main agent's own questions

> **when:**
> The main agent puts a question to the person itself, outside a round of `case-guppi`. The question is one of these:
> - a decision it needs in the report of `/pre-spec`;
> - a question at `/hi`;
> - a question at a stop of Work Mode;
> - the question whether another Case of the session is built again after a Case was bounded around a clash with it;
> - at `/pre-spec`, after the `ask-guppi` runs confirm their findings, the question whether each finding not closed is fixed or left.
>
> This is with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> Each such question takes the question shape of `.claude/skills/grill-me/SKILL.md`: its numbered `❓ **Qn** - **<title>**:` line, one `**Now:**` line, the label `**Options:**`, each option on a `🔹` line with one `**After:**` item, and the `➡️` line with the recommended answer.
> **＋** It stands in Russian, and its labels may stand translated.
> **－** The question which Frontier item is next, the question of an open `A` line at `/hi` — the Estimate by slug and its question —, the question that asks for the sign-off of a shown Case, and the choice between `/work` and `/carry` of `rule-spec-capture` keep their own form.

```then
update:
- slug: rule-orchestration
  replace:
  - old: a question at `/hi`, a question at a stop of Work Mode — takes the question shape
    new: a question at `/hi`, a question at a stop of Work Mode, the question whether another Case is built again after a clash (case 629.1), the question at `/pre-spec` whether each finding of `ask-guppi` not closed is fixed or left (`rule-prespec`, case 634.2) — takes the question shape
  change: the question after a clash and the question on a finding not closed are among the main agent's own questions in the grill-me shape (case 632.10)
- slug: estimate-orchestration-asks-in-the-grill-me-shape
  set:
    status: pending
    purpose: Whether each question the main agent puts to the person itself, at pre-spec, at /hi, at a stop of Work Mode, after a clash on whether another Case is built again, or at pre-spec on whether a finding of ask-guppi not closed is fixed or left, takes the question shape of grill-me, the exceptions kept in their own form
  change: the Criterion replaced whole — the When names the question after a clash and the question on a finding not closed (case 632.10)
```

```tasks
- [ ] update `rule-orchestration`
- [ ] update `estimate-orchestration-asks-in-the-grill-me-shape`
- [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
- [ ] read `estimate-orchestration-asks-in-the-grill-me-shape`
```

## Case 633 — ask-guppi at /pre-spec: a fixed frame around the findings, and its searches checked apart

> **context:**
> `ask-guppi` is the read-only helper agent that the main agent sends once, at the first `/pre-spec` of a session, to find Cases that clash with the vault or with each other. Its frame, `.claude/agents/ask-guppi.md` rendered from `rule-ask`, tells it to answer the three questions of `/pre-spec` with one numbered list of findings under each. `estimate-ask-finds` checks that answer. Its Criterion lets nothing reach the caller beyond the findings and a list of paths. It also reads the order of searches (the Grep of the rules first, then one Grep per other category) as the whole of the searching. The Estimate failed at the /hi of 1934 (raw/2026-10-04/1934/ledger.md L1), as it failed before (raw/2026-10-01/1441/ledger.md L33, raw/2026-10-04/0004/ledger.md L17). The dispatch it read, at the /pre-spec of 1439, gave the three lists in order, and each finding was sound. But the answer opened with a heading and a summary, closed with a paragraph on what the vault bears out and a "Not checked" list, and ran several Greps per category. I read the dispatch at the /pre-spec of 1934 (agent a6d84c6b7ce6994bf) against the same Criterion. It does the same things. It opens with a paragraph on which Spec it read and which Cases. After the findings it gives the facts that hold, a "Not done" list and a list of pages. It runs about twenty Greps after the category Greps, several of them to count again what a `context` states. It also says that three of these Greps covered `vault/wiki/decisions/`, which the frame forbids except for two reasons. Part of the extra text is what `CLAUDE.md` asks of every answer: say what is done and what is not done. Part of the extra searching is what the third question of `/pre-spec` needs, since a count can only be checked by running its search again.
>
> The person chose a fixed frame around the lists. One line before them names what was read. After them stands one list of what was not checked, then the paths. A summary and a list of what holds stay out. The person chose free Greps and Reads after the fixed start, to check a finding at `/pre-spec`. On Decision pages the person ruled that a count over them is not checked again: each Decision page states its own at its moment, and reading them again would mean editing history. So a count whose search covers `vault/wiki/decisions/` is not run again and is no finding. The ban of the frame on Decision pages stands. The person chose two sub-cases. 633.1 replaces the Criterion of `estimate-ask-finds` with the form of the answer alone, and sets its `purpose` and `method` anew, since both state the old promise. 633.2 moves the line on searches into a new Estimate, `estimate-ask-searches-at-prespec`. A Glob of `vault/**/estimate-ask-searches*.md` printed nothing, so the slug is free. The new Estimate has `ref: rule-ask`, so the vault query was not run. Each sub-case adds its sentence to a different passage of the Render, so the two `replace` anchors do not overlap.
>
> The check of this answer noted that five lines of the old Criterion of `estimate-ask-finds` are not carried word for word. That is on purpose, and each line has a new place:
> - The line that the answer opens with the lists now follows the new opening line on what was read.
> - The line on a list of paths that may stand after the findings becomes the line on a list of what was not checked, then the paths.
> - The line on the Grep of the rules moves to `estimate-ask-searches-at-prespec`, word for word.
> - The line that nothing reaches the caller beyond the findings and the paths becomes the line that refuses a summary, a list of what holds, an index line and page text.
> - The line that an answer with no list after the findings holds the promise narrows to an answer with no list of paths, since the list of what was not checked is now required.
>
> The check also noted that a `then` line of 633.2 on `vault/wiki/decisions/` shares words with the line of 633.1 on the `## Problem` of a deferring Decision. That is on purpose. 633.1 checks that the Problem stands in the finding, and 633.2 checks that the searches over the Decision pages go no further than that Problem.
>
> Frame checks. The moment this Case sets is the answer of `ask-guppi` at `/pre-spec`. A Grep of `ask-guppi` over `.claude/` printed 4 files: `.claude/agents/ask-guppi.md`, `.claude/agents/case-guppi.md`, `.claude/skills/pre-spec/SKILL.md` and `.claude/skills/hi/SKILL.md`. A Grep of `ask-guppi` over `vault/wiki/rules/`, leaving out `rule-ask.md`, printed 7 files: `rule-case-protocol.md`, `rule-case-build.md`, `rule-orchestration.md`, `rule-prespec.md`, `schema.yaml`, `rule-skill-hi.md` and `rule-rules-schema.md`. The hits in `rule-case-protocol.md` and the History hits in `rule-prespec.md` are History lines and were not read. None of the hits I read sets the form of the agent's answer or its searches at `/pre-spec`:
> - `rule-prespec` and its skill set what the main agent sends and its own report;
> - `rule-orchestration` sets only that `ask-guppi` asks at `/pre-spec`;
> - `rule-case-build` and `case-guppi.md` have `case-guppi` run the query itself;
> - `schema.yaml` and `rule-rules-schema` say that `ask-guppi` reaches a deferred Decision through `deferred_by`;
> - `rule-skill-hi` says the near lines of the Frontier need no `ask-guppi`.
>
> Each stays true. A Grep of `ask-guppi` over `vault/wiki/estimates/` printed 10 files. Two of them are the Estimates of `rule-ask`. The other eight are `estimate-case-build-writes-the-case`, `estimate-case-build-checks-the-finished-case`, `estimate-hi-takes-a-conserved-spec`, `estimate-hi-writes-frontier`, `estimate-internal-context-loaded`, `estimate-orchestration-shows-the-built-case`, `estimate-orchestration-puts-the-harness-before-plan-mode` and `estimate-prespec-reconciles`. Each speaks of when `ask-guppi` is sent or of the query of `case-guppi`, not of the form of the answer or the searches at `/pre-spec`, so their Criteria stand. `estimate-case-build-checks-the-finished-case` has `case-guppi` leave the Decision pages out of its own searches, which agrees with the person's ruling. `estimate-ask-query-before-a-create` checks the query that `case-guppi` runs before a `create`. The new sentence of 633.2 holds only at `/pre-spec`, so that Criterion stands. A Grep of `ask-guppi` over `guppi/` printed nothing, so no code judges the answer. The caller's prompt says Case 632 changes none of these pages, and it sets nothing about this answer, so its file was not read. The open Frontier item C4, on how `/pre-spec` checks a Spec beyond one run of `ask-guppi`, is left to its own Case. `rule-prespec` does not change here.

> **problem:**
> The frame of `ask-guppi` sets the three lists of `/pre-spec` and nothing around them. `estimate-ask-finds` refuses every word beyond the lists and the paths, and it reads the order of searches as a limit. Each run adds what `CLAUDE.md` and the third question need: what was read, what was not checked, and searches that check a count. The check fails each time on text and searches that are useful. The question is what may stand around the lists, how freely the agent searches at `/pre-spec`, and how each is checked.

> **recommend:**
> - **What may stand around the three lists**
>   - Recommended: (b) a fixed frame: one line before the first list that names what was read, and after the findings one list of what was not checked, then the paths; no summary and no list of what holds.
>   - Answer: agreed with the recommendation, (b).
> - **How freely the agent searches at /pre-spec**
>   - Recommended: (a) the fixed start stays, the Grep of the rules and one Grep per category; after them, more Greps and Reads are allowed to check a finding, and the frame gains one sentence that says so.
>   - Answer: agreed with the recommendation, (a).
> - **A count check that reaches the Decision pages**
>   - Recommended: (a) a search that runs again a count stated in a Case may cover `vault/wiki/decisions/`, file names and counts only, no Decision page opened.
>   - Answer: not as recommended. Other Decision pages are not counted again: that is extra context and needs no fixing. Each Decision page states its own at its moment, and reading them again would mean editing history all the time.
> - **One promise or two**
>   - Recommended: (a) two sub-cases: `estimate-ask-finds` keeps the form of the answer alone, and a new Estimate checks the searches at `/pre-spec`; both are read from the same transcript.
>   - Answer: agreed with the recommendation, (a).

### Case 633.1 — ask-guppi frames its findings at /pre-spec with one line on what it read and a list of what it did not check

> **given:**
> `rule-ask` — its Render is the text of `.claude/agents/ask-guppi.md`; the paragraph on `/pre-spec` changes
> **＋** `.claude/agents/ask-guppi.md` — the agent rendered from `rule-ask`
> **＋** `estimate-ask-finds` — the check whose Criterion is replaced whole and whose `purpose` and `method` are set anew
> **＋** `CLAUDE.md` — asks every answer to say what is done and what is not done; unchanged
> **＋** `.claude/skills/pre-spec/SKILL.md` — sends `ask-guppi` the plan file and the three questions; unchanged
> **＋** `vault/raw/<date>/event_log.md` — records each dispatch

> **when:**
> At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> The answer opens with one line that names what the agent read: the plan file, or the Spec that the plan's title line names, and the Cases it checked.
> **＋** Then stands one numbered list of findings under each question of `.claude/skills/pre-spec/SKILL.md`, in its order: what contradicts a page, a rule or another Case; an Estimate a Case does not name that speaks of the thing the Case changes; a fact of a `context` the vault does not bear out.
> **＋** Each finding names its Case and the page or the Cases it bears on; a question with no finding says "none".
> **＋** A finding that names a page carrying `deferred_by` gives the `## Problem` of the Decision that field names.
> **＋** After the findings stands one list of what the questions ask that the agent did not check, "none" when it checked all of it, and then a list of the paths of the files it read.
> **＋** The dispatch stands in `vault/raw/<date>/event_log.md`.
> **－** The findings are not put under the lines `exists`, `near`, `missing`, `rules` and tags/slug: those lines answer a question whether a thing exists.
> **－** No summary of the findings, no list of what holds, no index line and no page text reaches the caller.
> **－** An answer with no list of paths holds the promise as well.

```then
update:
- slug: rule-ask
  replace:
  - old: and a question with no finding says "none" (case 626.1).
    new: 'and a question with no finding says "none" (case 626.1). One line before the first list names what you read: the plan file, or the Spec its title line names, and the Cases you checked. After the findings stand one list of what the questions ask that you did not check, "none" when you checked all of it, and then the list of the paths of the files you read; no summary of the findings and no list of what holds (case 633.1).'
  change: ask-guppi frames its findings at /pre-spec with one line on what it read and, after them, a list of what it did not check before the paths; no summary, no list of what holds (case 633.1)
- slug: estimate-ask-finds
  set:
    status: pending
    purpose: Whether ask-guppi answers the questions of /pre-spec with one line on what it read, one numbered list of findings under each question, each finding naming its Case and the page or Cases it bears on, then a list of what it did not check and a list of the paths of the files it read, and nothing else
    method: 'by hand at the /hi of a later session: the answer of ask-guppi at a /pre-spec after the render of .claude/agents/ask-guppi.md by case 633.1, read in its agent transcript against the event log, recorded in the estimate line'
  change: the Criterion replaced whole — one line on what was read before the findings, a list of what was not checked after them and before the paths, no summary and no list of what holds; the line on the searches moved to estimate-ask-searches-at-prespec (case 633.1)
```

```tasks
- [ ] update `rule-ask`
- [ ] update `estimate-ask-finds`
- [ ] `uv run guppi render`: `.claude/agents/ask-guppi.md`
- [ ] read `estimate-ask-finds`
```

### Case 633.2 — ask-guppi searches as a finding needs at /pre-spec and leaves the Decision pages out of a count

> **given:**
> `rule-ask` — its Render is the text of `.claude/agents/ask-guppi.md`; the paragraph on the Greps changes
> **＋** `.claude/agents/ask-guppi.md` — the agent rendered from `rule-ask`
> **＋** `.claude/skills/pre-spec/SKILL.md` — the skill `/pre-spec`, whose first run sends `ask-guppi` the plan file and the three questions; unchanged
> **＋** `estimate-ask-searches-at-prespec` — the new Estimate
> **＋** `estimate-ask-query-before-a-create` — checks the searches of the query `case-guppi` runs before a `create`; unchanged
> **＋** `vault/wiki/rules/` — the rule pages the agent greps first
> **＋** `vault/wiki/decisions/` — the Decision pages, searched only for the two reasons the frame names

> **when:**
> At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> The agent starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs one Grep per other category the question touches.
> **＋** After those Greps it runs further Greps and Reads as a finding needs, including the search behind a count that a `context` states.
> **＋** A count of a `context` whose search covers `vault/wiki/decisions/` is not run again and is no finding.
> **－** No Grep or Read of the agent reaches `vault/wiki/decisions/`, except for the `## Problem` of a Decision that a `deferred_by` names and a Decision reached through a page's `origin` when the question asks why something was decided.

```then
create:
- slug: estimate-ask-searches-at-prespec
  type: estimate
  ref: rule-ask
  kind: QA
  purpose: Whether ask-guppi at /pre-spec starts with the Grep of the rules and one Grep per other category, then greps and reads as each finding needs, and leaves vault/wiki/decisions/ out of every search but the two reasons its frame names, a count over Decision pages not run again
  method: 'by hand at the /hi of a later session: the Grep, Glob and Read calls of ask-guppi at a /pre-spec after the render of .claude/agents/ask-guppi.md by case 633.2, read in its agent transcript against the Criterion, recorded in the estimate line'
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-ask
  replace:
  - old: When the question is about a check, reach the Estimates
    new: At `/pre-spec`, after these Greps, Grep and Read as each finding needs, including the search behind a count that a `context` states; a count whose search covers `vault/wiki/decisions/` is not run again and is no finding, since a Decision page states its own at its moment (case 633.2). When the question is about a check, reach the Estimates
  change: at /pre-spec ask-guppi greps and reads as each finding needs after the index Greps; a count over vault/wiki/decisions/ is not run again (case 633.2)
```

```tasks
- [ ] update `rule-ask`
- [ ] create `estimate-ask-searches-at-prespec`
- [ ] `uv run guppi render`: `.claude/agents/ask-guppi.md`
- [ ] read `estimate-ask-searches-at-prespec`
```

## Case 634 — /pre-spec checks each Case in its own ask-guppi run, and the same runs confirm their findings once

> **context:**
> At the first `/pre-spec` of a session, the main agent sends the read-only agent `ask-guppi` once over the whole plan, and the report then treats its answer as the check of the whole Spec. A Case rebuilt on a finding is checked only by the `case-guppi` that rebuilt it (case 561.1). One model run over twenty-odd sub-cases returns a sample of the findings, not all of them. `lesson-prespec-one-ask-guppi-run-samples-the-spec` records an example. The conserved Spec of session 1439 got ten findings at its own `/pre-spec`, and twelve at the `/pre-spec` of 1934. The lesson places eleven of the twelve:
> - eight on sub-cases that the first run had read and passed;
> - two on sub-cases written from that run's findings after it;
> - one on the fix of one of its findings.
>
> It places no twelfth, and this Case leaves that one unplaced. The lesson is clustered under `insight-prespec-after-findings-loop-unruled`, which is open again. Its `addressed_by` is `decision-case-561.1`. In that decision the person accepted the risk of a single run and asked for another option to be named (Case 561.4).
>
> The person chose these changes. The first `/pre-spec` sends one `ask-guppi` per top-level Case, all in one message. Each run judges its own Case and that Case's sub-cases, and reads the other Cases only to find a clash. The report names, for each run, the Case it judged and the list of what it did not check. That list is the one Case 633.1 adds to the answer of `ask-guppi`. The report never says the whole Spec is checked. The person asked whether a rebuilt Case would go to a new run. The person ruled a new run out, because a fresh agent always finds something and the checks would never end. The person chose that the same `ask-guppi` confirms its own findings once, with no new search and a fixed end. The confirmation comes after every `case-guppi` has answered and before the rebuilt Cases are shown. That way each rebuilt Case is ratified once, and the hook of `rule-prespec-onward` does not change. Its text in `guppi/onward.py` sends the agent on to the check and the exit after that ratification, which stays true. The person chose three sub-cases. 634.1 replaces the Criterion of `estimate-prespec-reconciles`, which has no `purpose`, and whose `method` names one reading by hand and does not state the old promise. 634.2 creates `estimate-prespec-confirms-the-findings-once`. A Glob of `vault/**/estimate-prespec-confirms*.md` printed nothing, so the slug is free. It has `ref: rule-prespec`, so the vault query was not run. 634.3 rewords the sentence of `rule-orchestration` that says `ask-guppi` is sent once, and replaces the Criterion of `estimate-orchestration-shows-the-built-case`. That Criterion says the same thing, and also says no `ask-guppi` comes before a showing, while the confirmation now comes before the showing of the rebuilt Cases. The `purpose` and `method` of that Estimate do not state the old promise, so they stand.
>
> The `/pre-spec` of session 2041 found six points in this Case, and each is fixed here:
> - A session that takes a conserved Spec has a plan file with only its title line, as `rule-skill-hi` sets it. So in that session the runs go one per top-level Case of the Spec that the title line names, as the opening line of 633.1 already expects.
> - The result of the confirmation stands in the main agent's own text after the horizontal rule. The `Stop` check of `rule-case-check` judges no text there (`estimate-case-check-refuses-text-outside-the-list`), so that Estimate already checks it and its Criterion stands. The list item of a Case keeps the form `orchestration.md` sets.
> - The question to fix or leave a finding comes after the confirmation, not in the report, since step 1 of the loop ties a question of the report to the time before any Case is sent back. Case 632.10, built again in parallel, adds that question to the list of the main agent's own questions in `rule-orchestration` and to `estimate-orchestration-asks-in-the-grill-me-shape`, so this Case touches neither.
> - The confirmation runs no Grep. The frame of `rule-ask` opens with the Grep of the rules for every question, so that sentence now leaves out the confirmation.
> - `estimate-case-build-checks-the-finished-case` reads its count from "the report of ask-guppi". 634.1 sets its `method` on the answers of the runs, one per top-level Case. Its Criterion reads only the index lines of the recipe of `ask-guppi`, not the runs, so it stands. Its `purpose`, counted by what `ask-guppi` still finds at `/pre-spec`, stays true.
> - The count of the lesson is stated above.
>
> The frame. Case 633 of this session changes `rule-ask` on the answer of `ask-guppi` at `/pre-spec`. No anchor of 634.1 or 634.2 in `rule-ask` touches text that 633 replaces or adds. The new paragraph of 634.2 stands after the five-line form of the answer, just before the paragraph on `/pre-spec`. Case 632 changes other sentences of `rule-orchestration`, so the anchor of 634.3 does not overlap them. `estimate-ask-finds`, as 633.1 replaces it, checks the answer of a run sent with the plan file and the questions. Each run per Case still is one, and it names the Cases it checked, so its Criterion stands. `estimate-prespec-gathers-the-answers-after-findings` stands: each of its lines stays true with the confirmation before the showing, and the showing in one reply stays. The batch of `rule-orchestration` lists the loop steps it takes, and it sends no Case on a finding of `ask-guppi`, so the new step does not reach it. The Purpose of `rule-prespec` says its question is asked once. That stays true, since the first run asks it once, split across the Cases.
>
> The check of this answer noted lines of the replaced Criteria that are not carried word for word. That is on purpose:
> - In 634.1, the When also names the render of `.claude/agents/ask-guppi.md`. The line on the check names the command as `uv run guppi prespec --check`. The line on the Frontier names its file and the session's ledger. The line on the dispatch gives one run per top-level Case of the plan, or of the conserved Spec that its title line names. The line on the report opens with what each run covered.
> - In 634.3, the line on `ask-guppi` drops the words that no `ask-guppi` comes before a showing, since the confirmation does.
>
> The check also noted that some `then` lines of 634.3 share words with lines of its siblings. Each pair speaks of a different promise, so each line stays in its own sub-case:
> - The line of 634.3 on how any built Case is shown sets the file, the list and the `ratification` of every showing. The line of 634.2 on the Cases built again sets only that they come in one reply after the confirmation, with its result after the horizontal rule.
> - The line of 634.3 on a ratified Case that changes, and the line of 634.1 on a finding in a Case, speak of different triggers.
> - The line of 634.3 on the showing, and the line of 634.1 that the agent writes no list of the decisions, speak of different replies.
>
> The searches this Case rests on:
> - A Grep of `ask-guppi.{0,80}once|once.{0,80}ask-guppi|asks once` over the repository, leaving out `vault/raw/`, `vault/archive/` and `vault/wiki/decisions/`, printed 11 files. Each is placed below:
>   - `.claude/skills/pre-spec/SKILL.md`, `.claude/agents/ask-guppi.md`, `vault/wiki/orchestration.md`, `rule-prespec.md`, `rule-ask.md`, `rule-orchestration.md`, `estimate-prespec-reconciles.md` and `estimate-orchestration-shows-the-built-case.md` enter the Case.
>   - `rule-index-check.md` speaks of the vault query of `case-guppi` and stands.
>   - `lesson-prespec-one-ask-guppi-run-samples-the-spec.md` records the error and stands.
>   - `tests/test_generate.py` holds a made-up page and stands.
>   - The other hits in the two Estimates are their `## Result` lines, a record that stands.
> - A Grep of `ask-guppi` over `vault/wiki/estimates/` printed 10 files: `estimate-ask-query-before-a-create`, `estimate-ask-finds`, `estimate-case-build-checks-the-finished-case`, `estimate-case-build-writes-the-case`, `estimate-hi-writes-frontier`, `estimate-hi-takes-a-conserved-spec`, `estimate-internal-context-loaded`, `estimate-orchestration-shows-the-built-case`, `estimate-orchestration-puts-the-harness-before-plan-mode` and `estimate-prespec-reconciles`. Three of them enter the Case. The others speak of the query of `case-guppi`, of the `- near` lines of `/hi`, of a conserved Spec, of what a subagent loads, or of `ask-guppi` asking at `/pre-spec`. Each stays true.
> - A Grep of `ask-guppi|ask_guppi` over `guppi/` printed nothing, so no code judges the dispatch.
> - A Grep of `ask-guppi` over `vault/wiki/rules/rule-case-protocol.md` printed two History lines, which were not read.
> - A Grep of `Waiting|bold label` over `vault/wiki/rules/`, `.claude/` and `guppi/` printed `.claude/skills/pre-spec/SKILL.md`, `rule-prespec.md`, `rule-orchestration.md` and `guppi/casecheck.py`. In `casecheck.py`, `round_opening` judges only a reply that shows a round of `case-guppi`, and an answer of `ask-guppi` is no round. So the new step waits as step 3 sets it.
>
> Not done:
> - A sub-case born of a finding is read by the confirmation only as far as the finding goes. The person accepted that a new error a fix brings in can show itself later.
> - No mark is written on `insight-prespec-after-findings-loop-unruled` or on its lesson. The lesson is of another session, and the librarian's run judges the Insight.

> **problem:**
> `/pre-spec` sends one `ask-guppi` over the whole plan and takes its answer as the check of the whole Spec, though one run returns only a sample of the findings. A Case rebuilt on a finding reaches the approved Spec read only by the agent that rebuilt it. The question is how the first check covers each Case, how a rebuilt Case is confirmed without a loop of checks that never ends, and what the report says about how much was checked.

> **recommend:**
> - **How the first check covers the whole plan**
>   - Recommended: (a) one `ask-guppi` run per top-level Case, all at once; each judges its own Case and its sub-cases and reads the others only to find a clash; no run is repeated.
>   - Answer: agreed with the recommendation, (a).
> - **How a rebuilt Case is read against the vault**
>   - Recommended: (b) one more `ask-guppi` run over the rebuilt Cases only, announced to the person before it starts.
>   - Answer: not answered. The person asked whether this meant the same `ask-guppi` or a new one, and said a new one is bad: an agent always finds an error, so the checks would never end, and the real question is how many checks are enough, a small point missed being acceptable. Replaced by **How many checks a rebuilt Case gets**.
> - **What the report says about how much was checked**
>   - Recommended: (a) the report names which Cases each run read and repeats each run's list of what it did not check, and never says the Spec is checked as a whole.
>   - Answer: agreed with the recommendation, (a).
> - **How many checks a rebuilt Case gets**
>   - Recommended: (b) the same `ask-guppi` confirms its own findings once: no new search and no new question; a finding not closed goes to the person as one question, fix or leave; the loop ends there.
>   - Answer: agreed with the recommendation, (b).
> - **When the found errors are confirmed as fixed**
>   - Recommended: (a) before the rebuilt Cases are shown, so that each is ratified once, already confirmed, and no hook changes.
>   - Answer: agreed with the recommendation, (a).
> - **How the Case is cut and checked**
>   - Recommended: (a) three sub-cases: the runs per Case with the coverage of the report, replacing the Criterion of `estimate-prespec-reconciles`; the confirmation, with a new Estimate; the sentence of `rule-orchestration`, replacing the Criterion of `estimate-orchestration-shows-the-built-case`.
>   - Answer: agreed with the recommendation, (a).
> - **Change**
>   - Asked: the `/pre-spec` of session 2041 found six points in this Case, and no question was put to the person on them.
>   - Taken: the runs follow the conserved Spec that the plan's title line names; the result of the confirmation stands after the horizontal rule; the question to fix or leave is a question after the confirmation; the confirmation runs no Grep, and the opening sentence of the frame of `rule-ask` leaves it out; the `method` of `estimate-case-build-checks-the-finished-case` reads the answers of the runs; the count of the lesson is stated with one finding unplaced.

### Case 634.1 — The first /pre-spec sends one ask-guppi per top-level Case, and the report names what each run covered

> **given:**
> `rule-prespec` and `.claude/skills/pre-spec/SKILL.md` — the skill and its render; the dispatch sentence and the opening of the report change
> **＋** `rule-ask` and `.claude/agents/ask-guppi.md` — the frame of the agent and its render; its Purpose, its description and its paragraph on `/pre-spec` change
> **＋** `estimate-prespec-reconciles` — its Criterion replaced whole
> **＋** `estimate-case-build-checks-the-finished-case` — its `method` set anew; its Criterion and `purpose` stand
> **＋** `guppi/prespec.py`, `vault/raw/<date>/<hi HHMM>/frontier.md` and the session's ledger — the check `uv run guppi prespec --check`, what it reads, and the `prespec` line that `guppi gate` writes; unchanged
> **＋** `case-guppi` and the hook of `rule-spec-write` — rebuild a Case on a finding and write it into the plan; unchanged
> **＋** `estimate-ask-finds` and `vault/raw/2026-10-04/2041/cases/case-633.md` — the answer of a run at `/pre-spec`, its list of what it did not check, as Case 633 sets it; unchanged here
> **＋** `rule-skill-hi` — sets the title line of the plan file of a session that takes a conserved Spec

> **when:**
> The person invokes `/pre-spec`, or the agent calls the skill, before the Spec is approved, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec` and `.claude/agents/ask-guppi.md` rendered from `rule-ask`.

> **then:**
> The agent runs `uv run guppi prespec --check` on the plan file with `--session <id>`, the eight-character id of the `hi:` line, and reads the first line of the output before the exit code — "no hi recorded for session …; nothing checked" means the wrong value; nothing is translated before the run.
> **＋** A finding in a Case — in its prose or in its body, a wrong fact of its `context` included — goes to the `case-guppi` of that Case by `SendMessage`; its new answer is shown and ratified again, and the hook of `rule-spec-write` writes it into the plan; the agent does not edit the text of a Case in the plan file.
> **＋** A finding in `vault/raw/<date>/<hi HHMM>/frontier.md` or in a line of the session's ledger is fixed there, and the command runs again until it prints no finding.
> **＋** At the first run of `/pre-spec` in the session, one `ask-guppi` is dispatched for each top-level Case outside `## Deferred` — of the plan, or of the conserved Spec that the plan's title line names, as `rule-skill-hi` sets that line — all in one message, each with the absolute path of the plan file, the id of the Case it judges and the instruction to read every Case outside `## Deferred` — `context`, `when`, `then`, the `then` block — and, for an `update` of a rule or an entity, the page's `estimates`; each run judges its own Case and its sub-cases and reads the other Cases only to find a clash with them; of a Case under `## Deferred` it reads only the slugs of its `defer` items; a later run of `/pre-spec` in the session dispatches no `ask-guppi`.
> **＋** Three questions: which decisions contradict a page of the vault, a rule of the vault, or each other; whether an Estimate the Case does not name speaks of the thing the Case changes; which fact of a `context` — a page's status, a count, a case number, a claim that no page holds a thing — the vault does not bear out.
> **＋** The agent answers the findings with one report before any Case is sent back: for each `ask-guppi` run, the Case it judged and its list of what it did not check; each finding numbered, with the fix it proposes or why it is already known, the findings that need the person apart from those that do not, and the decisions it needs from the person; after the Cases built again on the findings are ratified, it does not call `/pre-spec` again, but runs the check, fixes what it prints, and exits Plan Mode when the check prints no finding.
> **＋** `guppi gate` writes the stamped `prespec` line on the Skill call.
> **－** The report never says that the whole Spec is checked.
> **－** The agent writes no list of the decisions: the plan is the list.
> **－** The body of a deferred decision is not read; a Case that changes a page another Case of the plan defers is still a finding.

```then
update:
- slug: rule-prespec
  replace:
  - old: dispatch the `ask-guppi` agent once with the absolute path of the plan file and the instruction to read
    new: dispatch one `ask-guppi` agent for each top-level Case outside the `## Deferred` heading — of the plan, or, when the plan's title line names a conserved Spec, of that Spec — all in one message, each with the absolute path of the plan file, the id of the Case it judges — that Case and its sub-cases, the other Cases read only to find a clash with them (case 634.1) — and the instruction to read
  - old: 'Answer the findings with one report before any Case is sent back:'
    new: 'Answer the findings with one report before any Case is sent back: for each `ask-guppi` run, the Case it judged and its list of what it did not check, with no claim that the whole Spec is checked (case 634.1);'
  change: the first run of /pre-spec sends one ask-guppi per top-level Case of the plan or of the conserved Spec its title line names, all at once; the report names the Case each run judged and what it did not check, never the whole Spec as checked (case 634.1)
- slug: rule-ask
  replace:
  - old: The main agent asks once, at pre-spec, for the set of ratified Cases;
    new: The main agent asks at pre-spec, one run for each top-level Case of the set of ratified Cases (case 634.1);
  - old: the main agent asks once at pre-spec for the whole set;
    new: the main agent asks at pre-spec, one run per top-level Case of the set;
  - old: At `/pre-spec`, where the caller asks which Case of the plan contradicts
    new: At `/pre-spec`, where the caller names the Case you judge — that Case and its sub-cases, the other Cases of the plan read only to find a clash with them (case 634.1) — and asks which Case of the plan contradicts
  change: at pre-spec each ask-guppi run judges the top-level Case the caller names and reads the other Cases only for a clash (case 634.1)
- slug: estimate-prespec-reconciles
  set:
    status: pending
  change: the Criterion replaced whole — one ask-guppi per top-level Case at the first run, of the plan or of the conserved Spec its title line names, the report naming what each run judged and did not check (case 634.1)
- slug: estimate-case-build-checks-the-finished-case
  set:
    method: 'by hand: at /pre-spec of a later session after the render, the answers of the ask-guppi runs, one per top-level Case, read for each Case case-guppi built — a Case that departs from a chosen option, a page naming a changed slug that the Case misses, a rule acting at the same moment that the Case misses, a Case of the session named in the prompt whose page or moment the Case clashes with, an Estimate whose purpose or method still states the promise its replaced Criterion dropped, a claim of context that its search did not print, a search in context that the Case does not rest on, two sub-cases whose texts on one page contradict; the count of each in the reading line'
  change: the method reads the answers of the ask-guppi runs, one per top-level Case (case 634.1)
```

```tasks
- [ ] update `rule-prespec`
- [ ] update `rule-ask`
- [ ] update `estimate-prespec-reconciles`
- [ ] update `estimate-case-build-checks-the-finished-case`
- [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [ ] `uv run guppi render`: `.claude/agents/ask-guppi.md`
- [ ] read `estimate-prespec-reconciles`
```

### Case 634.2 — The ask-guppi runs confirm their own findings once, before the Cases built again are shown

> **given:**
> `rule-prespec` and `.claude/skills/pre-spec/SKILL.md` — the skill and its render; the sentence on a later run and a step of the loop after the findings change
> **＋** `rule-ask` and `.claude/agents/ask-guppi.md` — the frame of the agent and its render; its opening sentence on the Grep of the rules changes, and a form of answer to the confirmation is added
> **＋** `vault/raw/2026-10-04/2041/cases/case-633.md` — Case 633 changes the paragraph of `rule-ask` on `/pre-spec`, before which the new paragraph stands
> **＋** `vault/raw/2026-10-04/2041/cases/case-632.md` — Case 632.10 puts the question after the confirmation into the list of the main agent's own questions in `rule-orchestration`
> **＋** `estimate-prespec-confirms-the-findings-once` — the new Estimate
> **＋** `rule-prespec-onward` and `guppi/onward.py` — after the ratification of the Cases built again, the hook sends the agent to the check and the exit; unchanged
> **＋** `rule-case-check` — its `Stop` check judges no text after the horizontal rule, as `estimate-case-check-refuses-text-outside-the-list` checks; unchanged
> **＋** `case-guppi` and `.claude/skills/grill-me/SKILL.md` — rebuild a Case on a finding, and the shape of the question after the confirmation

> **when:**
> `/pre-spec` has reported findings that sent Cases of the plan back, and every `case-guppi` that got a finding has answered with its Case built again, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec` and `.claude/agents/ask-guppi.md` rendered from `rule-ask`.

> **then:**
> The main agent sends each `ask-guppi` run whose findings sent a Case back the Cases built again on them, by `SendMessage`, all in one message, and asks whether each of its findings is closed.
> **＋** Each `ask-guppi` answers with one line per finding of its own, under its number: `closed`, or `not closed` with one sentence on what still stands.
> **＋** The main agent asks the person a question after the confirmation, in the shape of `.claude/skills/grill-me/SKILL.md`: whether each finding not closed is fixed or left; it sends a finding to be fixed to the `case-guppi` of its Case.
> **＋** It then shows every Case built again in one reply, for one ratification, and writes what the confirmation found closed and not closed in its own text after the horizontal rule.
> **－** No Case goes to `ask-guppi` a second time, and no new `ask-guppi` is dispatched.
> **－** The answer of `ask-guppi` names no new finding; it runs no Grep, the Grep of the rules included, and reads only the Cases built again and the pages its findings name.
> **－** After that ratification the hook of `rule-prespec-onward` sends the agent to the check and the exit, as before.

```then
create:
- slug: estimate-prespec-confirms-the-findings-once
  type: estimate
  ref: rule-prespec
  kind: QA
  purpose: Whether after the findings of pre-spec the same ask-guppi runs confirm their own findings once on the Cases built again, before those Cases are shown, with no Grep, one line per finding, closed or not closed and no new finding, a finding not closed fixed or left by the person's answer to a question after the confirmation, the result standing after the horizontal rule of the showing, and no Case confirmed twice
  method: 'by hand at the /pre-spec of a later session whose findings send a Case back to its case-guppi, after the render of .claude/skills/pre-spec/SKILL.md and .claude/agents/ask-guppi.md by case 634.2: the SendMessage calls to ask-guppi, its tool calls and answers, and the replies up to the showing of the Cases built again, read in the transcript against the Criterion, recorded in the estimate line'
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-prespec
  replace:
  - old: by its own `case-guppi` (case 561.1).
    new: by its own `case-guppi` (case 561.1), and the findings that sent it back are confirmed once in the loop below (case 634.2).
  - old: 6. Show every Case built again in one reply,
    new: |-
      6. Send each `ask-guppi` run whose findings sent a Case back the Cases built again on them, by `SendMessage`, all in one message, and ask whether each of its findings is closed; wait for every answer as step 3 sets it. Then ask the person a question after the confirmation, in its grill-me shape: whether each finding not closed is fixed or left; a finding to be fixed goes to the `case-guppi` of its Case as in steps 2 to 5. No Case goes to `ask-guppi` a second time, and no new `ask-guppi` is dispatched (case 634.2).
      7. Show every Case built again in one reply, what step 6 found closed and not closed standing in your own text after the horizontal rule,
  change: 'the loop after the findings: the same ask-guppi runs confirm their own findings once before the Cases built again are shown; a finding not closed is fixed or left by the person''s answer to a question after the confirmation; the result stands after the horizontal rule; no second confirmation (case 634.2)'
- slug: rule-ask
  replace:
  - old: answer in one of the two forms set at the end
    new: answer in one of the forms set at the end
  - old: 'Always start with the Grep of the rules, whatever the question:'
    new: 'Always start with the Grep of the rules, whatever the question but the confirmation of your findings at /pre-spec set at the end:'
  - old: N from the page's `origin`
    new: |-
      N from the page's `origin`

      At `/pre-spec`, when the caller sends you again the Cases built again on the findings you gave and asks whether each finding is closed, answer with one line per finding of yours, under its number: `closed`, or `not closed` and one sentence on what still stands. Run no Grep, the Grep of the rules included: read only the Cases built again and the pages your findings name, and name no new finding (case 634.2).
  change: ask-guppi answers the confirmation of its own findings at pre-spec with no Grep, one line per finding, closed or not closed, no new finding (case 634.2)
```

```tasks
- [ ] update `rule-prespec`
- [ ] update `rule-ask`
- [ ] create `estimate-prespec-confirms-the-findings-once`
- [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [ ] `uv run guppi render`: `.claude/agents/ask-guppi.md`
- [ ] read `estimate-prespec-confirms-the-findings-once`
```

### Case 634.3 — orchestration.md says when ask-guppi is sent: one run per Case at the first /pre-spec, asked again only to confirm

> **given:**
> `rule-orchestration` — what the main agent does, rendered into `vault/wiki/orchestration.md`; the sentence on when `ask-guppi` is sent changes
> **＋** `vault/wiki/orchestration.md` — the render, loaded by `/hi`
> **＋** `estimate-orchestration-shows-the-built-case` — its Criterion replaced whole; its `purpose` and `method` stand
> **＋** `rule-prespec` — sets the runs per Case and their confirmation, by 634.1 and 634.2
> **＋** `vault/raw/2026-10-04/2041/cases/case-632.md` — Case 632 changes other sentences of `rule-orchestration`
> **＋** `case-guppi` and `ask-guppi` — the agents the main agent dispatches
> **＋** `.claude/skills/wait-what/SKILL.md` and `.claude/skills/grill-me/SKILL.md` — the plain explanation and the question shape
> **＋** `rule-case-check` — writes `raw/<date>/<hi HHMM>/cases/case-<N>.md` from the answer and checks the showing

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
> **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
> **＋** An answer with no Case heading and no first line `**Fact:**` is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
> **＋** The main agent shows the Case of an answer at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file the hook of `rule-case-check` wrote from the answer. In the same reply it writes the heading of the top-level Case with its name in Russian and, under it, one list with an item per Case and sub-case of the answer: its id, its name in Russian, and a short text in Russian on what done means and how it is checked, taken from the Estimate the Case creates or whose Criterion it replaces, or from the Estimate its `context` names as already checking the change. Then it writes one `ratification` with the ledger lines of every Case of the list as the answer holds them, and its own text after one horizontal rule. An answer in which a Case gives no such Estimate goes back to its `case-guppi` by `SendMessage` before the Case is shown.
> **＋** A reply that shows a Case and that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the answer holds it; a reply that shows a round and that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that shows the round again with nothing before its `**Context:**` paragraph or its first question.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new answer is sent and ratified again; the main agent edits no Case in the plan file.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` only at pre-spec, one run per top-level Case at its first run, never to build a Case, and asks a run again only to confirm its own findings.
> **－** The main agent writes no context of its own before the first question of a round.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.

```then
update:
- slug: rule-orchestration
  replace:
  - old: the agent dispatches `ask-guppi` once, at pre-spec.
    new: the agent dispatches `ask-guppi` only at pre-spec, one run per top-level Case at its first run, and asks a run again only to confirm its own findings, as `rule-prespec` sets it (case 634.3).
  change: ask-guppi is dispatched only at pre-spec, one run per top-level Case, and asked again only to confirm its findings (case 634.3)
- slug: estimate-orchestration-shows-the-built-case
  set:
    status: pending
  change: the Criterion replaced whole — ask-guppi only at pre-spec, one run per top-level Case, asked again only to confirm its findings (case 634.3)
```

```tasks
- [ ] update `rule-orchestration`
- [ ] update `estimate-orchestration-shows-the-built-case`
- [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
- [ ] read `estimate-orchestration-shows-the-built-case`
```
