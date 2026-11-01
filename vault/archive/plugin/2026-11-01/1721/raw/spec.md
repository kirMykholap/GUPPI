<!-- approved 19:54:47 · session cb575daf -->

# Session 1721 — the stale defers of two Estimates

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

```then
update:
- slug: rule-page-generation
  replace:
  - old: the cascade after all entries computes what is computed — `built`, the archive of a superseded decision, the severity of an Insight, the `rules` of an Entity from the `applies_to` of the live rules (case 305.3) — never by hand (case 104).
    new: the cascade after all entries computes what is computed — `built`, the archive of a superseded decision, the severity of an Insight, the `rules` of an Entity from the `applies_to` of the live rules (case 305.3) — never by hand (case 104); a superseded decision that a live page other than a Decision page names in `deferred_by` or `addressed_by` stays `superseded` under `wiki/decisions/` until no such page names it, by the judgment with which `guppi sprint-close` keeps a Decision page, so that no live page names an archived Decision (as set in case 982.1).
  change: a superseded decision that a live page names in deferred_by or addressed_by is not archived by the cascade
- slug: rule-decisions-schema
  replace:
  - old: a superseded Decision no longer describes the present (case 104.1);
    new: a superseded Decision no longer describes the present (case 104.1), but for one that a live page other than a Decision page names in `deferred_by` or `addressed_by`, which stays `superseded` until no such page names it (as set in case 982.1);
  change: the cascade keeps a superseded Decision page that a live page names in deferred_by or addressed_by
- slug: entity-glossary
  replace:
  - old: '`archived` when the cascade of `generate` then meets it;'
    new: '`archived` when the cascade of `generate` then meets it, but for one that a live page other than a Decision page names in `deferred_by` or `addressed_by`, which stays `superseded` until no such page names it;'
  - old: a superseded Decision, the lessons of an actioned Insight
    new: a superseded Decision that no live page names in `deferred_by` or `addressed_by`, the lessons of an actioned Insight
  change: the cascade archives a superseded Decision that no live page names
- slug: estimate-generate-cascades
  set:
    status: pending
    purpose: The cascade computes built, the archive of a superseded decision that no live page names in deferred_by or addressed_by, and the severity of an Insight, never by hand
  change: the Criterion replaced whole — a superseded Decision page that a live page names in deferred_by or addressed_by is kept, by the judgment the sprint close imports
```

```tasks
- [x] `.guppi/guppi/generate.py`: `KEEPERS`, the fields `deferred_by` and `addressed_by`, and one function that gives the slugs of the Decision pages that a page, not a Decision page and not standing `archived`, names in a field of `KEEPERS`; `archived_by_cascade` takes that set and leaves a superseded Decision page in it out of what it archives; `cascade` passes the set read from the pages after all entries; the docstring of the cascade says so.
- [x] `.guppi/guppi/sprint_close.py`: `judge_decisions` imports `KEEPERS` and the function from `.guppi/guppi/generate.py` over the pages the close does not move, and its own copy of the list leaves.
- [x] `.guppi/tests/test_generate.py`: a superseded Decision page that a live page names in `deferred_by`, or that an Insight names in `addressed_by`, stays `superseded` under `wiki/decisions/`; it becomes `archived` at the run after the last name is cleared; one test runs the cascade and the judgment of `.guppi/guppi/sprint_close.py` over the same pages and asserts that they keep the same Decision pages.
- [x] update `rule-page-generation`
- [x] update `rule-decisions-schema`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/decisions/schema.yaml`
- [x] update `entity-glossary`
- [x] `uv run --project .guppi guppi glossary`
- [x] update `estimate-generate-cascades`
- [x] read `estimate-generate-cascades`
```

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

```then
update:
- slug: estimate-prespec-notes-a-page-the-cascade-archives
  set:
    status: pending
  change: the Criterion replaced whole — a superseded Decision page that a live page still names is not archived, by the keep judgment of generate
```

```tasks
- [x] `.guppi/guppi/prespec.py`: `cascade_notes` reads the kept Decision pages by the function of `.guppi/guppi/generate.py` over the live pages, drops each name in `deferred_by` of a page that a decision line of the Case carrying the mark names, and passes the set to `archived_by_cascade`; the docstring of `cascade_notes` and the paragraph of the module on it say so.
- [x] `.guppi/tests/test_prespec.py`: a mark on a Decision page that a live page names in `deferred_by` or `addressed_by` gives no note for an `update` of that page; the same mark gives the note when the Case of the mark names the page that carries the `deferred_by`.
- [x] update `estimate-prespec-notes-a-page-the-cascade-archives`
- [x] read `estimate-prespec-notes-a-page-the-cascade-archives`
```

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

```then
update:
- slug: estimate-close-reports-the-run
  change: the defer of decision-case-971, archived as superseded, retired; the reading waits for its event
- slug: estimate-handoff-dispatches
  change: the defer of decision-case-976, archived as superseded, retired; the reading waits for its event
```

```tasks
- [x] update `estimate-close-reports-the-run`
- [x] update `estimate-handoff-dispatches`
```

## Case 983 — The backlog check passes the put-offs of the running session

> **context:**
> `guppi backlog` writes `vault/wiki/backlog.md`, and each line of it carries the number of sessions whose Frontier put the item off. `put_off_count` in `.guppi/guppi/backlog.py` counts the `[-]` lines of every `frontier.md` under `vault/raw/` and `vault/archive/`, read once by `sessions_of` through `frontiers` and `frontier_marks` of `.guppi/guppi/generate.py`; the Frontier of the running session is among them. The librarian writes the file after the session, but `guppi backlog --check` (the branch `if args.check` of `run`) renders in memory from the same sources and compares. So a session that puts off an item already on the list sees `backlog: vault/wiki/backlog.md differs from its sources` in its Work Mode Baseline until its librarian's run. The handoff of session 0141 found this cause on a copy of commit `cdfeb988`: exit 0 without the Frontier of session 2307, exit 1 with it, the difference being the three counts the librarian of 2307 then wrote. Retro takes such a red as red before the work (`rule-retro`), so it is noise, not debt; the brief of 0141 reports that its closing `guppi check` printed 13 lines and no `backlog.md differs from its sources` line. The person chose that the check accepts the file in either of two forms: the render with every Frontier, or the render without the Frontier of the newest session, the first entry of `frontiers`, which sorts newest first. A check step gets no session stamp: `run` of `.guppi/guppi/check.py` starts each step with no stdin and only `CLAUDE_PROJECT_DIR` added to the environment, so the newest Frontier stands for the running session, whose `frontier.md` `/hi` writes before any Baseline. The writer does not change, so the Criterion of `estimate-backlog-renders`, which speaks of the count the writer puts in the file, stands; the Criterion of `estimate-backlog-checks-the-file` says the check prints when the file differs from the render of its sources, which this change makes false, so the Case replaces it, and its `purpose`, which states the old promise. The Frontier is still read once, by `frontier_marks`; the second render drops the newest entry of the list `sessions_of` returns, so no second reader of a Frontier line is written (`rule-one-judgment-one-implementation`). A Grep of `backlog --check|backlog.md differs|differs from (the render of )?its sources` over `vault/wiki/`, `.claude/`, `.guppi/guppi/` and `.guppi/tests/` printed `rule-lint.md`, `rule-harness.md`, `rule-backlog.md`, `estimate-backlog-checks-the-file.md`, `estimate-clean-branch-writes-the-session-files.md`, `estimate-harness-pipeline.md`, `estimate-lint-runs-every-step.md`, `estimate-retro-red-in-the-baseline-is-not-charged.md`, `log.md`, `brief.md`, `backlog.py`, `test_backlog.py` and `test_check.py`. `rule-lint`, `estimate-lint-runs-every-step` and `test_check.py` name only the order of the steps; `estimate-harness-pipeline` and `estimate-clean-branch-writes-the-session-files` want the check to exit 0 on a committed tree or a clean version, which a check that accepts more still does; the hit of `rule-harness` is a History line and that of `estimate-retro-red-in-the-baseline-is-not-charged` a Result, and the hits of `log.md` and `brief.md` are not read. The two tests of `--check` that expect exit 1 write a file by hand or none, which matches neither render, so they stand. In `.guppi/links.md`, the block of `rule-backlog` names `estimate-backlog-checks-the-file`, `estimate-backlog-renders`, `rule-one-judgment-one-implementation`, `rule-sprint-close`, `rule-case-protocol` and the skills and the agent that run the command; none of them states what the check accepts. The blocks of `.guppi/guppi/backlog.py` and `.guppi/tests/test_backlog.py` name only `rule-backlog` and `entity-guppi`. The session's ledger holds no `error` lesson.

> **problem:**
> `guppi backlog --check` goes red in the Baseline of any session that puts off an item already on the list, though only the librarian's run of that session can write the new count, so every such session explains the same red again.

> **recommend:**
> - **What should the check do with the put-offs of the session that is running**
>   - Recommended: (b) the check accepts the file in either of two forms: the render with every Frontier, or the render without the Frontier of the newest session; the writer does not change.
>   - Answer: agreed, (b).

> **given:**
> `rule-backlog`: the rule of the backlog file, whose Purpose says what the check compares.
> **＋** `estimate-backlog-checks-the-file`: the check of `--check`, whose Criterion is replaced whole.
> **＋** `.guppi/guppi/backlog.py`: the writer and the check of the file.
> **＋** `.guppi/tests/test_backlog.py`: the tests of the writer and the check.
> **＋** `.guppi/guppi/generate.py`: `frontiers` and `frontier_marks`, the one reader of the Frontier files, read only.
> **＋** `rule-one-judgment-one-implementation`: one reader of a Frontier line.
> **＋** `vault/wiki/backlog.md`: the file the check compares.

> **when:**
> Someone runs `uv run --project .guppi guppi backlog --check`, by hand or through `uv run --project .guppi guppi check`, over `vault/wiki/backlog.md` and the `frontier.md` files that `frontiers` of `.guppi/guppi/generate.py` finds.

> **then:**
> The check renders the file in memory once with every Frontier file and once without the Frontier file of the newest session, the first in the order of `frontiers` of `.guppi/guppi/generate.py`.
> **＋** When `vault/wiki/backlog.md` equals either render, the check is silent and exits 0.
> **＋** When it equals neither, the check prints one line on stdout that names the file and exits 1.
> **＋** `uv run --project .guppi guppi backlog` without `--check` writes the render with every Frontier file.
> **＋** `uv run --project .guppi guppi check` runs it after `sprint --check` and before `glossary --check`.
> **－** The check writes no file in either case.
> **－** `uv run --project .guppi guppi check` writes nothing to the tree.
> **－** The check reads each Frontier file once, by `frontier_marks` of `.guppi/guppi/generate.py`.

```then
update:
- slug: rule-backlog
  replace:
  - old: '`guppi backlog --check` renders in memory and names the file when it differs, and `uv run --project .guppi guppi check` runs it.'
    new: '`guppi backlog --check` renders in memory and names the file when it differs from the render with every Frontier and from the render without the Frontier of the newest session, since the put-offs of the running session enter the file only at the librarian''s run (as set in case 983). `uv run --project .guppi guppi check` runs it.'
  change: the check accepts the file without the put-offs of the newest session
