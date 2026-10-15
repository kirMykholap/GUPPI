## Case 809 — The shipped pages hold each pointer in a bracket of its own

> **context:**
> `guppi ship` builds the clean version of GUPPI that other people install, and the workflow `.github/workflows/prod.yml` writes it to the branch `prod` on a push of a tag `prod-*`. `guppi ship` removes each bracket that holds a pointer to a case, a decision or a session, and exits 1 on each pointer outside such a bracket, so the run writes nothing while one remains. The run of `guppi ship --review` of session 2118, saved in `vault/raw/2026-10-13/2118/ship-review.txt`, printed 196 lines: 82 on a pointer outside a bracket, in 30 pages with `core: true` and in the `schema.yaml` of four categories rendered from four of them, and 114 on a bracket that holds words beside its pointer, 31 of them on `guppi/`. Many of the pointers outside a bracket tell the history of this repository, such as `since case 272` in `rule-claude-md`. Some brackets with words hold what the sentence needs: in `case-schema.md`, the Render of `rule-case-protocol`, the whole definition of `replace`, `reword` and `rename` stands in brackets that end with a case number, so the clean copy would lose it; many others hold the slug of the rule that sets the behaviour, such as `` (`rule-sprint-close`, case 627.1) ``, which the copy would lose too.
>
> The person chose that each pointer outside a bracket moves into a bracket at the end of its sentence together with the words of history that go with it, so each sentence keeps its meaning here and the copy drops only the history; that a bracket that carries a definition is split so that the definition stays outside, and that the slug of a page with `core: true` moves out of its bracket, such as `as rule-sprint-close sets it (case 627.1)`, while a slug of a page that does not ship stays inside; that the code of `guppi ship` does not change; that the CI run by a tag `prod-*` waits for the librarian's run that applies these pages, in a later session of the sprint, where `estimate-sprint-plugin-ci-writes-a-clean-branch` is read by its own `method`; and that one new Estimate on `rule-clean-branch`, read by hand after that librarian's run, checks the pages. A bracket in this Case stands at the end of its clause, before a semicolon, a colon or a comma, as many brackets of these pages already do, and the clause reads whole without it. The brackets with words that hold only history and no definition or shipped slug stand, such as `(the shape before case 103)`, `(case 182, point 5)`, `(case 167, supersedes 157)` and `` (case 56, `lesson-render-governed-file-updated-as-rule-class-file`) ``; the `(cases 59.1–59.3, 59.6)` of `rule-prespec-hook` stands too.
>
> The review run is from before the librarian's run of session 2118, which applied Cases 806 and 807 to `rule-case-protocol`, `rule-case-build`, `rule-orchestration`, `rule-work-mode`, `rule-where-to-stop` and `rule-lint`. The first four were read whole here, and their new text holds its pointers in brackets. A Grep of `rule-where-to-stop.md` and `rule-lint.md` under `vault/wiki/rules/` for `[^(;,] [Cc]ases? \d|[Ss]essions? \d{4}` printed two lines of `rule-lint.md`, both History lines, which `guppi ship` replaces. The `## How it works` of `rule-skill-hi` names a session by the id `1b191eaf`, which is no pointer to `guppi ship`, since its id of a session is four digits; it stands outside this Case, and the reading of `estimate-sprint-plugin-ci-writes-a-clean-branch` may judge it. The update of `rule-page-generation` leaves its `deferred_by` as it stands.
>
> Case 808 of this session rewrites the bare case numbers of `guppi/` and checks the code by `estimate-clean-branch-code-holds-pointers-only-in-brackets`, and the lines of `--review` on `guppi/` are its promise, not this one. Both Cases write to `rule-clean-branch`: Case 808.1 replaces a sentence of its `## Purpose`, and the `create` of this Case adds the new Estimate to its `estimates` field, which `generate` fills from the `ref`; this Case writes no text of that page, so the two do not touch the same sentence. The other pages this Case changes are no pages of Case 808.
>
> At `/pre-spec`, `guppi prespec --check` found that the Frontier line of this item closes a sprint item with this Case while no update of the sprint page stood here. The person chose that this Case updates `entity-sprint-plugin`: the line of the milestone The clean branch says what remains, so the item stays open on the sprint page and comes back to the next Frontier with that remainder. The update leaves the `deferred_by` of that page, which Case 805 wrote, as it stands. Its `context` leaves bare case numbers in pages to this item: the one in a page with `core: true` that this Case meets, `in 59.8` of `rule-claude-md`, is written `case 59.8` here. The new Estimate carries a `ref`, so no vault query of `ask-guppi` was run; a Glob `vault/**/estimate-clean-branch-pages*` printed nothing, so its slug is free, and the tags `ci` and `plugin` stand in `vault/wiki/tags.md`. An `update` of a `Render` touches no Estimate whose only promise is that the file equals the Render. Two Estimates of these pages promise what a reworded sentence says, and their Criteria stand. The Criterion of `estimate-decisions-schema-checked` promises that `vault/wiki/decisions/schema.yaml` says that a new page carries `## Context` only for the short form of a deferred decision and in the two-line body of a Case superseded in its own session, and that the pages written before keep the sections they carry; the new wording, `An older page keeps the sections it carries` and `kept on the older pages that carry it`, says the same, the case numbers only moved into brackets. The Criterion of `estimate-glossary-terms-defined` promises that the terms the Purpose of `entity-glossary` names as not rows stand in no row; the new Purpose names the same terms as not rows, and the pointer only moved to the end of the clause. No other Estimate of these pages speaks of a sentence this Case rewords, since the rewording changes no behaviour. A Grep of `tests/` for `(Path\(__file__\)|REPO|ROOT|project_root\(\))[^\n]*(vault|wiki|Makefile|parents|parent)` printed `tests/test_case_schema.py`, `tests/test_orchestration.py`, `tests/test_schemas.py`, `tests/test_generate.py`, `tests/test_materialize.py` and `tests/test_lint.py`; the first five read the live `schema.yaml` files, `case-schema.md` or `orchestration.md` for the lists of a schema and for the blocks tagged `case`, `showing` and `defer`, which this Case does not touch, and `tests/test_lint.py` reads the `Makefile`, so no test fails on the new text. The last `make lint` printed 0 lines and exited 0 (`vault/wiki/brief.md`, Flags); this Case changes no code it runs. The `given` holds more than seven lines, since one promise covers every page the review run listed.

