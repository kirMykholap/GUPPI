## Case 628 — The close of a sprint runs in the librarian's run of a session of its own, and the next session opens the next sprint first

> **context:**
> `rule-sprint-close` says what the close of a sprint moves to the archive and what it keeps. Case 627 of this session builds the command `uv run guppi sprint-close --sprint <id>`. Without `--apply` it shows what would move. With `--apply` it marks the pages `archived` and runs `guppi cleanup`. No page yet says who runs the command or when, and no page says how the next sprint opens. The moment matters because a reading taken in a session reaches its Estimate page only at the librarian's run, when `guppi generate` applies it. For example, suppose the agent runs the close in Work Mode right after it reads a pending check. The command still sees that check `pending` and refuses. There is also a gap after the close. `guppi sprint` needs exactly one live sprint page, and `guppi materialize` gives every new page the sprint id it finds in the first `## <id>` heading of `vault/wiki/sprint.md`. After the close, no sprint page is live, `sprint.md` keeps the closed sprint's heading, and the pages of the next session would carry the id of a sprint that no later close archives. The close also archives the sprint page with its `## Backlog`, and `guppi backlog` reads that section only on the live sprint page. The person asked to take as many readings as possible before the close, sorted into groups, by setting up on purpose the moment each one needs.
>
> The person chose the place and the order as follows. The close runs in a session of its own (Q2), and every decision of that session belongs to the sprint it closes. The closing Case holds the command as a task line with the person's choices. The librarian runs it right after `guppi generate`, so the readings of that session count (Q1, Q11). Work Mode leaves the line, Retro counts it as waiting and not as debt, and the command ticks its own line by `render.command_line`, the one matcher of the tickers. Before the close, the session sorts the pending Estimates into groups by the kind of moment each `method` names, and sets up each moment it can. The closing Case names the groups and holds the tasks (Q4, Q8). The next sprint opens by a Case of the next session, not of the closing one (Q3). Between the close and that Case, `guppi sprint` and `make lint` report the missing sprint page, and that is expected (Q6). The closing run's brief puts the opening first under Next session. `/hi` takes no item of `sprint.md` then. The ledger hook refuses every decision line of that session, a `defer` excepted, until a `create` of `entity-sprint-<id>` stands (Q10). The run that writes the new sprint page gives all its pages the new id (Q5). One Case holds every sub-case (Q9, Q12). At `/pre-spec` the person made two more choices. The `## Backlog` of a closed sprint page goes into the general `backlog.md`, so `guppi backlog` also reads the `## Backlog` of each sprint page under `vault/archive/` (628.12). `entity-sprint-migration` lists six Estimates, three `passed` and three `pending`. The three pending ones — `estimate-sprint-migration-merges`, `estimate-sprint-migration-lint-clean` and `estimate-sprint-migration-leftovers-gone` — are read in the Work Mode of the closing session, before the librarian's run, and their Then names what holds before the close (628.9 to 628.11). The merge of `migration` into `main` leaves the promise of the closed sprint. It becomes the first work of the session that opens the next sprint, written as a line of the `## Backlog` of `entity-sprint-migration`, which `backlog.md` then shows. This choice replaces the earlier Q7 answer, under which only the line on `built` changed. The Then of `estimate-sprint-migration-merges` also drops the line "`vault/wiki/sprint.md` shows every Done-when line `[x]`". That line could not hold: Case 627.4 lets the close go ahead with the sprint page's own Estimates not passed, and after the close `guppi sprint` does not rewrite `sprint.md`. The Then of `estimate-sprint-migration-lint-clean` keeps its bar word for word: no finding but the `unread` of the sprint page's own Estimates. So at that reading every other Estimate is read, and no stale defer stands. An Estimate the close carries, or archives unread from its own rule, is still an `unread` finding when Work Mode reads `make lint`, and it fails this check. That is the bar the person kept.
>
> The sprint page. Its Slice 5 note "where the close of a sprint runs — a session of its own, a command or another place: not decided" keeps its milestone open until a Case cuts it (`rule-sprint`). 628.9 replaces that line by a note on the close of migration itself, which runs in a later session. 628.9 also replaces "the branch merged" in its Purpose, and adds the merge line to its `## Backlog`. Case 627, built again at the same time, updates the other line of that milestone, the `[[rule-sprint-close]]` item. Both use `replace` pairs, not the section whole. The deferred decision `decision-case-615` on `entity-sprint-migration` asks how much stays for the close of migration: which pending Estimates are read, carried or archived before the close. The person agreed on Case 627 that this session's Cases answer that question. 627.4 settles each pending Estimate. 628.2 takes the readings in groups. The four Estimates of the close are read by a test and the preview. So the decision line of 628.9 on `entity-sprint-migration` carries `{supersedes:case 615}`, as the line of Case 627 on that page does. The defer is retired, and the page leaves `backlog.md`.
>
> Frame checks. Each create has a `ref`, so the vault query of `ask-guppi` was not run. A Glob `vault/**/estimate-sprint-close-*.md` printed the four Estimates of Case 612, so the three new slugs are free. A Grep of ``sprint_id|first `## <id>`|`sprint` (field|is the)|sprint: <|the id of the (live|current) sprint`` ran over the repository outside `vault/archive/` and `vault/raw/`, and printed 22 files: `guppi/materialize.py`, `guppi/generate.py`, `guppi/sprint.py`, `guppi/cleanup.py`, `guppi/archive.py`, `tests/test_sprint.py`, `rule-sprint.md`, `rule-raw-archive.md`, `rule-cleanup.md`, `estimate-generate-writes.md`, `estimate-sprint-checks-the-file.md` and 11 Decision pages, which were not read. `estimate-generate-writes` and the docstring of `guppi/generate.py` say a page's `sprint` is the first `## <id>` of `sprint.md`, so 628.6 changes both. `rule-cleanup`, `rule-raw-archive`, `guppi/cleanup.py` and `guppi/archive.py` read the heading at their own step and stay true. In the run that opens a sprint, a page that `guppi cleanup` archives goes under the closed sprint's folder of `vault/archive/`, and this stands. `estimate-sprint-checks-the-file` says that a render error, such as no sprint page, is one line on stderr and exit 1. That is what happens after a close, as Q6 chose, so its Criterion stands.
>
> The ticks. A Grep of ``guppi sprint|guppi render`|ticked by|unticked`` over `vault/wiki/rules/` printed 14 files: `rule-page-generation`, `rule-work-mode`, `rule-retro`, `rule-orchestration`, `rule-case-protocol`, `rule-materialize`, `rule-documentation`, `rule-brief`, `rule-governed-files-hook`, `rule-backlog`, `rule-entities-schema`, `rule-sprint`, `rule-harness` and `rule-glossary`. These change: `rule-work-mode` (628.4), `rule-retro`, `rule-orchestration` and `rule-case-protocol` (628.1), and `rule-sprint` (628.5). The other hits do not speak of the close line. 628.5 narrows `render.command_line`, the matcher of all three tickers, so that a command no longer matches where a `-` or a word character follows it. `estimate-render-harness-ticks-the-spec` and `estimate-glossary-ticks-the-spec` speak of lines that hold `guppi render` and `guppi glossary`. No command of guppi extends those names, so each line they tick is still ticked, and both Criteria stand. `estimate-prespec-catches-a-command-line-off-form` judges lines outside a code span, which the matcher does not read, so it stands. The other Criteria this change makes false are replaced: `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` (628.4), `estimate-sprint-ticks-the-spec` (628.5), `estimate-hi-writes-frontier` (628.7), `estimate-brief-written` (628.8) and `estimate-backlog-renders` (628.12). In each one only the lines this Case speaks of change. A method that tied its reading to "the first" of something is set anew. `estimate-retro-loads`, `estimate-case-protocol-loaded` and `estimate-documentation-completes` speak of nothing this Case changes, so they stand.
>
> The notes of the hook. Some lines of a replaced Criterion are not carried, on purpose. In 628.9 to 628.11, each old When, "at the close of the sprint", gives way to the Work Mode of the closing session. In 628.9, the line on the merge into `main` and the last brief leaves the promise, as the person chose. In 628.12, the line on the items of `## Deferred` gains the archived sprint pages. One `then` line of 628.12, on `## Deferred` of `backlog.md`, shares words with a line of 628.8, on the Deferred list that the brief does not hold. The two speak of different files, so each stays in its own sub-case.
>
> Writers and hooks. A Grep of `only writer|librarian alone|written by hand` over `vault/wiki/rules/` printed `rule-insights-schema`, `rule-guppi-config`, `rule-entities-schema`, `rule-documentation`, `rule-lint`, `rule-vault-layout` and `rule-page-generation`. The sentence of `rule-documentation` that the librarian is the only writer to `vault/wiki/` stays true, since the librarian runs the command. The hooks on `Stop` in `.claude/settings.json` are `guppi ledger`, `guppi ratified`, `guppi casecheck`, `guppi context`, `guppi onward` and `guppi onward --plan`. The new refusal of `guppi ledger` refuses lines as its other refusals do, and `estimate-ledger-write-lifts` stands. `guppi ratified` writes a shown Case into the plan file from the reply. A Case whose decision lines are refused for a missing sprint is ratified again after the opening Case, and the hook replaces its section. Case 627.1 writes the Purpose of `rule-sprint-close`, which now ends by pointing to `## How it works` of that page. 628.1 writes that section alone, so the two texts agree. Case 629 changes no page that this Case changes.

