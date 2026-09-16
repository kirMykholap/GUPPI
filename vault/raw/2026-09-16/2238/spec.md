<!-- approved 01:26:48 · session cf5992b5 -->

# Spec — 2026-09-16, session 2238

## Case 209 — `rule-sprint`: the sprint as a page, `sprint.md` as its render

> **context:**
> `sprint.md` is the backlog of the sprint `migration`: the goal, the Definition of done, the Slices. It is a working file without a schema: `index.md` §1 says the librarian writes it, lint does not check it, `rule-brief` tells the librarian to change it "only when `handoff.md` tells you to", `/hi` reads it whole through `rule-internal-context`, `cleanup` and `archive` take the sprint id from its first `## migration` heading. The vault, asked through `ask-guppi`: no sprint page, no field from an Entity to a Rule, no render of `sprint.md`; the slugs `rule-sprint` and `entity-sprint-migration` are free; the tag `sprint` is not declared. The governed-files hook (`guppi/guard.py`) refuses an edit of any file a live Rule page names in `governs`, whatever the rule's force. `built` is computed by the cascade of `generate` once every Estimate of the page is `passed`. This Case touches no Estimate: the page is new; its Estimate is created by 209.1.

> **problem:**
> The close of an item in a session does not reach the sprint: the file is rewritten by hand a session later, and each time it is a Case of its own (F7 today, flag 5 of the handoff). No mechanism lets the `built` of a page close an item of the backlog. The sprint is the one file that says what gets built, and the one file whose state nobody computes.

> **given:**
> The cascade of `generate` computes `built` on an Entity or a Rule once each of its Estimates is `passed`; `cleanup` sets `archived`.
> **＋** The guard refuses `Edit` and `Write` of a file a live Rule page names in `governs`.
> **＋** `sprint_id` reads the first `## <id>` heading of `sprint.md`.
> **＋** Order is the content of a page, not a field of an Entity MOC (`index.md` §6).
> **－** The script writes no page of `wiki/`: it reads statuses and writes one file.

> **when:**
> The librarian runs `uv run guppi sprint` after `cleanup` and `render`, before the brief.

> **then:**
> The rule `rule-sprint` is a child of `rule-documentation`, where `generate` puts it, with `implementation_ref: [guppi/sprint.py, tests/test_sprint.py]` and `governs: vault/wiki/sprint.md`.
> **＋** A hand edit of `sprint.md` is refused by the guard with the same line as for a harness file.
> **＋** The backlog changes only by an `update` of the page `entity-sprint-migration` — a Case, not the librarian, not a hand.
> **－** Neither `sprint_id` nor the archive path changes: the `## migration` heading stays the first of the file.

```then
create:
  - slug: rule-sprint
    type: rule
    kind: Leaf
    ref: rule-documentation
    purpose: Prevents the sprint's backlog from drifting from the pages it names
    enforcement: check
    implementation_ref: [guppi/sprint.py, tests/test_sprint.py]
    governs: vault/wiki/sprint.md
    tags: [session, workflow, harness, librarian, sprint]
    sections:
      Purpose: |
        Prevents the sprint's backlog from drifting from the pages it names. The sprint is
        a page — an Entity MOC whose `estimates` are its Definition of done and whose
        `## Backlog` lists the open Slices, each item a wikilink to a page. `vault/wiki/sprint.md`
        is not a document: `guppi sprint` writes it from that page, one tick per item by the
        status of the page it names. The librarian runs the script after `cleanup` and
        `render`, before the brief, so the file shows the pages of that same run; `/hi`
        reads the file as before. `governs` names the file, so the governed-files hook
        refuses a hand edit; the backlog changes by an `update` of the sprint page, a Case.
        The first `## <id>` heading of the file is the sprint id `sprint_id`, `cleanup` and
        `archive` read, unchanged.
new_tags:
  - tag: sprint
    meaning: the sprint page, its backlog and its render
    aliases: спринт
```

```tasks
- [ ] create `rule-sprint` (`ref: rule-documentation`)
- [x] `guppi/sprint.py`; the command `guppi sprint` in `guppi/cli.py`; `tests/test_sprint.py`
- [x] `new_tags`: `sprint` — «спринт»
- [x] `make style`, `make test`
```

### Case 209.1 — the render of the backlog by statuses

> **when:**
> `guppi sprint` runs with a live page `entity-sprint-migration`.

> **then:**
> The file `vault/wiki/sprint.md` gets: `# Sprint`; `## <id>`, the id being the page's slug without `entity-sprint-`; the text of the page's `## Purpose` as it is; `**Done when**` — one line per Estimate of the page's `estimates`: `- [x]` when `passed`, `- [ ]` otherwise, then the Estimate's `purpose` and its status.
> **＋** Then the page's `## Backlog`: each `### <Slice>` as a heading, each item line `- [[slug]] — <text>` as `- [x]` when the page `slug` is `built`, `passed` or `archived`, `- [ ]` otherwise, with its status and, when present, its `deferred_by` after ` · `.
> **＋** A Slice whose every item is `[x]` gets `[x]` in its heading; a Slice without items stays open.
> **＋** The page's `## Closed` section is copied as it is, after the backlog.
> **－** An item whose `slug` has no live or archived page: one line on stderr, exit 1, the file not written.
> **－** The file holds nothing beyond this: no line by hand, no history.

```then
create:
  - slug: estimate-sprint-renders-the-backlog
    type: estimate
    ref: rule-sprint
    kind: QA
    purpose: guppi sprint writes sprint.md from the sprint page, one tick per item by the status of the page it names
    method: pytest tests/test_sprint.py, plus one reading of the rendered sprint.md after the librarian's run
    tags: [harness, sprint]
```

```tasks
- [ ] create `estimate-sprint-renders-the-backlog` (`ref: rule-sprint`)
- [x] `guppi/sprint.py`: read the page, statuses through `guppi/pages.py`, write the file; tests first
- [ ] read `estimate-sprint-renders-the-backlog`
```

### Case 209.2 — `entity-sprint-migration` and the first promise: lint clean

> **given:**
> Items 1–4 of the Definition of done are today what `make lint` checks: fields by schema, Estimate pages present, no broken ref, no orphan, no status contradiction.
> **＋** Lint counts the 62 findings of the Decision pages of Cases 1–28 today.

> **when:**
> Someone reads `make lint` at the close of the sprint.

> **then:**
> `make lint` exits 0: no finding in any category, `unmigrated` included — the old Estimate shape is gone, the counter at zero; the one exception is `unread` on the Estimates of the sprint page itself not yet read at that moment.
> **＋** The page `entity-sprint-migration` exists: an Entity MOC, `purpose` the goal of the sprint; `## Purpose` the goal and "open since 2026-09-09"; `## Backlog` — `### Slice 3b`: `rule-work-mode`, `rule-subagent-guppi`; `### Slice 4`: the item of the promise of 209.3; `### Slice 5`: the items of the Estimates of 209.2–209.4 and `rule-spec-box`; `## Closed` — Slices 0–3d in one paragraph, 3d closed by session 1955, the recut remainder 42 by lint.
> **－** Item F7 is not done on its own: today's `sprint.md` is replaced by the first render.

```then
create:
  - slug: entity-sprint-migration
    type: entity
    kind: MOC
    purpose: The repository works by the model in wiki/index.md — Phase 1 and Phase 2 of docs/migration/migration-plan.md closed
    tags: [sprint, workflow]
    sections:
      Purpose: |
        Open since 2026-09-09. The repository works by the model in `wiki/index.md`: Phase 1
        (the harness built by its own rules) and Phase 2 (the surviving pages brought into
        conformance) of `docs/migration/migration-plan.md` are closed. Done when the three
        Estimates of this page pass: lint clean, the leftovers gone, the branch merged.
      Backlog: |
        ### Slice 3b — Work Mode

        - [[rule-work-mode]] — Work Mode: the Spec as tasks with code, the ticked boxes in `spec.md`, the test of each Estimate written first and turned green; cases 183, 206
        - [[rule-subagent-guppi]] — what a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case; cases 183, 206

        ### Slice 4 — conversion of the parked pages by group

        - [[estimate-sprint-migration-leftovers-gone]] — every page of `vault/parked/` and every document of 2026-08 under `docs/` converted, archived or deleted by a decision

        ### Slice 5 — closing

        - [[estimate-sprint-migration-lint-clean]] — `make lint` exit 0: the 31 Decision pages of Cases 1–28 decided, `unmigrated` at zero
        - [[estimate-sprint-migration-merges]] — `make test` green, `migration` merged into `main`
        - [[rule-spec-box]] — the Spec box, case 207, after Slice 3b
      Closed: |
        Slices 0–2 closed by 2026-09-10: layout; ledger, event log, `/hi`; renderer, lint,
        indexes, `/ask`, pre-task. Slice 3 (materialize, generate, cleanup, librarian, retro,
        handoff) built 2026-09-10, closed 2026-09-12. Slice 3c (the raw lifecycle: the archive
        of an applied session, the tail, one archive root, the ledger of a session, the status
        cascades, the slug checked against the archive) built 2026-09-13. Slice 3d (the
        Estimate model, case 182) opened and closed 2026-09-16: Cases 187–190 ratified in
        session 1034 and conserved, repaired by 193–198 and built in session 1651, case 191
        taken up by 201–203 and built in session 1955 — `generate`, `lint`, `pre-task` by the
        model. The recut of each old Estimate at its first touch runs on past the Slice: lint
        counts the remainder as `unmigrated` (42 at the close of 3d) and the old shape is
        removed when it reaches zero. Kept without a page: `/grill-me`; `git pull` in `/hi`
        without an upstream (decision 11.1); `gh` not logged in, no GitHub remote (11.2) —
        both decided again at the close (`estimate-sprint-migration-leftovers-gone`).
  - slug: estimate-sprint-migration-lint-clean
    type: estimate
    ref: entity-sprint-migration
    kind: QA
    purpose: make lint exits 0 at the close of the sprint, unmigrated included, but for the unread of the sprint page's own Estimates
    method: make lint, exit 0 — or only unread lines on the Estimates of entity-sprint-migration
    tags: [sprint, tests]
```

