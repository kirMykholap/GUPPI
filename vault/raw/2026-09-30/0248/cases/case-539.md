## Case 539 — `generate` moves no line of the sprint page, and the finish conditions stand only under Done when

> **context:**
> After the cascade, `guppi generate` reads the `frontier.md` of every session. It moves to the `## Backlog` of the sprint page any milestone item that three sessions in a row put off, and it drops a milestone that the move leaves with no item (cases 354.1, 354.2). The librarian's run over session 0138 moved four items out of Slice 5 — closing of `entity-sprint-migration`: `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges`, `rule-spec-box` and `rule-morph`. The first two are Estimates of the sprint page, its finish conditions, and they can be read only at the close. So every session puts them off, and the move always takes them. `vault/wiki/backlog.md` now lists them as work put off in 3 sessions, while `vault/wiki/sprint.md` still shows them under Done when, which it reads from the page's `estimates`. The move worked as ratified. The person chose three things. First, the move goes, because in practice it gets in the way: a line of the sprint page moves only when the person asks for it. Second, the finish conditions of a sprint stand under Done when and are never item lines, so each milestone holds exactly the items whose closing closes it. Third, `rule-spec-box` and `rule-morph` stay in the Backlog. In the second round the person also chose three things. `estimate-sprint-moves-a-passed-over-item` is renamed to `estimate-sprint-items-move-only-by-a-case` and gets the opposite promise, with a test. `estimate-sprint-drops-an-emptied-milestone` is deleted. The principle is one sentence in `rule-sprint`, and no check enforces it. The Criterion of `estimate-brief-written`, replaced by Case 538.2 in this session, named the Flags line on moves. That Case is rebuilt by its own `case-guppi` without the line, so this Case does not touch that Estimate. By the same rule, `estimate-sprint-migration-leftovers-gone` also leaves Slice 5, which then holds only its note on the close of a sprint. The note keeps the milestone open. No page is created without a `ref`, so no vault query ran.
> In the frame, the change makes six texts false, and this Case rewrites each one. The first is the sentence of `rule-sprint` on the move. The second is two sentences of the Purpose of `rule-page-generation`: the list of the steps and of what they read, where no step reads the Frontiers any more, and the sentence on the move. The third is the Flags item and the sentence on how the sprint page changes in the Render of `rule-brief`; those pairs stay off the paragraph on `carry` that Case 538.2 rewrites. The fourth is the reason that the Render of `rule-skill-hi` gives for opening a sprint line with its slugs in code spans, namely that `generate` counts it; the form of the line stays, and `guppi backlog` still reads its slugs for its count. The fifth is the words "the reader of the sprint move" in `rule-backlog` and in the docstring of `guppi/backlog.py`. The sixth is the same words in the Criterion of `estimate-backlog-renders`: at pre-spec the person chose to replace that Criterion whole, in sub-case 539.4. `estimate-hi-writes-frontier` asks for the slug in a code span and gives no reason, so it stands. `estimate-sprint-renders-the-backlog` promises one Done when line per Estimate, and that does not change. The functions `frontiers` and `frontier_marks` stay in `guppi/generate.py`, because `guppi/backlog.py` imports them. The History lines of the moves already made stay on the sprint page. The code change runs from the working tree in Work Mode. No reader refuses an old form in the meantime, so no old form is kept.
> Three things will look like gaps at the check and are on purpose. First, sub-case 539.1 carries no line of the old Criterion of `estimate-sprint-moves-a-passed-over-item`: the count, the move, its History line and its exceptions are the promise the person chose to reverse. Second, sub-case 539.4 carries every line of the old Criterion of `estimate-backlog-renders` but one. The line on the count now names `generate.frontier_marks` without the words on the move, and it adds that `guppi/backlog.py` holds no copy of that reader. Third, some sub-cases share words. Sub-cases 539.1 and 539.2 both say that the sprint page changes only by a Case: one for `generate`, one for the frame of the librarian. Sub-cases 539.1 and 539.3 both say that the rule pages no longer name the move, each for its own pages. Sub-cases 539.3 and 539.4 both speak of the lines of `## Deferred` in `backlog.md`: one for the sprint page, one for the promise of the script. Each sub-case keeps its words so that it reads alone. Not done: a check that refuses a finish condition written as an item, which the person did not take; the close of a sprint, still a note of Slice 5 (Frontier item C2); and `rule-spec-box` and `rule-morph`, which stay in the Backlog.