- slug: estimate-backlog-checks-the-file
  set:
    status: pending
    purpose: guppi backlog --check names backlog.md when it differs from the render with every Frontier and from the render without the Frontier of the newest session, exit 1, and writes nothing
    method: uv run --project .guppi pytest .guppi/tests/test_backlog.py
  change: the Criterion replaced whole — the check accepts the file without the put-offs of the newest session
```

```tasks
- [x] update `rule-backlog`
- [x] update `estimate-backlog-checks-the-file`
- [x] `.guppi/guppi/backlog.py`: `render` takes the list of sessions as an argument; the branch `--check` of `run` reads `sessions_of` once and passes when the file equals the render of that list or of that list without its first entry; the docstring says so.
- [x] `.guppi/tests/test_backlog.py`: `--check` is silent on a file written before the newest session put an item off, red when the put-off of an older session is missing from the file, and reads each Frontier once by `frontier_marks`.
- [x] read `estimate-backlog-checks-the-file`
```

## Case 984 — A change that keeps a check's answer makes no related Case

> **context:**
> When the main agent starts `case-guppi` for a Frontier item, its prompt names each related Case of the session by its id, one sentence on what it sets and which pages it changes, and the path of its case file, as `## Who builds a Case` of the Render of `rule-orchestration` sets it. Since case 938 a Case is related when it sets the form of a text a check reads, or how the check reads it, where the Case of the item may write text of that kind. `estimate-orchestration-names-related-cases-in-the-dispatch` failed at the Retro of session 0141 (line 14 of `vault/raw/2026-11-01/0141/ledger.md`): the reading counted Case 977 as related to every later item, since it changed how `check_bare_links` of `/pre-spec` reads the prose of the plan, and the prompts of Cases 980 and 981 named it without its path, the second without its sentence. The main agent had judged Case 977 not related (the `context` of `vault/raw/2026-11-01/0141/cases/case-980.md`), and the `context` of `vault/raw/2026-11-01/0141/cases/case-977.md` says its change keeps the answer of that check on every input but a `[[schema]]` with a `schema.md` in a category folder, which no page holds. The handoff of session 0141 says that under a narrower reading of related the prompts of 980 and 981 would pass. The person chose to narrow the term: a Case whose change to a check leaves the answer of that check the same on each text the Case of the item may write is not related by that change, since what a builder needs to know is a check that may answer otherwise on its own text. The Render gains that limit by one `replace` pair, `vault/wiki/orchestration.md` changes at the librarian's render, and the Estimate gets a Criterion replaced whole with one more `－` line, its `purpose` set anew since it states the old promise, and a `method` that waits for the librarian's render of the new Render into `vault/wiki/orchestration.md` and then reads the prompts of the first session that runs on it, at its Retro. A finding of `/pre-spec` showed that a reading at the Retro of this session would read prompts written under the old text, since the new text lands only at the librarian's render after this session; the person chose to read it in the first session after the render. The method opens with `by hand, after` and names that event before a colon, so Retro leaves the Estimate `pending` until the event, as `case-schema.md` sets it (case 781). The schema of the rules, in `vault/wiki/rules/schema.yaml`, lets a rule of the agent's own conduct have its text in the context as its guard; the person chose no hook on the prompt, which the documentation of Claude Code hooks (https://code.claude.com/docs/en/hooks) says could block an `Agent` call and read its `prompt`. `rule-estimates-schema` keeps a `failed` Estimate as debt until a person decides; this Case is that decision. A Grep `may write text of that kind` over `vault/wiki/` printed `rules/rule-orchestration.md` (the Render and a History line), `orchestration.md`, `log.md` and `estimates/estimate-orchestration-names-related-cases-in-the-dispatch.md`; the Render line enters the Case by its pair, the rendered file follows the render, and the Estimate is replaced whole. A Grep `judges related` over `.claude/` printed `.claude/agents/case-guppi.md`, whose frame says the main agent judges which Cases are related; it stands, since the judgment stays with the main agent. In `.guppi/links.md` the block of `rule-orchestration` names `rule-case-build` and `entity-glossary` among its neighbours; a Grep `related` over `vault/wiki/glossary.md` printed nothing, so no row defines the term. `.guppi/tests/test_orchestration.py` reads the live `orchestration.md`, but only its blocks tagged `showing` and `defer`, which this Case does not change. The session's ledger holds no `lesson[error]` line, so no `addresses` mark is written.

> **problem:**
> The check of the prompt failed again on a Case whose change to a check altered nothing a later Case could write, because the term related counts every change to how a check reads a text.

> **recommend:**
> - **What settles the failed check?**
>   - Recommended: (a) narrow what related means: a change to a check that keeps its answer on each text the Case of the item may write makes no related Case; the Criterion replaced and read again at the Retro of this session.
>   - Answer: agreed, (a).
> - **When is the narrowed check read?**
>   - Recommended: (a) at the Retro of the first session that runs on the new text, after the librarian's render.
>   - Answer: agreed, (a).

> **given:**
> `rule-orchestration`: its Render sets what the prompt of `case-guppi` names, rendered into `vault/wiki/orchestration.md`.
> **＋** `estimate-orchestration-names-related-cases-in-the-dispatch`: its Criterion is replaced whole.
> **＋** `case-guppi`: the agent the prompt starts.
> **＋** `raw/<date>/<hi HHMM>/frontier.md` and `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the item and the case files the prompt names.
> **＋** `~/.claude/projects/`: the folder of the transcript of the session.

> **when:**
> The main agent dispatches `case-guppi` by an `Agent` call to build the Case of an item of `raw/<date>/<hi HHMM>/frontier.md`, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The prompt of the call names each Case of the session, ratified or already shown, that changes a page the item names or sets what happens at the same moment as the item: the same kind of reply, the same hook event or the same command.
> **＋** The prompt also names each Case of the session, ratified or already shown, that sets the form of a text a check reads, or how the check reads it, when the Case of the item may write text of that kind, such as the `method` of an Estimate.
> **＋** Each such Case stands in the prompt by its id, one sentence on what it sets and which pages it changes, and the path of its case file `raw/<date>/<hi HHMM>/cases/case-<N>.md`.
> **＋** When the item is one of two or more items that one answer of the person took up, the prompt also names each other Case of that batch by its id and its Frontier item, and by the path of its case file where that file stands.
> **＋** The main agent judges which Cases of the session are related, and the prompt does not send `case-guppi` to search the Cases of the session.
> **－** A Case of the session that changes no page the item names, acts at another moment, sets no form of a text of a kind the Case of the item may write and is no Case of the same batch need not stand in the prompt.
> **－** A Case that only writes a text a check reads, and sets no form of it, is not related by that text alone.
> **－** A Case whose change to a check leaves the answer of that check the same on each text the Case of the item may write is not related by that change.
> **－** When no Case of the session is related and the item is taken up alone, the prompt names none and holds the Case id, the Frontier item with its source and the person's words.

```then
update:
- slug: rule-orchestration
  replace:
  - old: where the Case of the item may write text of that kind, such as the `method` of an Estimate that `uv run --project .guppi guppi check` reads, by its id
    new: where the Case of the item may write text of that kind and the change may alter what the check answers on such text, such as the `method` of an Estimate that `uv run --project .guppi guppi check` reads, by its id
  change: a Case whose change to a check keeps the answer of that check on each text the Case of the item may write is not related by that change
