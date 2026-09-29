## Case 500 — Slice 3g: the Estimates of the librarian's and the vault's tools recut to one Criterion, and the note on the old shape gives way to its removal

> **context:**
> Each Estimate page holds one promise, its Criterion. A Criterion should hold only `When:`, the trigger and the input it acts on, and `Then:`, what must hold after. The page carries its promise as a `purpose` field and its way of checking as a `method` field. The older Estimates lack both fields. They carry `## Context` and `## Method` and stack `### case N` blocks, and `make lint` counts them as `unmigrated`. This group holds the last five: `estimate-ask-finds`, `estimate-index-check-merges`, `estimate-cleanup-moves`, `estimate-raw-archive` and `estimate-tests-clock-pinned`. Here is where it goes wrong: `estimate-cleanup-moves` holds a head paragraph and three blocks. One block moves the old archive folders once. One tells `cleanup.py` to stop writing index files that no longer exist. One gives the page "a `### case 102.2` block, `pending`". A new reading cannot tell those acts from the promise.
> The person decided in the first round on this item. The twelve old pages went in three Cases by area: case 498 took rendering and settings, case 499 the end of a session, and this Case takes the rest. Each page gets one Criterion, no page is split, and each live half of a reading stays. This last Case replaces the note of Slice 3g with a note on removing the checks of the old shape once lint counts zero, so Slice 3g stays open (case 202). This Case closes the Frontier line C1. A Criterion that records a one-time act gets a Criterion of the repeating behaviour (case 485). None of the five has `purpose` or `method`, so each `update` sets both, and setting `method` drops `## Context` and `## Method` (case 211). Each Criterion is replaced whole and goes back to `pending`, and its reading waits for a later session (case 428.1). All five rules go from `built` to `draft` until the reading. None of the five lost its Criterion to a tool fault like case 211.3. Their History shows only Criteria that cases 23.1, 33, 35.1, 100.1, 102.2, 105.1, 145.1, 147.2, 147.3, 147.6, 166.4 and 174 wrote on purpose, so nothing is restored.
> What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording. The content of the old lines is carried, except for the lines named here. Each line that gives a page a block or sets it `pending` goes out as bookkeeping. In 500.1 two lines go out as a one-time Research question: "whether `@` expands in an agent file" and "the tokens of one dispatch". Block 147.2 quoted the new Render. It becomes the behaviour that Render gives, the Grep of the rules first, and the line "No read of a `*-index.md`" goes out, because the files no longer exist. The name of the fifth answer line, tags/slug, stands in plain text, because a code span with a `/` reads as a path that `given` must name. In 500.2 "The name of the rule does not change" goes out as a bound of an edit, and the head's "comparisons made per category" is now the Grep and its count that the Render names. The Render also leaves Estimates out of the check, and that is kept. In 500.3 the migration of block 102.2 and the removal of the index writer of 147.6 go out as one-time acts, and so does "no index file is written". The History and `log.md` lines are worded as `history` in `guppi/cleanup.py` writes them: the page gets its line, and `log.md` gets the same text with the page's category and slug in front. In 500.4 the `－` line "a date-level unit dated the day of the run is not looked at" is carried by the first `＋` line, and "that gap is `rule-materialize`'s" goes out as a pointer. In 500.5 the old line names `guppi.ledger.run`, but `tests/test_conftest.py` calls `guppi.event.run`. So the line promises a `run()` without `now`, as the test reads it. "`make test` is green on the tree of this session" moves into `method`. The `Makefile` half of the last `－` line goes out as a bound of an edit, and the `test-*` targets stay.
> The check also notes that 500.4 shares words with 500.1 on the day's event log, and with 500.3 on the exit codes and the rerun. This is expected. In 500.1 each dispatch of `ask-guppi` is written into the event log. In 500.4 `guppi archive` leaves the event log where it is. 500.3 and 500.4 are two scripts with the same contract for a failed move and a rerun, each promised for its own script and read by its own test file, as cases 33 and 100.1 signed them.
> The frame. The kept lines were read against `.claude/agents/ask-guppi.md`, the Render of `rule-index-check`, `guppi/cleanup.py`, `guppi/archive.py`, `tests/conftest.py`, `tests/test_conftest.py` and the frame of the librarian, and none is contradicted but the one line of 500.5 named above. Stdout lines, History lines and headers that hold a `/` stand in plain quotation marks or in words. `estimate-sprint-migration-lint-clean` promises that `unmigrated` is at zero at the close. This Case makes the count zero after the librarian's run and does not change that promise, so it is not touched. `estimate-lint-counts-the-unmigrated` stays true at zero, since it promises no line then. No behaviour changes, so no code, test, Render or hook changes, and no reader keeps an old form. The Case creates no page, so no vault query was run. Not done: the removal of the checks of the old shape, which the new note holds for a later session, and with it the wording of the Criterion of `estimate-sprint-migration-lint-clean` on the counter.

