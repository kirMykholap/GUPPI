<!-- approved 23:07:01 · session 43d72f8c -->

# Spec — session 1654, 2026-09-25

## Case 425 — Apply the rename of `rule-frame-check` to `rule-case-build`

> **context:**
> Case 419.2 replaced the agent `frame-guppi` with `case-guppi`. For the page `rule-frame-check` it signed two `update` items: first the new `Purpose` and `Render`, then the `rename` to `rule-case-build`. A Case has one ledger line per page. `materialize` takes the first item with that slug for it (`find_item` in `guppi/materialize.py`), and the second item, with the `rename`, drops out without a word. The sections were applied, the rename was not. So the rule stands under the old slug, and its Render stands between the markers `rule-frame-check`. At the same time `rule-case-protocol`, `rule-skill-hi` and their renders `vault/wiki/case-schema.md` and `.claude/skills/hi/SKILL.md` name the page `rule-case-build` in a code span, and it does not exist. Lint does not check such code spans. The slug `rule-case-build` is free: no page has it in `wiki/` or in the archive.
> `rename` in `guppi/generate.py` moves the page. It changes the old slug as a whole word in all its sections but History. The Render markers change too, so `render` finds them by the new slug. It changes the same slug in all live pages: in `children` of `rule-plan-mode`, in `target` of `estimate-case-build-writes-the-case`, in the lists and text of decision pages. After that the decision page of 419.2 names the rule by the new slug twice in `given`: that is what this mechanism writes, and the Case does not edit it. `.claude/agents/case-guppi.md` is rendered without markers, so its text does not change.
> What the frame check showed. A Grep over `vault/wiki/` without `brief.md` and `log.md` found only one Estimate that names the old slug: `estimate-case-build-writes-the-case`, and only in `target`. No Estimate names the new slug. The Criterion of `estimate-case-build-writes-the-case` speaks of the behaviour of `case-guppi`, and the rename does not change behaviour. So the Estimate gets no `update`: `rename` changes only its `target`.
> What this Case does not do. It does not close the cause: no check refuses two items of one slug in one `then` block, though the schema asks for one item per target. That is a separate item. The line `update rule-frame-check` in `raw/2026-09-25/1228/spec.md` stays unticked: `generate` ticks it by the ledger of session 1228, not by this Case. `git rm .claude/agents/frame-guppi.md` is W25 and is not part of this Case.
> C4 is a separate Case, not a sub-case of this one. The reading entry of `estimate-frame-check-finds-a-contradiction` failed on the rename of the Estimate, and that rename was applied. The rename of the rule does not touch it: after this Case it fails the same way. Its question is another: the reading was taken on a Criterion the same session replaced. It must be decided how to mark that entry so that the unit 1228 is applied whole. W26 and W27 depend on C4, not on this Case.

> **problem:**
> The rename signed in Case 419.2 is not applied. Harness files and rule pages name the rule by a slug that does not exist. It must be decided by which path to apply the rename now.

> **given:**
> `rule-frame-check` — the rule of the agent `case-guppi`, renamed `rule-case-build`
> **＋** `.claude/agents/case-guppi.md` — the file its Render writes
> **＋** `rule-plan-mode` — its parent, which lists it in `children`
> **＋** `estimate-case-build-writes-the-case` — its Estimate, which names it in `target`
> **＋** `rule-case-protocol` and its render `vault/wiki/case-schema.md` — a text that names the rule by the new slug
> **＋** `rule-skill-hi` and its render `.claude/skills/hi/SKILL.md` — a text that names the rule by the new slug
> **＋** `guppi/generate.py` — the `rename` of an `update` (case 258.1)

> **when:**
> `uv run guppi generate` applies the `update` of `rule-frame-check` that carries `rename: rule-case-build`, and `uv run guppi render` runs after it.

> **then:**
> The rule has the slug `rule-case-build`, its History says it was renamed from `rule-frame-check`, and no live page has the slug `rule-frame-check`.
> **＋** Its Render stands between markers that name `rule-case-build`, and `uv run guppi render` leaves `.claude/agents/case-guppi.md` with the text it holds.
> **＋** `rule-plan-mode` names `rule-case-build` in `children`, and `estimate-case-build-writes-the-case` names `rule-case-build` in `target`.
> **＋** The code span `rule-case-build` in `rule-case-protocol`, `vault/wiki/case-schema.md`, `rule-skill-hi` and `.claude/skills/hi/SKILL.md` names a live page.
> **－** The Criterion and the `status` of `estimate-case-build-writes-the-case` do not change.

```then
update:
- slug: rule-frame-check
  rename: rule-case-build
  change: 'renamed: the rule of the agent case-guppi; the rename of case 419.2, lost by materialize, applied (case 425)'
```

```tasks
- [x] update `rule-frame-check` — the page renamed `rule-case-build`
- [x] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [x] by hand: a Grep of `rule-frame-check` over `vault/wiki/` finds it only in History lines, `brief.md` and `log.md`
```

## Case 426 — Refuse a second item of one slug in a `then` block

> **context:**
> `materialize` finds the item of a `then` block for a ledger line with the function `find_item`. The function searches by the kind of decision and the slug and takes the first item it finds. A ledger line answers one item. When a second item of the same kind and slug stands under one Case, `materialize` does not read it and marks nothing. So in Case 419.2 the second `update` of the page `rule-frame-check` was lost, the one that carried the `rename`. The Case schema asks for one item per target in each kind of decision. But no check refuses the second item.
> The checks of the plan's lines and items are one module, `judge` in `guppi/prespec.py`; the comparison with the ratified copy runs outside it, in `check`. `guppi casecheck --subagent` on `SubagentStop` builds a Spec in memory from the answer of `case-guppi` and runs `judge`. That is the earliest place where the `then` block is seen: before the Case is shown to the person. After the ratification the `Stop` hook `guppi ratified` runs `judge` on each written Case. Then `/pre-spec` runs it. So the check goes into `check_lines` inside `judge`, and all three places get it by import. In `judge` the `then` block comes from `then_blocks`, which joins all fences tagged `then` of one Case. So the second item is found in another fence too. A separate check in `read_tasks` of `guppi/ratified.py` would see only the chat form. It would be a second copy of one judgment.
> What the frame check showed. The Render of `rule-prespec` lists all findings of `--check`. Without the new finding that list becomes incomplete, so the Case changes the Render by one `replace` pair. That wording stands in the Render once. The Criterion of `estimate-prespec-matches-lines-and-items` speaks of the match of ledger lines and items, and that is exactly what the Case changes. So its Criterion is replaced whole by the `when` and `then` of this Case. The Criterion of `estimate-prespec-checks-the-form-of-an-item` speaks of the form of an Estimate item. The Criteria of `estimate-case-check-sends-back-a-faulty-case` and `estimate-spec-write-checks-the-written-case` speak of the findings of `judge` in general, of none in particular. These three are not touched. The Criterion of `estimate-generate-ticks-the-spec` says that two entries of one kind and slug in one Case tick two lines, in order: that stays true of `generate`, which does not change; after this Case such a pair no longer reaches it. The Purpose of `rule-case-check` and How it works of `rule-spec-write` say that the checks are imported. That stays true. The line of the schema "one entry per target" also stays true, and now it is checked. There is no `create` here, so no vault query is due.
> What the Case does not do. `materialize` does not change: the Spec it reads has already passed `judge` three times. It reads older Specs as before. Whether they hold two items of one kind and slug, other than the Spec of session 1228, is not checked. To mark such an item in `materialize` is a separate promise of `rule-materialize`. If needed, that is a separate Case.

> **problem:**
> Two items of one kind and slug can stand under one Case. No check refuses them, and `materialize` applies only the first without a word. It must be decided where and in what form a check refuses the second item.

> **given:**
> `rule-prespec` — the rule of `/pre-spec`; its Render lists the findings of `uv run guppi prespec --check`
> **＋** `.claude/skills/pre-spec/SKILL.md` — the file its Render writes
> **＋** `estimate-prespec-matches-lines-and-items` — the promise that decision lines and items of the plan match
> **＋** `guppi/prespec.py` — `judge` and its `check_lines`, which `guppi/casecheck.py` and `guppi/ratified.py` import
> **＋** `tests/test_prespec.py` — the tests of `--check`
> **＋** `tests/test_casecheck.py` — the tests of the check of an answer of `case-guppi` on `SubagentStop`
> **＋** `rule-case-protocol` and its render `vault/wiki/case-schema.md` — a `then` block holds one entry per target under each decision type