- slug: estimate-orchestration-names-related-cases-in-the-dispatch
  set:
    status: pending
    purpose: Whether the main agent's prompt to case-guppi names each Case of the session that changes a page the item names, acts at the same moment, or sets the form of a text a check reads, or how the check reads it, where the Case of the item may write text of that kind and the change may alter what the check answers on it, by its id, one sentence on what it sets and which pages it changes, and the path of its case file, and each other Case of a batch of items the person took up in one answer
    method: 'by hand, after the librarian''s render of this Criterion''s rule text into vault/wiki/orchestration.md: at the Retro of the first session that runs on that render, each Agent call of that session that dispatched case-guppi for the Case of an item, read in the transcript of the session under ~/.claude/projects/ against the Criterion, only the Cases the Criterion counts as related judged and a Case named beyond them not counted, a related Case left unnamed or named without its sentence, the pages it changes or the path of its case file counted in the reading line and the transcript named (the first session after 2026-11-01/1721)'
  change: the Criterion replaced whole — a change to a check that keeps its answer on each text the Case of the item may write makes no related Case; purpose and method set anew, the reading after the render
```

```tasks
- [x] update `rule-orchestration`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
- [x] update `estimate-orchestration-names-related-cases-in-the-dispatch`
- [x] read `estimate-orchestration-names-related-cases-in-the-dispatch`
```

## Case 985 — The builder follows a changed step into the harness code

> **context:**
> When a Case changes what a step writes, copies or shows, `case-guppi` must find each other text that reads that output or does the same step. The rule sends it to Grep `vault/wiki/rules/` and `.claude/` only. The reading of `estimate-case-build-reads-the-readers-of-a-changed-step` failed for the third time (ledger of session 0141, line 18): Case 972 of session 2307 changed the wait check of pre-spec for a `method` the plan writes and missed the `method` an Estimate page keeps when an `update` replaces its Criterion whole. Both inputs are judged in the `update` loop of `plan_findings` in `.guppi/guppi/prespec.py`: a `method` under `set` by `waits_for_another_session`, and with none, the kept one by `kept_method_waits`, which reads it by `kept_method`; I read that loop and both functions whole. The note of that build lists those lines of `prespec.py` among its reads, so the place was in the code, which the Grep the rule sets does not reach. The two earlier failures (sessions 2005 and 0431) missed a text of another kind each, and Cases 948 and 966 added a sentence each. The person chose to widen the rule into `.guppi/guppi/`. The new clause goes into the sentence on a changed step of the Render of `rule-case-build`, and the Criterion of the Estimate is replaced whole to match; its `When` line and its last `Then` line are rewritten on purpose, the first to name a function of `.guppi/guppi/` among the doers of a step, the second to name a place of code among what enters the Case; its `purpose` and `method` are set anew, since the `method` waited for the session of the Render of Case 966, which has passed. The rule that governs the option is `rule-case-build` itself; the new clause is consistent with `rule-one-judgment-one-implementation`, a neighbour of `rule-case-build` in `.guppi/links.md`, since it only reads the places of one judgment. A Grep `does the same step|same step|readers-of-a-changed-step` over `vault/wiki/`, `.claude/` and `.guppi/guppi/` printed `brief.md`, `.claude/agents/case-guppi.md`, `log.md`, the Estimate, `rule-case-build` and `insight-case-build-changes-a-step-without-reading-its-readers`; the insight is `actioned` and its proposal still holds, and `brief.md` and `log.md` are not read. A Grep `case-guppi\.md|rule-case-build` over `.guppi/tests/` printed `test_guppi_package.py`, whose tests over every file of `.claude/` refuse the old commands and the paths `guppi/` and `tests/` at the start of a path, which the new `.guppi/guppi/` is not, by `reword_pattern` of `.guppi/guppi/generate.py`. The block of `.claude/agents/case-guppi.md` in `.guppi/links.md` names no neighbour that this clause makes false. Frontier item C2 also changes the Render of `rule-case-build`, in the sentence on `.guppi/links.md`; this Case leaves that sentence alone. The session's ledger holds no `error` lesson.

> **problem:**
> The search that finds the readers of a changed step does not reach the harness code, so a step done by a function there is changed on one input and missed on another.

> **recommend:**
> - **What changes after the third failed reading**
>   - Recommended: (a) the rule follows a step into the harness code.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build`: its Render holds the sentence on the readers of a changed step.
> **＋** `.claude/agents/case-guppi.md`: rendered from `rule-case-build`.
> **＋** `estimate-case-build-reads-the-readers-of-a-changed-step`: its Criterion is replaced whole.
> **＋** `vault/wiki/rules/`: the Rule pages the builder searches for the readers of a step.
> **＋** `.claude/`: the harness files the builder searches for the readers of a step.
> **＋** `.guppi/guppi/`: the harness code the builder now searches too.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case that changes what a step of a skill, an agent, a hook or a function of `.guppi/guppi/` writes, copies or shows, or adds a path on which a step does so, and is about to answer with its summary.

> **then:**
> It searches `vault/wiki/rules/` and `.claude/` for the name of that output — a line such as `Branch:`, a file or a list — and for the name of the step.
> **＋** Where a function of `.guppi/guppi/` does the step, it also searches `.guppi/guppi/` for the name of that function and of the function it judges by.
> **＋** It reads each step and skill that reads that output or does the same step, the steps after it in the same text and the new path its own Case adds included.
> **＋** Where a function of `.guppi/guppi/` does the step, it reads each place that calls that function or the function it judges by, and each other place that makes the same judgment on another input, such as the value a plan writes and the value a live page keeps.
> **＋** Each step, skill or place of code that the change makes false enters the Case, or the `context` of the Case names it and says why it stands.
> **－** A hit in a History line, in `log.md` or in `brief.md` is not read.

```then
update:
- slug: rule-case-build
  replace:
  - old: the new path your Case adds and each agent, skill and hook the step leads to included; each one the change makes false enters the Case, or `context` names it and says why it stands (as set in cases 924 and 966).
    new: the new path your Case adds and each agent, skill and hook the step leads to included; where a function of `.guppi/guppi/` does the step, such as a check, Grep `.guppi/guppi/` too for the name of that function and of the function it judges by, and read each place that calls them and each other place that makes the same judgment on another input, such as the value a plan writes and the value a live page keeps; each one the change makes false enters the Case, or `context` names it and says why it stands (as set in cases 924, 966 and 985).
  change: the readers of a changed step include the places of the harness code that call the function of the step or make its judgment on another input
- slug: estimate-case-build-reads-the-readers-of-a-changed-step
  set:
    status: pending
    purpose: Whether case-guppi, when its Case changes what a step writes, copies or shows or adds a path to it, reads each step and skill that reads that output or does the same step, the steps after it and the new path included, and, where a function of .guppi/guppi/ does the step, each place that calls it or makes the same judgment on another input, and names each one in context or enters it in the Case
    method: 'by hand, after the /pre-spec of the first session whose case-guppi runs on the Render of rule-case-build that holds the sentence on following a step into the code of .guppi/guppi/: the findings of ask-guppi at that /pre-spec, read in the agent transcript of that ask-guppi under ~/.claude/projects/, for a Case that changes a step and misses a step, a skill or a place of code that reads its output or does the same step, the count and the transcript in the estimate line'
  change: the Criterion replaced whole — the readers of a changed step include the places of the harness code; pending again after the failed reading of session 0141
```

```tasks
- [x] update `rule-case-build`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [x] update `estimate-case-build-reads-the-readers-of-a-changed-step`
- [x] read `estimate-case-build-reads-the-readers-of-a-changed-step`
```

## Case 986 — The builder reads the whole block of each page it changes, again at the final check

> **context:**
> At the start of each session a hook writes `.guppi/links.md`, the graph of the links between the pages and the harness files: one block per page and per file, each neighbour with its purpose line. The Render of `rule-case-build` tells `case-guppi` to find the block of each page and file its Case changes by a Grep with lines of context, while it reads the frame, and to say in `context` where the file holds no block. The reading of `estimate-case-build-reads-the-link-graph-of-what-it-changes` failed in session 0141: 2 of 4 Cases of session 2307 found the block of each existing page and file they change, and no `context` said that a page it creates has no block. In the transcripts under `~/.claude/projects/c--PROJECTS-GUPPI/8d8876d7-f627-4f65-95f7-cb7b7172cd46/subagents/`, a Grep with the pattern `"pattern":"[^"]*","path":"[^"]*links\.md"` showed that each build searched the file with one pattern of the pages it had in mind early in the build (Case 972 at line 142 of `agent-ab08bcaa476ca5d9f.jsonl`, Case 975 at line 82 of `agent-aa121a9ddfe7235f9.jsonl`), and the pages and files it missed were not in that pattern. The handoff of session 0141 also notes that a Grep with `-A 40` printed part of the 96-line block of `rule-case-build`. The person chose to read the blocks again at the check of the finished Case, for each page and file the tasks change whose block was not read; to read each block whole, from its heading to the next heading; to expect no block of a page or file the Case creates and say nothing of it; and to replace the Criterion of the Estimate whole, with its `purpose` and `method` set anew. The rule that governs the options is `rule-case-build` itself, and `case-schema.md`, by which a promise changes only by a Criterion replaced whole; a Criterion kept would still demand a line on a created page. Four lines of the old Criterion are rewritten on purpose: the `When` line now covers the whole build up to the summary, since the reading moves to the final check too; the first `Then` line now names only a page or file that exists before the Case and reads the block whole from its line; the line on judging the neighbours now speaks of each block, since a build reads more than one; and the `－` line on a missing block now names only a page or file that exists before the Case, with a second `－` line for a created one. The Purpose of `rule-link-graph-at-session-start` says the builder reads a block by a Grep, which the Read of the whole block makes partly false, so it gets a pair. A Grep `links\.md|link graph|graph of the links` over `vault/wiki/` printed `brief.md`, `entity-guppi.md`, `estimate-case-build-reads-the-link-graph-of-what-it-changes.md`, `log.md`, `rule-case-build.md`, `rule-harness.md`, `rule-link-graph-at-session-start.md` and `estimate-link-graph-at-session-start-writes-the-file.md`; `brief.md` and `log.md` are not read, `entity-guppi` and `rule-harness` name the graph as a part of GUPPI and a hook of the harness and stand, and the Criterion of `estimate-link-graph-at-session-start-writes-the-file` speaks of how the file is written, not read, and stands. A Grep `links\.md` over `.claude/` printed `.claude/agents/case-guppi.md`, which the render changes. The blocks of `rule-case-build`, `.claude/agents/case-guppi.md`, the Estimate and `rule-link-graph-at-session-start` in `.guppi/links.md` were read whole; no neighbour is made false: `entity-link-graph` says the reader opens only the neighbours that bear on its question, which still holds, and the Estimates of `rule-case-build` other than this one speak of other steps. `estimate-case-build-checks-the-finished-case` lists the searches of the final check and not this one; it stands, since this Estimate checks the new reading at that check, and nothing is signed twice. `estimate-case-build-reads-by-need-and-in-parts` stands: a block read whole by a Read with `offset` is a part of a file read in parts. A Grep `case-guppi\.md|rule-case-build` over `.guppi/tests/` printed `test_guppi_package.py`, whose tests refuse the old commands and a path that starts with `guppi/` or `tests/`, by `reword_pattern` of `.guppi/guppi/generate.py`, which I read whole; the new texts hold no such command or path. Case 985 of this session changes the sentence on a changed step in the same paragraph of the Render as the new sentence of the final check; the pairs touch different sentences and say nothing against each other. The session's ledger holds no `error` lesson.

