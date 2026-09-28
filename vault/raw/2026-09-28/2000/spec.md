<!-- approved 22:11:12 · session 8b77e5ae -->

# Spec — session 2000, 2026-09-28

## Case 482 — the librarian's commit takes guppi.toml

> **context:**
> The `render` step writes each rule-controlled file from its Rule page. The librarian then commits with `git add vault CLAUDE.md .claude`, and `rule-close` forbids any path outside those three. Until case 476.1 every rendered file stood under one of those paths. `guppi.toml`, the settings file rendered from `rule-guppi-config`, is written at the repository root. So the librarian's run of 2026-09-28 wrote it and left it untracked (brief, Flags). A fresh clone then has no `guppi.toml`, and the pre-spec language check reports `guppi.toml: missing` there.
> The person decided in one round. The commit is widened, and the file stays at the root: moving it into `.claude/` would change `guppi/config.py`, its tests and every page that names the file. The command names `guppi.toml` directly. The render does not print a list of the files it wrote: among the `governs` fields of the Rule pages, `guppi.toml` is the only path outside `vault`, `CLAUDE.md` and `.claude`. A later rendered file outside these paths comes through a Case that widens the commit again. The file that is untracked now goes into this session's Work Mode commit, because its content is what the Rule page already renders. The promise also gains a line that no rendered file stays untracked after the commit.
> The frame. The Render of `rule-close` says "never a path outside those three", and the Criterion of `estimate-close-commits` says "No path outside those three". The change makes both false, so the Case changes the Render and replaces the Criterion whole. The old Criterion is in the shape used before case 193: a paragraph cut into short lines, then a block of case 89.2. The check of the answer notes each of its lines as not carried, because the new `when` and `then` rewrite them as whole statements. Their content is carried: a live run, one commit after the Retro commit, `vault/` and the rendered files, the message convention, never `--amend`, and the report with its counts, flags and lint total in twenty lines or fewer. Only "No path outside those three" changes, by the person's decision, to four paths. The update brings the Estimate to the new shape, so it sets `method` and `purpose`, which the page lacks; `rule-estimates-schema` leaves `purpose` out on older pages only until their recut. The docstring of `guppi/render.py` says the librarian commits the rendered files in its own commit (case 89.2). That stays true. The Criterion of `estimate-guppi-config-fills-the-languages` speaks of what the file holds, not of where it is committed, so it is not touched. The decision pages of case 89 quote the old command. They are records and stay as they are.
> The reader of the changed text is the librarian agent, not code. It reads `.claude/agents/librarian-guppi.md` after the next render, and nothing refuses in between, so no old form is kept. The Case needs no `create`, so no vault query was run. Not done: the render does not report the files it wrote, and the file does not move.

> **problem:**
> The librarian's commit takes only `vault`, `CLAUDE.md` and `.claude`, and `render` writes `guppi.toml` at the repository root. So the settings file that the checks read is never committed, and a fresh clone lacks it.

> **given:**
> `rule-close` — the librarian's close; its Render holds the commit command and the ban on other paths
> **＋** `.claude/agents/librarian-guppi.md` — the librarian's text, rendered from `rule-close`
> **＋** `vault/` — the pages the librarian's run writes
> **＋** `guppi.toml` — the settings file, written at the repository root
> **＋** `rule-guppi-config` — governs `guppi.toml`, rendered in full
> **＋** `guppi/render.py` — the renderer that writes the governed files
> **＋** `estimate-close-commits` — the promise on the librarian's commit
> **＋** `rule-estimates-schema` — a recut page carries `method` and `purpose`

> **when:**
> After a live run, the librarian commits at the close, as `.claude/agents/librarian-guppi.md` says.

> **then:**
> `git log` shows one commit after the Retro commit. It takes `vault/`, `CLAUDE.md`, `.claude` and `guppi.toml`: `git add vault CLAUDE.md .claude guppi.toml`.
> **＋** It stays one commit, separate from the session's, with the message `docs(vault): librarian, <date>`, and never `--amend`.
> **＋** After the commit, `git status` shows no file that `guppi/render.py` wrote as untracked, `guppi.toml` included.
> **＋** The report reaches the main agent with the counts, the flags and the lint total, in twenty lines or fewer.
> **－** The commit takes no path outside `vault/`, `CLAUDE.md`, `.claude` and `guppi.toml`.

