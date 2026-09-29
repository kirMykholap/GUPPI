## Case 494 — Slice 3g: the done-conditions of the sprint recut to `When:` and `Then:`, and the note on every other Estimate leaves the Slice

> **context:**
> Each Estimate page holds one promise, its Criterion. A Criterion should hold only `When:`, the trigger and the input it acts on, and `Then:`, what must hold after. Older Estimates also open with `Given:`, a set of lines that describe the code and the cases as they stood on the day the promise was written. This last group holds the five done-conditions of `entity-sprint-migration` that still carry `Given:`: lint clean, the leftovers gone, the branch merged, the Rule-class files dissolved, and `index.md` gone. `estimate-sprint-migration-file-route-gone` has no `Given:` and is not touched. Their `Given:` describes the vault of September: the 62 findings of Cases 1–28, the list of the leftover folders, the scripts of the old `file` route, the map `index.md`. The one on `estimate-sprint-migration-merges` is not its own: it describes the cascade, the guard and `sprint_id` from the parent Case 209.
> The person decided in the first round on this item. The five are recut like the rest: `Given:` out, `When:` and `Then:` kept as the condition at the close. What becomes of them after the close stays with the open item of Slice 5 (case 478.2). A lost ratified text is restored, and a page with no `purpose` gets one. None of the five lost its Criterion to a tool fault like case 211.3. Their History shows only Criteria that cases 209, 229.1, 233.5, 244, 301, 306.7, 310.3, 318, 321, 329 and 367 wrote on purpose, so nothing is restored and no commit needs to be read. All five have `purpose` and `method`, so no field is set but `status`. Each Criterion is replaced whole and goes back to `pending`. Its reading waits for the close of the sprint, or for a later session (case 428.1).
> What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording. The content of the old lines is carried, except for the lines named here. Each `Given:` goes out. In 494.1 the line that the page `entity-sprint-migration` exists with its sections, and the `－` line on item F7 and "today's `sprint.md`", record the one-time build of the page in case 209.2, so they go out (case 485). In 494.3 "the render shows the three Done-when lines `[x]`" is a count that went stale, because the page now lists six Estimates. It becomes "every Done-when line". In 494.4 the pointer "`make lint` is the reading of `estimate-sprint-migration-lint-clean`" goes out. The two `－` lines on what Slice 3f did not do, the Renders `case-schema.md` and `CLAUDE.md` and the template engine, go out as bounds of an edit, and the template engine stays in the Backlog. The edge of `rule-sprint` to `entity-sprint` is named in words, "the sprint's rule to the sprint MOC", so that `given` stays within its frame. In 494.5 the old `When:`, "The last Case of theme 4 is applied by the librarian", is a one-time trigger. It becomes the reading its `method` names, the tree read for `§N` and `index.md`. Paths inside the promises are named in `given` or written in words, because a code span with a `/` reads as a path that `given` must name.
> The check also notes that 494.5 shares words with 494.4, since both say that `index.md` does not exist. This is expected. They were ratified as two done-conditions of the sprint by cases 301 and 310.3. 494.4 promises that no Rule-class file stands at the close of Slice 3f, and 494.5 promises that no pointer to the map remains in the tree. The recut keeps both as the person signed them.
> The note. Every item of the current milestone decides the Frontier: `guppi sprint` shows a line with no `[[slug]]` before its first ` — ` as a note, `- [ ] <text>`, and never ticks it. It leaves only by the `update` of the Case that ends it (case 313). This is the last group of the item, so 494.6 removes the line from `## Milestones` of `entity-sprint-migration` with one `replace` pair, and `uv run guppi sprint` writes the new `vault/wiki/sprint.md` at the librarian's run. The anchor of the pair runs from the note to the start of the next line, since a line break matches any whitespace, and its `new` keeps that start. So the pair removes one line and hits the page once. The other note of Slice 3g, on the old shape, stays word for word. Its "until lint counts no `unmigrated` page" keeps `estimate-end-of-work-order` on the Frontier, since its `## Context` and `## Method` sections count as `unmigrated`, and the first round left its `Given:` to that item. Slice 3g stays current with that one note, and no line goes to `## Closed` until the Slice closes.
> The frame. Each kept line was read against the sprint page, the `Makefile` and the tree. The sprint page lists six Estimates in `estimates`. No behaviour changes, so no code, test, Render or hook changes, and no reader keeps an old form. `rule-sprint` and `guppi/sprint.py` read a note as it is described here. The Case creates no page, so no vault query was run. Not done: the fate of a sprint's done-conditions after the close (case 478.2), and the old-layout item C2.

> **problem:**
> The five done-conditions of the sprint still open with a `Given:` of the vault as it stood in September, and some lines record the build of the page or a count that went stale. The item that asks for this recut also stands as an unticked note in Slice 3g, and nothing but a Case removes it.