> **problem:**
> Nothing says where the close of a sprint runs, who calls it, or how the next sprint opens. Run in the wrong place, the close refuses the readings of its own session. Between the close and a new sprint page, the vault has no live sprint, and the pages written then would belong to a closed sprint. The closed sprint page also takes its Backlog into the archive, and the checks of migration wait for a moment that the close itself removes. The question is where the close runs, how its readings are taken first, how the next session opens the next sprint before anything else, and where the Backlog and the checks of the closed sprint go.

> **recommend:**
> - **Which step of a session runs the close with `--apply`?**
>   - Recommended: (a) the librarian's run, right after `guppi generate`, from a task line of the closing session's Spec that holds the command with the person's choices.
>   - Answer: agreed.
> - **Does the close get a session of its own?**
>   - Recommended: (a) a session of its own, whose Plan Mode holds only the closing Case and the Cases that prepare its readings.
>   - Answer: agreed.
> - **How does the next sprint start?**
>   - Recommended: (a) the closing Case creates the next sprint page in the same session.
>   - Answer: (b): a Case of the next session creates it.
> - **How does the closing session take the pending readings before the close?**
>   - Recommended: (a) the rule of the close sets the grouping, with no code: the pending Estimates sorted by the kind of moment their method names, each moment set up in Work Mode, only the rest carried or archived unread.
>   - Answer: agreed.
> - **Which sprint do the pages written before the next sprint opens belong to?**
>   - Recommended: (b) the new sprint's id, taken from the `create` of `entity-sprint-<id>` in the same unit.
>   - Answer: agreed.
> - **What do `guppi sprint` and `make lint` do between the close and the opening of the next sprint?**
>   - Recommended: (a) it stays an error, as the person's answer reads: the brief flags it and the next session's Baseline holds the red.
>   - Answer: (a). The person had first said that one session closes the sprint and that all of its decisions belong to that sprint. After that, every test runs, and a check may report that no sprint is open, which is normal. The next session must start by opening a new sprint.
> - **What happens to the check of migration that says the close is the sprint page set `built`?**
>   - Recommended: (a) replace its Criterion whole now: the line on `built` gives way to the librarian's run of the command, the lines on `make test` and the merge kept.
>   - Answer: agreed; later replaced by the person's answer at `/pre-spec` on when the three Estimates of migration are read (see the second **Change**).
> - **Where does the grouping of the pending readings stand?**
>   - Recommended: (a) in the closing Case: its `context` lists the groups, its `tasks` hold a `by hand` task per moment and a `read` line per Estimate.
>   - Answer: agreed.
> - **How is this Case split, and what checks each part?**
>   - Recommended: (a) three sub-cases, one new check each, all on `rule-sprint-close`: the librarian runs the close; the readings in groups; the next sprint opens first.
>   - Answer: agreed.
> - **What makes the next session open the new sprint first?**
>   - Recommended: (b) the brief and `/hi`, plus a ledger hook that refuses every decision line but a `defer` until a `create` of a sprint page stands.
>   - Answer: agreed.
> - **How does the close command, with your choices, reach the librarian?**
>   - Recommended: (a) keep the task line, and change Work Mode, Retro, `rule-orchestration` and the ticker of `guppi sprint` so that the librarian runs it and the command ticks it.
>   - Answer: agreed.
> - **How is this Case cut, now that more checks must change?**
>   - Recommended: (a) one Case with every sub-case: the three new checks, the migration check and one sub-case per check the change makes false.
>   - Answer: agreed.
> - **Change**
>   - Asked: at `/pre-spec`, on where the `## Backlog` lines of a closed sprint page go, the person said the backlog should pass between sprints, and that the Backlog of the sprint page goes into the general `backlog.md`.
>   - Taken: 628.12: `guppi backlog` reads the `## Backlog` of each sprint page, live or under `vault/archive/`; `rule-backlog` and the Criterion of `estimate-backlog-renders` say so, and `## How it works` of `rule-sprint-close` names it.
> - **Change**
>   - Asked: at `/pre-spec`, on when the three Estimates of migration are read, option (a): in the Work Mode of the closing session, before the librarian's run, their Then naming what holds before the close — `make test` green on the last commit, `make lint` with no finding but the unread of the sprint page's own Estimates, the leftovers gone — the merge into `main` leaving the promise of the closed sprint and becoming the first work of the session that opens the next sprint.
>   - Taken: 628.9 to 628.11 replace the When of the three, and the Then of `estimate-sprint-migration-merges` keeps only `make test`; their purposes and methods are set anew; `entity-sprint-migration` gets the merge as a line of its `## Backlog`, its Slice 5 note replaced by the close of migration, and "the branch merged" out of its Purpose.
> - **Change**
>   - Asked: on Case 627, the person agreed that the change to the sprint page also closes the question put off on it by `decision-case-615`, how much stays for the close of migration, answered by what this session set; the Case that changes the other line of the same milestone carries the same mark.
>   - Taken: the decision line of 628.9 on `entity-sprint-migration` carries `{supersedes:case 615}`; the defer is retired and the page leaves `backlog.md`.

### Case 628.1 — The librarian runs the close from the closing Case's task line, after the readings of its session are applied

> **given:**
> `estimate-sprint-close-runs-in-the-librarian-run` — the new promise, on `rule-sprint-close`
> **＋** `rule-sprint-close` — the rule of the close of `entity-sprint-<id>`; it gains the section `## How it works`
> **＋** `vault/raw/2026-10-04/1439/cases/case-627.md` — Case 627, whose Purpose of that page points to `## How it works`, and which builds `guppi sprint-close`
> **＋** `rule-documentation` — the frame of `librarian-guppi`, rendered into `.claude/agents/librarian-guppi.md`
> **＋** `rule-retro`, `rule-orchestration` and `rule-case-protocol` — which boxes wait for the librarian, who ticks them and their forms; rendered into `.claude/skills/retro/SKILL.md`, `vault/wiki/orchestration.md` and `vault/wiki/case-schema.md`
> **＋** `guppi/sprint_close.py` and `tests/test_sprint_close.py` — the command ticks its own line; its tests
> **＋** `guppi/render.py` — `command_line`, the one matcher of a command line of the Spec
> **＋** `/hi` and `vault/archive/` — where the session opens and where the close moves pages

