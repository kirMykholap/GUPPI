<!-- approved 19:32:19 · session 8b8ce20f -->

# Spec — session 1439, 2026-10-04

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

```then
update:
- slug: rule-sprint-close
  set:
    enforcement: check
    implementation_ref:
    - guppi/sprint_close.py
    - tests/test_sprint_close.py
  sections:
    Purpose: 'Prevents a closed sprint from leaving its finished work among the live pages, so that the vault does not only grow. `uv run guppi sprint-close --sprint <id>` closes `entity-sprint-<id>`: without `--apply` it prints what the close would move, what it keeps and each Estimate under `vault/wiki/estimates/` that stands `pending` or `failed`, and changes nothing; with `--apply` it sets `archived` on each page the close moves, with a History line, and runs `guppi cleanup`, which moves them (case 627.1). Before anything moves, each Estimate that stands `pending` or `failed` is put to the person, who has it read, carries it into the next sprint, or archives it unread (case 612.4); the run takes the choices by slug, `--carry <slug>` and `--archive-unread <slug>`, an Estimate read now being read before the run, and refuses, moving nothing, while a listed Estimate has neither passed nor been named. An Estimate that the sprint page lists is read now or archived unread with the sprint page, never carried, so the close goes ahead with the sprint page''s own Estimates not passed; one read now whose reading came out `failed` goes to the archive with the sprint page with no choice by name, and any other Estimate whose reading came out `failed` is carried by `--carry`; the record of the close keeps its status (case 627.4). Then the Decision pages of the sprint go to the archive, but a Decision page that a live page names in `deferred_by` or `addressed_by` stays (case 612.1). The `actioned` Insights of the sprint go, and its `error` lessons that joined no Insight; its `knowledge` lessons, its `open` Insights and their lessons stay (case 612.2). The sprint page and the Estimates it lists go; every other `passed` Estimate stays, the contract of its rule (case 612.3). Where the close runs — who calls the command and at what moment — and how the next sprint opens are set in `## How it works` of this page (case 628.1).'
  change: the close is the command guppi sprint-close, its preview and its run with --apply, the choices by slug; the close goes ahead once each Estimate of the sprint page is read or archived unread, a failed reading settling it; the guard named; where the close runs pointed to How it works (case 627.1)
- slug: entity-sprint-migration
  replace:
  - old: '[[rule-sprint-close]] — what the close of a sprint moves to the archive and what it keeps (case 612.1)'
    new: '[[rule-sprint-close]] — what the close of a sprint moves to the archive and what it keeps (cases 612.1, 627)'
  change: 'Slice 5: the item rule-sprint-close names case 627, which builds the command of the close; the question put off by case 615 closed (case 627.1)'
- slug: rule-decisions-schema
  replace:
  - old: '`archived` the moment the cascade of `generate` meets it so: a superseded Decision no longer describes the present (case 104.1).'
    new: '`archived` the moment the cascade of `generate` meets it so: a superseded Decision no longer describes the present (case 104.1); `guppi sprint-close` also sets `archived` on a Decision page of the sprint it closes, but for one that a live page names in `deferred_by` or `addressed_by` (`rule-sprint-close`, case 627.1).'
  change: a Decision page is archived also by the close of its sprint (case 627.1)
- slug: rule-cleanup
  replace:
  - old: '`archived` is a status the generator sets.'
    new: '`archived` is a status the generator sets, and `guppi sprint-close` at the close of a sprint (`rule-sprint-close`, case 627.1).'
  change: guppi sprint-close also sets archived (case 627.1)
- slug: estimate-sprint-close-archives-the-decisions
  set:
    status: pending
    method: pytest tests/test_sprint_close.py -k decisions; by hand, the output of the preview uv run guppi sprint-close --sprint migration over the live vault read against the Then
  change: the When replaced whole — the run with --apply over a made-up vault, after each Estimate of the sprint page not passed is read or archived unread, or the preview over the live vault; the Then kept, one line on the preview added; the method a pytest test and the preview of migration (case 627.1)
```

```tasks
- [ ] update `rule-sprint-close`
- [ ] update `entity-sprint-migration`
- [ ] update `rule-decisions-schema`
- [ ] update `rule-cleanup`
- [ ] update `estimate-sprint-close-archives-the-decisions`
- [ ] `guppi/sprint_close.py`: the command — the preview, the choices by slug, the refusal while a listed Estimate is neither passed nor named, the marks through the writer of `guppi/generate.py`, then `guppi cleanup`
- [ ] `guppi/cli.py`: `sprint-close` registered
- [ ] `tests/test_sprint_close.py`: `-k decisions` — over a made-up vault of one sprint, the Decision pages of the sprint archived, one named in `deferred_by` and one in `addressed_by` of a live page kept, one of another sprint kept; the preview names the same pages and moves none; the clock pinned
- [ ] `uv run guppi render`: `vault/wiki/decisions/schema.yaml`
- [ ] `uv run guppi sprint`
- [ ] read `estimate-sprint-close-archives-the-decisions`
```

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

```then
update:
- slug: rule-insights-schema
  replace:
  - old: A Lesson is archived only when its Insight was actioned — its `clustered` children are archived by the cascade of `generate` (case 104.2) — and that Insight stays live with its `pattern` in its index line; a recurrence after the pattern was supposedly fixed is caught there, at the cost of one index line, and reopens the Insight.
    new: A Lesson is archived when its Insight was actioned — its `clustered` children are archived by the cascade of `generate` (case 104.2) — or, an `error` Lesson that joined no Insight, at the close of its sprint; that Insight stays live with its `pattern` in its index line until the close of its sprint, which archives it (`rule-sprint-close`, case 627.2); a recurrence inside the sprint after the pattern was supposedly fixed is caught there, at the cost of one index line, and reopens the Insight.
  - old: an `actioned` Insight is never archived by the cascade, it is kept for the recurrence.
    new: an `actioned` Insight is never archived by the cascade, it is kept for the recurrence until the close of its sprint, which archives it (`rule-sprint-close`, case 627.2).
  change: an actioned Insight and an error Lesson that joined no Insight are archived at the close of their sprint (case 627.2)
- slug: rule-lessons-schema
  replace:
  - old: a lesson with no pair is simply still `new`, and will be reconsidered next session anyway.
    new: a lesson with no pair is simply still `new`, and will be reconsidered next session anyway, until the close of its sprint archives a `new` lesson of kind `error` (`rule-sprint-close`, case 627.2).
  - old: Archived when its Insight is `actioned`.
    new: Archived when its Insight is `actioned`, or, a `new` Lesson of kind `error`, at the close of its sprint (`rule-sprint-close`, case 627.2).
  change: a new error Lesson is archived at the close of its sprint (case 627.2)
- slug: estimate-sprint-close-archives-done-insights-and-lone-lessons
  set:
    status: pending
    method: pytest tests/test_sprint_close.py -k insights; by hand, the output of the preview uv run guppi sprint-close --sprint migration over the live vault read against the Then
  change: the When replaced whole — the run with --apply over a made-up vault, after each Estimate of the sprint page not passed is read or archived unread, or the preview over the live vault; the Then kept, one line on the preview added; the method a pytest test and the preview of migration (case 627.2)