> **recommend:**
> Replace each Criterion whole with only `When:` and `Then:`, kept as the condition at the close, less the lines that record a one-time act or bounds of an edit. Remove the note with one `replace` pair and render `sprint.md` again. Leaving the note until Slice 3g closes was rejected, because it would keep a finished item on the Frontier of every session.

### Case 494.1 — `make lint` clean at the close of the sprint

> **given:**
> `estimate-sprint-migration-lint-clean` — the promise, its Criterion replaced whole
> **＋** `entity-sprint-migration` — the sprint page it is a done-condition of
> **＋** `Makefile` — the target `lint`
> **＋** `guppi/lint.py` — the findings, `unmigrated` and `unread` among them

> **when:**
> Someone reads `make lint` at the close of the sprint.

> **then:**
> `make lint` exits 0: no finding in any category, `unmigrated` included — the old Estimate shape is gone, the counter at zero; the one exception is `unread` on the Estimates of the sprint page itself not yet read at that moment.

> **tasks:**
> - [ ] update `estimate-sprint-migration-lint-clean`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given and the one-time build of the sprint page out (case 494.1)`
> - [ ] read `estimate-sprint-migration-lint-clean` — `make lint` at the close of the sprint

> **ratification:**
> ```
> - decision[case 494.1][update][estimate-sprint-migration-lint-clean]{ref:estimate-sprint-migration-lint-clean}
> ```

### Case 494.2 — The leftovers gone at the close of the sprint

> **given:**
> `estimate-sprint-migration-leftovers-gone` — the promise, its Criterion replaced whole
> **＋** `entity-sprint-migration` — the sprint page it is a done-condition of
> **＋** `vault/parked/` — the parked pages
> **＋** `docs/` — the documents of 2026-08
> **＋** `docs/migration/` — the rule documents of the migration
> **＋** `vault/archive/` — the archive and its roots
> **＋** `vault/raw/` — the date folders

> **when:**
> Someone reads the tree of the repository at the close of the sprint.

> **then:**
> `vault/parked/` is empty or absent: each of its pages became a live vault page or lies in the archive.
> **＋** Under `docs/` no 2026-08 document remains, and no rule document of `docs/migration/`; each became a page, was archived, or was deleted by a decision named in the reading.
> **＋** `vault/archive/` has no root outside the folders of its sprints; `vault/raw/` has no date folder without a session.
> **＋** A decision stands on `git pull` without an upstream and on `gh` without a login — keep as is, or repair — and is named in the reading.
> **－** What to do with each thing this promise does not decide: those are the Cases of Slices 4 and 5.

> **tasks:**
> - [ ] update `estimate-sprint-migration-leftovers-gone`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given out (case 494.2)`
> - [ ] read `estimate-sprint-migration-leftovers-gone` — by hand on the tree at the close of the sprint

> **ratification:**
> ```
> - decision[case 494.2][update][estimate-sprint-migration-leftovers-gone]{ref:estimate-sprint-migration-leftovers-gone}
> ```

### Case 494.3 — Tests green and the branch merged at the close

> **given:**
> `estimate-sprint-migration-merges` — the promise, its Criterion replaced whole
> **＋** `entity-sprint-migration` — the sprint page it is a done-condition of
> **＋** `Makefile` — the target `test`
> **＋** `guppi/generate.py` — the cascade that sets the page `built`
> **＋** `vault/wiki/sprint.md` — the render that shows the Done-when lines

> **when:**
> Someone reads `git log` of `main` at the close of the sprint.

> **then:**
> `make test` is green on the last commit of `migration`.
> **＋** `migration` is merged into `main`; the last brief is written by the librarian on `main`.
> **＋** The cascade sets `entity-sprint-migration` `built` — that is the close of the sprint; `vault/wiki/sprint.md` shows every Done-when line `[x]`.

> **tasks:**
> - [ ] update `estimate-sprint-migration-merges`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given of another Case out, the count of Done-when lines out (case 494.3)`
> - [ ] read `estimate-sprint-migration-merges` — `make test` on the last commit of `migration`, then `git log` of `main` after the merge

> **ratification:**
> ```
> - decision[case 494.3][update][estimate-sprint-migration-merges]{ref:estimate-sprint-migration-merges}
> ```

### Case 494.4 — No Rule-class file at the close of Slice 3f

> **given:**
> `estimate-sprint-migration-rule-class-files-dissolved` — the promise, its Criterion replaced whole
> **＋** `vault/wiki/<category>/schema.yaml` — the schema file of a category
> **＋** `rule-<category>-schema` — the Leaf that renders it
> **＋** `rule-page-schemas` — the MOC of the schema rules
> **＋** `entity-glossary` — the page `glossary.md` is written from
> **＋** `guppi/` — the scripts, read for the `file` route and the retired term
> **＋** `tests/` — the tests, read for the retired term

> **when:**
> The reading at the close of Slice 3f: `ls` of the schemas and `index.md`, a grep of the `file` route and of the retired term over `guppi/` and `tests/`, `uv run guppi render --check` and `uv run guppi glossary --check`.

> **then:**
> No Rule-class file: every `vault/wiki/<category>/schema.yaml` is the Render of the Leaf `rule-<category>-schema` (`enforcement: render`, `governs` that yaml), with the description of its fields as yaml data; no `schema.md`; `glossary.md` is written by `guppi glossary` from the `## Terms` of `entity-glossary`, a table "term — meaning — page" grouped by the parent MOC, under a rule with `governs`, `implementation_ref` and `--check`; no `index.md`, and every §N pointer in the vault replaced by a slug.
> **＋** The scripts hold no `file` route: no `RULE_CLASS`, no `category: file`, no "applied by hand", no `rule_class_path`, no `prose_names`; the vault changes only by the scripts, from decisions.
> **＋** Every rule has its parent by the criterion of the audit: under a category's MOC a rule that holds for that category alone, the MOC made at two or more such rules, else the schemas under `rule-page-schemas`; `applies_to` on a Rule and `rules` on an Entity carry the edge Rule → Entity, the sprint's rule to the sprint MOC the first.
> **＋** "Rule-class" is a retired term in the Case schema and in the glossary, and no docstring of `guppi/` and no test name of `tests/` carries it.