```then
update:
- slug: rule-close
  replace:
  - old: git add vault CLAUDE.md .claude &&
    new: git add vault CLAUDE.md .claude guppi.toml &&
  - old: never a path outside those three.
    new: never a path outside those four. After the commit, no file the render wrote stands untracked.
  change: the commit takes guppi.toml, the settings file rendered at the root (case 482)
- slug: estimate-close-commits
  set:
    status: pending
    purpose: The librarian's run ends in one separate commit of vault, CLAUDE.md, .claude and guppi.toml, with no rendered file left untracked, and a report of twenty lines or fewer
    method: 'by hand after the next librarian run: git log shows its commit and the paths it touched, git status shows no untracked file the render wrote, and the report is read in the transcript'
  change: the Criterion replaced whole — the commit takes guppi.toml, and no rendered file stays untracked (case 482)
```

```tasks
- [x] update `rule-close`
- [x] update `estimate-close-commits`
- [x] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [x] one-off: this session's Work Mode commit takes `guppi.toml`
- [ ] read `estimate-close-commits` — by hand, after the next librarian run
```

## Case 483 — Retro writes the end of a frontier item only in What is not done

> **context:**
> At `/retro`, the agent writes a report in two parts. The frontier is a numbered list of what still needs an end. The close has three blocks: Ratified, What got done and What is not done. The rule of case 468.1 puts each fact in one part: the frontier holds the text of each item, and What is not done holds each number with its end. The Retro of session 1318 wrote the whole report in one reply. It gave every frontier item its proposed end, and What is not done gave the same ends again. Item 3 read "Result: short defer, Case 481", and What is not done read "3 — defer, Case 481". So `estimate-retro-report-holds-each-fact-once` failed for the second time (L39 of `raw/2026-09-28/1318/ledger.md`). The Render of `rule-retro` never says that a frontier item carries no end. It also asks What is not done for "its ledger line number where it has one", and those lines are not yet written when the report is written. That Retro said so in its own close: "the ledger lines and Case 481 are not written yet".
> This Case changes a page and does not create one, so no vault query was needed. The new Criterion keeps every line of the old one word for word except one. The line on What is not done is replaced on purpose: the end becomes the one the agent proposes, and the ledger line number is dropped. Two lines are added: a frontier item names no end, and the close stands in the same reply as the frontier. The frame holds no contradiction. `rule-handoff` and `estimate-handoff-holds-each-fact-once` rebuild What is not done in words from the items and their ends. They name no ledger line number of the Retro close, so this Case leaves them true. Of the other Estimates of `rule-retro`, `estimate-retro-loads` speaks of readings, and `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` and `estimate-retro-red-in-the-baseline-is-not-charged` speak of red checks. None of the three speaks of the layout of the report, so they are not touched. The person chose: the end only in What is not done, one reply without line numbers, a skeleton of the report in the skill, and the Criterion replaced whole.

> **problem:**
> The Retro report writes the end of each frontier item twice: once on the item and once in What is not done. A Case that ends an item is then named in two parts. The Render allows this because it does not forbid an end on an item. It also asks What is not done for ledger line numbers that do not exist when the report is written.

> **given:**
> `rule-retro` — its Render: the sentences on the frontier and on the close
> **＋** `.claude/skills/retro/SKILL.md` — the skill rendered from `rule-retro`
> **＋** `estimate-retro-report-holds-each-fact-once` — its Criterion replaced whole
> **＋** `uv run guppi tail` — the decision lines and ledger lines the report counts from
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the unticked boxes the frontier sorts
> **＋** `rule-handoff` — rebuilds What is not done from the items and their ends; unchanged

> **when:**
> The person invokes `/retro` in a session where `uv run guppi tail` prints its decision lines and `raw/<date>/<hi HHMM>/spec.md` holds unticked boxes, and the agent writes the frontier and the close.

