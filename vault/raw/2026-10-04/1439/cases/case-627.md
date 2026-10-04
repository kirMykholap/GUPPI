## Case 627 — The close of a sprint as a command that goes ahead once the sprint page's own Estimates are settled

> **context:**
> `rule-sprint-close` says what the close of a sprint moves to the archive and what it keeps. Case 612 decided this. No code does it today. A page leaves `vault/wiki/` only when `guppi cleanup` moves it, and `guppi cleanup` moves only a page that already stands `archived`. The rule also sets a condition: pages move only after every Estimate of the sprint page has passed. These two facts block each other. The four Estimates of the rule are each read "after the first close of a sprint", and that close is the close of migration. That close cannot run, because the Estimates of `entity-sprint-migration` are read only at the close itself. For example, `estimate-sprint-migration-merges` says that the cascade sets the sprint page `built` and that this is the close. The rule page also gave its code and the change of the schema texts to the Case that decides where the close runs, which is the next item of the Frontier.
>
> The person chose that this Case builds the tool and leaves the place to the next Case (627.1 to 627.4). The command is `uv run guppi sprint-close --sprint <id>`. Without `--apply` it prints what would move, what stays and each Estimate that stands `pending` or `failed`, and it changes nothing. With `--apply` it marks the pages `archived`, writing them through the writer of `guppi/generate.py` as `guppi cleanup` already does, and then runs `guppi cleanup`. The person's choices reach the run by slug, `--carry <slug>` and `--archive-unread <slug>`. The run refuses and moves nothing while a listed Estimate has neither passed nor been named. The person saw that the close could never pass if it waited for its own Estimates. So the close goes ahead with the sprint page's own Estimates not passed: each one is read or archived unread, never carried, because the page it checks goes to the archive.
>
> After ratification the person asked for two changes. First, each of the four Estimates is read in two parts. A pytest test runs the command with `--apply` over a small made-up vault. A reading by hand compares the preview over the live vault, `uv run guppi sprint-close --sprint migration`, with the Then. No real close is needed for either part. This session updates the four Estimates, and the ledger hook refuses a reading of an Estimate that its own session creates or updates (case 428.1). So the four are read in a later session, and at the close of migration they need not be carried. This replaces the When of each of the four whole: the old When line, with its condition that each Estimate stands `passed`, is not carried, and that is on purpose. Each Then keeps its lines word for word and gains one line on what the preview shows, since a preview moves nothing and the old lines speak only of pages under `vault/archive/`. Second, an Estimate read now whose reading comes out `failed` counts as settled. Before this change such an Estimate was neither passed nor named, so the run refused for good, and for an Estimate of the sprint page, which cannot be carried, there was no way out. Now it is carried by `--carry`, or, when the sprint page lists it, it goes to the archive with the sprint page with no choice by name, and the record of the close keeps its status. The Then of `estimate-sprint-close-settles-unread-estimates` also gains the one exception on carrying. The four Thens share words because they all describe pages moving to `vault/archive/`, and the lines on the preview are worded alike on purpose. Each Then still checks a different kind of page, or, in 627.4, the settling of Estimates and not their move, so they stay four promises. The `method` of all four is set anew, and so is the `purpose` of `estimate-sprint-close-settles-unread-estimates`, which stated the old choice of three ways for every Estimate. The other three purposes do not name the condition and stand. The close of migration does not run in this session.
>
> Case 628 of this session, in `vault/raw/2026-10-04/1439/cases/case-628.md`, decides where the close runs. In 628.1 the close runs in the librarian's run of a session of its own, from the task line of the closing Case, after `guppi generate` and before `guppi cleanup`. It writes this into a new section `## How it works` of `rule-sprint-close`, beside the Purpose that 627.1 writes. At the person's request, the last sentence of that Purpose points to `## How it works`, in place of saying that where the close runs is not decided. The rest of the Purpose agrees with that section: the command runs `guppi cleanup` itself, and Case 628 says that the librarian's own later `guppi cleanup` step then moves nothing. Case 628 also replaces the Criterion of `estimate-sprint-migration-merges`, settles the sentence of `rule-documentation` on the librarian as the only writer, and sends the `## Backlog` lines of a closed sprint page to `backlog.md`. That last point is the person's answer at `/pre-spec`, and it makes no text of this Case false, since 627.3 says only that the sprint page goes to the archive. Case 628 is being built again at the same time as this Case, so its new text was not read beside this one.
>
> `/pre-spec` found that this Case closes the Frontier line of the sprint item `rule-sprint-close` but changes no line of the sprint page. So 627.1 now names this Case on that item's line of `entity-sprint-migration`, by one `replace` of that line alone. Case 628 changes other lines of the same page: the Slice 5 note, a phrase of its Purpose and a line of its `## Backlog`. The page carries the deferred decision `decision-case-615`, which asked how much is left for the close of migration: which pending Estimates are read, carried or archived before the close. `backlog.md` lists the page for it. In Q3 the person had chosen to leave that question open. Changing the page made that choice impossible, and the person chose in Q8 to close the question with this update. The question is answered by the step that settles each pending Estimate at the close (627.4), by the readings taken in groups (628.2), and by the four Estimates read without a real close. So the decision line of 627.1 on `entity-sprint-migration` carries `{supersedes:case 615}`, and Case 628 carries the same mark on its own line.
>
> Frame checks. A Grep of `stays live|archived only|never archived|kept for the recurrence|archive is not needed|Archived when` over the repository outside `vault/archive/`, `vault/raw/` and `vault/wiki/decisions/` printed 14 lines in 10 files:
> - `guppi/generate.py`
> - `vault/wiki/insights/schema.yaml`
> - `.claude/agents/librarian-guppi.md`
> - `rule-insights-schema.md`
> - `rule-lessons-schema.md`
> - `rule-sprint-close.md`
> - `vault/wiki/lessons/schema.yaml`
> - `rule-synthesis.md`
> - `estimate-synthesis-clusters.md`
> - `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest.md`
>
> The hit in `guppi/generate.py`, line 1226, is a docstring on a child read in the archive, and it stays true. The three rendered files change through their rule pages: 627.2 changes `rule-insights-schema` and `rule-lessons-schema`, and 627.5 changes `rule-synthesis`. `/pre-spec` also found that the sentence of `rule-lessons-schema` saying a lesson with no pair stays `new` and is reconsidered next session becomes false at a close, so 627.2 replaces it too. The person chose in 627.5 to replace the Criterion of `estimate-synthesis-clusters`, since its reason that an actioned Insight stays live becomes false after a close. In that Criterion only that reason changes. Its line that a lesson without a pair stays `new` speaks of one librarian run, and it stays true. `estimate-synthesis-keeps-actioned-by-the-mark` speaks of an Insight that is live and `actioned` while the synthesis runs. That still holds inside a sprint, so its Criterion stands. The `status` field of `rule-decisions-schema` says that only the cascade archives a Decision page, so 627.1 changes it. A Grep of `only (writer|script that writes)|the one writer|writes? (a|every) page|status the generator` over `vault/wiki/` printed `glossary.md`, `entity-glossary.md`, `rule-documentation.md`, `rule-cleanup.md`, `rule-page-generation.md` and 8 Decision pages, which were not read. `rule-cleanup` says that `archived` is a status the generator sets, so 627.1 changes it. `rule-page-generation` says that `generate` is the only writer to `wiki/`. That sentence stands in the sense it already has beside `guppi cleanup`, which writes History lines and moves pages through the same writer. `estimate-cleanup-moves` checks the move of a page marked `archived`, and it does not say who sets the mark, so its Criterion stands. The moment this Case sets is the close of a sprint. A Grep of `sprint-close|sprint_close|close of (a|the) sprint` over the repository outside `vault/archive/` and `vault/raw/` printed 52 files. Under `vault/wiki/rules/` and `.claude/` it printed only `rule-sprint-close.md`. In code it printed only `tests/test_lint.py` and `tests/test_prespec.py`, whose hits are sample methods of the check of a reading tied to a one-off moment. The new methods name no first moment, so that check passes them. A Grep of `rule-sprint-close` outside `vault/archive/`, `vault/raw/` and `vault/wiki/decisions/` hit `brief.md`, `sprint.md` and `log.md`, which were not read. It also hit `entity-sprint`, `entity-sprint-migration`, the four Estimates and the Result of `estimate-case-build-writes-the-case`, and all of these stay true. A Grep over `vault/raw/2026-10-04/1439/cases/case-629.md` for the headings and the slugs of the pages this Case changes printed its headings and one line of its `context`. Case 629 changes the check of a built Case and none of these pages. No `create` is proposed, so the vault query was not run.

