## Case 488 — Slice 3g: the Estimates of the glossary and `entity-guppi` recut to `When:` and `Then:`

> **context:**
> Each Estimate page holds one promise, its Criterion. A Criterion should hold only `When:`, which is the trigger and the input it acts on, and `Then:`, which is what must hold after. The older Estimates also open with `Given:`, a set of lines that describe the code, the tests or the history as they stood on the day the promise was written. The five Estimates of this group were all written by one parent Case (306), and four of them carry the same `Given:` text, copied from that parent. It speaks of `rule-sprint`, of MOCs and Leaves, and of superseded Cases, and none of it bears on the promise. Two of the five also promise the wrong thing. `estimate-guppi-tests-green` has the `purpose` "make test is green on the branch", but its `Then:` describes the one-time build of `entity-guppi`. `estimate-glossary-terms-defined` describes the one-time build of the glossary table, "a table of 49 rows", and the row splits of that day.
> The person decided in one round. Slice 3g's item on the `Given:` pages goes in seven Cases by area, one group per Case, and this session takes one group now. This Case takes the first group, the glossary and `entity-guppi`, with one sub-case per Estimate. A Criterion that records a one-time act gets a new Criterion that states the repeating behaviour its name, its `purpose` and the code give today (case 485). The done-conditions of the sprint are recut like the rest in their own group. `estimate-end-of-work-order` goes to the old-layout item. A page with no `purpose` gets one in the same change. All five pages of this group already have `purpose` and `method`, so no field is set but `status`. Each Criterion is replaced whole and goes back to `pending`. Its reading waits for a later session (case 428.1). The note of Slice 3g stays as it is until the last group (cases 484.7, 485.6).
> What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording. The content of the old lines is carried, except for the lines named here. Each `Given:` goes out whole. The input moves into `When:`. In 488.1 that is the `## Terms` table and step 6 of the librarian's frame. In 488.3 it is the units under `vault/raw/` with a `materialize.yaml`. 488.1 drops "`index.md` is not read", because the file no longer exists. It keeps the refusals of the old text and adds three that `guppi/glossary.py` and `tests/test_glossary.py` already hold: a `where` that is no `[[slug]]`, no `## Terms` section, and no single live `entity-glossary`. 488.2 drops "after `sprint --check`". The `Makefile` runs `backlog --check` between the two now, and the order is not the promise. It adds that a missing file differs, because `run` compares it as `None`. The finding line of 488.2 names the file outside its code span, because a span with a `/` reads as a path that `given` must name. 488.3 keeps the form of the line in `vault/wiki/case-schema.md` ("a glossary line `- [ ] `uv run guppi glossary``") and the two `－` lines of the old text, and it names the unit that is not applied whole, as `tick_command_lines` of `guppi/render.py` reads it. 488.4 drops the build of the table, its 49 rows and the two rows that split. It also drops the line on how a term enters or leaves, which the Purpose of `entity-glossary` keeps. It keeps the purpose, a live page in each `where` that defines its term and no term twice, and the terms the Purpose names as not rows. 488.5 drops the whole build of `entity-guppi`: its kind, its `children`, `code_ref`, the `parent` of `entity-sprint`, the `applies_to` of `rule-harness`, and the phase MOCs without `applies_to`. The line that the cascade writes `rules` is promised by `estimate-generate-writes-rules-from-applies-to`. 488.5 keeps the one line of its purpose, `make test` with no failed test.
> The check of the answer also notes that the `then` lines of 488.4 share words with 488.1. This is expected. 488.1 promises that the script refuses a table with a dead `where` or a term twice and writes nothing. 488.4 promises the state of the table itself, read at each librarian's run, including the judgment by hand that the page defines the term. No script makes that judgment.
> The frame. No behaviour changes, so no code, test, Render or hook changes, and no reader keeps an old form. Each kept line was read against `guppi/glossary.py`, `tick_command_lines` and `applied_whole` of `guppi/render.py`, the `Makefile`, step 6 of `.claude/agents/librarian-guppi.md` and the table of `entity-glossary`. None of them is contradicted. The sentence of `rule-estimates-schema` that an older page carries its `Given:` "until the one pass of its migration" stays true while other groups remain. The Purpose of `rule-glossary` says `make lint` runs the check "after `sprint --check`". That is still true, since it runs later in the same target. `rule-glossary`, `entity-glossary` and `entity-guppi` have no other Estimates, so none is left alone. `estimate-sprint-ticks-the-spec` and `estimate-render-harness-ticks-the-spec` use the same tick helper and belong to the group of the tickers. 488.6 gives `entity-sprint-migration` an `update` with only `change`, because pre-spec asks for one under a Case that closes a `sprint` line. The Case creates no page, so no vault query was run. Not done: the other six groups (31 pages), and `estimate-end-of-work-order` with the old-layout item C2.