> **problem:**
> The pages that ship hold pointers outside a bracket, so `guppi ship` exits 1 and the CI run writes no clean branch, and some brackets that `guppi ship` removes hold a definition or the slug of a shipped rule that the sentence needs.

> **recommend:**
> - **How a sentence with a pointer outside a bracket is rewritten**
>   - Recommended: (a) the pointer and its history words go into one bracket at the end of the sentence.
>   - Answer: agreed, (a).
> - **Which brackets with words change**
>   - Recommended: (a) fix the brackets that carry a definition, and move the slug of a shipped page out of its bracket.
>   - Answer: agreed, (a).
> - **Whether the code of `guppi ship` changes too**
>   - Recommended: (a) pages only; the code stays as it is.
>   - Answer: agreed, (a).
> - **When the CI run takes place**
>   - Recommended: (a) after the librarian's run, in a later session of the sprint.
>   - Answer: agreed, (a).
> - **How the rewording is checked**
>   - Recommended: (a) one new Estimate on `rule-clean-branch` for the pages.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec`, the Frontier closes the sprint item with this Case, so the person was asked whether this Case updates `entity-sprint-plugin` so that the line of the milestone The clean branch says what remains, or the item is put off instead; the person agreed to the update. The findings of `/pre-spec` also asked that `context` name `estimate-glossary-terms-defined` and `estimate-decisions-schema-checked` and say that both Criteria hold, and that it correct what it said of Case 808 and `rule-clean-branch`.
>   - Taken: an `update` of `entity-sprint-plugin` rewrites the milestone line with what remains; `context` names the two Estimates and why their Criteria stand, and says that Case 808 and this Case both write to `rule-clean-branch`, on no common sentence.

> **given:**
> `rule-clean-branch`: the rule of the pointer and of the clean version, the target of the new Estimate.
> **＋** `estimate-clean-branch-pages-hold-pointers-only-in-brackets`: the new check of the pages.
> **＋** `vault/wiki/`: the pages with `core: true`, the `schema.yaml` of each category, `case-schema.md`, `orchestration.md` and `glossary.md`.
> **＋** `.claude/`: the harness files rendered from the pages this Case changes.
> **＋** `guppi/`: the code, whose lines belong to `estimate-clean-branch-code-holds-pointers-only-in-brackets`.
> **＋** `entity-glossary`: the terms, reworded.
> **＋** `entity-sprint`: the sprint as a kind, reworded.
> **＋** `entity-sprint-plugin`: the live sprint page, whose milestone line says what remains.
> **＋** `rule-agent-writing`: reworded.
> **＋** `rule-backlog`: reworded.
> **＋** `rule-brief`: reworded, its Render too.
> **＋** `rule-carry-over`: reworded, its Render too.
> **＋** `rule-case-build`: reworded.
> **＋** `rule-case-check`: reworded.
> **＋** `rule-case-example`: reworded.
> **＋** `rule-case-protocol`: reworded, its Render too.
> **＋** `rule-claude-md`: reworded.
> **＋** `rule-cleanup`: reworded.
> **＋** `rule-decisions-schema`: reworded, its Render too.
> **＋** `rule-documentation`: reworded, its Render too.
> **＋** `rule-end-of-work`: reworded.
> **＋** `rule-entities-schema`: reworded, its Render too.
> **＋** `rule-estimates-schema`: reworded, its Render too.
> **＋** `rule-event-log`: reworded.
> **＋** `rule-git-context`: reworded.
> **＋** `rule-insights-schema`: reworded, its Render too.
> **＋** `rule-internal-context`: reworded.
> **＋** `rule-language`: reworded.
> **＋** `rule-ledger-tail`: reworded.
> **＋** `rule-ledger-write`: reworded.
> **＋** `rule-lessons-schema`: reworded, its Render too.
> **＋** `rule-materialize`: reworded.
> **＋** `rule-orchestration`: reworded, its Render too.
> **＋** `rule-page-generation`: reworded.
> **＋** `rule-page-read`: reworded.
> **＋** `rule-page-schemas`: reworded.
> **＋** `rule-permissions`: reworded.
> **＋** `rule-prespec-hook`: reworded.
> **＋** `rule-raw-archive`: reworded.
> **＋** `rule-render-harness`: reworded.
> **＋** `rule-retro`: reworded, its Render too.
> **＋** `rule-retro-commit`: reworded.
> **＋** `rule-retro-onward`: reworded.
> **＋** `rule-rules-schema`: reworded, its Render too.
> **＋** `rule-search-leaves-out-decisions`: reworded.
> **＋** `rule-skill-grill-me`: reworded.
> **＋** `rule-skill-hi`: reworded, its Render too.
> **＋** `rule-skill-sprint-close`: reworded.
> **＋** `rule-skill-sprint-open`: reworded.
> **＋** `rule-spec-capture`: reworded.
> **＋** `rule-spec-reconcile`: reworded.
> **＋** `rule-spec-write`: reworded.
> **＋** `rule-sprint`: reworded.
> **＋** `rule-synthesis`: reworded.
> **＋** `rule-work-mode`: reworded, its Render too.

> **when:**
> `uv run guppi ship --review <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.

> **then:**
> It prints no line on a pointer outside a bracket of its own in a page under `vault/wiki/` with `core: true`, in the `schema.yaml` of a category or in a file of `.claude/` that such a page renders.
> **＋** Each line of `--review` on those files shows a bracket that holds only pointers and the words that go with them, such as the history of this repository that a pointer names, when a thing was measured or which session a pointer names.
> **＋** No bracket that `--review` lists on those files holds the definition of a term that its sentence needs, or the slug of a page with `core: true` by which its sentence names the rule that sets what it says.
> **－** Each page under `vault/wiki/` keeps every pointer it held, with the words that go with it, in a bracket, and each sentence keeps its meaning in this repository.
> **－** A line on a file under `guppi/` is no part of this promise.