```tasks
- [ ] create `entity-sprint-migration` (no `ref`; `kind: MOC`; `sections: Purpose, Backlog, Closed`)
- [ ] create `estimate-sprint-migration-lint-clean` (`ref: entity-sprint-migration`)
- [ ] the first `uv run guppi sprint` in Work Mode — `sprint.md` replaced by the render
- [ ] read `estimate-sprint-migration-lint-clean`
```

### Case 209.3 — the second promise: the leftovers gone

> **given:**
> Slice 4 and Slice 5 today list things outside the vault: `vault/parked/`, `docs/superpowers/`, `docs/HANDOFF.md`, `docs/migration/rule-*.md`, the 2026-08 documents under `docs/`, the old `vault/archive/` of August, the `raw/<date>/` folders holding only an `event_log.md`, decisions 11.1 and 11.2.

> **when:**
> Someone reads the tree of the repository at the close of the sprint.

> **then:**
> `vault/parked/` is empty or absent: each of its pages became a live vault page or lies in the archive.
> **＋** Under `docs/` no 2026-08 document and no `docs/migration/rule-*.md` remains; each became a page, was archived, or was deleted by a decision named in the reading.
> **＋** `vault/archive/` has no root outside `<sprint>/`; `raw/` has no date folder without a session.
> **＋** A decision stands on `git pull` without an upstream and on `gh` without a login — keep as is, or repair — and is named in the reading.
> **－** What to do with each thing this promise does not decide: those are the Cases of Slices 4 and 5.

```then
create:
  - slug: estimate-sprint-migration-leftovers-gone
    type: estimate
    ref: entity-sprint-migration
    kind: QA
    purpose: vault/parked/, the 2026-08 documents, the old archive root and the empty raw date folders are gone by decision at the close of the sprint
    method: one reading of the tree by hand at the close of the sprint, each path and decision named in the estimate line
    tags: [sprint, git]
```

```tasks
- [ ] create `estimate-sprint-migration-leftovers-gone` (`ref: entity-sprint-migration`)
- [ ] read `estimate-sprint-migration-leftovers-gone`
```

### Case 209.4 — the third promise: the branch merged

> **when:**
> Someone reads `git log` of `main` at the close of the sprint.

> **then:**
> `make test` is green on the last commit of `migration`.
> **＋** `migration` is merged into `main`; the last brief is written by the librarian on `main`.
> **＋** The cascade sets `entity-sprint-migration` `built` — that is the close of the sprint; the render shows the three Done-when lines `[x]`.

```then
create:
  - slug: estimate-sprint-migration-merges
    type: estimate
    ref: entity-sprint-migration
    kind: QA
    purpose: make test green on the last commit of migration and the branch merged into main
    method: make test on the last commit of migration, then git log of main after the merge
    tags: [sprint, git, tests]
```

```tasks
- [ ] create `estimate-sprint-migration-merges` (`ref: entity-sprint-migration`)
- [ ] read `estimate-sprint-migration-merges`
```

### Case 209.5 — the librarian's step

> **given:**
> `rule-documentation` is a render MOC; its Render is the frame of `.claude/agents/librarian-guppi.md`; the steps `cleanup` and `render` are named in the frame by name.
> **＋** An `update` of a Render touches the Estimate of the live reading of that Render — `estimate-documentation-completes` (case 187).

> **when:**
> The librarian walks the frame after `render`.

> **then:**
> The frame names the step: "Run `uv run guppi sprint`. Every line on its stderr is a flag" — after `render`, before the brief.
> **＋** The Criterion of `estimate-documentation-completes` gains one line: `guppi sprint` runs after `render` and before the brief; the rest of the Criterion stands as it is.

```then
update:
  - slug: rule-documentation
    replace:
      - old: |
          4. Run `uv run guppi render`. The pages are final after cleanup, so the governed
             files are written from them here. Every line on its stderr is a flag; a file it
             could not write is left to the next session start.
        new: |
          4. Run `uv run guppi render`. The pages are final after cleanup, so the governed
             files are written from them here. Every line on its stderr is a flag; a file it
             could not write is left to the next session start.

          5. Run `uv run guppi sprint`. It writes `vault/wiki/sprint.md` from the sprint page
             by the statuses of this run. Every line on its stderr is a flag.
    change: step 5 of the frame — guppi sprint after render, before the brief (case 209.5)
  - slug: estimate-documentation-completes
    set: {status: pending, method: "make test-documentation, the pipeline over tests/test_materialize.py, tests/test_generate.py and tests/test_cleanup.py; the live reading by hand"}
    sections:
      Criterion: |
        make test-documentation runs the tests of materialize, generate and cleanup as one
        pipeline, green. Live, after a librarian run: every decision line of the session's
        ledger has a Decision page and its target page; no page exists that no ledger line
        produced; the agent read only handoff.md, the yamls materialize named, the four
        indexes and tags.md, plus the wiki pages it names in the report with one of the
        four reasons of its frame (same or near; a candidate cluster; a script's error; a
        fact for the brief) and the outcome, and no ledger, Spec, plan, Decision page or archive file (the Makefile,
        guppi/ and tests/ are the scripts' own and may be read); it edited no yaml entry beyond the marks and the entries of the index
        check and the synthesis; its commands are in event_log.md; its commit is separate
        from the session's; it did not stop to ask.

        ### case 73.8

        When:
        `librarian-guppi` starts.

        Then:
        Its first input is the `handoff.md` the dispatch names, `raw/<hi date>/<hi HHMM>/handoff.md`;
        the other three inputs are unchanged.

        ### case 89.1

        When:
        The librarian reaches the end of its run.

        Then:
        After `cleanup` and before the brief it runs `uv run guppi render`, and the governed
        files are written from the pages of that same run.
        **＋** Every line on its stderr is a flag for the brief.
        **＋** After `render` and before the brief it runs `uv run guppi sprint`; every line on its stderr is a flag (case 209.5).
        **＋** `make lint` at the close then passes its `render --check` step.
        **－** A file the render could not write is left to the next session start; the librarian
        does not write it by hand.

        ### case 90.3

        When:
        The handoff tells the librarian to do what the criterion of `rule-documentation` forbids
        — repair an entry of the yaml, or read `ledger.md`, a Spec, a decision page or the
        archive.

        Then:
        The librarian does not do it.
        **＋** It names the instruction in the report: what was asked, and why it was refused.
        **－** The handoff itself is checked by nothing: it is written from memory, and the
        refusal is the librarian's work, not its author's.
        **－** A refusal does not stop the run: the librarian asks no questions, the person is
        gone.

        ### case 100.2

        When:
        The librarian works by its frame (the Render of `rule-documentation`).

        Then:
        A step between Brief and Close (shown again at pre-task: the brief reads the yamls the walk named, so the archive runs after it): "Archive. Run `uv run guppi archive`. Every line on its stderr is a flag; the units it moved and the units it kept, with the reason, go into the report." The brief is already written; the commit picks the move up.
        **＋** `rule-raw-archive` is the sixth child of `rule-documentation`, after `rule-cleanup`.
        **＋** The ban on reading `vault/archive/` stays.
        **＋** The session of the run is found as `cleanup` finds it — the latest `<HHMM>/` folder of the run day, else the nearest date back — and is skipped even when dated before the run day (a session across midnight).
        **＋** `estimate-documentation-completes` gets a `### case 100.2` block, `pending`.

        ### case 147.5

        When:
        `guppi render` writes `librarian-guppi.md`.

        Then:
        "Your inputs are three: the `handoff.md` …, every `materialize.yaml` …, and `vault/wiki/tags.md`; the index lines you compare with are the Greps `rule-index-check` and `rule-synthesis` name"; the four reasons to open a page — as they are.
    change: one line in the block of case 89.1 — guppi sprint after render and before the brief (case 209.5)
```

```tasks
- [ ] update `rule-documentation`: one `replace` in the Render — the step after `render`
- [ ] update `estimate-documentation-completes`: `sections: Criterion` — the current text plus the line on `guppi sprint`; `set: {status: pending}`
- [ ] `guppi render`: `.claude/agents/librarian-guppi.md`; `render --check` exit 0
- [ ] read `estimate-documentation-completes`
```

### Case 209.6 — the librarian no longer writes `sprint.md`

> **given:**
> The Render of `rule-brief` holds the sentence "Change `vault/wiki/sprint.md` only when `handoff.md` tells you to, and only as it says"; the Criterion of `estimate-brief-written` repeats it in its last line.

> **when:**
> The librarian writes the brief.

> **then:**
> The brief says nothing about an edit of `sprint.md`; the sentence is gone from the Render.
> **＋** A handoff flag that asks for a change of the sprint goes into the Flags of the brief as a Case of the next Plan Mode — the librarian does not carry it out.
> **＋** The Criterion of `estimate-brief-written`: its last line reads "The brief states no decision and no judgment of the work; a change of the sprint is a Case, never the librarian's edit"; the rest of the text stands as it is.

```then
update:
  - slug: rule-brief
    replace:
      - old: "and flags only. Add no decision and no judgment of the work. Change `vault/wiki/sprint.md` only when `handoff.md` tells you to, and only as it says."
        new: "and flags only. Add no decision and no judgment of the work. A handoff flag that asks for a change of the sprint goes into Flags as a Case of the next Plan Mode; the sprint page changes by a Case, and `vault/wiki/sprint.md` is written by `guppi sprint`, never by you (case 209.6)."
    change: the librarian never edits sprint.md — a sprint change is a Case, the file is the render of guppi sprint (case 209.6)
  - slug: estimate-brief-written
    set: {status: pending, method: "one reading by hand after the first librarian run, recorded in the estimate line"}
    sections:
      Criterion: |
        Given:
        The librarian writes `brief.md` by the frame — the Render of `rule-brief` — after `generate`, from the yaml of the run, `handoff.md` and the output of `make lint`.
        **＋** A fact no input carries — the status of an Estimate, the `severity` of an Insight — is read from the page, and the page is named in the report.
        **－** The brief of `/carry` is the promise of `estimate-carry-over-writes`, not of this one.

        When:
        The librarian rewrites `vault/wiki/brief.md` at the end of its run.

        Then:
        The brief holds five sections in order: Where things stand, Readings due, Deferred, Flags, Readings at the close.
        **＋** Where things stand — from "What actually got done" of `handoff.md` and the counts of the yaml: pages created and updated per category.
        **＋** Readings due — every Estimate `pending` or `failed` after `generate`: the Estimate, the rule that stands `draft`, and where it is read — from the unticked `read` line of the session's Spec or from the page's `method`; a `failed` one first, with the result of its reading in one line; nothing from the previous brief.
        **＋** Deferred — at most seven: the targets of the `defer` entries of this run, the items of the previous list whose decision no `supersedes` retired, every `open` Insight; ranked by `severity` — its own or that of the related Insight — then by the number of briefs the item stood in; an Insight's line carries its slug, `severity`, `pattern` and its Proposal in one or two sentences.
        **＋** Flags, no limit: entries `incomplete`, `failed`, `near`, `unparsed`; `failed` Estimates; MOC candidates; stale defers; contradictions; the lint output; a handoff flag that asks for a change of the sprint, as a Case of the next Plan Mode.
        **＋** Readings at the close — `make test`, `make lint`, page counts.
        **－** The brief states no decision and no judgment of the work; a change of the sprint is a Case, never the librarian's edit.
    change: the last line of the Criterion — a change of the sprint is a Case, never the librarian's edit; the sprint flag lands in Flags (case 209.6)