> **when:**
> `uv run guppi prespec --check <plan>` compares the decision lines of the session's window with the items of the plan's `then` blocks.

> **then:**
> A decision line whose Case has no heading in the plan is the finding `case N: line [kind][slug]: no Case N heading in the plan`; one whose Case holds no item of its kind and slug is `case N: line [kind][slug] has no item in the plan`.
> **＋** An item with no decision line of its kind and slug under its own Case heading — a sub-case's heading included — is the finding `case N: item [kind][slug] has no decision line`.
> **＋** A nested `estimate` of a `create` needs no line of its own: the line of its parent covers it.
> **＋** A second item of one kind and slug under one Case heading — in the same fence tagged `then` or in another one — is the finding `case N: item [kind][slug] stands twice — one entry per target`: one decision line covers one item.
> **－** A `create` and an `update` of one slug, or items of one slug under two Case headings — sub-cases included — are no finding of this kind.

```then
update:
- slug: rule-prespec
  replace:
  - old: for every item that has no line,
    new: for every item that has no line, for every second item of one kind and slug under one Case — a `then` block holds one entry per target, and `materialize` lifts only the first (case 426),
  change: the Render names the finding of a second item of one kind and slug under one Case (case 426)
- slug: estimate-prespec-matches-lines-and-items
  set:
    status: pending
  change: the Criterion replaced whole — a second item of one kind and slug under one Case is a finding (case 426)
```

```tasks
- [x] update `rule-prespec` — the Render names the finding of a second item of one kind and slug
- [x] update `estimate-prespec-matches-lines-and-items` — its Criterion replaced whole by the `when` and `then` of this Case
- [x] `guppi/prespec.py`: `check_lines` reports a second item of one kind and slug under one Case; the docstring names the finding
- [x] `tests/test_prespec.py`: two `update` items of one slug in one fence, and in two fences of one Case, are the finding; a `create` and an `update` of one slug, and one slug under two sub-cases, are none
- [x] `tests/test_casecheck.py`: an answer of `case-guppi` whose `tasks` hold two `update` lines of one slug exits 2 with the finding
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [ ] read `estimate-prespec-matches-lines-and-items`
```

## Case 427 — Retire the reading entry of ledger line 40 of session 1228 by the mark `superseded_by`

> **context:**
> In the ledger of session 1228, line 40 is the reading of `estimate-frame-check-finds-a-contradiction`, taken on the old Criterion, on dispatches of `frame-guppi`. In the same Spec Case 419.2 replaced that Criterion whole and renamed the page to `estimate-case-build-writes-the-case`. So `generate` does not find the page, sets `failed` on the entry and repeats that error at each run. The handoff of session 1228 asked not to apply this reading: by case 283 a reading of an Estimate is not taken while its new Criterion is not built.
> While the entry carries `failed`, the yaml of session 1228 is not applied whole. The function `applied_whole` in `guppi/render.py` asks every entry for `applied` or `superseded_by`, and none with `failed`. So `render` does not tick the render lines in the Spec of session 1228, and `kept_reason` in `guppi/archive.py` keeps the unit in `raw/`. All other entries and decisions of this yaml carry `applied`.
> There is no mark that retires a reading entry by a decision. Only `materialize` sets `superseded_by`, from a `{supersedes:case N}`, and only on an entry with `case`. A reading entry has no field `case`. The mark cannot be derived automatically: by case 280 a reading that stands in the ledger after the decision line of its own Case counts as a reading of the new Criterion. Such a rule would also retire legitimate readings of Work Mode. The person chose a one-off migration signed by this Case.
> The value of the mark is `427`, not `419.2`. Case 419.2 replaced the Criterion and renamed the page, but it signed nothing about the reading entry. This Case signs the retirement of the entry. The code already accepts such an entry without a change. `generate` skips an entry with `superseded_by` without a line on stderr. It writes a decision page only for an entry with `case`, so nothing is written for this entry. `superseded_cases` reads only entries with `case`, so no section of the Spec is skipped. `materialize` does not touch the entry again: it appends only lines that are not in the yaml, and lifts again only an entry with `failed` and no `kind`. Only words change: the docstring of `guppi/materialize.py` lists the writer of each field of an entry and gets a second writer of `superseded_by`, and the Purpose of `rule-materialize` says the same.
> What the frame check showed. `rule-permissions` says that a script writes `materialize.yaml` and that this write is not allowed to the agent. That stays true: the list of permissions does not change, the client asks the person before this edit, and this Case signs the edit itself. The list of yaml marks in `rule-documentation` says nothing of `superseded_by`, so it also stays true. The Criterion of `estimate-materialize-marks-superseded` promises that an entry without `case` gets no mark from `materialize`. `materialize` does not change, so that also stays true. The Criteria of `estimate-render-harness-ticks-the-spec`, `estimate-raw-archive` and `estimate-generate-fails-alone` speak of an entry with `superseded_by` in general. Their behaviour does not change, so none of them gets an `update`. The edit of the Purpose touches no Estimate.
> What the Case does not do. The `read` line in the Spec of session 1228 for the reading of the new Criterion stays unticked: that reading is still to be taken, and the line names the old slug `estimate-frame-check-finds-a-contradiction` until the migration of Case 432 writes the new one. The unit 1228 is dated by the day of the run, so `archive` takes it only at a run on a later day. The open Insight `insight-retro-reading-taken-on-a-criterion-the-session-replaces` asks for the check that keeps such a reading from being written; Case 428.1 brings it in, not this Case.

> **problem:**
> The entry of ledger line 40 of session 1228 never applies, and there is no mark that retires it by a decision. So the unit 1228 is not applied whole, its render lines are not ticked, and `archive` keeps it. It must be decided by which mark and by which writer to retire the entry.

> **given:**
> `raw/2026-09-25/1228/materialize.yaml` — the yaml of session 1228; its entry of ledger line 40, the reading of `estimate-frame-check-finds-a-contradiction`
> **＋** `rule-materialize` — the rule of `materialize`; its Purpose says who marks an entry `superseded_by`
> **＋** `guppi/materialize.py` — its docstring lists each field of an entry with its writer
> **＋** `guppi/generate.py` — `apply`, which skips an entry with `superseded_by`
> **＋** `guppi/render.py` — `applied_whole`, the test before the render lines of a Spec are ticked
> **＋** `guppi/archive.py` — `kept_reason`, the test before a unit moves to the archive
> **＋** `raw/2026-09-25/1228/spec.md` — the Spec of session 1228, which holds its render lines

> **when:**
> The one-off migration of Case 427 sets `superseded_by: '427'` on the entry of ledger line 40 in `raw/2026-09-25/1228/materialize.yaml` and removes its `failed`, and then `uv run guppi generate`, `uv run guppi render` and `uv run guppi archive` run.
> **＋** Someone reads the docstring of `guppi/materialize.py` or the Purpose of `rule-materialize` to learn who writes `superseded_by`.

> **then:**
> `uv run guppi generate` skips the entry: it writes no page for the entry and prints no stderr line for it.
> **＋** `applied_whole` of `guppi/render.py` is true for `raw/2026-09-25/1228/materialize.yaml`, and `uv run guppi render` ticks the render lines of `raw/2026-09-25/1228/spec.md`.
> **＋** `kept_reason` of `guppi/archive.py` gives no reason for the unit 1228, and the first `uv run guppi archive` on a day after 2026-09-25 moves the unit to the archive.
> **＋** The docstring of `guppi/materialize.py` and the Purpose of `rule-materialize` name two writers of `superseded_by`: `materialize` from a `{supersedes:case N}`, and, on an `estimate` entry, the one-off migration of a ratified Case, with the number of that Case as the value.
> **－** The entry sets no `status`, no `## Result` and no `checked` on any page.
> **－** `uv run guppi materialize` does not change the entry again.