> **problem:**
> The five Estimates of the glossary and `entity-guppi` still open with a `Given:` copied from another Case. Two of them promise a build that happened once and not the behaviour their name and `purpose` state. So a reading of them checks a state of the code that goes stale, or checks nothing that can happen again.

> **recommend:**
> Replace each Criterion whole with only `When:` and `Then:`, taken from the code as it runs today, and give the two one-time Criteria the promise of their `purpose`. Archiving those two was rejected, because their `purpose` names a behaviour that still needs a check.

### Case 488.1 — The glossary written from the table of terms

> **given:**
> `estimate-glossary-renders-the-terms` — the promise, its Criterion replaced whole
> **＋** `rule-glossary` — the rule it promises for
> **＋** `entity-glossary` — the page whose `## Terms` table is the source
> **＋** `guppi/glossary.py` — `render`, `rows` and `group_of`, which write the file or refuse
> **＋** `vault/wiki/glossary.md` — the file written
> **＋** `.claude/agents/librarian-guppi.md` — step 6 of the librarian's frame, which runs the script
> **＋** `tests/test_glossary.py` — the tests the reading runs

> **when:**
> `uv run guppi glossary` runs without a flag, from step 6 of the librarian's frame in `.claude/agents/librarian-guppi.md` or by hand, and reads the `## Terms` table of `entity-glossary`.

> **then:**
> `vault/wiki/glossary.md` is written and the run exits 0. The file holds `# Glossary`, then the line "Written by `guppi glossary` from the `## Terms` of `entity-glossary`; a term changes by an `update` of that page", then one group `## [[<moc>]]` for each parent MOC of the pages in `where`, in the order of first appearance in the table. Each group holds the table `| term | meaning | where |` with its rows in the order of the table.
> **＋** A page in `where` that has no `parent`, such as a root MOC or a placeholder not yet placed, is its own group.
> **＋** A `where` with no live page, a `where` that is no `[[slug]]`, a row that is not three cells, a term twice, no `## Terms` section, or no single live `entity-glossary` gives one line on stderr and exit 1, and the file is not written.
> **＋** The librarian's frame takes each line on stderr of the run as a flag.
> **－** The file holds no line that the table does not give, apart from the heading and the source line.

> **tasks:**
> - [ ] update `estimate-glossary-renders-the-terms`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given and the index.md line out (case 488.1)`
> - [ ] read `estimate-glossary-renders-the-terms` — `pytest tests/test_glossary.py`, then by hand on the `vault/wiki/glossary.md` of a later librarian's run

> **ratification:**
> ```
> - decision[case 488.1][update][estimate-glossary-renders-the-terms]{ref:estimate-glossary-renders-the-terms}
> ```

### Case 488.2 — The check of the glossary file

> **given:**
> `estimate-glossary-checks-the-file` — the promise, its Criterion replaced whole
> **＋** `rule-glossary` — the rule it promises for
> **＋** `entity-glossary` — the page the file is rendered from
> **＋** `guppi/glossary.py` — `run` with `--check`, which renders in memory and compares
> **＋** `vault/wiki/glossary.md` — the file compared
> **＋** `Makefile` — the target `lint`, which runs the check
> **＋** `tests/test_glossary.py` — the tests the reading runs

> **when:**
> `uv run guppi glossary --check` runs, as the target `lint` of the `Makefile` runs it, and renders the file from `entity-glossary` in memory.

> **then:**
> When `vault/wiki/glossary.md` differs from the render or is missing, stdout holds one line `glossary: <file> differs from entity-glossary`, the file named by its path from the project root, and the check exits 1.
> **＋** When the file equals the render, the check exits 0 with no output.
> **－** The check writes no file and ticks no line of a Spec.

> **tasks:**
> - [ ] update `estimate-glossary-checks-the-file`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given and the order in make lint out (case 488.2)`
> - [ ] read `estimate-glossary-checks-the-file` — `pytest tests/test_glossary.py`, then `make lint` after a later librarian's run

> **ratification:**
> ```
> - decision[case 488.2][update][estimate-glossary-checks-the-file]{ref:estimate-glossary-checks-the-file}
> ```

### Case 488.3 — The glossary lines of an applied Spec ticked

> **given:**
> `estimate-glossary-ticks-the-spec` — the promise, its Criterion replaced whole
> **＋** `rule-glossary` — the rule it promises for
> **＋** `guppi/glossary.py` — `run`, which calls the tick after it writes the file
> **＋** `guppi/render.py` — `tick_command_lines` and `applied_whole`, the one tick of the command lines
> **＋** `vault/wiki/glossary.md` — the file whose write comes before the tick
> **＋** `vault/raw/` — the units, each with its `spec.md` and `materialize.yaml`
> **＋** `vault/wiki/case-schema.md` — the form of a glossary line of `tasks`
> **＋** `tests/test_glossary.py` — the tests the reading runs