> **problem:**
> Nothing does the close of a sprint, and its four Estimates cannot be read: they wait for a close that waits for every reading, the sprint page's own included. The question is what this Case builds, what condition lets the close go ahead, and how its checks get read.

> **recommend:**
> - **What does this Case build, and what does it leave to the Case on where the close runs?**
>   - Recommended: (a) the tool here, the place there: one command, `guppi sprint-close`, marks the pages `archived` for `guppi cleanup`, with a preview that changes nothing; this Case changes the texts the moves make false; the next Case sets who calls it, when, and how the next sprint opens.
>   - Answer: (a).
> - **How do the four Estimates of the close get a moment when they can be read?**
>   - Recommended: (a) a pytest test over a made-up vault and the preview over the live vault, read in this session, each Criterion replaced to name the command.
>   - Answer: (b): each method gains the pytest test, the When and Then stay, and the reading by hand waits for a real close.
> - **What does this Case do with the three Estimates of migration itself?**
>   - Recommended: (a) leave them to the close; the preview lists them; the deferred decision on `entity-sprint-migration` stays open.
>   - Answer: (a). The person added that if every Estimate had to pass at the close, the sprint could never close, since its own Estimates wait for the real close. So the close must be allowed with Estimates not passed, and this can change later. The mechanism is settled now, and the close itself runs later.
> - **What must be true before the close moves any page?**
>   - Recommended: (a) settled, not passed: each Estimate of the sprint page that has not passed is read now or archived unread with the sprint page, never carried; the text of `rule-sprint-close` and the When of the four Estimates change; their Then stays.
>   - Answer: agreed.
> - **How do your choices on pending Estimates reach the command?**
>   - Recommended: (a) by slug on the command line, `--carry <slug>` and `--archive-unread <slug>`; an Estimate read now is read before the run; the run refuses while a listed Estimate has neither passed nor been named.
>   - Answer: agreed.
> - **What happens to a check of the synthesis that says an actioned Insight stays live for good?**
>   - Recommended: (a) replace the Criterion of `estimate-synthesis-clusters` whole, so that an actioned Insight stays live until the close of its sprint; read again at the next librarian run with at least two lesson entries.
>   - Answer: agreed.
> - **Can an Estimate of the sprint page be carried into the next sprint?**
>   - Recommended: (a) add the exception to the Then of `estimate-sprint-close-settles-unread-estimates`: an Estimate the sprint page lists is read now or archived unread.
>   - Answer: agreed.
> - **Change**
>   - Asked: both changes. Read the four Estimates over the preview of the command on the live vault, beside a pytest test over a made-up vault, so that they are read in Work Mode and need not be carried at the close of migration. Close the gap of a reading that comes out `failed`: such an Estimate counts as settled, carried by `--carry`, or archived with the sprint page when the sprint page lists it, its status kept in the record of the close.
>   - Taken: the When of each of the four names the run with `--apply` over the made-up vault of `tests/test_sprint_close.py` or the preview over the live vault. Each Then keeps its lines and gains one line on what the preview shows. Each method is a pytest test and a reading by hand of the preview of migration. The ledger hook refuses a reading of an Estimate that its own session updates (case 428.1), so the four are read in a later session, with no real close needed, not in this Work Mode. The Then of 627.4 gains the line on a failed reading. The rule's Purpose says that an Estimate of the sprint page that stands `failed` goes with the sprint page with no choice by name. The tests of `-k settle` gain the failed case.
> - **Change**
>   - Asked: in 627.1 only, the last sentence of the Purpose of `rule-sprint-close` points to the section `## How it works` that Case 628.1 writes on the same page, in place of saying that where the close runs and how the next sprint opens are not decided.
>   - Taken: the last sentence of the Purpose now reads that these are set in `## How it works` of this page (case 628.1). The `given` of 627.1 names the case file of Case 628.
> - **Does the change to the sprint page also close the question put off on it?**
>   - Recommended: (a) close the question with this update: the decision line of this Case on `entity-sprint-migration` carries the mark that closes the deferred decision, which the settling step, the readings in groups and the four Estimates read without a real close answer; Case 628 carries the same mark; this Case changes only its own milestone line.
>   - Answer: agreed.