```

```tasks
- [ ] update `rule-brief`: one `replace` in the Render
- [ ] update `estimate-brief-written`: `sections: Criterion` — the current text with the last line replaced; `set: {status: pending}`
- [ ] `guppi render`; `render --check` exit 0
- [ ] read `estimate-brief-written`
```

### Case 209.7 — the Rule-class files

> **when:**
> Someone reads the map, the glossary and the rules schema after Work Mode.

> **then:**
> `index.md` §1: `sprint.md` is the file `guppi sprint` writes from `entity-sprint-migration`; not a page, no schema, lint does not check it, the guard refuses a hand edit.
> **＋** `glossary.md`, the Sprint row: the sprint is an Entity MOC with its Estimates as the Definition of done and the backlog in its body; `sprint.md` is its render.
> **＋** `rules/schema.md`: `governs` is allowed on a `check` rule whose script writes the file; the guard reads the field the same way.
> **－** `rule-claude-md` is not touched: "`sprint.md` names the slices" stays true.

```then
update:
  - slug: index
    file: vault/wiki/index.md
    change: "§1 — sprint.md is the file guppi sprint writes from entity-sprint-migration: not a page, no schema, exempt from lint, a hand edit refused by the guard (case 209.7)"
  - slug: glossary
    file: vault/wiki/glossary.md
    change: "the Sprint row — an Entity MOC whose Estimates are the Definition of done and whose body holds the backlog; sprint.md its render, written by guppi sprint (case 209.7)"
  - slug: rules-schema
    file: vault/wiki/rules/schema.md
    change: "governs allowed on a check rule whose script writes the file; the guard reads the field alike (case 209.7)"
```

```tasks
- [x] update `index.md` (`file`, `change`), by hand
- [x] update `glossary.md`, by hand
- [x] update `rules/schema.md`, by hand
```

## Case 210 — the stray `ref` field on Estimate pages

> **context:**
> The Estimate schema (`estimates/schema.md`) names the fields of the page: `type`, `kind`, `status`, `target`, `purpose`, `method`, `checked`, `origin`, `sprint`, `created`, `tags`; the link to the target is `target`. Before case 208 `materialize` lifted every key of a `then` item into `fields`, and the item's `ref` landed on the page as a field; the code was fixed in session 1955 (`lesson-materialize-item-ref-lifted-as-a-page-field`, clustered under `insight-materialize-lift-loses-a-schema-field`). The pages remain: today 15 Estimate pages of cases 188, 189 and 190 carry `ref:` — not 13 as the handoff said: `estimate-carry-over-writes`, `-case-protocol-acknowledging-reply`, `-case-protocol-case-form`, `-case-protocol-ledger-line-form`, `-hi-writes-frontier`, `-materialize-fails-alone`, `-materialize-finds-a-rule-class-item`, `-materialize-lifts-a-lesson`, `-materialize-marks-exists`, `-materialize-marks-superseded`, `-materialize-shows`, `-materialize-skips-a-carried-over-unit`, `-plan-mode-names-its-estimates`, `-render-sync-reports`, `-spec-capture-offers-the-fork`. Lint does not count a field the schema does not know. `set` in `generate` assigns a value and cannot remove a key. This Case touches no Estimate: no rule changes.

> **problem:**
> Fifteen pages carry a field the schema does not have and nobody ratified; it doubles `target` and will one day diverge from it. An `update` cannot remove it — `set` does not delete; fifteen `update` lines for one mechanical fix is noise in the ledger without content.

> **given:**
> The Estimate schema names the fields of the page, and `ref` is not one of them; the link to the target is `target`.
> **＋** A page's History takes a line written by hand, with a date and a source.
> **－** `generate` takes no part: `set` does not remove a key.

> **when:**
> Someone reads the frontmatter of the pages under `vault/wiki/estimates/` after Work Mode.

> **then:**
> No Estimate page carries a `ref` field; `target` on each stands as it was.
> **＋** Each of the fifteen pages carries a History line: `- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210`.
> **＋** The edit is a script's, run once from the scratchpad by path — `index.md` §1: the scripts are the only writers to `wiki/`.
> **－** Nothing else on these pages changes; `make lint` gets no new finding.

```then
migration:
  - what: a one-off script removes the `ref:` line from the frontmatter of every page under vault/wiki/estimates/ and appends the History line on each
    pages: 15
```

```tasks
- [x] one-off migration script, run once by path: remove `^ref: ` from the 15 pages under `vault/wiki/estimates/`, append the History line on each
- [x] `make lint`: no new finding; `git diff --stat` — exactly 15 files
```

## Case 211 — a recut brings the page to the shape of the model

> **context:**
> A recut is the first touch of an old Estimate page: an `update` that replaces the Criterion whole and sets `pending` (cases 193, 201–204). `generate` then writes `sections` and `set`, and keeps `## Context` and `## Method` "where a page carries them" (`estimate-generate-writes`, `estimates/schema.md`); the field `method` appears only on pages born after 193. So the six recuts of session 1955 stayed in the old shape: five — `estimate-generate-writes`, `-generate-walks-dates`, `-lint-catches`, `-pretask-reconciles`, `-materialize-assembles` — without a `method` field and with the two old sections; the sixth, `estimate-case-protocol-case-form`, is in the shape of the model. Lint counts the remainder as `unmigrated` (42) and drops the checks of the old shape once the counter reads zero (case 202). `index.md` §7, `case-schema.md`, `estimates/schema.md` and `schema.yaml` say "until the recut" and do not say what a recut must do. This Case touches two promises of `rule-page-generation` — `estimate-generate-writes` (the shape of the page) and `estimate-generate-fails-alone` (the refusal) — one per sub-case; `-cascades`, `-walks-dates` and `-writes-the-decision-page` it does not touch.

> **problem:**
> A recut that leaves the page in the old shape is no recut: the `unmigrated` counter does not fall, and the page gets a third state — a new Criterion beside the old sections — while lint reads its `method` from the section. Nobody has to write `set: {method: …}` and `generate` does not have to drop the sections, so both forget.

> **given:**
> `guppi generate` applies `set` to the frontmatter and `sections` as whole replacements; the failure of one entry touches no other (`estimate-generate-fails-alone`).
> **＋** The field `method` is one line; `## Method` of the old shape is the same text as a section.
> **＋** The tests in `tests/test_generate.py` fix the behaviour; the live reading is the librarian's run of this session.
> **－** `lint`, `materialize` and `pretask` do not change.

### Case 211.1 — `set.method` drops the old sections

> **when:**
> `guppi generate` applies an `update` to an Estimate page, and `set` carries `method`.

> **then:**
> The field `method` is written after `purpose`; the sections `## Context` and `## Method`, where the page carries them, are dropped; the other sections stand.
> **＋** History: `updated: <change>`, as for any `update`.
> **－** An `update` without `set.method` touches no section: a page nobody recuts stays as it is.