> **then:**
> The frontier is one numbered list of what needs an end in this Retro: each unticked box that is debt, and what the agent noticed during Work Mode.
> **＋** A `read` line without its line in the Tail, whose slug this session neither creates nor updates, is debt, and so is a box of code, a test, a command or a migration left unticked.
> **＋** Under the list stand two lines, not numbered: the count of the boxes that wait for the librarian, and the slugs of the `read` lines whose slug this session creates or updates, by a decision line of that slug or by an `update` that renames a page to it.
> **－** The frontier names no box that waits for the librarian one by one, and holds no list of the ratifications.
> **－** An item of the frontier is its text alone: it names no end, and no Case, reading or lesson that ends it.
> **＋** The close has three parts. Ratified is one line with the ids of the Cases ratified, from `uv run guppi tail`, this session's folder first, a Case that a `{supersedes:case N}` line names not counted, and no page.
> **＋** The close stands in the same reply as the frontier.
> **＋** What got done holds the commit, the code files and tests changed, the result of `make test` and `make style`, and the readings and lessons written by their ledger line numbers, except a reading or a lesson that is the end of an item of the frontier.
> **＋** What is not done holds each number of the frontier with the end the agent proposes, a short defer with its Case id, and the person approves or changes the ends there; it holds no text of an item, no ledger line number and no repeat of the two lines under the frontier.
> **－** No Case, box, reading or lesson is named in two parts of the report.

````then
update:
- slug: rule-retro
  replace:
  - old: The frontier names no box that waits for the librarian one by one and holds no list of the ratifications (case 468.1).
    new: 'The frontier names no box that waits for the librarian one by one and holds no list of the ratifications (case 468.1). An item of the frontier is its text alone: it names no end, and no Case, reading or lesson that ends it; its end stands only in What is not done (case 483).'
  - old: 'What is not done: each number of the frontier with the end it took, and its ledger line number where it has one, with no text of the item and no repeat of the two lines under the frontier.'
    new: 'What is not done: each number of the frontier with the end you propose, a short defer with its Case id, with no text of the item, no ledger line number and no repeat of the two lines under the frontier. The frontier and the close stand in one reply, and the person approves or changes the ends there; the lines of the ends are written after it (case 483).'
  - old: No Case, box, reading or lesson is named in two parts of the report (case 468.1).
    new: |-
      No Case, box, reading or lesson is named in two parts of the report (case 468.1). The report has this form, its labels in the language of the chat (case 483):

      ```
      1. <text of the item>
      2. <text of the item>

      <N> boxes wait for the librarian.
      Read in a later session: `<slug>`, `<slug>`.

      Ratified: <ids of the Cases>.
      What got done: <commit>; <code files and tests>; make test <result>; make style <result>; <readings and lessons by L<n>>.
      What is not done:
      - 1 — <end>
      - 2 — <end>
      ```
  change: a frontier item is its text alone; its end, with the Case id of a defer, stands only in What is not done, with no ledger line number; the frontier and the close stand in one reply, in the form of a skeleton (case 483)
- slug: estimate-retro-report-holds-each-fact-once
  set:
    status: pending
  change: the Criterion replaced whole — a frontier item names no end; What is not done holds the proposed end of each number with no ledger line number; the frontier and the close stand in one reply (case 483)
````

```tasks
- [x] update `rule-retro`
- [x] update `estimate-retro-report-holds-each-fact-once`
- [x] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
- [ ] read `estimate-retro-report-holds-each-fact-once` — by hand, at the first `/retro` after the render
```

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

```then
update:
- slug: estimate-prespec-catches-a-command-line-off-form
  set:
    status: pending
  change: the Criterion replaced whole — When and Then only, Given and the bounds line out (case 484.1)
```

```tasks
- [x] update `estimate-prespec-catches-a-command-line-off-form`
- [ ] read `estimate-prespec-catches-a-command-line-off-form`
```

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

```then
update:
- slug: estimate-prespec-catches-a-superseded-case
  set:
    status: pending
  change: the Criterion replaced whole — When and Then only, Given and the bounds lines out (case 484.2)
```

```tasks
- [x] update `estimate-prespec-catches-a-superseded-case`
- [ ] read `estimate-prespec-catches-a-superseded-case`
```

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