```then
update:
- slug: rule-materialize
  replace:
  - old: or each becomes an entry of its own from its ledger line (case 309).
    new: 'or each becomes an entry of its own from its ledger line (case 309). An `estimate` entry carries no `case`, so no `{supersedes}` reaches it: a reading that must not apply is retired only by a ratified Case, whose one-off migration sets `superseded_by` to the number of that Case on the entry and removes its `failed` (case 427).'
  change: a reading that must not apply is retired by a one-off migration of a ratified Case, superseded_by set to its number (case 427)
```

```tasks
- [x] update `rule-materialize` — the Purpose names the retirement of a reading by a ratified Case
- [x] `guppi/materialize.py`: the docstring names the one-off migration of a ratified Case as the writer of `superseded_by` on an `estimate` entry, the number of that Case as the value (case 427)
- [x] one-off migration: in `raw/2026-09-25/1228/materialize.yaml`, the entry `line: 40` gets `superseded_by: '427'` and loses `failed`
- [x] by hand: at the librarian's run after the migration, `generate` prints no line for `estimate-frame-check-finds-a-contradiction`, and `render` ticks the render lines of `raw/2026-09-25/1228/spec.md`
```

## Case 428 — What a session changes, it does not measure: the ledger hook refuses a reading of such an Estimate

> **context:**
> Today the hook `guppi ledger` on `Stop` writes each `estimate[...]` line of a `LEDGER` block into the session's ledger and checks nothing in it. Retro and the end of Work Mode take readings by lists: by a `read` line of an older Spec or by the Work list of the brief. The slug is not held against the decisions of the same session. So an Estimate whose Criterion a Case of this session replaced gets a reading on the old Criterion. That happened in session 1749 with `estimate-retro-loads`. The same happened in session 1228 with `estimate-frame-check-finds-a-contradiction`: a Case of the same session replaced its Criterion and renamed the page. There `generate` failed on the entry, and Case 427 retired it by a one-off migration. Case 283 forbids such a reading, but only in the words of the Render of `rule-retro`, and only while the new Criterion is not built. No code checks that rule.
> The person chose a simple rule: what a session changes, it does not measure. The hook does not write an `estimate[<slug>]` line when a decision line `create` or `update` of `<slug>` stands in this session. The decisions come from the session's `ledger.md` and from the lines the hook writes on the same `Stop`. The hook reads each line by `parse_line` of `guppi/materialize.py`: that is the one parse of a ledger line. The import stands inside the function, because `guppi/materialize.py` imports `guppi/ledger.py`. The hook judges by the ledger alone: it needs no task ticks and no memory in the event log. The condition holds the whole session. So a refused line of the transcript is refused again at every `Stop`. The hook exits 2 with the reason only when the line stands in the reply just finished. It skips an older line without a word. A line of a text followed by a tool call is first judged at the next `Stop` and is also skipped without a word. Its absence shows in the Tail at Retro.
> The hook closes the case of 1228 without the Spec. The decision line `update` names the old slug of the renamed page, and the reading there was taken by the old slug. The hook does not catch a reading by the new slug of the same rename: no decision line names it. The person chose a judgment of the hook by the ledger alone. Retro is the agent's judgment, and the agent may read the Spec. After Case 432 the `read` line of a renamed Estimate names the new slug. So at Retro the exception from debt and the refusal of a reading also cover the slug an `update` of this session renames a page to. Otherwise the renamed Estimate's own `read` line would become debt at the Retro of the same session.
> The cost of the rule. A reading of a new Criterion waits for a later session, even a pytest reading in Work Mode. That may not be the next session: the reading of Case 430 waits for the first prompt past 400 000 tokens. Part of case 280 stops working for this session: a reading after the decision line of its own Case no longer ticks the `read` line of that Case in the same session. A reading of a later session ticks it. But it ticks it only while the unit lies in `raw/`. `tick_read` does not read the archive, and `kept_reason` does not look at open `read` lines. The person accepted this: the status `pending` of the Estimate and the lint finding `unread` carry the debt. This note goes to the handoff, not into the Case. The choice between "built" and "not built" goes away: the rule does not depend on whether the tasks are ticked.
> What the frame check showed. The sentence of `rule-ledger-write` that the hook is "interpreting nothing" becomes false, so the Case changes it by a `replace` pair. The Criterion of `estimate-ledger-write-lifts` promises that each line of a `LEDGER` block lands in the ledger. That becomes false, so sub-case 428.2 replaces it whole. In the Render of `rule-case-protocol` the `estimate[...]` lines are written at the moment the measurement exists. For a measurement of what the session changed that becomes false, so the Render gets one pair. The paragraph of the Render of `rule-retro` on readings takes a reading when the build is finished and closes the line of the old Criterion "at the moment its `method` names". That moment can fall in this same session. So sub-case 428.3 replaces the paragraph whole, together with the Criterion of `estimate-retro-loads`. The opening list of Retro in the Render knows two kinds of an unticked line: waiting for the librarian, or debt. The Criterion of `estimate-retro-report-holds-each-fact-once` says the same. A third kind — a `read` line whose reading waits for a later session — makes both false. Sub-case 428.4 changes them.
> What is not touched. `rule-page-generation` and the Criterion of `estimate-generate-ticks-the-spec` describe what `generate` does with the `read` line of a Case ratified after the reading. They do not say that a reading in the same session occurs, and they stay true. In the Purpose of `rule-materialize` a reading folds into the unapplied `create` of its slug in the unit. The Criterion of `estimate-materialize-assembles` folds an `estimate` line into the `create` of the same unit. `estimate-materialize-refolds-a-reading-on-a-supersede` moves such a folded reading. For the unit of one session this path no longer occurs, because the hook refuses such a line. But these statements stay true of what `materialize` does with a ledger where such a line stands, so they are not touched. In `case-schema.md` the paragraph on tasks stays true: `generate` still ticks the `read` line, only by a reading of a later session. `rule-work-mode` holds only a Purpose, and it is not touched. In the Purpose of `rule-spec-box` the box writes readings into the ledger of its folder. That is a deferred placeholder, and it names the ledger hook inside a worktree as an open question. The Case does not touch it. The other hooks on `Stop` — `guppi ratified`, `guppi casecheck`, `guppi context` — do not judge ledger lines. The slug `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` is free: no page has it in `wiki/` or in `archive/`. There are four sub-cases, because the Case touches four promises.

> **problem:**
> No check holds an `estimate[...]` line against the decisions of its session. So a reading of an Estimate that this session created, replaced or renamed lands in the ledger on a Criterion nobody built. The person chose the rule: what a session changes, it does not measure. It must be decided how the hook checks it and which pages change with it.

### Case 428.1 — The ledger hook does not write a reading of an Estimate this session creates or changes

> **given:**
> `rule-ledger-write` — the rule of the ledger hook
> **＋** `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` — the promise this Case creates
> **＋** `rule-case-protocol` and its render `vault/wiki/case-schema.md` — when the agent writes an `estimate[...]` line
> **＋** `insight-retro-reading-taken-on-a-criterion-the-session-replaces` — the Insight this Case actions
> **＋** `guppi/ledger.py` — `run`, the write of the fresh lines of the session
> **＋** `guppi/materialize.py` — `parse_line`, the one parse of a ledger line
> **＋** `tests/test_ledger.py` — the tests of the hook

> **when:**
> The `Stop` hook `uv run guppi ledger` finds a fresh `estimate[<slug>]` line in a `LEDGER` block of the session, and a decision line `create` or `update` of `<slug>` stands in the session's ledger or among the lines the hook writes on the same `Stop`.

> **then:**
> The line is not written: what a session changes, it does not measure, and the reading of `<slug>` waits for a later session.
> **＋** A reading of the old slug of a page that an `update` of this session renames is refused by the same rule: the decision line names the old slug.
> **＋** The other lines of the `Stop` are written as before.
> **＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: estimate[<slug>] not written — case N creates or updates <slug> in this session; what a session changes it does not measure: take the reading in a later session and name it in the handoff."
> **＋** A refused line of an earlier text of the transcript is skipped at every later `Stop` without a word.
> **－** A reading of a slug that no decision line `create` or `update` of this session names is written as before; a `defer` line of the slug does not refuse it.
> **－** Without a `hi`, and with `stop_hook_active`, the hook acts as before and judges no line.