```then
update:
  - slug: estimate-generate-writes
    set: {status: pending, method: "pytest in tests/test_generate.py against a temp vault; the live reading once by hand"}
    sections:
      Criterion: |
        Given:
        `guppi generate` applies the entries of a `materialize.yaml` in order; the `sections` of an `update` entry are whole replacements, `set` writes fields.
        **＋** An `update` entry for an Estimate carries `sections.Criterion` and `set: {status: pending}`; a `create` entry carries `kind`, `purpose`, `method`, `tags` as fields (194.1).
        **＋** An `estimate` entry carries `status` and `result`; the `result` opens with the date of the reading and the command (199).
        **＋** The tests in `tests/test_generate.py` fix the behaviour; the live reading is the librarian's run of this session.
        **－** `materialize`, `cleanup` and `lint` do not change here.

        When:
        `guppi generate` applies one entry of a yaml to a page.

        Then:
        A `create` becomes a page: `type`, the fields of the entry, `status` by category (entity and rule `draft`, estimate `pending`, lesson `new`, insight `open`), `origin`, `sprint` — the first `## <id>` of `sprint.md`, `created` — the yaml's date, `tags`; the body sections from `sections`, `## Purpose` from `purpose` on a rule or an entity; a `ref` lands in the parent's `children` or the target's `estimates` with History `child <slug> added` / `estimate <slug> added`, at the end of the run when the parent comes later in the yaml.
        **＋** An Estimate page carries `purpose`, `method` and `checked` as fields, in that order after `target`; `## Criterion` from `sections`; neither `## Context` nor `## Method` is written.
        **＋** A `create` whose slug is a placeholder (`draft`, no `kind`) fills it: `created` and `deferred_by` kept, History `created over placeholder`; any other existing page is a collision, not a rename.
        **＋** An `update` applies `set` to the frontmatter, `sections` as whole replacements, `replace` inside the body (whitespace collapsed, exactly one occurrence), History `updated: <change>`; an `update` of an Estimate with `sections.Criterion` replaces the section whole.
        **＋** An `update` of an Estimate whose `set` carries `method` writes the field after `purpose` and drops `## Context` and `## Method` where the page carries them — the field replaces the section, the Case is reached by `origin`; an `update` without `set.method` touches no section (case 211.1).
        **＋** An `update`, `estimate`, `delete` or `defer` whose slug is not under `wiki/` finds the page under `vault/archive/` (`raw/` folders excluded) and edits it there.
        **＋** An `estimate` sets `status`, overwrites `## Result`, writes `checked` — the date the `result` opens with, else the yaml's date — and appends History `status: a → b · <ledger pointer>`.
        **＋** A `delete` sets `archived` with History `deleted`; a `delete` outside the vault is a line on stdout, the entry applied, no page written.
        **＋** A `defer` with a page appends the decision slug to `deferred_by` (rule, entity, insight) with History `deferred`; without a page it writes a placeholder `draft` with the Case's fields and `deferred_by`.
        **＋** A `lesson` writes the lesson only, `source` when the line carries it; no Estimate is created.
        **＋** Every ref field is written as `"[[slug]]"`, a list as `["[[a]]", "[[b]]"]`; a slug without a category prefix stays bare; read through the brackets.
        **＋** A `create` in `insights` applies only with the mark `librarian`; a `delete` of an Insight is refused always.
        **＋** History lines and `log.md` lines carry the date of the run and end with `[[decision-case-N]]` or the ledger pointer; `log.md` is appended after each entry; a tag of `new_tags` lands in `tags.md`, a used and undeclared one goes to stderr.
        **－** No body section is derived from a ref field; a section a page still carries is not touched, except the two `set.method` drops.
        **－** `criterion_block` on an `update` and an entry of kind `remove_criterion` are not applied: a shape the script does not know — the entry fails alone (`estimate-generate-fails-alone`).
        **－** The Decision page, the failure of an entry and the cascade are three other Estimates.
    change: one line in the Criterion — an update of an Estimate with set.method writes the field and drops ## Context and ## Method (case 211.1)
```

```tasks
- [ ] update `estimate-generate-writes`: `sections: Criterion` — the current text plus the line on `set.method`; `set: {status: pending}`
- [x] `guppi/generate.py`: drop the two sections on `set.method` of an Estimate; docstring; tests first in `tests/test_generate.py`
- [x] read `estimate-generate-writes`
```

### Case 211.2 — a recut without `method` fails alone

> **when:**
> `guppi generate` applies an `update` with `sections.Criterion` to an Estimate page without a `method` field, and `set` carries no `method`.

> **then:**
> The entry fails alone: `generate: <slug>: a recut without method (case 211)` on stderr, `failed` in the yaml, the page untouched, exit 1; the other entries apply.
> **－** A page with a `method` field takes `sections.Criterion` without `set.method`, as today.

```then
update:
  - slug: estimate-generate-fails-alone
    set: {status: pending}
    sections:
      Criterion: |
        Given:
        `guppi generate` applies the entries of a `materialize.yaml` in order; the `sections` of an `update` entry are whole replacements, `set` writes fields.
        **＋** An `update` entry for an Estimate carries `sections.Criterion` and `set: {status: pending}`; a `create` entry carries `kind`, `purpose`, `method`, `tags` as fields (194.1).
        **＋** An `estimate` entry carries `status` and `result`; the `result` opens with the date of the reading and the command (199).
        **＋** The tests in `tests/test_generate.py` fix the behaviour; the live reading is the librarian's run of this session.
        **－** `materialize`, `cleanup` and `lint` do not change here.

        When:
        `guppi generate` meets an entry it cannot apply, or one already handled.

        Then:
        An entry that fails — a collision, a `ref` naming no page, a `replace` absent or not unique, a field of an unexpected shape, an unknown `kind`, any exception — is printed on stderr as `generate: <slug>: <what>`, marked `failed` in the yaml and skipped; the rest apply; the exit code is 1; no entry ends the run.
        **＋** An `update` with `sections.Criterion` on an Estimate page without a `method` field, whose `set` carries no `method`, fails the same way: `generate: <slug>: a recut without method (case 211)`; a page with the field takes the Criterion as before (case 211.2).
        **＋** Every applied entry is marked `applied: <time>`; a stale `failed` mark is dropped on apply; a rerun writes nothing.
        **＋** An entry with `failed` and no `kind` is skipped with its mark kept and the line `generate: line N: not lifted by materialize; <message>`, exit 1.
        **＋** An entry with `superseded_by` is not applied and leaves no line; the Decision page of its Case is still written.
        **＋** A Rule-class file entry prints `a Rule-class file, applied by hand` and is marked applied; an `update` with no content prints `an update with no content in the Spec; applied by hand` and is marked applied.
        **－** The failure of one entry changes no other page: `log.md` after it is level with the pages.
    change: one line in the Criterion — a recut without method fails alone (case 211.2)
```

```tasks
- [ ] update `estimate-generate-fails-alone`: `sections: Criterion` — the current text plus the line on a recut without `method`; `set: {status: pending}`
- [x] `guppi/generate.py`: the refusal; tests first
- [x] read `estimate-generate-fails-alone`
```

### Case 211.3 — the five pages of 1955 get `method`

> **when:**
> The librarian applies the yaml of this session after the build of 211.1.

> **then:**
> `estimate-generate-writes`, `-generate-walks-dates`, `-lint-catches`, `-pretask-reconciles`, `-materialize-assembles` carry a `method` field with the text of their `## Method` sections in one line; `## Context` and `## Method` are dropped.
> **＋** `unmigrated` reads 34 after the run: these five, `estimate-pretask-hook-gates` (213.2), `estimate-permissions` (215) and `estimate-brief-written` (209.6) leave the old shape; `estimate-documentation-completes` keeps its `### case` blocks.
> **－** The Criterion of these pages does not change; no `pending` is set — except on `estimate-generate-writes`, whose Criterion 211.1 changes.

```then
update:
  - slug: estimate-generate-writes
    set: {method: "pytest in tests/test_generate.py against a temp vault; the live reading once by hand"}
    change: method as a field, the old sections dropped — the recut completed (case 211.3)
  - slug: estimate-generate-walks-dates
    set: {method: "tests/test_generate.py with two dated folders; live, the librarian's first run"}
    change: method as a field, the old sections dropped — the recut completed (case 211.3)
  - slug: estimate-lint-catches
    set: {method: "pytest in tests/test_lint.py, one test per defect class; the live reading once by hand, written into the estimate line"}
    change: method as a field, the old sections dropped — the recut completed (case 211.3)
  - slug: estimate-pretask-reconciles
    set: {method: "One reading by hand, written into the estimate line — the exception the Method rule allows"}
    change: method as a field, the old sections dropped — the recut completed (case 211.3)
  - slug: estimate-materialize-assembles
    set: {method: "pytest in tests/test_materialize.py against a temp vault; the live reading once by hand"}
    change: method as a field, the old sections dropped — the recut completed (case 211.3)
```

```tasks
- [ ] update the five pages: `set: {method: …}`, `change` (the `then` block above)
- [ ] `make lint` after the librarian's run: `unmigrated: 34`
```

### Case 211.4 — the Rule-class files

> **when:**
> Someone reads the Case schema, the Estimate schema and the map after Work Mode.

> **then:**
> `case-schema.md`: an `update` of an Estimate carries `slug`, `set: {status: pending}`, `change` — and `set.method` when the page has no `method` field; the recut brings the page to the shape of case 193.
> **＋** `estimates/schema.md` and `schema.yaml`: `## Context` and `## Method` are dropped by the `update` that sets `method`; a recut without `method` `generate` refuses.
> **＋** `index.md` §7: the old sections stand "until the `update` that sets `method`".

```then
update:
  - slug: case-schema
    file: vault/wiki/case-schema.md
    change: "an update of an Estimate carries set.method when the page has no method field — the recut brings the page to the shape of case 193 (case 211.4)"
  - slug: estimates-schema
    file: vault/wiki/estimates/schema.md
    change: "the rows ## Context and ## Method — dropped by the update that sets method; a recut without method is refused by generate (case 211.4)"
  - slug: estimates-schema-yaml
    file: vault/wiki/estimates/schema.yaml
    change: "the comments on the optional fields and sections — dropped by the update that sets method (case 211.4)"
  - slug: index
    file: vault/wiki/index.md
    change: "§7 — the old sections stand until the update that sets method (case 211.4)"
```

```tasks
- [x] update `case-schema.md`, by hand
- [x] update `estimates/schema.md` and `estimates/schema.yaml`, by hand
- [x] update `index.md` §7, by hand
```

## Case 212 — `estimate-plan-mode-names-its-estimates`: a reading on a MOC beside a pipeline

> **context:**
> `rule-plan-mode` is a MOC with four children and two Estimates: `estimate-plan-mode-verified` (`method: make test-plan-mode`, the pipeline over the children) and `estimate-plan-mode-names-its-estimates` (case 187, `method` a live reading of the Spec at the close: every Case names its Estimate by slug). The clause of 112.1 in `rule-lint` (`estimate-lint-catches`): a MOC's Estimate with a `make <target>` passes always, and "by hand" passes only when every child's Estimate is a reading too. The children of Plan Mode — `rule-pretask` among them — have tests, so lint prints `method: says by hand while estimate-pretask-checks-the-plan names a test file`. The Case touches one promise of `rule-lint` — `estimate-lint-catches`; the other Estimates of lint it does not touch. `estimate-lint-catches` gets its `method` field from 211.3 in the same yaml, earlier in ledger order.

