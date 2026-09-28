## Case 484 — Slice 3g: the Estimates of `rule-prespec` recut to `When:` and `Then:`

> **context:**
> Each Estimate page holds one promise of a rule, its Criterion. Since case 378.2 a Criterion has only `When:`, the trigger and the input it acts on, and `Then:`, what must hold after. The frame of a Case stays in the Case and on its Decision page. Older Estimates still open with `Given:`: lines that describe the code, the tests or the history as they stood when the promise was written. Those lines go stale when the code moves on. For example, `estimate-prespec-simulates-the-pairs` says in `Given:` that pre-spec "has no check of an anchor at all", and that check is now the promise itself. Some of these pages also have `－` lines on what one edit left alone, such as "Nothing else in pre-spec changes". Those lines state no behaviour. A search on 2026-09-28 found `Given:` in the Criterion of 43 Estimate pages, spread over about 25 target rules.
> The person decided in one round. This Case takes one group, the six Estimates of `rule-prespec` that hold `Given:`, with one sub-case for each Estimate (case 395, and the eleven of case 396 onward). The one note of Slice 3g stays as it is until the last group. Each Criterion is replaced whole and goes back to `pending`. Its reading is a pytest run and waits for a later session (case 428.1). A `－` line on the bounds of an edit goes out with its group, and a `－` line that states real behaviour of the check stays. No lint count of the `Given:` pages is added.
> What each new Criterion keeps and drops. The check of the answer noted each old line that the new Criterion does not carry word for word. The `Then:` lines are now carried word for word, except for the changes below, each made on purpose.
> The `Given:` lines go out: the state of the code ("has no check of an anchor at all", "`check_form` already reads"), what `materialize` and `generate` do, the cases each check stands on, the lines on `tests/test_prespec.py` (the file is in `given` and in `method`), "the conditions of the parent", and the line that `rule-prespec` renders the skill.
> The exit code of the command ("exit 1 on any") goes out of 484.1 and 484.5. `estimate-prespec-checks-the-plan` promises it for every finding ("Each finding is one line on stdout; exit 1 on any finding, 0 on none"), so a second copy would sign one promise twice.
> A `Given:` line that states behaviour of this check moves into `Then:`. These are the form the tickers match (484.1), and the rule that a `create` reads `enforcement` from the item and an `update` from the page (484.4). `enforcement_of` in `guppi/prespec.py` reads no `render_mode`, so that word goes out.
> The input moves into `When:`: the `tasks` block (484.1), the record lines of the window and a line with `{supersedes:case N}` (484.2), the items of the `then` blocks (484.3, 484.4), and the pairs and the live pages (484.6). The `When:` of 484.5 is kept word for word.
> Two finding texts are split. The old ones hold a code span with a `/`: the markers `<!-- /slug -->` in 484.4, and "a tests/ file" in 484.3. `frame_name` of `guppi/prespec.py` reads any span with a `/` as a path that `given` must name. So the new lines name the markers, and the list of method forms, outside the span of the finding. The finding line of 484.1 splits the same way: the old text nests code spans inside one another, and each span now stands alone.
> These `－` lines go out as bounds of an edit: "Nothing else in pre-spec changes" (on two pages), "`lint` does not change" and "The behaviour of lint does not change". The line in `estimate-prespec-catches-a-superseded-case` on a Frontier line closed by a superseded Case, "a finding as today", also goes out. That behaviour is promised by `estimate-prespec-checks-the-frontier`: "A line closed `case N` is a finding when the plan has no heading of Case N".
> The frame. Each `then` line rests on `guppi/prespec.py`, and was read against it:
> - 484.1: the finding text and `OFF_FORM_LINE` in `check_tasks`.
> - 484.2: `check_lines`, which matches the plan heading by the exact Case id, so a superseded sub-case is found by its own heading alone.
> - 484.3: `check_form`, `NO_FORM`, and `names_a_form` imported from `guppi/lint.py`.
> - 484.4: `check_markers`, which matches the markers of the item's own slug, and `enforcement_of`, which reads `enforcement` from the item on a `create` and from the page on an `update`.
> - 484.5: `check_bare_links` and `plan_prose`.
> - 484.6: `check_pairs`.
> - One exception: the form the tickers match in 484.1 rests on `vault/wiki/case-schema.md`, "the command in the first code span is what the ticker matches (case 235)".
> The Render of `rule-prespec` describes each of these findings in its own words, not in the text of the finding line. It does not say that the markers are those of the item's own slug, or where `enforcement` is read from; those stand in the code only. No behaviour changes, so no code, test, Render or hook changes, and no reader keeps an old form. The sentence of `rule-estimates-schema` "a page written before carries its `Given:` until the one pass of its migration" stays true while other groups remain. The other Estimates of `rule-prespec` speak of other findings and are not touched. `estimate-prespec-hook-gates` targets `rule-prespec-hook` and belongs to another group. Pre-spec asks for an `update` of the sprint page under a Case that closes a `sprint` line, so 484.7 gives `entity-sprint-migration` an `update` with only `change`, and its note stands. The Case creates no page, so no vault query was run. Not done: the other 37 pages with `Given:`, the bounds lines on pages outside this group, and the pages with `### case N` blocks (the sibling item C2).

