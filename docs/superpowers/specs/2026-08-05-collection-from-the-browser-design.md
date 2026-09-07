# Slice 2b — collection from the browser

**Date:** 2026-08-05
**Status:** design, approved in conversation, no code yet
**Predecessor:** `2026-08-05-vacancies-as-a-tool-design.md` (slice 2a, merged as `51bd4dd`).
Section 12 of that document is the source material this one replaces.

The page `/vacancies` is a tool for reading collected vacancies. It cannot collect
them: that still means a terminal, `uv run python -m jobhunt.cli parse --profile … --mode full`,
and knowing which mode to pass. This slice puts collection behind two buttons and
makes a run that takes minutes observable while it runs.

---

## 1. Scope

**In:** two collection buttons on `/vacancies`, a background run inside the app
process, a live progress line, protection against a second run, an honest summary
when it ends, and the table refreshing itself with the current filters.

**Out, deliberately:**

- **The «условия изменились» banner** (tags or the collection frame changed since the
  last run). It needs a snapshot of the conditions at run time — its own mechanism and
  its own edge cases. Deferred by the owner's decision.
- **A schedule** («collect every morning»). The moment it appears, the executor has to
  outlive both the browser and the request; that is the queue this design deliberately
  does not build (§3).
- **Resuming an interrupted run.** A run killed mid-way is marked `interrupted` and can
  be started again from the beginning. What it had already collected survives — the
  runner commits after every source+tag pair.
- **Cancelling a run from the page.** Nothing stops a run except the process dying.
- **Adding or removing tags and editing the collection frame from the browser** — slice 3.

## 2. Decisions taken before the design

Four questions were answered by the owner; each one closed a fork rather than a detail.

**Durability: the tab does not matter, a restart interrupts.** The run lives in the app
process. Closing the tab does nothing to it; restarting the container kills it, and the
run is then marked interrupted rather than resumed. This is what makes a thread
sufficient and a job queue unnecessary.

**Progress: a counter over pairs plus what is running right now.** Not a bare spinner,
because a run of several minutes with no numbers is indistinguishable from a hung one.
The denominator is exact — tags × sources are known before the first request.

**Both modes are exposed, with labels that name the purpose.** «Проверить новое» and
«Полная сверка», each with one line of explanation underneath.

**The banner is deferred** (§1).

## 3. Why a thread and not a queue

Three executors were considered.

**A thread inside the app process, with the state in the database — chosen.** The route
starts a daemon thread which calls `run_profile` with its own session factory. The truth
about "is a run in progress" lives in the database, not in process memory, because
`parse` from the host has not gone anywhere: an in-memory guard would not see it at all.
Progress is read from journal rows that are already committed per pair — no new
mechanism is needed to produce it.

**FastAPI `BackgroundTasks`** — less code, but the task is tied to a request/response
pair, there is no handle on it, and an exception inside it goes nowhere. Observability
and the guard would still have to go through the database, so the work above remains,
minus the control.

**A separate worker container with a job queue in the database** — the honest
decoupling, and the right answer the day a schedule appears. It costs a new compose
service, a new lifecycle and a new class of failures, and it buys durability across
restarts, which the owner explicitly does not want. The road stays open: §4 puts the
run's state in the database, which is where a queue would read it from.

## 4. Data model

Today `ParseRun` is one row per **source + tag pair**. There is no entity for "a run of a
profile": the four requests behind one press are not related to each other by anything.
The panel needs exactly what is missing — a denominator, a "running now" flag, a summary
and a guard.

### 4.1 New table `parse_batches`

| Column | Type | Meaning |
|---|---|---|
| `id` | UUID pk | |
| `profile_id` | UUID fk → `profiles`, `ON DELETE CASCADE` | whose collection |
| `mode` | `full` \| `quick` | same vocabulary as `ParseRun.mode` |
| `status` | `running` \| `finished` \| `interrupted` | lifecycle only — see below |
| `started_at`, `finished_at` | timestamptz | `finished_at` null while running |
| `planned_requests` | int | enabled tags × sources, fixed at open time |
| `started_by` | `web` \| `cli` | who owns the process running it (§7) |
| `last_progress_at` | timestamptz | touched after every finished pair |

`ParseRun` gains `batch_id` — a nullable FK to `parse_batches`. Nullable because the 40
rows already in the production database have no batch and inventing one for them would
be inventing a fact. Migration `0008`.

`planned_requests` is stored rather than recomputed: tags can be toggled while a run is
in flight, and a denominator that moves under the numerator is worse than none. It also
matches what the runner actually does — `run_profile` reads the tag set once, at the
start, and does not re-read it (its docstring says so explicitly).

**There is no `failed` status, on purpose.** The batch describes a lifecycle — started,
ended, or killed — not a verdict on the collection. A run in which every request failed
still ends as `finished`; what went wrong is in the journal rows, which already carry
`failed` / `truncated` / `ids_incomplete` per request and say which source and which tag.
A second place holding a verdict would eventually disagree with the first.

### 4.2 The batch is opened by a shared helper, not by the route