### Case 627.1 — The command closes a sprint and archives its Decision pages

> **given:**
> `rule-sprint-close` — the rule of the close of `entity-sprint-<id>`, a Leaf under `entity-sprint`; its Purpose and guard change
> **＋** `vault/raw/2026-10-04/1439/cases/case-628.md` — Case 628, whose 628.1 writes `## How it works` of the same page
> **＋** `entity-sprint-migration` — the sprint page; the line of its item `rule-sprint-close` names this Case
> **＋** `guppi/sprint_close.py` — the new command `guppi sprint-close`, its preview and its run with `--apply`
> **＋** `guppi/cli.py` — registers the command
> **＋** `tests/test_sprint_close.py` — the tests over a made-up vault of one sprint
> **＋** `rule-cleanup` — moves each page marked `archived` under `vault/archive/`; one sentence changes
> **＋** `rule-decisions-schema` — the `status` field of a Decision page under `vault/wiki/decisions/`
> **＋** `vault/wiki/decisions/schema.yaml` — rendered from `rule-decisions-schema`
> **＋** `estimate-sprint-close-archives-the-decisions` — its When replaced, its Then kept with one line added, its method set anew

> **when:**
> `uv run guppi sprint-close --sprint <id> --apply` closes the sprint `entity-sprint-<id>` of the made-up vault of `tests/test_sprint_close.py`, after each Estimate that `entity-sprint-<id>` lists and that does not stand `passed` is read or archived unread, as the person chooses; someone reads `vault/wiki/decisions/` and `vault/archive/` after it.
> **＋** Or the preview `uv run guppi sprint-close --sprint <id>` runs over the live vault, and someone reads its output against `vault/wiki/decisions/`.