```then
update:
- slug: estimate-prespec-catches-a-method-without-a-form
  set:
    status: pending
  change: the Criterion replaced whole — When and Then only, Given and the bounds line out (case 484.3)
```

```tasks
- [x] update `estimate-prespec-catches-a-method-without-a-form`
- [ ] read `estimate-prespec-catches-a-method-without-a-form`
```

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

```then
update:
- slug: estimate-prespec-catches-an-unwrapped-render
  set:
    status: pending
  change: the Criterion replaced whole — When and Then only, Given out (case 484.4)
```

```tasks
- [x] update `estimate-prespec-catches-an-unwrapped-render`
- [ ] read `estimate-prespec-catches-an-unwrapped-render`
```

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

```then
update:
- slug: estimate-prespec-catches-bare-wikilinks
  set:
    status: pending
  change: the Criterion replaced whole — When and Then only, Given and the bounds line out (case 484.5)
```

```tasks
- [x] update `estimate-prespec-catches-bare-wikilinks`
- [ ] read `estimate-prespec-catches-bare-wikilinks`
```

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

```then
update:
- slug: estimate-prespec-simulates-the-pairs
  set:
    status: pending
  change: the Criterion replaced whole — When and Then only, Given out (case 484.6)
```

```tasks
- [x] update `estimate-prespec-simulates-the-pairs`
- [ ] read `estimate-prespec-simulates-the-pairs`
```

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

```then
update:
- slug: entity-sprint-migration
  change: 'Slice 3g: the Estimates of rule-prespec recut to When and Then; the note on every other Estimate stands (case 484)'
```

```tasks
- [x] update `entity-sprint-migration`
```

## Case 485 — Slice 3g: the old-layout Estimates of session start and `/hi` recut to one Criterion

> **context:**
> Each Estimate page states one promise about a rule and says how to check it. Pages written before the Estimate model of case 193 still use the old layout. They have a `## Context` section and a `## Method` section instead of a `method` field, no `purpose` field, and often a Criterion built as a stack of dated `### case N` blocks, one added per change. `make lint` counts these pages as `unmigrated` and reports 18 (brief). The stacks mix behaviour that repeats at every run with things done once or with bookkeeping. For example, `estimate-git-context-current` still promises that it "gets a `### case 115` block, `pending`", and `estimate-hi-no-read-calls` that it "gets a `### case 101.3` block". One of the 18, `estimate-close-commits`, is already recut by case 482, so 17 remain, over 16 rules.
> The person decided in two rounds. The 17 pages go in four Cases by area: session start and `/hi`, render and settings, the end of a session and the librarian, and the rest (`estimate-ask-finds`, `estimate-tests-clock-pinned`). This Case takes session start and `/hi`, with one sub-case per Estimate. Each new Criterion keeps the behaviour that the code and the Render show today. It drops lines that record a one-time act or bookkeeping, and this `context` names each dropped line. A line that the code no longer honours, with no decision that removed it, is dropped as well. Each old `## Method` becomes a `method` field that a later session can repeat, and the update that sets it also removes `## Context` and `## Method` (case 211). The pages also get the `purpose` field they lack. A one-time act is a line of a Case's `tasks` list, never an Estimate, and no new status is made for it. The fate of a sprint's done-conditions after the close of the sprint stays with the open item of Slice 5 (case 478.2). The Slice 3g note stays as it is until the last group, as on C1 (484.7). The Case of the last group ticks the note and adds a new note: remove the code that still reads the old layout, in a later session, once lint shows zero (case 202).
> What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording. Their content is carried, except for the lines named here. 485.1 keeps both halves of the promise: without `/hi` the line reaches no ledger and the reply the person sees names the cause, and with `/hi` it reaches the ledger with its time. The ledger path is now `vault/raw/<hi date>/<hi HHMM>/ledger.md`, since case 103.1 moved the ledger into the session folder. The exit code and the stderr line of the refusal are not written into 485.1, because `estimate-ledger-write-lifts` promises them ("Without a `hi`: exit 2 with the reason, the ledger untouched"), and a second copy would sign one promise twice. "Both readings taken end to end" is a way of reading, so it moves into `method`. 485.2 drops the `hi` line of `event_log.md`, because `estimate-event-log-records` promises it. It also drops the marker bookkeeping of block 101.3, and keeps the order of the children as the order of the context, with the output of `guppi tail` as the line `Tail:`. 485.3 drops "a diff on that line is a Frontier item", because `estimate-hi-writes-frontier` promises it ("a hand edit shown by `Render:`"). It also drops the bookkeeping line and the `{supersedes:case 106}` line of block 115. 485.3 keeps "no pull happens later in the session": no code enforces it, but the event log records every Bash call with its command, so a reading can check it. 485.4 and 485.5 drop nothing. They carry every old line as a whole statement, and the Render note in brackets of block 101.2, `partial` and the skill file, becomes its own line. Every kept line was read against `.claude/skills/hi/SKILL.md`, `guppi/tail.py` with `uncovered_lines` and `units_with`, and `guppi/ledger.py`. None of them is contradicted by the code, so the rule on a line the code no longer honours drops nothing here.
> The frame. No behaviour changes, so no Render, code, test or hook changes, and no reader keeps an old form. `rule-estimates-schema` says the older pages lack `purpose` and `method` "until their recut", and that stays true. `estimate-lint-counts-the-unmigrated` promises how lint counts, not how many pages it counts, so it is not touched. The other Estimates of these rules (`estimate-hi-writes-frontier`, `estimate-internal-context-loaded`) are already in the new layout and are not touched. `rule-git-context` and `rule-github-issues` carry `deferred_by` for the pull and `gh` state. No open Frontier line of this session names them, and this Case changes only their Estimates, so their backlog items stand. `rule-session-start` is a MOC, so its Estimate's method names `make test-session-start`. All the children of `rule-skill-hi` are render children of a full MOC, so `by hand` passes lint for `estimate-hi-no-read-calls`. The Case creates no page, so no vault query was run. Not done: the other three groups, the ticking of the Slice 3g note, and the removal of the old-layout code.

