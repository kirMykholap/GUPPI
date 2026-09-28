## Case 491 — Slice 3g: the Estimates of the Spec tickers and the sprint recut to `When:` and `Then:`

> **context:**
> Each Estimate page holds one promise, its Criterion. A Criterion should hold only `When:`, the trigger and the input it acts on, and `Then:`, what must hold after. Older Estimates also open with `Given:`, a set of lines that describe the code and the cases as they stood on the day the promise was written. This group holds four such pages. Three belong to `rule-sprint`: the tick of the `guppi sprint` lines of a Spec, the check of `sprint.md`, and the drop of a milestone left empty. The fourth is the tick of the `guppi render` lines of a Spec, on `rule-render-harness`. Their `Given:` repeats what `guppi sprint` and `guppi render` do on exit, which yaml counts as applied whole, and which tests fix the behaviour. Two of the pages also carry `－` lines on the bounds of an old edit: "`make lint` writes nothing to the tree" and "Nothing is added at `SessionStart` or in `/hi`".
> The person decided in the first round on this item. The item goes in seven Cases by area, one group per Case. The lines on the bounds of an edit go out. A lost ratified text is restored, and a page with no `purpose` gets one. This group is the fourth, after cases 488, 489 and 490. None of these pages lost its Criterion to a tool fault like case 211.3. Their History shows only `created`, readings, and the Criteria that cases 235 and 250.1 replaced on purpose, so nothing is restored and no commit needs to be read. All four pages already have `purpose` and `method`, so no field is set but `status`. Each Criterion is replaced whole and goes back to `pending`. Its reading waits for a later session (case 428.1). The note of Slice 3g stays as it is until the last group.
> What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording, and the paths now read `vault/raw/` in place of `raw/`. The content of the old lines is carried, except for the lines named here. Each `Given:` goes out. The definition of a yaml applied whole moves from `Given:` into `Then:` in 491.1 and 491.4. "The script writes the file and exits 0, or writes nothing and exits 1" goes out, because the tick promises only what follows a run that wrote and exited 0, and "a run that exits 1 ticks nothing" stays. In 491.2 the lines "`make lint` writes nothing to the tree" and "Nothing is added at `SessionStart` or in `/hi`" go out as bounds of an edit, and "the file is written in neither case" stays. The finding line of 491.2 names the file outside its code span, because a span with a `/` reads as a path that `given` must name. `make lint` still runs `sprint --check` after `render --check` and before `guppi lint`, with `backlog --check` and `glossary --check` between, so that line stays. In 491.3 the definition of the current milestone and the rule for a note move from `Given:` into `Then:`, and "rule 229.3 does not change for it", a bound of an edit, becomes "stays".
> The check also notes that the `then` lines of 491.1 and 491.4 share most of their words. This is expected. Both `guppi sprint` and `guppi render` call the one helper `tick_command_lines` of `guppi/render.py`, each with its own command. Each script has its own promise and its own test file, and case 488.3 recut the third caller, `guppi glossary`, in the same form. The lines differ where the scripts differ: `guppi render` also has `--sync`, which ticks nothing.
> The frame. Each kept line was read against `guppi/sprint.py`, `tick_command_lines` and `applied_whole` of `guppi/render.py`, `is_carried_over` of `guppi/materialize.py`, the move after the cascade in `guppi/generate.py`, and the target `lint` of the `Makefile`. None is contradicted. No behaviour changes, so no code, test, Render or hook changes, and no reader keeps an old form. The other Estimates of `rule-sprint` and `rule-render-harness` either have no `Given:` or speak of other steps, so they are not touched. `estimate-render-harness-reproduces` and `estimate-render-sync-reports` are old-layout pages and belong to item C2. The Case creates no page, so no vault query was run. Not done: the other three groups (13 pages).

> **problem:**
> The four Estimates of the Spec tickers and the sprint still open with a `Given:` that repeats the code of their day, and two of them carry lines on the bounds of an old edit. So their promises mix the trigger and the result with a frame that goes stale.

> **recommend:**
> Replace each Criterion whole with only `When:` and `Then:`. Move the behaviour stated in `Given:` into `Then:`, and drop the bounds lines and the repeats of what another promise holds. Keeping `Given:` as a comment on the page was rejected, because the schema allows only `When:` and `Then:` in a Criterion.