```then
create:
- slug: estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session
  type: estimate
  kind: QA
  purpose: Whether the ledger hook refuses a reading of an Estimate that a decision line of the same session creates or updates, and says why only for the reply just finished
  method: uv run pytest tests/test_ledger.py — piped payloads and a session ledger in a temp vault
  tags:
  - session
  - hooks
  - harness
  - ledger
  ref: rule-ledger-write
update:
- slug: rule-ledger-write
  replace:
  - old: 'interpreting nothing: the text verbatim,'
    new: the text verbatim,
  - old: and writes nothing, so it cannot loop.
    new: |-
      and writes nothing, so it cannot loop.

      **What a session changes, it does not measure** (case 428.1). An `estimate[<slug>]` line is not written when a decision line `create` or `update` of `<slug>` stands in the session's ledger or among the lines of the same `Stop`, each line read by `parse_line` of `guppi/materialize.py`; a reading of the old slug of a page an `update` renames falls under the same rule, since the decision line names the old slug. The reading waits for a later session. The judgment reads the ledger alone and holds the whole session, so a refused line of the transcript is refused again at every `Stop`: the hook exits 2 with one stderr line per refused line only when the line stands in the reply just finished, and skips an older one without a word. A reading of the new slug of a rename is not caught here: no decision line names it.
  set:
    implementation_ref:
    - guppi/ledger.py
    - guppi/materialize.py
    - guppi/gate.py
    - tests/test_ledger.py
    - tests/test_gate.py
    - .claude/settings.json
  change: the hook refuses a reading of an Estimate that a decision line of the session creates or updates (case 428.1)
- slug: rule-case-protocol
  replace:
  - old: lines the moment the measurement or the lesson exists,
    new: lines the moment the measurement or the lesson exists — a reading of an Estimate that a decision line of this session creates or updates waits for a later session, and the ledger hook refuses it (case 428.1) —
  change: a reading of an Estimate the session creates or updates waits for a later session (case 428.1)
- slug: insight-retro-reading-taken-on-a-criterion-the-session-replaces
  set:
    status: actioned
    addressed_by: decision-case-428.1
  change: 'actioned: the ledger hook refuses a reading of an Estimate that a decision line of the same session creates or updates (case 428.1)'
```

```tasks
- [x] update `rule-ledger-write` — How it works names the refusal; `implementation_ref` names `guppi/materialize.py` and `tests/test_ledger.py`
- [x] create `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session`
- [x] update `rule-case-protocol` — an `estimate[...]` line of a change of the session waits for a later session
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] update `insight-retro-reading-taken-on-a-criterion-the-session-replaces` — actioned
- [x] `guppi/ledger.py`: `run` parses the lines of the session's `ledger.md` and the fresh lines by `materialize.parse_line`, imported inside the function; an `estimate` line whose slug a `create` or `update` decision line names is not written; exit 2 with one stderr line per refused line of `last_assistant_message`, silence for an older one; the docstring names the refusal (case 428.1)
- [x] `tests/test_ledger.py`: a reading of a slug with a `create` line, and with an `update` line, in the session's ledger is refused, the other lines written; a decision line in the same reply refuses it too; the stderr line and exit 2 for a refused line of the finished reply, exit 0 and no line for one of an earlier text; a reading of a slug with a `defer` line only, or with a decision line of another session, is written
- [ ] read `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session`
```

### Case 428.2 — The promise of the ledger excepts a refused reading

> **given:**
> `estimate-ledger-write-lifts` — the promise that every line of a `LEDGER` block lands in the ledger once
> **＋** `rule-ledger-write` — its target, the rule of the ledger hook
> **＋** `guppi/ledger.py` — the hook
> **＋** `raw/<hi date>/<hi HHMM>/ledger.md` — the session's ledger, which the hook writes
> **＋** `guppi/gate.py` — the refusal of a `Skill` call for an item of the Spec without a ledger line, and its advice to the agent
> **＋** `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` — the refusal of Case 428.1, which this promise excepts

> **when:**
> The `Stop` hook `uv run guppi ledger` fires at the end of a turn of the main agent, with `transcript_path` and `last_assistant_message` in its payload; or `guppi gate` refuses a `Skill` call for an item of the Spec without a ledger line.

> **then:**
> In a session with a `hi` recorded, every line `- decision[`, `- estimate[`, `- lesson[` inside a `LEDGER` block of any text of the main agent in the transcript, the reply just finished included, lands in `raw/<hi date>/<hi HHMM>/ledger.md` with the time of writing, once — a body already in the ledger of any session is not written again.
> **＋** A block in a text followed by a tool call in the same turn reaches the ledger at the next `Stop` of the session, with the time of that `Stop`; the reply that ends in the text lands it now.
> **＋** The gate's advice to the agent reads "The text before a tool call waits for the next Stop: end this reply in text with the LEDGER block, then call /<skill> in the next reply."
> **－** An `estimate[...]` line the hook refuses by `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` does not land.
> **－** Without a `hi`: exit 2 with the reason, the ledger untouched; with `stop_hook_active`: exit 0, nothing written.
> **－** The last turn of a session that ends in a tool call has no `Stop` after it; its lines are a finding of Retro, not of the hook.

```then
update:
- slug: estimate-ledger-write-lifts
  set:
    status: pending
  change: the Criterion replaced whole — a reading the hook refuses as a change of the session does not land; Given dropped, its input moved into When (case 428.2)
```

```tasks
- [x] update `estimate-ledger-write-lifts` — its Criterion replaced whole by the `when` and `then` of this Case
- [ ] read `estimate-ledger-write-lifts`
```

### Case 428.3 — Retro takes no reading of what the session changed

> **given:**
> `rule-retro` — the rule of `/retro`; its Render says which readings Retro takes
> **＋** `.claude/skills/retro/SKILL.md` — the file its Render writes
> **＋** `estimate-retro-loads` — the promise of the readings at Retro
> **＋** `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` — the refusal of Case 428.1, which Retro follows

> **when:**
> The person invokes `/retro`, and the agent takes the readings of the session's Estimates.

> **then:**
> A reading measures the Criterion the page carries at the moment of the reading — the one ratified last; its line is written only when the work that Criterion names is built — rendered, written, run.
> **＋** An Estimate that this session creates or updates — by a decision line of its slug, or by an `update` that renames a page to it — gets no reading in this session, built or not; the handoff names it as a reading of a later session.
> **＋** The `read` line of its old Criterion in an earlier Spec is not read; the reading of the new Criterion closes it in a later session, at the moment its `method` names.
> **－** A reading of an Estimate this session neither creates nor updates is taken as before, once its work is built.

```then
update:
- slug: rule-retro
  replace:
  - old: |-
      Take the readings of this session's Estimates whose work is finished and write their
      lines; name in the handoff any Estimate whose reading cannot be taken yet. A reading measures the Criterion the page carries at the moment of the reading, the one ratified last, and its line is written only when the work that Criterion names is built; an Estimate whose Criterion a Case of this session replaced and whose build is not finished at Retro has no reading in this session — the `read` line of the old Criterion in an earlier Spec is not debt and is not read, the reading of the new Criterion closes it at the moment its `method` names (case 283).
    new: 'Take the readings of the Estimates whose work is finished and that this session neither creates nor updates — by a decision line of its slug, or by an `update` that renames a page to it — and write their lines; name in the handoff any Estimate whose reading cannot be taken yet, and every Estimate this session creates or updates. A reading measures the Criterion the page carries at the moment of the reading, the one ratified last, and its line is written only when the work that Criterion names is built. What a session changes, it does not measure: an Estimate this session creates or updates has no reading in this session, built or not, and the ledger hook refuses one (case 428.1); the `read` line of its old Criterion in an earlier Spec is not debt and is not read, and the reading of the new Criterion closes it in a later session, at the moment its `method` names (cases 283, 428.3).'
  change: Retro takes no reading of an Estimate the session creates or updates, built or not (case 428.3)
- slug: estimate-retro-loads
  set:
    status: pending
  change: the Criterion replaced whole — an Estimate the session creates or updates gets no reading at its Retro, built or not (case 428.3)
```

```tasks
- [x] update `rule-retro` — the Render: no reading of what the session changes, in this session
- [x] update `estimate-retro-loads` — its Criterion replaced whole by the `when` and `then` of this Case
- [x] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
- [ ] read `estimate-retro-loads`
```