> **problem:**
> The Criteria of six Estimates of `rule-prespec` still open with `Given:`, and some carry `－` lines on the bounds of an old edit. So their promises describe a state of the code that goes stale, and they do not read as the trigger and the result alone.

> **recommend:**
> Replace each Criterion whole with a `When:` that names the command and the input it reads, and a `Then:` that carries the old promise lines word for word where they still hold. Drop the state lines, the bounds lines and the lines another Estimate already promises. Set each page `pending`, to be read by its pytest run in a later session. Rewriting all 43 pages in one Case was rejected: one showing with 43 promises is too many to read and sign.

### Case 484.1 — A render or sprint line off the ticker's form

> **given:**
> `estimate-prespec-catches-a-command-line-off-form` — the promise, its Criterion replaced whole
> **＋** `rule-prespec` — the rule it promises for; its Render describes the finding
> **＋** `.claude/skills/pre-spec/SKILL.md` — the skill `/pre-spec`, rendered from `rule-prespec`, which runs the check
> **＋** `guppi/prespec.py` — `check_tasks` and `OFF_FORM_LINE`, which judge the line
> **＋** `tests/test_prespec.py` — the tests the reading runs

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` reads the `tasks` block of every Case of a plan, as `/pre-spec` runs it on the plan of this Plan Mode.

> **then:**
> A `tasks` line whose text after the box opens with the word `render` or `sprint`, or with `guppi render`, `guppi sprint`, `uv run guppi render` or `uv run guppi sprint` outside a code span, is a finding `case N: render line off form: <line>`.
> **＋** The form the tickers of `render` and `sprint` match is `` - [ ] `uv run guppi render`: … `` and `` - [ ] `uv run guppi sprint` ``, the command in the first code span.
> **－** A line that opens with a code span holding the command is no finding; a `read` line that names the command in a later span is no finding (235).

> **tasks:**
> - [ ] update `estimate-prespec-catches-a-command-line-off-form`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given and the bounds line out (case 484.1)`
> - [ ] read `estimate-prespec-catches-a-command-line-off-form`

> **ratification:**
> ```
> - decision[case 484.1][update][estimate-prespec-catches-a-command-line-off-form]{ref:estimate-prespec-catches-a-command-line-off-form}
> ```

### Case 484.2 — A superseded Case still in the plan

> **given:**
> `estimate-prespec-catches-a-superseded-case` — the promise, its Criterion replaced whole
> **＋** `rule-prespec` — the rule it promises for; its Render describes the finding
> **＋** `guppi/prespec.py` — `check_lines`, which judges the headings and the lines of a superseded Case
> **＋** `guppi/materialize.py` — `parse_line`, which reads the record lines of the window
> **＋** `tests/test_prespec.py` — the tests the reading runs

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` reads a plan and the record lines of the session's window, and a decision line of the window carries `{supersedes:case N}`.

> **then:**
> A `{supersedes:case N}` in the session's window while `## Case N` or `### Case N` still stands in the plan is a finding `case N: superseded by case M, still in the plan`.
> **＋** A decision line of Case N, N superseded by a line of the window, is no finding "no Case N heading" and needs no item in the plan.
> **＋** A superseded sub-case: the one heading `### Case N.M` leaves; the parent with its other sub-cases stays.
> **－** A `{supersedes:case N}` on a Case of an earlier session — a defer taken up — finds no heading N in the plan and is no finding.