> **when:**
> The session that closes `entity-sprint-<id>` runs from `/hi` to the librarian's run, its closing Case holding the task line `uv run guppi sprint-close --sprint <id> --apply` with the person's choices; someone reads its ledger, its `spec.md`, its `handoff.md`, the librarian's event log and report, and `vault/archive/` after it.
> **＋** Or `tests/test_sprint_close.py` runs `guppi sprint-close --apply` over a made-up vault whose `spec.md` holds that line.

> **then:**
> The ledger of the session holds the decision lines of the closing Case and of the Cases that prepare its readings, and no other decision line but a `defer`.
> **＋** Work Mode neither runs nor ticks the close line, and the handoff does not name it as debt.
> **＋** The librarian runs the line as it stands after `guppi generate` and before `guppi cleanup`, and a reading that the session's ledger holds is applied before the command reads the Estimates.
> **＋** After a run that moved the pages, the line stands ticked in `spec.md`, found by `command_line` of `guppi/render.py`.
> **－** A run that refuses moves nothing and ticks nothing, and the librarian names its stderr lines as flags.

> **tasks:**
> - [ ] update `rule-sprint-close`
>   - sections.How it works:
>     ````
>     The close runs in a session of its own, whose Plan Mode holds only the closing Case and the Cases that prepare its readings, so that all of its decisions belong to the sprint it closes: the closing Case holds the task line `uv run guppi sprint-close --sprint <id> --apply` with the person's choices; Work Mode leaves that line, Retro counts it as waiting, and the librarian runs it after `guppi generate` and before `guppi cleanup`, so that the readings of that session count; the command ticks its line, found by `render.command_line`, once it moved the pages (case 628.1).
>
>     Before the closing Case, the session sorts the Estimates that stand `pending` or `failed` into groups by the kind of moment their `method` names; the closing Case names the groups in its `context` and holds one `by hand` task per moment that Work Mode sets up and one `read` line per Estimate, and only an Estimate still unread after Work Mode is carried or archived unread (case 628.2).
>
>     No sprint is open from the close until a Case of the next session, its first, creates `entity-sprint-<new id>`: the brief of the closing run names that opening first under the Cases of Next session, `/hi` takes no item of `sprint.md` meanwhile, the ledger hook refuses every other decision line of that session but a `defer` until the `create` stands, and every page of the run that writes the new sprint page carries the new id; `guppi sprint` and `make lint` report the missing sprint page until then, and that is expected (case 628.3). The `## Backlog` of a closed sprint page stays in `backlog.md`, since `guppi backlog` reads it under `vault/archive/` too (case 628.12).
>     ````
>   - change: `where the close runs, in How it works: the librarian's run of a session of its own, from the closing Case's task line; the readings taken in groups first; the next sprint opened first by the next session; the Backlog of a closed sprint kept in backlog.md (case 628.1)`
> - [ ] update `rule-documentation`
>   - old: `` 2. Run `uv run guppi generate`. Every line on its stderr is a flag. ``
>   - new: `` 2. Run `uv run guppi generate`. Every line on its stderr is a flag. Then, when an unticked task line of the session's `spec.md` opens with a code span holding `guppi sprint-close` and `--apply`, run that command as the line holds it: the readings this run applied count, and the command runs `guppi cleanup` itself (`rule-sprint-close`, case 628.1). Every line on its stderr is a flag; a refusal moves nothing, and the run goes on. After a close, `guppi sprint` in step 5 finds no live sprint page; its error is a flag. ``
>   - change: `the librarian runs the close line of the Spec after generate (case 628.1)`
> - [ ] update `rule-retro`
>   - old: `` A `create`, `update` or `defer` line of a page, a `guppi render` line, a `guppi sprint` line, ``
>   - new: `` A `create`, `update` or `defer` line of a page, a `guppi render` line, a `guppi sprint` line, a `guppi sprint-close` line (`rule-sprint-close`, case 628.1), ``
>   - change: `a guppi sprint-close line waits for the librarian and is not debt (case 628.1)`
> - [ ] update `rule-orchestration`
>   - old: `` `render`, `sprint` and `glossary` the render, sprint and glossary lines (cases 226, 250, 270, 306); ``
>   - new: `` `render`, `sprint` and `glossary` the render, sprint and glossary lines (cases 226, 250, 270, 306), and `guppi sprint-close`, which the librarian runs, its own line (case 628.1); ``
>   - change: `guppi sprint-close ticks its own line (case 628.1)`
> - [ ] update `rule-case-protocol`
>   - old: ``` a glossary line `- [ ] `uv run guppi glossary`` — the command in the first code span is what the ticker matches (case 235) ```
>   - new: ``` a glossary line `- [ ] `uv run guppi glossary``, a close line `- [ ] `uv run guppi sprint-close --sprint <id> --apply …``, which the librarian runs and the command ticks (`rule-sprint-close`, case 628.1) — the command in the first code span is what the ticker matches (case 235) ```
>   - change: `the close line of a sprint is a task line form (case 628.1)`
> - [ ] create `estimate-sprint-close-runs-in-the-librarian-run`
>   - kind: `QA`
>   - purpose: `Whether the close of a sprint runs in the librarian's run of a session of its own, from the task line of its closing Case, after guppi generate and before guppi cleanup, so that the readings of that session count, with Work Mode leaving the line, Retro not counting it as debt and the command ticking it`
>   - method: `pytest tests/test_sprint_close.py -k tick; by hand, after the librarian's run of the session that closes a sprint: its ledger, spec.md, handoff.md, the librarian's event log and report, and vault/archive/`
>   - tags: `[sprint, workflow, librarian]`
> - [ ] `guppi/sprint_close.py`: after a run with `--apply` that moved the pages, tick each unticked task line of a `spec.md` under `vault/raw/` that `render.command_line("guppi sprint-close --sprint <id> --apply")` matches, imported from `guppi/render.py`, not copied (`rule-one-judgment-one-implementation`); a refused run ticks nothing; the docstring
> - [ ] `tests/test_sprint_close.py`: `-k tick` — the line ticked after a run that moved, left unticked after a refusal, a line of another sprint id left; the clock pinned
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-sprint-close-runs-in-the-librarian-run`

> **ratification:**
> ```
> - decision[case 628.1][update][rule-sprint-close]{ref:rule-sprint-close}
> - decision[case 628.1][update][rule-documentation]{ref:rule-documentation}
> - decision[case 628.1][update][rule-retro]{ref:rule-retro}
> - decision[case 628.1][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 628.1][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 628.1][create][estimate-sprint-close-runs-in-the-librarian-run]{ref:rule-sprint-close}{tags:sprint,workflow,librarian}
> ```

### Case 628.2 — The closing session takes the pending readings in groups before the close

> **given:**
> `estimate-sprint-close-takes-the-readings-in-groups` — the new promise, on `rule-sprint-close`
> **＋** `rule-sprint-close` — the rule of the close of `entity-sprint-<id>`; its `## How it works`, written by 628.1, sets the grouping
> **＋** `vault/raw/<date>/<hi HHMM>/spec.md` — the Spec of the closing session
> **＋** `vault/raw/<date>/<hi HHMM>/ledger.md` — the ledger of the closing session
> **＋** `vault/wiki/estimates/` — the Estimates that stand `pending` or `failed`

> **when:**
> The session that closes `entity-sprint-<id>` runs its Plan Mode and its Work Mode; someone reads its closing Case in `vault/raw/<date>/<hi HHMM>/spec.md` and its `vault/raw/<date>/<hi HHMM>/ledger.md` after its Work Mode.