`ingest/batches.py`: `open_batch`, `finish_batch`, `touch`, `sweep_interrupted`. Both
entry points — the web route and `cmd_parse` — go through it. If the web opened batches
on its own, a run started from the terminal would be invisible to the guard and to the
status line, and the whole point of keeping the state in the database would be lost.

`run_profile` receives the batch id and fills the rest in: it stamps `batch_id` on every
`ParseRun` it creates, touches `last_progress_at` after each pair (the commit is already
there, so this costs nothing), and finalises the batch in its `finally`.

### 4.3 The guard is a partial unique index, not a check in code

```sql
CREATE UNIQUE INDEX uq_parse_batches_one_running_per_profile
    ON parse_batches (profile_id) WHERE status = 'running';
```

"Read, then insert" loses to two presses in a row; an index never does. The second press
gets a database error which the route turns into a message (§7).

### 4.4 The `running` row becomes observable — and that creates stuck rows

`run_source` inserts the journal row and finalises it inside one transaction, so
"running right now" is invisible from any other session. This is a known limitation
(state handoff, section 6). The fix is a commit right after the insert.

The same fix breaks the property that limitation was paired with: **an interrupted run
used to leave no dangling rows, and now it will.** Two things answer that, and neither
is optional:

- **`last_progress_at`.** A batch that has not moved for **30 minutes** is considered
  dead. **Corrected 2026-08-05 by the final review; the original number was 15 and the
  arithmetic under it was wrong.** The ceiling is not «25 pages × 2 s of pacing» — the
  stamp is written once per source+tag pair, so the gap to clear is the longest one pair
  can take, and that is bounded by the slowest source and by the request timeout, not by
  the pacing: dou.ua issues up to 41 requests (`max_batches=40` plus the first page)
  against `request_timeout_seconds = 30`, ≈ 21 minutes, and `HttpClient._respect_delay`
  subtracts elapsed time from the pacing, so a slow response absorbs the 2 s rather than
  adding to it. Fifteen sat *under* that ceiling, and this rule does more than colour a
  line: the next run supersedes a stale batch and starts collecting, so declaring a live
  runner dead puts two collection threads on one profile. Thirty clears the ceiling and
  still fails fast enough to be usable. Raise `max_batches`, `max_pages` or the timeout
  and this arithmetic has to be redone.
- **A sweep at container start** — `jobhunt sweep-batches`, called by
  `docker-entrypoint.sh` right after `alembic upgrade head`. Not the FastAPI
  lifespan, although that is the obvious place: inside the web process the only
  way to get a session outside a request is `session_scope()`, which reads
  `settings.database_url` — the developer's database. Every test that does
  `with TestClient(app)` would then sweep production data, which `CLAUDE.md`
  forbids outright. Batches with `started_by='web'` in status `running` become
  `interrupted`: the process that owned them has just died. Batches with
  `started_by='cli'` are left alone — they live in another process, and
  restarting the container is none of their business. The sweep also closes the
  `ParseRun` rows of those batches that were left in status `running`;
  otherwise the panel's "what is running now" would keep naming a request that
  ended when the process did.

## 5. What appears on the page

A collection panel above the table, next to the tag panel. Two buttons:

- **«Проверить новое»** — «верхушка выдачи за сутки; пропавших не трогает»
- **«Полная сверка»** — «вся выдача; отмечает исчезнувшие вакансии»

The subtitles are not decoration. The difference between the modes is not speed, it is
**the right to judge**: quick mode reads only the top of the listing (work.ua with the
"за добу" filter and at most 5 pages, dou.ua at most 3 batches), so absence from its
result means nothing, and it therefore never touches `mark_missing` or
`rebuild_tag_links`. Full mode walks the listing (up to 25 pages / 40 batches) and, if it
hits the ceiling, marks itself `truncated` / `ids_incomplete` and refuses to judge that
source anyway. A user who cannot see this difference will eventually deactivate live
vacancies by pressing the wrong button.

Under the buttons, one status line with three faces:

- **idle** — when the last run happened and how it ended: «сегодня в 14:20, полная
  сверка: 4 запроса, найдено 57, новых 0»
- **running** — «2 из 4 запросов: work.ua, „IT Director“, найдено 128»
- **ended badly** — see §7.

While a run is in progress both buttons are disabled and say why. This includes a run
started from the terminal, because the flag lives in the database.

## 6. Progress and completion

The panel is a self-refreshing fragment: `GET /vacancies/collection`.

While the batch is `running` the fragment carries `hx-trigger="every 3s"`; once the run
has ended the fragment no longer carries it and the polling stops by itself. No timer of
ours, no JavaScript.

The numbers come from rows that are already committed: the numerator is the count of
this batch's `ParseRun` rows that have finished, the denominator is `planned_requests`,
"what is running now" is the row still in status `running`, and "found" is the sum of
`found_count`.