> **tasks:**
> - [ ] update `estimate-prespec-catches-a-superseded-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given and the bounds lines out (case 484.2)`
> - [ ] read `estimate-prespec-catches-a-superseded-case`

> **ratification:**
> ```
> - decision[case 484.2][update][estimate-prespec-catches-a-superseded-case]{ref:estimate-prespec-catches-a-superseded-case}
> ```

### Case 484.3 — A method that names no form

> **given:**
> `estimate-prespec-catches-a-method-without-a-form` — the promise, its Criterion replaced whole
> **＋** `rule-prespec` — the rule it promises for; its Render describes the finding
> **＋** `guppi/prespec.py` — `check_form` and `NO_FORM`, which judge the method of an item
> **＋** `guppi/lint.py` — `names_a_form`, the one predicate of the forms
> **＋** `tests/test_prespec.py` — the tests the reading runs

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` reads the items of the plan's `then` blocks before the Spec is approved.

> **then:**
> A `create` of an Estimate, or an `update` carrying `set: {method: …}`, whose `method` names none of the forms lint classifies (a `make <target>`, the word `pytest`, a path under `tests/`, or the words `by hand`) gives one line `case N: <create|update> <slug>: method names no form`, which goes on to name those forms.
> **＋** A `create` of an Estimate with no `method` at all gives the same finding.
> **＋** The predicate is one, lifted out of `guppi/lint.py`; `pre-spec` writes no second one.
> **－** Existence is not checked in the plan: the file under `tests/` is written in Work Mode and lint checks it later.
> **－** The branch of a MOC stays with lint: `pre-spec` does not judge whether the Estimate of a MOC needs a `make` target.

> **tasks:**
> - [ ] update `estimate-prespec-catches-a-method-without-a-form`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given and the bounds line out (case 484.3)`
> - [ ] read `estimate-prespec-catches-a-method-without-a-form`

> **ratification:**
> ```
> - decision[case 484.3][update][estimate-prespec-catches-a-method-without-a-form]{ref:estimate-prespec-catches-a-method-without-a-form}
> ```

### Case 484.4 — A Render not wrapped in its markers

> **given:**
> `estimate-prespec-catches-an-unwrapped-render` — the promise, its Criterion replaced whole
> **＋** `rule-prespec` — the rule it promises for; its Render describes the finding
> **＋** `guppi/prespec.py` — `check_markers` and `enforcement_of`, which judge the text of a Render
> **＋** `<!-- slug -->` and `<!-- /slug -->` — the markers a Render of a page opens and closes with
> **＋** `tests/test_prespec.py` — the tests the reading runs

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` reads the items of the plan's `then` blocks that carry `sections: Render`.

> **then:**
> An item whose target is a page with `enforcement: render`, and whose text does not open with `<!-- slug -->` and close with `<!-- /slug -->` of its own slug, gives one line `case N: <create|update> <slug>: Render is not wrapped in`, followed by the two markers of that slug.
> **＋** In a `create` the `enforcement` of the target is read from the item itself, and in an `update` from the page.
> **＋** The check judges only the text the item itself writes, and does not simulate the Spec in entry order.
> **＋** A target without `enforcement: render` gives no finding.
> **＋** A wrapped text is silent; exit 0 on a clean plan stands.
> **－** The child's marker line in the parent is not checked here: its true value is known only after every item of the Spec is applied.

> **tasks:**
> - [ ] update `estimate-prespec-catches-an-unwrapped-render`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given out (case 484.4)`
> - [ ] read `estimate-prespec-catches-an-unwrapped-render`

> **ratification:**
> ```
> - decision[case 484.4][update][estimate-prespec-catches-an-unwrapped-render]{ref:estimate-prespec-catches-an-unwrapped-render}
> ```

### Case 484.5 — A bare wikilink that names no page