> **then:**
> The `context` of the closing Case sorts each Estimate under `vault/wiki/estimates/` that stands `pending` or `failed` into groups by the kind of moment its `method` names.
> **＋** The `tasks` of the closing Case hold one `by hand` task per moment that Work Mode sets up, and one `read` line per Estimate of each group.
> **＋** Work Mode sets up each such moment, and the ledger holds a reading of each Estimate whose moment came.
> **－** The close line names by `--carry` or `--archive-unread` only an Estimate still unread after Work Mode.

> **tasks:**
> - [ ] create `estimate-sprint-close-takes-the-readings-in-groups`
>   - kind: `QA`
>   - purpose: `Whether the session that closes a sprint sorts the pending and failed Estimates into groups by the kind of moment their method names, sets up each moment it can in its Work Mode, and carries or archives unread only those still unread`
>   - method: `by hand, after the Work Mode of the session that closes a sprint: its closing Case, spec.md and ledger read against the Criterion`
>   - tags: `[sprint, workflow]`
> - [ ] read `estimate-sprint-close-takes-the-readings-in-groups`

> **ratification:**
> ```
> - decision[case 628.2][create][estimate-sprint-close-takes-the-readings-in-groups]{ref:rule-sprint-close}{tags:sprint,workflow}
> ```

### Case 628.3 — The next session opens the next sprint first, and its pages carry the new id

> **given:**
> `estimate-sprint-close-next-session-opens-the-sprint` — the new promise, on `rule-sprint-close`
> **＋** `entity-sprint-<id>`, `entity-sprint-<new id>` and the slug prefix `entity-sprint-` — the closed sprint page, the next one, and any sprint page
> **＋** `rule-ledger-write` — the `Stop` hook `guppi ledger`; its Purpose gains the refusal
> **＋** `guppi/ledger.py` and `tests/test_ledger.py` — the hook and its tests
> **＋** `rule-materialize`, `guppi/materialize.py` and `tests/test_materialize.py` — the yaml's `sprint`; its Purpose, the script and its tests
> **＋** `rule-brief` and `rule-skill-hi` — the brief's Next session and the Frontier of `/hi`, changed by 628.8 and 628.7
> **＋** `vault/wiki/brief.md`, `vault/wiki/sprint.md` and `vault/raw/<date>/<hi HHMM>/frontier.md` — what the brief and `/hi` write and read

> **when:**
> The librarian's run of the session that closes `entity-sprint-<id>` ends with no live sprint page, and the next session opens with `/hi`; someone reads `vault/wiki/brief.md`, that session's `vault/raw/<date>/<hi HHMM>/frontier.md`, the refusals of `uv run guppi ledger` in its transcript, its ledger, and the pages of its librarian's run.
> **＋** Or `tests/test_ledger.py` and `tests/test_materialize.py` run `guppi ledger` and `guppi materialize` over a made-up vault with no live sprint page.

> **then:**
> The first line of the `Cases` of Next session in `vault/wiki/brief.md` is `open the next sprint — no sprint is open since the close of <id>`.
> **＋** `/hi` writes that line first under `## Cases` of `frontier.md`, and takes no item of `vault/wiki/sprint.md`.
> **＋** While no live `entity-sprint-` page stands, `guppi ledger` refuses each decision line of the session but a `defer`, with one stderr line, until the session's ledger or the same reply holds a `create` decision line of an `entity-sprint-` slug.
> **＋** Each page that the librarian's run of that session writes carries `sprint: <new id>`, the id of the `entity-sprint-<new id>` that the run creates.
> **－** An `estimate` or `lesson` line is not refused for this reason.
> **－** The error of `guppi sprint` in the closing run is a flag of the brief, not a failure of this promise.

> **tasks:**
> - [ ] update `rule-ledger-write`
>   - old: `would materialize pages from it the next day.`
>   - new: `` would materialize pages from it the next day. It also refuses, while no live page `vault/wiki/entities/entity-sprint-<id>.md` stands, every decision line of the session but a `defer`, until the session's ledger or the same reply holds a `create` decision line of an `entity-sprint-` slug, with one stderr line that names the opening of the next sprint, so that the session after the close of a sprint opens the next sprint first (`rule-sprint-close`, case 628.3). ``
>   - change: `refuses the decision lines of a session with no live sprint page until it creates one (case 628.3)`
> - [ ] update `rule-materialize`
>   - old: `` The mechanism and the full list of an entry's fields, each with its writer, live in the docstring of `guppi/materialize.py`. ``
>   - new: `` The yaml's `sprint` is the first `## <id>` heading of `sprint.md`, but in a unit whose ledger holds a `create` decision line of `entity-sprint-<id>` it is that `<id>`, so that the session that opens a sprint belongs to it (`rule-sprint-close`, case 628.3). The mechanism and the full list of an entry's fields, each with its writer, live in the docstring of `guppi/materialize.py`. ``
>   - change: `the yaml's sprint is the id of a sprint page the unit creates (case 628.3)`
> - [ ] create `estimate-sprint-close-next-session-opens-the-sprint`
>   - kind: `QA`
>   - purpose: `Whether after the close of a sprint the brief puts the opening of the next sprint first, /hi takes no item of sprint.md, the ledger hook refuses every decision line but a defer until a create of a sprint page stands, and the pages of the run that opens it carry its id`
>   - method: `pytest tests/test_ledger.py -k sprint and tests/test_materialize.py -k sprint; by hand, at the librarian's run of the session after the close of a sprint: the brief before it, its frontier.md, the refusals of guppi ledger in its transcript, its ledger and the sprint field of the pages of its run`
>   - tags: `[sprint, workflow, ledger]`
> - [ ] `guppi/ledger.py`: the refusal — no live `entity-sprint-` page, a decision line other than a `defer`, and no `create` decision line of an `entity-sprint-` slug in the session's ledger or the reply; one stderr line; readings and lessons pass; the docstring
> - [ ] `tests/test_ledger.py`: `-k sprint` — refused with no sprint page, a `defer` and a reading passed, accepted once the `create` stands in the ledger or the same reply, accepted with a live sprint page
> - [ ] `guppi/materialize.py`: the yaml's `sprint` from a `create` decision line of `entity-sprint-<id>` in the unit, else the heading of `sprint.md`
> - [ ] `tests/test_materialize.py`: `-k sprint` — a unit that creates `entity-sprint-next` gets `sprint: next`; a unit with none gets the heading's id
> - [ ] read `estimate-sprint-close-next-session-opens-the-sprint`

> **ratification:**
> ```
> - decision[case 628.3][update][rule-ledger-write]{ref:rule-ledger-write}
> - decision[case 628.3][update][rule-materialize]{ref:rule-materialize}
> - decision[case 628.3][create][estimate-sprint-close-next-session-opens-the-sprint]{ref:rule-sprint-close}{tags:sprint,workflow,ledger}
> ```

### Case 628.4 — Work Mode leaves the close line to the librarian