### Case 428.4 — The opening list of Retro: a `read` line of what the session changed waits for a later session

> **given:**
> `rule-retro` — the rule of `/retro`; its Render says how the opening list marks an unticked box
> **＋** `.claude/skills/retro/SKILL.md` — the file its Render writes
> **＋** `estimate-retro-report-holds-each-fact-once` — the promise of the opening list and the close of Retro
> **＋** `guppi/tail.py` — `uv run guppi tail`, the Tail the skill loads
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the session's Spec, whose unticked boxes the list holds

> **when:**
> The person invokes `/retro` in a session where `uv run guppi tail` prints its decision lines and `raw/<date>/<hi HHMM>/spec.md` holds unticked boxes; the agent writes the opening message and the close.

> **then:**
> The opening message holds one numbered list of what is not done: the unticked boxes of `raw/<date>/<hi HHMM>/spec.md` per Case, each marked as waiting for the librarian, as waiting for a later session, or as debt, and what the agent noticed during Work Mode.
> **＋** A `read` line is marked as waiting for a later session when this session creates or updates its slug — by a decision line of that slug, or by an `update` that renames a page to it; another `read` line without its line in the Tail is debt.
> **－** The opening message holds no list of the ratifications.
> **＋** The close holds every ratification of the session, one line per Case, from `uv run guppi tail` grouped by Case, this session's folder first, a Case a `{supersedes:case N}` line names not counted.
> **＋** The close holds what got done.
> **＋** The close holds what is not done: the numbers of the opening list, each with the end it took.
> **－** No ratification and no box is named twice in the report.

```then
update:
- slug: rule-retro
  replace:
  - old: — a `read` line without its line in the Tail is debt,
    new: — a `read` line whose slug this session creates or updates, by a decision line of that slug or by an `update` that renames a page to it, listed as waiting for a later session, neither debt nor the librarian's (case 428.4) — another `read` line without its line in the Tail is debt,
  change: the opening list of Retro marks a read line of a change of the session as waiting for a later session (case 428.4)
- slug: estimate-retro-report-holds-each-fact-once
  set:
    status: pending
  change: 'the Criterion replaced whole — a third mark in the opening list: a read line whose reading waits for a later session (case 428.4)'
```

```tasks
- [x] update `rule-retro` — the Render: the opening list marks a `read` line of a change of the session as waiting for a later session
- [x] update `estimate-retro-report-holds-each-fact-once` — its Criterion replaced whole by the `when` and `then` of this Case
- [x] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
- [ ] read `estimate-retro-report-holds-each-fact-once`
```

## Case 429 — Several `{supersedes:case N}` on one decision line

> **context:**
> A decision deferred several times stands in the `deferred_by` of its page under each Case that deferred it. When the decision is taken up, the decision line carries `{supersedes:case N}`. `parse_line` in `guppi/materialize.py` parses a ledger line for all readers. It puts the marks in braces into a dictionary, and of two blocks with one key the last stays. So a line holds one `supersedes`, and `lift_line` marks `superseded_by` on the entries of one Case only. `decision_record` builds the list `supersedes` from the entries of a Case, and `generate` already walks that list. For each decision named it sets `superseded` and removes its slug from the `deferred_by` of the targets (`clear_deferred_by`). So the limit sits only in the parse of the line. The case of `rule-context-size` showed it: its Case has fewer decision lines than defers. A second `update` line of the same slug is no way out: it would apply the same `then` item twice.
> The form of the mark. The grammar already knows a repeated block: `{addresses:<lesson slug>}` stands once per lesson, and `parse_line` collects it into a list (case 284.2). Several `{supersedes:case N}` blocks side by side fit the same grammar and the same `BRACES`. A list inside one block, `{supersedes:case 1,case 2}`, is read by today's parse without a word as one Case with the number `1,case 2`. The ledger hook writes the line verbatim and does not judge marks. By Case 428.1 it will read lines by `parse_line`, but only the kind and the slug. `casecheck` passes the parsed records whole to `judge` of `guppi/prespec.py`, and `judge` reads `supersedes` through `superseded_in_window`. Lint reads the field `supersedes` of a decision page, and that is already a list. All readers get the parse by import from one module, as `CLAUDE.md` asks. Before this session no decision line in a ledger under `vault/` carried two real marks. The only line with two blocks lies in the archive and holds `{supersedes:case N}` as text. In the ledger of this session the line of Case 430 already carries several blocks. Only `materialize` as this Case changes it reads that line right.
> Where the form changes. The field `supersedes` of a yaml entry becomes a list, like `addresses`. In the yamls already written it is one value. `decision_record` rebuilds the decision record from all entries of the unit, so it reads the old form too. `superseded_in_window` today turns the value into a string. With a list it would give a junk key, so it walks each Case of the list. Through it `check_lines`, the demand for a `tasks` block, the comparison with the ratified copy and the check of an answer of `case-guppi` in `casecheck` get the same. The code of `generate` does not change: `decision-case-419.2` already shows it, with two `supersedes` from two lines.
> What taking up a deferred decision retires. One short-form Case can defer several pages at once, as the archived `decision-case-416` did. `generate` removes the defer the line supersedes from the `deferred_by` of each target of its `defer` list, not only from the page taken up. The new rule asks to name each Case of the page's `deferred_by`. So taking up one page also retires the same defers from the other pages they hold. That will be so for `rule-work-mode` and `rule-subagent-guppi`, which share their defer Cases. That is existing behaviour of `generate`, and the Case does not change it. A page that stays open gets a new defer at the close of Plan Mode.
> What the frame check showed. The Case creates no page, so no vault query is due. The Render of `rule-case-protocol` speaks of the mark in two places. On taking up a deferred decision it says "writing `{supersedes:case N}` on the line", and on the ledger line it says the mark stands "when they apply". Both places get a `replace` pair, and `vault/wiki/case-schema.md` is rendered again. The glossary line in `entity-glossary` speaks of one Case per mark. It gets a pair, and `vault/wiki/glossary.md` is rebuilt.
> Two promises in one Case. The Criterion of `estimate-materialize-marks-superseded` speaks of a line with one mark. That is the promise of `materialize` the Case changes, so its Criterion is replaced by the `when` and `then` of the Case. The Criterion of `estimate-case-protocol-ledger-line-form` speaks of the form of a line as the agent writes it. Its "`{supersedes:case N}` when it applies" admits both a line with a list inside one block and a taken-up decision that names only part of its defers. The new rules of the Render are not checked by that Criterion. So its Criterion is also replaced whole, by the text the item writes under `sections`. So one Case touches two promises (case 204), and `judge` accepts that form. A split into sub-cases would need new numbers and `{supersedes:case 429}` on a ratified Case, and its heading would stay in the plan. The method of this Estimate also gets the first take-up of a decision with several Cases in its `deferred_by`. The readings of both Estimates wait for the next session (case 428.1).
> Which Estimates do not change and why. The Criterion of `estimate-materialize-refolds-a-reading-on-a-supersede` speaks of a line with `{supersedes:case N}` and a `create` of Case N that holds `folded`. The edit runs `refold` for each block of the line on its own, so each of its statements stays true for each Case named, and its Criterion is not replaced. `estimate-prespec-catches-a-superseded-case`, `estimate-prespec-requires-a-task-line` and `estimate-prespec-checks-the-ratified-copy` speak of any mark of the window. `estimate-retro-report-holds-each-fact-once` and the Renders of `rule-retro` and `rule-prespec` also speak of the Case the mark names. After the edit of `superseded_in_window` all of that stays true for each mark. `estimate-generate-writes-the-decision-page` speaks of each `supersedes` of a decision record, and `generate` does not change. `estimate-materialize-assembles` names the field `supersedes`, but not its form. The Case adds or changes no hook.

> **problem:**
> One decision line can retire only one defer. So a decision deferred several times, once taken up, leaves the other Cases in `deferred_by` and their entries without `superseded_by`. The form of several marks on one line must be chosen, and `materialize` must mark each Case named.