```

```tasks
- [ ] update `rule-insights-schema`
- [ ] update `rule-lessons-schema`
- [ ] update `estimate-sprint-close-archives-done-insights-and-lone-lessons`
- [ ] `tests/test_sprint_close.py`: `-k insights` — an `actioned` Insight and a `new` `error` lesson of the sprint archived; a `knowledge` lesson, an `open` Insight and its children kept; the preview names the same pages and moves none; the clock pinned
- [ ] `uv run guppi render`: `vault/wiki/insights/schema.yaml`
- [ ] `uv run guppi render`: `vault/wiki/lessons/schema.yaml`
- [ ] read `estimate-sprint-close-archives-done-insights-and-lone-lessons`
```

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

```then
update:
- slug: estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest
  set:
    status: pending
    method: pytest tests/test_sprint_close.py -k sprint_page; by hand, the output of the preview uv run guppi sprint-close --sprint migration over the live vault read against the Then
  change: the When replaced whole — the run with --apply over a made-up vault, after each Estimate of the sprint page not passed is read or archived unread, or the preview over the live vault; the Then kept, one line on the preview added; the method a pytest test and the preview of migration (case 627.3)
```

```tasks
- [ ] update `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest`
- [ ] `tests/test_sprint_close.py`: `-k sprint_page` — the sprint page and its Estimates archived, one of them archived unread; a `passed` Estimate of a rule kept and still listed; `entity-sprint` kept; the preview names the same pages and moves none; the clock pinned
- [ ] read `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest`
```

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

```then
update:
- slug: estimate-sprint-close-settles-unread-estimates
  set:
    status: pending
    purpose: At the close of a sprint each pending or failed Estimate is put to the person, who has it read, carries it into the next sprint or archives it unread, before any page moves; an Estimate of the sprint page is read or archived with the sprint page and never carried, and a reading that comes out failed settles its Estimate
    method: pytest tests/test_sprint_close.py -k settle; by hand, the output of the preview uv run guppi sprint-close --sprint migration over the live vault read against the Then
  change: the Criterion replaced whole — the run over a made-up vault or the preview over the live vault; an Estimate of the sprint page that has not passed is read or archived unread and never carried; a reading that comes out failed settles its Estimate, carried or archived with the sprint page; the method a pytest test and the preview of migration (case 627.4)
```

```tasks
- [ ] update `estimate-sprint-close-settles-unread-estimates`
- [ ] `tests/test_sprint_close.py`: `-k settle` — the preview lists each `pending` and `failed` Estimate and changes nothing; `--apply` refuses and moves nothing while one is neither passed nor named; `--carry` keeps an Estimate live with its status; `--archive-unread` archives it and takes it off `estimates`; `--carry` on an Estimate of the sprint page refused; an Estimate of the sprint page that stands `failed` goes with the sprint page with no choice by name, and the record keeps its status; the clock pinned
- [ ] read `estimate-sprint-close-settles-unread-estimates`
```

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

```then
update:
- slug: rule-synthesis
  replace:
  - old: 'The archive is not needed: a lesson is archived only when its Insight was actioned, and that Insight stays live with its pattern in its index line, so a recurrence is caught there at the cost of one Grep line.'
    new: 'The archive is not needed: a lesson is archived when its Insight was actioned, and that Insight stays live with its pattern in its index line until the close of its sprint, so a recurrence inside the sprint is caught there at the cost of one Grep line; the close of a sprint archives its actioned Insights and its `error` lessons that joined no Insight (`rule-sprint-close`, case 627.5).'
  - old: 'The archive is not needed: an actioned Insight stays live with its pattern in its index line;'
    new: 'The archive is not needed: an actioned Insight stays live with its pattern in its index line until the close of its sprint;'
  change: an actioned Insight stays live until the close of its sprint (case 627.5)
- slug: estimate-synthesis-clusters
  set:
    status: pending
  change: the Criterion replaced whole — an actioned Insight stays live until the close of its sprint (case 627.5)