> **given:**
> `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — its Criterion replaced whole, its `purpose` and `method` set anew
> **＋** `rule-work-mode` — the skill `/work`, rendered into `.claude/skills/work/SKILL.md`; one sentence changes
> **＋** `rule-spec-box` — `/box`, which calls `/work` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec
> **＋** `vault/raw/<date>/<hi HHMM>/spec.md` and `vault/raw/<date>/<hi HHMM>/work.md` — the Spec it runs and the file it writes
> **＋** `vault/wiki/` — the pages the skill does not write
> **＋** `rule-sprint-close` — the close line, run by the librarian

> **when:**
> The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, after `uv run guppi render` wrote `.claude/skills/work/SKILL.md` from `rule-work-mode`.
> **＋** Or `/box` calls `/work` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec.

> **then:**
> `uv run guppi render --check` exits 0: `.claude/skills/work/SKILL.md` equals the Render of `rule-work-mode`.
> **＋** When a `!` substitution of `.claude/skills/work/SKILL.md` comes back empty, the agent runs its command itself — `git branch --show-current` before the check of the branch, `make test` and `make lint` before the first change — and uses that result.
> **＋** On the branch `main` the skill stops and says so, and nothing is written or changed.
> **＋** On another branch, before the first change, the agent writes `raw/<date>/<hi HHMM>/work.md`: under `## Baseline` the exit code of `make test` and of `make lint` with each failing test and each lint finding line as printed, and an empty `## Expected red`.
> **＋** When `work.md` already stands, its `## Baseline` stays as it is.
> **＋** The agent runs the tasks of `raw/<date>/<hi HHMM>/spec.md` in the order the Spec holds them, and ticks each box of code, a test, a migration or a `by hand` check in the reply that finishes the task; a task line that opens with a code span holding `guppi sprint-close` it neither runs nor ticks, since the librarian runs it.
> **＋** A task that changes `make lint`, one of its steps or a hook of the working tree that reads a page or a governed file the same Spec updates adds one line under `## Expected red` in the same reply: the check, and the page or file it waits for.
> **＋** With a folder from `/box`, `work.md` holds a third section, `## Conserved Spec`, naming the folder; the tasks run and ticked are those of that folder's `spec.md`; and the agent deletes that folder's `carry.md` when the last task is done, before the Work readings.
> **－** The skill writes no page of `vault/wiki/`, and it ticks no line of a page, a render, the sprint, the glossary or a reading.

> **tasks:**
> - [ ] update `rule-work-mode`
>   - old: `The lines of a page, a render, the sprint, the glossary and a reading are ticked by the librarian's scripts, not here.`
>   - new: `` The lines of a page, a render, the sprint, the glossary and a reading are ticked by the librarian's scripts, not here. A task line that opens with a code span holding `guppi sprint-close` is neither run nor ticked here: the librarian runs it, and the command ticks it (`rule-sprint-close`, case 628.4). ``
>   - change: `Work Mode leaves the close line of a sprint to the librarian (case 628.4)`
> - [ ] update `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
>   - set: `{status: pending, purpose: "Whether /work stops on main, writes the baseline of make test and make lint into work.md before the first change — running a command itself when its substitution is empty — and keeps it on a resume, runs the tasks of the Spec of the session or of the folder /box gives it in order with their ticks but leaves a guppi sprint-close line to the librarian, names that folder under Conserved Spec and deletes its carry.md, and marks an expected red under Expected red", method: "uv run guppi render --check; by hand, a /work the agent calls at the fork, a /work that /box calls and the /work of a session that closes a sprint: the branch, work.md, the ticks of the Spec, the guppi sprint-close line neither run nor ticked, the carry.md of the folder and each Expected red line read against the Criterion, and, where a substitution came back empty, the agent's own run of its command, recorded in the estimate line"}`
>   - change: `the Criterion replaced whole — a guppi sprint-close line is neither run nor ticked by Work Mode; purpose and method name it (case 628.4)`
> - [ ] `uv run guppi render`: `.claude/skills/work/SKILL.md`
> - [ ] read `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`

> **ratification:**
> ```
> - decision[case 628.4][update][rule-work-mode]{ref:rule-work-mode}
> - decision[case 628.4][update][estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline]{ref:rule-work-mode}
> ```

### Case 628.5 — The ticker of `guppi sprint` leaves the close line

> **given:**
> `estimate-sprint-ticks-the-spec` — its Criterion replaced whole, its `method` set anew
> **＋** `rule-sprint` — `guppi sprint`, which writes `vault/wiki/sprint.md` and ticks its lines in the Specs; one sentence changes
> **＋** `guppi/render.py` — `command_line`, the one matcher of the tickers of `render`, `sprint` and `glossary`
> **＋** `guppi/sprint.py` and `tests/test_sprint.py` — its docstring and its tests
> **＋** `vault/raw/` — the units whose `spec.md` the ticker reads
> **＋** `rule-sprint-close` — the close line, ticked by `guppi sprint-close`

> **when:**
> `guppi sprint` without a flag wrote `vault/wiki/sprint.md` and exits 0, and reads the units under `vault/raw/` that have a `materialize.yaml`.

> **then:**
> In the `spec.md` of every unit whose yaml is applied whole, every unticked task line that opens with a code span holding `guppi sprint` becomes `- [x]`. A yaml is applied whole when each entry carries `applied` or `superseded_by` and none carries `failed`. Nothing else in the file changes.
> **－** A line where `guppi sprint` sits in a later code span, such as a `read` line or a description, is not ticked.
> **－** A line whose first code span holds `guppi sprint-close` is not ticked: `guppi sprint-close` ticks it.
> **－** `--check` ticks nothing, and a run that exits 1 ticks nothing.
> **－** A unit without a yaml, with an entry not applied, with a `failed` entry, or marked by `carry.md`, is not touched.

> **tasks:**
> - [ ] update `rule-sprint`
>   - old: `` never a `read` line that names the command later — ``
>   - new: `` never a `read` line that names the command later, nor a line whose code span holds `guppi sprint-close`, which that command ticks (case 628.5) — ``
>   - change: `the ticker of guppi sprint leaves a guppi sprint-close line (case 628.5)`
> - [ ] update `estimate-sprint-ticks-the-spec`
>   - set: `{status: pending, method: "pytest tests/test_sprint.py; by hand, after a librarian's run, the spec.md of each unit under vault/raw/ whose guppi sprint line it ticked, and any guppi sprint-close line there left as it stood"}`
>   - change: `the Criterion replaced whole — a guppi sprint-close line is not ticked by guppi sprint (case 628.5)`
> - [ ] `guppi/render.py`: `command_line` matches the command only where no `-` or word character follows it; its docstring
> - [ ] `guppi/sprint.py`: the docstring names the close line as not ticked
> - [ ] `tests/test_sprint.py`: a `guppi sprint-close` line left unticked beside a ticked `guppi sprint` line
> - [ ] read `estimate-sprint-ticks-the-spec`

> **ratification:**
> ```
> - decision[case 628.5][update][rule-sprint]{ref:rule-sprint}
> - decision[case 628.5][update][estimate-sprint-ticks-the-spec]{ref:rule-sprint}
> ```

### Case 628.6 — A new page takes the sprint of its yaml

> **given:**
> `estimate-generate-writes` — its Criterion replaced whole
> **＋** `guppi/generate.py` and `tests/test_generate.py` — writes the pages; its docstring changes; its tests
> **＋** `guppi/materialize.py` — sets the yaml's `sprint` from a `create` of `entity-sprint-<id>`, by 628.3
> **＋** `vault/wiki/sprint.md` — whose first `## <id>` heading is the sprint id otherwise
> **＋** `vault/archive/` and `raw/` — where an entry whose slug is not live finds its page, `raw/` folders excluded
> **＋** `vault/wiki/log.md` and `vault/wiki/tags.md` — where `generate` appends
> **＋** `estimate-generate-fails-alone` — the promise of an entry that fails alone; unchanged

> **when:**
> `guppi generate` applies one entry of a yaml to a page.