> **then:**
> Each Decision page under `vault/wiki/decisions/` whose `sprint` is `<id>` stands under `vault/archive/`.
> **＋** The preview names each such page among the pages the close would move, and moves none.
> **－** A Decision page that a live page names in `deferred_by` or `addressed_by` stays under `vault/wiki/decisions/`.
> **－** A Decision page whose `sprint` is another sprint does not move.

> **tasks:**
> - [ ] update `rule-sprint-close`
>   - set: `{enforcement: check, implementation_ref: [guppi/sprint_close.py, tests/test_sprint_close.py]}`
>   - sections.Purpose:
>     ````
>     Prevents a closed sprint from leaving its finished work among the live pages, so that the vault does not only grow. `uv run guppi sprint-close --sprint <id>` closes `entity-sprint-<id>`: without `--apply` it prints what the close would move, what it keeps and each Estimate under `vault/wiki/estimates/` that stands `pending` or `failed`, and changes nothing; with `--apply` it sets `archived` on each page the close moves, with a History line, and runs `guppi cleanup`, which moves them (case 627.1). Before anything moves, each Estimate that stands `pending` or `failed` is put to the person, who has it read, carries it into the next sprint, or archives it unread (case 612.4); the run takes the choices by slug, `--carry <slug>` and `--archive-unread <slug>`, an Estimate read now being read before the run, and refuses, moving nothing, while a listed Estimate has neither passed nor been named. An Estimate that the sprint page lists is read now or archived unread with the sprint page, never carried, so the close goes ahead with the sprint page's own Estimates not passed; one read now whose reading came out `failed` goes to the archive with the sprint page with no choice by name, and any other Estimate whose reading came out `failed` is carried by `--carry`; the record of the close keeps its status (case 627.4). Then the Decision pages of the sprint go to the archive, but a Decision page that a live page names in `deferred_by` or `addressed_by` stays (case 612.1). The `actioned` Insights of the sprint go, and its `error` lessons that joined no Insight; its `knowledge` lessons, its `open` Insights and their lessons stay (case 612.2). The sprint page and the Estimates it lists go; every other `passed` Estimate stays, the contract of its rule (case 612.3). Where the close runs — who calls the command and at what moment — and how the next sprint opens are set in `## How it works` of this page (case 628.1).
>     ````
>   - change: `the close is the command guppi sprint-close, its preview and its run with --apply, the choices by slug; the close goes ahead once each Estimate of the sprint page is read or archived unread, a failed reading settling it; the guard named; where the close runs pointed to How it works (case 627.1)`
> - [ ] update `entity-sprint-migration`
>   - old: `[[rule-sprint-close]] — what the close of a sprint moves to the archive and what it keeps (case 612.1)`
>   - new: `[[rule-sprint-close]] — what the close of a sprint moves to the archive and what it keeps (cases 612.1, 627)`
>   - change: `Slice 5: the item rule-sprint-close names case 627, which builds the command of the close; the question put off by case 615 closed (case 627.1)`
> - [ ] update `rule-decisions-schema`
>   - old: `` `archived` the moment the cascade of `generate` meets it so: a superseded Decision no longer describes the present (case 104.1). ``
>   - new: `` `archived` the moment the cascade of `generate` meets it so: a superseded Decision no longer describes the present (case 104.1); `guppi sprint-close` also sets `archived` on a Decision page of the sprint it closes, but for one that a live page names in `deferred_by` or `addressed_by` (`rule-sprint-close`, case 627.1). ``
>   - change: `a Decision page is archived also by the close of its sprint (case 627.1)`
> - [ ] update `rule-cleanup`
>   - old: `` `archived` is a status the generator sets. ``
>   - new: `` `archived` is a status the generator sets, and `guppi sprint-close` at the close of a sprint (`rule-sprint-close`, case 627.1). ``
>   - change: `guppi sprint-close also sets archived (case 627.1)`
> - [ ] update `estimate-sprint-close-archives-the-decisions`
>   - set: `{status: pending, method: "pytest tests/test_sprint_close.py -k decisions; by hand, the output of the preview uv run guppi sprint-close --sprint migration over the live vault read against the Then"}`
>   - change: `the When replaced whole — the run with --apply over a made-up vault, after each Estimate of the sprint page not passed is read or archived unread, or the preview over the live vault; the Then kept, one line on the preview added; the method a pytest test and the preview of migration (case 627.1)`
> - [ ] `guppi/sprint_close.py`: the command — the preview, the choices by slug, the refusal while a listed Estimate is neither passed nor named, the marks through the writer of `guppi/generate.py`, then `guppi cleanup`
> - [ ] `guppi/cli.py`: `sprint-close` registered
> - [ ] `tests/test_sprint_close.py`: `-k decisions` — over a made-up vault of one sprint, the Decision pages of the sprint archived, one named in `deferred_by` and one in `addressed_by` of a live page kept, one of another sprint kept; the preview names the same pages and moves none; the clock pinned
> - [ ] `uv run guppi render`: `vault/wiki/decisions/schema.yaml`
> - [ ] `uv run guppi sprint`
> - [ ] read `estimate-sprint-close-archives-the-decisions`