> **problem:**
> `generate` moves sprint items by a count of put-offs. That count always reaches the finish conditions of the sprint, which can only be read at the close, so the move turns them into put-off work in `backlog.md`. The person wants no line of the sprint page to move without their request. They also want the finish conditions to stand only under Done when, so that each milestone holds exactly the items whose closing closes it.

> **recommend:**
> Remove the move and the drop of an emptied milestone from `guppi/generate.py`. Turn the promise of the move into the promise that nothing moves, and delete the promise of the drop. Remove the words on the move from `rule-sprint`, `rule-page-generation`, `rule-brief`, `rule-skill-hi`, `rule-backlog` and the Criterion of `estimate-backlog-renders`. Write the principle into `rule-sprint`. Take the three finish conditions off the item lists of `entity-sprint-migration`. Exempting the finish conditions from the move was rejected: it keeps a mechanism that the person found gets in the way, and it puts the finish conditions back into every Frontier as items to put off.

### Case 539.1 — `generate` moves no line of the sprint page

> **given:**
> `guppi/generate.py` — the script; the move and the drop after the cascade are removed
> **＋** `tests/test_generate.py` — the tests of the move, replaced by one test that nothing moves
> **＋** `rule-sprint` — the rule of the sprint page; says how its lists change
> **＋** `rule-page-generation` — the rule of `generate`; names the steps it computes beyond the yaml and what they read
> **＋** `estimate-sprint-moves-a-passed-over-item` — the promise of the move, renamed and turned to its opposite
> **＋** `estimate-sprint-drops-an-emptied-milestone` — the promise that an emptied milestone leaves, deleted
> **＋** `entity-sprint-<id>` — the sprint page, its `## Milestones`, `## Backlog` and History
> **＋** `frontier.md` under `vault/raw/` and `vault/archive/` — the Frontiers the move counted

> **when:**
> `uv run guppi generate` runs over the vault with one live page `entity-sprint-<id>`, and the `frontier.md` of three or more sessions in a row, under `vault/raw/` or `vault/archive/`, holds a `[-]` line that names an item of its `## Milestones` in a code span.

> **then:**
> After the run, `## Milestones` and `## Backlog` of `entity-sprint-<id>` stand as before it, each line in its place, unless an entry of the run changes the page.
> **＋** A milestone whose items were all put off keeps its heading under `## Milestones`.
> **＋** `guppi/generate.py` writes no line about a move into the History of `entity-sprint-<id>`, and it prints no such line on stdout.
> **＋** A line of `entity-sprint-<id>` moves only through an entry of a Case the person ratified, an `update` that `generate` applies like any other.
> **－** `rule-sprint` and `rule-page-generation` name no move of a sprint line by `generate`.

> **tasks:**
> - [ ] update `rule-sprint` — the sprint page changes only by a Case
>   - old: `` the backlog changes by an `update` of the sprint page, a Case, and by one move of `generate`: a milestone item passed over in three sessions in a row goes to the Backlog, and a milestone the move left with no line leaves the Milestones (cases 354.1, 354.2). ``
>   - new: `` the milestones and the backlog change only by an `update` of the sprint page, a Case: `generate` moves no line of the page, however many sessions put an item off (case 539.1). ``
>   - change: `the move of a passed-over item and the drop of an emptied milestone removed; the sprint page changes only by a Case (case 539.1)`
> - [ ] update `rule-page-generation` — the move leaves the steps of the script, and no step reads the Frontiers
>   - old: `` the pages, the Specs, the ledgers and the Frontiers of `raw/` and the archive by the steps this page names — the cascade, the move of the sprint, the ticks of the Spec ``
>   - new: `` the pages, the Specs and the ledgers of `raw/` by the steps this page names — the cascade, the ticks of the Spec ``
>   - old: `` After the cascade, the script moves a milestone item of the sprint page passed over in three sessions in a row to its Backlog, by the Frontiers of `raw/` and the archive, and drops a milestone the move left with no line (`rule-sprint`, cases 354.1, 354.2). ``
>   - new: `` The script moves no line of the sprint page: a milestone item leaves its milestone only by a Case (`rule-sprint`, case 539.1). ``
>   - change: `the move of a passed-over sprint item and the drop of an emptied milestone removed, and with them the reading of the Frontiers (case 539.1)`
> - [ ] update `estimate-sprint-moves-a-passed-over-item` — renamed; the Criterion replaced whole: nothing moves
>   - rename: `estimate-sprint-items-move-only-by-a-case`
>   - set: `{status: pending, purpose: "Whether generate leaves every line of the sprint page in place, a milestone item put off in many sessions in a row included, so that a line moves only by a Case", method: "uv run pytest tests/test_generate.py -k moves_no_line; then by hand, the History of entity-sprint-<id> after the librarian's run of a later session: no line of generate on a move"}`
>   - change: `renamed from estimate-sprint-moves-a-passed-over-item and the Criterion replaced whole — generate moves no line of the sprint page (case 539.1)`
> - [ ] delete `estimate-sprint-drops-an-emptied-milestone`
>   - impact: `The promise ends with the move (case 539.1): no milestone is emptied by generate, so none is dropped; cleanup takes the slug out of the estimates of rule-sprint`
> - [ ] `guppi/generate.py` — `move_passed_over`, `passes_in_a_row`, `PASSES_TO_MOVE` and their call after the cascade removed, and the paragraph of the docstring on the move; `frontiers` and `frontier_marks` stay, since `guppi/backlog.py` imports them
> - [ ] `tests/test_generate.py` — the six tests of the move removed; one test `test_generate_moves_no_line_of_the_sprint_page`: a sprint page whose items are put off in three and more sessions in a row stands unchanged after the run, and stdout names no move
> - [ ] read `estimate-sprint-items-move-only-by-a-case` in a later session, after the librarian's run

