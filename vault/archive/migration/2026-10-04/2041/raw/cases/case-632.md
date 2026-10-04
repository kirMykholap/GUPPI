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

> **tasks:**
> - [ ] update `rule-sprint-close`
>   - sections.Purpose: `` Prevents a closed sprint from leaving its finished work among the live pages, so that the vault does not only grow: without a close, the Decision pages, the `actioned` Insights, the `error` lessons that joined no Insight, the sprint page and its Estimates of every past sprint stay among the pages that each search of the vault reads (cases 612, 627.1, 632.1). ``
>   - change: `## How it works left the Leaf: the mechanism in the docstring of guppi/sprint_close.py, the closing session in orchestration.md; the Purpose states the failure it prevents (case 632.1)`
> - [ ] update `rule-cleanup`
>   - change: `## How it works left the Leaf, its mechanism in the docstring of guppi/cleanup.py (case 632.1)`
> - [ ] update `rule-orchestration`
>   - old: `` while another Case is built, as `## Showing and signing a Case` sets it (case 598.1). ``
>   - new:
>     ```
>     while another Case is built, as `## Showing and signing a Case` sets it (case 598.1).
>
>     The session that closes a sprint is a session of its own: its Plan Mode holds only the closing Case and the Cases that prepare its readings, so that all of its decisions belong to the sprint it closes, and the closing Case holds the task line `uv run guppi sprint-close --sprint <id> --apply` with the person's choices, which the librarian runs (`rule-sprint-close`, case 628.1). Before the closing Case, the main agent sorts the Estimates that stand `pending` or `failed` into groups by the kind of moment their `method` names; the closing Case names the groups in its `context` and holds one `by hand` task per moment that Work Mode sets up and one `read` line per Estimate, and only an Estimate still unread after Work Mode is carried or archived unread (case 628.2). From the close until the first Case of the next session creates the next sprint page, `guppi sprint` and `make lint` report the missing sprint page, and that is expected (cases 628.3, 632.1).
>     ```
>   - change: `the session that closes a sprint — a session of its own, its readings in groups, the missing sprint page expected — moved here from the How it works of rule-sprint-close (case 632.1)`
> - [ ] `guppi/cleanup.py`: the docstring gains the facts of the section that it lacks — `sprint` is the first `## <id>` heading of `sprint.md`; the History lines `archived · cleanup` and `restored · cleanup`; a rerun moves nothing and exits 0; a file that cannot be moved, or a name already taken in the archive, is reported on stderr with exit 1, and the other pages still move
> - [ ] one-off, by hand: the `## How it works` section of `vault/wiki/rules/rule-cleanup.md` is removed, its heading and text, after the docstring of `guppi/cleanup.py` holds each of its facts
> - [ ] one-off, by hand: the `## How it works` section of `vault/wiki/rules/rule-sprint-close.md` is removed, its heading and text; each of its facts stands in the docstring of `guppi/sprint_close.py`, in the new paragraph of `rule-orchestration`, or in `rule-documentation`, `rule-work-mode`, `rule-retro`, `rule-skill-hi`, `rule-brief`, `rule-ledger-write`, `rule-materialize` or `rule-backlog`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`

> **ratification:**
> ```
> - decision[case 632.1][update][rule-sprint-close]{ref:rule-sprint-close}
> - decision[case 632.1][update][rule-cleanup]{ref:rule-cleanup}
> - decision[case 632.1][update][rule-orchestration]{ref:rule-orchestration}
> ```

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

> **tasks:**
> - [ ] update `rule-documentation`
>   - old: `` the open Insights and the `## Backlog` of the sprint page. ``
>   - new: `` the open Insights and the `## Backlog` of each sprint page, live or under `vault/archive/` (`rule-backlog`, case 632.2). ``
>   - change: `step 5 reads the Backlog of each sprint page, live or archived (case 632.2)`
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`

> **ratification:**
> ```
> - decision[case 632.2][update][rule-documentation]{ref:rule-documentation}
> ```

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

> **tasks:**
> - [ ] update `entity-sprint`
>   - old: `` its Estimates are its Definition of done, its `## Milestones` ``
>   - new: `` its Estimates are its Definition of done, read before its close, and one that has not passed by then goes to the archive with the sprint page, its status kept in the record of the close (`rule-sprint-close`, case 632.3); its `## Milestones` ``
>   - change: `the Estimates are the Definition of done read before the close; one not passed is archived with the sprint page (case 632.3)`
> - [ ] update `rule-sprint`
>   - old: `` whose `estimates` are its Definition of done — ``
>   - new: `` whose `estimates` are its Definition of done, read before its close, one that has not passed by then going to the archive with the sprint page, its status kept in the record of the close (`rule-sprint-close`, case 632.3) — ``
>   - change: `the Estimates of a sprint page are its Definition of done read before the close (case 632.3)`
> - [ ] update `entity-sprint-migration`
>   - old: `` the `file` route out of the scripts. ``
>   - new: `` the `file` route out of the scripts. Each Estimate of this page is read before the close of the sprint; one that has not passed by then goes to the archive with this page, its status kept in the record of the close (`rule-sprint-close`, case 632.3). ``
>   - change: `each Estimate of the page is read before the close; one not passed is archived with the page (case 632.3)`
> - [ ] `uv run guppi sprint`