**The table refreshes itself the htmx-native way.** The response in which the batch is
first seen to be finished carries `HX-Trigger: jobhunt-collected`; the filters form
gains a second trigger, `jobhunt-collected from:body`. The event name is spelled with a
dash and not a colon on purpose: `:` introduces modifiers in htmx's trigger grammar
(`delay:`, `from:`), and an event name is not the place to find out how its tokenizer
resolves the ambiguity. The table is re-requested **with
the current filters**, because the request still comes from the form — the panel knows
nothing about filters and must not.

Adding a trigger to that form is the same attribute that produced the double request
closed at the end of slice 2a. The rule holds: the form's trigger names its sources, and
the new event is a separate spec in the same list, not a widening of the existing one.

Three seconds against ~6 ms of render is two orders of magnitude of headroom, but the
number has to be measured on the production database, and the plan will say so.

## 7. Errors and edge cases

**Nothing to collect.** No profile, or no enabled tags: the buttons are disabled and say
what is missing. The same check `cmd_parse` already performs before it starts.

**A second press.** The refusal comes from the index. The route answers `409` with the
panel fragment; the global `htmx:responseError` handler in `base.html` swaps it in — the
same path already used by the status cell, verified in the browser in slice 2a.

**A run started from the terminal.** «Сбор идёт (запущен из терминала)», buttons
disabled. It cannot be stopped from the browser, and should not be — we do not own that
process.

**A restart mid-run.** The startup sweep marks the batch `interrupted`; the panel says
«прошлый сбор прерван перезапуском» and offers to run again. Everything collected before
the break survives.

**A stuck batch.** If the process was killed in a way that skipped the sweep — a
`SIGKILL`ed CLI run, say — the 15-minute rule applies: the panel reports that the run has
shown no sign of life since a given time, and a new run closes the stale batch as
`interrupted` **in the same transaction** in which it opens its own. Otherwise the unique
index would refuse the new one.

**Profiles are independent.** The index is per profile, so collecting for profile A does
not block profile B.

**Partial failure.** The summary must be honest: «4 запроса, 1 с ошибкой, 1 усечён».
What counts as a problem — `failed`, `truncated`, an incomplete id set, a tag too broad
— is defined today inside `cli.py` (`_is_broad_tag` and the four lists in `cmd_parse`).
It moves to a module both the CLI and the panel import, so the two cannot drift on what
a problem is. This is the only refactoring the slice takes on, and it takes it because
the alternative is two definitions of the same word.

**A failure inside the thread.** `run_profile` already isolates per-pair failures into
journal rows, and it is the one place that finalises the batch — in its own `finally`,
because it owns the batch id. The thread around it only closes the HTTP client and logs;
it does **not** finalise the batch a second time. One owner, or the two will disagree
about the end time and the status. If the process dies so hard that even that `finally`
does not run, the startup sweep and the 15-minute rule are what remain — which is
exactly the case they exist for.

## 8. Boundaries and tests

**The htmx target invariant already covers the panel** — every swap target declared in a
template must exist in the rendered page, checked for a profile with vacancies and for
one without. The panel is exactly the shape that produced Critical C2 in slice 2a: it
must be in the markup always, including for a profile with no tags at all.

**A new AST boundary:** no module under `web/` writes `parse_batches` directly —
constructing `ParseBatch`, or `update()`/`insert()`/`delete()` against it, is allowed
only in `ingest/batches.py`. The web layer reads the batch state through
`web/data/collection.py` and writes it only through that helper. The rule is stated in
§4.2; in this project a rule without a test has twice failed to survive a slice.

**One test per rule, each failing when its own protection is removed:**

| Rule | Test |
|---|---|
| One running batch per profile | opening a second one raises |
| The sweep is owner-aware | a `web` batch becomes `interrupted` at startup, a `cli` batch does not |
| The staleness rule | a batch with an old `last_progress_at` is superseded by a new run |
| Progress arithmetic | 4 planned, 2 finished, the third running → the expected line |
| The summary is honest | a batch with one failed and one truncated request says so |
| Modes differ in the right to judge | a quick run leaves `missed_checks` and tag links untouched |

**No thread is started in tests.** The route calls a start function which the test
replaces — the same technique the CLI tests already use on `run_profile`. No test reaches
the network; the existing network boundary guards the imports.

## 9. Requirements for the implementation plan

1. **The migration and `ingest/batches.py` come first**, before any route. The guard, the
   sweep and the staleness rule are the parts everything else assumes; building the panel
   first would mean building it against a state model that does not exist yet.
2. **The observability fix to `run_source` is its own task**, with the CLI as its first
   consumer: it changes transaction boundaries in the most dangerous code in the project,
   and it must not arrive bundled with a new page element.
3. **The shared problem-summary module is extracted before the panel uses it**, not
   after — a copy in the web layer would be a second definition from the first commit.
4. **The polling interval is measured on the production database** and the number goes
   into the plan, the way slice 2a measured the fragment response before deciding whether
   client-side filtering was needed.
5. **The last task is a live browser check** with a written list of scenarios, not a step
   inside another task. Slice 2a's list is in the state handoff, section 5в; the two
   harness traps recorded there (Cyrillic typed through `insertText` fires no `keyup`;
   first batches are not full lists) apply to whoever writes the next script.