> **problem:**
> Five Estimates of session start and `/hi` still use the old layout: sections instead of a `method` field, no `purpose`, and Criteria stacked from dated blocks. Their promises mix repeating behaviour with one-time acts and bookkeeping, lint counts them as `unmigrated`, and a reading cannot tell which lines still hold.

### Case 485.1 — A ledger line only in a session opened with `/hi`

> **given:**
> `estimate-session-start-context` — the promise, its Criterion replaced whole
> **＋** `rule-session-start` — the MOC it promises for
> **＋** `/hi` — the skill that opens a working session
> **＋** `guppi/ledger.py` — the `Stop` hook that writes or refuses the lines
> **＋** `vault/raw/<date>/event_log.md` — the log the hook reads for a `hi` line
> **＋** `vault/raw/<hi date>/<hi HHMM>/ledger.md` — the ledger of the session
> **＋** `tests/test_event.py` — tests the reading runs
> **＋** `tests/test_ledger.py` — tests the reading runs

> **when:**
> The main agent ends a reply that carries a `- decision[...]` line inside a `LEDGER` block, and the `Stop` hook `guppi/ledger.py` looks in `vault/raw/<date>/event_log.md` for a `hi` line of the session.

> **then:**
> In a session opened without `/hi`, the line reaches no ledger of the session, and the reply the person sees names the cause.
> **＋** In a session opened with `/hi`, the line reaches `vault/raw/<hi date>/<hi HHMM>/ledger.md` once, with the time of writing before it.

```then
update:
- slug: estimate-session-start-context
  set:
    status: pending
    purpose: A ledger line reaches the session's ledger only in a session opened with /hi, and a refusal tells the person why
    method: 'make test-session-start; by hand: one session opened without /hi whose reply carries a LEDGER block, and the ledger of the next working session after its first ratification, written into the estimate line'
  change: the Criterion replaced whole — one When and Then, the session folder of the ledger; purpose and method set, Context and Method out (case 485.1)
```

```tasks
- [x] update `estimate-session-start-context`
- [ ] read `estimate-session-start-context` — `make test-session-start`, then by hand in a later session
```

### Case 485.2 — The output of `/hi` present with no read call