> **problem:**
> The last five Estimates of the old layout still have no `purpose` or `method`, still carry `## Context` and `## Method`, and stack blocks that record migrations, removed index files and one-time questions next to their promise. Lint counts them as `unmigrated`. The note of Slice 3g asks for exactly this recut, and nothing but a Case removes it.

> **recommend:**
> Replace each Criterion whole with one `When:` and `Then:` of the repeating behaviour. Set `purpose` and `method`, and carry the one line of 500.5 as the test reads it. Replace the Slice note with the note on removing the old-layout checks. Closing Slice 3g now and sending the removal to the Backlog was rejected in the first round, because the removal belongs to this Slice.

### Case 500.1 — `ask-guppi` finds a page by meaning and answers in five lines

> **given:**
> `estimate-ask-finds` — the promise, its Criterion replaced whole
> **＋** `rule-ask` — the rule it promises for
> **＋** `.claude/agents/ask-guppi.md` — the agent rendered from `rule-ask`
> **＋** `vault/wiki/rules/` — the rule pages the agent greps first
> **＋** `vault/archive/` — the archive, searched by slug alone
> **＋** `vault/raw/<date>/event_log.md` — the day's event log

> **when:**
> The main agent dispatches `ask-guppi` through the `Agent` tool with a question, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> The answer is exactly five lines: `exists`, `near`, `missing`, `rules` and the tags/slug line, each present, "none" when empty. No index line or page text reaches the caller beyond them.
> **＋** The agent starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs one Grep per other category the question touches.
> **＋** A question about an existing page names its slug under `exists`, whether it is asked in English or in Russian.
> **＋** A proposal that crosses a rule or a lesson, such as a `SessionStart` hook meant to block, names it on the `rules` line.
> **＋** A named slug gets on the tags/slug line `free`, `live` with its category, or `archived at <path> by [[decision-case-N]]`, found by a Glob over `vault/archive/`, N from the `origin` of the archived page.
> **＋** The agent opens an archived page only when the question names its slug and asks what it said or why it was withdrawn.
> **＋** Each dispatch stands in `vault/raw/<date>/event_log.md`.
> **－** The archive is not searched by meaning: the `exists` and `near` lines name live pages only.

> **tasks:**
> - [ ] update `estimate-ask-finds`
>   - set: `{status: pending, purpose: "ask-guppi finds a page by meaning in either language, names the rule a proposal crosses and the state of a named slug, and answers in five lines", method: "by hand in a later session: three dispatches of ask-guppi, one existing page asked in English and in Russian, one proposal that crosses a known rule, each read against the event log"}`
>   - change: `the Criterion replaced whole — the head and the blocks 105.1 and 147.2 into one When and Then, the one-time questions and the index files out; purpose and method set, Context and Method out (case 500.1)`
> - [ ] read `estimate-ask-finds` — by hand on three dispatches in a later session

> **ratification:**
> ```
> - decision[case 500.1][update][estimate-ask-finds]{ref:estimate-ask-finds}
> ```

### Case 500.2 — The librarian's index check merges a duplicate within its category

> **given:**
> `estimate-index-check-merges` — the promise, its Criterion replaced whole
> **＋** `rule-index-check` — the rule it promises for, spliced into the librarian's frame
> **＋** `.claude/agents/librarian-guppi.md` — the librarian's frame that holds the check
> **＋** `vault/wiki/` — the category folders the Grep reads

> **when:**
> The librarian's run does the index check of `.claude/agents/librarian-guppi.md`, as rendered from `rule-index-check`, over the `create` entries of each `materialize.yaml`.