> **problem:**
> The builder reads the graph of links once, early, so a page or file added to the Case later is never looked up, a long block is cut short, and a created page is held to a duty it cannot meet.

> **recommend:**
> - **When does the builder read the blocks?**
>   - Recommended: (a) again at the final check, for each page and file the tasks change whose block was not read.
>   - Answer: agreed, (a).
> - **What about a page or file the Case creates?**
>   - Recommended: (a) no block expected, nothing said.
>   - Answer: agreed, (a).
> - **How does the builder read a long block whole?**
>   - Recommended: (a) find the line, then read to the next heading.
>   - Answer: agreed, (a).
> - **How is the change checked?**
>   - Recommended: (a) rewrite that check whole.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build`: its Render holds the sentence on `.guppi/links.md` and the check of the finished Case.
> **＋** `.claude/agents/case-guppi.md`: rendered from `rule-case-build`.
> **＋** `estimate-case-build-reads-the-link-graph-of-what-it-changes`: its Criterion is replaced whole.
> **＋** `rule-link-graph-at-session-start`: its Purpose says how the builder reads a block.
> **＋** `.guppi/links.md`: the graph of the links that the builder reads.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case and answers with its summary.

> **then:**
> For each page and file the Case changes that exists before the Case, it finds the line `## <slug or path>` of its block in `.guppi/links.md` by a Grep with the line number, and reads the block whole, from that line to the next line that opens with `## `.
> **＋** At the check of the finished Case, it lists each page and file that the tasks of the Case change, and reads the block of each one whose block it has not read in that build.
> **＋** From each block it judges, by what each neighbour is for, which neighbours bear on the change.
> **＋** It opens each neighbour whose purpose line bears on the change, whole or in parts as the Render sets for its kind of text.
> **＋** Each neighbour that the change makes false enters the Case, or the `context` of the Case names it and says why it stands.
> **－** Where `.guppi/links.md` is missing or holds no block of a page or file that exists before the Case, the `context` of the Case says so.
> **－** A page or file the Case creates has no block, and the `context` of the Case says nothing of it.

```then
update:
- slug: rule-case-build
  replace:
  - old: Read too, for each page and file the Case changes, its block in `.guppi/links.md`
    new: Read too, for each page and file the Case changes that exists before the Case, its block in `.guppi/links.md`
  - old: find it by a Grep for its line `## <slug or path>` with lines of context, read the purpose line
    new: find its line `## <slug or path>` by a Grep with its line number, read the block whole by a Read from that line to the next line that opens with `## `, and read on where the block goes past the limit of that Read; read the purpose line
  - old: and where the file is missing or holds no block of that page or file, `context` says so (as set in case 967.2).
    new: and where the file is missing or holds no block of such a page or file, `context` says so; a page or file the Case creates has no block yet, and `context` says nothing of it (as set in cases 967.2 and 986).
  - old: For a fact that no slug marks, read the index lines of the recipe of `.claude/agents/ask-guppi.md` and judge them by meaning.
    new: For a fact that no slug marks, read the index lines of the recipe of `.claude/agents/ask-guppi.md` and judge them by meaning. List each page and file that the tasks of the Case change, and read the block in `.guppi/links.md` of each one that exists before the Case and whose block you have not read in this build, as the paragraph on the frame of the Case sets it (as set in case 986).
  change: the builder reads the whole block of each existing page and file it changes, again at the check of the finished Case, and says nothing of a page it creates
- slug: rule-link-graph-at-session-start
  replace:
  - old: the builder reads the block of each page and file its Case changes by a Grep.
    new: the builder finds the block of each page and file its Case changes by a Grep and reads it whole.
  change: the builder finds a block by a Grep and reads it whole
- slug: estimate-case-build-reads-the-link-graph-of-what-it-changes
  set:
    status: pending
    purpose: Whether case-guppi reads whole, for each page and file its Case changes that exists before the Case, its block in .guppi/links.md, again at the check of the finished Case for each one whose block it has not read, opens each neighbour whose purpose line bears on the change, and says nothing of a page it creates
    method: 'by hand, after the /pre-spec of the first session whose case-guppi runs on the Render of rule-case-build that holds the sentence on reading the block of .guppi/links.md again at the check of the finished Case: the agent transcript of each case-guppi of that session under ~/.claude/projects/, for each Case, whether a Grep of .guppi/links.md and a Read from its line cover the whole block of each existing page and file the tasks of the Case change, and whether each neighbour that bears on the change is opened or named in context; the count and the transcripts in the estimate line'
  change: the Criterion replaced whole — the block read whole, again at the final check, and no word on a created page; pending again after the failed reading of session 0141
