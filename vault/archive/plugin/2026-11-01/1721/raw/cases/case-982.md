## Case 982 — A replaced Decision stays live while a page still names it

> **context:**
> When a decision puts off several pages, each page gets the decision in its `deferred_by`. A later Case that replaces that decision by `{supersedes:case N}` removes the name only from the pages that its own decision lines name (case 467.3), but `decision` of `.guppi/guppi/generate.py` still sets the whole earlier page `superseded`. Then `cascade` of the same run archives every superseded Decision page by `archived_by_cascade` (case 104.1), and `guppi cleanup` moves it out of `wiki/`. In session 0141, Cases 979, 980 and 981.2 each replaced Cases 971 and 976 and each named one other Estimate, so `estimate-close-reports-the-run` kept `deferred_by: ["[[decision-case-971]]"]` and `estimate-handoff-dispatches` kept `deferred_by: ["[[decision-case-976]]"]`, both pages archived under `vault/archive/plugin/2026-11-01/0141/decisions/`, as the Flags of the brief report. Nothing failed: lint takes an archived slug as a known ref, `backlog.md` lists both, and the librarian keeps an Estimate with `deferred_by` out of `Work` (`.claude/agents/librarian-guppi.md`, the Next session step). But the vault names, as the reason two Estimates wait, a decision it says no longer holds. The person asked why this happens and chose to fix the cause and to take both Estimates up now.
>
> The sprint close already keeps such a page: `judge_decisions` of `.guppi/guppi/sprint_close.py` keeps a Decision page of the sprint that a live page, not a Decision page and not one the close moves, names in a field of `KEEPERS`, `deferred_by` or `addressed_by` (case 627.1). I read `cascade`, `archived_by_cascade`, `decision`, `clear_deferred_by` and `supersede_children` of `.guppi/guppi/generate.py` and `judge_decisions` of `.guppi/guppi/sprint_close.py` whole: the two answer apart on a superseded Decision page that a live page names, which the close keeps and the cascade archives. The person chose that both keep it, for both fields, by one function and one list of `.guppi/guppi/generate.py`, which `.guppi/guppi/sprint_close.py` already imports from (`rule-one-judgment-one-implementation`). `cascade_notes` of `.guppi/guppi/prespec.py`, which `/pre-spec` and the check of a case file call (`.guppi/guppi/casecheck.py`, the call after the comment on case 739.2), predicts the archive by `archived_by_cascade` from the status of the pages alone; Case 982.2 gives it the same keep, so a Case is judged at build time as the librarian's run will judge it. The person agreed to that task in Case 982.1; it stands in its own sub-case because it replaces the Criterion of another Estimate.
>
> A Grep of `archived_by_cascade` over `.guppi/` printed `.guppi/guppi/generate.py` and `.guppi/guppi/prespec.py`. A Grep of `104\.1|archive of a superseded|superseded decision|superseded Decision` over `vault/wiki/**/*.md`, `.claude/**` and `.guppi/guppi/**` printed `vault/wiki/glossary.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-page-generation.md`, `vault/wiki/rules/rule-decisions-schema.md`, `vault/wiki/entities/entity-glossary.md`, `vault/wiki/estimates/estimate-generate-cascades.md`, `vault/wiki/estimates/estimate-generate-writes.md`, `vault/wiki/estimates/estimate-prespec-notes-a-page-the-cascade-archives.md` and `.guppi/guppi/generate.py`. The sentences of `rule-page-generation`, the field `status` of `rule-decisions-schema`, the row `archived` of `entity-glossary` (from which `guppi glossary` writes `glossary.md`) and the Criterion of `estimate-generate-cascades` change in Case 982.1. The hit in `estimate-generate-writes.md` is a History line, and the hit in `estimate-prespec-notes-a-page-the-cascade-archives.md` stands in its Result; its Criterion is replaced in Case 982.2. `rule-case-check` names among the pages the cascade archives "the Decision page of a superseded Case", by the judgment that `/pre-spec` prints. It stands, since `estimate-case-check-notes-a-page-the-cascade-archives` leaves which pages give a note to `estimate-prespec-notes-a-page-the-cascade-archives`. `estimate-sprint-close-archives-the-decisions` stands: the close keeps the same pages after its code moves into the shared function. `estimate-generate-writes-the-decision-page` stands: a `supersedes` still clears only the targets its Case names, and a page that stands `archived` keeps its status and its place (case 683). A Grep of `rule-page-generation|rule-decisions-schema|decisions/schema|decisions" / "schema|estimate-generate-cascades|estimate-close-reports-the-run|estimate-handoff-dispatches` over `.guppi/tests/` printed `.guppi/tests/test_generate.py`, `.guppi/tests/test_lint.py` and `.guppi/tests/test_ship.py`. Each writes its own copy under a temporary folder, so no test reads these files live. The tests of the shared defer in `.guppi/tests/test_generate.py` do not assert the status of the earlier page after a partial take-up, so they stand. In `.guppi/links.md`, `.guppi/tests/test_prespec.py` has no block; the blocks of the other changed pages and files name no neighbour whose purpose bears on the cascade but `rule-sprint-close`, whose Estimate stands as said. The ledger of session 1721 holds no `error` lesson.
>
> The new Criterion of `estimate-generate-cascades` keeps each line of the old one but the line on a superseded Decision page, which now carries the keep, and the new Criterion of `estimate-prespec-notes-a-page-the-cascade-archives` keeps each line but the list of archived pages and the line on the function that judges them, which now name the keep. The two `then` blocks of Cases 982.1 and 982.2 share words on purpose: the first states what the cascade does, the second what the note of `/pre-spec` predicts of it, and each is the Criterion of its own Estimate. Case 982.3 shares a few words with Case 982.2, on `deferred_by`, but it states a change of two pages, not of a check. The row `Decision (status)` of `entity-glossary` says that the cascade archives a superseded page, so Case 982.1 changes it beside the row `archived`. The `then` of Case 982.3 states only what `estimate-generate-writes-the-decision-page` checks, by its test run. Once the two pages carry no `deferred_by`, `guppi backlog` leaves them out of `backlog.md`, as `rule-backlog` sets it. No method reads that file in this session, and the next brief shows it.