> **problem:**
> The clause of 112.1 was written when a MOC had one Estimate covering its children: "by hand" on such a MOC would hide the children's tests. Now a MOC can carry a second, cross-cutting Estimate — a reading of the behaviour of Plan Mode itself, not a pipeline; no test checks it, and naming `make test-plan-mode` in its `method` would be false. Lint names a contradiction that is none.

> **given:**
> `guppi lint` reads the `method` of every Estimate against its target; the tests in `tests/test_lint.py` fix the classes of findings, the live reading is `make lint` in the librarian's run.
> **＋** `estimate-plan-mode-verified` names `make test-plan-mode`, a target of the Makefile.
> **－** The Makefile and `render --check` do not change.

> **when:**
> `uv run guppi lint` reads the `method` of an Estimate whose target is a MOC.

> **then:**
> A `make <target>` of the Makefile passes, whatever stands beside it.
> **＋** A reading (`by hand`, `reading`) passes when every child's Estimate is a reading, or when another Estimate of the same MOC names a `make <target>` of the Makefile.
> **＋** Otherwise a finding `method: says by hand while <child estimate> names a test file`, one per page.
> **－** The Leaf rule does not change.

```then
update:
  - slug: estimate-lint-catches
    set: {status: pending}
    sections:
      Criterion: |
        Given:
        `guppi lint` reads every live page of `wiki/<category>/` against the category's `schema.yaml` and writes nothing.
        **＋** `estimates/schema.yaml` (193): `purpose`, `method`, `checked` are optional fields; `## Context`, `## Method` optional sections; `## Result` required on `passed` and `failed`.
        **＋** The tests in `tests/test_lint.py` fix the behaviour, one per class; the live reading is `make lint` in the librarian's run of this session.
        **－** `render --check` and the Makefile do not change.

        When:
        `uv run guppi lint` reads the live pages of the vault.

        Then:
        Every live page is checked against the `schema.yaml` of its category; one line per finding, `<category>/<slug>: <class>: <what>`; exit 1 on any finding, 0 and no output on a clean vault; nothing is written.
        **＋** `schema`: a missing required field or section, a value outside the list, a conditional not met; `## When` is never required on a Decision page; `schema-prose`: `schema.md` and `schema.yaml` naming different fields or sections.
        **＋** `ref`: a slug in `parent`, `children`, `estimates`, `target`, `insight`, `addressed_by`, `deferred_by` or in a History wikilink that no live or archived page carries; a `[[…]]` in a body may name a hub file under `wiki/` by stem or path; a `[[slug]]` under a Decision page's `## Criterion` that is no Estimate; a `### case N` block of an Estimate with no decision page.
        **＋** `origin`: both forms resolve in `raw/` or in `vault/archive/`; in neither, or in both, a finding.
        **＋** `path`: a file of `implementation_ref` or `governs` that does not exist.
        **＋** `orphan`: a live entity, rule or estimate that no live page's frontmatter names; a lesson and an Insight never.
        **＋** `status`: `built` with an Estimate not `passed`, `draft` with every one `passed`; an Estimate `passed` or `failed` without `## Result`; an Estimate whose target is not an entity or a rule, or does not list it in `estimates`.
        **＋** `unread`: every Estimate `pending` or `failed` — one finding each, `unread: <status>`; red between a change of a promise and its reading, by design.
        **＋** `method`: the `method` field, or on a page of the old shape the `## Method` section; for a MOC's Estimate a named `make <target>` of the Makefile passes whatever stands beside it, and a reading (`by hand`, `reading`) passes when the Estimates of every child are readings or when another Estimate of the same MOC names a `make <target>` of the Makefile (case 212); for a Leaf's Estimate a `tests/` file that exists, the word `pytest`, a `make <target>` of the Makefile or a reading; else a finding.
        **＋** `decision`: a decision page with none of the four lists, or with `kind`/`target_slug`; a listed slug with a category prefix and no page.
        **＋** `deferred`: a placeholder earns one finding `deferred: <N> times since case <M>` in place of its `schema` and `orphan` findings; a page with `deferred_by` whose fields are in place earns none.
        **＋** `unmigrated`: one line, `estimates: unmigrated: <N> pages in the shape before case 193` — the live Estimates without a `method` field, or with `## Context`, `## Method` or a `### case N` block; no line at zero.
        **－** `make lint` runs it after `render --check`; neither writes.
        **－** The checks of the old shape — `## Method` as a section, the `### case N` blocks — leave by a separate `update` of this rule once the counter reads zero; not this Case.
    change: the method line of the Criterion — a reading on a MOC's Estimate passes beside a sibling Estimate that names a make target (case 212)
```

```tasks
- [ ] update `estimate-lint-catches`: `sections: Criterion` — the current text with the `method` line changed; `set: {status: pending}`
- [x] `guppi/lint.py`: `check_method`, the MOC branch; docstring; tests first in `tests/test_lint.py`
- [x] read `estimate-lint-catches`
- [x] `make lint`: the finding on `estimate-plan-mode-names-its-estimates` leaves
```

## Case 213 — the session bound by its stamp, not by position

> **context:**
> The Insight `insight-ledger-hi-tied-to-its-session-by-position` (`open`, severity 1, four lessons, deferred by 192 and 205) describes one fault: a `hi` was bound to its session by the `session-start` lines around it in the event log, and a foreign start or midnight broke the binding. Half of it is closed: `UserPromptSubmit` writes the `hi` with the session's stamp (case 111), the ledger hook finds the window by the stamp and walks back across midnight (`hi_moment`, `session_event_logs`), the binding by position left with case 136.3. Two readers keep the old logic: `guppi pretask --check` — without `--session` and without `CLAUDE_SESSION_ID` (empty in the agent's Bash, checked in this session) it takes the last `session-start` of today's log — a foreign one beside a parallel session, none after midnight (`lesson-pretask-check-session-fallback-stops-at-midnight`); and the hook `PreToolUse ExitPlanMode` — it reads today's log only, so after midnight it sees no `hi` and lets Plan Mode close without `/pre-task`. The stamp is in the context: the line `hi: HH:MM:SS <stamp> → raw/…` the hook prints at `/hi`. The Case touches `estimate-pretask-checks-the-plan` (`rule-pretask`), `estimate-pretask-hook-gates` (`rule-pretask-hook`) and `estimate-pretask-reconciles` (the Render of `rule-pretask`) — one per sub-case; `rule-ledger-write` and `rule-event-log` it does not touch. `estimate-pretask-hook-gates` is of the old shape: its `update` carries `set.method` (case 211) and its Criterion is written whole in the form of the model, the block of 136.2 folded in.

> **problem:**
> Two readers guess the session where the ledger hook knows it. Guessing by position is the cause the Insight names; while it lives in `pretask`, the Insight cannot close, and `/pre-task` after midnight checks the wrong session or nothing, in silence.

> **given:**
> The ledger hook finds the session's window by the stamp: the first `hi` of the stamp after its first `session-start`, over the logs from today back to the date of that start (`ledger.session_event_logs`, `hi_moment`).
> **＋** `UserPromptSubmit` prints `hi: HH:MM:SS <stamp> → raw/<date>/<HHMM>/` into the context.
> **＋** Tests with a pinned clock (`rule-tests-clock-pinned`) fix the crossing of midnight.
> **－** `CLAUDE_SESSION_ID` is empty in the agent's Bash; nothing leans on it.

### Case 213.1 — `pretask --check` does not guess the session

> **when:**
> `guppi pretask --check <plan>` runs.

> **then:**
> The stamp is `--session`, else `CLAUDE_SESSION_ID`; with neither, one line on stderr `pretask: no session id; pass --session <stamp> from the hi: line`, exit 2, nothing checked.
> **＋** The session's window is found as the ledger hook finds it: by the stamped `hi`, over the logs back to the date of its `session-start`; the `hi` of yesterday's session is found after midnight.
> **－** The last `session-start` of today's log is not read any more.

```then
update:
  - slug: estimate-pretask-checks-the-plan
    set: {status: pending}
    sections:
      Criterion: |
        Given:
        `guppi pretask --check <plan>` reads the Cases of the plan by their headings, the `then` blocks, the session's `frontier.md` and the session's ledger window; `guppi gate` writes the `pretask` line with the session's stamp on the Skill call.
        **＋** An Estimate item of a `then` block is a `create` with `ref`, or an `update` with `set: {status: pending}`; its Criterion is the Case's `given`, `when` and `then` unless the item wrote `sections: Criterion` itself (194.1).
        **＋** The ledger hook finds the session's window by the stamp: the first `hi` of the stamp after its first `session-start`, over the logs from today back to the date of that start (case 213).
        **＋** The tests in `tests/test_pretask.py` fix `--check`; the live reading is the `/pre-task` of this session.
        **－** The `PreToolUse ExitPlanMode` hook (`rule-pretask-hook`) does not change here.

        When:
        `guppi pretask --check <plan>` runs in a session with a `hi`.

        Then:
        One finding per line on stdout, exit 1 on any, 0 and silent when clean; without a `hi` in the session's window, exit 0 and one line on stderr.
        **＋** The stamp is `--session`, else `CLAUDE_SESSION_ID`; with neither, one line on stderr `pretask: no session id; pass --session <stamp> from the hi: line`, exit 2, nothing checked; the last `session-start` of today's log is not read (case 213.1).
        **＋** The session's window is found as the ledger hook finds it — by the stamped `hi`, over the logs back to the date of its `session-start` — so the `hi` of yesterday's session is found after midnight (case 213.1).
        **＋** Lines: a decision line of the window with no item of its kind under its own Case heading; an item with no line; a `defer` line matches a `defer` item, a Rule-class file line an `update` with that `file` or `slug`; an item under another sub-case's heading is a finding.
        **＋** The frontier `raw/<hi date>/<hi HHMM>/frontier.md`: a missing file, an open line, a `case N` whose heading the plan lacks, a `defer case N` with no `defer` item under Case N.
        **＋** Tasks: a Case with a line of a kind other than `defer` and no `tasks` block; an Estimate a `then` block creates or sets `pending` with no task line naming its slug.
        **＋** Governed: an `update` item with `file` on a path a live Rule page governs.
        **＋** Form: a Case whose `then` block holds two or more Estimate items without a written `sections: Criterion` — one promise per Case, split it; an `update` of an Estimate whose page does not exist; a `create` of an Estimate whose `ref` names no live rule or entity.
        **＋** Grammar: every record line of the window — the session's ledger whole plus the date-level ledgers from the `hi` time on — through `materialize.parse_line`; one that does not parse is a finding with its file and line number.
        **＋** A `then` block that does not parse: the error as a finding of its Case.
        **－** No finding on a Leaf `create` without `method`, an `update` without `contract` or a derived slug: those keys are not read.
    change: two lines in the Criterion — the stamp from --session or the environment, refused without one; the window found as the ledger hook finds it, across midnight (case 213.1)