> **ratification:**
> ```
> - decision[case 632.3][update][entity-sprint]{ref:entity-sprint}
> - decision[case 632.3][update][rule-sprint]{ref:rule-sprint}
> - decision[case 632.3][update][entity-sprint-migration]{ref:entity-sprint-migration}
> ```

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

> **tasks:**
> - [ ] update `estimate-sprint-migration-lint-clean`
>   - set:
>     ```
>     status: pending
>     purpose: 'make lint in the Work Mode of the session that closes the sprint, before the librarian''s run, shows no finding, unmigrated included, but the unread of the sprint page''s own Estimates and of the Estimates read only at or after the closing librarian''s run, which the close line carries'
>     method: 'make lint in the Work Mode of the session that closes the sprint, before the librarian''s run: exit 0, or only unread lines on the Estimates of entity-sprint-migration and on Estimates whose method names a moment at or after that librarian''s run and that the close line names by --carry, each such line named in the estimate line'
>     ```
>   - change: `the Criterion replaced whole — an unread Estimate that the close line carries because its moment comes at or after the closing librarian's run fails nothing (case 632.4)`
> - [ ] read `estimate-sprint-migration-lint-clean`

> **ratification:**
> ```
> - decision[case 632.4][update][estimate-sprint-migration-lint-clean]{ref:entity-sprint-migration}
> ```

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

> **tasks:**
> - [ ] update `estimate-sprint-close-next-session-opens-the-sprint`
>   - set:
>     ```
>     status: pending
>     purpose: 'Whether after the close of a sprint the brief puts the opening of the next sprint first, /hi takes no item of sprint.md, the ledger hook refuses every decision line but a defer until a create of a sprint page stands, and the pages written from the ledger of the session that opens it carry its id'
>     method: 'pytest tests/test_ledger.py -k sprint and tests/test_materialize.py -k sprint; by hand, at the librarian''s run of the session after the close of a sprint: the brief before it, its frontier.md, the refusals of guppi ledger in its transcript, its ledger and the sprint field of the pages written from that ledger'
>     ```
>   - change: `the Criterion replaced whole — the new sprint id goes to the pages written from the ledger that creates the sprint page, as materialize sets it (case 632.5)`
> - [ ] read `estimate-sprint-close-next-session-opens-the-sprint`

> **ratification:**
> ```
> - decision[case 632.5][update][estimate-sprint-close-next-session-opens-the-sprint]{ref:rule-sprint-close}
> ```

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