```

```tasks
- [ ] update `rule-synthesis`
- [ ] update `estimate-synthesis-clusters`
- [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [ ] read `estimate-synthesis-clusters`
```

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

```then
create:
- slug: estimate-sprint-close-runs-in-the-librarian-run
  kind: QA
  purpose: Whether the close of a sprint runs in the librarian's run of a session of its own, from the task line of its closing Case, after guppi generate and before guppi cleanup, so that the readings of that session count, with Work Mode leaving the line, Retro not counting it as debt and the command ticking it
  method: 'pytest tests/test_sprint_close.py -k tick; by hand, after the librarian''s run of the session that closes a sprint: its ledger, spec.md, handoff.md, the librarian''s event log and report, and vault/archive/'
  tags:
  - sprint
  - workflow
  - librarian
  ref: rule-sprint-close
update:
- slug: rule-sprint-close
  sections:
    How it works: |-
      The close runs in a session of its own, whose Plan Mode holds only the closing Case and the Cases that prepare its readings, so that all of its decisions belong to the sprint it closes: the closing Case holds the task line `uv run guppi sprint-close --sprint <id> --apply` with the person's choices; Work Mode leaves that line, Retro counts it as waiting, and the librarian runs it after `guppi generate` and before `guppi cleanup`, so that the readings of that session count; the command ticks its line, found by `render.command_line`, once it moved the pages (case 628.1).

      Before the closing Case, the session sorts the Estimates that stand `pending` or `failed` into groups by the kind of moment their `method` names; the closing Case names the groups in its `context` and holds one `by hand` task per moment that Work Mode sets up and one `read` line per Estimate, and only an Estimate still unread after Work Mode is carried or archived unread (case 628.2).

      No sprint is open from the close until a Case of the next session, its first, creates `entity-sprint-<new id>`: the brief of the closing run names that opening first under the Cases of Next session, `/hi` takes no item of `sprint.md` meanwhile, the ledger hook refuses every other decision line of that session but a `defer` until the `create` stands, and every page of the run that writes the new sprint page carries the new id; `guppi sprint` and `make lint` report the missing sprint page until then, and that is expected (case 628.3). The `## Backlog` of a closed sprint page stays in `backlog.md`, since `guppi backlog` reads it under `vault/archive/` too (case 628.12).
  change: 'where the close runs, in How it works: the librarian''s run of a session of its own, from the closing Case''s task line; the readings taken in groups first; the next sprint opened first by the next session; the Backlog of a closed sprint kept in backlog.md (case 628.1)'
- slug: rule-documentation
  replace:
  - old: 2. Run `uv run guppi generate`. Every line on its stderr is a flag.
    new: '2. Run `uv run guppi generate`. Every line on its stderr is a flag. Then, when an unticked task line of the session''s `spec.md` opens with a code span holding `guppi sprint-close` and `--apply`, run that command as the line holds it: the readings this run applied count, and the command runs `guppi cleanup` itself (`rule-sprint-close`, case 628.1). Every line on its stderr is a flag; a refusal moves nothing, and the run goes on. After a close, `guppi sprint` in step 5 finds no live sprint page; its error is a flag.'
  change: the librarian runs the close line of the Spec after generate (case 628.1)
- slug: rule-retro
  replace:
  - old: A `create`, `update` or `defer` line of a page, a `guppi render` line, a `guppi sprint` line,
    new: A `create`, `update` or `defer` line of a page, a `guppi render` line, a `guppi sprint` line, a `guppi sprint-close` line (`rule-sprint-close`, case 628.1),
  change: a guppi sprint-close line waits for the librarian and is not debt (case 628.1)
- slug: rule-orchestration
  replace:
  - old: '`render`, `sprint` and `glossary` the render, sprint and glossary lines (cases 226, 250, 270, 306);'
    new: '`render`, `sprint` and `glossary` the render, sprint and glossary lines (cases 226, 250, 270, 306), and `guppi sprint-close`, which the librarian runs, its own line (case 628.1);'
  change: guppi sprint-close ticks its own line (case 628.1)
- slug: rule-case-protocol
  replace:
  - old: a glossary line `- [ ] `uv run guppi glossary`` — the command in the first code span is what the ticker matches (case 235)
    new: a glossary line `- [ ] `uv run guppi glossary``, a close line `- [ ] `uv run guppi sprint-close --sprint <id> --apply …``, which the librarian runs and the command ticks (`rule-sprint-close`, case 628.1) — the command in the first code span is what the ticker matches (case 235)
  change: the close line of a sprint is a task line form (case 628.1)
```

```tasks
- [ ] update `rule-sprint-close`
- [ ] update `rule-documentation`
- [ ] update `rule-retro`
- [ ] update `rule-orchestration`
- [ ] update `rule-case-protocol`
- [ ] create `estimate-sprint-close-runs-in-the-librarian-run`
- [ ] `guppi/sprint_close.py`: after a run with `--apply` that moved the pages, tick each unticked task line of a `spec.md` under `vault/raw/` that `render.command_line("guppi sprint-close --sprint <id> --apply")` matches, imported from `guppi/render.py`, not copied (`rule-one-judgment-one-implementation`); a refused run ticks nothing; the docstring
- [ ] `tests/test_sprint_close.py`: `-k tick` — the line ticked after a run that moved, left unticked after a refusal, a line of another sprint id left; the clock pinned
- [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
- [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-sprint-close-runs-in-the-librarian-run`
```

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

```then
create:
- slug: estimate-sprint-close-takes-the-readings-in-groups
  kind: QA
  purpose: Whether the session that closes a sprint sorts the pending and failed Estimates into groups by the kind of moment their method names, sets up each moment it can in its Work Mode, and carries or archives unread only those still unread
  method: 'by hand, after the Work Mode of the session that closes a sprint: its closing Case, spec.md and ledger read against the Criterion'
  tags:
  - sprint
  - workflow
  ref: rule-sprint-close
```

```tasks
- [ ] create `estimate-sprint-close-takes-the-readings-in-groups`
- [ ] read `estimate-sprint-close-takes-the-readings-in-groups`
```

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

```then
create:
- slug: estimate-sprint-close-next-session-opens-the-sprint
  kind: QA
  purpose: Whether after the close of a sprint the brief puts the opening of the next sprint first, /hi takes no item of sprint.md, the ledger hook refuses every decision line but a defer until a create of a sprint page stands, and the pages of the run that opens it carry its id
  method: 'pytest tests/test_ledger.py -k sprint and tests/test_materialize.py -k sprint; by hand, at the librarian''s run of the session after the close of a sprint: the brief before it, its frontier.md, the refusals of guppi ledger in its transcript, its ledger and the sprint field of the pages of its run'
  tags:
  - sprint
  - workflow
  - ledger
  ref: rule-sprint-close
update:
- slug: rule-ledger-write
  replace:
  - old: would materialize pages from it the next day.
    new: would materialize pages from it the next day. It also refuses, while no live page `vault/wiki/entities/entity-sprint-<id>.md` stands, every decision line of the session but a `defer`, until the session's ledger or the same reply holds a `create` decision line of an `entity-sprint-` slug, with one stderr line that names the opening of the next sprint, so that the session after the close of a sprint opens the next sprint first (`rule-sprint-close`, case 628.3).
  change: refuses the decision lines of a session with no live sprint page until it creates one (case 628.3)
- slug: rule-materialize
  replace:
  - old: The mechanism and the full list of an entry's fields, each with its writer, live in the docstring of `guppi/materialize.py`.
    new: The yaml's `sprint` is the first `## <id>` heading of `sprint.md`, but in a unit whose ledger holds a `create` decision line of `entity-sprint-<id>` it is that `<id>`, so that the session that opens a sprint belongs to it (`rule-sprint-close`, case 628.3). The mechanism and the full list of an entry's fields, each with its writer, live in the docstring of `guppi/materialize.py`.
  change: the yaml's sprint is the id of a sprint page the unit creates (case 628.3)
```

```tasks
- [ ] update `rule-ledger-write`
- [ ] update `rule-materialize`
- [ ] create `estimate-sprint-close-next-session-opens-the-sprint`
- [ ] `guppi/ledger.py`: the refusal — no live `entity-sprint-` page, a decision line other than a `defer`, and no `create` decision line of an `entity-sprint-` slug in the session's ledger or the reply; one stderr line; readings and lessons pass; the docstring
- [ ] `tests/test_ledger.py`: `-k sprint` — refused with no sprint page, a `defer` and a reading passed, accepted once the `create` stands in the ledger or the same reply, accepted with a live sprint page
- [ ] `guppi/materialize.py`: the yaml's `sprint` from a `create` decision line of `entity-sprint-<id>` in the unit, else the heading of `sprint.md`
- [ ] `tests/test_materialize.py`: `-k sprint` — a unit that creates `entity-sprint-next` gets `sprint: next`; a unit with none gets the heading's id
- [ ] read `estimate-sprint-close-next-session-opens-the-sprint`
```

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

```then
update:
- slug: rule-work-mode
  replace:
  - old: The lines of a page, a render, the sprint, the glossary and a reading are ticked by the librarian's scripts, not here.
    new: 'The lines of a page, a render, the sprint, the glossary and a reading are ticked by the librarian''s scripts, not here. A task line that opens with a code span holding `guppi sprint-close` is neither run nor ticked here: the librarian runs it, and the command ticks it (`rule-sprint-close`, case 628.4).'
  change: Work Mode leaves the close line of a sprint to the librarian (case 628.4)
- slug: estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline
  set:
    status: pending
    purpose: Whether /work stops on main, writes the baseline of make test and make lint into work.md before the first change — running a command itself when its substitution is empty — and keeps it on a resume, runs the tasks of the Spec of the session or of the folder /box gives it in order with their ticks but leaves a guppi sprint-close line to the librarian, names that folder under Conserved Spec and deletes its carry.md, and marks an expected red under Expected red
    method: 'uv run guppi render --check; by hand, a /work the agent calls at the fork, a /work that /box calls and the /work of a session that closes a sprint: the branch, work.md, the ticks of the Spec, the guppi sprint-close line neither run nor ticked, the carry.md of the folder and each Expected red line read against the Criterion, and, where a substitution came back empty, the agent''s own run of its command, recorded in the estimate line'
  change: the Criterion replaced whole — a guppi sprint-close line is neither run nor ticked by Work Mode; purpose and method name it (case 628.4)
```

```tasks
- [ ] update `rule-work-mode`
- [ ] update `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
- [ ] `uv run guppi render`: `.claude/skills/work/SKILL.md`
- [ ] read `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
```

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

```then
update:
- slug: rule-sprint
  replace:
  - old: never a `read` line that names the command later —
    new: never a `read` line that names the command later, nor a line whose code span holds `guppi sprint-close`, which that command ticks (case 628.5) —
  change: the ticker of guppi sprint leaves a guppi sprint-close line (case 628.5)
- slug: estimate-sprint-ticks-the-spec
  set:
    status: pending
    method: pytest tests/test_sprint.py; by hand, after a librarian's run, the spec.md of each unit under vault/raw/ whose guppi sprint line it ticked, and any guppi sprint-close line there left as it stood
  change: the Criterion replaced whole — a guppi sprint-close line is not ticked by guppi sprint (case 628.5)
```

```tasks
- [ ] update `rule-sprint`
- [ ] update `estimate-sprint-ticks-the-spec`
- [ ] `guppi/render.py`: `command_line` matches the command only where no `-` or word character follows it; its docstring
- [ ] `guppi/sprint.py`: the docstring names the close line as not ticked
- [ ] `tests/test_sprint.py`: a `guppi sprint-close` line left unticked beside a ticked `guppi sprint` line
- [ ] read `estimate-sprint-ticks-the-spec`
```

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

```then
update:
- slug: estimate-generate-writes
  set:
    status: pending
  change: the Criterion replaced whole — a page's sprint is the sprint of the yaml, the new sprint's id in the unit that creates its page (case 628.6)
```

```tasks
- [ ] update `estimate-generate-writes`
- [ ] `guppi/generate.py`: the docstring — `sprint` is the yaml's `sprint`, else the first `## <id>` heading of `sprint.md`
- [ ] `tests/test_generate.py`: a yaml whose `sprint` differs from the heading of `sprint.md` writes the yaml's `sprint` on a created page
- [ ] read `estimate-generate-writes`
```

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

```then
update:
- slug: rule-skill-hi
  replace:
  - old: and none of a later milestone, of the Backlog or of Closed (case 229.3);
    new: and none of a later milestone, of the Backlog or of Closed (case 229.3) — and none at all while the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, which then stands as the first Cases line, before every other (`rule-sprint-close`, case 628.7);
  change: the opening of the next sprint first, and no item of a closed sprint (case 628.7)
- slug: estimate-hi-writes-frontier
  set:
    status: pending
    method: 'by hand at the /hi of the session after the close of a sprint, written into the estimate line; unit: the frontier findings of guppi prespec --check in tests/test_prespec.py'
  change: the Criterion replaced whole — the opening of the next sprint first, no milestone item while it stands (case 628.7)
```

```tasks
- [ ] update `rule-skill-hi`
- [ ] update `estimate-hi-writes-frontier`
- [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [ ] read `estimate-hi-writes-frontier`
```

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

```then
update:
- slug: rule-brief
  replace:
  - old: '`Cases`, what needs a decision: a line of `## For the next session` of `handoff.md`,'
    new: '`Cases`, what needs a decision: after a run whose `guppi sprint-close --apply` moved the sprint page, first the line `open the next sprint — no sprint is open since the close of <id>` (`rule-sprint-close`, case 628.8); a line of `## For the next session` of `handoff.md`,'
  change: after a close, the opening of the next sprint is the first Cases line (case 628.8)
- slug: estimate-brief-written
  set:
    status: pending
    method: by hand at the /hi after the librarian's run of the session that closes a sprint, recorded in the estimate line
  change: the Criterion replaced whole — after a close, the first Cases line opens the next sprint (case 628.8)
```

```tasks
- [ ] update `rule-brief`
- [ ] update `estimate-brief-written`
- [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [ ] read `estimate-brief-written`
```

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

```then
update:
- slug: entity-sprint-migration
  replace:
  - old: 'where the close of a sprint runs — a session of its own, a command or another place: not decided (case 612.1)'
    new: 'the close of migration — a session of its own: the pending readings taken in groups, `make test`, `make lint` and the tree read in its Work Mode, then `uv run guppi sprint-close --sprint migration --apply` in the librarian''s run (case 628.9)'
  - old: the leftovers gone, the branch merged,
    new: the leftovers gone, `make test` green on the last commit of `migration`,
  - old: '- [[rule-morph]] — the morph mechanism: the initiation at install sets the category set of the project, the development set by default, held as data so that a changed set rewrites no rule; case 239'
    new: |-
      - [[rule-morph]] — the morph mechanism: the initiation at install sets the category set of the project, the development set by default, held as data so that a changed set rewrites no rule; case 239
      - the merge of `migration` into `main` — the first work of the session that opens the next sprint, after its opening Case (case 628.9)
  change: the Slice 5 note on where the close runs cut into the close of migration; make test in the Purpose for the branch merged; the merge a Backlog line for the next sprint; the question put off by case 615 closed (case 628.9)
- slug: estimate-sprint-migration-merges
  set:
    status: pending
    purpose: make test green on the last commit of migration, read in the Work Mode of the session that closes it
    method: make test on the last commit of migration, in the Work Mode of the session that closes it, before the librarian's run
  change: the Criterion replaced whole — read before the close; the merge into main and the line on sprint.md leave this promise (case 628.9)
```

```tasks
- [ ] update `entity-sprint-migration`
- [ ] update `estimate-sprint-migration-merges`
- [ ] read `estimate-sprint-migration-merges`
```

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

```then
update:
- slug: estimate-sprint-migration-lint-clean
  set:
    status: pending
    purpose: make lint exits 0 in the Work Mode of the session that closes the sprint, before the librarian's run, unmigrated included, but for the unread of the sprint page's own Estimates
    method: make lint in the Work Mode of the session that closes the sprint, before the librarian's run, exit 0 — or only unread lines on the Estimates of entity-sprint-migration
  change: the Criterion replaced whole — read in the Work Mode of the closing session, before the close (case 628.10)
```

```tasks
- [ ] update `estimate-sprint-migration-lint-clean`
- [ ] read `estimate-sprint-migration-lint-clean`
```

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

```then
update:
- slug: estimate-sprint-migration-leftovers-gone
  set:
    status: pending
    purpose: vault/parked/, the 2026-08 documents and the old archive root are gone, git tracks no raw date folder without a session, and the repository has no remote, each by a decision named in the reading, read in the Work Mode of the session that closes the sprint
    method: one reading of the tree by hand in the Work Mode of the session that closes the sprint, before the librarian's run, each path and decision named in the estimate line
  change: the Criterion replaced whole — read in the Work Mode of the closing session, before the close (case 628.11)
```

```tasks
- [ ] update `estimate-sprint-migration-leftovers-gone`
- [ ] read `estimate-sprint-migration-leftovers-gone`
```

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

```then
update:
- slug: rule-backlog
  replace:
  - old: each line of the `## Backlog` of the sprint page —
    new: each line of the `## Backlog` of each sprint page, live or under `vault/archive/`, so that the Backlog of a closed sprint stays in the list (`rule-sprint-close`, case 628.12) —
  change: the Backlog of an archived sprint page stays in backlog.md (case 628.12)
- slug: estimate-backlog-renders
  set:
    status: pending
    purpose: guppi backlog writes backlog.md from the conserved Specs, the pages with deferred_by, the open Insights and the Backlog of each sprint page, live or archived, each item with its purpose and its count
    method: uv run pytest tests/test_backlog.py, plus one reading of vault/wiki/backlog.md after the librarian's run of the session that closes a sprint
  change: the Criterion replaced whole — the Backlog of each sprint page, live or archived (case 628.12)
```

```tasks
- [ ] update `rule-backlog`
- [ ] update `estimate-backlog-renders`
- [ ] `guppi/backlog.py`: read the `## Backlog` of each `entity-sprint-<id>` page under `vault/archive/` too, by the item reader of `guppi/sprint.py`; the docstring
- [ ] `tests/test_backlog.py`: the Backlog lines of an archived sprint page and of a live one both shown, a slug of both standing once
- [ ] read `estimate-backlog-renders`
```

## Case 629 — The check of a built Case compares it with the session's other Cases, and a Case built again comes back by its changed sub-cases

> **context:**
> Two items are taken together, at the person's word. The first is C6. Each time `case-guppi` finishes an answer, the `SubagentStop` hook `guppi casecheck --subagent` runs `prespec.judge` over a Spec text built from the Cases of that one answer. So it never compares an answer with the session's other Cases. The comparison of two Cases that write one part of one page is `check_same_target` in `guppi/prespec.py`. It runs only at `/pre-spec`, and after ratification in the `Stop` hook `guppi ratified`, by `prespec.written_findings`. In this session, Cases 627 and 628 were ratified in one batch. The `Stop` hook then printed that case 628.1 writes the section Purpose of `rule-sprint-close` that case 627.1 writes too, and both Cases were built and ratified again. When Case 628 was built, Case 627 stood only in the store `<plan>.checked.json`, not in the plan file. So a check of the plan alone would have missed it.
>
> The second item is C4, `rule-case-rebuild-cost`. It is a placeholder page with one Purpose, deferred by cases 566 and 570. `case-guppi` is told to answer with the whole Case again after a finding of the hook and after any message. In session 2356 a Case with fourteen sub-cases came back whole three times for a change of a few lines of one sub-case. Its `context` also lists searches that changed nothing. The hook can already write an answer of sub-cases alone into the Case file: it replaces only their sections there (`write_case_files`). But it judges such a sub-case without its parent, so it reads no `given` for its frame and no earlier `recommend` for the titles of the rounds.
>
> The person chose these answers. The early check compares an answer with the plan's Cases and with the stored Cases not yet ratified. It leaves out a stored Case with findings, a Case that a `{supersedes}` mark retired, and the answer's own earlier parts. A clash is a finding, and the check after ratification stays as a backstop (Q1–Q4). `case-guppi` answers again by its changed sub-cases alone while the parent's own parts stand, and with the whole Case otherwise (Q5, Q8). `context` keeps only the searches the Case rests on (Q6). No rule splits a large item (Q7). The changes go on `rule-case-build` and `rule-case-check`, and the placeholder is retired by a `delete` that carries `{supersedes:case 566}` and `{supersedes:case 570}` (Q9). One Case holds five sub-cases, one promise each (Q10).
>
> The frame. A Grep of `SubagentStop` over `vault/wiki/rules/` printed `rule-orchestration`, `rule-case-check`, `rule-case-rebuild-cost`, `rule-hook-registry` and `rule-spec-reconcile`. Over `.claude/` it printed `.claude/settings.json`, where `guppi casecheck --subagent` is the only hook on that event. `rule-orchestration` and `rule-spec-reconcile` say the hook writes the Case file from the answer, and that stays true. A Grep of `whole again|Case whole|sub-cases? alone|holds sub-cases|holds that sub-case` ran over `vault/wiki/*.md`, `vault/wiki/rules/`, `vault/wiki/estimates/`, `.claude/` and `guppi/*.py`. It printed 12 files. `rule-case-build`, `.claude/agents/case-guppi.md` and `estimate-case-build-writes-the-case` change (629.2). The other hits stand: `log.md`, which is not read; `case-schema.md`, `rule-case-protocol` and `estimate-spec-write-removes-a-superseded-case`, on a `{supersedes}` mark of a sub-case; `estimate-case-check-sends-back-a-faulty-round` and `guppi/casecheck.py`, on a round answered whole; `estimate-case-check-sends-back-a-faulty-case`, on the file of a lone sub-case; `estimate-case-check-sends-back-a-ratified-case-in-another-shape`, which gives an answer of sub-cases alone no finding, as Q8 needs; and `rule-language`, on the file sent whole. `orchestration.md`, read whole, sends a Case again whole in its file and lists the Cases of the answer. The file stays whole, so it stands. A Grep of `rule-case-rebuild-cost` over the repository outside `vault/archive/` and `vault/raw/` printed `brief.md`, `backlog.md`, `log.md` and the Decision pages 566 and 570. `backlog.md` is written from `deferred_by`, so the item leaves it after the `delete`.
>
> The findings of `/pre-spec`. A Case stored with a finding cannot be shown or written into the Spec. So when the other Case is the one that should change (Q2), `case-guppi` still bounds its own Case so that the finding goes, and its `context` names the other Case and the change it needs. The main agent then asks the person whether that Case is built again. 629.1 says so in `then` and adds it to `rule-orchestration`. `estimate-orchestration-signs-a-batch-together` already sets the batch when the person's word asks that a ratified Case change, and `estimate-orchestration-shows-the-built-case` sets the showing, which does not change. Both stand. Case 628, built again in this session, changes another sentence of `rule-orchestration`, on the ticks of Work Mode, so the two anchors do not meet. The new tests of 629.1 run under `-k session_clash`, because `-k clash` is the selector of `estimate-case-check-sends-back-a-case-number-held-by-another-agent`. 629.1 reads a stored entry under its number alone, as that Estimate, 629.3 and 629.4 do.
>
> The Estimates. `estimate-case-check-sends-back-a-faulty-case` says the hook runs `judge` over the answer's Cases. It says nothing of other Cases or a stored parent, so it stands. `estimate-case-check-notes-a-then-line-shared-by-siblings` says a lone sub-case gets no sibling note from the hook. 629.3 adds only the stored parent, not the siblings, so it stands. `estimate-case-build-records-the-rounds-in-recommend` already lets an item stand under a sub-case's heading, so it stands.
>
> The notes of the hook. One line of the Criterion of `estimate-case-check-requires-each-question-of-the-rounds` is not carried: the line that looked for a title only in the answer. 629.4 replaces it with the line that also reads the store, which is the change itself. Four `then` lines share words with a line of a sibling: 629.4 with 629.1 and 629.3, and 629.5 with 629.2 twice. In each pair the two lines speak of different things: a title of a round against a clash between Cases or a lone sub-case, and the frame check of a finished Case against the answer again. The lines of 629.2 and 629.5 are also carried word for word from the Criteria they replace. So each line stays in its own sub-case.
>
> No refused text is lost between the render and the code. An answer of sub-cases alone that the old hook judges gets at worst a finding, and `case-guppi` answers again with the whole Case. The `then` of 629.2 and 629.5 carry the Criteria they replace word for word but one line, so they hold more than seven `**＋**` lines.
>
> Not done: no rule splits a large item into several Cases (Q7). `case-guppi` does not write the Case file itself (Q5). A search that `context` keeps still lists each file it printed (case 557.1).

> **problem:**
> A clash between two Cases of one session is found only after the person ratified both, so they are built and ratified twice. And a Case changed in one sub-case is written and returned whole, its `context` full of searches that changed nothing. The question is how the early check sees the session's other Cases, how a Case comes back by its changed parts, and what `context` keeps.

> **recommend:**
> - **Which other Cases does the early check compare an answer with?**
>   - Recommended: (b) the ratified Cases of the plan file and the Cases built but not yet ratified in the store, leaving out a stored Case with findings, one a supersedes mark replaced, and the answer's own earlier version.
>   - Answer: agreed.
> - **What does the early check do when an answer clashes with another Case?**
>   - Recommended: (a) a finding: `case-guppi` changes its own Case, and where the other Case should change the main agent asks the person.
>   - Answer: agreed.
> - **Does the late check, after ratification, stay?**
>   - Recommended: (a) keep it as a backstop.
>   - Answer: agreed.
> - **What will check that the early check compares an answer with the other Cases?**
>   - Recommended: (a) a new Estimate on `rule-case-check`, the Criterion of `estimate-case-check-sends-back-a-faulty-case` standing.
>   - Answer: agreed.
> - **How does a Case come back when only a sub-case changed?**
>   - Recommended: (b) the changed sub-cases alone, plus the parent when its own parts changed, the hook checking them with the parent's stored parts and merging them into the store and the file.
>   - Answer: agreed; its part on the parent was replaced by the question on the parent's own text.
> - **What does a Case's `context` say about the searches it ran?**
>   - Recommended: (b) only the searches the Case rests on, each with its pattern and paths.
>   - Answer: agreed.
> - **Is a large item split into several Cases?**
>   - Recommended: (a) no rule for this now; the context names it as not done.
>   - Answer: agreed.
> - **When the parent's own text changes, what comes back?**
>   - Recommended: (a) the whole Case; the changed sub-cases alone only while the parent's `context`, `problem` and `recommend` stand as they were.
>   - Answer: agreed.
> - **Where does the decision on the cost of rebuilding a Case live?**
>   - Recommended: (a) on `rule-case-build` and `rule-case-check`, the placeholder retired by a `delete` with both supersedes marks.
>   - Answer: agreed.
> - **How are the two items cut, and what checks each part?**
>   - Recommended: (a) one Case with five sub-cases: the clash with other Cases, a new Estimate; the answer by changed sub-cases with the placeholder retired, the Criterion of `estimate-case-build-writes-the-case` replaced; a lone sub-case judged with its stored parent, a new Estimate; the titles of the rounds read in the stored `recommend` too, the Criterion of `estimate-case-check-requires-each-question-of-the-rounds` replaced; `context` keeping only the searches the Case rests on, the Criterion of `estimate-case-build-checks-the-finished-case` replaced.
>   - Answer: agreed.

### Case 629.1 — The check of an answer compares its Cases with the session's other Cases

> **given:**
> `rule-case-check` — the check of the answer of `case-guppi` at `SubagentStop`; its Purpose gains a sentence
> **＋** `estimate-case-check-sends-back-a-clash-with-another-case` — the new promise, on `rule-case-check`
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py` — the hook and its tests
> **＋** `guppi/prespec.py` — `check_same_target`, the one judgment of a clash, run by `/pre-spec` too
> **＋** `guppi/ratified.py` — the `Stop` hook of `rule-spec-write`, which runs the same judgment after ratification
> **＋** the plan file of the session, `<plan>.checked.json` beside it and `raw/<date>/<hi HHMM>/ledger.md` — what the hook reads
> **＋** `rule-orchestration` — what the main agent does with a built Case, rendered into `vault/wiki/orchestration.md`; one sentence is added
> **＋** `rule-case-build` — the instructions of `case-guppi`, which fix a finding in the Case and say in `context` why a page stands
> **＋** `vault/raw/2026-10-04/1439/cases/case-628.md` — Case 628, which changes another sentence of `rule-orchestration`
> **＋** `estimate-case-check-sends-back-a-faulty-case` and `estimate-case-check-sends-back-a-case-number-held-by-another-agent` — the checks of the answer's own Cases and of a number held by another agent

> **when:**
> `SubagentStop` fires when `case-guppi` answers with a Case, and `uv run guppi casecheck --subagent` reads the Cases of the answer, the plan file of the session, `<plan>.checked.json` beside it and the session's `raw/<date>/<hi HHMM>/ledger.md`.
> **＋** Or `tests/test_casecheck.py` runs it over a made-up plan file, store and ledger.
> **＋** The main agent receives the answer of `case-guppi` that passed, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The hook judges the Cases of the answer together with the other Cases of the session by `check_same_target` of `guppi/prespec.py`, imported, not copied: each Case of the plan file, and each entry of `<plan>.checked.json` under its number alone whose id the plan file does not hold.
> **＋** A Case of the answer whose `update` of a page sets one field to another value than another Case, writes a section that another Case writes, or replaces whole the Criterion of an Estimate that another Case replaces whole, gets a finding that names both Cases, the page and the field or the section.
> **＋** The finding is stored with the Case, the hook exits 2, and `case-guppi` answers again before the main agent shows the Case.
> **＋** Where the other Case should change rather than its own, `case-guppi` still changes its own Case so that no finding stands, and its `context` names the other Case and the change it needs; the main agent shows the Case as it stands and asks the person whether that other Case is built again, and on the person's yes sends it to its `case-guppi` by `SendMessage`, in a batch when it is ratified.
> **－** A stored Case that has findings, an entry joined with an agent id, and a Case whose number a `{supersedes:case N}` mark of the session's ledger names are not compared.
> **－** A Case whose id the answer holds is compared only as the answer holds it, and an answer that holds a top-level Case is compared with no part of that Case's family in the plan file or the store.
> **－** Two other Cases that clash with each other give this answer no finding.
> **－** The `Stop` hook `uv run guppi ratified` keeps its check of the Cases it writes, by the same function.

```then
create:
- slug: estimate-case-check-sends-back-a-clash-with-another-case
  kind: QA
  purpose: Whether the check of an answer of case-guppi sends back a Case that sets one field, writes one section or replaces one Criterion that another Case of the session, ratified or only stored, sets, writes or replaces too, and whether the main agent asks the person when the other Case should change instead
  method: uv run pytest tests/test_casecheck.py -k session_clash; then by hand a live answer of case-guppi that the hook sends back for a clash with another Case of the session, that Case shown and ratified once, and, where its context names another Case that should change, the main agent's question to the person and its SendMessage on a yes
  tags:
  - hooks
  - harness
  - workflow
  ref: rule-case-check
update:
- slug: rule-case-check
  replace:
  - old: the Case reaches the person in a file the hook writes from the answer that passed them (case 452.1).
    new: the Case reaches the person in a file the hook writes from the answer that passed them (case 452.1). The check of an answer compares its Cases with the other Cases of the session, ratified or not, by the judgment the check after ratification runs, so a Case that writes what another Case writes goes back to `case-guppi` before the person first sees it (case 629.1).
  change: the check of an answer compares its Cases with the other Cases of the session, from the plan file and the store (case 629.1)
- slug: rule-orchestration
  replace:
  - old: an answer in which a Case gives no such Estimate goes back to its `case-guppi` by `SendMessage` before it is shown (case 561.9);
    new: an answer in which a Case gives no such Estimate goes back to its `case-guppi` by `SendMessage` before it is shown (case 561.9); a Case whose `context` says that another Case of the session, which it was bounded around after a clash, should change instead is shown as it stands, and the main agent asks the person, in the shape of a question it puts itself, whether that other Case is built again, and on the person's yes sends it to its `case-guppi` by `SendMessage`, in a batch when it is ratified, as `## Showing and signing a Case` sets it (case 629.1);
  change: the main agent asks the person whether a Case that another Case was bounded around after a clash is built again (case 629.1)
```

```tasks
- [ ] update `rule-case-check`
- [ ] update `rule-orchestration`
- [ ] create `estimate-case-check-sends-back-a-clash-with-another-case`
- [ ] `guppi/casecheck.py`: `check_answer` judges the Cases of the answer with the other Cases of the session by `prespec.check_same_target` — the plan's Cases, then the store's entries under the number alone that the plan does not hold, built by `ratified.case_section`, without an entry with findings, one a `{supersedes}` mark of the ledger names, and the answer's own ids and the family of a top-level Case it holds, then the answer's Cases last — keeping each finding that opens with a Case of the answer; `subagent` passes the plan text; the docstring
- [ ] `guppi/prespec.py`: the docstring of `check_same_target` names its second caller, the check of the answer of `case-guppi`
- [ ] `tests/test_casecheck.py`: `-k session_clash` — a clash with a Case of the plan and with a stored Case not yet ratified, each sent back; none with a stored Case with findings, an entry joined with an agent id, one a supersedes mark names, the answer's own earlier version, or two other Cases that clash with each other
- [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
- [ ] read `estimate-case-check-sends-back-a-clash-with-another-case`
```

### Case 629.2 — `case-guppi` answers again by its changed sub-cases while the parent's own parts stand

> **given:**
> `rule-case-build` — the instructions of `case-guppi`, rendered into `.claude/agents/case-guppi.md`; one sentence changes
> **＋** `estimate-case-build-writes-the-case` — its Criterion replaced whole, its `method` set anew
> **＋** `rule-case-rebuild-cost` — the placeholder of the deferred decision, retired
> **＋** `rule-case-check` — the hook that checks the answer and writes the file of the Case
> **＋** `.claude/skills/grill-me/SKILL.md`, `vault/wiki/case-schema.md`, `vault/wiki/ratification.md`, `.claude/agents/ask-guppi.md` and `.claude/settings.json` — what `case-guppi` loads and reads
> **＋** `estimate-case-check-sends-back-a-ratified-case-in-another-shape` — the check of a ratified Case built again, which gives an answer of sub-cases alone no finding

> **when:**
> The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.
> **＋** Or the hook of `rule-case-check` sends its answer back with findings.

> **then:**
> `case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` whole before it answers.
> **＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
> **＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
> **＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in English, with no Case heading and nothing else but the context of a first round.
> **＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
> **＋** When no fork is open, its answer is the Case whole in English in the chat form of `vault/wiki/case-schema.md`, its ledger lines in the form of `vault/wiki/ratification.md`, from the heading to the fence of `ratification`, and nothing else.
> **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
> **＋** It runs on `model: opus` with `effort: medium` and the tools Read, Grep and Glob.
> **－** Asked again after the hook of `rule-case-check` sent findings back, or by a message, it answers with the changed sub-cases alone, each from its heading to the fence of its `ratification`, when the parent's `context`, `problem` and `recommend` stand as they were; an item of `recommend` whose answer changed only that sub-case stands under its heading, and the hook writes the sub-cases into the file of the Case beside the parts that did not change.
> **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
> **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
> **－** It writes no file and no ledger line.

```then
update:
- slug: rule-case-build
  replace:
  - old: when it sends findings back, fix the Case and answer with it whole again. Asked again by a message, answer with the Case whole again, changed as asked, or with a round when the message opens a fork.
    new: when it sends findings back, fix the Case and answer with it again. Asked again by a message, answer with the Case again, changed as asked, or with a round when the message opens a fork. An answer again holds the Case whole, or, where the parent's `context`, `problem` and `recommend` stand as they were, the changed sub-cases alone, each from its heading to the fence of its `ratification`, an item of `recommend` whose answer changed only that sub-case under its heading; the hook writes them into the file of the Case beside the parts that did not change (case 629.2).
  change: case-guppi answers again by its changed sub-cases alone while the parent's own parts stand (case 629.2)
- slug: estimate-case-build-writes-the-case
  set:
    status: pending
    method: 'by hand: live dispatches in a session after the render — one item with a fork, answered by a round and then the Case, one Case with a create without a ref, one that changes a hook, and a change the person asked for on one sub-case of a Case with sub-cases, answered by that sub-case alone; the tokens and seconds of each dispatch in the estimate line'
  change: the Criterion replaced whole — asked again, case-guppi answers by its changed sub-cases alone while the parent's own parts stand (case 629.2)
delete:
- slug: rule-case-rebuild-cost
  impact: the placeholder of the decision deferred by cases 566 and 570; the answer by changed sub-cases lands on rule-case-build and rule-case-check, the context's searches on rule-case-build, and the split of a large item is not done
```

```tasks
- [ ] update `rule-case-build`
- [ ] update `estimate-case-build-writes-the-case`
- [ ] delete `rule-case-rebuild-cost`
- [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [ ] read `estimate-case-build-writes-the-case`
```

### Case 629.3 — The check judges a lone sub-case with its stored parent

> **given:**
> `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent` — the new promise, on `rule-case-check`
> **＋** `rule-case-check` — the check of the answer of `case-guppi`
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py` — the hook and its tests
> **＋** `guppi/prespec.py` — `judge`, whose frame check reads a sub-case's `given` from its parent; `/pre-spec`, which runs it over the plan
> **＋** `<plan>.checked.json` — the store of checked answers

> **when:**
> `SubagentStop` fires when `case-guppi` answers with sub-cases of a Case N alone, and `<plan>.checked.json` beside the plan file of the session holds Case N under its number alone.
> **＋** Or `tests/test_casecheck.py` runs `uv run guppi casecheck --subagent` over such an answer and a made-up store.

> **then:**
> The hook builds the Spec text it judges with the stored section of Case N before the sub-cases of the answer, so `prespec.judge` of `guppi/prespec.py` reads the `given` and `context` of Case N for a sub-case of the answer that has none of its own, as `/pre-spec` reads them in the plan.
> **＋** A slug or a path in a code span of the `when` or `then` of such a sub-case, or a slug of its `then` block, that the `given` of Case N does not name is a finding of that sub-case, stored and sent back as any other finding.
> **－** A finding or a note on Case N itself is not given to the answer, and Case N is neither stored nor written again from this answer.
> **－** With no stored Case N, the sub-cases are judged alone, and a sub-case with no `given` of its own gets no finding on its frame.

```then
create:
- slug: estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent
  kind: QA
  purpose: Whether the check of an answer of case-guppi that holds sub-cases alone judges their frame against the given of their stored parent, and gives the answer no finding of the parent itself
  method: uv run pytest tests/test_casecheck.py -k lone; then by hand a live answer of case-guppi with sub-cases alone, its stored entries and the findings sent back read against the Criterion
  tags:
  - hooks
  - harness
  - workflow
  ref: rule-case-check
```

```tasks
- [ ] create `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent`
- [ ] `guppi/casecheck.py`: `check_answer` puts the section of the stored top-level Case of a lone sub-case, built by `ratified.case_section` from its entry under the number alone, before the sub-cases in the Spec text it judges, and keeps only the findings and notes of the answer's Cases; the docstring
- [ ] `tests/test_casecheck.py`: `-k lone` — a lone sub-case whose `then` names a slug the stored parent's `given` does not name gets a finding; one whose names stand there gets none; a finding of the stored parent is not given to the answer; with no stored parent, no frame finding
- [ ] read `estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent`
```

### Case 629.4 — The titles of the rounds are looked for in the stored `recommend` too

> **given:**
> `estimate-case-check-requires-each-question-of-the-rounds` — its Criterion replaced whole, its `method` set anew
> **＋** `rule-case-check` — the check of the answer of `case-guppi`
> **＋** `guppi/casecheck.py` and `tests/test_casecheck.py` — the hook and its tests
> **＋** `.claude/skills/grill-me/SKILL.md` — the title line of a question of a round
> **＋** `<plan>.checked.json` — the store of checked answers

> **when:**
> `SubagentStop` fires when `case-guppi` answers with a Case, and `agent_transcript_path` holds the agent's earlier outputs with no Case heading, which are its rounds of questions on that Case.

> **then:**
> `uv run guppi casecheck --subagent` takes the title of each question of those rounds from its line `❓ **Q<n>** - **<title>**:`, the title line of the template of `.claude/skills/grill-me/SKILL.md`.
> **＋** It takes titles only from a round that the function of `guppi/casecheck.py` that judges the form of a round finds in form, the function the check of 601.1 sends a round back by; a round out of form gives no title.
> **＋** A title that no item of a `recommend` opens with, in bold, among the Cases of the answer and the entries of `<plan>.checked.json` under the number alone of each Case of their family that the answer does not hold, is a finding of the top-level Case — of the first Case of the answer when it holds sub-cases alone — that names the title, sent back and stored as any other finding.
> **－** An answer with no earlier round gives no such finding.
> **－** A title asked in more than one round is looked for once.
> **－** The words of an item after its title are not judged.
> **－** A round out of form that came back unchanged, passed the check of its form and was shown gives no title either.

```then
update:
- slug: estimate-case-check-requires-each-question-of-the-rounds
  set:
    status: pending
    method: 'pytest tests/test_casecheck.py -k rounds over a temp agent transcript: a round and a Case whose recommend holds every title, one that misses a title, a title asked in two rounds, a round out of form whose titles are not required, an answer with no round, and an answer of sub-cases alone whose titles stand in the recommend of its stored parent; then by hand a Case the hook sends back for a missing title'
  change: the Criterion replaced whole — a title held in the stored recommend of a Case of the family that the answer does not hold is no finding (case 629.4)
```

```tasks
- [ ] update `estimate-case-check-requires-each-question-of-the-rounds`
- [ ] `guppi/casecheck.py`: `check_rounds` reads the titles of the `recommend` of each stored entry, under the number alone, of the family of the answer's Cases that the answer does not hold; the docstring
- [ ] `tests/test_casecheck.py`: `-k rounds` — an answer of sub-cases alone whose round titles stand in the stored parent's `recommend` gets no finding; a title in neither gets one
- [ ] read `estimate-case-check-requires-each-question-of-the-rounds`
```

### Case 629.5 — `context` keeps only the searches the Case rests on

> **given:**
> `rule-case-build` — the instructions of `case-guppi`, rendered into `.claude/agents/case-guppi.md`; one sentence is added
> **＋** `estimate-case-build-checks-the-finished-case` — its Criterion replaced whole, its `purpose` and `method` set anew
> **＋** `.claude/agents/ask-guppi.md` — the recipe whose index lines it reads for a fact no slug marks
> **＋** `vault/wiki/rules/` and `.claude/` — where it searches for the words that name a moment
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the case files of the Cases its prompt names

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, has built a Case and is about to answer with it.

> **then:**
> It puts each option the person chose in its rounds, or the person's own words where they answered outside the options, beside the `then` and `recommend` of the Case, and the Case holds each one; where the frame shows after a round that a chosen option cannot hold as written, its answer is a round on that point, not a Case with another behaviour.
> **＋** For each page whose text the change makes false, it searches the live pages of the vault, leaving out the Decision pages, and the code, for the page's slug, and reads each hit that `given` does not name around the line of the hit; for a fact that no slug marks, it reads the index lines of the recipe of `.claude/agents/ask-guppi.md` and judges them by meaning.
> **＋** When the change sets what happens at a moment — a reply, a hook event, a command — it searches `vault/wiki/rules/` and `.claude/` for the words that name that moment, reads each passage of each hit that sets a form or a behaviour at that moment, and the Case either does not cover that moment or names the other rule in `given`.
> **＋** It reads the case file `raw/<date>/<hi HHMM>/cases/case-<N>.md` of each Case of the session that the prompt of its call names, and no other Case of the session; where that Case changes a page the Case changes or sets what happens at the same moment, the Case does not cover that moment or names the case file in `given`, and its new text of that page does not contradict the text of that Case.
> **＋** When the Case replaces the Criterion of an Estimate, it reads the `purpose` and `method` of that Estimate, and the same `update` sets anew each one that states the old promise.
> **＋** Each hit that the change makes false enters the Case, or its `context` says why it stands.
> **＋** The `context` names a search only when the Case rests on it: a search with a hit that enters the Case, a search with a hit that stands and needs the reason why, or a search that a claim that no text says something rests on; a search that found nothing to change and that no claim rests on is left out.
> **＋** A claim of `context` about a text names the search it rests on: its pattern, the paths it ran over, and each file the search printed, a file it does not read included, or the count it printed; it claims nothing the search did not print.
> **＋** It reads side by side the finished new texts of all its sub-cases that change one page, and the Case holds no contradiction between them.
> **－** A hit in a History line, in `log.md` or in `brief.md` is not read.

```then
update:
- slug: rule-case-build
  replace:
  - old: A claim of `context` about a search names its pattern and the paths it ran over,
    new: '`context` names a search only when the Case rests on it: a search with a hit that enters the Case, with a hit that stands and needs the reason why, or that a claim that no text says something rests on; a search that found nothing to change and that no claim rests on is left out (case 629.5). A claim of `context` about a search names its pattern and the paths it ran over,'
  change: the context of a Case keeps only the searches the Case rests on (case 629.5)
- slug: estimate-case-build-checks-the-finished-case
  set:
    status: pending
    purpose: Whether case-guppi checks its finished Case before it answers — the chosen options, the pages that name a slug the change makes false, the rules that act at the moment the change sets, the Cases of the session its prompt names, the purpose and method of an Estimate whose Criterion it replaces, what each search printed and that the context keeps only the searches the Case rests on, the sub-cases that change one page — counted by what ask-guppi still finds at pre-spec
    method: 'by hand: at /pre-spec of a later session after the render, the report of ask-guppi read for each Case case-guppi built — a Case that departs from a chosen option, a page naming a changed slug that the Case misses, a rule acting at the same moment that the Case misses, a Case of the session named in the prompt whose page or moment the Case clashes with, an Estimate whose purpose or method still states the promise its replaced Criterion dropped, a claim of context that its search did not print, a search in context that the Case does not rest on, two sub-cases whose texts on one page contradict; the count of each in the reading line'
  change: the Criterion replaced whole — the context names only the searches the Case rests on (case 629.5)
```

```tasks
- [ ] update `rule-case-build`
- [ ] update `estimate-case-build-checks-the-finished-case`
- [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [ ] read `estimate-case-build-checks-the-finished-case`
```

## Deferred

## Case 630 — A moment in Work Mode for the person to change a ratified Case waits for a later session

> **context:**
> `estimate-spec-write-reaches-the-approved-spec` waits for a Case ratified in Work Mode, and `/work` runs to the librarian with no stop for the person, as `vault/wiki/where-to-stop.md` sets it; its condition 4, a task whose text opens with `stop:`, is the one stop a Spec can carry. The lesson `lesson-work-mode-a-staged-moment-promised-inside-a-run-with-no-stop` of session 0112 records the agent promising such a moment that never came. In session 1439 the person put the remaining items off to go to work.

> **problem:**
> Whether Work Mode gives the person a moment to ask a change of a ratified Case, by a `stop:` task or otherwise, is put off.

```then
defer:
  - slug: estimate-spec-write-reaches-the-approved-spec
    type: estimate
    purpose: "A Case ratified after the approval reaches spec.md from its stored answer; its reading by hand waits for a Case ratified in Work Mode, which no stop of /work yet gives the person"
```

## Case 631 — The reading of make lint with a red backlog step waits for a later session

> **context:**
> `estimate-lint-runs-every-step` is read by hand at the Baseline of a `/work` whose backlog step is red, a moment no session has met, and `vault/wiki/` is written by no hand, so it cannot be staged as the method reads. In session 1439 the person added the item of a method that spoils `backlog.md` for one run of `make lint` and restores it by `git checkout`, then put it off to go to work.

> **problem:**
> Whether the method of `estimate-lint-runs-every-step` reads `make lint` over a tree whose `backlog.md` is spoiled for the run is put off.

```then
defer:
  - slug: estimate-lint-runs-every-step
    type: estimate
    purpose: "Whether make lint runs all five steps when an earlier one is red; its reading waits for a Baseline whose backlog step is red, or for a method that stages one"
```