```

```tasks
- [ ] update `estimate-pretask-checks-the-plan`: `sections: Criterion` — the current text plus the lines on the stamp and the window; `set: {status: pending}`
- [x] `guppi/pretask.py`: `resolve_session` without the fallback, the window through `ledger.session_event_logs`; docstring; tests first, one across midnight
- [x] read `estimate-pretask-checks-the-plan`
```

### Case 213.2 — the `ExitPlanMode` hook sees the `hi` across midnight

> **when:**
> The hook `PreToolUse ExitPlanMode` looks for the `hi` and the `pretask` mark of this session.

> **then:**
> It reads the logs the ledger hook reads — from today back to the date of this session's `session-start`; the `hi` and the `pretask` of yesterday's session are found after midnight.
> **－** The rest of the hook does not change: without a `hi` it lets the call through, with a `hi` and no `pretask` it refuses.

```then
update:
  - slug: estimate-pretask-hook-gates
    set: {status: pending, method: "pytest in tests/test_pretask.py with piped payloads against a temp event log; the live reading once by hand, written into the estimate line"}
    sections:
      Criterion: |
        Given:
        A `PreToolUse` payload naming `ExitPlanMode`, with the session's stamp.
        **＋** The ledger hook reads the event logs from today back to the date of this session's `session-start` (`ledger.session_event_logs`, case 55.1).
        **＋** The tests in `tests/test_pretask.py` fix the hook with piped payloads against a temp event log; the live reading is the approval of the next plan.
        **－** The `--check` pass of `rule-pretask` does not change here.

        When:
        The hook `guppi pretask` on `ExitPlanMode` asks whether `/pre-task` ran in this session.

        Then:
        With no `pretask` line of this session's stamp after its `hi`, exit 2 with a reason naming `/pre-task` and the session; with the line, exit 0; any other tool, exit 0.
        **＋** The window is open when the logs hold a `hi` of the session's stamp and a `pretask` of the same stamp after it; a mark of another stamp or `--------` does not count; a foreign `session-start` resets nothing (case 136.2).
        **＋** The logs it reads are the ledger hook's — from today back to the date of this session's `session-start` — so the `hi` and the `pretask` of yesterday's session are found after midnight (case 213.2).
        **－** Without a `hi` of this session the call passes, as before.
    change: the Criterion in the form of the model, the block of 136.2 folded in, plus the logs read across midnight; method as a field, the old sections dropped (case 213.2)
```

```tasks
- [ ] update `estimate-pretask-hook-gates`: `sections: Criterion` — the text in the form of the model plus the line on the logs across midnight; `set: {status: pending, method}`
- [x] `guppi/pretask.py`: the hook path through `ledger.session_event_logs`; a test across midnight
- [x] read `estimate-pretask-hook-gates`
```

### Case 213.3 — the skill passes the stamp

> **when:**
> The person invokes `/pre-task`, or the agent calls the skill.

> **then:**
> The agent runs `uv run guppi pretask --check <plan> --session <stamp>`, the stamp from the `hi:` line of this session in the context.
> **－** The rest of the Render does not change.

```then
update:
  - slug: rule-pretask
    replace:
      - old: "Run `uv run guppi pretask --check <the plan file of this Plan Mode>`. It prints one line"
        new: "Run `uv run guppi pretask --check <the plan file of this Plan Mode> --session <stamp>`, the stamp from the `hi:` line the `UserPromptSubmit` hook put in the context at `/hi` (case 213.3). It prints one line"
    change: "the check takes --session with the stamp of the hi line (case 213.3)"
  - slug: estimate-pretask-reconciles
    set: {status: pending}
    sections:
      Criterion: |
        Given:
        `guppi pretask --check <plan>` reads the Cases of the plan by their headings, the `then` blocks, the session's `frontier.md` and the session's ledger window; `guppi gate` writes the `pretask` line with the session's stamp on the Skill call.
        **＋** An Estimate item of a `then` block is a `create` with `ref`, or an `update` with `set: {status: pending}`; its Criterion is the Case's `given`, `when` and `then` unless the item wrote `sections: Criterion` itself (194.1).
        **＋** The tests in `tests/test_pretask.py` fix `--check`; the live reading is the `/pre-task` of this session.
        **－** The `PreToolUse ExitPlanMode` hook (`rule-pretask-hook`) does not change here.

        When:
        The person invokes `/pre-task`, or the agent calls the skill, before the Spec is approved.

        Then:
        The agent runs `guppi pretask --check` on the plan file with `--session <stamp>`, the stamp from the `hi:` line of this session in the context (case 213.3), and fixes the plan, the frontier or the line for every finding until the command prints nothing; `guppi gate` writes the stamped `pretask` line into the event log on the Skill call.
        **＋** The agent lists every decision of this Plan Mode, one line each: slug — kind — `purpose` for a `create`, an `update`, a `delete`; a `defer` by its slug and the word `defer`; for an `update` of a rule or an entity, the page's `estimates` and which of them the Case names by slug.
        **＋** `ask-guppi` is dispatched once with the list, the absolute path of the plan file, the instruction to read every Case outside `## Deferred` — `when`, `then`, the `then` block — and two questions: which decisions contradict a page, `index.md` or each other; whether an Estimate the Case does not name speaks of the thing the Case changes.
        **＋** Every finding returned is raised as a Case or named in one line as already known; then Plan Mode exits again.
        **－** The body of a deferred decision is not read; a Case that changes a page another Case of the plan defers is still a finding.
    change: "the first line of Then — the check runs with --session from the hi line (case 213.3)"
```

```tasks
- [ ] update `rule-pretask`: one `replace` in the Render — the command line
- [ ] update `estimate-pretask-reconciles`: `sections: Criterion` — the current text with the first line of `then` changed; `set: {status: pending}`
- [ ] `guppi render`: `.claude/skills/pre-task/SKILL.md`; `render --check` exit 0
- [ ] read `estimate-pretask-reconciles`
```

### Case 213.4 — the Insight closed

> **when:**
> The librarian applies the yaml of this session.

> **then:**
> `insight-ledger-hi-tied-to-its-session-by-position` — `status: actioned`, `addressed_by: decision-case-213.1`; the cascade archives its four lessons.
> **－** A new lesson with the same root cause reopens it, as with any Insight.

```then
update:
  - slug: insight-ledger-hi-tied-to-its-session-by-position
    set: {status: actioned, addressed_by: "[[decision-case-213.1]]"}
    change: the binding by position retired in pretask --check and the ExitPlanMode hook; the ledger hook already bound by the stamp (case 213)