### Case 491.1 — The `guppi sprint` lines of an applied Spec ticked

> **given:**
> `estimate-sprint-ticks-the-spec` — the promise, its Criterion replaced whole
> **＋** `rule-sprint` — the rule it promises for
> **＋** `guppi/sprint.py` — `run`, which calls the tick after it writes the file
> **＋** `guppi/render.py` — `tick_command_lines` and `applied_whole`, the one tick of the command lines
> **＋** `guppi/materialize.py` — `units_with` and `is_carried_over`, the units walked and the ones passed by
> **＋** `vault/wiki/sprint.md` — the file whose write comes before the tick
> **＋** `vault/raw/` — the units, each with its `spec.md` and `materialize.yaml`
> **＋** `tests/test_sprint.py` — the tests the reading runs

> **when:**
> `guppi sprint` without a flag wrote `vault/wiki/sprint.md` and exits 0, and reads the units under `vault/raw/` that have a `materialize.yaml`.

> **then:**
> In the `spec.md` of every unit whose yaml is applied whole, every unticked task line that opens with a code span holding `guppi sprint` becomes `- [x]`. A yaml is applied whole when each entry carries `applied` or `superseded_by` and none carries `failed`. Nothing else in the file changes.
> **－** A line where `guppi sprint` sits in a later code span, such as a `read` line or a description, is not ticked.
> **－** `--check` ticks nothing, and a run that exits 1 ticks nothing.
> **－** A unit without a yaml, with an entry not applied, with a `failed` entry, or marked by `carry.md`, is not touched.

> **tasks:**
> - [ ] update `estimate-sprint-ticks-the-spec`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given out, the yaml applied whole stated (case 491.1)`
> - [ ] read `estimate-sprint-ticks-the-spec` — `pytest tests/test_sprint.py`, then by hand on the `spec.md` of a later session after its librarian's run

> **ratification:**
> ```
> - decision[case 491.1][update][estimate-sprint-ticks-the-spec]{ref:estimate-sprint-ticks-the-spec}
> ```

### Case 491.2 — The check of the sprint file

> **given:**
> `estimate-sprint-checks-the-file` — the promise, its Criterion replaced whole
> **＋** `rule-sprint` — the rule it promises for
> **＋** `guppi/sprint.py` — `run` with `--check`, which renders in memory and compares
> **＋** `vault/wiki/sprint.md` — the file compared
> **＋** `entity-sprint-<id>` — the sprint page the file is rendered from
> **＋** `Makefile` — the target `lint`, which runs the check
> **＋** `tests/test_sprint.py` — the tests the reading runs

> **when:**
> Someone runs `uv run guppi sprint --check`, by hand or through the target `lint` of the `Makefile`, and it renders the file from the sprint page in memory.

> **then:**
> When `vault/wiki/sprint.md` differs from the render of the page, stdout holds one line `sprint: <file> differs from entity-sprint-<id>`, the file named by its path from the project root, and the check exits 1. When the file equals the render, the check exits 0 with no output. The file is written in neither case.
> **＋** The target `lint` of the `Makefile` runs it after `render --check` and before `guppi lint`.
> **－** A render error, such as no sprint page, two sprint pages or a slug with no page, is one line on stderr and exit 1, as with `guppi sprint`.

> **tasks:**
> - [ ] update `estimate-sprint-checks-the-file`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given and the bounds lines out (case 491.2)`
> - [ ] read `estimate-sprint-checks-the-file` — `pytest tests/test_sprint.py`, then `make lint` after a later librarian's run

> **ratification:**
> ```
> - decision[case 491.2][update][estimate-sprint-checks-the-file]{ref:estimate-sprint-checks-the-file}
> ```

### Case 491.3 — A milestone left empty by the move leaves the Milestones

> **given:**
> `estimate-sprint-drops-an-emptied-milestone` — the promise, its Criterion replaced whole
> **＋** `rule-sprint` — the rule it promises for
> **＋** `guppi/generate.py` — the move of an item after the cascade, and the drop of its milestone
> **＋** `guppi/sprint.py` — `milestone_blocks` and `item_slugs`, the milestones, items and notes; the current milestone
> **＋** `entity-sprint-<id>` — the sprint page: its `## Milestones`, `## Backlog`, `## Closed` and History
> **＋** `tests/test_generate.py` — the tests the reading runs

