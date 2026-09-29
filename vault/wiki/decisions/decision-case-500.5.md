---
type: decision
case: "500.5"
status: current
update: ["[[estimate-tests-clock-pinned]]"]
origin: raw/2026-09-29/0137/ledger.md#case-500.5
sprint: migration
created: 2026-09-29
tags: [tests, harness]
---

## Context

Each Estimate page holds one promise, its Criterion. A Criterion should hold only `When:`, the trigger and the input it acts on, and `Then:`, what must hold after. The page carries its promise as a `purpose` field and its way of checking as a `method` field. The older Estimates lack both fields. They carry `## Context` and `## Method` and stack `### case N` blocks, and `make lint` counts them as `unmigrated`. This group holds the last five: `estimate-ask-finds`, `estimate-index-check-merges`, `estimate-cleanup-moves`, `estimate-raw-archive` and `estimate-tests-clock-pinned`. Here is where it goes wrong: `estimate-cleanup-moves` holds a head paragraph and three blocks. One block moves the old archive folders once. One tells `cleanup.py` to stop writing index files that no longer exist. One gives the page "a `### case 102.2` block, `pending`". A new reading cannot tell those acts from the promise.
The person decided in the first round on this item. The twelve old pages went in three Cases by area: case 498 took rendering and settings, case 499 the end of a session, and this Case takes the rest. Each page gets one Criterion, no page is split, and each live half of a reading stays. This last Case replaces the note of Slice 3g with a note on removing the checks of the old shape once lint counts zero, so Slice 3g stays open (case 202). This Case closes the Frontier line C1. A Criterion that records a one-time act gets a Criterion of the repeating behaviour (case 485). None of the five has `purpose` or `method`, so each `update` sets both, and setting `method` drops `## Context` and `## Method` (case 211). Each Criterion is replaced whole and goes back to `pending`, and its reading waits for a later session (case 428.1). All five rules go from `built` to `draft` until the reading. None of the five lost its Criterion to a tool fault like case 211.3. Their History shows only Criteria that cases 23.1, 33, 35.1, 100.1, 102.2, 105.1, 145.1, 147.2, 147.3, 147.6, 166.4 and 174 wrote on purpose, so nothing is restored.
What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording. The content of the old lines is carried, except for the lines named here. Each line that gives a page a block or sets it `pending` goes out as bookkeeping. In 500.1 two lines go out as a one-time Research question: "whether `@` expands in an agent file" and "the tokens of one dispatch". Block 147.2 quoted the new Render. It becomes the behaviour that Render gives, the Grep of the rules first, and the line "No read of a `*-index.md`" goes out, because the files no longer exist. The name of the fifth answer line, tags/slug, stands in plain text, because a code span with a `/` reads as a path that `given` must name. In 500.2 "The name of the rule does not change" goes out as a bound of an edit, and the head's "comparisons made per category" is now the Grep and its count that the Render names. The Render also leaves Estimates out of the check, and that is kept. In 500.3 the migration of block 102.2 and the removal of the index writer of 147.6 go out as one-time acts, and so does "no index file is written". The History and `log.md` lines are worded as `history` in `guppi/cleanup.py` writes them: the page gets its line, and `log.md` gets the same text with the page's category and slug in front. In 500.4 the `－` line "a date-level unit dated the day of the run is not looked at" is carried by the first `＋` line, and "that gap is `rule-materialize`'s" goes out as a pointer. In 500.5 the old line names `guppi.ledger.run`, but `tests/test_conftest.py` calls `guppi.event.run`. So the line promises a `run()` without `now`, as the test reads it. "`make test` is green on the tree of this session" moves into `method`. The `Makefile` half of the last `－` line goes out as a bound of an edit, and the `test-*` targets stay.
The check also notes that 500.4 shares words with 500.1 on the day's event log, and with 500.3 on the exit codes and the rerun. This is expected. In 500.1 each dispatch of `ask-guppi` is written into the event log. In 500.4 `guppi archive` leaves the event log where it is. 500.3 and 500.4 are two scripts with the same contract for a failed move and a rerun, each promised for its own script and read by its own test file, as cases 33 and 100.1 signed them.
The frame. The kept lines were read against `.claude/agents/ask-guppi.md`, the Render of `rule-index-check`, `guppi/cleanup.py`, `guppi/archive.py`, `tests/conftest.py`, `tests/test_conftest.py` and the frame of the librarian, and none is contradicted but the one line of 500.5 named above. Stdout lines, History lines and headers that hold a `/` stand in plain quotation marks or in words. `estimate-sprint-migration-lint-clean` promises that `unmigrated` is at zero at the close. This Case makes the count zero after the librarian's run and does not change that promise, so it is not touched. `estimate-lint-counts-the-unmigrated` stays true at zero, since it promises no line then. No behaviour changes, so no code, test, Render or hook changes, and no reader keeps an old form. The Case creates no page, so no vault query was run. Not done: the removal of the checks of the old shape, which the new note holds for a later session, and with it the wording of the Criterion of `estimate-sprint-migration-lint-clean` on the counter.

## Problem

The last five Estimates of the old layout still have no `purpose` or `method`, still carry `## Context` and `## Method`, and stack blocks that record migrations, removed index files and one-time questions next to their promise. Lint counts them as `unmigrated`. The note of Slice 3g asks for exactly this recut, and nothing but a Case removes it.

## Given

`estimate-tests-clock-pinned` — the promise, its Criterion replaced whole
**＋** `rule-tests-clock-pinned` — the rule it promises for
**＋** `tests/conftest.py` — the autouse fixture
**＋** `tests/test_conftest.py` — the test of the fixture
**＋** `tests/` — the suite the fixture covers
**＋** `guppi/` — the modules whose clock is pinned
**＋** `Makefile` — the targets `test` and `test-*`

## History

- 2026-09-29 created · raw/2026-09-29/0137/ledger.md#case-500.5