> **then:**
> For each `create` other than an Estimate, the librarian runs the Grep of its category under `vault/wiki/`: `^(purpose|deferred_by):`, `root_cause` for lessons, `pattern` for insights. It compares the entry's `purpose`, or `root_cause` for a lesson, with every line the Grep returns.
> **＋** The report names each Grep and the number of lines compared.
> **＋** A `create` whose thing already has a page becomes an `update` of that slug with `change: "merged by librarian: <why>"` and `librarian: merged`, every other field of the entry as it was.
> **＋** A page that is close but not the same keeps the entry and adds `near: <slug>`.
> **＋** Every page opened is named in the report, with the index line that did not settle same or near.
> **－** No comparison crosses categories.

> **tasks:**
> - [ ] update `estimate-index-check-merges`
>   - set: `{status: pending, purpose: "The librarian's index check turns a create whose thing already has a page into an update of that page and marks a near one, comparing within one category by the Grep of its index lines", method: "by hand on the report of a later librarian's run, against its materialize.yaml"}`
>   - change: `the Criterion replaced whole — the head and the block 147.3 into one When and Then, the bound on the rule's name out; purpose and method set, Context and Method out (case 500.2)`
> - [ ] read `estimate-index-check-merges` — by hand on the report of a later librarian's run

> **ratification:**
> ```
> - decision[case 500.2][update][estimate-index-check-merges]{ref:estimate-index-check-merges}
> ```

### Case 500.3 — `cleanup` moves an archived page out and a restored one back

> **given:**
> `estimate-cleanup-moves` — the promise, its Criterion replaced whole
> **＋** `rule-cleanup` — the rule it promises for
> **＋** `guppi/cleanup.py` — the script `guppi cleanup`, its `history` and its `unlink`
> **＋** `vault/wiki/` — the live pages and `log.md`
> **＋** `vault/archive/<sprint>/<date>/<HHMM>/<category>/` — the archive folder of a moved page
> **＋** `vault/raw/<date>/` — the date folder whose latest session names the run
> **＋** `tests/test_cleanup.py` — the tests the reading runs

> **when:**
> `uv run guppi cleanup` runs over the live pages of `vault/wiki/` and the pages under the archive.

> **then:**
> A live page with `status: archived` moves under the same file name to `vault/archive/<sprint>/<date>/<HHMM>/<category>/`. The date is the day of the run, and the session is the latest session folder of `vault/raw/<date>/`, else the latest of the nearest date back. With no session folder at all, the page goes into the category folder under the date, with no session level.
> **＋** The moved page gets the History line "- <date> archived · cleanup", and a page moved back gets "- <date> restored · cleanup". Each History line that cleanup writes also goes to `log.md` with the page's category and slug in front, such as "- <date> <category>/<slug> archived · cleanup".
> **＋** Its slug leaves the `children` of live pages and the `estimates` of entities and rules, the field only, and that page gets the History line "- <date> child <slug> archived · cleanup" or "- <date> estimate <slug> archived · cleanup". No section is rebuilt, and an Insight's `children` keep the slug.
> **＋** Wikilinks in page bodies stay, and a page with any other status stays.
> **＋** A page under the archive, at any depth, whose status is no longer `archived` moves back to its category folder under `vault/wiki/`.
> **＋** A live page whose `parent` or `target` is archived is reported on stderr and left.
> **＋** A rerun moves nothing and exits 0. A file that cannot move, or a name already taken in the archive, is a line on stderr and exit 1, and the other pages still move.
> **＋** Live, a run with nothing to move exits 0 and leaves `git diff` empty.

> **tasks:**
> - [ ] update `estimate-cleanup-moves`
>   - set: `{status: pending, purpose: "guppi cleanup moves an archived page into the archive of the session of the run and a restored one back, and unlinks its slug from the live lists without rebuilding a section", method: "pytest tests/test_cleanup.py, plus by hand on the cleanup of a later librarian's run"}`
>   - change: `the Criterion replaced whole — the head and the blocks 102.2, 147.6 and 166.4 into one When and Then, the one-time migration and the index files out, the History and log lines as the script writes them; purpose and method set, Context and Method out (case 500.3)`
> - [ ] read `estimate-cleanup-moves` — `pytest tests/test_cleanup.py`, then by hand on the cleanup of a later librarian's run