```

```tasks
- [x] update `rule-case-build`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [x] update `rule-link-graph-at-session-start`
- [x] update `estimate-case-build-reads-the-link-graph-of-what-it-changes`
- [x] read `estimate-case-build-reads-the-link-graph-of-what-it-changes`
```

## Case 987 — The person approves a long Spec in the CLI by typing /approve-spec

> **context:**
> At the end of Plan Mode the main agent calls `ExitPlanMode`, and Claude Code shows the plan file for approval. GUPPI writes each ratified Case whole into that file. The Claude Code CLI shows a plan whole before it offers approval, and for a plan above the size it can show it offers none: the person can only press Esc or ask for a shorter plan. `lesson-plugin-cli-withholds-approval-of-a-long-plan` records this for a plan file of 15347 bytes in install A of session 2026-10-29/0327, and `lesson-plugin-cli-withholds-approval-in-every-window` records the same refusal in an empty folder with no GUPPI, in two windows of different size, while the VS Code extension approved a larger plan. The Spec capture, `guppi spec` on `PostToolUse` of `ExitPlanMode` in `.guppi/guppi/spec.py`, runs only after that approval, so in the CLI a Spec of a few Cases never reaches `spec.md` and Work Mode never starts. `insight-plugin-cli-withholds-approval-of-a-long-plan` is `open` and carries `deferred_by: decision-case-957`, whose Problem reads: "No Case of this session decides how GUPPI lets a long Spec be approved in the Claude Code CLI"; Case 957 put the item off to wait for a fix from Anthropic. The changelog of Claude Code read by `WebFetch` at https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md, its first 100 000 characters, versions 2.1.301 to 2.1.316, names no fix of this refusal; the rest of the file was not read. The page https://code.claude.com/docs/en/permission-modes says that Shift+Tab leaves plan mode without approving a plan, and states no size limit of a plan. The page https://code.claude.com/docs/en/hooks says that `UserPromptSubmit` receives a skill the person typed as the line typed, with `permission_mode` among its fields, one of whose values is `plan`, and that a hook that blocks the prompt stops the command. The page https://code.claude.com/docs/en/skills says that with `disable-model-invocation: true` Claude cannot invoke a skill on its own while the person can still type it.
>
> The person chose a typed approval: where the CLI withholds the approval, the person presses Esc, leaves Plan Mode with Shift+Tab and types `/approve-spec`. Case 987.1 adds the skill `/approve-spec` and a hook on `UserPromptSubmit`, `uv run --project .guppi guppi spec --typed`, which takes the plan file into `spec.md` as an approval does and gives the agent the same line. It refuses the prompt in Plan Mode, so that Work Mode can edit, and, before `/pre-spec` or while the check of the plan finds a finding, by the judgment the hook of `rule-prespec-hook` runs at `ExitPlanMode`. One page owns each part: the hook is code of `.guppi/guppi/spec.py`, so `rule-spec-capture`, whose `implementation_ref` names that file, owns it and its new text states the typed path whole; the new rule `rule-skill-approve-spec` owns only the text of the skill, and its Purpose and Render point to the hook of `rule-spec-capture`, with no `implementation_ref`. Its Estimate, `estimate-skill-approve-spec-takes-the-spec`, checks the command as the person meets it, skill and hook together, which is what that rule prevents. The skill takes `disable-model-invocation: true`, so the approval stays the person's. Case 987.2 has the main agent name that way. The person first chose that the agent names it after its call of `ExitPlanMode` is refused with no words, but the documentation shows the agent gets no reply at that moment: https://code.claude.com/docs/en/interactive-mode says "On a permission prompt, `Esc` declines the action, the same as **No** without a comment", and https://code.claude.com/docs/en/permissions says "If you select **No** without a comment on a prompt from the main conversation, Claude Code stops the turn". The agent also cannot tell a person who refused from a CLI that offered no approval. So, by the person's answer to a later round, the reply that calls `ExitPlanMode` holds, before the call, one line worded as a condition, which claims nothing the agent cannot know, as `rule-agent-writing` and `CLAUDE.md` ask ("Name a real source or remove the claim"). At `/pre-spec` the person agreed that the trials in the CLI wait for the librarian's run after this session, since the skill, its hook in `.claude/settings.json` and the new sentence of `orchestration.md` are rendered only then; the by-hand part of each method opens with `after` and that event, and only the test of 987.1 is read in this session. Case 989 of this session moves its trial of `/box` to the same moment. The README note of Case 957 is left to the item of `entity-sprint-plugin` that writes the README. Case 987.1 sets the insight `actioned` and carries `{supersedes:case 957}`, so that `generate` clears its defer. A Glob `vault/**/*approve*` printed only `estimate-spec-write-reaches-the-approved-spec.md`, so the new slugs are free; both `create` lines carry a `ref`.
>
> One judgment, one implementation: a Grep of `.guppi/guppi/` for `get\("prompt"\)|\["prompt"\]` printed `event.py` and `sprint.py`, which read a typed `/hi` by `is_hi_prompt` of `.guppi/guppi/event.py`, and `gate.py`, whose `skill_of` reads the first word of a typed prompt. I read `is_hi_prompt`, `hi_refusal` and `skill_of` whole: on a command alone, a command with arguments after a space, and a prompt with spaces around it, both answer alike, and both refuse a command followed by a tab or a line break. So 987.1 moves the body of `is_hi_prompt` into one function for a named command, which `is_hi_prompt` and `spec --typed` call, and reads Plan Mode by `PLAN_MODE` of `event.py`, the value `hi_refusal` reads. The gate is `gate` of `.guppi/guppi/prespec.py`, which I read whole with `window`, `prespec_mark` and `plan_findings`: its judgment moves into one function that returns the reason or nothing, which `gate` prints as before and `spec --typed` calls; `plan_path` of `.guppi/guppi/ledger.py` finds the plan file for both.
>
> The frame. A Grep for `ExitPlanMode` over `.claude/` printed `skills/box/SKILL.md`, `skills/work/SKILL.md`, `skills/carry/SKILL.md` and `settings.json`, and over `vault/wiki/rules/` printed `rule-prespec-hook`, `rule-hook-registry`, `rule-work-mode`, `rule-spec-box`, `rule-orchestration`, `rule-spec-capture`, `rule-carry-over` and `rule-session`. The renders of `rule-work-mode`, `rule-carry-over` and `rule-spec-box` say their skill follows the line printed after `ExitPlanMode`, which the typed path makes false, so 987.1 rewords them. I read whole each sentence those pairs touch: the description of the skill `/work`, which also says the person types it to resume and `/box` calls it with a conserved Spec; its Purpose sentence on when `/work` starts; the description and the opening sentence of `/carry`; and the description of `/box` and its sentence on its argument. Each stays true with the new words. Of the other Cases of this session, only Case 989 changes one of these pages: it changes the last sentence of the Purpose of `rule-spec-box`, on where the second part of `/box` is noted, and I read its finished file whole. The sentences differ, so the pairs do not meet. `rule-spec-capture` says the file has three writers, the hook on `ExitPlanMode` among them, and gains the typed path. `rule-prespec-hook` and `rule-session` say the hook on `ExitPlanMode` refuses an exit before `/pre-spec`, which stays true. `rule-hook-registry` gains the new command. `rule-orchestration` is 987.2: I read whole the sentence of its Render that its pair ends, which says that in a working session the rules of the harness come before the Plan Mode instructions of Claude Code, that the agent asks by a plain question and never by a picker tool, and that it calls `ExitPlanMode` only after `/pre-spec`. The new sentence after it agrees with each part. Case 984 of this session, whose finished file I read whole, changes another sentence of that Render, under `## Who builds a Case`, on which Cases the prompt of `case-guppi` names as related, and its Estimate; the pair of 987.2 stands under `## Plan Mode and the Frontier`, so the two pairs do not meet, and neither text speaks of the other's moment. The `.guppi/links.md` blocks of `rule-spec-capture`, `rule-hook-registry`, `rule-work-mode`, `rule-carry-over`, `rule-spec-box`, `rule-orchestration`, the insight, `.guppi/guppi/spec.py` and `.claude/settings.json` name no other neighbour that the change makes false. The glossary row of Spec says it is approved as Claude Code's plan, which stands, since `/approve-spec` takes the same plan file. `onward --plan` of `.guppi/guppi/onward.py`, whose docstring I read, sends the agent on toward `ExitPlanMode` after `/pre-spec`, after a reply with a `LEDGER` block or after a reply the ledger hook sent back (case 696.2); the reply that then calls `ExitPlanMode` carries the line of 987.2 as any such reply does, so the hook needs no change. `estimate-orchestration-puts-the-harness-before-plan-mode` stands: its Then says the agent calls `ExitPlanMode` only after `/pre-spec` has run and asks by no picker in Plan Mode, and the line of 987.2 is a plain line of the reply that keeps both. `estimate-skill-sprint-open-starts-at-hi` judges a `/hi` by `is_hi_prompt` of `.guppi/guppi/event.py`, and `estimate-event-log-records` judges a `/hi` by its `permission_mode` and says that any other prompt is silent there; both stand, since `is_hi_prompt` keeps its answer on every input when its body moves into the shared function, and the event hook does not judge `/approve-spec`, which `spec --typed` judges. `estimate-hook-registry-rendered` stands: its Then says every hook the harness runs is registered by a line of the Render of `rule-hook-registry`, and 987.1 registers the new hook there. `estimate-prespec-hook-reports-a-pointer-outside-a-bracket` stands: its When names the judgment the hook runs at `ExitPlanMode`, and that judgment keeps its findings when `spec --typed` calls it too. The Criteria of `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-work-mode-takes-the-work-readings`, `estimate-carry-over-writes`, `estimate-spec-box-runs-a-conserved-spec`, `estimate-spec-capture-appends` and `estimate-spec-capture-offers-the-fork` speak of the path after `ExitPlanMode`, which still holds, and stand: the same line after `/approve-spec` is the promise of `estimate-skill-approve-spec-takes-the-spec`. `estimate-prespec-hook-gates` stands, since `gate` keeps its output.
>
> The new hook is one more member of the hooks of `UserPromptSubmit`. A Grep for the existing member `casecheck --prompt` over `vault/wiki/` printed `log.md`, `rules/rule-case-check.md`, `rules/rule-hook-registry.md` and three Estimates of the Case check; over `.claude/` it printed `settings.json`; over `.guppi/guppi/` it printed `casecheck.py` and `ledger.py`. Only the Render of `rule-hook-registry` and `settings.json` list the members; the hit in `rule-case-check` is a History line, and the others name that hook alone. The new skill file stands in `.claude/skills/`: a Grep of `.guppi/guppi/` for `\.claude/skills|skills/` printed `links.py`, `recall.py` and `ship.py`. `links.py` reads each skill of the folder into the graph, `recall.py` reads only the skill `/hi`, and `ship.py` writes the file of a Render of a page with `core: true`, so the new rule, `core: true`, ships its skill once it is no longer `draft`. No `.gitignore` stands under `.claude/`. A Grep of `.guppi/tests/` for `(REPO|ROOT|repo_root|PROJECT|parents\[\d\]).*(settings\.json|orchestration\.md|SKILL\.md|skills)` printed `test_guppi_package.py` and `test_orchestration.py`. The first checks that the command of each hook in its `HOOKS` stands in `settings.json`, and `spec` is not among them. The second reads the blocks tagged `showing` and `defer` of `orchestration.md`, which 987.2 does not touch. Both stand. The session's ledger holds no `error` lesson. Two lines of `then` share their words: in 987.1 the hook tells the person, when `/approve-spec` comes in Plan Mode, to leave it with Shift+Tab, and in 987.2 the reply that calls `ExitPlanMode` names Esc, Shift+Tab and `/approve-spec` before the call. They are two moments with two promises, so nothing is signed twice.

> **problem:**
> In the Claude Code CLI a Spec of a few Cases cannot be approved, so the session never reaches Work Mode, and GUPPI gives the person no other way to approve it.