> **given:**
> `guppi/materialize.py` and `tests/test_materialize.py` — `parse_line`, the one parse of a ledger line; `lift_line`, `refold` and `decision_record`, the supersede mark; and their tests
> **＋** `guppi/prespec.py` and `tests/test_prespec.py` — `superseded_in_window`, which `judge` and `guppi/casecheck.py` reach, and its tests
> **＋** `estimate-materialize-marks-superseded` — the promise of the mark
> **＋** `estimate-case-protocol-ledger-line-form` — the promise of the written form of a ledger line and its marks
> **＋** `rule-case-protocol` and its render `vault/wiki/case-schema.md` — the form of a ledger line and the take-up of a deferred decision
> **＋** `entity-glossary` and its render `vault/wiki/glossary.md` — the term `supersedes`
> **＋** `CLAUDE.md` "One judgment, one implementation" — the parse of a ledger line lives in one module

> **when:**
> `uv run guppi materialize` lifts a decision line that carries one `{supersedes:case N}` block or several, and the entries of each Case N stand in this unit's `materialize.yaml` or in the `materialize.yaml` of another unit.

> **then:**
> For each Case N that a block of the line names, every entry with `case: N` gets `superseded_by`, whatever its kind, and the `decisions` record of that Case gets it too.
> **＋** The entry of the line carries `supersedes` as a list with one Case per block, in the order of the blocks. The `decisions` record of its Case lists under `supersedes` every Case that its lines name.
> **＋** The `materialize.yaml` of another unit is written with that mark only.
> **＋** An entry of Case N marked while no heading of Case N stands in the unit's `spec.md` carries no `incomplete: [then]`, and its `decisions` record no `case_text` and no `incomplete` for a section.
> **－** An entry without `case` — an `estimate` or a `lesson` entry — gets no mark.
> **－** An entry of an existing `materialize.yaml` whose `supersedes` is one value, not a list, is read as a list of one.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: and writing `{supersedes:case N}` on the line.
    new: and writing on one of its decision lines one `{supersedes:case N}` block for each Case in the page's `deferred_by`, so that every defer of the page is retired (case 429).
  - old: '`{source:...}` and `{supersedes:...}` are present only when they apply (case 75.1);'
    new: '`{source:...}` and `{supersedes:...}` are present only when they apply (case 75.1), and a line carries one `{supersedes:case N}` block per Case it supersedes, several side by side, never a list inside one block (case 429);'
  change: a decision line carries one {supersedes:case N} block per Case it supersedes; a deferred decision taken up names every Case of its deferred_by (case 429)
- slug: entity-glossary
  replace:
  - old: written `{supersedes:case N}`, which marks every entry of that Case superseded and clears its `deferred_by` (case 200.2)
    new: written `{supersedes:case N}`, one block per Case and several on one line, each of which marks every entry of its Case superseded and clears its `deferred_by` (cases 200.2, 429)
  change: 'the term supersedes: one block per Case, several on one line (case 429)'
- slug: estimate-materialize-marks-superseded
  set:
    status: pending
  change: the Criterion replaced whole — a decision line may carry several {supersedes:case N} blocks, and each named Case is marked (case 429)
- slug: estimate-case-protocol-ledger-line-form
  set:
    status: pending
    method: 'by hand: the ledger and the preview of the first session where a lesson and the Case that closes its cause stand together, and of the first Case that takes up a decision with more than one Case in its deferred_by'
  sections:
    Criterion: |-
      When:
      The agent writes the ledger lines of a session: the decision lines in the reply that acknowledges a ratification, a lesson line the moment the lesson exists.

      Then:
      A decision line is `- decision[case N][kind][slug]` with `{ref:...}` when the target has a ref, `{tags:...}` on a `create`, and `{supersedes:case N}` when it applies.
      **＋** A line that supersedes more than one Case carries one `{supersedes:case N}` block per Case, side by side, never a list inside one block.
      **＋** A Case that takes up a deferred decision carries, on one of its decision lines, one `{supersedes:case N}` block for each Case in the page's `deferred_by`.
      **＋** When a Case of this session closes the root cause of a lesson of this session, the line written second carries the mark: `{addresses:<lesson slug>}` on the decision line when the lesson line stands first, `{addressed_by:case N}` on the lesson line when the decision lines stand first; one mark per lesson.
      **＋** The mark stands in the preview of the ledger lines the person ratifies, or in the `LEDGER` block of the lesson line.
      **－** A lesson whose fix is ratified in another session gets no mark.
  change: the Criterion replaced whole — one {supersedes:case N} block per Case, never a list; a deferred decision taken up names every Case of its deferred_by (case 429)
```

```tasks
- [x] update `rule-case-protocol` — the Render: one `{supersedes:case N}` block per Case on a line; a deferred decision taken up names every Case of its `deferred_by`
- [x] update `entity-glossary` — the term `supersedes`: one block per Case, several on one line
- [x] update `estimate-materialize-marks-superseded` — its Criterion replaced whole by the `when` and `then` of this Case
- [x] update `estimate-case-protocol-ledger-line-form` — its Criterion replaced whole by the text below; the method names the first take-up of a decision deferred more than once
- [x] `guppi/materialize.py`: `parse_line` returns `supersedes` as a list, one Case per `{supersedes:case N}` block, as it does for `addresses`; `lift_line` marks and refolds each Case of the list, here or in another unit's yaml; `decision_record` reads a list and the one value of an existing yaml; the docstring says a line may carry several blocks (case 429)
- [x] `tests/test_materialize.py`: a line with two blocks marks the entries and the `decisions` records of both Cases, one in this unit and one in another unit's yaml; its entry carries both in order; a folded reading of a `create` of each Case is refolded; an existing entry with one value is read as a list of one; the assertions on one value become a list of one
- [x] `guppi/prespec.py`: `superseded_in_window` takes each Case of the list
- [x] `tests/test_prespec.py`: a line of the window with two blocks — both Cases need no item, both headings still in the plan are two findings, both sections of the ratified copy are no finding
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] `uv run guppi glossary`
- [ ] read `estimate-materialize-marks-superseded` — in the next session (case 428.1)
- [ ] read `estimate-case-protocol-ledger-line-form` — in the next session (case 428.1)
```

## Case 430 — The context-size note past 400 000 tokens: information, not an order

> **context:**
> Two hooks count the size of the context from the transcript. The hook `uv run guppi context` on `Stop` shows the person a line with the size after each reply. Past 400 000 tokens it appends `— past 400 000: close the session` to it. The hook `uv run guppi context --prompt` on `UserPromptSubmit` prints an order to the agent past the limit: open the reply by saying that the session must be closed by /retro, then /handoff, before the next Case. Below the limit it is silent.
> In session 1228 the limit was passed at 456 635 tokens. The hook printed the order, but the person had just asked for /retro, and the agent called /retro at once without opening its reply with the recommendation. So the reading of `estimate-context-size-warns-past-the-limit` is recorded `failed`. Its Criterion promises an order the agent obeys.
> The person said that past 400 000 the hook must not demand to finish at once, but inform: the session is already costly, taking on new work is not recommended, and when the Frontier holds open items, deferring them is better. That is an informative note, not a direct instruction. The limit of 400 000 stays: in the person's words, the rest works, with no complaints. This also answers the question of Cases 404, 409, 418 and 422. Case 404 deferred the limit, and Cases 409, 418 and 422 the limit and the text of the hook past it, to a session that reaches the limit. Case 409 already recorded that the person reads the note as "take no more work", not as an order to go to Retro at once. Case 429 allowed several `{supersedes:case N}` on one decision line. So the line of `rule-context-size` retires all four deferred decisions at once.
> C5 and C9 are one Case without sub-cases. Both items are about the text past the limit, and it lies in one promise, `estimate-context-size-warns-past-the-limit`. Its Criterion is replaced whole. The line of the hook on `Stop` changes its end with it: `close the session` is the same kind of order, and in the same Criterion. Otherwise the person's words would stay true only in half. If the end of the line must stay, that is a change of this Case.
> What the frame check showed. How it works of `rule-context-size` has a sentence on the order. It becomes false, so the Case changes it by one `replace` pair. The Purpose of `rule-context-size`, that the person sees how full the context is, stays true. The field `purpose` of `estimate-context-size-warns-past-the-limit` says that the agent tells the person to close the session. That becomes false, so it is replaced together with the Criterion. The Criterion of `estimate-context-size-shown-after-each-reply` promises only the start of the line on `Stop`, so the Case does not touch it. Two more hooks run on `UserPromptSubmit` beside `guppi context --prompt`. `guppi event prompt` writes the `hi` line on `/hi` (`rule-event-log`). `guppi gate` refuses a typed `/pre-spec`, `/retro`, `/handoff` by the rules `rule-retro-commit` and `rule-ledger-write`. None of them reads the output of `guppi context`, and the note contradicts none of them. The commands in `.claude/settings.json` and the Render of `rule-hook-registry` do not change. The docstrings of `guppi/context.py` and `tests/test_context.py`, and the test of the limit, name the old order; the tasks edit them. The decision pages of 392.2 and of the earlier defers are history, and the Case does not edit them. There is no `create`, so no vault query is due. By Case 428.1 the next session measures the new Criterion, at the first prompt past 400 000 tokens.

> **problem:**
> Past 400 000 tokens the hook gives the agent an order to close the session, and the person wants only an informative note. The Criterion promises that the agent obeys the order, and the reading of that promise failed. It must be decided what both hooks say past the limit and what the Estimate promises.

> **given:**
> `rule-context-size` — the rule of the context-size hooks; its How it works states what they print past the limit
> **＋** `estimate-context-size-warns-past-the-limit` — the promise past 400 000 tokens
> **＋** `guppi/context.py` — `prompt_text` and `stop_line`, the texts past the limit
> **＋** `tests/test_context.py` — the tests of the limit
> **＋** `.claude/settings.json` — the `UserPromptSubmit` hook `uv run guppi context --prompt` and the `Stop` hook `uv run guppi context`

> **when:**
> The person sends a prompt and the `UserPromptSubmit` hook `uv run guppi context --prompt` reads the transcript; after the reply the `Stop` hook `uv run guppi context` runs.

> **then:**
> At N of 400 000 or more, the `UserPromptSubmit` hook prints to the agent's context `context: <N> tokens, past 400 000 — the session is already costly` and a note for the person, not an order: taking on more work is not recommended, and while the Frontier holds open items, deferring them is the better course.
> **＋** The agent passes the note to the person in its reply and goes on with what the person asked.
> **＋** At N of 400 000 or more, the line of the `Stop` hook ends with `— past 400 000: costly, better take no more work`.
> **－** No text of either hook orders the agent or the person to close the session, and none names /retro or /handoff.
> **－** Below 400 000 the `UserPromptSubmit` hook prints nothing, and the line of the `Stop` hook has no such end.

```then
update:
- slug: rule-context-size
  replace:
  - old: 'At N of 400 000 or more the line ends with `— past 400 000: close the session`, and `uv run guppi context --prompt` on `UserPromptSubmit` prints to the agent''s context the size and the order to tell the person to close the session with /retro, then /handoff, before the next Case;'
    new: 'At N of 400 000 or more the line ends with `— past 400 000: costly, better take no more work`, and `uv run guppi context --prompt` on `UserPromptSubmit` prints to the agent''s context the size and a note for the agent to pass to the person, not an order: the session is already costly, taking on more work is not recommended, and while the Frontier holds open items, deferring them is the better course (case 430);'
  change: past 400 000 tokens both hooks give a note, not an order to close the session; the limit stays (case 430)