> **ratification:**
> ```
> - decision[case 627.1][update][rule-sprint-close]{ref:rule-sprint-close}
> - decision[case 627.1][update][entity-sprint-migration]{ref:entity-sprint-migration}{supersedes:case 615}
> - decision[case 627.1][update][rule-decisions-schema]{ref:rule-decisions-schema}
> - decision[case 627.1][update][rule-cleanup]{ref:rule-cleanup}
> - decision[case 627.1][update][estimate-sprint-close-archives-the-decisions]{ref:rule-sprint-close}
> ```

### Case 627.2 — The close archives the actioned Insights and the lone error lessons of the sprint

> **given:**
> `estimate-sprint-close-archives-done-insights-and-lone-lessons` — its When replaced, its Then kept with one line added, its method set anew
> **＋** `entity-sprint` — the MOC over the sprint pages `entity-sprint-<id>`
> **＋** `guppi/sprint_close.py` — selects the Insights and lessons of the sprint
> **＋** `tests/test_sprint_close.py` — the tests over a made-up vault of one sprint
> **＋** `rule-cleanup` — moves each page marked `archived` under `vault/archive/`
> **＋** `rule-insights-schema` — when an Insight under `vault/wiki/insights/` and a Lesson are archived
> **＋** `vault/wiki/insights/schema.yaml` — rendered from `rule-insights-schema`
> **＋** `rule-lessons-schema` — the `status` field of a lesson under `vault/wiki/lessons/`, and the sentence on a lesson with no pair
> **＋** `vault/wiki/lessons/schema.yaml` — rendered from `rule-lessons-schema`

> **when:**
> `uv run guppi sprint-close --sprint <id> --apply` closes the sprint `entity-sprint-<id>` of the made-up vault of `tests/test_sprint_close.py`, after each Estimate that `entity-sprint-<id>` lists and that does not stand `passed` is read or archived unread, as the person chooses; someone reads `vault/wiki/insights/`, `vault/wiki/lessons/` and `vault/archive/` after it.
> **＋** Or the preview `uv run guppi sprint-close --sprint <id>` runs over the live vault, and someone reads its output against `vault/wiki/insights/` and `vault/wiki/lessons/`.

> **then:**
> Each Insight under `vault/wiki/insights/` whose `sprint` is `<id>` and that stands `actioned` stands under `vault/archive/`.
> **＋** Each lesson under `vault/wiki/lessons/` whose `sprint` is `<id>`, whose `kind` is `error` and that stands `new` stands under `vault/archive/`.
> **＋** The preview names each such Insight and lesson among the pages the close would move, and moves none.
> **－** A lesson whose `kind` is `knowledge` stays under `vault/wiki/lessons/`.
> **－** An Insight that stands `open`, and each lesson its `children` lists, stay live.