> **when:**
> `uv run guppi glossary` without a flag wrote `vault/wiki/glossary.md` and exits 0, and reads the units under `vault/raw/` that have a `materialize.yaml`.

> **then:**
> In the `spec.md` of every unit whose yaml is applied whole, every unticked task line that opens with a code span holding `guppi glossary` becomes `- [x]`. A yaml is applied whole when each entry carries `applied` or `superseded_by` and none carries `failed`. Nothing else in the file changes.
> **＋** The form of the line in `vault/wiki/case-schema.md` is `` - [ ] `uv run guppi glossary` ``, the command in the first code span.
> **－** A line that names `guppi glossary` only in a later code span, such as a `read` line, is not ticked.
> **－** `--check` ticks nothing, and a run that exits 1 ticks nothing.
> **－** A unit whose yaml is not applied whole is not touched.

> **tasks:**
> - [ ] update `estimate-glossary-ticks-the-spec`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given out (case 488.3)`
> - [ ] read `estimate-glossary-ticks-the-spec` — `pytest tests/test_glossary.py`, then by hand on the `spec.md` of a later session after its librarian's run

> **ratification:**
> ```
> - decision[case 488.3][update][estimate-glossary-ticks-the-spec]{ref:estimate-glossary-ticks-the-spec}
> ```

### Case 488.4 — Each term names a live page that defines it

> **given:**
> `estimate-glossary-terms-defined` — the promise, its Criterion replaced whole
> **＋** `entity-glossary` — the page it promises for; its `## Terms` table and its Purpose
> **＋** `guppi/glossary.py` — `rows`, which reads the table at the librarian's run
> **＋** `guppi/lint.py` — the `ref` finding on a link that names no page

> **when:**
> `uv run guppi glossary` reads the `## Terms` table of `entity-glossary` at the librarian's run, and `guppi lint` and a reader read the same table.

> **then:**
> Each row names in `where` a `[[slug]]` of a live page, and that page defines the term of the row.
> **＋** No term stands in two rows.
> **－** The terms that the Purpose of `entity-glossary` names as not rows, C4 model, Delegate and the retired terms, stand in no row.

> **tasks:**
> - [ ] update `estimate-glossary-terms-defined`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the one-time build of the table out, the purpose kept as When and Then (case 488.4)`
> - [ ] read `estimate-glossary-terms-defined` — by hand on the table after a later librarian's run, and `make lint` with no `ref` finding on `entity-glossary`

> **ratification:**
> ```
> - decision[case 488.4][update][estimate-glossary-terms-defined]{ref:estimate-glossary-terms-defined}
> ```

### Case 488.5 — The suite of the harness green on the branch

> **given:**
> `estimate-guppi-tests-green` — the promise, its Criterion replaced whole
> **＋** `entity-guppi` — the MOC it promises for
> **＋** `Makefile` — the target `test`, which runs the suite
> **＋** `tests/` — the suite of the harness

> **when:**
> `make test` runs `uv run pytest -q` over `tests/` on the working branch, after a Work Mode.

> **then:**
> pytest reports no failed test and no error, and `make test` exits 0.
> **－** A skipped test is not a failure.

> **tasks:**
> - [ ] update `estimate-guppi-tests-green`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the one-time build of entity-guppi out, the purpose kept as When and Then (case 488.5)`
> - [ ] read `estimate-guppi-tests-green` — `make test` after the Work Mode of a later session

> **ratification:**
> ```
> - decision[case 488.5][update][estimate-guppi-tests-green]{ref:estimate-guppi-tests-green}
> ```

### Case 488.6 — The sprint page records the group of the glossary and `entity-guppi`

> **given:**
> `entity-sprint-migration` — the sprint page; its Slice 3g holds the note on every other Estimate
> **＋** `vault/wiki/sprint.md` — the render of the sprint page
> **＋** `/hi` — builds the Frontier from `vault/wiki/sprint.md`
> **＋** `rule-glossary` — a rule whose Estimates this Case recuts
> **＋** `entity-glossary` — an entity whose Estimate this Case recuts
> **＋** `entity-guppi` — an entity whose Estimate this Case recuts

> **when:**
> The librarian's run applies the `update` of `entity-sprint-migration`.

> **then:**
> The History of `entity-sprint-migration` says that the Estimates of `rule-glossary`, `entity-glossary` and `entity-guppi` are recut.

> **tasks:**
> - [ ] update `entity-sprint-migration`
>   - change: `Slice 3g: the Estimates of rule-glossary, entity-glossary and entity-guppi recut to When and Then; the note on every other Estimate stands (case 488)`

> **ratification:**
> ```
> - decision[case 488.6][update][entity-sprint-migration]{ref:entity-sprint-migration}
> ```