```

```tasks
- [ ] update `insight-ledger-hi-tied-to-its-session-by-position`: `set: {status: actioned, addressed_by}`, `change`
```

## Case 214 — `materialize` lifts fields by the schema, not by a skip list

> **context:**
> `insight-materialize-lift-loses-a-schema-field` (`open`, severity 1, three lessons) was actioned by case 144.3 — "the table exists in code, `REQUIRED`" — and reopened by the librarian of 1955 with a third lesson: `_lift_item` copies every key of a `then` item into `fields` except a fixed skip list; case 194.1 gave the Estimate item a `ref`, the list was not extended, and `ref` landed on 15 pages as a field (F3, case 210). `REQUIRED` is the table of what is missing; the table of what *may* land on a page is not in the code — it is on disk: the `schema.yaml` of each category lists its `required` and `optional` fields. The Case touches one promise of `rule-materialize` — `estimate-materialize-assembles` (it gets `method` from 211.3, earlier in ledger order); `-marks-superseded`, `-fails-alone`, `-shows` and the others it does not touch.

> **problem:**
> A skip list is wrong by construction: every new key of an item becomes a page field until somebody remembers the list. Three lessons are three times the same thing: the parser decided what reaches the page and was wrong, and lint named the page.

> **given:**
> The `schema.yaml` of each category lists the fields of its page: `required` and `optional`.
> **＋** The tests in `tests/test_materialize.py` fix the lift; the live reading is the librarian's run of this session.
> **－** `generate` does not change: it writes `fields` as it gets them.

### Case 214.1 — the lift by the schema

> **when:**
> `guppi materialize` lifts a `create` or `defer` item of a `then` block into an entry.

> **then:**
> Only the keys the category's `schema.yaml` names as fields reach `fields`; the structural keys of the item go where they go today — `ref` to the entry, `sections`, `tags`, `file`.
> **＋** A key that is neither in the schema nor structural is marked `unknown: [key]` on the entry; `--show` prints it; the page does not get it; the entry applies.
> **＋** `incomplete` is counted by `REQUIRED`, as today.
> **－** The keys of the old shape (`method`, `contract`, `estimate_slug`, `estimate_kind` on a rule's item) stay silently ignored — they are named in the Criterion, not `unknown`.

```then
update:
  - slug: estimate-materialize-assembles
    set: {status: pending}
    sections:
      Criterion: |
        Given:
        A unit `raw/<date>/<HHMM>/` holds `ledger.md` and `spec.md`; a Case in the Spec has a heading, the sections `given`, `when`, `then` and a `then` block.
        **＋** `guppi generate` applies the `sections` of an `update` entry as whole replacements and writes every field of a `create` entry's `fields` into the frontmatter.
        **＋** The `schema.yaml` of each category lists the fields of its page: `required` and `optional` (case 214).
        **＋** The tests in `tests/test_materialize.py` fix the behaviour; the live reading is the librarian's run.

        When:
        `guppi materialize` lifts a record line of a ledger against its Spec.

        Then:
        One entry per record line, in ledger order: `case`, `kind`, `category` from the slug prefix, `slug`, `ref`, `source`, `supersedes`, `tags`, `origin`, `line`, `text`, `decision`; from the `then` block — `fields`, `sections`, `replace`, `change`, `impact`; what the block lacks is `incomplete`, never invented.
        **＋** Only the keys the category's `schema.yaml` names as fields reach `fields` of a `create` or `defer` entry; the structural keys of the item go where they go — `ref` to the entry, `sections`, `tags`, `file`; a key that is neither is marked `unknown: [key]` on the entry, printed by `--show`, never written to the page, and the entry applies; `incomplete` is counted by `REQUIRED` as before (case 214.1).
        **＋** An Estimate has its own line and its own entry; the `ref` of the line is the Estimate itself.
        **＋** An `update` entry for an Estimate carries `sections.Criterion` — the text the item wrote under `sections: Criterion` itself, else the `given`, `when` and `then` of its Case verbatim with their operands as `Given:`, `When:`, `Then:` — replacing what stood there, and `set: {status: pending}` unless the item set a status itself; the `given` of a sub-case is its parent's when it has none of its own.
        **＋** A `create` entry for an Estimate keeps `kind`, `purpose`, `method`, `tags` as fields; its Criterion the same way: the written text when there is one, else the Case's; `## Context` and `## Method` are not written.
        **＋** One decision entry per Case: `decision`, `case_text`, `targets`; a sub-case inherits `context`, `problem`, `recommend`, `given`, never `when`.
        **＋** An `estimate` line for a page of the same ledger is folded into its `create`; for an earlier page it is an `estimate` entry. The `new_tags` of any Case reach the yaml once. An existing yaml is extended, never rewritten.
        **－** An `update` entry carries no `contract`, and no Estimate is derived from it; a `create` carries no `method`, `estimate_kind` or `estimate_slug`; neither `criterion_block`, `case_removed` nor `remove_criterion` is derived.
        **－** The keys `contract`, `estimate_slug`, `estimate_kind` and `method` on a rule's item are ignored: they reach neither the page, nor `incomplete`, nor `unknown`.
        **－** A line the grammar does not parse goes under `unparsed`; the run goes on.
    change: one line in the Criterion — fields lifted by the category's schema.yaml, an unknown key marked unknown and never written (case 214.1)
```

```tasks
- [ ] update `estimate-materialize-assembles`: `sections: Criterion` — the current text plus the lines on the lift by the schema and `unknown`; `set: {status: pending}`
- [x] `guppi/materialize.py`: `_lift_item` by `schema.yaml`, the `unknown` mark, `--show`; docstring; tests first
- [x] read `estimate-materialize-assembles`
```

### Case 214.2 — the Insight closed

> **when:**
> The librarian applies the yaml of this session.

> **then:**
> `insight-materialize-lift-loses-a-schema-field` — `status: actioned`, `addressed_by: decision-case-214.1`; the cascade archives its three lessons.
> **－** A new lesson with the same root cause reopens it.

```then
update:
  - slug: insight-materialize-lift-loses-a-schema-field
    set: {status: actioned, addressed_by: "[[decision-case-214.1]]"}
    change: the lift by the schema — a key the schema does not name never reaches a page (case 214)