> **ratification:**
> ```
> - decision[case 539.1][update][rule-sprint]{ref:rule-sprint}
> - decision[case 539.1][update][rule-page-generation]{ref:rule-page-generation}
> - decision[case 539.1][update][estimate-sprint-moves-a-passed-over-item]{ref:rule-sprint}
> - decision[case 539.1][delete][estimate-sprint-drops-an-emptied-milestone]{ref:estimate-sprint-drops-an-emptied-milestone}
> ```

### Case 539.2 — the brief names no move of the sprint

> **given:**
> `rule-brief` — the frame of the brief, whose Render is spliced into the frame of the librarian
> **＋** `.claude/agents/librarian-guppi.md` — the rendered frame of the librarian
> **＋** `vault/wiki/brief.md` — the brief the librarian writes
> **＋** `entity-sprint-<id>` — the sprint page
> **＋** `guppi/generate.py` — the script whose printed lines the Flags read

> **when:**
> The librarian rewrites `vault/wiki/brief.md` at the end of its run, with `.claude/agents/librarian-guppi.md` rendered from `rule-brief`.

> **then:**
> The frame asks for no Flags line on an item that `guppi/generate.py` moved to the Backlog of `entity-sprint-<id>`, and none on a dropped milestone, so the Flags of `vault/wiki/brief.md` hold no such line.
> **＋** The frame says that `entity-sprint-<id>` changes only by a Case.
> **－** The other kinds of flag that the frame names stand as before, the lint output included.
> **－** The paragraph of the frame on the brief of the skill `carry` does not change here.

> **tasks:**
> - [ ] update `rule-brief` — Flags name no move of the sprint, and the sprint page changes only by a Case
>   - old: `` contradictions; every item `generate` moved to the Backlog in this run — its slug, its milestone, the count and the sessions — and every milestone it dropped, from the lines it printed (case 354.4); the lint output. ``
>   - new: `contradictions; the lint output.`
>   - old: `` the sprint page changes by a Case, or by the move of `generate` (case 354.1), and ``
>   - new: `the sprint page changes only by a Case (case 539.2), and`
>   - change: `Flags no longer name items moved to the Backlog or milestones dropped; the sprint page changes only by a Case (case 539.2)`
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`

> **ratification:**
> ```
> - decision[case 539.2][update][rule-brief]{ref:rule-brief}
> ```

### Case 539.3 — the finish conditions of a sprint stand only under Done when

> **given:**
> `rule-sprint` — the rule of the sprint page; its `estimates` are the Definition of done
> **＋** `entity-sprint-migration` — the sprint page, its `## Milestones` and `## Backlog`
> **＋** `vault/wiki/sprint.md` — written by `uv run guppi sprint`
> **＋** `vault/wiki/backlog.md` — written by `uv run guppi backlog`
> **＋** `rule-backlog` — the rule of `backlog.md`; names the reader of the count
> **＋** `guppi/backlog.py` — the script; its docstring names the reader of the count
> **＋** `rule-skill-hi` — the rule whose Render is the skill `/hi`; gives the form of a sprint line of the Frontier