> **tasks:**
> - [ ] update `rule-insights-schema`
>   - old: `` A Lesson is archived only when its Insight was actioned — its `clustered` children are archived by the cascade of `generate` (case 104.2) — and that Insight stays live with its `pattern` in its index line; a recurrence after the pattern was supposedly fixed is caught there, at the cost of one index line, and reopens the Insight. ``
>   - new: `` A Lesson is archived when its Insight was actioned — its `clustered` children are archived by the cascade of `generate` (case 104.2) — or, an `error` Lesson that joined no Insight, at the close of its sprint; that Insight stays live with its `pattern` in its index line until the close of its sprint, which archives it (`rule-sprint-close`, case 627.2); a recurrence inside the sprint after the pattern was supposedly fixed is caught there, at the cost of one index line, and reopens the Insight. ``
>   - old: `` an `actioned` Insight is never archived by the cascade, it is kept for the recurrence. ``
>   - new: `` an `actioned` Insight is never archived by the cascade, it is kept for the recurrence until the close of its sprint, which archives it (`rule-sprint-close`, case 627.2). ``
>   - change: `an actioned Insight and an error Lesson that joined no Insight are archived at the close of their sprint (case 627.2)`
> - [ ] update `rule-lessons-schema`
>   - old: `` a lesson with no pair is simply still `new`, and will be reconsidered next session anyway. ``
>   - new: `` a lesson with no pair is simply still `new`, and will be reconsidered next session anyway, until the close of its sprint archives a `new` lesson of kind `error` (`rule-sprint-close`, case 627.2). ``
>   - old: `` Archived when its Insight is `actioned`. ``
>   - new: `` Archived when its Insight is `actioned`, or, a `new` Lesson of kind `error`, at the close of its sprint (`rule-sprint-close`, case 627.2). ``
>   - change: `a new error Lesson is archived at the close of its sprint (case 627.2)`
> - [ ] update `estimate-sprint-close-archives-done-insights-and-lone-lessons`
>   - set: `{status: pending, method: "pytest tests/test_sprint_close.py -k insights; by hand, the output of the preview uv run guppi sprint-close --sprint migration over the live vault read against the Then"}`
>   - change: `the When replaced whole — the run with --apply over a made-up vault, after each Estimate of the sprint page not passed is read or archived unread, or the preview over the live vault; the Then kept, one line on the preview added; the method a pytest test and the preview of migration (case 627.2)`
> - [ ] `tests/test_sprint_close.py`: `-k insights` — an `actioned` Insight and a `new` `error` lesson of the sprint archived; a `knowledge` lesson, an `open` Insight and its children kept; the preview names the same pages and moves none; the clock pinned
> - [ ] `uv run guppi render`: `vault/wiki/insights/schema.yaml`
> - [ ] `uv run guppi render`: `vault/wiki/lessons/schema.yaml`
> - [ ] read `estimate-sprint-close-archives-done-insights-and-lone-lessons`

> **ratification:**
> ```
> - decision[case 627.2][update][rule-insights-schema]{ref:rule-insights-schema}
> - decision[case 627.2][update][rule-lessons-schema]{ref:rule-lessons-schema}
> - decision[case 627.2][update][estimate-sprint-close-archives-done-insights-and-lone-lessons]{ref:rule-sprint-close}
> ```

### Case 627.3 — The close archives the sprint page and its Estimates and keeps every other passed Estimate

> **given:**
> `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest` — its When replaced, its Then kept with one line added, its method set anew
> **＋** `entity-sprint` — the MOC over the sprint pages `entity-sprint-<id>` under `vault/wiki/entities/`
> **＋** `guppi/sprint_close.py` — selects the sprint page and its Estimates under `vault/wiki/estimates/`
> **＋** `tests/test_sprint_close.py` — the tests over a made-up vault of one sprint
> **＋** `rule-cleanup` — moves each page marked `archived` under `vault/archive/` and takes its slug off the `estimates` lists