> **ratification:**
> ```
> - decision[case 500.3][update][estimate-cleanup-moves]{ref:estimate-cleanup-moves}
> ```

### Case 500.4 — `archive` moves a done unit of raw whole into the archive

> **given:**
> `estimate-raw-archive` — the promise, its Criterion replaced whole
> **＋** `rule-raw-archive` — the rule it promises for
> **＋** `guppi/archive.py` — the script `guppi archive`, with `materialize.parse_line` for the record lines
> **＋** `vault/raw/<date>/` — a date folder, its date-level `ledger.md` and its `event_log.md`
> **＋** `vault/raw/<date>/<HHMM>/` — a session folder
> **＋** `vault/archive/<sprint>/<date>/raw/` — the archive of a date-level unit
> **＋** `vault/archive/<sprint>/<date>/<HHMM>/raw/` — the archive of a session
> **＋** `tests/test_archive.py` — the tests the reading runs

> **when:**
> `uv run guppi archive` runs, as a step of the librarian's run or by hand, over the units under `vault/raw/<date>/`.

> **then:**
> A unit is a session folder `vault/raw/<date>/<HHMM>/` that holds a `ledger.md`, or a date-level `ledger.md` at the root of `vault/raw/<date>/` with its yaml. A unit is done when its yaml exists, every entry under `entries` carries `applied` or `superseded_by`, and the number of every line of its `ledger.md` that `materialize.parse_line` reads as a record stands in the `line` or `folded` of an entry or under `unparsed`.
> **＋** Only units dated before the day of the run are looked at. The session of the run is never looked at, even when it is dated before the run day: it is the latest session folder of the run day, else of the nearest date back.
> **＋** A done session moves whole to `vault/archive/<sprint>/<date>/<HHMM>/raw/`. A done date-level ledger moves with its yaml and everything else at the date root to `vault/archive/<sprint>/<date>/raw/`. With it goes every session folder of the date that has no ledger of its own, each to `vault/archive/<sprint>/<date>/<HHMM>/raw/`. No file is cut.
> **＋** `event_log.md` stays in `vault/raw/<date>/`.
> **＋** Stdout holds one line per unit: "archive: raw/<date>/<HHMM> → archive/<sprint>/<date>/<HHMM>/raw", "archive: raw/<date> → archive/<sprint>/<date>/raw", or "archive: raw/<date>[/<HHMM>] kept: <reason>". The reason is `no yaml`, `N entries not applied` or `N ledger lines outside the yaml`.
> **＋** The exit is 0. A name already taken in the archive, or a move that fails, is a line on stderr and exit 1, and the other units still move. A rerun moves nothing and exits 0.
> **－** `origin`, History, `log.md` and the yaml are not rewritten.
> **－** A folder without `ledger.md` is not a unit.
> **－** An entry that a supersedes from another unit did not mark keeps its unit in `vault/raw/<date>/`.

> **tasks:**
> - [ ] update `estimate-raw-archive`
>   - set: `{status: pending, purpose: "guppi archive moves a done unit of raw whole into the archive of its date, keeps an undone one with its reason, and never touches the session of the run", method: "pytest tests/test_archive.py, plus by hand on the archive step of a later librarian's run: its stdout, the raw folder and the origin findings of make lint before and after"}`
>   - change: `the Criterion replaced whole — the block 100.1 as When and Then, the pointer to rule-materialize out; purpose and method set, Context and Method out (case 500.4)`
> - [ ] read `estimate-raw-archive` — `pytest tests/test_archive.py`, then by hand on the archive step of a later librarian's run

> **ratification:**
> ```
> - decision[case 500.4][update][estimate-raw-archive]{ref:estimate-raw-archive}
> ```

### Case 500.5 — The clock of the tests is pinned

> **given:**
> `estimate-tests-clock-pinned` — the promise, its Criterion replaced whole
> **＋** `rule-tests-clock-pinned` — the rule it promises for
> **＋** `tests/conftest.py` — the autouse fixture
> **＋** `tests/test_conftest.py` — the test of the fixture
> **＋** `tests/` — the suite the fixture covers
> **＋** `guppi/` — the modules whose clock is pinned
> **＋** `Makefile` — the targets `test` and `test-*`