> **then:**
> A `create` becomes a page: `type`, the fields of the entry, `status` by category (entity and rule `draft`, estimate `pending`, lesson `new`, insight `open`), `origin`, `sprint` — the `sprint` of the yaml, which `guppi materialize` takes from the first `## <id>` of `sprint.md` or, in a unit whose ledger creates `entity-sprint-<id>`, from that `<id>`, `created` — the yaml's date, `tags`; the body sections from `sections`, `## Purpose` from `purpose` on a rule or an entity; a `ref` lands in the parent's `children` or the target's `estimates` with History `child <slug> added` / `estimate <slug> added`, at the end of the run when the parent comes later in the yaml.
> **＋** An Estimate page carries `purpose`, `method` and `checked` as fields, in that order after `target`; `## Criterion` from `sections`; neither `## Context` nor `## Method` is written.
> **＋** A `create` whose slug is a placeholder (`draft`, no `kind`) fills it: `created` and `deferred_by` kept, History `created over placeholder`; any other existing page is a collision, not a rename.
> **＋** An `update` applies `set` to the frontmatter, `sections` as whole replacements, `replace` inside the body (whitespace collapsed, exactly one occurrence), History `updated: <change>`; an `update` of an Estimate with `sections.Criterion` replaces the section whole.
> **＋** An `update`, `estimate`, `delete` or `defer` whose slug is not under `vault/wiki/` finds the page under `vault/archive/` (`raw/` folders excluded) and edits it there.
> **＋** An `estimate` sets `status`, overwrites `## Result`, writes `checked` — the date the `result` opens with, else the yaml's date — and appends History `status: a → b · <ledger pointer>`.
> **＋** A `delete` sets `archived` with History `deleted`; a `delete` outside the vault is a line on stdout, the entry applied, no page written.
> **＋** A `defer` with a page appends the decision slug to `deferred_by` (rule, entity, insight) with History `deferred`; without a page it writes a placeholder `draft` with the Case's fields and `deferred_by`.
> **＋** A `lesson` writes the lesson only, `source` when the line carries it; no Estimate is created.
> **＋** Every ref field is written as `"[[slug]]"`, a list as `["[[a]]", "[[b]]"]`; a slug without a category prefix stays bare; read through the brackets.
> **＋** A `create` in `insights` applies only with the mark `librarian`; a `delete` of an Insight is refused always.
> **＋** History lines and `log.md` lines carry the date of the run and end with `[[decision-case-N]]` or the ledger pointer; `log.md` is appended after each entry; a tag of `new_tags` lands in `tags.md`, a used and undeclared one goes to stderr.
> **－** No body section is derived from a ref field; a section the entry does not name under `sections` or reach by `replace` is not touched.
> **－** An `update` of an Estimate whose `set` carries `method` drops no section.
> **－** `criterion_block` on an `update` and an entry of kind `remove_criterion` are not applied: a shape the script does not know — the entry fails alone (`estimate-generate-fails-alone`).

> **tasks:**
> - [ ] update `estimate-generate-writes`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a page's sprint is the sprint of the yaml, the new sprint's id in the unit that creates its page (case 628.6)`
> - [ ] `guppi/generate.py`: the docstring — `sprint` is the yaml's `sprint`, else the first `## <id>` heading of `sprint.md`
> - [ ] `tests/test_generate.py`: a yaml whose `sprint` differs from the heading of `sprint.md` writes the yaml's `sprint` on a created page
> - [ ] read `estimate-generate-writes`

> **ratification:**
> ```
> - decision[case 628.6][update][estimate-generate-writes]{ref:rule-page-generation}
> ```

### Case 628.7 — `/hi` puts the opening of the next sprint first and takes no item of a closed sprint

> **given:**
> `estimate-hi-writes-frontier` — its Criterion replaced whole, its `method` set anew
> **＋** `rule-skill-hi` — the skill `/hi`, rendered into `.claude/skills/hi/SKILL.md`; one sentence changes
> **＋** `vault/wiki/sprint.md`, `vault/wiki/brief.md` and `vault/wiki/backlog.md` — what `/hi` loads
> **＋** `vault/raw/<date>/<hi HHMM>/frontier.md` — the Frontier it writes
> **＋** `tests/test_prespec.py` — the frontier findings of `guppi prespec --check`
> **＋** `rule-sprint-close` — the gap between the close and the next sprint

> **when:**
> The person invokes `/hi`. The agent assembles the Frontier from `vault/wiki/sprint.md`, `vault/wiki/brief.md`, `vault/wiki/backlog.md` and the output of the skill's commands, and closes its lines in Plan Mode.

> **then:**
> The Frontier is written to `raw/<date>/<hi HHMM>/frontier.md` in the lists `## Cases`, with lines `- [ ] C<n> — <title> · <source>`, `## Work`, with lines `- [ ] W<n> — <title> · <source>`, and `## Ask`, with lines `` - [ ] A<n> — `<slug>` — <question> · brief ``. The title of a line of the current milestone or of the backlog opens with the slug of each of its pages in a code span.
> **＋** The kind comes from the source. Cases: first, when the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, that line, and then no item of the current milestone; on a plan branch, the unfinished plan and each conserved Spec of `vault/wiki/backlog.md`, with the source `backlog`; then the items of the current milestone; the `Cases` list of the brief's Next session; a hand edit shown by `Render:`; a `failed` reading or a lesson of the ledger's Tail; an item the person adds. Work: the `Work` list of the brief's Next session; a dirty tree by `git status`. Ask: the `Ask the person` list of the brief's Next session.
> **＋** The other items of the backlog are not lines. `## Cases` ends with the line `Backlog: N items`, where N is the count in `vault/wiki/backlog.md`. Under a Cases line, an indented line `- near` names by slug each backlog item whose `purpose` is near that line in meaning. The agent judges this from the loaded file, with no `ask-guppi`. An item the person brings onto the Frontier becomes a Cases line with the source `backlog`.
> **＋** A line closes by appending the closer and keeping the source. An item ended closes `[x] … · case N` when decided, or `[x] … · work` when done with no decision. A line of the sprint page left for a later session closes `[-] … · sprint · defer`. An item of the backlog left as it stands closes `[-] … · backlog · kept`. A decision of any other source put off closes `[-] … · defer case N`.
> **＋** An item closed `defer` or `kept` has no short Case and no ledger line. A sprint item never closes `· defer case N`.
> **＋** Only the current milestone gives items. A later milestone and Closed give none, and the sprint page's Backlog reaches the Frontier only through the backlog. A decision line of the Tail is not an item.
> **＋** In the chat the Cases are shown as a checklist. Each line stands as `raw/<date>/<hi HHMM>/frontier.md` holds it, `- [ ] C<n> — <title> · <source>`, with its detail on an indented line under it and the `- near` line under that, and the line `Backlog: N items` comes last. The Work is shown as one block. Only Cases are cut into sub-cases. A `W` that turns out to need a decision closes `· case N`. A `C` that needs none closes `· work`.
> **－** At `/hi` no Case stands in the chat as a bold line, and no Case has its detail as a paragraph.
> **－** Pre-spec finds an open line under `## Cases`. A `W` or an `A` line stands open until its work is done and closes `· work` where that work is done: at `/hi`, in Work Mode or at Retro. Claude Code's plan mode does not stop the agent from writing `frontier.md`.

> **tasks:**
> - [ ] update `rule-skill-hi`
>   - old: `and none of a later milestone, of the Backlog or of Closed (case 229.3);`
>   - new: `` and none of a later milestone, of the Backlog or of Closed (case 229.3) — and none at all while the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, which then stands as the first Cases line, before every other (`rule-sprint-close`, case 628.7); ``
>   - change: `the opening of the next sprint first, and no item of a closed sprint (case 628.7)`
> - [ ] update `estimate-hi-writes-frontier`
>   - set: `{status: pending, method: "by hand at the /hi of the session after the close of a sprint, written into the estimate line; unit: the frontier findings of guppi prespec --check in tests/test_prespec.py"}`
>   - change: `the Criterion replaced whole — the opening of the next sprint first, no milestone item while it stands (case 628.7)`
> - [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] read `estimate-hi-writes-frontier`