> **when:**
> `uv run guppi sprint-close --sprint <id> --apply` closes the sprint `entity-sprint-<id>` of the made-up vault of `tests/test_sprint_close.py`, after each Estimate that `entity-sprint-<id>` lists and that does not stand `passed` is read or archived unread, as the person chooses; someone reads `vault/wiki/entities/`, `vault/wiki/estimates/` and `vault/archive/` after it.
> **＋** Or the preview `uv run guppi sprint-close --sprint <id>` runs over the live vault, and someone reads its output against `vault/wiki/entities/` and `vault/wiki/estimates/`.

> **then:**
> `entity-sprint-<id>` and each Estimate its `estimates` lists stand under `vault/archive/`.
> **＋** The preview names `entity-sprint-<id>` and each of those Estimates among the pages the close would move, and moves none.
> **－** Every other Estimate that stands `passed` stays under `vault/wiki/estimates/`, and the rule or Entity that lists it keeps it in `estimates`.
> **－** The close does not archive the MOC `entity-sprint`.

> **tasks:**
> - [ ] update `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest`
>   - set: `{status: pending, method: "pytest tests/test_sprint_close.py -k sprint_page; by hand, the output of the preview uv run guppi sprint-close --sprint migration over the live vault read against the Then"}`
>   - change: `the When replaced whole — the run with --apply over a made-up vault, after each Estimate of the sprint page not passed is read or archived unread, or the preview over the live vault; the Then kept, one line on the preview added; the method a pytest test and the preview of migration (case 627.3)`
> - [ ] `tests/test_sprint_close.py`: `-k sprint_page` — the sprint page and its Estimates archived, one of them archived unread; a `passed` Estimate of a rule kept and still listed; `entity-sprint` kept; the preview names the same pages and moves none; the clock pinned
> - [ ] read `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest`

> **ratification:**
> ```
> - decision[case 627.3][update][estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest]{ref:rule-sprint-close}
> ```

### Case 627.4 — The close settles each unread Estimate, the sprint page's own read or archived unread

> **given:**
> `estimate-sprint-close-settles-unread-estimates` — its Criterion replaced whole, its `purpose` and `method` set anew
> **＋** `entity-sprint` — the MOC over the sprint pages `entity-sprint-<id>`
> **＋** `guppi/sprint_close.py` — the preview, the choices `--carry` and `--archive-unread`, the refusal
> **＋** `tests/test_sprint_close.py` — the tests over a made-up vault of one sprint
> **＋** `rule-cleanup` — moves each page marked `archived` under `vault/archive/` and takes its slug off the `estimates` lists
> **＋** `vault/wiki/estimates/` — the Estimates the close lists

> **when:**
> `uv run guppi sprint-close --sprint <id>` closes the sprint `entity-sprint-<id>` of the made-up vault of `tests/test_sprint_close.py`, its preview first and then its run with `--apply`, after each Estimate that `entity-sprint-<id>` lists and that does not stand `passed` is read or archived unread, as the person chooses; someone reads the record of the close, `vault/wiki/estimates/` and `vault/archive/` after it.
> **＋** Or the preview `uv run guppi sprint-close --sprint <id>` runs over the live vault, and someone reads its output against `vault/wiki/estimates/`.

> **then:**
> Before any page of the close moves, the close lists to the person each Estimate under `vault/wiki/estimates/` that stands `pending` or `failed`.
> **＋** For each listed Estimate the person chooses one way: read it now, carry it into the next sprint, or archive it unread.
> **＋** An Estimate read now has its reading in the ledger.
> **＋** An Estimate read now whose reading comes out `failed` counts as settled: it is carried into the next sprint, or, when `entity-sprint-<id>` lists it, it stands under `vault/archive/` with the sprint page; the record of the close keeps its status.
> **＋** An Estimate carried into the next sprint stays under `vault/wiki/estimates/` with its status.
> **＋** An Estimate archived unread stands under `vault/archive/`, and the page that listed it no longer lists it in `estimates`.
> **－** No page of the close moves before the person has chosen for each listed Estimate.
> **－** An Estimate that `entity-sprint-<id>` lists is not carried into the next sprint: the person reads it now or archives it unread.