> **problem:**
> A replaced decision is archived whole while a page it put off still names it, so that page waits on a decision the vault calls gone. Two Estimates stand so now.

> **recommend:**
> - **How the cause is fixed**
>   - Recommended: (a) the cascade keeps a replaced record while a page still names it.
>   - Answer: agreed, (a).
> - **What happens to the two checks now**
>   - Recommended: (a) take both up in this Case.
>   - Answer: agreed, (a).
> - **Which links keep a replaced record live**
>   - Recommended: (a) both fields, with one keep rule for the cascade and the sprint close.
>   - Answer: agreed, (a).
> - **How the take-up of the two checks is checked**
>   - Recommended: (b) the check that already covers it, `estimate-generate-writes-the-decision-page`.
>   - Answer: agreed, (b).

### Case 982.1 — The cascade keeps a replaced Decision that a live page names

> **given:**
> `.guppi/guppi/generate.py`: the cascade, `archived_by_cascade` and the new shared keep judgment.
> **＋** `.guppi/guppi/sprint_close.py`: `judge_decisions`, which imports the shared keep judgment.
> **＋** `.guppi/tests/test_generate.py`: the tests of the cascade.
> **＋** `rule-page-generation`: the sentence on the cascade.
> **＋** `rule-decisions-schema`: the field `status` of its Render `vault/wiki/decisions/schema.yaml`.
> **＋** `entity-glossary`: the rows `Decision (status)` and `archived`.
> **＋** `wiki/estimates/`: the folder of the Estimates that the cascade counts.
> **＋** `wiki/lessons/`: the folder where the cascade reads the status of a child of an Insight.
> **＋** `estimate-generate-cascades`: its Criterion is replaced whole.
> **＋** `rule-one-judgment-one-implementation`: one judgment in one module.

> **when:**
> `uv run --project .guppi guppi generate` runs the cascade after all entries of a unit.

> **then:**
> An entity or rule whose live Estimates are all `passed` becomes `built`; a `built` one with a live Estimate not `passed` returns to `draft`; an Estimate standing `archived` with its file still under `wiki/estimates/`, or a slug with no page, is not counted; History `status: a → b · cascade`.
> **＋** A Decision page with `status: superseded` becomes `archived` with History `archived · superseded`, unless a page of `vault/wiki/` that is no Decision page and does not stand `archived` names it in `deferred_by` or `addressed_by`; `superseded_by` and `deferred_by` are not touched.
> **＋** Such a named Decision page stays `superseded` under `vault/wiki/decisions/`, and becomes `archived` at the first run after no such page names it.
> **＋** The pages that keep a Decision page are judged by one function and one list of fields of `.guppi/guppi/generate.py`, and `.guppi/guppi/sprint_close.py` imports both for the Decision pages it keeps at the close of a sprint.
> **＋** Every `clustered` child of an Insight with `status: actioned` becomes `archived` with History `archived · insight actioned`; the Insight's `children` does not change.
> **＋** The `severity` of every Insight is recounted: a child's status is read under `wiki/lessons/`, else in the archive; a child with no page counts live; an `open` Insight at 0 becomes `archived` with History `archived · no live child`, `children` kept; an `actioned` one at 0 stays.
> **－** A page without Estimates keeps its status, and the cascade writes no section of any page.