> **ratification:**
> ```
> - decision[case 628.7][update][rule-skill-hi]{ref:rule-skill-hi}
> - decision[case 628.7][update][estimate-hi-writes-frontier]{ref:rule-skill-hi}
> ```

### Case 628.8 — The brief of the closing run names the opening of the next sprint first

> **given:**
> `estimate-brief-written` — its Criterion replaced whole, its `method` set anew
> **＋** `rule-brief` — the brief step of the librarian, rendered into `.claude/agents/librarian-guppi.md`; one sentence changes
> **＋** `rule-carry-over` — the skill `carry`, the second writer of the brief
> **＋** `vault/wiki/brief.md` — the brief
> **＋** `vault/raw/<date>/<hi HHMM>/handoff.md` and `vault/raw/<date>/<hi HHMM>/frontier.md` — what the brief takes its lists from
> **＋** `vault/wiki/backlog.md` and `vault/wiki/sprint.md` — where the deferred items and the sprint items stand
> **＋** `rule-sprint-close` — the close, run by `guppi sprint-close --apply`

> **when:**
> The librarian rewrites `vault/wiki/brief.md` at the end of its run.

> **then:**
> The brief holds, in order: Where things stand, Readings due, Flags, Next session, Readings at the close.
> **＋** It holds no Deferred list and no cap on deferred items. They stand in `vault/wiki/backlog.md`.
> **＋** Where things stand, Readings due and Readings at the close are as before.
> **＋** Readings due takes from each Estimate page its `status`, `target` and `method`, and from the target rule its `status`.
> **＋** Flags keep their kinds of lines — marked entries, failed Estimates, MOC candidates, stale defers, contradictions, the lint output — and add one kind: a read that the librarian's frame says its job does not need, with what was read, the part of the job it served, and the handoff when the handoff asked for it.
> **＋** Next session holds `Cases`, `Work` and `Ask the person`. `Cases` is what needs a decision: after a run whose `guppi sprint-close --apply` moved the sprint page, first the line `open the next sprint — no sprint is open since the close of <id>`; a line of `## For the next session` of `handoff.md`, a handoff flag with a question or a request to change the sprint, a `failed` Estimate, a contradiction, a defect the librarian found; one line per item, with what and from where. `Work` is what is done without a decision: every `pending` reading of Readings due by its slug but one that `Ask the person` holds, the unticked boxes of the Specs, a ledger line this run did not apply, a dirty tree; one line per item.
> **＋** `Ask the person` holds each line of `## Ask the person` of `handoff.md`: the Estimate by slug, the mark `needs the person` and its question, as the handoff wrote them.
> **＋** An item stands in one list only. A list with no item is the line "none".
> **＋** The brief of the skill `carry` keeps a short shape: Where things stand, Flags and Next session, without Readings due, Readings at the close and a Deferred list. In its Next session, `Work` and `Ask the person` take the open `W` and `A` lines of the session's `frontier.md`, and `Cases` is the line "none", since a deferred decision stands in `vault/wiki/backlog.md` and a sprint item on `vault/wiki/sprint.md`. `rule-brief` and `rule-carry-over` both say so.
> **－** The brief states no decision: the sort by kind is not a judgment of the work.

> **tasks:**
> - [ ] update `rule-brief`
>   - old: `` `Cases`, what needs a decision: a line of `## For the next session` of `handoff.md`, ``
>   - new: `` `Cases`, what needs a decision: after a run whose `guppi sprint-close --apply` moved the sprint page, first the line `open the next sprint — no sprint is open since the close of <id>` (`rule-sprint-close`, case 628.8); a line of `## For the next session` of `handoff.md`, ``
>   - change: `after a close, the opening of the next sprint is the first Cases line (case 628.8)`
> - [ ] update `estimate-brief-written`
>   - set: `{status: pending, method: "by hand at the /hi after the librarian's run of the session that closes a sprint, recorded in the estimate line"}`
>   - change: `the Criterion replaced whole — after a close, the first Cases line opens the next sprint (case 628.8)`
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] read `estimate-brief-written`

> **ratification:**
> ```
> - decision[case 628.8][update][rule-brief]{ref:rule-brief}
> - decision[case 628.8][update][estimate-brief-written]{ref:rule-brief}
> ```

### Case 628.9 — `make test` of migration is read before the close, and its merge into `main` goes to the next sprint

> **given:**
> `estimate-sprint-migration-merges` — its Criterion replaced whole, its `purpose` and `method` set anew
> **＋** `entity-sprint-migration` — the sprint page: its Slice 5 note, a phrase of its Purpose and a new line of its `## Backlog`
> **＋** `decision-case-615` — the question put off on that page, closed by this update
> **＋** `vault/raw/2026-10-04/1439/cases/case-627.md` — Case 627, which updates the other line of the same milestone and carries the same mark
> **＋** `rule-sprint-close` — the close, run by the librarian after the Work Mode of the closing session
> **＋** `migration` and `main` — the branch of the sprint and the branch it merges into
> **＋** `make test` — the tests of the repository

> **when:**
> In the Work Mode of the session that closes `entity-sprint-migration`, before the librarian's run, someone runs `make test` on the last commit of the branch `migration`.

> **then:**
> `make test` is green on the last commit of `migration`.
> **－** The merge of `migration` into `main` is not part of this promise: it is the first work of the session that opens the next sprint, a line of the `## Backlog` of `entity-sprint-migration`.

> **tasks:**
> - [ ] update `entity-sprint-migration`
>   - old: `where the close of a sprint runs — a session of its own, a command or another place: not decided (case 612.1)`
>   - new: `` the close of migration — a session of its own: the pending readings taken in groups, `make test`, `make lint` and the tree read in its Work Mode, then `uv run guppi sprint-close --sprint migration --apply` in the librarian's run (case 628.9) ``
>   - old: `the leftovers gone, the branch merged,`
>   - new: `` the leftovers gone, `make test` green on the last commit of `migration`, ``
>   - old:
>     ```
>     - [[rule-morph]] — the morph mechanism: the initiation at install sets the category set of the project, the development set by default, held as data so that a changed set rewrites no rule; case 239
>     ```
>   - new:
>     ```
>     - [[rule-morph]] — the morph mechanism: the initiation at install sets the category set of the project, the development set by default, held as data so that a changed set rewrites no rule; case 239
>     - the merge of `migration` into `main` — the first work of the session that opens the next sprint, after its opening Case (case 628.9)
>     ```
>   - change: `the Slice 5 note on where the close runs cut into the close of migration; make test in the Purpose for the branch merged; the merge a Backlog line for the next sprint; the question put off by case 615 closed (case 628.9)`
> - [ ] update `estimate-sprint-migration-merges`
>   - set: `{status: pending, purpose: "make test green on the last commit of migration, read in the Work Mode of the session that closes it", method: "make test on the last commit of migration, in the Work Mode of the session that closes it, before the librarian's run"}`
>   - change: `the Criterion replaced whole — read before the close; the merge into main and the line on sprint.md leave this promise (case 628.9)`
> - [ ] read `estimate-sprint-migration-merges`

> **ratification:**
> ```
> - decision[case 628.9][update][entity-sprint-migration]{ref:entity-sprint-migration}{supersedes:case 615}
> - decision[case 628.9][update][estimate-sprint-migration-merges]{ref:entity-sprint-migration}
> ```

### Case 628.10 — `make lint` of migration is read before the close

> **given:**
> `estimate-sprint-migration-lint-clean` — its Criterion replaced whole, its `purpose` and `method` set anew
> **＋** `entity-sprint-migration` — the sprint page whose Estimates are the one exception
> **＋** `rule-sprint-close` — the close, run by the librarian after the Work Mode of the closing session
> **＋** `make lint` — the checks of the vault and the scripts

> **when:**
> In the Work Mode of the session that closes `entity-sprint-migration`, before the librarian's run, someone reads `make lint`.

