---
type: decision
case: "491.1"
status: current
update: ["[[estimate-sprint-ticks-the-spec]]"]
origin: raw/2026-09-28/2229/ledger.md#case-491.1
sprint: migration
created: 2026-09-28
tags: [harness, sprint]
---

## Context

Each Estimate page holds one promise, its Criterion. A Criterion should hold only `When:`, the trigger and the input it acts on, and `Then:`, what must hold after. Older Estimates also open with `Given:`, a set of lines that describe the code and the cases as they stood on the day the promise was written. This group holds four such pages. Three belong to `rule-sprint`: the tick of the `guppi sprint` lines of a Spec, the check of `sprint.md`, and the drop of a milestone left empty. The fourth is the tick of the `guppi render` lines of a Spec, on `rule-render-harness`. Their `Given:` repeats what `guppi sprint` and `guppi render` do on exit, which yaml counts as applied whole, and which tests fix the behaviour. Two of the pages also carry `－` lines on the bounds of an old edit: "`make lint` writes nothing to the tree" and "Nothing is added at `SessionStart` or in `/hi`".
The person decided in the first round on this item. The item goes in seven Cases by area, one group per Case. The lines on the bounds of an edit go out. A lost ratified text is restored, and a page with no `purpose` gets one. This group is the fourth, after cases 488, 489 and 490. None of these pages lost its Criterion to a tool fault like case 211.3. Their History shows only `created`, readings, and the Criteria that cases 235 and 250.1 replaced on purpose, so nothing is restored and no commit needs to be read. All four pages already have `purpose` and `method`, so no field is set but `status`. Each Criterion is replaced whole and goes back to `pending`. Its reading waits for a later session (case 428.1). The note of Slice 3g stays as it is until the last group.
What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording, and the paths now read `vault/raw/` in place of `raw/`. The content of the old lines is carried, except for the lines named here. Each `Given:` goes out. The definition of a yaml applied whole moves from `Given:` into `Then:` in 491.1 and 491.4. "The script writes the file and exits 0, or writes nothing and exits 1" goes out, because the tick promises only what follows a run that wrote and exited 0, and "a run that exits 1 ticks nothing" stays. In 491.2 the lines "`make lint` writes nothing to the tree" and "Nothing is added at `SessionStart` or in `/hi`" go out as bounds of an edit, and "the file is written in neither case" stays. The finding line of 491.2 names the file outside its code span, because a span with a `/` reads as a path that `given` must name. `make lint` still runs `sprint --check` after `render --check` and before `guppi lint`, with `backlog --check` and `glossary --check` between, so that line stays. In 491.3 the definition of the current milestone and the rule for a note move from `Given:` into `Then:`, and "rule 229.3 does not change for it", a bound of an edit, becomes "stays".
The check also notes that the `then` lines of 491.1 and 491.4 share most of their words. This is expected. Both `guppi sprint` and `guppi render` call the one helper `tick_command_lines` of `guppi/render.py`, each with its own command. Each script has its own promise and its own test file, and case 488.3 recut the third caller, `guppi glossary`, in the same form. The lines differ where the scripts differ: `guppi render` also has `--sync`, which ticks nothing.
The frame. Each kept line was read against `guppi/sprint.py`, `tick_command_lines` and `applied_whole` of `guppi/render.py`, `is_carried_over` of `guppi/materialize.py`, the move after the cascade in `guppi/generate.py`, and the target `lint` of the `Makefile`. None is contradicted. No behaviour changes, so no code, test, Render or hook changes, and no reader keeps an old form. The other Estimates of `rule-sprint` and `rule-render-harness` either have no `Given:` or speak of other steps, so they are not touched. `estimate-render-harness-reproduces` and `estimate-render-sync-reports` are old-layout pages and belong to item C2. The Case creates no page, so no vault query was run. Not done: the other three groups (13 pages).

## Problem

The four Estimates of the Spec tickers and the sprint still open with a `Given:` that repeats the code of their day, and two of them carry lines on the bounds of an old edit. So their promises mix the trigger and the result with a frame that goes stale.

## Given

`estimate-sprint-ticks-the-spec` — the promise, its Criterion replaced whole
**＋** `rule-sprint` — the rule it promises for
**＋** `guppi/sprint.py` — `run`, which calls the tick after it writes the file
**＋** `guppi/render.py` — `tick_command_lines` and `applied_whole`, the one tick of the command lines
**＋** `guppi/materialize.py` — `units_with` and `is_carried_over`, the units walked and the ones passed by
**＋** `vault/wiki/sprint.md` — the file whose write comes before the tick
**＋** `vault/raw/` — the units, each with its `spec.md` and `materialize.yaml`
**＋** `tests/test_sprint.py` — the tests the reading runs

## History

- 2026-09-29 created · raw/2026-09-28/2229/ledger.md#case-491.1