> **tasks:**
> - [ ] `.guppi/guppi/generate.py`: `KEEPERS`, the fields `deferred_by` and `addressed_by`, and one function that gives the slugs of the Decision pages that a page, not a Decision page and not standing `archived`, names in a field of `KEEPERS`; `archived_by_cascade` takes that set and leaves a superseded Decision page in it out of what it archives; `cascade` passes the set read from the pages after all entries; the docstring of the cascade says so.
> - [ ] `.guppi/guppi/sprint_close.py`: `judge_decisions` imports `KEEPERS` and the function from `.guppi/guppi/generate.py` over the pages the close does not move, and its own copy of the list leaves.
> - [ ] `.guppi/tests/test_generate.py`: a superseded Decision page that a live page names in `deferred_by`, or that an Insight names in `addressed_by`, stays `superseded` under `wiki/decisions/`; it becomes `archived` at the run after the last name is cleared; one test runs the cascade and the judgment of `.guppi/guppi/sprint_close.py` over the same pages and asserts that they keep the same Decision pages.
> - [ ] update `rule-page-generation`
>   - old: `` the cascade after all entries computes what is computed — `built`, the archive of a superseded decision, the severity of an Insight, the `rules` of an Entity from the `applies_to` of the live rules (case 305.3) — never by hand (case 104). ``
>   - new: `` the cascade after all entries computes what is computed — `built`, the archive of a superseded decision, the severity of an Insight, the `rules` of an Entity from the `applies_to` of the live rules (case 305.3) — never by hand (case 104); a superseded decision that a live page other than a Decision page names in `deferred_by` or `addressed_by` stays `superseded` under `wiki/decisions/` until no such page names it, by the judgment with which `guppi sprint-close` keeps a Decision page, so that no live page names an archived Decision (as set in case 982.1). ``
>   - change: `a superseded decision that a live page names in deferred_by or addressed_by is not archived by the cascade`
> - [ ] update `rule-decisions-schema`
>   - old: `a superseded Decision no longer describes the present (case 104.1);`
>   - new: `` a superseded Decision no longer describes the present (case 104.1), but for one that a live page other than a Decision page names in `deferred_by` or `addressed_by`, which stays `superseded` until no such page names it (as set in case 982.1); ``
>   - change: `the cascade keeps a superseded Decision page that a live page names in deferred_by or addressed_by`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/decisions/schema.yaml`
> - [ ] update `entity-glossary`
>   - old: `` `archived` when the cascade of `generate` then meets it; ``
>   - new: `` `archived` when the cascade of `generate` then meets it, but for one that a live page other than a Decision page names in `deferred_by` or `addressed_by`, which stays `superseded` until no such page names it; ``
>   - old: `a superseded Decision, the lessons of an actioned Insight`
>   - new: `` a superseded Decision that no live page names in `deferred_by` or `addressed_by`, the lessons of an actioned Insight ``
>   - change: `the cascade archives a superseded Decision that no live page names`
> - [ ] `uv run --project .guppi guppi glossary`
> - [ ] update `estimate-generate-cascades`
>   - set: `{status: pending, purpose: "The cascade computes built, the archive of a superseded decision that no live page names in deferred_by or addressed_by, and the severity of an Insight, never by hand"}`
>   - change: `the Criterion replaced whole — a superseded Decision page that a live page names in deferred_by or addressed_by is kept, by the judgment the sprint close imports`
> - [ ] read `estimate-generate-cascades`

> **ratification:**
> ```
> - decision[case 982.1][update][rule-page-generation]{ref:rule-page-generation}
> - decision[case 982.1][update][rule-decisions-schema]{ref:rule-decisions-schema}
> - decision[case 982.1][update][entity-glossary]{ref:entity-glossary}
> - decision[case 982.1][update][estimate-generate-cascades]{ref:rule-page-generation}
> ```

### Case 982.2 — The cascade note of pre-spec reads the same keep

> **given:**
> `.guppi/guppi/prespec.py`: `cascade_notes`, which `/pre-spec` and the check of a case file call.
> **＋** `.guppi/tests/test_prespec.py`: the tests of the cascade notes.
> **＋** `.guppi/guppi/generate.py`: the shared keep judgment and `archived_by_cascade`.
> **＋** `estimate-prespec-notes-a-page-the-cascade-archives`: its Criterion is replaced whole.
> **＋** `rule-prespec-hook`: the hook that does not block the exit from Plan Mode on a note.

> **when:**
> `uv run --project .guppi guppi prespec --check <plan> --session <id>` reads the `then` blocks of the plan and the decision lines of the session's window.
> **＋** Or `.guppi/tests/test_prespec.py` runs it over a made-up plan.

> **then:**
> For each `update` item of the plan whose page the cascade of `.guppi/guppi/generate.py` archives once the items of the plan apply, the check prints one line that opens with `note:` and names the Case of the `update`, the page and the Case whose item sets off the archive.
> **＋** The pages archived are: each lesson standing `clustered` among the `children` of an Insight that an `update` of the plan sets `status: actioned`; each Insight standing `open` whose every child stands `archived` once the items of the plan apply; and the Decision page of each Case that a `{supersedes:case N}` mark on a decision line of the session names, but for one that a live page other than a Decision page still names in `deferred_by` or `addressed_by`.
> **＋** A name in `deferred_by` no longer keeps a Decision page when a decision line of the Case that carries the mark names that page, as `generate` clears it.
> **＋** The pages are judged by `archived_by_cascade` and the keep judgment of `.guppi/guppi/generate.py`, which the cascade of `uv run --project .guppi guppi generate` calls too.
> **＋** An `update` and the item that sets off its archive in one Case, or in two sub-cases of one Case, give the note too.
> **＋** The note is no finding: it does not change the exit code, and the hook of `rule-prespec-hook` does not block the exit from Plan Mode on it.
> **＋** The agent answers the note in one line in the chat, and the person may change a Case or keep the `update`.
> **－** A `create`, `delete` or `defer` item of such a page gives no note.
> **－** A rule or an entity that the cascade moves between `built` and `draft` gives no note.

> **tasks:**
> - [ ] `.guppi/guppi/prespec.py`: `cascade_notes` reads the kept Decision pages by the function of `.guppi/guppi/generate.py` over the live pages, drops each name in `deferred_by` of a page that a decision line of the Case carrying the mark names, and passes the set to `archived_by_cascade`; the docstring of `cascade_notes` and the paragraph of the module on it say so.
> - [ ] `.guppi/tests/test_prespec.py`: a mark on a Decision page that a live page names in `deferred_by` or `addressed_by` gives no note for an `update` of that page; the same mark gives the note when the Case of the mark names the page that carries the `deferred_by`.
> - [ ] update `estimate-prespec-notes-a-page-the-cascade-archives`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a superseded Decision page that a live page still names is not archived, by the keep judgment of generate`
> - [ ] read `estimate-prespec-notes-a-page-the-cascade-archives`