- slug: estimate-context-size-warns-past-the-limit
  set:
    status: pending
    purpose: Past 400 000 tokens of context the agent passes the person a note that the session is costly and more work is not recommended
  change: the Criterion replaced whole — past 400 000 tokens a note for the person, not an order to close the session (case 430)
```

```tasks
- [x] update `rule-context-size` — How it works: past the limit a note for the person, not an order
- [x] update `estimate-context-size-warns-past-the-limit` — its Criterion replaced whole by the `when` and `then` of this Case
- [x] `guppi/context.py`: `prompt_text` prints `context: <N> tokens, past 400 000 — the session is already costly.` and the note for the agent to pass to the person — taking on more work is not recommended; while the Frontier holds open items, deferring them is the better course (rule-context-size); `stop_line` ends with `— past 400 000: costly, better take no more work`; the docstring says the same (case 430)
- [x] `tests/test_context.py`: past the limit the prompt text holds the note and neither `/retro` nor `/handoff`, and the `Stop` line ends with `— past 400 000: costly, better take no more work`; below the limit, as before; the docstring names case 430
- [x] `uv run pytest tests/test_context.py`
- [ ] read `estimate-context-size-warns-past-the-limit`
```

## Case 431 — The form of a Case in the chat: a Criterion on the Case `case-guppi` built, with no new check

> **context:**
> `estimate-case-protocol-case-form` promises the form of a Case shown in the chat. It is read by hand over the Cases of a session at its close. The last reading, in session 0051, stands `failed`. The `context` of one Case held a count of items, and the Case was not about it. The `then` of another Case held a `－` line that described bookkeeping, not behaviour. `ask-guppi` found these faults at pre-spec, that is after the person had seen the Case.
> Now the agent `case-guppi` builds each Case. Before the showing the hook `guppi casecheck --subagent` (`rule-case-check`) runs its answer through `judge` of `guppi/prespec.py` and through the check of the chat form. The script catches the order of sections and a missing section, anything extra in the `ratification` fence, a `then` item without a decision line, an Estimate without a `read` line. `check_frame` also catches a slug or path in `when` and `then` that `given` does not name. No check catches a count in `context`: the Purpose of `rule-case-check` and the docstring of `guppi/casecheck.py` say plainly that the script does not tell a count from other words. The script catches a bookkeeping `－` line only when it names a slug or path that `given` does not name. A line that names a thing of `given` but speaks of a record, not of behaviour, passes. The new finding of `judge` of this session, a second item of one slug, does not touch these faults. So only `case-guppi`'s own reading of the schema holds these faults, and only this Estimate checks them.
> The Criterion of the Estimate nearly matches the Render of `rule-case-protocol`, but it has fallen behind it. `When:` says that the agent shows the Case. Now `case-guppi` builds the Case, and the main agent shows it unchanged. The line on `context` does not ask what the Render asks: that `context` says what `case-guppi` found in the frame. The other lines of the Criterion match the Render and stay as they are.
> What the frame check showed. The Render of `rule-case-protocol` and the Purpose of `rule-case-check` stay true: the Case changes neither the form nor the checks. The Criterion of `estimate-case-check-sends-back-a-faulty-case` speaks of the findings of `judge` in general, and the Criterion of `estimate-case-build-writes-the-case` speaks of what `case-guppi` reads and what it answers. The Case does not touch them. `estimate-case-protocol-shows-the-built-case` also holds the phrase on the agent's text after the horizontal rule. There it describes the same behaviour from the side of the showing, so it stays in both Estimates. The Case changes no code, and no second copy of one judgment appears. There is no `create` here, so no vault query is due. By the rule of this session a reading of an Estimate the session changes waits for the next session.

> **problem:**
> The reading of the form of a Case stands `failed`. No check catches a count in `context` or a bookkeeping `－` line, and the Criterion has fallen behind the Render. It must be decided whether to keep the Criterion and read it again, to replace it, or to move a part of the form into a check.

> **given:**
> `estimate-case-protocol-case-form` — the promise of the form of a Case shown in the chat
> **＋** `rule-case-protocol` and its render `vault/wiki/case-schema.md` — the form of a Case in the chat
> **＋** `.claude/agents/case-guppi.md` — the agent that builds each Case
> **＋** `rule-case-check` — the checks that run on an answer of `case-guppi` before it is shown

> **when:**
> The main agent shows in the chat a Case that `case-guppi` built, at its first showing or again.

> **then:**
> The Case opens with the heading `## Case N — name`, a sub-case with `### Case N.M — name` under its parent, and holds its sections in the order of the Sections table of `vault/wiki/case-schema.md`, each one blockquote whose first line is `**name:**`.
> **＋** `context` is prose: the mechanism in plain words first, then the state of the pages the Case changes, the vault's answer, what `case-guppi` found in the frame and why an Estimate of the rule is not touched; a case number stands in `context` or `problem` only when the Case is about that case, and a count of items stands in none of the story sections unless the Case is about that count.
> **＋** `given` holds the frame, one thing per line — each page, module, file and test the Case touches and the rule that constrains, its slug or path in a code span and its role — and no state.
> **＋** In `given`, `when` and `then` each line after the first opens with `**＋**` or `**－**`, a `**－**` line names something of `given` or `when`, and `then` holds behaviour only.
> **＋** `tasks` names by slug each Estimate the Case creates or replaces, and under a line whose item writes content that content stands as sub-points; no `contract` line and no "block N" line.
> **＋** A pair under `replace` or `reword` stands only when the Case says what the sentence around each match names; a Case that changes the behaviour of a page gives an `update` to each Estimate of that page whose Criterion speaks of the change.
> **＋** `ratification` holds only the preview of the ledger lines in an untagged fence; the agent's own text stands after the Case, after one horizontal rule, and the reply ends with a plain question.
> **＋** A Case with sub-cases is shown in one reply: the parent's `context`, `problem` and `recommend`, then each sub-case whole.