> **when:**
> `pytest` collects `tests/`, and a test calls the `run()` of a module of `guppi/` without `now`, or the code reads the clock outside `run()`.

> **then:**
> Before every test, an autouse fixture in `tests/conftest.py` sets into every module of `guppi/` that carries a `datetime` attribute a subclass whose `now(tz=None)` returns `2001-01-01 00:00:00 UTC`, and `astimezone` gives the same second. A test that leaves the code on the real clock sees the year 2001 and fails on the day it is written.
> **＋** The list of modules comes from a walk over `guppi/`, never from a hand list: a new module with a clock is covered with no change to the fixture.
> **＋** `tests/test_conftest.py` shows it: a `run()` without `now` writes a time dated 2001, and `datetime.strptime`, `fromisoformat` and the constructor of the subclass work as before.
> **＋** The targets `test` and `test-*` of the `Makefile` run under the same fixture.
> **－** A test that passes `now` does not notice the fixture: `run()` reads no clock.

> **tasks:**
> - [ ] update `estimate-tests-clock-pinned`
>   - set: `{status: pending, purpose: "A test that leaves the code on the real clock fails on the day it is written: every guppi module's clock is pinned to 2001 by one autouse fixture", method: "pytest tests/test_conftest.py, plus make test green under the fixture"}`
>   - change: `the Criterion replaced whole — the block 145.1 as When and Then, the run the test calls named as it reads, the green run of make test into method; purpose and method set, Context and Method out (case 500.5)`
> - [ ] read `estimate-tests-clock-pinned` — `pytest tests/test_conftest.py`, then `make test` after the Work Mode of a later session

> **ratification:**
> ```
> - decision[case 500.5][update][estimate-tests-clock-pinned]{ref:estimate-tests-clock-pinned}
> ```

### Case 500.6 — The note of Slice 3g gives way to the removal of the old-layout checks

> **given:**
> `entity-sprint-migration` — the sprint page; its Slice 3g holds the note on the old shape
> **＋** `guppi/sprint.py` — renders a note as `- [ ] <text>` and never ticks it
> **＋** `vault/wiki/sprint.md` — the render of the sprint page
> **＋** `/hi` — builds the Frontier from `vault/wiki/sprint.md`
> **＋** `rule-ask` — a rule whose Estimate this Case recuts
> **＋** `rule-index-check` — a rule whose Estimate this Case recuts
> **＋** `rule-cleanup` — a rule whose Estimate this Case recuts
> **＋** `rule-raw-archive` — a rule whose Estimate this Case recuts
> **＋** `rule-tests-clock-pinned` — a rule whose Estimate this Case recuts

> **when:**
> `uv run guppi sprint` renders `vault/wiki/sprint.md` from `entity-sprint-migration` at the librarian's run, and the next `/hi` builds the Frontier from it.

> **then:**
> Slice 3g holds one note, on removing the checks of the old shape once `make lint` counts no `unmigrated` page, and the Frontier holds it as a `C` line. The note on the old shape recut is gone from the page and from the render.
> **＋** The History of `entity-sprint-migration` says that the Estimates of the librarian's and the vault's tools are recut and that the recut of the old shape is done.
> **－** No line is added to `## Closed`: Slice 3g stays open.
> **－** The checks of the old shape do not change in this Case.

> **tasks:**
> - [ ] update `entity-sprint-migration`
>   - old: `` - the old shape recut: every Estimate whose Criterion still holds `### case N` blocks brought to one Criterion, until lint counts no `unmigrated` page ``
>   - new: `` - the old shape removed: once `make lint` counts no `unmigrated` page, the checks of the shape before case 193 leave the scripts, `rule-estimates-schema` and `estimate-lint-counts-the-unmigrated` (case 202) ``
>   - change: `Slice 3g: the Estimates of rule-ask, rule-index-check, rule-cleanup, rule-raw-archive and rule-tests-clock-pinned recut to one Criterion; the recut of the old shape done (cases 498-500), its note replaced by the note on removing the checks of the old shape`
> - [ ] `uv run guppi sprint`

> **ratification:**
> ```
> - decision[case 500.6][update][entity-sprint-migration]{ref:entity-sprint-migration}
> ```