> **ratification:**
> ```
> - decision[case 982.2][update][estimate-prespec-notes-a-page-the-cascade-archives]{ref:rule-prespec}
> ```

### Case 982.3 — The two Estimates leave their archived defers

> **given:**
> `estimate-close-reports-the-run`: put off by the archived `decision-case-971`.
> **＋** `estimate-handoff-dispatches`: put off by the archived `decision-case-976`.
> **＋** `.guppi/guppi/generate.py`: a `supersedes` clears the `deferred_by` of the pages its Case names.
> **＋** `decision-case-982.3`: the Decision page of this sub-case.

> **when:**
> `uv run --project .guppi guppi generate` applies the `update` of `estimate-close-reports-the-run` and of `estimate-handoff-dispatches`, whose decision lines carry `{supersedes:case 971}` and `{supersedes:case 976}`.

> **then:**
> Neither `estimate-close-reports-the-run` nor `estimate-handoff-dispatches` carries `deferred_by`.
> **＋** Both stand `pending`, their Criterion, `purpose` and `method` unchanged.
> **＋** `decision-case-971` and `decision-case-976` stay `archived` where they lie and take `decision-case-982.3` into their `superseded_by`.
> **－** No other page that `decision-case-971` or `decision-case-976` put off changes.

> **tasks:**
> - [ ] update `estimate-close-reports-the-run`
>   - change: `the defer of decision-case-971, archived as superseded, retired; the reading waits for its event`
> - [ ] update `estimate-handoff-dispatches`
>   - change: `the defer of decision-case-976, archived as superseded, retired; the reading waits for its event`

> **ratification:**
> ```
> - decision[case 982.3][update][estimate-close-reports-the-run]{ref:rule-close}{supersedes:case 971}{supersedes:case 976}
> - decision[case 982.3][update][estimate-handoff-dispatches]{ref:rule-handoff}{supersedes:case 971}{supersedes:case 976}
> ```