> **given:**
> `estimate-prespec-catches-bare-wikilinks` — the promise, its Criterion replaced whole
> **＋** `rule-prespec` — the rule it promises for; its Render describes the finding
> **＋** `.claude/skills/pre-spec/SKILL.md` — the skill `/pre-spec`, rendered from `rule-prespec`, which runs the check
> **＋** `guppi/prespec.py` — `check_bare_links` and `plan_prose`, which judge the links
> **＋** `vault/wiki/` — the live pages, the archived pages and the hub files a link may name
> **＋** `tests/test_prespec.py` — the tests the reading runs

> **when:**
> The person invokes `/pre-spec`, and `guppi prespec --check <plan> --session <id>` reads the plan file.

> **then:**
> One line `case N: [[slug]] outside a code span names no page` is printed for every `[[slug]]` in the plan file outside a code span — in the blockquotes and in the strings of the `then` blocks — that has no live or archived page.
> **＋** A slug a `create` of the same plan carries, and a hub file of `wiki/` by its stem or its path, are not a finding.
> **＋** One line per slug and Case, however many times it stands.
> **－** A `[[slug]]` inside backticks, and inside a fenced block tagged other than `then`, is not read.

> **tasks:**
> - [ ] update `estimate-prespec-catches-bare-wikilinks`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given and the bounds line out (case 484.5)`
> - [ ] read `estimate-prespec-catches-bare-wikilinks`

> **ratification:**
> ```
> - decision[case 484.5][update][estimate-prespec-catches-bare-wikilinks]{ref:estimate-prespec-catches-bare-wikilinks}
> ```

### Case 484.6 — The pairs of the plan applied in entry order

> **given:**
> `estimate-prespec-simulates-the-pairs` — the promise, its Criterion replaced whole
> **＋** `rule-prespec` — the rule it promises for; its Render describes the finding
> **＋** `guppi/prespec.py` — `check_pairs`, which applies the pairs in memory
> **＋** `tests/test_prespec.py` — the tests the reading runs

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` reads a plan whose Cases carry `replace` or `reword` pairs, and the live pages of the vault, before the Spec is approved.

> **then:**
> The `replace` and `reword` pairs of every Case of the plan are applied in entry order to copies of the pages in memory, whitespace collapsed as `generate` collapses it; nothing is written to disk.
> **＋** An anchor that misses, or hits more than once, gives one line with its Case, the page's slug and the opening of its `old`.
> **＋** The anchor is judged against the page as the Spec leaves it, not as it stands today.
> **－** The meaning of the words in their place is not judged by a machine.

> **tasks:**
> - [ ] update `estimate-prespec-simulates-the-pairs`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given out (case 484.6)`
> - [ ] read `estimate-prespec-simulates-the-pairs`

> **ratification:**
> ```
> - decision[case 484.6][update][estimate-prespec-simulates-the-pairs]{ref:estimate-prespec-simulates-the-pairs}
> ```

### Case 484.7 — The note of Slice 3g stands after the group of `rule-prespec`

> **given:**
> `entity-sprint-migration` — the sprint page; its Slice 3g holds the note on every other Estimate
> **＋** `vault/wiki/sprint.md` — the render of the sprint page
> **＋** `/hi` — builds the Frontier from `vault/wiki/sprint.md`
> **＋** `rule-prespec` — the rule whose Estimates this Case recuts

> **when:**
> The next `/hi` builds the Frontier from `vault/wiki/sprint.md`, drawn from `entity-sprint-migration`.

> **then:**
> Slice 3g still shows the one unticked note on every other Estimate, and the Frontier holds it as a `C` line.
> **＋** The History of `entity-sprint-migration` says that the Estimates of `rule-prespec` are recut.
> **－** The note is not ticked or reworded: it leaves Slice 3g with the Case that recuts the last group.

> **tasks:**
> - [ ] update `entity-sprint-migration`
>   - change: `Slice 3g: the Estimates of rule-prespec recut to When and Then; the note on every other Estimate stands (case 484)`

> **ratification:**
> ```
> - decision[case 484.7][update][entity-sprint-migration]{ref:entity-sprint-migration}
> ```