> **tasks:**
> - [ ] create `estimate-clean-branch-pages-hold-pointers-only-in-brackets`
>   - ref: `rule-clean-branch`
>   - kind: `QA`
>   - purpose: `Whether the pages with core: true, the schema.yaml of each category and the files of .claude/ rendered from such pages hold each pointer to a case, a decision or a session in a bracket of its own, so that guppi ship --review prints no line on a pointer outside a bracket there and no bracket it removes holds a definition or the slug of a shipped rule that the sentence needs`
>   - method: `by hand, after the librarian's run that applies case 809: the lines of uv run guppi ship --review into an empty temporary folder on vault/wiki/ and .claude/, read against the Criterion`
>   - tags: `[ci, plugin]`
> - [ ] update `entity-glossary`
>   - old: `Not rows, by the decision of case 306.3: C4 model`
>   - new: `Not rows: C4 model`
>   - old: `Librarian Report / Session Digest — their decisions stand in the archived ledgers of 2026-09-08 and 2026-09-09.`
>   - new: `Librarian Report / Session Digest (by the decision of case 306.3; their decisions stand in the archived ledgers of 2026-09-08 and 2026-09-09).`
>   - old: `` `create` a page (an Estimate is its own `create`, with `ref` on its target, case 193); ``
>   - new: `` `create` a page, an Estimate being its own `create` with `ref` on its target (case 193); ``
>   - old: `a page written before case 513 keeps its Context and Given (case 513)`
>   - new: `an older page keeps its Context and Given (one written before case 513, case 513)`
>   - old: `` for a Case built by `case-guppi` from session 2026-09-27/1819 on, its Case file (case 513); ``
>   - new: `` for a Case built by `case-guppi`, its Case file (from session 2026-09-27/1819 on, case 513); ``
>   - change: `each pointer stands in a bracket of its own, a definition outside it`
> - [ ] update `entity-sprint`
>   - old: `` its status kept in the record of the close (`rule-sprint-close`, case 632.3); ``
>   - new: `` its status kept in the record of the close, as `rule-sprint-close` sets it (case 632.3); ``
>   - change: `the slug of rule-sprint-close stands outside the bracket of its pointer`
> - [ ] update `entity-sprint-plugin`
>   - old: `no session data such as the Frontier or the sprint`
>   - new: `` no session data such as the Frontier or the sprint; what remains: once the librarian's run applies the rewording of the pages (case 809), the owner pushes a tag `prod-*` on a commit of `plugin`, and the CI run it starts is read by its Estimate ``
>   - change: `the milestone The clean branch says what remains after the rewording of the pages`
> - [ ] update `rule-agent-writing`
>   - old: `` the answer first and the not-done named. Until case 272 the rule was the section `## Style` of the Render of `rule-claude-md`: a standing condition with no page and no Estimate. ``
>   - new: `` the answer first and the not-done named (until case 272 the rule was the section `## Style` of the Render of `rule-claude-md`, a standing condition with no page and no Estimate). ``
>   - change: `the history of the rule stands in the bracket of its pointer`
> - [ ] update `rule-backlog`
>   - old: `` Prevents a deferred item from dropping out of sight. Before case 451 the brief carried at most seven deferred items, and an item cut off the seven stood on no list the next session read; a Spec conserved by `carry` stood only in the brief `carry` wrote. ``
>   - new: `` Prevents a deferred item from dropping out of sight (before case 451 the brief carried at most seven deferred items, and an item cut off the seven stood on no list the next session read; a Spec conserved by `carry` stood only in the brief `carry` wrote). ``
>   - old: `` so that the Backlog of a closed sprint stays in the list (`rule-sprint-close`, case 628.12) ``
>   - new: `` so that the Backlog of a closed sprint stays in the list, as `rule-sprint-close` sets it (case 628.12) ``
>   - change: `each pointer stands in a bracket of its own, the slug of rule-sprint-close outside it`
> - [ ] update `rule-brief`
>   - old: `` first the line `open the next sprint — no sprint is open since the close of <id>` (`rule-sprint-close`, case 628.8); ``
>   - new: `` first the line `open the next sprint — no sprint is open since the close of <id>`, as `rule-sprint-close` sets it (case 628.8); ``
>   - change: `the slug of rule-sprint-close stands outside the bracket of its pointer`
> - [ ] update `rule-carry-over`
>   - old: `` and `/box` runs it (`rule-spec-box`, case 591). ``
>   - new: `` and `/box` runs it, as `rule-spec-box` sets it (case 591). ``
>   - change: `the slug of rule-spec-box stands outside the bracket of its pointer`
> - [ ] update `rule-case-build`
>   - old: `` Until case 419.2 the agent was `frame-guppi`, which read the frame of a Case the main agent wrote and returned the contradictions only; whether a subagent pays for its tokens and time, the question of cases 403 and 408, is the method of its Estimate. ``
>   - new: `` Whether a subagent pays for its tokens and time is the method of its Estimate (the question of cases 403 and 408; until case 419.2 the agent was `frame-guppi`, which read the frame of a Case the main agent wrote and returned the contradictions only). ``
>   - change: `the history of the agent stands in the bracket of its pointer`
> - [ ] update `rule-case-check`
>   - old: `` Until case 419 no script read a Case before its ratification: the hook of `rule-spec-write` checks it only after the person signed, and a fault of the form was found by the person or at pre-spec ([[insight-case-form-chat-form-read-by-no-script]]). ``
>   - new: `` The hook of `rule-spec-write` checks a Case only after the person signed it (until case 419 no script read a Case before its ratification, and a fault of the form was found by the person or at pre-spec, [[insight-case-form-chat-form-read-by-no-script]]). ``
>   - change: `the history of the check stands in the bracket of its pointer`
> - [ ] update `rule-case-example`
>   - old: `` Until case 717.1 the examples stood in `case-schema.md`, the Render of [[rule-case-protocol]], which `case-guppi` reads whole on every dispatch, a dispatch that answers only with rounds included, and every later turn of the dispatch read them again from the cache. Here they stand apart, and ``
>   - new: `` The examples stand apart from `case-schema.md`, the Render of [[rule-case-protocol]], which `case-guppi` reads whole on every dispatch, a dispatch that answers only with rounds included (until case 717.1 they stood there, and every later turn of the dispatch read them again from the cache). Here ``
>   - change: `the history of the examples stands in the bracket of its pointer`
> - [ ] update `rule-case-protocol`
>   - old: `` Until case 595 `/hi` loaded the file into the main agent's context with what the main agent does and the one rule; those moved to `rule-orchestration` and `rule-ratification`, with the child `rule-atomicity` and the Estimates of the behaviours that moved, so the main agent no longer carries the form of a Case it does not build. Until case 273 the Render was a section of `CLAUDE.md` and the schema a file edited by hand; the two said the same thing twice and were signed twice. ``
>   - new: `` What the main agent does and the one rule stand in `rule-orchestration` and `rule-ratification`, with the child `rule-atomicity`, so the main agent does not carry the form of a Case it does not build (until case 595 `/hi` loaded this file into the main agent's context with them, and they moved there with the Estimates of the behaviours that moved; until case 273 the Render was a section of `CLAUDE.md` and the schema a file edited by hand, so the two said the same thing twice and were signed twice). ``
>   - old: `` a task that waits for the person's word before it runs opening its text with `stop:` (`rule-where-to-stop`, case 531.7); ``
>   - new: `` a task that waits for the person's word before it runs opening its text with `stop:`, as `rule-where-to-stop` sets it (case 531.7); ``
>   - old: `or pre-spec reports the pair — case 543)`
>   - new: `or pre-spec reports the pair) (case 543)`
>   - old: `` a slug goes through `rename`, case 274.1) ``
>   - new: `` a slug goes through `rename`) (case 274.1) ``
>   - old: `` `origin`, History and Result kept — case 258.1) ``
>   - new: `` `origin`, History and Result kept) (case 258.1) ``
>   - old: `` which the librarian runs and the command ticks (`rule-sprint-close`, case 628.1) ``
>   - new: `` which the librarian runs and the command ticks, as `rule-sprint-close` sets it (case 628.1) ``
>   - change: `each pointer stands in a bracket of its own; the definitions of replace, reword and rename and the slugs of shipped rules stand outside it`
> - [ ] update `rule-claude-md`
>   - old: `` The section "Migration mode", carried from the hand-written file of 2026-09-12, left with case 288.3, each of its items a Rule with a Render of its own by then; "Commands" left with it — `make style` before a commit is `rule-retro`'s, and "no new dependencies" came with the file in 59.8 and was never decided on its own. `rule-language` and `rule-agent-writing` have this page as their parent since case 272. `rule-case-protocol` was a child from case 66 to case 273, when its Render became `case-schema.md` and its parent `rule-plan-mode`. ``
>   - new: `` `rule-language` and `rule-agent-writing` have this page as their parent (since case 272; the section "Migration mode", carried from the hand-written file of 2026-09-12, left with case 288.3, each of its items a Rule with a Render of its own by then, and "Commands" left with it — `make style` before a commit is `rule-retro`'s, and "no new dependencies" came with the file in case 59.8 and was never decided on its own; `rule-case-protocol` was a child from case 66 to case 273, when its Render became `case-schema.md` and its parent `rule-plan-mode`). ``
>   - change: `the history of the page stands in the bracket of its pointers`
> - [ ] update `rule-cleanup`
>   - old: `` and `guppi sprint-close` at the close of a sprint (`rule-sprint-close`, case 627.1). ``
>   - new: `` and `guppi sprint-close` at the close of a sprint, as `rule-sprint-close` sets it (case 627.1). ``
>   - change: `the slug of rule-sprint-close stands outside the bracket of its pointer`
> - [ ] update `rule-decisions-schema`
>   - old: `` from a target page's `deferred_by` (a deferred decision, case 52.3), ``
>   - new: `` from the `deferred_by` of the target page of a deferred decision (case 52.3), ``
>   - old: `A page written before case 513 keeps the sections it carries and is not rewritten (case 513).`
>   - new: `An older page keeps the sections it carries and is not rewritten (one written before case 513, case 513).`
>   - old: `` but for one that a live page names in `deferred_by` or `addressed_by` (`rule-sprint-close`, case 627.1). ``
>   - new: `` but for one that a live page names in `deferred_by` or `addressed_by`, as `rule-sprint-close` sets it (case 627.1). ``
>   - old: `` for a Case built by `case-guppi` from session 2026-09-27/1819 on, its Case file `cases/case-<N>.md` with every section, N the id of the top-level Case; once the session is archived ``
>   - new: `` for a Case built by `case-guppi`, its Case file `cases/case-<N>.md` with every section, N the id of the top-level Case (from session 2026-09-27/1819 on). Once the session is archived ``
>   - old: `and in the two-line body of a Case superseded in its own session (case 299.4); kept on the pages written before case 513; any other Case keeps it in its Case file (case 513).`
>   - new: `and in the two-line body of a Case superseded in its own session (case 299.4), and kept on the older pages that carry it (written before case 513); any other Case keeps it in its Case file (case 513).`
>   - old: `absent on a short-form defer and on the pages written before case 544 (case 544.8).`
>   - new: `absent on a short-form defer and on the older pages written without it (before case 544, case 544.8).`
>   - old: `` written by `generate`, before case 513, on the page of a Case that had one: the pages of Cases before 201 carry it by the model of case 52.1, and the pages from case 376 on by case 378.3; the pages of Cases 201 to 375 carry none. A page written after case 513 carries none, and the Case file holds it (case 513). ``
>   - new: `` kept only on older pages that `generate` wrote with it (before case 513, on the page of a Case that had one: the pages of Cases before 201 carry it by the model of case 52.1, and the pages from case 376 on by case 378.3; the pages of Cases 201 to 375 carry none). A newer page carries none, and the Case file holds it (case 513). ``
>   - old: `` Only on pages written before case 72, which keep it: the Case's `when`. A page written after case 72 has no `## When` (case 72.2). ``
>   - new: `` Only on older pages, which keep it: the Case's `when` (written before case 72). A newer page has no `## When` (case 72.2). ``
>   - old: `` Only on pages written before case 201.2, which keep it: one `- [[estimate-x]] § case N` line per block the Case wrote under the shape before case 193. A page written after carries none: ``
>   - new: `` Only on older pages, which keep it: one `- [[estimate-x]] § case N` line per block the Case wrote in an older shape (written before case 201.2, in the shape before case 193). A newer page carries none: ``
>   - change: `each pointer stands in a bracket of its own with the history it names, the slug of rule-sprint-close outside it`
> - [ ] update `rule-documentation`
>   - old: `` `vault/raw/<date>/<hi HHMM>/handoff.md` (the session's folder, case 73), ``
>   - new: `` `vault/raw/<date>/<hi HHMM>/handoff.md` in the session's folder (case 73), ``
>   - old: `` the command runs `guppi cleanup` itself (`rule-sprint-close`, case 628.1). ``
>   - new: `` the command runs `guppi cleanup` itself, as `rule-sprint-close` sets it (case 628.1). ``
>   - old: `` with the closed sprint marked (`rule-sprint`, case 743.5). ``
>   - new: `` with the closed sprint marked, as `rule-sprint` sets it (case 743.5). ``
>   - old: `` live or under `vault/archive/` (`rule-backlog`, case 632.2). ``
>   - new: `` live or under `vault/archive/`, as `rule-backlog` sets it (case 632.2). ``
>   - change: `the session's folder and the slugs of shipped rules stand outside the brackets of their pointers`
> - [ ] update `rule-end-of-work`
>   - old: `` and before the librarian (`rule-spec-box`, case 591). ``
>   - new: `` and before the librarian, as `rule-spec-box` sets it (case 591). ``
>   - change: `the slug of rule-spec-box stands outside the bracket of its pointer`
> - [ ] update `rule-entities-schema`
>   - old: `seen by Obsidian since case 148.1 (case 166.1)`
>   - new: `seen by Obsidian (since case 148.1; case 166.1)`
>   - change: `each pointer stands in a bracket of its own`
> - [ ] update `rule-estimates-schema`
>   - old: `` `purpose`, `method` and `checked` are the fields of the model of case 182: one line each. ``
>   - new: `` `purpose`, `method` and `checked` are one line each (the fields of the model of case 182). ``
>   - old: `Written from the Case since case 193 (case 350).`
>   - new: `Written from the Case (since case 193; case 350).`
>   - change: `each pointer stands in a bracket of its own`
> - [ ] update `rule-event-log`
>   - old: `` a refused call leaves no mark. Until case 136.1 the three skills wrote them through a `!` substitution where `CLAUDE_SESSION_ID` is empty, so every mark read `--------` (case 136.1). ``
>   - new: `` a refused call leaves no mark (until case 136.1 the three skills wrote them through a `!` substitution where `CLAUDE_SESSION_ID` is empty, so every mark read `--------`). ``
>   - old: `` **A limit lifted.** Until case 111 the `hi` line carried `--------` and the ledger hook looked for a `hi` after the last `session-start` of its own session, so two sessions open at once could not be told apart; on 2026-09-14 a session restored by `resume` in the same second took the `hi` of the session that typed it. With the stamp on the `hi` line a `hi` of one session never belongs to another (case 111.1). ``
>   - new: `` **A limit lifted.** With the stamp on the `hi` line a `hi` of one session never belongs to another, so two sessions open at once are told apart (until case 111 the `hi` line carried `--------` and the ledger hook looked for a `hi` after the last `session-start` of its own session, and on 2026-09-14 a session restored by `resume` in the same second took the `hi` of the session that typed it; case 111.1). ``
>   - change: `the history of the marks stands in the bracket of its pointer`
> - [ ] update `rule-git-context`
>   - old: `` From case 528 to case 787 the repository had no remote: `origin` had been the product repository this vault was split from and `migration` had no upstream, so the pull that stood first in this block failed at every session start. Since case 787 `origin` is the public repository `GUPPI` on GitHub, and `/hi` still runs no `git pull`. ``
>   - new: `` `/hi` runs no `git pull` (from case 528 to case 787 the repository had no remote: `origin` had been the product repository this vault was split from and `migration` had no upstream, so the pull that stood first in this block failed at every session start; since case 787 `origin` is the public repository `GUPPI` on GitHub). ``
>   - change: `the history of the remote stands in the bracket of its pointers`
> - [ ] update `rule-insights-schema`
>   - old: `` which archives it (`rule-sprint-close`, case 627.2); a recurrence ``
>   - new: `` which archives it as `rule-sprint-close` sets it (case 627.2); a recurrence ``
>   - old: `` it is kept for the recurrence until the close of its sprint, which archives it (`rule-sprint-close`, case 627.2). ``
>   - new: `` it is kept for the recurrence until the close of its sprint, which archives it as `rule-sprint-close` sets it (case 627.2). ``
>   - change: `the slug of rule-sprint-close stands outside the brackets of its pointers`
> - [ ] update `rule-internal-context`
>   - old: `` `orchestration.md` and `ratification.md` are listed since case 595, in place of `case-schema.md`, listed from case 273: they reach ``
>   - new: `` `orchestration.md` and `ratification.md` are listed in place of `case-schema.md` (since case 595; `case-schema.md` was listed from case 273): they reach ``
>   - old: `` `glossary.md` is listed since case 288.1: it left the `@` import of `CLAUDE.md`, which every subagent loads and none of them needs. ``
>   - new: `` `glossary.md` is listed here and not in the `@` import of `CLAUDE.md`, which every subagent loads and none of them needs (since case 288.1). ``
>   - old: `` `where-to-stop.md` is listed after `orchestration.md` since case 689.1: ``
>   - new: `` `where-to-stop.md` is listed after `orchestration.md` (since case 689.1): ``
>   - change: `each pointer stands in a bracket of its own`
> - [ ] update `rule-language`
>   - old: `` — English and Russian in this project (case 476.4). Until case 272 the rule was a section of the Render of `rule-claude-md`: a standing condition with no page and no Estimate. ``
>   - new: `` — English and Russian in this project (case 476.4; until case 272 the rule was a section of the Render of `rule-claude-md`, a standing condition with no page and no Estimate). ``
>   - change: `the history of the rule stands in the bracket of its pointer`
> - [ ] update `rule-ledger-tail`
>   - old: `` Shows at `/hi`, and at `/retro` since case 126, every ledger line ``
>   - new: `` Shows at `/hi` and at `/retro` (since case 126) every ledger line ``
>   - change: `the pointer stands in a bracket of its own`
> - [ ] update `rule-ledger-write`
>   - old: `` opens the next sprint first (`rule-sprint-close`, case 628.3). ``
>   - new: `` opens the next sprint first, as `rule-sprint-close` sets it (case 628.3). ``
>   - change: `the slug of rule-sprint-close stands outside the bracket of its pointer`
> - [ ] update `rule-lessons-schema`
>   - old: `` until the close of its sprint archives a `new` lesson of kind `error` (`rule-sprint-close`, case 627.2). ``
>   - new: `` until the close of its sprint archives a `new` lesson of kind `error`, as `rule-sprint-close` sets it (case 627.2). ``
>   - old: `` or, a `new` Lesson of kind `error`, at the close of its sprint (`rule-sprint-close`, case 627.2). ``
>   - new: `` or, a `new` Lesson of kind `error`, at the close of its sprint, as `rule-sprint-close` sets it (case 627.2). ``
>   - change: `the slug of rule-sprint-close stands outside the brackets of its pointers`
> - [ ] update `rule-materialize`
>   - old: `` so that the session that opens a sprint belongs to it (`rule-sprint-close`, case 628.3). ``
>   - new: `` so that the session that opens a sprint belongs to it, as `rule-sprint-close` sets it (case 628.3). ``
>   - change: `the slug of rule-sprint-close stands outside the bracket of its pointer`
> - [ ] update `rule-orchestration`
>   - old: `` The session that closes a sprint follows the skill `/sprint-close`, and the session that opens the next sprint the skill `/sprint-open`, which load only in those sessions (`rule-skill-sprint-close`, `rule-skill-sprint-open`, case 743.8). ``
>   - new: `` The session that closes a sprint follows the skill `/sprint-close` of `rule-skill-sprint-close`, and the session that opens the next sprint the skill `/sprint-open` of `rule-skill-sprint-open`, which load only in those sessions (case 743.8). ``
>   - old: `` whether each finding of `ask-guppi` not closed is fixed or left (`rule-prespec`, case 634.2) ``
>   - new: `` whether each finding of `ask-guppi` not closed is fixed or left, as `rule-prespec` sets it (case 634.2) ``
>   - old: `` since the record of a Case takes the marks of all its lines (`rule-page-generation`, case 673). ``
>   - new: `` since the record of a Case takes the marks of all its lines, as `rule-page-generation` sets it (case 673). ``
>   - change: `the slugs of shipped rules stand outside the brackets of their pointers`
> - [ ] update `rule-page-generation`
>   - old: `` a milestone item leaves its milestone only by a Case (`rule-sprint`, case 539.1). ``
>   - new: `` a milestone item leaves its milestone only by a Case, as `rule-sprint` sets it (case 539.1). ``
>   - change: `the slug of rule-sprint stands outside the bracket of its pointer`
> - [ ] update `rule-page-read`
>   - old: `` — in session 0051 an agent read the order of the `Stop` hooks from the History of `rule-hook-registry` ([[lesson-hooks-matching-hooks-of-one-event-run-in-parallel]]). ``
>   - new: `` — an agent read the order of the `Stop` hooks from the History of `rule-hook-registry` (in session 0051, [[lesson-hooks-matching-hooks-of-one-event-run-in-parallel]]). ``
>   - change: `the session stands in the bracket of the lesson`
> - [ ] update `rule-page-schemas`
>   - old: `` Prevents the shape of a page category from living in a file nobody ratified. Until case 304 the six `schema.yaml` and their `schema.md` stood outside the graph — no `purpose`, no History, no Estimate, changed by hand by an `update` with `file`. ``
>   - new: `` Prevents the shape of a page category from living in a file nobody ratified (until case 304 the six `schema.yaml` and their `schema.md` stood outside the graph — no `purpose`, no History, no Estimate, changed by hand by an `update` with `file`). ``
>   - change: `the history of the schemas stands in the bracket of its pointer`
> - [ ] update `rule-permissions`
>   - old: `A Grep whose path was that folder itself asked all the same in session 1448, so a second rule names the folder itself beside the rule for what lies inside it (case 693).`
>   - new: `A second rule names the folder itself beside the rule for what lies inside it, since a Grep whose path was that folder itself asked all the same (in session 1448, case 693).`
>   - change: `the session stands in the bracket of its pointer`
> - [ ] update `rule-prespec-hook`
>   - old: `` the hook runs the same judgment at the exit (case 561.3). Named `pretask` until case 261. ``
>   - new: `` the hook runs the same judgment at the exit (case 561.3; named `pretask` until case 261). ``
>   - change: `the old name stands in the bracket of its pointer`
> - [ ] update `rule-raw-archive`
>   - old: `` the session of the run still left out (`rule-sprint-close`, case 743.1). ``
>   - new: `` the session of the run still left out, as `rule-sprint-close` sets it (case 743.1). ``
>   - old: `` still gitignored (`rule-sprint-close`, case 743.3). ``
>   - new: `` still gitignored, as `rule-sprint-close` sets it (case 743.3). ``
>   - change: `the slug of rule-sprint-close stands outside the brackets of its pointers`
> - [ ] update `rule-render-harness`
>   - old: `` the renderer runs with lint and as the librarian's step after `cleanup` (case 89.1); the tick of case 226.2 belongs to that step. ``
>   - new: `` the renderer runs with lint and as the librarian's step after `cleanup` (case 89.1), and its tick of the render lines of the Spec belongs to that step (case 226.2). ``
>   - change: `the pointer stands in a bracket of its own`
> - [ ] update `rule-retro`
>   - old: `` `raw/<date>/<hi HHMM>/spec.md` (the session's folder, case 73), ``
>   - new: `` `raw/<date>/<hi HHMM>/spec.md` in the session's folder (case 73), ``
>   - old: `` a `guppi sprint-close` line (`rule-sprint-close`, case 628.1), ``
>   - new: `` a `guppi sprint-close` line, as `rule-sprint-close` names it (case 628.1), ``
>   - change: `the session's folder and the slug of rule-sprint-close stand outside the brackets of their pointers`
> - [ ] update `rule-retro-commit`
>   - old: `` has no ledger line (`rule-ledger-write`, case 122). ``
>   - new: `` has no ledger line, as `rule-ledger-write` sets it (case 122). ``
>   - change: `the slug of rule-ledger-write stands outside the bracket of its pointer`
> - [ ] update `rule-retro-onward`
>   - old: `and in session 1834 the run stopped there (case 596).`
>   - new: `and the run once stopped there (in session 1834, case 596).`
>   - old: `which Claude Code keeps set from that refusal until the person's next message, as the transcript of session 1237 shows;`
>   - new: `which Claude Code keeps set from that refusal until the person's next message (as the transcript of session 1237 shows);`
>   - change: `each session stands in a bracket`
> - [ ] update `rule-rules-schema`
>   - old: `` so the guard reads the field alike (`rule-sprint`, case 209.7). ``
>   - new: `` so the guard reads the field alike, as `rule-sprint` sets it (case 209.7). ``
>   - old: `seen by Obsidian since case 148.1 (case 166.1)`
>   - new: `seen by Obsidian (since case 148.1; case 166.1)`
>   - old: `` `case-schema.md` is listed here since case 273; the glossary arrives through ``
>   - new: `` `case-schema.md` is listed here (since case 273); the glossary arrives through ``
>   - change: `each pointer stands in a bracket of its own, the slug of rule-sprint outside it`
> - [ ] update `rule-search-leaves-out-decisions`
>   - old: `in the reading of session 1343 nine Greps over the wiki carried no exclusion, and one put it first, where it leaves nothing out.`
>   - new: `nine Greps over the wiki carried no exclusion, and one put it first, where it leaves nothing out (in the reading of session 1343).`
>   - change: `the session stands in a bracket`
> - [ ] update `rule-skill-grill-me`
>   - old: `It served the person's own interviews without a page until case 443.1.`
>   - new: `It served the person's own interviews without a page (until case 443.1).`
>   - old: `The question template is an indented code block, the form it took when case 443.1 was written, before case 444 let a fenced value carry a shorter fence.`
>   - new: `The question template is an indented code block (the form it took when case 443.1 was written, before case 444 let a fenced value carry a shorter fence).`
>   - change: `each pointer stands in a bracket of its own`
> - [ ] update `rule-skill-hi`
>   - old: `` is left by the `UserPromptSubmit` hook `guppi event prompt` (`rule-event-log`, case 111.1), which sees the session id; ``
>   - new: `` is left by the `UserPromptSubmit` hook `guppi event prompt` of `rule-event-log`, which sees the session id (case 111.1); ``
>   - old: `` closed `[x] … · case N` by the opening Case (`rule-sprint-close`, cases 628.7, 769.2); ``
>   - new: `` closed `[x] … · case N` by the opening Case, as `rule-sprint-close` sets it (cases 628.7, 769.2); ``
>   - old: `` a working file of the session (`rule-permissions`, case 363). ``
>   - new: `` a working file of the session, which `rule-permissions` allows (case 363). ``
>   - old: `` is taken whole and run by `/box` (`rule-spec-box`, case 591): ``
>   - new: `` is taken whole and run by `/box`, as `rule-spec-box` sets it (case 591): ``
>   - old: `` The skill writes no event line of its own since case 111.4: a `!` substitution never saw `CLAUDE_SESSION_ID` (every `hi` of sessions A–M carried `--------`), so the `hi` line is the `UserPromptSubmit` hook's, which reads the session id from its payload (`rule-event-log`, case 111.1). ``
>   - new: `` The skill writes no event line of its own (since case 111.4): a `!` substitution never saw `CLAUDE_SESSION_ID` (every `hi` of sessions A–M carried `--------`), so the `hi` line is written by the `UserPromptSubmit` hook of `rule-event-log`, which reads the session id from its payload (case 111.1). ``
>   - change: `each pointer stands in a bracket of its own, the slugs of shipped rules outside it`
> - [ ] update `rule-skill-sprint-close`
>   - old: `` Until case 743 these steps stood in a paragraph of `orchestration.md`, which every session loads. ``
>   - new: `` These steps stand apart from `orchestration.md`, which every session loads (until case 743 they stood in a paragraph of it). ``
>   - old: `` which `.claude/agents/librarian-guppi.md` runs ([[rule-sprint-close]], case 628.1). ``
>   - new: `` which `.claude/agents/librarian-guppi.md` runs as [[rule-sprint-close]] sets it (case 628.1). ``
>   - change: `each pointer stands in a bracket of its own, the link to rule-sprint-close outside it`
> - [ ] update `rule-skill-sprint-open`
>   - old: `` Until case 743 nothing set what the opening Case asks, and the steps of the turn of a sprint stood in `orchestration.md`, which every session loads. ``
>   - new: `` The skill sets what the opening Case asks, apart from `orchestration.md`, which every session loads (until case 743 nothing set it, and the steps of the turn of a sprint stood in `orchestration.md`). ``
>   - old: `marks the last sprint closed ([[rule-sprint]], case 743.5), and the person may type it too.`
>   - new: `marks the last sprint closed, as [[rule-sprint]] sets it (case 743.5), and the person may type it too.`
>   - change: `each pointer stands in a bracket of its own, the link to rule-sprint outside it`
> - [ ] update `rule-spec-capture`
>   - old: `` the person took that Spec at the Frontier (`rule-spec-box`, case 591). ``
>   - new: `` the person took that Spec at the Frontier, as `rule-spec-box` sets it (case 591). ``
>   - change: `the slug of rule-spec-box stands outside the bracket of its pointer`
> - [ ] update `rule-spec-reconcile`
>   - old: `Since case 441 the hooks alone write the Cases into the plan:`
>   - new: `The hooks alone write the Cases into the plan (since case 441):`
>   - old: `the comparison with a ratified copy that stood here from case 387.3 is gone (case 445.1).`
>   - new: `the comparison with a ratified copy that stood here is gone (from case 387.3 to case 445.1).`
>   - old: `` A payload the hook cannot read: exit 0 with one line on stderr; it never raises. Until case 445.1 the rule was a comparison: `guppi ratified --edit` on `PostToolUse` compared an edited plan with a ratified copy `<plan>.ratified.md` and marked a changed Case in `<plan>.waiting.json` for its showing; the copy, the marks and that hook are gone. ``
>   - new: `` A payload the hook cannot read: exit 0 with one line on stderr; it never raises (until case 445.1 the rule was a comparison: `guppi ratified --edit` on `PostToolUse` compared an edited plan with a ratified copy `<plan>.ratified.md` and marked a changed Case in `<plan>.waiting.json` for its showing; the copy, the marks and that hook are gone). ``
>   - change: `the history of the guard stands in the brackets of its pointers`
> - [ ] update `rule-spec-write`
>   - old: `` Until case 387 the agent wrote each Case into the plan file itself, translated from the chat, and nobody compared the two. Now `case-guppi` writes the whole Case in English, and a hook copies its stored answer (cases 437, 441). ``
>   - new: `` `case-guppi` writes the whole Case in English, and a hook copies its stored answer (cases 437, 441; until case 387 the agent wrote each Case into the plan file itself, translated from the chat, and nobody compared the two). ``
>   - change: `the history of the hook stands in the bracket of its pointers`
> - [ ] update `rule-sprint`
>   - old: `` its status kept in the record of the close (`rule-sprint-close`, case 632.3) ``
>   - new: `` its status kept in the record of the close, as `rule-sprint-close` sets it (case 632.3) ``
>   - change: `the slug of rule-sprint-close stands outside the bracket of its pointer`
> - [ ] update `rule-synthesis`
>   - old: `` its `error` lessons that joined no Insight (`rule-sprint-close`, case 627.5). ``
>   - new: `` its `error` lessons that joined no Insight, as `rule-sprint-close` sets it (case 627.5). ``
>   - change: `the slug of rule-sprint-close stands outside the bracket of its pointer`
> - [ ] update `rule-work-mode`
>   - old: `` the librarian runs it, and the command ticks it (`rule-sprint-close`, case 628.4). ``
>   - new: `` the librarian runs it, and the command ticks it, as `rule-sprint-close` sets it (case 628.4). ``
>   - change: `the slug of rule-sprint-close stands outside the bracket of its pointer`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] `uv run guppi render`: `vault/wiki/rules/schema.yaml`
> - [ ] `uv run guppi render`: `vault/wiki/entities/schema.yaml`
> - [ ] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`
> - [ ] `uv run guppi render`: `vault/wiki/decisions/schema.yaml`
> - [ ] `uv run guppi render`: `vault/wiki/lessons/schema.yaml`
> - [ ] `uv run guppi render`: `vault/wiki/insights/schema.yaml`
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] `uv run guppi render`: `.claude/skills/carry/SKILL.md`
> - [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
> - [ ] `uv run guppi render`: `.claude/skills/work/SKILL.md`
> - [ ] `uv run guppi glossary`
> - [ ] read `estimate-clean-branch-pages-hold-pointers-only-in-brackets`

> **ratification:**
> ```
> - decision[case 809][create][estimate-clean-branch-pages-hold-pointers-only-in-brackets]{ref:rule-clean-branch}{tags:ci,plugin}
> - decision[case 809][update][entity-glossary]{ref:entity-glossary}
> - decision[case 809][update][entity-sprint]{ref:entity-sprint}
> - decision[case 809][update][entity-sprint-plugin]{ref:entity-sprint-plugin}
> - decision[case 809][update][rule-agent-writing]{ref:rule-agent-writing}
> - decision[case 809][update][rule-backlog]{ref:rule-backlog}
> - decision[case 809][update][rule-brief]{ref:rule-brief}
> - decision[case 809][update][rule-carry-over]{ref:rule-carry-over}
> - decision[case 809][update][rule-case-build]{ref:rule-case-build}
> - decision[case 809][update][rule-case-check]{ref:rule-case-check}
> - decision[case 809][update][rule-case-example]{ref:rule-case-example}
> - decision[case 809][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 809][update][rule-claude-md]{ref:rule-claude-md}
> - decision[case 809][update][rule-cleanup]{ref:rule-cleanup}
> - decision[case 809][update][rule-decisions-schema]{ref:rule-decisions-schema}
> - decision[case 809][update][rule-documentation]{ref:rule-documentation}
> - decision[case 809][update][rule-end-of-work]{ref:rule-end-of-work}
> - decision[case 809][update][rule-entities-schema]{ref:rule-entities-schema}
> - decision[case 809][update][rule-estimates-schema]{ref:rule-estimates-schema}
> - decision[case 809][update][rule-event-log]{ref:rule-event-log}
> - decision[case 809][update][rule-git-context]{ref:rule-git-context}
> - decision[case 809][update][rule-insights-schema]{ref:rule-insights-schema}
> - decision[case 809][update][rule-internal-context]{ref:rule-internal-context}
> - decision[case 809][update][rule-language]{ref:rule-language}
> - decision[case 809][update][rule-ledger-tail]{ref:rule-ledger-tail}
> - decision[case 809][update][rule-ledger-write]{ref:rule-ledger-write}
> - decision[case 809][update][rule-lessons-schema]{ref:rule-lessons-schema}
> - decision[case 809][update][rule-materialize]{ref:rule-materialize}
> - decision[case 809][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 809][update][rule-page-generation]{ref:rule-page-generation}
> - decision[case 809][update][rule-page-read]{ref:rule-page-read}
> - decision[case 809][update][rule-page-schemas]{ref:rule-page-schemas}
> - decision[case 809][update][rule-permissions]{ref:rule-permissions}
> - decision[case 809][update][rule-prespec-hook]{ref:rule-prespec-hook}
> - decision[case 809][update][rule-raw-archive]{ref:rule-raw-archive}
> - decision[case 809][update][rule-render-harness]{ref:rule-render-harness}
> - decision[case 809][update][rule-retro]{ref:rule-retro}
> - decision[case 809][update][rule-retro-commit]{ref:rule-retro-commit}
> - decision[case 809][update][rule-retro-onward]{ref:rule-retro-onward}
> - decision[case 809][update][rule-rules-schema]{ref:rule-rules-schema}
> - decision[case 809][update][rule-search-leaves-out-decisions]{ref:rule-search-leaves-out-decisions}
> - decision[case 809][update][rule-skill-grill-me]{ref:rule-skill-grill-me}
> - decision[case 809][update][rule-skill-hi]{ref:rule-skill-hi}
> - decision[case 809][update][rule-skill-sprint-close]{ref:rule-skill-sprint-close}
> - decision[case 809][update][rule-skill-sprint-open]{ref:rule-skill-sprint-open}
> - decision[case 809][update][rule-spec-capture]{ref:rule-spec-capture}
> - decision[case 809][update][rule-spec-reconcile]{ref:rule-spec-reconcile}
> - decision[case 809][update][rule-spec-write]{ref:rule-spec-write}
> - decision[case 809][update][rule-sprint]{ref:rule-sprint}
> - decision[case 809][update][rule-synthesis]{ref:rule-synthesis}
> - decision[case 809][update][rule-work-mode]{ref:rule-work-mode}
> ```