> **recommend:**
> - **What GUPPI does when the CLI withholds the approval**
>   - Recommended: (c) approval by a typed command after leaving Plan Mode.
>   - Answer: agreed, (c).
> - **What the person types**
>   - Recommended: (a) `/approve`.
>   - Answer: the person's own name, `/approve-spec`.
> - **What the command checks before it takes the Spec**
>   - Recommended: (a) the same checks as the exit, through the same code, and the command refused while the session is still in Plan Mode.
>   - Answer: agreed, (a).
> - **How the person learns the way**
>   - Recommended: (a) the agent names the way after an exit refused with no words of the person.
>   - Answer: agreed, (a).
> - **How the Case is checked**
>   - Recommended: (a) a new Estimate, checked by a test of the hook and a by-hand trial in the CLI in this session's Work Mode.
>   - Answer: agreed, (a).
> - **What becomes of the insight and the README note**
>   - Recommended: (a) the insight closed as fixed by this Case, the README left to its item of the sprint.
>   - Answer: agreed, (a).
> - **How the agent's words after a refused exit are checked**
>   - Recommended: (a) a new Estimate, read in the record of the same CLI trial.
>   - Answer: agreed, (a).
> - **When the agent names the way**
>   - Recommended: (a) in the reply that calls `ExitPlanMode`, one line before the call, worded as a condition, since the documentation shows that after Esc at the dialog Claude Code stops the turn and the agent gets no reply.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec`, the person agreed that the trials in the CLI do not run in this session's Work Mode, since the skill `/approve-spec`, its hook in `.claude/settings.json` and the new sentence of `orchestration.md` exist only after the librarian's render after this session.
>   - Taken: the by-hand part of the method of each new Estimate waits for the librarian's run after this session; only the test of 987.1 is read in this session.

### Case 987.1 — /approve-spec takes the Spec where the CLI withholds the approval

> **given:**
> `rule-skill-approve-spec`: the new rule of the skill `/approve-spec`.
> **＋** `.claude/skills/approve-spec/SKILL.md`: the skill, rendered from that rule.
> **＋** `.guppi/guppi/spec.py`: the Spec capture, which gains the typed path.
> **＋** `.guppi/guppi/event.py`: the reading of a typed command and of Plan Mode.
> **＋** `.guppi/guppi/prespec.py`: the gate that the exit and the typed path share.
> **＋** `.guppi/tests/test_spec.py`: the tests of the Spec capture.
> **＋** `rule-spec-capture`: the writers of `raw/<hi date>/<hi HHMM>/spec.md`.
> **＋** `rule-hook-registry`: the hooks of `.claude/settings.json`.
> **＋** `rule-work-mode`, `rule-carry-over`, `rule-spec-box`: the rules of `/work`, `/carry` and `/box`, the skills that follow the line given after an approval.
> **＋** `/pre-spec` and `/hi`: the check of the plan, and the command that opens a working session.
> **＋** `insight-plugin-cli-withholds-approval-of-a-long-plan`: the insight this Case fixes.
> **＋** `estimate-skill-approve-spec-takes-the-spec`: the new check of `/approve-spec`.

> **when:**
> In a working session the person types `/approve-spec`, and `uv run --project .guppi guppi spec --typed` of `.guppi/guppi/spec.py` runs on `UserPromptSubmit`.

> **then:**
> Out of Plan Mode, after `/pre-spec`, with a plan file of the session that the check of the plan passes, the hook appends that plan file to `raw/<hi date>/<hi HHMM>/spec.md` under its stamp, once, as `rule-spec-capture` sets it for an approval by `ExitPlanMode`.
> **＋** The hook then gives the agent the line it gives after `ExitPlanMode`: the fork between `/work` and `/carry`, or the call of `/box` for a plan that names a conserved Spec.
> **＋** The skill `.claude/skills/approve-spec/SKILL.md` tells the agent to follow that line.
> **－** While the session is in Plan Mode, the hook blocks the prompt and tells the person to leave Plan Mode with Shift+Tab and type `/approve-spec` again.
> **－** Before `/pre-spec`, or while the check of the plan finds a finding, the hook blocks the prompt with the reason that `gate` of `.guppi/guppi/prespec.py` judges at `ExitPlanMode`, by the same function.
> **－** With no plan file of the session, or with no `/hi` of the session, the hook blocks the prompt and says why.
> **－** A blocked prompt leaves `spec.md` as it stands.
> **－** The agent cannot start `/approve-spec` itself.
> **－** Any other prompt passes the hook, and nothing is written.

```then
create:
- slug: rule-skill-approve-spec
  ref: rule-plan-mode
  type: rule
  kind: Leaf
  purpose: Prevents a Spec from staying unapproved where the Claude Code CLI withholds the approval of a plan longer than it can show
  enforcement: render
  governs: .claude/skills/approve-spec/SKILL.md
  render_mode: full
  core: true
  tags:
  - session
  - workflow
  - harness
  - plugin
  - render
  sections:
    Purpose: 'Prevents a Spec from staying unapproved where the Claude Code CLI withholds the approval of a plan longer than it can show. The CLI shows a plan whole before it offers approval and offers none for a plan above the size it can show, whatever the window, while the VS Code extension approves the same plan; GUPPI writes each ratified Case whole into the plan file, so a Spec of a few Cases could not leave Plan Mode in the CLI. There the person presses Esc at the dialog, leaves Plan Mode with Shift+Tab and types `/approve-spec`. The hook that judges that prompt and takes the plan file into `spec.md` is the hook of `rule-spec-capture`, which sets when it blocks the prompt and what it writes; this page sets the text of the skill, which tells the agent to follow the line that hook gives. The skill carries `disable-model-invocation: true`: the agent cannot start it, since the approval is the person''s.'
    Render: |-
      <!-- rule-skill-approve-spec -->
      ---
      name: approve-spec
      description: The person's approval of the Spec where the Claude Code CLI withholds it, typed out of Plan Mode after /pre-spec; a hook takes the plan file into spec.md and gives the next step.
      disable-model-invocation: true
      ---

      The person typed `/approve-spec`: the approval of the Spec where the Claude Code CLI withholds the approval of a plan longer than it can show. The hook of `rule-spec-capture` on `UserPromptSubmit` judged the prompt before it reached you, and let it through: the session is out of Plan Mode, `/pre-spec` ran, the check of the plan finds nothing, and the plan file of the session now stands in `raw/<hi date>/<hi HHMM>/spec.md`.

      Follow the line of that hook in your context, as after `ExitPlanMode`: ask the person the fork between `/work` and `/carry` by `AskUserQuestion` and call the skill picked, or, where the line names a conserved Spec, call `/box` with its folder and ask the person nothing. Write nothing into the plan file.
      <!-- /rule-skill-approve-spec -->
- slug: estimate-skill-approve-spec-takes-the-spec
  ref: rule-skill-approve-spec
  kind: QA
  purpose: Whether /approve-spec, typed by the person out of Plan Mode after /pre-spec, appends the plan file of the session to its spec.md and gives the agent the line of an approval, and is blocked in Plan Mode, before /pre-spec, while the check of the plan finds a finding, or with no plan file
  method: 'uv run --project .guppi pytest .guppi/tests/test_spec.py -k typed; by hand, after the librarian''s run that applies the create of rule-skill-approve-spec and renders .claude/settings.json and .claude/skills/approve-spec/SKILL.md: in a standalone terminal window, the Claude Code CLI on a copy of the repository, a working session whose plan the CLI withholds and whose check of /pre-spec passes, /approve-spec typed once in Plan Mode and once after Esc and Shift+Tab, then the transcript of that session under ~/.claude/projects/ and its spec.md read against the Criterion'
  tags:
  - session
  - workflow
  - harness
  - plugin
update:
- slug: rule-spec-capture
  replace:
  - old: 'The file has three writers: the hook `guppi spec` on `PostToolUse` of `ExitPlanMode`, which appends the approved plan to `raw/<hi date>/<hi HHMM>/spec.md` once, stamped;'
    new: 'The file has three writers: the hook `guppi spec` on `PostToolUse` of `ExitPlanMode`, which appends the approved plan to `raw/<hi date>/<hi HHMM>/spec.md` once, stamped, and, where the Claude Code CLI withholds that approval, on `UserPromptSubmit` when the person types `/approve-spec`, as `uv run --project .guppi guppi spec --typed`, which blocks the prompt while the session is in Plan Mode, before `/pre-spec` or while the check of the plan finds a finding — by the judgment of `gate` of `.guppi/guppi/prespec.py`, the same function the hook of `rule-prespec-hook` runs at `ExitPlanMode` — and with no plan file or no `/hi` of the session, and otherwise appends the plan file of the session in the same way and gives the agent the same line, the skill of `rule-skill-approve-spec` telling the agent to follow it;'
  change: the Spec capture takes the plan file when the person types /approve-spec
- slug: rule-hook-registry
  replace:
  - old: '{ "type": "command", "command": "uv run --project .guppi guppi sprint --hi", "timeout": 30 },'
    new: '{ "type": "command", "command": "uv run --project .guppi guppi sprint --hi", "timeout": 30 }, { "type": "command", "command": "uv run --project .guppi guppi spec --typed", "timeout": 30 },'
  change: UserPromptSubmit → guppi spec --typed
- slug: rule-work-mode
  replace:
  - old: 'Its skill `/work` starts after `ExitPlanMode`:'
    new: 'Its skill `/work` starts after the approval of the Spec, by `ExitPlanMode` or by `/approve-spec`:'
  - old: at the fork ExitPlanMode prints;
    new: at the fork printed after the approval of the Spec, by ExitPlanMode or by /approve-spec;
  change: /work follows the approval by ExitPlanMode or by /approve-spec
- slug: rule-carry-over
  replace:
  - old: at the fork ExitPlanMode prints.
    new: at the fork printed after the approval of the Spec, by ExitPlanMode or by /approve-spec.
  - old: Called after `ExitPlanMode`, when
    new: Called after the approval of the Spec, by `ExitPlanMode` or by `/approve-spec`, when
  change: /carry follows the approval by ExitPlanMode or by /approve-spec