> **when:**
> `guppi generate` moves, after the cascade, the last item line out of a milestone of the sprint page into its `## Backlog`.

> **then:**
> The heading `### <name>` of that milestone leaves `## Milestones`. The next milestone with an item not done, or with no item, becomes the current one.
> **＋** The History of the sprint page gets the line `milestone <name> left the Milestones: its items moved to the Backlog · generate`, and stdout gets one line.
> **－** A milestone with no item before the run stays.
> **－** A milestone where a note is left stays. A note is a line that names no `[[slug]]` before its first ` — `, and it is never moved.
> **－** Nothing is written to `## Closed`: nothing of that milestone was built.

> **tasks:**
> - [ ] update `estimate-sprint-drops-an-emptied-milestone`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given out, the current milestone and the note stated (case 491.3)`
> - [ ] read `estimate-sprint-drops-an-emptied-milestone` — `pytest tests/test_generate.py`, the tests of the move

> **ratification:**
> ```
> - decision[case 491.3][update][estimate-sprint-drops-an-emptied-milestone]{ref:estimate-sprint-drops-an-emptied-milestone}
> ```

### Case 491.4 — The `guppi render` lines of an applied Spec ticked

> **given:**
> `estimate-render-harness-ticks-the-spec` — the promise, its Criterion replaced whole
> **＋** `rule-render-harness` — the rule it promises for
> **＋** `guppi/render.py` — `run`, `tick_command_lines` and `applied_whole`
> **＋** `guppi/materialize.py` — `units_with` and `is_carried_over`, the units walked and the ones passed by
> **＋** `vault/raw/` — the units, each with its `spec.md` and `materialize.yaml`
> **＋** `tests/test_render.py` — the tests the reading runs

> **when:**
> `guppi render` without a flag wrote the governed files and exits 0, and reads the units under `vault/raw/` that have a `materialize.yaml`.

> **then:**
> In the `spec.md` of every unit whose yaml is applied whole, every unticked task line whose text opens with a code span holding `guppi render` becomes `- [x]`. A yaml is applied whole when each entry carries `applied` or `superseded_by` and none carries `failed`, as `guppi archive` counts it. Nothing else in the file changes.
> **－** A line where `guppi render` sits in a later code span, such as a `read` line or a line that names the command in its description, is not ticked.
> **－** `--check` and `--sync` tick nothing, and a run that exits 1 ticks nothing.
> **－** A unit without a yaml, with an entry that carries neither `applied` nor `superseded_by`, with a `failed` entry, or marked by `carry.md`, is not touched.

> **tasks:**
> - [ ] update `estimate-render-harness-ticks-the-spec`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given out, the yaml applied whole stated (case 491.4)`
> - [ ] read `estimate-render-harness-ticks-the-spec` — `pytest tests/test_render.py`, then by hand on the `spec.md` of a later session after its librarian's run

> **ratification:**
> ```
> - decision[case 491.4][update][estimate-render-harness-ticks-the-spec]{ref:estimate-render-harness-ticks-the-spec}
> ```

### Case 491.5 — The sprint page records the group of the Spec tickers and the sprint

> **given:**
> `entity-sprint-migration` — the sprint page; its Slice 3g holds the note on every other Estimate
> **＋** `vault/wiki/sprint.md` — the render of the sprint page
> **＋** `/hi` — builds the Frontier from `vault/wiki/sprint.md`
> **＋** `rule-sprint` — a rule whose Estimates this Case recuts
> **＋** `rule-render-harness` — a rule whose Estimate this Case recuts

> **when:**
> The librarian's run applies the `update` of `entity-sprint-migration`.

> **then:**
> The History of `entity-sprint-migration` says that the Estimates of `rule-sprint` and the Spec tick of `rule-render-harness` are recut.

> **tasks:**
> - [ ] update `entity-sprint-migration`
>   - change: `Slice 3g: the Estimates of rule-sprint and the Spec tick of rule-render-harness recut to When and Then; the note on every other Estimate stands (case 491)`

> **ratification:**
> ```
> - decision[case 491.5][update][entity-sprint-migration]{ref:entity-sprint-migration}
> ```