> **when:**
> The librarian runs `uv run guppi sprint` and `uv run guppi backlog` after `generate` has applied the update of `entity-sprint-migration`, and a reader reads `rule-sprint`, `rule-backlog` and `rule-skill-hi`.

> **then:**
> `vault/wiki/sprint.md` shows each Estimate of `entity-sprint-migration` under Done when only, and no item of a milestone or of `## Backlog` names one of them.
> **＋** Slice 5 — closing holds only its note on the close of a sprint, and it stays the current milestone, open.
> **＋** `vault/wiki/backlog.md` lists no Estimate of `entity-sprint-migration`. The other lines of the page's `## Backlog` stay, and `backlog.md` lists them with their counts as before.
> **＋** `rule-sprint` says that the Estimates of a sprint page stand only under Done when, never as an item line, so that each milestone holds exactly the items whose closing closes it.
> **＋** `rule-backlog` and the docstring of `guppi/backlog.py` name `generate.frontier_marks` as the reader of the count, with no move of the sprint.
> **＋** `rule-skill-hi` keeps the form of a sprint line, its title opening with its slugs in code spans, and gives no count by `generate` as its reason.
> **－** The `estimates` of `entity-sprint-migration` do not change, so the Done when list stays whole.
> **－** No check refuses an item line that names an Estimate of the sprint page.

> **tasks:**
> - [ ] update `rule-sprint` — the Estimates of a sprint page stand only under Done when
>   - old: `` whose `estimates` are its Definition of done and whose `## Milestones` lists the Slices in order ``
>   - new: `` whose `estimates` are its Definition of done — rendered under Done when and never written as an item line of a milestone or of the Backlog, so that each milestone holds exactly the items whose closing closes it (case 539.3) — and whose `## Milestones` lists the Slices in order ``
>   - change: `the Estimates of a sprint page stand only under Done when, never as an item line (case 539.3)`
> - [ ] update `entity-sprint-migration` — the finish conditions off the item lists
>   - sections.Milestones:
>     ```
>     ### Slice 5 — closing
>
>     - the close of a sprint — `entity-sprint-<id>` and the Estimates it lists go to the archive together once each has passed: a done-condition of a sprint has nothing left to guard after the close; not yet decided (case 478.2)
>     ```
>   - sections.Backlog:
>     ```
>     - the product model: `kind: test | measurement | reading`, `ask-guppi` through Entities, the vault-query questions before a product's records (session 1119); `applies_to` and `rules` taken into Slice 3f (case 301)
>     - reuse, the edge: `uses` / `used_by` between Entities — `uses` written in the Case on the side that uses, `used_by` computed by the cascade of `generate`, the pair checked by lint, the pattern of `applies_to` / `rules`; no edge Rule → Rule (cases 305, 319)
>     - reuse, the question: the vault query before a `create` asks a second question — what of the existing this thing could use, by the index lines of the Entities — and the answer stands in `context`; the Case names what it found in `uses` or says why it is not used (case 319)
>     - reuse, the hook: a lint finding on two live Entities naming one path in `code_ref` with no edge between them; a new module written beside an existing one in another file is caught by the question alone, not by a script (case 319)
>     - a template engine for the rendered files — one script with the shape of each file declared, once a third render beside `sprint.md` and `glossary.md` appears (case 301)
>     - [[rule-work-mode]] — the rest of Work Mode past the skill `/work` of case 479.2: the test of each Estimate written first and turned green, and the full model the person plans; cases 183, 206
>     - [[rule-subagent-guppi]] — what a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case; cases 183, 206
>     - [[rule-spec-box]] — the Spec box, case 207, after Slice 3b
>     - [[rule-morph]] — the morph mechanism: the initiation at install sets the category set of the project, the development set by default, held as data so that a changed set rewrites no rule; case 239
>     ```
>   - change: `the finish conditions lint-clean, merges and leftovers-gone stand only under Done when: off Slice 5 and the Backlog (case 539.3)`
> - [ ] update `rule-backlog` — the reader of the count named without the move
>   - old: `` The count reads the Frontier files by `generate.frontier_marks`, the reader of the sprint move, and the Specs ``
>   - new: `` The count reads the Frontier files by `generate.frontier_marks`, and the Specs ``
>   - change: `the reader of the count named without the sprint move, removed by case 539.1 (case 539.3)`
> - [ ] update `rule-skill-hi` — the form of a sprint line kept, the count by `generate` gone as its reason
>   - old: ``` `` — so that `generate` counts it (case 354.3). ```
>   - new: ``` ``. ```
>   - change: `a sprint line keeps its slugs in code spans; the count by generate, removed by case 539.1, is no longer its reason (case 539.3)`
> - [ ] `guppi/backlog.py` — the docstring of the module and of `sessions_of` name `generate.frontiers` and `generate.frontier_marks` without "the reader of the sprint move"
> - [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] `uv run guppi sprint`