- slug: rule-spec-box
  replace:
  - old: prints after ExitPlanMode.
    new: prints after the approval of the Spec, by ExitPlanMode or by /approve-spec.
  - old: the line printed after `ExitPlanMode` names
    new: the line printed after the approval of the Spec, by `ExitPlanMode` or by `/approve-spec`, names
  change: /box follows the approval by ExitPlanMode or by /approve-spec
- slug: insight-plugin-cli-withholds-approval-of-a-long-plan
  set:
    status: actioned
    addressed_by: decision-case-987.1
  change: 'actioned: the person approves a long Spec in the CLI by typing /approve-spec'
```

```tasks
- [x] create `rule-skill-approve-spec`
- [x] update `rule-spec-capture`
- [x] update `rule-hook-registry`
- [x] update `rule-work-mode`
- [x] update `rule-carry-over`
- [x] update `rule-spec-box`
- [x] update `insight-plugin-cli-withholds-approval-of-a-long-plan`
- [x] create `estimate-skill-approve-spec-takes-the-spec`
- [x] `.guppi/guppi/event.py`: the body of `is_hi_prompt` moves into one function that judges a typed prompt for a named command, which `is_hi_prompt` calls with `/hi`.
- [x] `.guppi/guppi/prespec.py`: the judgment of `gate` moves into one function that returns the reason of a refusal or nothing; `gate` prints that reason as before.
- [x] `.guppi/guppi/spec.py`: `--typed` on `UserPromptSubmit` reads `/approve-spec` by the function of `event.py` and Plan Mode by `PLAN_MODE`, runs the function of `prespec.py`, finds the plan file by `plan_path` of `ledger.py`, appends it by `append_plan` and prints the line of `fork_output` as `hookSpecificOutput` of `UserPromptSubmit`, or exits 2 with the reason; the docstring names the typed path.
- [x] `.guppi/tests/test_spec.py`: tests named with `typed` for each line of the `then` above.
- [x] `uv run --project .guppi guppi render`: `.claude/settings.json`
- [x] `uv run --project .guppi guppi render`: `.claude/skills/approve-spec/SKILL.md`
- [x] `uv run --project .guppi guppi render`: `.claude/skills/work/SKILL.md`
- [x] `uv run --project .guppi guppi render`: `.claude/skills/carry/SKILL.md`
- [x] `uv run --project .guppi guppi render`: `.claude/skills/box/SKILL.md`
- [ ] read `estimate-skill-approve-spec-takes-the-spec`
```

### Case 987.2 — The agent names the typed approval before it leaves Plan Mode

> **given:**
> `rule-orchestration`: its Render, `vault/wiki/orchestration.md`, what the main agent does.
> **＋** `rule-skill-approve-spec`: the rule of `/approve-spec`, the command the line names.
> **＋** `/pre-spec`: the check after which the agent calls `ExitPlanMode`.
> **＋** `estimate-orchestration-names-the-typed-approval`: the new check of the line.

> **when:**
> In a working session the main agent writes the reply that calls `ExitPlanMode`.

> **then:**
> Before the call, the reply holds one line worded as a condition: if the Claude Code CLI offers no approval for this plan, press Esc, leave Plan Mode with Shift+Tab and type `/approve-spec`.
> **＋** The line claims nothing of the client: it does not say that the CLI withholds the approval.
> **－** The line adds no step and no question: the agent calls `ExitPlanMode` in the same reply, only after `/pre-spec`, as before.

```then
create:
- slug: estimate-orchestration-names-the-typed-approval
  ref: rule-orchestration
  kind: QA
  purpose: Whether the reply in which the main agent calls ExitPlanMode holds, before the call, one line worded as a condition that names Esc, Shift+Tab and /approve-spec for a CLI that offers no approval, and claims nothing of the client
  method: 'by hand, after the librarian''s run that applies the update of rule-orchestration naming /approve-spec and renders vault/wiki/orchestration.md: in the trial in the Claude Code CLI that reads estimate-skill-approve-spec-takes-the-spec, the reply that calls ExitPlanMode read in the transcript of that session under ~/.claude/projects/ against the Criterion'
  tags:
  - session
  - workflow
  - harness
  - plugin
update:
- slug: rule-orchestration
  replace:
  - old: calls `ExitPlanMode` only after `/pre-spec` (case 561.14).
    new: 'calls `ExitPlanMode` only after `/pre-spec` (case 561.14). The reply that calls `ExitPlanMode` holds, before the call, one line worded as a condition: if the Claude Code CLI offers no approval for this plan, the person presses Esc, leaves Plan Mode with Shift+Tab and types `/approve-spec`. The agent cannot tell whether the CLI offered the approval, and after Esc at the dialog Claude Code stops the turn, so the line comes before the call and claims nothing of the client.'
  change: the reply that calls ExitPlanMode names /approve-spec, worded as a condition, before the call