> **tasks:**
> - [ ] update `rule-skill-hi`
>   - old: `` on a plan branch the unfinished plan, and each conserved Spec `backlog.md` names, one line each with the source `backlog`, first; the items of the sprint's current milestone — the first with an open item or with none — and none of a later milestone, of the Backlog or of Closed (case 229.3) — and none at all while the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, which then stands as the first Cases line, before every other (`rule-sprint-close`, case 628.7); ``
>   - new: `` first, when the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, that line (`rule-sprint-close`, case 628.7); then, on a plan branch, the unfinished plan, and each conserved Spec `backlog.md` names, one line each with the source `backlog` — but none while that opening line stands: the session that opens a sprint takes no conserved Spec, which waits in `backlog.md` for the next session (case 632.6); the items of the sprint's current milestone — the first with an open item or with none — and none of a later milestone, of the Backlog or of Closed (case 229.3), and none at all while that opening line stands (case 628.7); ``
>   - change: `the opening of the next sprint alone comes first; no conserved Spec on the Frontier while it stands (case 632.6)`
> - [ ] update `estimate-hi-writes-frontier`
>   - set: `status: pending`
>   - change: `the Criterion replaced whole — no conserved Spec is a Cases line while the opening of the next sprint stands (case 632.6)`
> - [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] read `estimate-hi-writes-frontier`

> **ratification:**
> ```
> - decision[case 632.6][update][rule-skill-hi]{ref:rule-skill-hi}
> - decision[case 632.6][update][estimate-hi-writes-frontier]{ref:rule-skill-hi}
> ```

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

> **tasks:**
> - [ ] update `estimate-hi-takes-a-conserved-spec`
>   - set:
>     ```
>     status: pending
>     method: 'uv run guppi render --check; by hand, a session whose person takes a conserved Spec at the Frontier: frontier.md, the title line of the plan file and the session''s ledger read against the Criterion; and the /hi of the session after the close of a sprint: its frontier.md and backlog.md'
>     ```
>   - change: `the Criterion replaced whole — a session that does not open a sprint takes a conserved Spec as before; the session that opens the next sprint takes none (case 632.7)`
> - [ ] read `estimate-hi-takes-a-conserved-spec`

> **ratification:**
> ```
> - decision[case 632.7][update][estimate-hi-takes-a-conserved-spec]{ref:rule-skill-hi}
> ```

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

> **tasks:**
> - [ ] update `estimate-case-check-sends-back-a-case-number-held-by-another-agent`
>   - set: `` method: uv run pytest tests/test_casecheck.py -k subagent_clash, then by hand an answer of case-guppi the hook sends back for this reason ``
>   - change: `the method selects -k subagent_clash, so that the tests of session_clash are not run (case 632.8)`

> **ratification:**
> ```
> - decision[case 632.8][update][estimate-case-check-sends-back-a-case-number-held-by-another-agent]{ref:rule-case-check}
> ```

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

> **tasks:**
> - [ ] update `estimate-insights-schema-checked`
>   - set: `status: pending`
>   - change: `the Criterion replaced whole — the prose stands as data, with no claim that it is word for word the old schema.md (case 632.9)`
> - [ ] read `estimate-insights-schema-checked`

> **ratification:**
> ```
> - decision[case 632.9][update][estimate-insights-schema-checked]{ref:rule-insights-schema}
> ```

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

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` a question at `/hi`, a question at a stop of Work Mode — takes the question shape ``
>   - new: `` a question at `/hi`, a question at a stop of Work Mode, the question whether another Case is built again after a clash (case 629.1), the question at `/pre-spec` whether each finding of `ask-guppi` not closed is fixed or left (`rule-prespec`, case 634.2) — takes the question shape ``
>   - change: `the question after a clash and the question on a finding not closed are among the main agent's own questions in the grill-me shape (case 632.10)`
> - [ ] update `estimate-orchestration-asks-in-the-grill-me-shape`
>   - set:
>     ```
>     status: pending
>     purpose: 'Whether each question the main agent puts to the person itself, at pre-spec, at /hi, at a stop of Work Mode, after a clash on whether another Case is built again, or at pre-spec on whether a finding of ask-guppi not closed is fixed or left, takes the question shape of grill-me, the exceptions kept in their own form'
>     ```
>   - change: `the Criterion replaced whole — the When names the question after a clash and the question on a finding not closed (case 632.10)`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-orchestration-asks-in-the-grill-me-shape`

> **ratification:**
> ```
> - decision[case 632.10][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 632.10][update][estimate-orchestration-asks-in-the-grill-me-shape]{ref:rule-orchestration}
> ```