> **ratification:**
> ```
> - decision[case 539.3][update][rule-sprint]{ref:rule-sprint}
> - decision[case 539.3][update][entity-sprint-migration]{ref:entity-sprint-migration}
> - decision[case 539.3][update][rule-backlog]{ref:rule-backlog}
> - decision[case 539.3][update][rule-skill-hi]{ref:rule-skill-hi}
> ```

### Case 539.4 — the promise of `backlog.md` names its count reader without the move

> **given:**
> `estimate-backlog-renders` — the promise of what `guppi backlog` writes
> **＋** `guppi/backlog.py` — the script `uv run guppi backlog`, which the librarian runs after `guppi sprint`
> **＋** `vault/wiki/backlog.md` — the file it writes; the governed-files hook refuses a hand edit
> **＋** `guppi/generate.py` — `frontier_marks`, the reader of the Frontier lines; `generate` applies the defers
> **＋** `guppi/materialize.py` — the Spec reader; `materialize` lifts the defers
> **＋** `entity-sprint-<id>` — the sprint page, its `## Backlog`
> **＋** `rule-carry-over` — the skill `carry`, which writes `carry.md` and runs the script
> **＋** `vault/wiki/`, `vault/raw/` and `vault/archive/` — the pages, and the session folders with their `frontier.md`, `spec.md` and `carry.md`

> **when:**
> `uv run guppi backlog` runs over `vault/wiki/`, `vault/raw/` and `vault/archive/`. The librarian runs it after `guppi sprint`, and the skill `carry` runs it after it writes `carry.md`.

> **then:**
> The script writes `vault/wiki/backlog.md`: the heading `# Backlog`, the line `N items`, then `## Conserved Specs` and `## Deferred`.
> **＋** `## Conserved Specs` holds each session folder under `vault/raw/` that holds `carry.md`. Each has one line that names its `spec.md` and its Cases. Under that line stands one line per item of its `then` blocks, with the kind and the slug, read by the Spec reader of `guppi/materialize.py`.
> **＋** `## Deferred` holds one line per item. The items are each live page with a `deferred_by` that is not empty, each Insight whose `status` is `open`, and each line of the `## Backlog` of `entity-sprint-<id>`. A line holds the slug, the page's `purpose` (for an Insight, its `pattern` and `severity`) and the count. A Backlog line that names no page stands by its text.
> **＋** The count of an item is the number of sessions whose `frontier.md`, under `vault/raw/` or `vault/archive/`, holds a `[-]` line that names its slug in a code span of its title. It is read by `generate.frontier_marks`, and `guppi/backlog.py` holds no copy of that reader.
> **＋** `N` counts the conserved Specs and the lines of `## Deferred`. A slug that stands under a conserved Spec does not stand again under `## Deferred`, and a slug of two sources stands once.
> **＋** A folder whose `carry.md` is gone shows nothing. Its defers enter `## Deferred` through `deferred_by` once `materialize` and `generate` have applied them.
> **－** The script writes no page of `vault/wiki/` and no file but `vault/wiki/backlog.md`. The governed-files hook refuses a hand edit of that file.

> **tasks:**
> - [ ] update `estimate-backlog-renders`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the reader of the count named without the sprint move, removed by case 539.1 (case 539.4)`
> - [ ] read `estimate-backlog-renders` in a later session: `uv run pytest tests/test_backlog.py`, and `vault/wiki/backlog.md` after the librarian's run

> **ratification:**
> ```
> - decision[case 539.4][update][estimate-backlog-renders]{ref:rule-backlog}
> ```