> **then:**
> `make lint` exits 0: no finding in any category, `unmigrated` included — the old Estimate shape is gone, the counter at zero; the one exception is `unread` on the Estimates of the sprint page itself not yet read at that moment.

> **tasks:**
> - [ ] update `estimate-sprint-migration-lint-clean`
>   - set: `{status: pending, purpose: "make lint exits 0 in the Work Mode of the session that closes the sprint, before the librarian's run, unmigrated included, but for the unread of the sprint page's own Estimates", method: "make lint in the Work Mode of the session that closes the sprint, before the librarian's run, exit 0 — or only unread lines on the Estimates of entity-sprint-migration"}`
>   - change: `the Criterion replaced whole — read in the Work Mode of the closing session, before the close (case 628.10)`
> - [ ] read `estimate-sprint-migration-lint-clean`

> **ratification:**
> ```
> - decision[case 628.10][update][estimate-sprint-migration-lint-clean]{ref:entity-sprint-migration}
> ```

### Case 628.11 — The leftovers of migration are read before the close

> **given:**
> `estimate-sprint-migration-leftovers-gone` — its Criterion replaced whole, its `purpose` and `method` set anew
> **＋** `entity-sprint-migration` — the sprint page it checks
> **＋** `rule-sprint-close` — the close, run by the librarian after the Work Mode of the closing session
> **＋** `rule-raw-archive` — keeps the `event_log.md` of a past date in `vault/raw/<date>/`
> **＋** `vault/parked/`, `docs/`, `docs/migration/migration-plan.md`, `vault/archive/`, `vault/raw/`, the session folders `vault/raw/<date>/<HHMM>/` and `.claude/skills/hi/SKILL.md` — the paths the reading looks at

> **when:**
> In the Work Mode of the session that closes `entity-sprint-migration`, before the librarian's run, someone reads the tree of the repository.

> **then:**
> `vault/parked/` is absent: its pages were deleted by a decision named in the reading, and git history keeps them.
> **＋** Under `docs/` no 2026-08 document remains, and no rule document of `docs/migration/`; each became a page, was archived, or was deleted by a decision named in the reading.
> **＋** `vault/archive/` has no root outside the folders of its sprints, and the decision that deleted the old root is named in the reading.
> **＋** Every file under `vault/raw/` that git tracks lies in a session folder `vault/raw/<date>/<HHMM>/`.
> **＋** The repository has no remote, and `.claude/skills/hi/SKILL.md` runs neither `git pull` nor `gh`; the decision is named in the reading.
> **－** `docs/migration/migration-plan.md` is outside this promise: the Case that closes the sprint deletes it.
> **－** The `event_log.md` of a past date stays in `vault/raw/<date>/`, as `rule-raw-archive` keeps it, and does not fail this promise.

> **tasks:**
> - [ ] update `estimate-sprint-migration-leftovers-gone`
>   - set: `{status: pending, purpose: "vault/parked/, the 2026-08 documents and the old archive root are gone, git tracks no raw date folder without a session, and the repository has no remote, each by a decision named in the reading, read in the Work Mode of the session that closes the sprint", method: "one reading of the tree by hand in the Work Mode of the session that closes the sprint, before the librarian's run, each path and decision named in the estimate line"}`
>   - change: `the Criterion replaced whole — read in the Work Mode of the closing session, before the close (case 628.11)`
> - [ ] read `estimate-sprint-migration-leftovers-gone`

> **ratification:**
> ```
> - decision[case 628.11][update][estimate-sprint-migration-leftovers-gone]{ref:entity-sprint-migration}
> ```

### Case 628.12 — The Backlog of a closed sprint page stays in `backlog.md`

> **given:**
> `estimate-backlog-renders` — its Criterion replaced whole, its `purpose` and `method` set anew
> **＋** `rule-backlog` — `guppi backlog`, which writes `vault/wiki/backlog.md`; one phrase of its Purpose changes
> **＋** `guppi/backlog.py` and `tests/test_backlog.py` — the script and its tests
> **＋** `guppi/materialize.py` and `guppi/generate.py` — the Spec reader and `generate.frontier_marks`, which the script imports
> **＋** `entity-sprint-<id>` — each sprint page, live under `vault/wiki/entities/` or archived under `vault/archive/`
> **＋** `vault/raw/`, `vault/archive/`, `carry.md` and `frontier.md` — the conserved Specs and the Frontier files the script reads
> **＋** `rule-sprint-close` — the close that archives the sprint page

> **when:**
> `uv run guppi backlog` runs over `vault/wiki/`, `vault/raw/` and `vault/archive/`. The librarian runs it after `guppi sprint`, and the skill `carry` runs it after it writes `carry.md`.

> **then:**
> The script writes `vault/wiki/backlog.md`: the heading `# Backlog`, the line `N items`, then `## Conserved Specs` and `## Deferred`.
> **＋** `## Conserved Specs` holds each session folder under `vault/raw/` that holds `carry.md`. Each has one line that names its `spec.md` and its Cases. Under that line stands one line per item of its `then` blocks, with the kind and the slug, read by the Spec reader of `guppi/materialize.py`.
> **＋** `## Deferred` holds one line per item. The items are each live page with a `deferred_by` that is not empty, each Insight whose `status` is `open`, and each line of the `## Backlog` of each `entity-sprint-<id>`, live under `vault/wiki/entities/` or archived under `vault/archive/`. A line holds the slug, the page's `purpose` (for an Insight, its `pattern` and `severity`) and the count. A Backlog line that names no page stands by its text.
> **＋** The count of an item is the number of sessions whose `frontier.md`, under `vault/raw/` or `vault/archive/`, holds a `[-]` line that names its slug in a code span of its title. It is read by `generate.frontier_marks`, and `guppi/backlog.py` holds no copy of that reader.
> **＋** `N` counts the conserved Specs and the lines of `## Deferred`. A slug that stands under a conserved Spec does not stand again under `## Deferred`, and a slug of two sources stands once.
> **＋** A folder whose `carry.md` is gone shows nothing. Its defers enter `## Deferred` through `deferred_by` once `materialize` and `generate` have applied them.
> **－** The script writes no page of `vault/wiki/` and no file but `vault/wiki/backlog.md`. The governed-files hook refuses a hand edit of that file.

> **tasks:**
> - [ ] update `rule-backlog`
>   - old: `` each line of the `## Backlog` of the sprint page — ``
>   - new: `` each line of the `## Backlog` of each sprint page, live or under `vault/archive/`, so that the Backlog of a closed sprint stays in the list (`rule-sprint-close`, case 628.12) — ``
>   - change: `the Backlog of an archived sprint page stays in backlog.md (case 628.12)`
> - [ ] update `estimate-backlog-renders`
>   - set: `{status: pending, purpose: "guppi backlog writes backlog.md from the conserved Specs, the pages with deferred_by, the open Insights and the Backlog of each sprint page, live or archived, each item with its purpose and its count", method: "uv run pytest tests/test_backlog.py, plus one reading of vault/wiki/backlog.md after the librarian's run of the session that closes a sprint"}`
>   - change: `the Criterion replaced whole — the Backlog of each sprint page, live or archived (case 628.12)`
> - [ ] `guppi/backlog.py`: read the `## Backlog` of each `entity-sprint-<id>` page under `vault/archive/` too, by the item reader of `guppi/sprint.py`; the docstring
> - [ ] `tests/test_backlog.py`: the Backlog lines of an archived sprint page and of a live one both shown, a slug of both standing once
> - [ ] read `estimate-backlog-renders`

> **ratification:**
> ```
> - decision[case 628.12][update][rule-backlog]{ref:rule-backlog}
> - decision[case 628.12][update][estimate-backlog-renders]{ref:rule-backlog}
> ```