> **tasks:**
> - [ ] update `estimate-sprint-close-settles-unread-estimates`
>   - set: `{status: pending, purpose: "At the close of a sprint each pending or failed Estimate is put to the person, who has it read, carries it into the next sprint or archives it unread, before any page moves; an Estimate of the sprint page is read or archived with the sprint page and never carried, and a reading that comes out failed settles its Estimate", method: "pytest tests/test_sprint_close.py -k settle; by hand, the output of the preview uv run guppi sprint-close --sprint migration over the live vault read against the Then"}`
>   - change: `the Criterion replaced whole — the run over a made-up vault or the preview over the live vault; an Estimate of the sprint page that has not passed is read or archived unread and never carried; a reading that comes out failed settles its Estimate, carried or archived with the sprint page; the method a pytest test and the preview of migration (case 627.4)`
> - [ ] `tests/test_sprint_close.py`: `-k settle` — the preview lists each `pending` and `failed` Estimate and changes nothing; `--apply` refuses and moves nothing while one is neither passed nor named; `--carry` keeps an Estimate live with its status; `--archive-unread` archives it and takes it off `estimates`; `--carry` on an Estimate of the sprint page refused; an Estimate of the sprint page that stands `failed` goes with the sprint page with no choice by name, and the record keeps its status; the clock pinned
> - [ ] read `estimate-sprint-close-settles-unread-estimates`

> **ratification:**
> ```
> - decision[case 627.4][update][estimate-sprint-close-settles-unread-estimates]{ref:rule-sprint-close}
> ```

### Case 627.5 — The synthesis keeps an actioned Insight live until the close of its sprint

> **given:**
> `estimate-synthesis-clusters` — its Criterion replaced whole
> **＋** `rule-synthesis` — two passages on an actioned Insight that stays live
> **＋** `.claude/agents/librarian-guppi.md` — `librarian-guppi`, the agent the Render of `rule-synthesis` splices into
> **＋** `rule-sprint-close` — moves the actioned Insights of a sprint under `vault/archive/` at its close
> **＋** `vault/wiki/lessons/` — the lessons whose index lines the synthesis greps
> **＋** `vault/wiki/insights/` — the Insights whose index lines the synthesis greps
> **＋** `estimate-documentation-completes` — the promise of the flag of a read the frame does not need; unchanged
> **＋** `vault/wiki/brief.md` — where the synthesis is reported

> **when:**
> `librarian-guppi` does the synthesis in a live run whose `materialize.yaml` holds at least two lesson entries.

> **then:**
> The brief names the Greps of the synthesis, `^(root_cause|deferred_by):` over `vault/wiki/lessons/` and `^(pattern|deferred_by):` over `vault/wiki/insights/`, with the number of lines each printed.
> **＋** The brief gives one line for each lesson entry: its slug and the lesson or Insight it joined, or none and a few words on why no index line of either Grep shares its root cause.
> **＋** Two lessons with one root cause and no Insight give one `create` of an Insight with `pattern`, both children, the union of their tags, `Pattern` and `Proposal`, and one `update` per lesson with `set: {status: clustered, insight: <slug>}`.
> **＋** A lesson whose root cause matches the pattern of a live Insight gives an `update` of that Insight with the lesson added to its `children`, and an `update` of the lesson.
> **＋** Every entry the synthesis adds carries `librarian: synthesis`.
> **＋** Every lesson page read at synthesis is named in the report with the outcome: the Insight it joined, or none and why.
> **＋** A lesson without a pair stays `new`, and its line in the brief is no flag.
> **－** A read of another session's `materialize.yaml` or of a page under `vault/archive/` fails nothing here: an actioned Insight stays live with its pattern in its index line until the close of its sprint, and the flag of such a read is the promise of `estimate-documentation-completes`.

> **tasks:**
> - [ ] update `rule-synthesis`
>   - old: `The archive is not needed: a lesson is archived only when its Insight was actioned, and that Insight stays live with its pattern in its index line, so a recurrence is caught there at the cost of one Grep line.`
>   - new: `` The archive is not needed: a lesson is archived when its Insight was actioned, and that Insight stays live with its pattern in its index line until the close of its sprint, so a recurrence inside the sprint is caught there at the cost of one Grep line; the close of a sprint archives its actioned Insights and its `error` lessons that joined no Insight (`rule-sprint-close`, case 627.5). ``
>   - old: `The archive is not needed: an actioned Insight stays live with its pattern in its index line;`
>   - new: `The archive is not needed: an actioned Insight stays live with its pattern in its index line until the close of its sprint;`
>   - change: `an actioned Insight stays live until the close of its sprint (case 627.5)`
> - [ ] update `estimate-synthesis-clusters`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — an actioned Insight stays live until the close of its sprint (case 627.5)`
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] read `estimate-synthesis-clusters`

> **ratification:**
> ```
> - decision[case 627.5][update][rule-synthesis]{ref:rule-synthesis}
> - decision[case 627.5][update][estimate-synthesis-clusters]{ref:rule-synthesis}
> ```