```

```tasks
- [x] update `rule-orchestration`
- [x] create `estimate-orchestration-names-the-typed-approval`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
- [ ] read `estimate-orchestration-names-the-typed-approval`
```

## Case 988 — The form of a ledger line is read without waiting for a new tag

> **context:**
> `rule-ratification` is `draft` for one reason. The cascade of `.guppi/guppi/generate.py` (the method `cascade` of its generator) sets a rule `built` only when each Estimate in its `estimates` stands `passed`, and `estimate-ratification-ledger-line-form` stands `pending`. Its `method`, set by case 961.5, waits for a lesson line that declares a new tag by a `{newtag:...}` block. A Grep for `\{newtag:` over every `ledger.md` under `vault/` printed nothing, so no session has written such a line. While the page is `draft`, `drafts` of `.guppi/guppi/ship.py`, through `is_draft_core` of `.guppi/guppi/pages.py`, gives a line for it, and `guppi ship` writes no clean version without `--allow-draft`. The brief of the last librarian's run (`vault/wiki/brief.md`, `## Flags`) reports that `guppi check` printed 13 lines, `rule-ratification` among the 10 lines `status: a page with core: true that is draft`. The other lines of the Criterion can be read now: a Grep for `\{addresses:|\{addressed_by:` over the ledgers under `vault/archive/plugin/` printed a count of 8 matches in five files, the five files the `method` names, and `vault/archive/migration/2026-10-04/1439/raw/ledger.md` stands. The new-tag block is checked from the side of the ledger hook by `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag` of `rule-ledger-write`, which stands `passed`: the hook writes no lesson line whose tag `vault/wiki/tags.md` does not hold unless a `{newtag:...}` block declares it, so no line of another form reaches a ledger. This Case writes the Criterion again without the new-tag line, and its `method` reads the archived ledgers at Retro. The rule that governs the `method` is `rule-estimates-schema`: a reading by hand names the place of its evidence, the transcript of a session under `~/.claude/projects/` included, which the new `method` keeps. The sentence of the Render of `rule-ratification` on the `{newtag:...}` block stays true, and the hook's Estimate checks it. The put-off of `decision-case-907`, the removal of `PLAIN_SPRINTS` from `.guppi/guppi/caseid.py` after the sprint `plugin` closes, stays as it stands, so this Case carries no `{supersedes:case 907}`: `next_id` of that file gives a sprint that `is_plain` does not accept a number such as `plugin-1`, so the removal before the close would break the plain numbers of the open sprint, and the put-off sets no status of the page. A Grep for `ratification-ledger-line-form` over `vault/wiki/`, `.claude/`, `.guppi/guppi/` and `.guppi/tests/` printed `vault/wiki/brief.md`, `vault/wiki/log.md` and `vault/wiki/rules/rule-ratification.md`; the rule page lists the Estimate in `estimates`, which stands, and no test reads the Estimate's live file. The `estimates` of `rule-ratification` hold two more Estimates: `estimate-ratification-loaded` speaks of the loading of `ratification.md`, and `estimate-ratification-case-id-carries-the-sprint` of Case ids, so neither changes. The session's ledger holds no `lesson[error]` line, so this Case adds no mark.

> **problem:**
> `rule-ratification` stays `draft`, and blocks the clean version, because its check of the ledger-line form waits for a lesson line with a new tag that no session has written, while the rest of that check can be read now and the new-tag form is already checked from the side of the hook.

> **recommend:**
> - **What happens to the put-off removal of the sprint list**
>   - Recommended: (a) leave it waiting: the put-off stays, and the removal waits for the first session after `plugin` closes.
>   - Answer: agreed, (a).
> - **How the check of the ledger-line form gets its reading**
>   - Recommended: (a) drop the new-tag line from this check and read the rest at Retro, from the archived ledgers and their transcripts; the new-tag form stays checked by the hook's Estimate.
>   - Answer: agreed, (a).

> **given:**
> `estimate-ratification-ledger-line-form`: its Criterion is replaced whole and its `method` changes.
> **＋** `rule-ratification`: the rule it checks, rendered into `vault/wiki/ratification.md`.
> **＋** `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag`: the check of the new-tag block from the side of the ledger hook.
> **＋** `rule-estimates-schema`: the form of a `method`.

> **when:**
> The agent writes the ledger lines of a session — the decision lines in the reply that acknowledges a ratification, a lesson line the moment the lesson exists — with `vault/wiki/ratification.md` rendered from `rule-ratification`.

> **then:**
> A decision line is `- decision[case N][kind][slug]` with `{ref:...}` when the target has a ref, `{tags:...}` on a `create`, and `{supersedes:case N}` when it applies.
> **＋** A line that supersedes more than one Case carries one `{supersedes:case N}` block per Case, side by side, never a list inside one block.
> **＋** A Case that takes up a deferred decision carries, on one of its decision lines, one `{supersedes:case N}` block for each Case in the page's `deferred_by`.
> **＋** When a Case of this session closes the root cause of a lesson of this session, the line written second carries the mark: `{addresses:<lesson slug>}` on the decision line when the lesson line stands first, `{addressed_by:case N}` on the lesson line when the decision lines stand first; one mark per lesson.
> **＋** For a Case with sub-cases, the `N` of `{addressed_by:case N}` is the sub-case whose decision line closes the cause, never the parent, which has no decision line.
> **＋** The mark stands in the preview of the ledger lines the person ratifies, or in the `LEDGER` block of the lesson line.
> **－** A lesson whose fix is ratified in another session gets no mark.

```then
update:
- slug: estimate-ratification-ledger-line-form
  set:
    status: pending
    method: 'by hand, at Retro: the decision and lesson lines that carry an addresses or addressed_by mark in vault/archive/plugin/2026-10-14/0232/raw/ledger.md, vault/archive/plugin/2026-10-14/1536/raw/ledger.md, vault/archive/plugin/2026-10-16/2104/raw/ledger.md, vault/archive/plugin/2026-10-17/2307/raw/ledger.md and vault/archive/plugin/2026-10-29/2341/raw/ledger.md, and the line in vault/archive/migration/2026-10-04/1439/raw/ledger.md that takes up a page with two Cases in its deferred_by, each with its preview in the transcript of its session under ~/.claude/projects/, read against the Criterion, all recorded in one estimate line (the take-up line is that of case 629.2)'
  change: the Criterion replaced whole — the new-tag block of a lesson line is left to the check of the ledger hook; the method reads the archived ledgers and waits for no new tag
```

```tasks
- [x] update `estimate-ratification-ledger-line-form`
- [x] read `estimate-ratification-ledger-line-form`
```

## Case 989 — A trial run on a copy reads the check of /box

> **context:**
> `/box` runs a Spec that an earlier session saved by `/carry` and could not finish: it checks the Spec, runs it on its own branch, merges the branch back and has the librarian write the pages on the shared branch. `rule-spec-box` has `core: true` and stands `draft`. Its History shows that it went back to `draft` by the cascade after Case 956.4 added two steps to `/box`, showing `report.md` and committing it alone, and replaced the Criterion of `estimate-spec-box-runs-a-conserved-spec`, which set that Estimate `pending`. Its method waits for a session that runs a saved Spec by `/box`, and none has run since. The last reading, of 2026-10-04 in session 1416, passed each step but the two new ones. This session cannot run `/box` on the live repository, since `estimate-spec-box-refuses-a-stale-spec` promises that `guppi box --check` refuses a session that ratified a Case of its own. While the page is `draft`, the brief of the last librarian's run reports it among the lines of `guppi check` ("10 `status: a page with core: true that is draft`"), and `drafts` of `.guppi/guppi/ship.py` stops the build of the clean version before it writes `prod` for each such page. The page has no `deferred_by`. It stands in `backlog.md` because `deferred` of `.guppi/guppi/backlog.py`, read whole, lists each line of the `## Backlog` of each sprint page, the closed ones under `vault/archive/` too, and the closed sprint `migration` names `[[rule-spec-box]]` there. `finished` drops such a line once its page stands `built` (as read whole in case 962). The person chose a trial on a copy of the repository. At `/pre-spec` the person agreed that it runs after the librarian's run of this session and not in its Work Mode. The Render of `rule-orchestration` says a file rendered from a Rule page "changes at the librarian's render after the session" (case 690.2), and no task of this Case renders `.claude/skills/box/SKILL.md` earlier. The method of the Estimate is set anew, opening its by-hand part with `after` and the event, and its Criterion and its status stand. The Case is checked by `estimate-spec-box-runs-a-conserved-spec`. Its Criterion already promises each step of `/box`, the two new ones too, and only its moment changes. `estimate-spec-box-refuses-a-stale-spec` stays `passed`, since `guppi box --check` does not change.
>
> The Purpose of `rule-spec-box` ends by pointing to a line of the Backlog of the closed sprint `entity-sprint-migration` for the second part of `/box`. Case 962 put that work as a note in the Backlog of the live sprint page `entity-sprint-plugin`. That note now holds the work in the backlog list, and the person chose to point there. The second part stays out of this Case. No Estimate checks the pointer, since an update of a Purpose touches no Estimate (case 378.5). Case 987.1 of this session rewords two sentences of the Render of `rule-spec-box`, the description of `/box` and the sentence on its argument. This Case changes only the last sentence of the Purpose, so the pairs do not meet. I read the finished file of Case 987 whole. Its pairs on `rule-spec-box` touch only the Render. Its render line of `.claude/skills/box/SKILL.md` is run by the librarian. The by-hand part of each of its methods waits for the librarian's run after this session, so its trials and this one wait for the same event. The trial of this Case waits for the librarian's run that applies this Case's `update` of `rule-spec-box`, and that run renders `.claude/skills/box/SKILL.md` from the page as it then stands. A Grep of `estimate-spec-box-runs-a-conserved-spec|second part` over `vault/wiki/` (with `log.md` and `brief.md` left out) printed `backlog.md`, `entities/entity-sprint-plugin.md` and `rules/rule-spec-box.md`, and over `.claude/` it printed nothing. `backlog.md` is written by its script. The note of `entity-sprint-plugin` stays true. A Grep of `rule-spec-box|box/SKILL|spec-box-runs` over `.guppi/tests/` printed only a docstring of `test_box.py`, so no test reads the changed text live. The `.guppi/links.md` block of `rule-spec-box` names no neighbour that the change makes false. `lesson-box-cannot-act-on-the-prespec-findings-of-a-conserved-spec` is part of the second part. The session's ledger holds no `error` lesson, so no line carries `{addresses:...}`.

> **problem:**
> The check of `/box` waits for a run that no session plans, so `rule-spec-box` stays `draft`, `guppi check` reports it, the build of the clean version is refused, and the Purpose points to the second part of `/box` on a closed sprint page.

> **recommend:**
> - **How the waiting check of /box gets read**
>   - Recommended: (a) a trial run on a copy of the repository, in this session's Work Mode.
>   - Answer: agreed, (a).
> - **Where the page points for the second part of /box**
>   - Recommended: (a) to the note on the live sprint page `entity-sprint-plugin`.
>   - Answer: agreed, (a).
> - **Whether the second part of /box enters this Case**
>   - Recommended: (a) no, it stays a note on the sprint page.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec`, the person agreed that the trial of `/box` runs after the librarian's run of this session, since `.claude/skills/box/SKILL.md` is rendered only then, and not in this session's Work Mode.
>   - Taken: the method of `estimate-spec-box-runs-a-conserved-spec` waits for that librarian's run, and the task that stopped Work Mode for the trial is gone.

> **given:**
> `rule-spec-box`: the rule of `/box`, whose Purpose points to the second part.
> **＋** `.claude/skills/box/SKILL.md`: the skill, as rendered from that rule.
> **＋** `estimate-spec-box-runs-a-conserved-spec`: the check of `/box`, whose method is set anew.
> **＋** `entity-sprint-plugin`: the live sprint page, whose Backlog holds the second part as a note.
> **＋** `/carry`: the skill that saves the Spec of the trial.
> **＋** `~/.claude/projects/`: the folder of the transcripts the reading reads.

> **when:**
> After the librarian's run that applies the `update` of `rule-spec-box` and renders `.claude/skills/box/SKILL.md`, the person runs on a copy of the repository a session that saves a small Spec by `/carry` and a second session that runs it by `/box`.

> **then:**
> The second session runs `/box` through the dispatch of `librarian-guppi` and the commit of `report.md`.
> **＋** Git log, the branches and the folders of the copy, and the transcript of the second session under `~/.claude/projects/`, are read against the Criterion of `estimate-spec-box-runs-a-conserved-spec`, and its estimate line names that transcript.
> **＋** The Purpose of `rule-spec-box` points to the note on the second part of `/box` in the Backlog of `entity-sprint-plugin`.
> **－** The trial writes nothing to the live repository; the estimate line is the only record of it.
> **－** The second part of `/box` is not designed here, and the note of `entity-sprint-plugin` stays as it stands.

```then
update:
- slug: rule-spec-box
  replace:
  - old: Both wait for a second part (a line of the Backlog of `entity-sprint-migration`, case 591).
    new: Both wait for a second part (a note of the Backlog of `entity-sprint-plugin`, as set in case 962).
  change: the second part of /box is pointed to on the live sprint page
- slug: estimate-spec-box-runs-a-conserved-spec
  set:
    method: 'uv run --project .guppi guppi render --check; by hand, after the librarian''s run that applies the update of rule-spec-box pointing to the Backlog of entity-sprint-plugin and renders .claude/skills/box/SKILL.md: on a copy of the repository, one session saves a small Spec by /carry and a second session takes it at its Frontier and runs it by /box; git log, the branches, the folders of that session and of the conserved Spec, the librarian''s commit and the commit of report.md read in the copy, and the dispatch line and the text shown to the person read in the transcript of the second session under ~/.claude/projects/, recorded in the estimate line with that transcript named'
  change: 'method: a trial run of /box on a copy of the repository, after the librarian''s run that renders the skill'
```

```tasks
- [x] update `rule-spec-box`
- [x] update `estimate-spec-box-runs-a-conserved-spec`
- [ ] read `estimate-spec-box-runs-a-conserved-spec`
```