> **tasks:**
> - [ ] update `estimate-sprint-migration-rule-class-files-dissolved`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given, the pointer to lint-clean and the bounds of the Slice out (case 494.4)`
> - [ ] read `estimate-sprint-migration-rule-class-files-dissolved` — by hand, the reading its `method` names, in a later session

> **ratification:**
> ```
> - decision[case 494.4][update][estimate-sprint-migration-rule-class-files-dissolved]{ref:estimate-sprint-migration-rule-class-files-dissolved}
> ```

### Case 494.5 — `index.md` gone, and no pointer to it

> **given:**
> `estimate-sprint-migration-index-dissolved` — the promise, its Criterion replaced whole
> **＋** `vault/wiki/index.md` — the map that is gone
> **＋** `vault/wiki/` — the live pages
> **＋** `.claude/` — the harness files
> **＋** `guppi/` — the docstrings of the scripts
> **＋** `CLAUDE.md` — the system prompt
> **＋** `vault/raw/` — the ledgers, which keep their pointers

> **when:**
> Someone reads the tree for `vault/wiki/index.md`, and reads `vault/wiki/`, `.claude/`, `guppi/` and `CLAUDE.md` for a `§N` and for `index.md`, each hit by hand.

> **then:**
> `vault/wiki/index.md` does not exist.
> **＋** No live page of `vault/wiki/`, no harness file and no docstring of `guppi/` points at a `§N` or at `index.md` as a source.
> **－** The archive and the ledgers under `vault/raw/` keep their pointers.

> **tasks:**
> - [ ] update `estimate-sprint-migration-index-dissolved`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — When and Then only, Given out, the one-time trigger of theme 4 replaced by the reading of the method (case 494.5)`
> - [ ] read `estimate-sprint-migration-index-dissolved` — by hand, the reading its `method` names, in a later session

> **ratification:**
> ```
> - decision[case 494.5][update][estimate-sprint-migration-index-dissolved]{ref:estimate-sprint-migration-index-dissolved}
> ```

### Case 494.6 — The note on every other Estimate leaves Slice 3g

> **given:**
> `entity-sprint-migration` — the sprint page; its `## Milestones` holds the two notes of Slice 3g
> **＋** `guppi/sprint.py` — renders a note as `- [ ] <text>`, never ticked
> **＋** `vault/wiki/sprint.md` — the render of the sprint page
> **＋** `/hi` — builds the Frontier from `vault/wiki/sprint.md`
> **＋** `estimate-end-of-work-order` — the page with `Given:` left to the note on the old shape

> **when:**
> `uv run guppi sprint` renders `vault/wiki/sprint.md` from `entity-sprint-migration` at the librarian's run, and the next `/hi` builds the Frontier from it.

> **then:**
> Slice 3g holds one note, on the old shape recut, and the Frontier holds it as a `C` line; the note on every other Estimate is gone from the page and from the render.
> **＋** The History of `entity-sprint-migration` says that the note on every other Estimate is done and removed.
> **－** The note on the old shape stays word for word: its "until lint counts no `unmigrated` page" keeps `estimate-end-of-work-order` on the Frontier.
> **－** No line is added to `## Closed`: Slice 3g stays open.

> **tasks:**
> - [ ] update `entity-sprint-migration`
>   - old: `` - every other Estimate: `Given:` out, the input of the scenario into `When:`, the `－` lines on the bounds of an edit out, each Criterion replaced whole - the old shape recut ``
>   - new: `- the old shape recut`
>   - change: `Slice 3g: the note on every other Estimate removed, its last group recut (cases 484, 488-494); the note on the old shape stands`
> - [ ] `uv run guppi sprint`

> **ratification:**
> ```
> - decision[case 494.6][update][entity-sprint-migration]{ref:entity-sprint-migration}
> ```