```

```tasks
- [ ] update `insight-materialize-lift-loses-a-schema-field`: `set: {status: actioned, addressed_by}`, `change`
```

## Case 215 — `estimate-permissions`: the Criterion by the facts

> **context:**
> `rule-permissions` renders the `permissions` block of `.claude/settings.json`: an allow list of nine entries — Edit and Write for `frontier.md`, `spec.md`, `handoff.md` under `vault/raw/**`, Write for `carry.md` there, Edit and Write for `vault/wiki/brief.md`; `deny` and `ask` empty. Its one Estimate `estimate-permissions` (`passed`, the old shape: `## Context`, `## Method`, no `method` field) carries a Criterion assembled by case 200.5 from that Case's `given`/`when`/`then`: the `given` speaks of the supersedes of 189 and 195, the `when` of `/carry`, the `then` says "eight entries" and lists nine; `## Method` says "six entries". The reading of 1955 passed on the set and called the count the Criterion's own error. The Case touches one promise — `estimate-permissions`; the Render of `rule-permissions` does not change.

> **problem:**
> The Criterion names three different numbers and conditions that have nothing to do with permissions; it cannot be read by the letter. This is a recut of an old page, and by case 211 it carries `set.method`.

> **given:**
> `.claude/settings.json` is rendered from `rule-permissions`; the JSON case of `tests/test_render.py` fixes the allow list.
> **＋** The live probe is the Write of `frontier.md` at `/hi` in Plan Mode and an edit of `spec.md` in Work Mode, each recorded as asked or not asked.
> **－** Nothing else under `wiki/` is allowed.

> **when:**
> The agent writes or edits a working file of the session — `frontier.md`, `spec.md`, `handoff.md`, `carry.md` under `vault/raw/**` — or `vault/wiki/brief.md`.

> **then:**
> The client does not ask: the allow list holds nine entries — Edit and Write for `frontier.md`, `spec.md`, `handoff.md` under `vault/raw/**`; Write for `carry.md` under `vault/raw/**`; Edit and Write for `vault/wiki/brief.md`.
> **－** `deny` and `ask` are empty; nothing else under `wiki/` is allowed.

```then
update:
  - slug: estimate-permissions
    set: {status: pending, method: "the nine entries in the rendered .claude/settings.json and the JSON case of tests/test_render.py; the live probe — the Write of frontier.md at /hi in Plan Mode and one edit of spec.md in Work Mode, each recorded as asked or not asked"}
    change: the Criterion replaced whole by the facts — nine entries named, the given and when about permissions; method as a field, the old sections dropped (case 215)
```

```tasks
- [ ] update `estimate-permissions`: the Criterion — the `given`, `when`, `then` of this Case; `set: {status: pending, method: …}`
- [x] read `estimate-permissions`
```

## Case 216 — the Spec of 1955 ticked

> **context:**
> `raw/2026-09-16/1955/spec.md` holds 48 task lines, 27 ticked, 21 not: the `update`/`create` lines of pages (applied by the librarian of 1955, the pages live), three `uv run guppi render` lines (`render --check` exit 0), `{supersedes:case 191}` (`decision-case-191` in the archive), `read estimate-case-protocol-case-form` (`passed`, ledger 1955 line 41). No Estimate is touched.

> **problem:**
> Retro counts the unticked lines; 21 lines of finished work read as debt.

> **given:**
> Each of the 21 lines matches a page, a file or a reading that exists.

> **when:**
> Someone reads `raw/2026-09-16/1955/spec.md` after Work Mode.

> **then:**
> All 48 task lines are ticked.
> **－** Nothing else in the file changes.

```then
migration:
  - what: tick the 21 open task lines of raw/2026-09-16/1955/spec.md — the page lines, the render lines, the supersedes line and the read line — by hand, each checked against the page, the file or the ledger line
    lines: 21
```

```tasks
- [x] one-off: 21 lines `- [ ]` → `- [x]` in `raw/2026-09-16/1955/spec.md`
```

## Case 221 — `pretask --check`: a `ref` to a page the same plan creates

> **context:**
> `estimate-pretask-checks-the-plan` (its Criterion written whole by Case 213.1 today) promises a finding on a `create` of an Estimate whose `ref` names no live rule or entity. `case-schema.md` says a rule with several promises is a parent Case that creates the rule and one sub-case per Estimate — the form of Case 209. `pretask --check` on this plan prints four findings: `estimate-sprint-renders-the-backlog` → `rule-sprint`, three Estimates → `entity-sprint-migration` — pages that Cases 209 and 209.2 of the same plan create. The Case touches the same promise as 213.1; the Criterion is written whole — the text of 213.1 plus one line.

> **problem:**
> The check contradicts the schema: by its letter an Estimate of a new rule cannot be ratified in the session that creates the rule.

> **given:**
> As 213.1.
> **＋** `case-schema.md`: a rule with several promises is a parent Case that creates the rule, its sub-cases create the Estimates.

> **when:**
> `guppi pretask --check <plan>` reads a `create` of an Estimate.

> **then:**
> A `ref` that names a live rule or entity, or the slug of a `create` item of category `rules` or `entities` in the same plan, is no finding.
> **－** Any other `ref` is a finding, as today.

```then
update:
  - slug: estimate-pretask-checks-the-plan
    set: {status: pending}
    sections:
      Criterion: |
        Given:
        `guppi pretask --check <plan>` reads the Cases of the plan by their headings, the `then` blocks, the session's `frontier.md` and the session's ledger window; `guppi gate` writes the `pretask` line with the session's stamp on the Skill call.
        **＋** An Estimate item of a `then` block is a `create` with `ref`, or an `update` with `set: {status: pending}`; its Criterion is the Case's `given`, `when` and `then` unless the item wrote `sections: Criterion` itself (194.1).
        **＋** The ledger hook finds the session's window by the stamp: the first `hi` of the stamp after its first `session-start`, over the logs from today back to the date of that start (case 213).
        **＋** A rule with several promises is a parent Case that creates the rule and one sub-case per Estimate (`case-schema.md`).
        **＋** The tests in `tests/test_pretask.py` fix `--check`; the live reading is the `/pre-task` of this session.
        **－** The `PreToolUse ExitPlanMode` hook (`rule-pretask-hook`) does not change here.

        When:
        `guppi pretask --check <plan>` runs in a session with a `hi`.

        Then:
        One finding per line on stdout, exit 1 on any, 0 and silent when clean; without a `hi` in the session's window, exit 0 and one line on stderr.
        **＋** The stamp is `--session`, else `CLAUDE_SESSION_ID`; with neither, one line on stderr `pretask: no session id; pass --session <stamp> from the hi: line`, exit 2, nothing checked; the last `session-start` of today's log is not read (case 213.1).
        **＋** The session's window is found as the ledger hook finds it — by the stamped `hi`, over the logs back to the date of its `session-start` — so the `hi` of yesterday's session is found after midnight (case 213.1).
        **＋** Lines: a decision line of the window with no item of its kind under its own Case heading; an item with no line; a `defer` line matches a `defer` item, a Rule-class file line an `update` with that `file` or `slug`; an item under another sub-case's heading is a finding.
        **＋** The frontier `raw/<hi date>/<hi HHMM>/frontier.md`: a missing file, an open line, a `case N` whose heading the plan lacks, a `defer case N` with no `defer` item under Case N.
        **＋** Tasks: a Case with a line of a kind other than `defer` and no `tasks` block; an Estimate a `then` block creates or sets `pending` with no task line naming its slug.
        **＋** Governed: an `update` item with `file` on a path a live Rule page governs.
        **＋** Form: a Case whose `then` block holds two or more Estimate items without a written `sections: Criterion` — one promise per Case, split it; an `update` of an Estimate whose page does not exist; a `create` of an Estimate whose `ref` names neither a live rule or entity nor the slug of a `create` item of category `rules` or `entities` in the same plan (case 221).
        **＋** Grammar: every record line of the window — the session's ledger whole plus the date-level ledgers from the `hi` time on — through `materialize.parse_line`; one that does not parse is a finding with its file and line number.
        **＋** A `then` block that does not parse: the error as a finding of its Case.
        **－** No finding on a Leaf `create` without `method`, an `update` without `contract` or a derived slug: those keys are not read.
    change: "the Form line of the Criterion — a ref to a rule or entity the same plan creates is no finding (case 221)"
```

```tasks
- [ ] update `estimate-pretask-checks-the-plan`: `sections: Criterion` — the text of 213.1 plus the line on a `create` of the same plan; `set: {status: pending}`
- [x] `guppi/pretask.py`: the plan's `create` slugs in the `ref` check; test first
- [x] read `estimate-pretask-checks-the-plan`
```

## Case 222 — the corrections of pre-task

> **context:**
> `ask-guppi` read the Spec against the vault at pre-task and found seven places that contradict a rule or the code: the refusal of 211.2 would hit three entries of this same yaml without `set.method` (209.5, 209.6, 211.1); 209 promised a position among `children` that `generate` does not give; 209.2 promised a `make lint` exit 0 unreachable while the sprint page's own Estimates stand unread; a line of 213.3's Criterion said the hook does not change beside 213.2 which changes it; 213.4 set the Insight `actioned` and left its `deferred_by` of 192 and 205, which the brief would keep listing; 211.3 counted `unmigrated` 37 where the run gives 34; 210 edited pages by hand where `index.md` §1 says the scripts are the only writers to `wiki/`, with a History line ending in no pointer. Each is amended in place in the Spec above. 213.1 and 221 replace the Criterion of `estimate-pretask-checks-the-plan` twice in one plan; the later text contains the earlier and applies last — known, not changed.

> **problem:**
> The `deferred_by` of the Insight is cleared only by a `supersedes` of the deferring Case, one Case per line; 213.4's line carries none.

> **given:**
> A `{supersedes:case N}` on a decision line marks every entry of Case N superseded and clears the `deferred_by` its `defer` set (case 200.2).

> **when:**
> The librarian applies the yaml of this session.

> **then:**
> `insight-ledger-hi-tied-to-its-session-by-position` carries no `deferred_by`: the defers of 192 and 205 are superseded by this Case; `decision-case-192` and `decision-case-205` are `superseded` and archived.
> **－** The `actioned` status and `addressed_by` of 213.4 stand.

```then
update:
  - slug: insight-ledger-hi-tied-to-its-session-by-position
    change: "the defers of cases 192 and 205 taken up by case 213 — deferred_by cleared (case 222)"
```

```tasks
- [ ] update `insight-ledger-hi-tied-to-its-session-by-position`: `change` — the defers of 192 and 205 taken up by Case 213
```

## Deferred

## Case 217 — `generate` ticks the page lines of the Spec

> **context:**
> `rule-page-generation` applies the entries of a yaml to pages and knows nothing of the Spec; `rule-work-mode` (`draft`, Slice 3b) ticks the task lines of `spec.md` as the work goes; the librarian is forbidden to read the Spec (`estimate-documentation-completes`). The yaml lies in the session's folder beside `spec.md`; each entry carries `case`, `kind` and `slug`.

> **problem:**
> Nobody ticks the task lines on a `create` or `update` of a page or on `guppi render`: every Spec ends its session with them open, and Retro counts them as debt — 21 in the Spec of 1955.

```then
defer:
  - slug: rule-page-generation
    type: rule
    purpose: "generate ticks, in the session's spec.md, the task line under the entry's Case whose kind and slug it names — `- [ ] create <slug>` / `update <slug>` / `defer <slug>` — once the entry applied, and the librarian's render step ticks its `guppi render` line the same way; a line not found is no error; the lines on code, tests, migrations and readings stay the agent's; the script reads the Spec, not the librarian — said in the Criterion; a one-off tick of the older Specs is case 216, not this; with Slice 3b, which fixes who ticks what"
```

## Case 218 — Slice 3b: `rule-work-mode`, `rule-subagent-guppi`

> **context:**
> `rule-work-mode` and `rule-subagent-guppi` are placeholders, `draft`, `deferred_by: decision-case-183, decision-case-206`, `deferred: 14 times since case 29`, in their nineteenth brief. Case 206 put Slice 3b after the build of 201–203; that build closed with session 1955. With case 209 Slice 3b is the first open Slice of `entity-sprint-migration`, and case 217 leaves it the question of who ticks which task line.

> **problem:**
> This session took fourteen items of the Frontier — the sprint page, the recut rule, the session binding, the lift by the schema — and has no room for the Plan Mode of a Slice; Work Mode needs a session of its own, as 206 said.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: "Work Mode: the Spec as tasks with code, the ticked boxes in spec.md, the test of each Estimate written first and turned green; who ticks which task line (case 217); the Plan Mode of a session of its own, the first open Slice of the sprint page"
  - slug: rule-subagent-guppi
    type: rule
    purpose: "what a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case; with rule-work-mode, the next session"
```

## Case 219 — `rule-spec-box`

> **context:**
> `rule-spec-box` is the placeholder of case 207, `draft`, `deferred_by: decision-case-207`, lint `missing field kind`, `missing field estimates`, `orphan`; its `purpose` holds the whole argument — a session that opens a conserved Spec in a git worktree and runs its Work Mode, the librarian once after the merge. Case 207 put it after Slice 3b; case 209 lists it under Slice 5 of the sprint page.

> **problem:**
> The box leans on Work Mode, which is not written; nothing about it can be decided before Slice 3b.

```then
defer:
  - slug: rule-spec-box
    type: rule
    purpose: "the Spec box of case 207 — a conserved Spec run in a worktree on its own branch, Work Mode only, the librarian once after the merge; after Slice 3b; its open questions as 207 left them: the skill and its conditions, the ledger hook and guppi gate inside a worktree, the cut of a Spec into boxes, a third end of a session, subagent or session"
```

## Case 220 — `git pull` without an upstream, `gh` without a login

> **context:**
> `rule-git-context` (`built`) pulls at `/hi` and prints the failure when the branch has no upstream; `rule-github-issues` (`built`) lists the open issues and prints `gh auth login` when `gh` is not logged in. Both print their line at every `/hi`; decisions 11.1 and 11.2 parked them for the close of the sprint, and case 209 lists that close under `estimate-sprint-migration-leftovers-gone`.

> **problem:**
> Whether to set an upstream and log `gh` in, or to keep both lines as they are, is the sprint's closing decision, not this session's; the Frontier names it every session until then.

```then
defer:
  - slug: rule-git-context
    type: rule
    purpose: "the pull without an upstream at /hi — set the upstream of `migration`, or keep the printed failure as the decision 11.1 made it; at the close of the sprint, read by estimate-sprint-migration-leftovers-gone"
  - slug: rule-github-issues
    type: rule
    purpose: "gh not logged in, no GitHub remote — log in and add the remote, or keep the printed line as decision 11.2 made it; at the close of the sprint, read by estimate-sprint-migration-leftovers-gone"
```

## Retro

## Case 223 — `rule-carry-over`: the stray `ref` field

> **context:**
> `rule-carry-over` (`draft`, parent `rule-end-of-work`) carries a `ref: rule-end-of-work` field beside `parent` — the same lift as on the 15 Estimate pages of case 210 (`lesson-materialize-item-ref-lifted-as-a-page-field`), on a rule page; `rules/schema.yaml` names no `ref`. Case 214.1 keeps `ref` off every page from now on; case 210 named the Estimate pages only, and Work Mode left this one as it stood.

> **problem:**
> One live rule page carries a field nobody ratified; the one-off of 210 did not cover it, and Retro ratifies no update.

```then
defer:
  - slug: rule-carry-over
    type: rule
    purpose: "drop the stray `ref` field from `rule-carry-over`, a one-off like case 210 — a script run once by path and a History line with the pointer; the next Plan Mode"
```