> **given:**
> `estimate-hi-no-read-calls` — the promise, its Criterion replaced whole
> **＋** `rule-skill-hi` — the MOC that renders the skill, its children in order
> **＋** `.claude/skills/hi/SKILL.md` — the skill `/hi`
> **＋** `rule-internal-context` — the child that loads the vault files
> **＋** `rule-git-context` — the child of the lines `Pull:`, `Render:`, `Branch:`, `Status:`
> **＋** `rule-github-issues` — the child of the line `Open issues:`
> **＋** `rule-ledger-tail` — the child of the line `Tail:`

> **when:**
> The person invokes `/hi`, and Claude Code expands `.claude/skills/hi/SKILL.md` before the agent's first turn.

> **then:**
> The context of the first turn holds the output of each block of the skill, in the order of the children of `rule-skill-hi`: the text of the files `rule-internal-context` loads, the lines `Pull:`, `Render:`, `Branch:` and `Status:` of `rule-git-context`, the line `Open issues:` of `rule-github-issues`, and the line `Tail:` of `rule-ledger-tail`.
> **－** The agent makes no read-tool call to get any of them.

```then
update:
- slug: estimate-hi-no-read-calls
  set:
    status: pending
    purpose: After /hi the output of every block of the skill is in the first turn's context with no read call
    method: 'by hand at the /hi of the next session: the first turn''s context and the tool calls before it read in the transcript, written into the estimate line'
  change: the Criterion replaced whole — one When and Then; the hi line left to estimate-event-log-records, the block bookkeeping out; purpose and method set, Context and Method out (case 485.2)
```

```tasks
- [x] update `estimate-hi-no-read-calls`
- [ ] read `estimate-hi-no-read-calls` — by hand, at the `/hi` of a later session
```

### Case 485.3 — The git state at `/hi`, and no pull after it

> **given:**
> `estimate-git-context-current` — the promise, its Criterion replaced whole
> **＋** `rule-git-context` — the rule it promises for; its Render holds the four lines
> **＋** `.claude/skills/hi/SKILL.md` — the skill `/hi` that runs them
> **＋** `guppi/render.py` — `render --sync`, the command of the `Render:` line
> **＋** `vault/raw/<date>/event_log.md` — the log that records each Bash call of the session

> **when:**
> The person invokes `/hi`, and `.claude/skills/hi/SKILL.md` runs the four commands of `rule-git-context`.

> **then:**
> The context holds `Pull:` with the output of `git pull --ff-only`, then `Render:` with the output of `uv run guppi render --sync` (a diff for each governed file that differed and was written, or nothing), then `Branch:` with the current branch and `Status:` with `git status --short`.
> **＋** A pull that fails prints its message on the `Pull:` line, and the skill still completes.
> **－** No `git pull` runs later in the session: `vault/raw/<date>/event_log.md` shows none after the `hi` line.

```then
update:
- slug: estimate-git-context-current
  set:
    status: pending
    purpose: At /hi the context holds the pull, the render sync, the branch and the status; a failing pull does not stop the skill, and no pull runs later
    method: by hand at the /hi of the next session on the current remote, and that session's event_log.md read at its close for a later git pull, written into the estimate line
  change: the Criterion replaced whole — one When and Then; the Frontier item left to estimate-hi-writes-frontier, the block bookkeeping out; purpose and method set, Context and Method out (case 485.3)
```

```tasks
- [x] update `estimate-git-context-current`
- [ ] read `estimate-git-context-current` — by hand, at the `/hi` of a later session and at its close
```

### Case 485.4 — The open issues, or the reason there are none

> **given:**
> `estimate-github-issues-listed` — the promise, its Criterion replaced whole
> **＋** `rule-github-issues` — the rule it promises for; its Render holds the line `Open issues:`
> **＋** `.claude/skills/hi/SKILL.md` — the skill `/hi` that runs it

> **when:**
> The person invokes `/hi`, and `.claude/skills/hi/SKILL.md` runs `gh issue list --limit 5`.

> **then:**
> The line `Open issues:` holds the list of open issues, or the message of `gh` itself that names why there is none.
> **＋** Neither answer stops `/hi`: the blocks after the line still run.