```then
update:
- slug: estimate-case-protocol-case-form
  set:
    status: pending
  change: the Criterion replaced whole — a Case built by case-guppi, and its context says what case-guppi found in the frame (case 431)
```

```tasks
- [x] update `estimate-case-protocol-case-form` — its Criterion replaced whole by the `when` and `then` of this Case
- [ ] read `estimate-case-protocol-case-form`
```

## Case 432 — Action on the Insight on the silent schema: the check before the showing and the new slug of a renamed Estimate

> **context:**
> The Insight `insight-workflow-case-schema-silent-on-what-the-scripts-accept` describes this mechanism. The Case schema does not say how the scripts read the text of a Case. The agent writes a form the scripts do not accept, and only pre-spec finds it. Case 383 first closed the Insight: the schema named the limits for a `replace` pair and for the `given` of a sub-case. Then `addressed_by` went to `decision-case-393`. The librarian of session 1228 added the lessons `lesson-prespec-read-line-of-a-renamed-estimate` and `lesson-prespec-wikilink-to-a-decision-page-not-yet-written` to the Insight, and the Insight became `open` again. The `Stop` hook found both faults after the ratification. The `SubagentStop` hook did not run yet then.
> Case 419 changed the place where such a form is found. `case-guppi` builds each Case. `guppi casecheck --subagent` builds a Spec in memory from its answer and runs `judge` of `guppi/prespec.py` on it. `judge` is the same checks as at pre-spec. When there is a finding, the agent is sent back, and the person does not see that Case. `judge` holds `check_bare_links` and `check_tasks`. So the part "only pre-spec finds it" of the Insight is no longer true. `check_bare_links` refuses a link `[[decision-case-N]]` to a decision page that does not exist yet before the showing. A working form already exists: the slug without brackets under `set`. Case 419.3 wrote it so, and the link appeared on the page of `insight-case-form-chat-form-read-by-no-script`.
> The lesson on the rename has another cause: two scripts decide in different ways which slug stands on a read line. `estimates_to_read` takes the slug of the `then` item, that is the old slug. The ticker `tick_read` in `guppi/generate.py` ticks a line by the slug of the reading entry. After `generate` the page lives under the new slug, and the reading names the new slug. The check before the showing makes `case-guppi` write the old slug, and the ticker never ticks such a line. That happened in the Spec of session 1228: no reading of W1 and W2 ticks the read lines of `estimate-case-protocol-checks-its-frame` and `estimate-frame-check-finds-a-contradiction`. So the early check does not close this lesson: it asks for the wrong form.
> The proposal of the Insight is to write the limit beside each form in the schema. That is a second copy of a judgment that already stands in `judge`. By the rule "one judgment, one implementation" such a copy is a defect from its first day.
> The frame check showed the following. The Render of `rule-prespec` describes the read line in one place, and the Case adds one `replace` pair there. The Criterion of `estimate-prespec-requires-a-task-line` speaks exactly of the read line, so the Criterion is replaced whole by the `when` and `then` of this Case. The Criterion of `estimate-generate-ticks-the-spec` speaks of the ticker, and the ticker does not change. The Criterion of `estimate-case-check-sends-back-a-faulty-case` speaks of the findings of `judge` in general. The Criterion of `estimate-prespec-checks-the-plan` speaks of the session, the window and the parse of lines. None of them is touched. `vault/wiki/case-schema.md` asks for a read line for an Estimate "by its slug". After this Case that is the new slug, so the phrase stays true, and no Estimate of `rule-case-protocol` is touched. There is no `create` in the Case, so no vault query is due.
> What the Case does not do. It does not write the limits of the scripts into the schema. It changes neither `check_bare_links` nor the ticker.

> **problem:**
> The Insight is `open` again and must be closed: actioned, rejected, or its proposal taken as it stands. The pattern "only pre-spec finds the form" is no longer true after Case 419. But one of the new lessons shows that the check before the showing asks, for a renamed Estimate, for a read line the ticker does not tick.

> **given:**
> `rule-prespec` and its render `.claude/skills/pre-spec/SKILL.md` — its Render names the task line of a reading
> **＋** `estimate-prespec-requires-a-task-line` — the promise that each Estimate to read has a read line of its own
> **＋** `guppi/prespec.py` — `estimates_to_read` and `check_tasks`, run by `judge`
> **＋** `tests/test_prespec.py` — the tests of the task line
> **＋** `guppi/generate.py` — `tick_read`, which ticks a read line by the slug of a reading
> **＋** `insight-workflow-case-schema-silent-on-what-the-scripts-accept` — the Insight this Case actions
> **＋** `raw/2026-09-25/1228/spec.md` — the Spec of session 1228, which holds read lines of renamed Estimates

> **when:**
> `uv run guppi prespec --check <plan>` reads the `tasks` block of each Case of the plan.

> **then:**
> A Case with a decision line of a kind other than `defer` in the window and no `tasks` block is the finding `case N: decision lines and no tasks block`.
> **＋** An Estimate the Case's `then` block creates or sets `pending` needs a line `` - [ ] read `<slug>` `` whose first backticked slug is that Estimate, matched by `READ_LINE`; with none, the finding `case N: <slug> has no task line`.
> **＋** An Estimate whose `update` carries `rename` is that Estimate under the slug of its `rename`, the slug its reading names; a read line of its old slug is not its own task line.
> **＋** A slug named only on another Estimate's read line is the finding `case N: <slug> is named on another read line, not its own`.
> **－** A Case that a `{supersedes:case N}` of the window names needs no `tasks` block.

```then
update:
- slug: rule-prespec
  replace:
  - old: has no task line of its own (case 327)
    new: has no task line of its own (case 327), and an Estimate whose `update` carries `rename` is read under the slug of its `rename`, the slug its reading names (case 432)
  change: 'the Render: the read line of a renamed Estimate names its new slug (case 432)'
- slug: estimate-prespec-requires-a-task-line
  set:
    status: pending
  change: the Criterion replaced whole — a renamed Estimate is read under the slug of its rename (case 432)
- slug: insight-workflow-case-schema-silent-on-what-the-scripts-accept
  set:
    status: actioned
    addressed_by: decision-case-432
  change: 'actioned: a form the scripts refuse is found by judge on SubagentStop before the Case is shown (case 419.3); a renamed Estimate is read under its new slug (case 432); the limits are not copied into the Case schema'
```

```tasks
- [x] update `rule-prespec` — the Render names the new slug of a renamed Estimate
- [x] update `estimate-prespec-requires-a-task-line` — its Criterion replaced whole by the `when` and `then` of this Case
- [x] update `insight-workflow-case-schema-silent-on-what-the-scripts-accept` — actioned
- [x] `guppi/prespec.py`: `estimates_to_read` gives the slug under `rename` for an Estimate `update` that carries one; the docstring says so
- [x] `tests/test_prespec.py`: a renamed Estimate set `pending` with a read line of its new slug is no finding; with a read line of its old slug alone, the finding names the new slug
- [x] one-off migration: in `raw/2026-09-25/1228/spec.md`, the read lines of `estimate-case-protocol-checks-its-frame` and `estimate-frame-check-finds-a-contradiction` become `` - [ ] read `estimate-case-protocol-shows-the-built-case` `` and `` - [ ] read `estimate-case-build-writes-the-case` ``
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [ ] read `estimate-prespec-requires-a-task-line`
```