```then
update:
- slug: estimate-github-issues-listed
  set:
    status: pending
    purpose: At /hi the context holds the open issues or the reason gh gives for none, and the skill completes
    method: by hand at the /hi of the next session, in the current gh state, written into the estimate line
  change: the Criterion replaced whole — one When and Then; purpose and method set, Context and Method out (case 485.4)
```

```tasks
- [x] update `estimate-github-issues-listed`
- [ ] read `estimate-github-issues-listed` — by hand, at the `/hi` of a later session
```

### Case 485.5 — The Tail of the ledger

> **given:**
> `estimate-ledger-tail` — the promise, its Criterion replaced whole
> **＋** `rule-ledger-tail` — the rule it promises for; its Render holds the line `Tail:`
> **＋** `guppi/tail.py` — the script `guppi tail`
> **＋** `guppi/archive.py` — `uncovered_lines`, the coverage of a line
> **＋** `guppi/materialize.py` — `units_with` and `parse_line`, the walk and the record lines
> **＋** `vault/raw/` — the folder of the ledgers and their yaml files
> **＋** `tests/test_tail.py` — the tests the reading runs
> **＋** `.claude/skills/hi/SKILL.md` — the skill `/hi` that splices the line

> **when:**
> `uv run guppi tail` runs, from the line `Tail:` of `.claude/skills/hi/SKILL.md` or by hand, over every `ledger.md` under `vault/raw/` and the `materialize.yaml` beside each.

> **then:**
> The script walks the date-level ledger of a date first, then its session ledgers in folder order, dates ascending. It prints every line that `parse_line` reads as a record and whose number is neither in the `line` or `folded` of an entry nor under `unparsed` of the yaml beside it. Each printed line opens with the date, and for a session ledger with the date, a slash and the session folder, then `L<n>:` and the line as the ledger holds it.
> **＋** A ledger without a yaml beside it prints every record line it has.
> **＋** A ledger fully covered prints nothing; with an empty tail the output is empty.
> **＋** Exit 0 always; a ledger that cannot be read is a line on stderr, and the walk goes on.
> **＋** The Render of `rule-ledger-tail`, `partial`, puts one line into `.claude/skills/hi/SKILL.md` between its markers: `` Tail: !`uv run guppi tail` ``.
> **－** `guppi/tail.py` holds no judgment of coverage of its own: the coverage of a line is `uncovered_lines` of `guppi/archive.py`, the one `guppi archive` uses.

```then
update:
- slug: estimate-ledger-tail
  set:
    status: pending
    purpose: guppi tail prints every ledger record line that no materialize.yaml covers, and /hi shows it as Tail
    method: 'pytest tests/test_tail.py; by hand at the /hi of the next session: the Tail line against a run of uv run guppi tail by hand, written into the estimate line'
  change: the Criterion replaced whole — one When and Then; purpose and method set, Context and Method out (case 485.5)
```

```tasks
- [x] update `estimate-ledger-tail`
- [ ] read `estimate-ledger-tail` — `pytest tests/test_tail.py`, then by hand at the `/hi` of a later session
```

### Case 485.6 — The note of Slice 3g stands after the group of session start and `/hi`

> **given:**
> `entity-sprint-migration` — the sprint page; its Slice 3g holds the note on the old layout
> **＋** `vault/wiki/sprint.md` — the render of the sprint page
> **＋** `/hi` — builds the Frontier from `vault/wiki/sprint.md`
> **＋** `rule-session-start` — the rule of the group this Case recuts

> **when:**
> The next `/hi` builds the Frontier from `vault/wiki/sprint.md`, drawn from `entity-sprint-migration`.

> **then:**
> Slice 3g still shows the one unticked note on the old layout, and the Frontier holds it as a `C` line.
> **＋** The History of `entity-sprint-migration` says that the old-layout Estimates of session start and `/hi` are recut.
> **－** The note is not ticked or reworded: the Case that recuts the last group ticks it.

```then
update:
- slug: entity-sprint-migration
  change: 'Slice 3g: the old-layout Estimates of session start and /hi recut to one Criterion; the note on the old layout stands (case 485)'
```

```tasks
- [x] update `entity-sprint-migration`
```
