<!-- approved 03:51:57 · session 031f3ab3 -->

# Spec — session 0137, 2026-09-29

## Case 497 — A lesson's pointer to its fix must name a decision line of the session

> **context:**
> A lesson line written after the Case that fixed its cause carries `{addressed_by:case N}`. The librarian's run (`materialize`) links the lesson to the decision only when a decision line of Case N stands before the lesson line in the session's ledger. Nothing checks the pointer when the line is written. A Case with sub-cases has no decision line of its own: its lines are N.1, N.2 and so on, and each has its own Decision page. So a pointer to the parent number never resolves. In session 2229, ledger line 52 pointed at `case 487`, whose lines are 487.1 to 487.4. The lesson `lesson-prespec-judged-a-pair-by-its-anchor-alone` went out without its link, and only the next morning's brief showed it. This is the pattern of `insight-ledger-line-written-unchecked`: a line written verbatim and read back only by `materialize`.
> The person chose three things. The ledger hook refuses such a line at once, the way it already refuses a lesson slug without its prefix (case 460.5). The rule text of `rule-case-protocol` says which number to name. The lesson of line 52 stays as it is. Nothing reads the mark once synthesis has run, the lesson joined no Insight, and the handoff of 2229 names the fix. Its `incomplete: [addressed_by]` stays in the yaml of 2229. Case 442 deferred a neighbour on `rule-ledger-write`: a lesson line with no mark at all, although a Case of the session closed its cause. The person chose to leave it deferred. This Case catches a mark that names the wrong Case, not a missing mark.
> The vault's answer: the only `create` is an Estimate with a `ref`, so no vault query ran. The ledgers under `vault/raw` hold exactly one `{addressed_by:...}` mark and no `{addresses:...}` mark. The first is the line of 2229. The frame:
> - The hook and `materialize` judge the mark by one function in `guppi/materialize.py`, by `CLAUDE.md` ("one judgment, one implementation"). The function reads the ledger lines in order, and one test runs both callers on the same lines. The order matters. `materialize` links a lesson only to a decision line that stands before it, so the hook asks the same thing. A decision line later in the same `LEDGER` block does not count.
> - `materialize` keeps its behaviour: `rule-materialize` and the Criterion of `estimate-materialize-carries-addresses` ("no decision line of Case N earlier in the unit") stay true and are not touched.
> - `estimate-ledger-write-lifts` lists each refusal of the hook in its `－` lines. It gains one line, so its Criterion is replaced whole (497.2).
> - `estimate-ledger-write-refuses-a-lesson-without-its-prefix` says that a lesson line with the prefix "is written as before". This Case would make that false for a line with a bad mark. So its Criterion is replaced whole (497.3), and that one sentence is not carried: it becomes "is not refused for its prefix", and the mark is judged apart. The prefix is judged first. A line refused for its prefix is not judged for its mark, so it gets one stderr line, not two.
> - `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` speaks only of `estimate[...]` lines and stands.
> - `estimate-case-protocol-ledger-line-form` promises the form of the mark. It gains the sub-case rule, and its Criterion is replaced whole (497.4). `estimate-case-protocol-loaded` is not touched by a change of a Render (case 378.5).
> - The other `Stop` hooks, `guppi ratified`, `guppi casecheck` and `guppi context`, do not read lesson lines.
> - The prefix refusal refuses a line at every `Stop`, since its slug never changes. The mark refusal depends on the ledger. A line refused from an earlier text is judged again at every `Stop` until it stands in the ledger. It is written at the first `Stop` where a decision line of its Case stands before it. The hook speaks only for the line in the reply just finished. A line whose Case never gets a decision line stays unwritten at the end of the session, and Retro sees it.
> - `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` stays true, and the Case does not update it. The hook runs from the working tree at once, and the text of 497.4 lands at the render. But that Criterion asks for the old form only where the reader refuses, in between, what the old text asks for, and the refused line is lost.
>   - Neither holds here. The old text says to name "that Case", and a mark with no decision line of its Case did not link under the old text either. A line that names a Case without sub-cases passes, as before.
>   - A refused line is not lost. In the reply just finished, the hook exits 2 and the agent writes the line again. From an earlier text, the line is judged again until its decision line stands.
> - Not done: the hook does not judge the `{addresses:<lesson slug>}` mark of a decision line, it does not catch a missing mark (case 442, still deferred), and the lesson of line 52 is not repaired.
> - The new Estimate and the three set `pending` are read in a later session (case 428.1).
>
> This Case is built again after pre-spec found these faults: the hook ignored the order of lines, a later `Stop` was said to skip a line it in fact writes, a line with both faults got two stderr lines, the Estimate of old forms was not named, and defer 442 was not named. The answer check noted that some `then` lines of 497.2, 497.3 and 497.4 share words with 497.1 and with each other. This is expected. All four speak of the same hook and the same mark. 497.1 is modelled on the prefix refusal that 497.3 keeps. 497.2 and 497.4 keep the other lines of their old Criteria word for word.

> **problem:**
> A lesson line can point to a Case that has no decision line before it in the session, such as the parent of sub-cases. The mark then never links, and nobody sees it until the librarian's run of the next day.

### Case 497.1 — The ledger hook refuses a lesson mark with no decision line before it

> **given:**
> `rule-ledger-write` — the rule of the ledger hook; its `How it works` gains the refusal
> **＋** `guppi/ledger.py` — the hook: the refusal, its order after the prefix check, and its stderr line
> **＋** `guppi/materialize.py` — the one ordered judgment of a mark, which the hook imports and `materialize` uses
> **＋** `tests/test_ledger.py` — the cases of the refusal, and the test that runs both callers on the same lines
> **＋** `estimate-ledger-write-refuses-a-lesson-without-its-prefix` — the prefix refusal, judged first
> **＋** `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — the rule of old forms for a reader that refuses
> **＋** `estimate-ledger-write-refuses-a-mark-with-no-decision-line` — the new promise

> **when:**
> The `Stop` hook `uv run guppi ledger` finds a fresh `lesson[<slug>]` line in a `LEDGER` block of the session, and the line carries `{addressed_by:case N}`.

> **then:**
> When no decision line of Case N stands before the lesson line — in the session's ledger, or earlier among the lines of the same `Stop` — the line is not written.
> **＋** The other lines of the `Stop` are written as before.
> **＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: lesson[<slug>] not written — {addressed_by:case <N>} names no decision line before it in this session; its sub-cases have case <N.1>, case <N.2>: write the line again after the decision line of the Case that closed the cause, naming that Case." The part on the sub-cases stands only when a decision line of a sub-case of N stands in the session.
> **＋** A refused line from an earlier text of the transcript is judged again at every `Stop` until it stands in the ledger. It is written at the first `Stop` where a decision line of Case N stands in the ledger before it. The hook says nothing about it.
> **＋** The hook and `guppi materialize` judge the mark by one function of `guppi/materialize.py`, over the ledger lines in their order, and give the same answer for the same lines.
> **－** A line that `estimate-ledger-write-refuses-a-lesson-without-its-prefix` refuses is not judged for its mark, and gets that refusal's stderr line alone.
> **－** A lesson line whose mark has a decision line of Case N before it is written as before, and so is a lesson line with no mark. A line already in the ledger of any session is not judged again.
> **－** Without a `hi`, and with `stop_hook_active`, the hook acts as before and judges no line.

```then
create:
- slug: estimate-ledger-write-refuses-a-mark-with-no-decision-line
  type: estimate
  ref: rule-ledger-write
  kind: QA
  purpose: Whether the ledger hook refuses a lesson line whose addressed_by mark has no decision line of its Case before it in the session, judges it again until that line stands, and says why only for the reply just finished
  method: uv run pytest tests/test_ledger.py — piped payloads and a session ledger in a temp vault
  tags:
  - session
  - hooks
  - harness
  - ledger
update:
- slug: rule-ledger-write
  replace:
  - old: skips an older one without a word, and writes the other lines as before.
    new: 'skips an older one without a word, and writes the other lines as before. A mark names a decision line before it (case 497.1): a `lesson[...]` line whose `{addressed_by:case N}` has no decision line of Case N before it — in the session''s ledger, or earlier among the lines of the same `Stop` — is not written, since `materialize` links a lesson only to a decision line of that Case earlier in the unit, and a Case with sub-cases has no line of its own (session 2229, ledger line 52). One function of `guppi/materialize.py` reads the ledger lines in order and gives each lesson line whose mark has no such decision line; the hook and `materialize` both call it. A line refused for its prefix is not judged for its mark. The hook exits 2 with one stderr line per refused line only when the line stands in the reply just finished, and that line names the decision lines of the sub-cases of N that stand in the session, when there are any. A refused line from an earlier text is judged again at every `Stop`, without a word, until a decision line of its Case stands before it, and is written then.'
  change: the ledger hook refuses a lesson line whose {addressed_by:case N} has no decision line of Case N before it (case 497.1)
```

```tasks
- [x] update `rule-ledger-write`
- [x] create `estimate-ledger-write-refuses-a-mark-with-no-decision-line`
- [x] `guppi/materialize.py` — one function over ledger lines in order that gives each lesson line whose `{addressed_by:case N}` has no decision line of Case N before it. `lift_line` judges the lesson mark by it. The docstring names the hook as its second caller
- [x] `guppi/ledger.py` — `refused_marks` beside `refused_lessons`, which calls that function on the session's ledger followed by the fresh lines and skips a line `refused_lessons` already refused. `run` leaves the lines out and prints the stderr line for the finished reply. The module docstring names the refusal and the order of the two checks
- [x] `tests/test_ledger.py` — `-k mark`: a mark to a parent with sub-case lines is refused aloud, with the sub-case ids. A mark to a Case with no line is refused aloud, with no sub-case part. A lesson above its decision line in the same block is refused. A refused line in an earlier text is not written while its Case has no line, and is written without a word at the `Stop` after the decision line lands. A mark with its decision line before it, in the ledger or in the same block, is written. A lesson with no mark is written. A line with no prefix and a bad mark gets the prefix line alone. A line already in a ledger is not judged. One test runs the hook and `materialize` on the same ledger lines and asserts that the lines they refuse and leave `incomplete: [addressed_by]` are the same
- [x] read `estimate-ledger-write-refuses-a-mark-with-no-decision-line`
```

### Case 497.2 — The promise of the ledger hook names the new refusal

> **given:**
> `estimate-ledger-write-lifts` — the promise of the hook; its Criterion replaced whole
> **＋** `guppi/ledger.py` — the hook it reads
> **＋** `guppi/gate.py` — the gate it names
> **＋** `raw/<hi date>/<hi HHMM>/ledger.md` — the session's ledger the hook writes
> **＋** `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` — a refusal it names
> **＋** `estimate-ledger-write-refuses-a-lesson-without-its-prefix` — a refusal it names
> **＋** `estimate-ledger-write-refuses-a-mark-with-no-decision-line` — the refusal it gains

> **when:**
> The `Stop` hook `uv run guppi ledger` fires at the end of a turn of the main agent, with `transcript_path` and `last_assistant_message` in its payload; or `guppi gate` refuses a `Skill` call for an item of the Spec without a ledger line.

> **then:**
> In a session with a `hi` recorded, every line `- decision[`, `- estimate[`, `- lesson[` inside a `LEDGER` block of any text of the main agent in the transcript, the reply just finished included, lands in `raw/<hi date>/<hi HHMM>/ledger.md` with the time of writing, once — a body already in the ledger of any session is not written again.
> **＋** A block in a text followed by a tool call in the same turn reaches the ledger at the next `Stop` of the session, with the time of that `Stop`; the reply that ends in the text lands it now.
> **＋** The gate's advice to the agent reads "The text before a tool call waits for the next Stop: end this reply in text with the LEDGER block, then call /<skill> in the next reply."
> **－** An `estimate[...]` line the hook refuses by `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` does not land.
> **－** A `lesson[...]` line the hook refuses by `estimate-ledger-write-refuses-a-lesson-without-its-prefix` does not land.
> **－** A `lesson[...]` line the hook refuses by `estimate-ledger-write-refuses-a-mark-with-no-decision-line` does not land while that refusal holds.
> **－** Without a `hi`: exit 2 with the reason, the ledger untouched; with `stop_hook_active`: exit 0, nothing written.
> **－** The last turn of a session that ends in a tool call has no `Stop` after it; its lines are a finding of Retro, not of the hook.

```then
update:
- slug: estimate-ledger-write-lifts
  set:
    status: pending
  change: the Criterion replaced whole — a lesson line refused for its mark does not land while the refusal holds (case 497.2)
```

```tasks
- [x] update `estimate-ledger-write-lifts`
- [x] read `estimate-ledger-write-lifts` — `uv run pytest tests/test_ledger.py tests/test_gate.py`, then by hand on the ledger of a later session
```

### Case 497.3 — The prefix check no longer promises that every prefixed lesson is written

> **given:**
> `estimate-ledger-write-refuses-a-lesson-without-its-prefix` — the promise of the prefix check; its Criterion replaced whole
> **＋** `guppi/ledger.py` — the hook it reads
> **＋** `guppi/materialize.py` — `category_of`, the table of prefixes
> **＋** `estimate-ledger-write-refuses-a-mark-with-no-decision-line` — the check that judges the mark of a prefixed line

> **when:**
> The `Stop` hook `uv run guppi ledger` finds a fresh `lesson[<slug>]` line in a `LEDGER` block of the session. `category_of` of `guppi/materialize.py` does not put its slug under the lessons folder: the slug does not start with the lesson prefix.

> **then:**
> The line is not written.
> **＋** The other lines of the `Stop` are written as before.
> **＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: lesson[<slug>] not written — a lesson slug starts with lesson-, then the area, then the cause: write the line again with the prefix."
> **＋** At every later `Stop`, a refused line from an earlier text of the transcript is skipped without a word.
> **－** A lesson line whose slug starts with the lesson prefix is not refused for its prefix; its mark is judged by `estimate-ledger-write-refuses-a-mark-with-no-decision-line`. A line already in the ledger of any session is not judged again.
> **－** `estimate[...]` and `decision[...]` lines are not judged by their prefix.
> **－** Without a `hi`, and with `stop_hook_active`, the hook acts as before and judges no line.

```then
update:
- slug: estimate-ledger-write-refuses-a-lesson-without-its-prefix
  set:
    status: pending
  change: the Criterion replaced whole — a prefixed lesson line is not refused for its prefix, its mark judged apart (case 497.3)
```

```tasks
- [x] update `estimate-ledger-write-refuses-a-lesson-without-its-prefix`
- [x] read `estimate-ledger-write-refuses-a-lesson-without-its-prefix` — `uv run pytest tests/test_ledger.py`
```

### Case 497.4 — The schema says which Case a lesson's mark names

> **given:**
> `rule-case-protocol` — the ledger paragraph of its Render
> **＋** `vault/wiki/case-schema.md` — the file rendered from it, which `/hi` loads
> **＋** `estimate-case-protocol-ledger-line-form` — the promise on the form of the marks; its Criterion replaced whole

> **when:**
> The agent writes the ledger lines of a session: the decision lines in the reply that acknowledges a ratification, a lesson line the moment the lesson exists.

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
- slug: rule-case-protocol
  replace:
  - old: carries `{addressed_by:case N}` instead, naming that Case — one of the two marks per pair
    new: carries `{addressed_by:case N}` instead, naming that Case — for a Case with sub-cases the sub-case whose decision line closes the cause, since the parent has no decision line and the ledger hook refuses a mark with no decision line of its Case before it (case 497.4) — one of the two marks per pair
  change: a lesson's addressed_by mark names the sub-case whose decision line closes the cause (case 497.4)
- slug: estimate-case-protocol-ledger-line-form
  set:
    status: pending
  change: the Criterion replaced whole — for a Case with sub-cases the mark names the sub-case (case 497.4)
```

```tasks
- [x] update `rule-case-protocol`
- [x] update `estimate-case-protocol-ledger-line-form`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-protocol-ledger-line-form` — by hand, the reading its `method` names, in a later session
```

## Case 498 — Slice 3g: the Estimates of rendering and settings recut to one Criterion

> **context:**
> Each Estimate page holds one promise, its Criterion. A Criterion should hold only `When:`, the trigger and the input it acts on, and `Then:`, what must hold after. The page carries its promise as a `purpose` field and its way of checking as a `method` field. Twelve older Estimates still have the layout from before this model. They have no `purpose` and no `method` field. They have a `## Context` and a `## Method` section. Most of them also stack one `### case N` block under the Criterion for each Case that changed them. `make lint` counts these twelve as `unmigrated`. Here is where it goes wrong: `estimate-render-harness-reproduces` holds a unit-and-live paragraph and four blocks. One of those blocks, 139.1, is a probe that ran once in session O, to see whether an agent file written mid-session can be called. A new reading cannot tell which lines are the promise and which record an act that happened once.
> The person decided in the first round on this item. The twelve go in three Cases by area, all in this session: this Case takes rendering and settings, case 499 takes the end of a session, and case 500 takes the librarian's and the vault's tools. Each page gets one Criterion, and no page is split. The live half of each reading stays. The last Case replaces the Slice note with a note on removing the old-layout checks, so Slice 3g stays open until a later session removes them after lint counts zero (case 202). A Criterion that records a one-time act gets a Criterion of the repeating behaviour (case 485). This group holds five pages: `estimate-render-harness-reproduces`, `estimate-render-sync-reports`, `estimate-settings`, `estimate-default-mode` and `estimate-governed-files-hook-refuses`. None of them has `purpose` or `method`, so each `update` sets both from the page's own Criterion and `## Method`. Setting `method` also drops `## Context` and `## Method` (case 211). Each Criterion is replaced whole and goes back to `pending`, and its reading waits for a later session (case 428.1). Their rules `rule-settings`, `rule-default-mode` and `rule-governed-files-hook` go from `built` to `draft` until the reading. `rule-render-harness` is `draft` already. None of the five lost its Criterion to a tool fault like case 211.3. Their History shows only Criteria that cases 18.1, 36.2, 59.7, 66, 71.1, 85.1, 85.2, 85.4, 88.1, 89.3, 89.4, 91 and 139.1 wrote on purpose, so nothing is restored.
> What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording. The content of the old lines is carried, except for the lines named here. "Unit, against a temp vault" and "Live:" name ways of reading, and they move into `method`. In 498.1, block 139.1 goes out as a one-time probe. Two more lines go out: the `－` line of 88.1 on how to read the clause, and the second half of the `－` line of 85.1, which follows from the first. The unit paragraph, 85.1, 88.1 and 89.4 become one list. The clause of 89.4 that `--sync` exits 0 on a JSON error also goes out of 498.1, because its `when` covers only the plain run and `--check`, and 498.2 promises the exit 0 of the sync on any render error. In 498.3 the line "Its Estimate reads the rendered file" becomes the lines it names. The page fields of `rule-settings` shrink to what the render does with them, and "that order is the order of the keys in the file" is kept. In 498.4, "the page" is named as `rule-default-mode` and its Purpose. In 498.5 the unit paragraph and block 91 join. The live probe on the file of `/hi` moves into `method`.
> The check of the answer also notes that the error line of 498.2 shares words with the line of 498.1 on a child without `enforcement: render`. This is expected. 498.1 promises that the plain render exits 1 and writes nothing on that fault. 498.2 promises that the sync at session start swallows any render error with exit 0, because a `SessionStart` hook cannot block. They are two promises, read by two different runs.
> The frame. Each kept line was read against `guppi/render.py`, `guppi/guard.py`, `tests/test_render.py`, `tests/test_guard.py`, the `Makefile` and the live `.claude/settings.json`, and none is contradicted. One sentence of the docstring of `guppi/render.py` calls "When Claude Code reads an agent file" "the reading of case 139.1 on `estimate-render-harness-reproduces`". After the recut the page no longer holds that reading, and the next reading overwrites its Result. So 498.1 has one task that writes the finding into the docstring in place of the pointer. That task changes no behaviour and no test. `estimate-render-harness-ticks-the-spec` promises the tick, not the render, and is left alone. `rule-settings` is a MOC, so its `method` names `make test-harness`. The render also fills the language placeholders, but no Estimate of this group promises that, and this Case adds no promise. The History line of 498.6 does not say the Slice note stands, because case 500.6 replaces that note in the same librarian's run. No behaviour changes, so no Render and no hook changes, and no reader keeps an old form. The Case creates no page, so no vault query was run. Not done: cases 499 and 500, the note of Slice 3g, and the removal of the old-layout checks.

> **problem:**
> The five Estimates of rendering and settings still have the layout from before case 193. They have no `purpose` or `method` field, they carry `## Context` and `## Method`, and four of them stack `### case N` blocks, one of them a probe that ran once. Lint counts them as `unmigrated`, and a reading of them cannot tell the promise from the record of past acts.

### Case 498.1 — The renderer writes each governed file from its Rule pages

> **given:**
> `estimate-render-harness-reproduces` — the promise, its Criterion replaced whole
> **＋** `rule-render-harness` — the rule it promises for
> **＋** `guppi/render.py` — `run`, `render_full`, `render_partial`, `check_json` and `differing`; its docstring points at the probe
> **＋** `vault/wiki/rules/` — the Rule pages with `enforcement: render`
> **＋** `tests/test_render.py` — the tests the reading runs

> **when:**
> `uv run guppi render` runs without a flag or with `--check`, and reads the Rule pages under `vault/wiki/rules/` that carry `enforcement: render`.

> **then:**
> The Render of a `full` page becomes the whole file its `governs` names, without the page's outer markers. Each `<!-- child -->` line is replaced by that child's text in the order of `children`, and the child's markers are kept.
> **＋** A file that cannot hold a comment, a `.json` target, takes each child's text without the child's markers.
> **＋** A `partial` page whose file no `full` page owns is spliced between its markers in the existing file, and the markers stay. A target without those markers gives exit 1, and nothing is written.
> **＋** A child without `enforcement: render` contributes nothing and needs no marker. A marker line for it in the parent's text gives exit 1, and nothing is written.
> **＋** Every `.json` target is parsed before anything is written. One that does not parse stops the whole write, stderr names the file and the page that owns it, and the run exits 1.
> **＋** `--check` names each file that differs, exits 1 and writes nothing. When every file is identical, it exits 0.
> **＋** Against the live vault, after `uv run guppi render`, `git diff --stat` names only the governed files whose Rule page changed since the last render. The diff of each is the text of that page's Render, and `uv run guppi render --check` then exits 0.
> **－** No file type other than `.json` is parsed.

```then
update:
- slug: estimate-render-harness-reproduces
  set:
    status: pending
    purpose: guppi render writes each governed harness file from its Rule pages, parses every json target before it writes, and --check names a file that differs
    method: 'pytest tests/test_render.py, plus by hand on the live vault after a later librarian''s render: git diff --stat, then guppi render --check'
  change: the Criterion replaced whole — the unit paragraph and the blocks 85.1, 88.1 and 89.4 into one When and Then, the one-time probe of 139.1 out; purpose and method set, Context and Method out (case 498.1)
```

```tasks
- [x] update `estimate-render-harness-reproduces`
- [x] `guppi/render.py` — the docstring sentence that points at "the reading of case 139.1 on `estimate-render-harness-reproduces`" states the finding instead: Claude Code reads the agent files at session start, so an agent the librarian renders can be called from the next session (case 139.1)
- [x] read `estimate-render-harness-reproduces` — `pytest tests/test_render.py`, then by hand on the live vault after a later librarian's render
```

### Case 498.2 — The sync at session start shows and writes back a parted file

> **given:**
> `estimate-render-sync-reports` — the promise, its Criterion replaced whole
> **＋** `rule-render-harness` — the rule it promises for
> **＋** `guppi/render.py` — `sync` and `run` with `--sync`
> **＋** `.claude/settings.json` — the `SessionStart` hook that runs the sync
> **＋** `tests/test_render.py` — the tests the reading runs

> **when:**
> A session starts, and the `SessionStart` hook of `.claude/settings.json` runs `uv run guppi render --sync` over the governed files.

> **then:**
> For each governed file that differs from its render, stdout holds a unified diff, the file as it is and then the rendered text, and the rendered text is written. The diff reaches the agent's first turn.
> **＋** An identical file is neither printed nor written.
> **＋** On a render error, one line goes to stderr, nothing is written, and the exit is 0.
> **＋** At a session start after a librarian's run that rendered, the hook prints nothing and writes nothing, and `uv run guppi render --check` then exits 0.
> **＋** At a session start after a governed file and its page have parted, the diff of that file is in the first turn, and the page's text is written back.

```then
update:
- slug: estimate-render-sync-reports
  set:
    status: pending
    purpose: At session start guppi render --sync shows the diff of each governed file that parted from its page and writes the page's text back, and is silent when every file matches
    method: pytest tests/test_render.py, plus by hand at the first turn of a later session
  change: the Criterion replaced whole — the unit and live paragraph as When and Then; purpose and method set, Context and Method out (case 498.2)
```

```tasks
- [x] update `estimate-render-sync-reports`
- [x] read `estimate-render-sync-reports` — `pytest tests/test_render.py`, then by hand at the first turn of a later session
```

### Case 498.3 — The settings file rendered whole from its MOC

> **given:**
> `estimate-settings` — the promise, its Criterion replaced whole
> **＋** `rule-settings` — the MOC it promises for, the `full` owner of the file
> **＋** `rule-default-mode` — its first child
> **＋** `rule-permissions` — its second child
> **＋** `rule-hook-registry` — its third child
> **＋** `.claude/settings.json` — the file rendered
> **＋** `vault/raw/<date>/event_log.md` — the day's event log with the `session-start` line
> **＋** `Makefile` — the target `test-harness`

> **when:**
> `uv run guppi render` writes `.claude/settings.json` from `rule-settings` and its children, and the next session starts from that file.

> **then:**
> The file is the Render of `rule-settings`, and the text of each child replaces its `<!-- child -->` line in the order of `children`: `rule-default-mode`, `rule-permissions`, `rule-hook-registry`. That order is the order of the keys in the file.
> **＋** The file parses as JSON, and `uv run guppi render --check` exits 0.
> **＋** The next session start writes its `session-start` line into `vault/raw/<date>/event_log.md`, from the hooks of the rendered file.
> **－** `rule-settings` holds no rule of its own about what a hook or a permission may be.

```then
update:
- slug: estimate-settings
  set:
    status: pending
    purpose: The settings file is rendered whole from rule-settings and its three children, parses as JSON and loads at session start
    method: 'make test-harness, then by hand at a later session start: json.load on the rendered file, guppi render --check, and the session-start line in the day''s event log'
  change: the Criterion replaced whole — the block 85.2 as When and Then, the line on its own reading into the lines it names; purpose and method set, Context and Method out (case 498.3)
```

```tasks
- [x] update `estimate-settings`
- [x] read `estimate-settings` — `make test-harness`, then by hand at a later session start
```

### Case 498.4 — A session opens in Plan Mode

> **given:**
> `estimate-default-mode` — the promise, its Criterion replaced whole
> **＋** `rule-default-mode` — the rule it promises for, a child of `rule-settings`
> **＋** `rule-settings` — the MOC that renders the file
> **＋** `.claude/settings.json` — the file that carries the mode
> **＋** `tests/test_render.py` — the tests the reading runs

> **when:**
> A session starts with `.claude/settings.json` as `guppi render` wrote it from `rule-settings`.

> **then:**
> `.claude/settings.json` carries `"defaultMode": "plan"` under `permissions`, the text of `rule-default-mode`, and the session opens in Plan Mode.
> **＋** The Purpose of `rule-default-mode` says why: nothing is written before a Case is ratified.
> **－** The Render of `rule-default-mode` holds no other permission field.

```then
update:
- slug: estimate-default-mode
  set:
    status: pending
    purpose: 'A session opens in Plan Mode: the settings file carries defaultMode plan from rule-default-mode'
    method: 'pytest tests/test_render.py, plus by hand at a later session start: the session opens in Plan Mode and nothing outside the plan file is edited without a sign-off'
  change: the Criterion replaced whole — the block 85.4 as When and Then, the page named; purpose and method set, Context and Method out (case 498.4)
```

```tasks
- [x] update `estimate-default-mode`
- [x] read `estimate-default-mode` — `pytest tests/test_render.py`, then by hand at a later session start
```

### Case 498.5 — The guard refuses a hand edit of a governed file

> **given:**
> `estimate-governed-files-hook-refuses` — the promise, its Criterion replaced whole
> **＋** `rule-governed-files-hook` — the rule it promises for
> **＋** `guppi/guard.py` — the hook `guppi guard`
> **＋** `.claude/settings.json` — the `PreToolUse` matcher of `Edit`, `Write` and `MultiEdit`
> **＋** `vault/wiki/rules/` — the live Rule pages whose `governs` the hook reads
> **＋** `vault/raw/<date>/event_log.md` — the day's event log
> **＋** `tests/test_guard.py` — the tests the reading runs

> **when:**
> Claude Code runs `uv run guppi guard` on `PreToolUse` of a tool call, and the hook reads the `governs` field of the live Rule pages under `vault/wiki/rules/`.

> **then:**
> An `Edit`, `Write` or `MultiEdit` on a governed path exits 2. Stderr names the file and the slug of the rule that governs it, and the client blocks the call.
> **＋** Before it exits 2, the hook appends one line to `vault/raw/<date>/event_log.md` with the time, the session, the tool, the path and the slug of the rule.
> **＋** Another tool or an ungoverned path exits 0.
> **＋** A payload the hook cannot read exits 0 with one line on stderr.
> **－** A call the hook lets through writes no event line: `PostToolUse` logs it.
> **－** A log the hook cannot write does not change the refusal: the exit stays 2, and the reason still goes to stderr.

```then
update:
- slug: estimate-governed-files-hook-refuses
  set:
    status: pending
    purpose: guppi guard refuses a hand edit of a governed harness file, names its rule and logs the refusal
    method: 'pytest tests/test_guard.py, plus by hand in a later session: one Edit of a governed file refused, the rule named, the line in the day''s event log'
  change: the Criterion replaced whole — the unit paragraph and the block 91 into one When and Then, the live probe into method; purpose and method set, Context and Method out (case 498.5)
```

```tasks
- [x] update `estimate-governed-files-hook-refuses`
- [ ] read `estimate-governed-files-hook-refuses` — `pytest tests/test_guard.py`, then by hand on one refused `Edit` in a later session
```

### Case 498.6 — The sprint page records the group of rendering and settings

> **given:**
> `entity-sprint-migration` — the sprint page whose History records the recut
> **＋** `rule-render-harness` — a rule whose Estimates this Case recuts
> **＋** `rule-settings` — a rule whose Estimate this Case recuts
> **＋** `rule-default-mode` — a rule whose Estimate this Case recuts
> **＋** `rule-governed-files-hook` — a rule whose Estimate this Case recuts

> **when:**
> The librarian's run applies the `update` of `entity-sprint-migration`.

> **then:**
> The History of `entity-sprint-migration` says that the Estimates of rendering and settings are recut.

```then
update:
- slug: entity-sprint-migration
  change: 'Slice 3g: the Estimates of rule-render-harness, rule-settings, rule-default-mode and rule-governed-files-hook recut to one Criterion (case 498)'
```

```tasks
- [x] update `entity-sprint-migration`
```

## Case 499 — Slice 3g: the Estimates of the end of a session recut to one Criterion, and the handoff names its file to the librarian

> **context:**
> Each Estimate page holds one promise, its Criterion. A Criterion should hold only `When:`, the trigger and the input it acts on, and `Then:`, what must hold after. The page carries its promise as a `purpose` field and its way of checking as a `method` field. The older Estimates lack both fields. They carry `## Context` and `## Method`, and stack `Given:` or `### case N` blocks, and `make lint` counts them as `unmigrated`. This group holds the two Estimates of the end of a session: `estimate-end-of-work-order`, which still opens with a `Given:` about the Spec hook, the cascade and the methods of other Estimates, and `estimate-handoff-dispatches`, which has a head paragraph and block 73.7. The two parts of the second page disagree. The head says the librarian is dispatched "with the date". Block 73.7 says it is dispatched with the path of `handoff.md`. The skill `/handoff` sends only `Materialize <date>.`, but the librarian's frame takes as its first input "the `handoff.md` your dispatch names". The History of `rule-handoff` records that case 73.7 meant the path, "the librarian is dispatched with its path". The Render never got the path, so the librarian has had to find the file on its own.
> The person decided in the first round on this item. The twelve old pages go in three Cases by area: case 498 took rendering and settings, this Case takes the end of a session, and case 500 takes the librarian's and the vault's tools and replaces the Slice note. Each page gets one Criterion, no page is split, and each live half of a reading stays. In the second round the person chose to keep the path in the promise and to change the skill to match. So 499.2 changes the Render of `rule-handoff` to send `Materialize <date> from <path of handoff.md>.` and recuts `estimate-handoff-dispatches` to that behaviour. Neither page has `purpose` or `method`, so each `update` sets both, and setting `method` drops `## Context` and `## Method` (case 211). Each Criterion is replaced whole and goes back to `pending`, and its reading waits for a later session (case 428.1). `rule-end-of-work` goes from `built` to `draft` until the reading. `rule-handoff` is `draft` already. Neither page lost its Criterion to a tool fault like case 211.3. Their History shows only Criteria that cases 38, 38.3, 73.7, 190.2 and 196.2 wrote on purpose, so nothing is restored.
> What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording. The content of the old lines is carried, except for the lines named here. In 499.1 the `Given:` goes out whole. Its lines describe the Spec hook, the cascade of case 190.2, the methods of three Estimates and the order of the entries of 190.x, and all of these are history. The line on `rule-carry-over` as a child is already in `Then:`. "`make test-end-of-work` is green" moves into `method`. The `－` line "The order of the three steps of the ordinary way does not change" goes out as a bound of an edit, because the order itself stands in the line before it. In 499.2 "with the date" gives way to the path the person chose. "The first turn's context holds git status --porcelain" is kept as the skill's own check.
> The check also notes that 499.2 shares words with 499.1 on `/handoff` on a dirty tree and on the commit after the handoff. This is expected. 499.1 promises the order of the ordinary end of a session, read across its folder, the event log and `git log`: the gate of `guppi/gate.py` refuses a dirty tree, and no other commit stands between the handoff and the librarian's. 499.2 promises what the skill does when it is called: it stops on a dirty tree, writes the note, dispatches with the path, and commits nothing itself. Both old pages held these lines, as cases 38 and 38.3 signed them. `estimate-session-phases-in-order` (case 493.4) promises that the marks of all five phases rise in time, a reading across the whole session. 499.1 promises the gate and the two ends inside End of Work, so it is not touched.
> The frame. The kept lines were read against the Render of `rule-handoff`, the Purpose and `children` of `rule-end-of-work`, `guppi/gate.py`, the `Makefile` and the frame of the librarian, `.claude/agents/librarian-guppi.md`. With the new Render, the librarian's "the `handoff.md` your dispatch names" becomes true. No test and no script reads the dispatch line. The new skill text lands at the render of the librarian's run. So the `/handoff` of this session still sends the date alone, and its librarian finds the folder as it has so far. Nothing refuses in between and nothing is lost, so no old form is kept. `estimate-handoff-holds-each-fact-once` promises the content of the three sections, not the dispatch, and is left alone. The pair of 499.2 hits the one sentence of the Render that names the dispatch. The History line of 499.3 does not say the Slice note stands, because case 500.6 replaces that note in the same librarian's run. The Case creates no page, so no vault query was run. Not done: case 500 and the note of Slice 3g, and the removal of the old-layout checks.

> **problem:**
> The two Estimates of the end of a session still have the layout from before case 193, and lint counts them as `unmigrated`. One of them promises two different dispatch texts, and the skill it reads sends neither the path it promised nor the file the librarian expects.

### Case 499.1 — A session ends one of two ways, the ordinary way in order

> **given:**
> `estimate-end-of-work-order` — the promise, its Criterion replaced whole
> **＋** `rule-end-of-work` — the MOC it promises for, its `children` and the two ends in its Purpose
> **＋** `rule-carry-over` — the second end, `/carry` straight after Plan Mode
> **＋** `rule-handoff` — the child that `rule-carry-over` follows
> **＋** `guppi/gate.py` — the gate that refuses `/handoff` on a dirty tree
> **＋** `vault/raw/<date>/<hi HHMM>/` — the session's folder, with `handoff.md`
> **＋** `vault/raw/<date>/event_log.md` — the day's event log
> **＋** `Makefile` — the target `test-end-of-work`

> **when:**
> A session ends, and someone reads its folder `vault/raw/<date>/<hi HHMM>/`, the day's event log `vault/raw/<date>/event_log.md` and `git log`.

> **then:**
> The session ended one of two ways: Work Mode, Retro, the commit, the handoff and the librarian; or `/carry` straight after Plan Mode.
> **＋** In the ordinary way the order holds: `/handoff` is refused while the tree is dirty; `handoff.md` exists before the librarian is dispatched; no other commit stands between the handoff and the librarian's commit.
> **＋** On leaving Plan Mode the agent asks the person which of the two ends, and starts nothing until it is answered.
> **＋** `rule-carry-over` is a child of `rule-end-of-work`, after `rule-handoff`.

```then
update:
- slug: estimate-end-of-work-order
  set:
    status: pending
    purpose: 'A session ends one of two ways, and the ordinary way keeps its order: the commit before /handoff, handoff.md before the librarian, no commit between the handoff and the librarian''s'
    method: 'make test-end-of-work, plus by hand at the close of a later session: its folder, the day''s event log and git log'
  change: the Criterion replaced whole — When and Then only, Given and the bounds line out, the green run of make test-end-of-work into method; purpose and method set, Context and Method out (case 499.1)
```

```tasks
- [x] update `estimate-end-of-work-order`
- [ ] read `estimate-end-of-work-order` — `make test-end-of-work`, then by hand at the close of a later session
```

### Case 499.2 — `/handoff` writes the note and dispatches the librarian with its path

> **given:**
> `rule-handoff` — the rule whose Render is the skill `/handoff`; its dispatch line changes
> **＋** `estimate-handoff-dispatches` — the promise, its Criterion replaced whole
> **＋** `.claude/skills/handoff/SKILL.md` — the skill rendered from `rule-handoff`
> **＋** `.claude/agents/librarian-guppi.md` — the librarian, whose first input is the `handoff.md` its dispatch names
> **＋** `guppi/gate.py` — the gate of `/handoff` and its `handoff` mark
> **＋** `vault/raw/<date>/<hi HHMM>/` — the session's folder, where `handoff.md` is written
> **＋** `vault/raw/<date>/event_log.md` — the day's event log

> **when:**
> The person invokes `/handoff` after the Retro, the gate of `guppi/gate.py` reads the tree, and the agent runs the skill `.claude/skills/handoff/SKILL.md` as rendered from `rule-handoff`.

> **then:**
> The skill's context holds `git status --porcelain`. On a dirty tree the skill stops and says "commit first", and nothing is written.
> **＋** On a clean tree the day's event log `vault/raw/<date>/event_log.md` holds the `handoff` mark of the call.
> **＋** The agent writes `handoff.md` into the session's folder `vault/raw/<date>/<hi HHMM>/`: one document with no `---` and the three sections `## Notes from memory`, `## Direct instructions to the librarian` and `## What actually got done`, with no Read call on the artifacts.
> **＋** Then the agent dispatches `librarian-guppi` with one line, `Materialize <date> from <path of handoff.md>.`, the path being that of the file just written, and shows the librarian's report to the person unchanged.
> **－** No commit follows the handoff except the librarian's own.

```then
update:
- slug: rule-handoff
  replace:
  - old: 'Then dispatch the `librarian-guppi` agent with one line: `Materialize <date>.`'
    new: 'Then dispatch the `librarian-guppi` agent with one line: `Materialize <date> from vault/raw/<date>/<hi HHMM>/handoff.md.`, the path of the file you just wrote.'
  change: the dispatch names handoff.md by its path, as case 73.7 meant and the librarian's frame reads (case 499.2)
- slug: estimate-handoff-dispatches
  set:
    status: pending
    purpose: /handoff stops on a dirty tree, writes handoff.md from memory into the session's folder and dispatches the librarian with its path, with no commit after
    method: 'by hand at the /handoff of a later session: the event log, handoff.md, the dispatch line and git log'
  change: the Criterion replaced whole — the head and the block 73.7 into one When and Then, the dispatch by the path; purpose and method set, Context and Method out (case 499.2)
```

```tasks
- [x] update `rule-handoff`
- [x] update `estimate-handoff-dispatches`
- [x] `uv run guppi render`: `.claude/skills/handoff/SKILL.md`
- [ ] read `estimate-handoff-dispatches` — by hand at the `/handoff` of a later session
```

### Case 499.3 — The sprint page records the group of the end of a session

> **given:**
> `entity-sprint-migration` — the sprint page whose History records the recut
> **＋** `rule-end-of-work` — a rule whose Estimate this Case recuts
> **＋** `rule-handoff` — a rule whose Estimate this Case recuts

> **when:**
> The librarian's run applies the `update` of `entity-sprint-migration`.

> **then:**
> The History of `entity-sprint-migration` says that the Estimates of the end of a session are recut.

```then
update:
- slug: entity-sprint-migration
  change: 'Slice 3g: the Estimates of rule-end-of-work and rule-handoff recut to one Criterion, the dispatch of the handoff by its path (case 499)'
```

```tasks
- [x] update `entity-sprint-migration`
```

## Case 500 — Slice 3g: the Estimates of the librarian's and the vault's tools recut to one Criterion, and the note on the old shape gives way to its removal

> **context:**
> Each Estimate page holds one promise, its Criterion. A Criterion should hold only `When:`, the trigger and the input it acts on, and `Then:`, what must hold after. The page carries its promise as a `purpose` field and its way of checking as a `method` field. The older Estimates lack both fields. They carry `## Context` and `## Method` and stack `### case N` blocks, and `make lint` counts them as `unmigrated`. This group holds the last five: `estimate-ask-finds`, `estimate-index-check-merges`, `estimate-cleanup-moves`, `estimate-raw-archive` and `estimate-tests-clock-pinned`. Here is where it goes wrong: `estimate-cleanup-moves` holds a head paragraph and three blocks. One block moves the old archive folders once. One tells `cleanup.py` to stop writing index files that no longer exist. One gives the page "a `### case 102.2` block, `pending`". A new reading cannot tell those acts from the promise.
> The person decided in the first round on this item. The twelve old pages went in three Cases by area: case 498 took rendering and settings, case 499 the end of a session, and this Case takes the rest. Each page gets one Criterion, no page is split, and each live half of a reading stays. This last Case replaces the note of Slice 3g with a note on removing the checks of the old shape once lint counts zero, so Slice 3g stays open (case 202). This Case closes the Frontier line C1. A Criterion that records a one-time act gets a Criterion of the repeating behaviour (case 485). None of the five has `purpose` or `method`, so each `update` sets both, and setting `method` drops `## Context` and `## Method` (case 211). Each Criterion is replaced whole and goes back to `pending`, and its reading waits for a later session (case 428.1). All five rules go from `built` to `draft` until the reading. None of the five lost its Criterion to a tool fault like case 211.3. Their History shows only Criteria that cases 23.1, 33, 35.1, 100.1, 102.2, 105.1, 145.1, 147.2, 147.3, 147.6, 166.4 and 174 wrote on purpose, so nothing is restored.
> What each new Criterion keeps and drops. The check of the answer notes every old line as not carried, because each new line is a whole statement and not the old wording. The content of the old lines is carried, except for the lines named here. Each line that gives a page a block or sets it `pending` goes out as bookkeeping. In 500.1 two lines go out as a one-time Research question: "whether `@` expands in an agent file" and "the tokens of one dispatch". Block 147.2 quoted the new Render. It becomes the behaviour that Render gives, the Grep of the rules first, and the line "No read of a `*-index.md`" goes out, because the files no longer exist. The name of the fifth answer line, tags/slug, stands in plain text, because a code span with a `/` reads as a path that `given` must name. In 500.2 "The name of the rule does not change" goes out as a bound of an edit, and the head's "comparisons made per category" is now the Grep and its count that the Render names. The Render also leaves Estimates out of the check, and that is kept. In 500.3 the migration of block 102.2 and the removal of the index writer of 147.6 go out as one-time acts, and so does "no index file is written". The History and `log.md` lines are worded as `history` in `guppi/cleanup.py` writes them: the page gets its line, and `log.md` gets the same text with the page's category and slug in front. In 500.4 the `－` line "a date-level unit dated the day of the run is not looked at" is carried by the first `＋` line, and "that gap is `rule-materialize`'s" goes out as a pointer. In 500.5 the old line names `guppi.ledger.run`, but `tests/test_conftest.py` calls `guppi.event.run`. So the line promises a `run()` without `now`, as the test reads it. "`make test` is green on the tree of this session" moves into `method`. The `Makefile` half of the last `－` line goes out as a bound of an edit, and the `test-*` targets stay.
> The check also notes that 500.4 shares words with 500.1 on the day's event log, and with 500.3 on the exit codes and the rerun. This is expected. In 500.1 each dispatch of `ask-guppi` is written into the event log. In 500.4 `guppi archive` leaves the event log where it is. 500.3 and 500.4 are two scripts with the same contract for a failed move and a rerun, each promised for its own script and read by its own test file, as cases 33 and 100.1 signed them.
> The frame. The kept lines were read against `.claude/agents/ask-guppi.md`, the Render of `rule-index-check`, `guppi/cleanup.py`, `guppi/archive.py`, `tests/conftest.py`, `tests/test_conftest.py` and the frame of the librarian, and none is contradicted but the one line of 500.5 named above. Stdout lines, History lines and headers that hold a `/` stand in plain quotation marks or in words. `estimate-sprint-migration-lint-clean` promises that `unmigrated` is at zero at the close. This Case makes the count zero after the librarian's run and does not change that promise, so it is not touched. `estimate-lint-counts-the-unmigrated` stays true at zero, since it promises no line then. No behaviour changes, so no code, test, Render or hook changes, and no reader keeps an old form. The Case creates no page, so no vault query was run. Not done: the removal of the checks of the old shape, which the new note holds for a later session, and with it the wording of the Criterion of `estimate-sprint-migration-lint-clean` on the counter.

> **problem:**
> The last five Estimates of the old layout still have no `purpose` or `method`, still carry `## Context` and `## Method`, and stack blocks that record migrations, removed index files and one-time questions next to their promise. Lint counts them as `unmigrated`. The note of Slice 3g asks for exactly this recut, and nothing but a Case removes it.

### Case 500.1 — `ask-guppi` finds a page by meaning and answers in five lines

> **given:**
> `estimate-ask-finds` — the promise, its Criterion replaced whole
> **＋** `rule-ask` — the rule it promises for
> **＋** `.claude/agents/ask-guppi.md` — the agent rendered from `rule-ask`
> **＋** `vault/wiki/rules/` — the rule pages the agent greps first
> **＋** `vault/archive/` — the archive, searched by slug alone
> **＋** `vault/raw/<date>/event_log.md` — the day's event log

> **when:**
> The main agent dispatches `ask-guppi` through the `Agent` tool with a question, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> The answer is exactly five lines: `exists`, `near`, `missing`, `rules` and the tags/slug line, each present, "none" when empty. No index line or page text reaches the caller beyond them.
> **＋** The agent starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs one Grep per other category the question touches.
> **＋** A question about an existing page names its slug under `exists`, whether it is asked in English or in Russian.
> **＋** A proposal that crosses a rule or a lesson, such as a `SessionStart` hook meant to block, names it on the `rules` line.
> **＋** A named slug gets on the tags/slug line `free`, `live` with its category, or `archived at <path> by [[decision-case-N]]`, found by a Glob over `vault/archive/`, N from the `origin` of the archived page.
> **＋** The agent opens an archived page only when the question names its slug and asks what it said or why it was withdrawn.
> **＋** Each dispatch stands in `vault/raw/<date>/event_log.md`.
> **－** The archive is not searched by meaning: the `exists` and `near` lines name live pages only.

```then
update:
- slug: estimate-ask-finds
  set:
    status: pending
    purpose: ask-guppi finds a page by meaning in either language, names the rule a proposal crosses and the state of a named slug, and answers in five lines
    method: 'by hand in a later session: three dispatches of ask-guppi, one existing page asked in English and in Russian, one proposal that crosses a known rule, each read against the event log'
  change: the Criterion replaced whole — the head and the blocks 105.1 and 147.2 into one When and Then, the one-time questions and the index files out; purpose and method set, Context and Method out (case 500.1)
```

```tasks
- [x] update `estimate-ask-finds`
- [ ] read `estimate-ask-finds` — by hand on three dispatches in a later session
```

### Case 500.2 — The librarian's index check merges a duplicate within its category

> **given:**
> `estimate-index-check-merges` — the promise, its Criterion replaced whole
> **＋** `rule-index-check` — the rule it promises for, spliced into the librarian's frame
> **＋** `.claude/agents/librarian-guppi.md` — the librarian's frame that holds the check
> **＋** `vault/wiki/` — the category folders the Grep reads

> **when:**
> The librarian's run does the index check of `.claude/agents/librarian-guppi.md`, as rendered from `rule-index-check`, over the `create` entries of each `materialize.yaml`.

> **then:**
> For each `create` other than an Estimate, the librarian runs the Grep of its category under `vault/wiki/`: `^(purpose|deferred_by):`, `root_cause` for lessons, `pattern` for insights. It compares the entry's `purpose`, or `root_cause` for a lesson, with every line the Grep returns.
> **＋** The report names each Grep and the number of lines compared.
> **＋** A `create` whose thing already has a page becomes an `update` of that slug with `change: "merged by librarian: <why>"` and `librarian: merged`, every other field of the entry as it was.
> **＋** A page that is close but not the same keeps the entry and adds `near: <slug>`.
> **＋** Every page opened is named in the report, with the index line that did not settle same or near.
> **－** No comparison crosses categories.

```then
update:
- slug: estimate-index-check-merges
  set:
    status: pending
    purpose: The librarian's index check turns a create whose thing already has a page into an update of that page and marks a near one, comparing within one category by the Grep of its index lines
    method: by hand on the report of a later librarian's run, against its materialize.yaml
  change: the Criterion replaced whole — the head and the block 147.3 into one When and Then, the bound on the rule's name out; purpose and method set, Context and Method out (case 500.2)
```

```tasks
- [x] update `estimate-index-check-merges`
- [ ] read `estimate-index-check-merges` — by hand on the report of a later librarian's run
```

### Case 500.3 — `cleanup` moves an archived page out and a restored one back

> **given:**
> `estimate-cleanup-moves` — the promise, its Criterion replaced whole
> **＋** `rule-cleanup` — the rule it promises for
> **＋** `guppi/cleanup.py` — the script `guppi cleanup`, its `history` and its `unlink`
> **＋** `vault/wiki/` — the live pages and `log.md`
> **＋** `vault/archive/<sprint>/<date>/<HHMM>/<category>/` — the archive folder of a moved page
> **＋** `vault/raw/<date>/` — the date folder whose latest session names the run
> **＋** `tests/test_cleanup.py` — the tests the reading runs

> **when:**
> `uv run guppi cleanup` runs over the live pages of `vault/wiki/` and the pages under the archive.

> **then:**
> A live page with `status: archived` moves under the same file name to `vault/archive/<sprint>/<date>/<HHMM>/<category>/`. The date is the day of the run, and the session is the latest session folder of `vault/raw/<date>/`, else the latest of the nearest date back. With no session folder at all, the page goes into the category folder under the date, with no session level.
> **＋** The moved page gets the History line "- <date> archived · cleanup", and a page moved back gets "- <date> restored · cleanup". Each History line that cleanup writes also goes to `log.md` with the page's category and slug in front, such as "- <date> <category>/<slug> archived · cleanup".
> **＋** Its slug leaves the `children` of live pages and the `estimates` of entities and rules, the field only, and that page gets the History line "- <date> child <slug> archived · cleanup" or "- <date> estimate <slug> archived · cleanup". No section is rebuilt, and an Insight's `children` keep the slug.
> **＋** Wikilinks in page bodies stay, and a page with any other status stays.
> **＋** A page under the archive, at any depth, whose status is no longer `archived` moves back to its category folder under `vault/wiki/`.
> **＋** A live page whose `parent` or `target` is archived is reported on stderr and left.
> **＋** A rerun moves nothing and exits 0. A file that cannot move, or a name already taken in the archive, is a line on stderr and exit 1, and the other pages still move.
> **＋** Live, a run with nothing to move exits 0 and leaves `git diff` empty.

```then
update:
- slug: estimate-cleanup-moves
  set:
    status: pending
    purpose: guppi cleanup moves an archived page into the archive of the session of the run and a restored one back, and unlinks its slug from the live lists without rebuilding a section
    method: pytest tests/test_cleanup.py, plus by hand on the cleanup of a later librarian's run
  change: the Criterion replaced whole — the head and the blocks 102.2, 147.6 and 166.4 into one When and Then, the one-time migration and the index files out, the History and log lines as the script writes them; purpose and method set, Context and Method out (case 500.3)
```

```tasks
- [x] update `estimate-cleanup-moves`
- [x] read `estimate-cleanup-moves` — `pytest tests/test_cleanup.py`, then by hand on the cleanup of a later librarian's run
```

### Case 500.4 — `archive` moves a done unit of raw whole into the archive

> **given:**
> `estimate-raw-archive` — the promise, its Criterion replaced whole
> **＋** `rule-raw-archive` — the rule it promises for
> **＋** `guppi/archive.py` — the script `guppi archive`, with `materialize.parse_line` for the record lines
> **＋** `vault/raw/<date>/` — a date folder, its date-level `ledger.md` and its `event_log.md`
> **＋** `vault/raw/<date>/<HHMM>/` — a session folder
> **＋** `vault/archive/<sprint>/<date>/raw/` — the archive of a date-level unit
> **＋** `vault/archive/<sprint>/<date>/<HHMM>/raw/` — the archive of a session
> **＋** `tests/test_archive.py` — the tests the reading runs

> **when:**
> `uv run guppi archive` runs, as a step of the librarian's run or by hand, over the units under `vault/raw/<date>/`.

> **then:**
> A unit is a session folder `vault/raw/<date>/<HHMM>/` that holds a `ledger.md`, or a date-level `ledger.md` at the root of `vault/raw/<date>/` with its yaml. A unit is done when its yaml exists, every entry under `entries` carries `applied` or `superseded_by`, and the number of every line of its `ledger.md` that `materialize.parse_line` reads as a record stands in the `line` or `folded` of an entry or under `unparsed`.
> **＋** Only units dated before the day of the run are looked at. The session of the run is never looked at, even when it is dated before the run day: it is the latest session folder of the run day, else of the nearest date back.
> **＋** A done session moves whole to `vault/archive/<sprint>/<date>/<HHMM>/raw/`. A done date-level ledger moves with its yaml and everything else at the date root to `vault/archive/<sprint>/<date>/raw/`. With it goes every session folder of the date that has no ledger of its own, each to `vault/archive/<sprint>/<date>/<HHMM>/raw/`. No file is cut.
> **＋** `event_log.md` stays in `vault/raw/<date>/`.
> **＋** Stdout holds one line per unit: "archive: raw/<date>/<HHMM> → archive/<sprint>/<date>/<HHMM>/raw", "archive: raw/<date> → archive/<sprint>/<date>/raw", or "archive: raw/<date>[/<HHMM>] kept: <reason>". The reason is `no yaml`, `N entries not applied` or `N ledger lines outside the yaml`.
> **＋** The exit is 0. A name already taken in the archive, or a move that fails, is a line on stderr and exit 1, and the other units still move. A rerun moves nothing and exits 0.
> **－** `origin`, History, `log.md` and the yaml are not rewritten.
> **－** A folder without `ledger.md` is not a unit.
> **－** An entry that a supersedes from another unit did not mark keeps its unit in `vault/raw/<date>/`.

```then
update:
- slug: estimate-raw-archive
  set:
    status: pending
    purpose: guppi archive moves a done unit of raw whole into the archive of its date, keeps an undone one with its reason, and never touches the session of the run
    method: 'pytest tests/test_archive.py, plus by hand on the archive step of a later librarian''s run: its stdout, the raw folder and the origin findings of make lint before and after'
  change: the Criterion replaced whole — the block 100.1 as When and Then, the pointer to rule-materialize out; purpose and method set, Context and Method out (case 500.4)
```

```tasks
- [x] update `estimate-raw-archive`
- [ ] read `estimate-raw-archive` — `pytest tests/test_archive.py`, then by hand on the archive step of a later librarian's run
```

### Case 500.5 — The clock of the tests is pinned

> **given:**
> `estimate-tests-clock-pinned` — the promise, its Criterion replaced whole
> **＋** `rule-tests-clock-pinned` — the rule it promises for
> **＋** `tests/conftest.py` — the autouse fixture
> **＋** `tests/test_conftest.py` — the test of the fixture
> **＋** `tests/` — the suite the fixture covers
> **＋** `guppi/` — the modules whose clock is pinned
> **＋** `Makefile` — the targets `test` and `test-*`

> **when:**
> `pytest` collects `tests/`, and a test calls the `run()` of a module of `guppi/` without `now`, or the code reads the clock outside `run()`.

> **then:**
> Before every test, an autouse fixture in `tests/conftest.py` sets into every module of `guppi/` that carries a `datetime` attribute a subclass whose `now(tz=None)` returns `2001-01-01 00:00:00 UTC`, and `astimezone` gives the same second. A test that leaves the code on the real clock sees the year 2001 and fails on the day it is written.
> **＋** The list of modules comes from a walk over `guppi/`, never from a hand list: a new module with a clock is covered with no change to the fixture.
> **＋** `tests/test_conftest.py` shows it: a `run()` without `now` writes a time dated 2001, and `datetime.strptime`, `fromisoformat` and the constructor of the subclass work as before.
> **＋** The targets `test` and `test-*` of the `Makefile` run under the same fixture.
> **－** A test that passes `now` does not notice the fixture: `run()` reads no clock.

```then
update:
- slug: estimate-tests-clock-pinned
  set:
    status: pending
    purpose: 'A test that leaves the code on the real clock fails on the day it is written: every guppi module''s clock is pinned to 2001 by one autouse fixture'
    method: pytest tests/test_conftest.py, plus make test green under the fixture
  change: the Criterion replaced whole — the block 145.1 as When and Then, the run the test calls named as it reads, the green run of make test into method; purpose and method set, Context and Method out (case 500.5)
```

```tasks
- [x] update `estimate-tests-clock-pinned`
- [x] read `estimate-tests-clock-pinned` — `pytest tests/test_conftest.py`, then `make test` after the Work Mode of a later session
```

### Case 500.6 — The note of Slice 3g gives way to the removal of the old-layout checks

> **given:**
> `entity-sprint-migration` — the sprint page; its Slice 3g holds the note on the old shape
> **＋** `guppi/sprint.py` — renders a note as `- [ ] <text>` and never ticks it
> **＋** `vault/wiki/sprint.md` — the render of the sprint page
> **＋** `/hi` — builds the Frontier from `vault/wiki/sprint.md`
> **＋** `rule-ask` — a rule whose Estimate this Case recuts
> **＋** `rule-index-check` — a rule whose Estimate this Case recuts
> **＋** `rule-cleanup` — a rule whose Estimate this Case recuts
> **＋** `rule-raw-archive` — a rule whose Estimate this Case recuts
> **＋** `rule-tests-clock-pinned` — a rule whose Estimate this Case recuts

> **when:**
> `uv run guppi sprint` renders `vault/wiki/sprint.md` from `entity-sprint-migration` at the librarian's run, and the next `/hi` builds the Frontier from it.

> **then:**
> Slice 3g holds one note, on removing the checks of the old shape once `make lint` counts no `unmigrated` page, and the Frontier holds it as a `C` line. The note on the old shape recut is gone from the page and from the render.
> **＋** The History of `entity-sprint-migration` says that the Estimates of the librarian's and the vault's tools are recut and that the recut of the old shape is done.
> **－** No line is added to `## Closed`: Slice 3g stays open.
> **－** The checks of the old shape do not change in this Case.

```then
update:
- slug: entity-sprint-migration
  replace:
  - old: '- the old shape recut: every Estimate whose Criterion still holds `### case N` blocks brought to one Criterion, until lint counts no `unmigrated` page'
    new: '- the old shape removed: once `make lint` counts no `unmigrated` page, the checks of the shape before case 193 leave the scripts, `rule-estimates-schema` and `estimate-lint-counts-the-unmigrated` (case 202)'
  change: 'Slice 3g: the Estimates of rule-ask, rule-index-check, rule-cleanup, rule-raw-archive and rule-tests-clock-pinned recut to one Criterion; the recut of the old shape done (cases 498-500), its note replaced by the note on removing the checks of the old shape'
```

```tasks
- [x] update `entity-sprint-migration`
- [x] `uv run guppi sprint`
```

## Case 501 — Each question in a round takes one fixed shape, set in the grill-me template

> **context:**
> When a choice is still open, `case-guppi` answers with a round of numbered questions. It builds the round on the template of the skill `grill-me`, which it loads through its `skills` field. The person's own `/grill-me` interviews use the same template. The template gives a question a title, a free body "including multiple choices", and a recommended answer. The instructions of `case-guppi` add one loose sentence: each question body tells what each option changes, "as a before and after". No script reads a round. In the rounds of session 2000, Case 482 Q2 and Q4 gave no before, and Case 483 Q3 and Q4 gave only "After:". `estimate-case-build-writes-a-plain-round` was read `failed` (L25 of `archive/migration/2026-09-28/2000/raw/ledger.md`). The rounds of this session came in mixed shapes. One of them put a list of costs under an option, a second label in all but name. Case 495 put the item off.
> The person chose these things. The shape goes into the template of `grill-me`, so that `/grill-me` and `case-guppi` share one template. A question states today once, on a `**Now:**` line. Every question takes the shape, and a question on something new says "nothing exists yet". Each option starts on its own line as a bold list item, with one nested `**After:**` item under it and nothing else. There is no list of costs, no second item and no other label. A cost is a plain sentence inside the `After:` text or in the reasoning after the arrow. At pre-spec the person added two things. The shape is worded once, in the template, and the instructions of `case-guppi` only point to it. The language of the labels does not matter: in the chat the labels stand translated and count as the same labels, because the shape is what is read.
> The vault's answer: every item is an `update` with a `ref`, so no vault query ran. `rule-case-build` carries `deferred_by: [[decision-case-495]]`, so its decision line in 501.2 carries `{supersedes:case 495}`, and the page leaves the backlog. What `case-guppi` found in the frame:
> - The question line keeps its colon, `❓ **Qn** - **<title>**:`, because `rule-case-protocol` describes how the main agent shows a round by that line. The body starts on the next line.
> - The shape is worded once as text, in the template of 501.1, and signed once as a promise, in `estimate-skill-grill-me-asks-in-rounds`, whose `when` already covers both `/grill-me` and a round of `case-guppi`. The new text of `rule-case-build` and `estimate-case-build-writes-a-plain-round` only point to it.
> - `estimate-case-protocol-shows-the-built-case` promises that the main agent translates a round line by line, each question "its title, body and recommended answer translated in place, nothing merged, dropped or added". It stays true and is not touched. A label translated in place keeps its line and its list item, so the shape reaches the chat whole. The `－` line of 501.1 says that a translated label counts as the same label.
> - The criterion of `estimate-case-build-writes-the-case` still holds true: a round is still "in the form of" the template.
> - `rule-skill-wait-what` keeps its own sentence, "as a before and after", for a re-explained round. Pointing it to the template is item C3 and is not done here.
> - Not done: the hook of `rule-case-check` still reads no round, so a question off the shape is found only at a reading.
> - The two Estimates set `pending` are read in a later session (case 428.1).
>
> The answer check noted that three lines of the old Criteria are not carried. Each is dropped on purpose:
> - "On the person's `/grill-me`, each question is numbered, with a title, a body and a recommended answer" in `estimate-skill-grill-me-asks-in-rounds` becomes the two shape lines. The shape covers `/grill-me` and `case-guppi` alike.
> - "The form of a round of `case-guppi` is not read here" in the same Estimate is no longer true: the shape of that form now lives in the template. It becomes a `－` line that leaves only the Context paragraph and the case numbers to the Estimates of `rule-case-build`.
> - "Each question body says what each option changes, as a before and after." in `estimate-case-build-writes-a-plain-round` moves to `estimate-skill-grill-me-asks-in-rounds`. There it is worded as the shape, so the same promise is not signed twice in two wordings.

> **problem:**
> A round of questions often does not say, for each option, what holds today and what holds after it, and its options run together in solid text. The template gives no shape, and the one sentence in the instructions of `case-guppi` is loose, so the before part gets dropped or merged and extra labels creep in.

### Case 501.1 — The grill-me template gives every question one shape

> **given:**
> `rule-skill-grill-me` — the rule of the skill; its Render gains the shape of a question
> **＋** `.claude/skills/grill-me/SKILL.md` — the file rendered from it
> **＋** `estimate-skill-grill-me-asks-in-rounds` — the promise of the skill; its Criterion replaced whole
> **＋** `.claude/agents/case-guppi.md` — the agent that loads the skill by `skills: [grill-me]`
> **＋** `rule-case-protocol` — the showing of a round by its question line, translated in place, which the shape keeps
> **＋** `estimate-case-protocol-shows-the-built-case` — the promise of how the main agent translates and shows a round
> **＋** `estimate-case-build-writes-the-case` — the promise of the Context paragraph of a round of `case-guppi`
> **＋** `estimate-case-build-writes-a-plain-round` — the promise of the plain words of a round of `case-guppi`

> **when:**
> The person types `/grill-me` on `UserPromptSubmit`, or `case-guppi` answers with a round of questions, with `.claude/skills/grill-me/SKILL.md` loaded by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, after `uv run guppi render` wrote `.claude/skills/grill-me/SKILL.md` from `rule-skill-grill-me`.

> **then:**
> `uv run guppi render --check` exits 0: `.claude/skills/grill-me/SKILL.md` equals the Render of `rule-skill-grill-me`.
> **＋** The agent asks in rounds: each round holds every question whose prerequisites are settled, and the agent waits for the answers before the next round.
> **＋** Each question opens with its numbered `❓ **Qn** - **<title>**:` line and closes with its `➡️` line, the recommended answer. Its body starts on the next line with one `**Now:**` line that says once what holds today, or that nothing exists yet.
> **＋** Each option starts on its own line as a list item with its name in bold. Under it stands one nested `**After:**` item that says what holds with that option.
> **＋** A fact the agent can look up it finds itself, or by a sub-agent when it can dispatch one; the person is asked only for decisions.
> **＋** The agent acts on the grill only after the shared understanding is confirmed, by the person's word unless the instructions that started the grill name another confirmation.
> **－** An option carries nothing under it but its `**After:**` item: no list of costs, no second item and no other label. A cost is a plain sentence inside the `**After:**` text or in the `➡️` line.
> **－** In the chat the labels may stand translated, as the main agent shows a round of `case-guppi` by `estimate-case-protocol-shows-the-built-case`. A translated label counts as the same label: the shape is what is read, not the language of the labels.
> **－** The Context paragraph of a round of `case-guppi` and the place of its case numbers are not read here. They are the promises of `estimate-case-build-writes-the-case` and `estimate-case-build-writes-a-plain-round`.
> **－** No sentence of `.claude/skills/grill-me/SKILL.md` requires the agent to dispatch a sub-agent.

```then
update:
- slug: rule-skill-grill-me
  replace:
  - old: |-
      Each question should be formatted like so:

          ❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

          ➡️ <your recommended answer>
    new: |-
      Each question should be formatted like so:

          ❓ **Q1** - **<question title>**:

          **Now:** <what holds today, said once for the question; "nothing exists yet" when nothing does>

          - **(a) <option name>**
            - **After:** <what holds with this option>
          - **(b) <option name>**
            - **After:** <what holds with this option>

          ➡️ <your recommended answer, and why>

      The body of a question starts on the line after its title. The `**Now:**` line says once what holds today. Each option starts on its own line as a list item with its name in bold, and under it stands one nested `**After:**` item: what holds with this option. An option has nothing else under it: no list of costs, no second item, no other label. A cost, when it matters, is a plain sentence inside the `**After:**` text or in the reasoning after `➡️`. Every question takes this shape, one on a new idea with nothing behind it too. In the language of the chat the labels may stand translated; the shape stays.
  change: 'every question of a round takes one shape: a Now line once, each option on its own line with one After item under it and nothing else (case 501.1)'
- slug: estimate-skill-grill-me-asks-in-rounds
  set:
    status: pending
  change: the Criterion replaced whole — every question of /grill-me and of case-guppi takes the Now and After shape, an option with nothing else under it, a translated label the same label (case 501.1)
```

```tasks
- [x] update `rule-skill-grill-me`
- [x] update `estimate-skill-grill-me-asks-in-rounds`
- [x] `uv run guppi render`: `.claude/skills/grill-me/SKILL.md`
- [x] read `estimate-skill-grill-me-asks-in-rounds` — `uv run guppi render --check`; by hand, one round read in the chat in a later session
```

### Case 501.2 — case-guppi points to the question shape of the template

> **given:**
> `rule-case-build` — the rule of `case-guppi`; its Render points to the question shape of the template
> **＋** `.claude/agents/case-guppi.md` — the file rendered from it
> **＋** `estimate-case-build-writes-a-plain-round` — the promise of a plain round; its Criterion replaced whole
> **＋** `.claude/skills/grill-me/SKILL.md` — the template that holds the shape
> **＋** `estimate-skill-grill-me-asks-in-rounds` — the promise that reads the shape

> **when:**
> `case-guppi` answers with a round of questions, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`.

> **then:**
> The `**Context:**` of a first round gives the mechanism in plain words, with one concrete example of where it goes wrong.
> **＋** The instructions of `case-guppi` point each question to the question shape of `.claude/skills/grill-me/SKILL.md` and word no shape of their own.
> **＋** Case numbers, the history of a slug and facts of the frame stand in the round only in the `➡️` line of a question, as the source of its recommendation.
> **＋** A term the person has not met in the chat is explained in a few words where it first stands, or a common word replaces it.
> **－** The shape of a question is read by `estimate-skill-grill-me-asks-in-rounds`, not here.
> **－** The `context` of a Case keeps its case numbers and frame facts: the sentence is about a round only.

```then
update:
- slug: rule-case-build
  replace:
  - old: each question body says what each option changes, as a before and after;
    new: each question takes the question shape of the grill-me template;
  change: each question of a round of case-guppi takes the question shape of the grill-me template, not restated (case 501.2)
- slug: estimate-case-build-writes-a-plain-round
  set:
    status: pending
  change: the Criterion replaced whole — the instructions point to the question shape of the grill-me template, read by estimate-skill-grill-me-asks-in-rounds; this promise keeps the Context, the case numbers and the terms (case 501.2)
```

```tasks
- [x] update `rule-case-build`
- [x] update `estimate-case-build-writes-a-plain-round`
- [x] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [x] read `estimate-case-build-writes-a-plain-round` — by hand, one round of case-guppi read in the chat against the Criterion, in a later session
```

## Case 502 — /wait-what explains with a real example and points its options to the grill-me shape

> **context:**
> `/wait-what` writes the agent's last text again in plain words when the person did not follow it: a round of questions, the short text on a Case, or a reply. Today it asks for "one concrete example of where it goes wrong". It also asks the `case-guppi` of a Case for a fact the main agent does not hold. It does not say that the example must be real, or that the main agent may find the line itself. In session 2000 the re-explanation of round 2 Q1 on Case 485 showed a made-up line, "guppi cleanup prints one line per moved file", marked as made up. `estimate-skill-wait-what-re-pitches` was read `failed` (L26 of `archive/migration/2026-09-28/2000/raw/ledger.md`), and `lesson-wait-what-invents-an-example` records the cause. In this session the main agent explained Case 497 with a real ledger line, L52 of `raw/2026-09-28/2229/ledger.md`, which it found itself, and that met the aim. The skill also keeps its own "as a before and after" for options, while the question template of `grill-me` now has a fixed shape (case 501.1).
> The person chose these things. The example is a real line, quoted with its path. The main agent finds the line itself. When no real example is found, the re-explanation says so in one sentence and gives the mechanism without one. A quoted line keeps its case numbers as written. Options take the shape of the `grill-me` template. One Criterion covers all of this.
> This is the Case built again after pre-spec, with three fixes the person agreed to:
> - The shape of a question is worded once, in the `grill-me` template (501.1). The Render and the Criterion here only point to the question shape of `.claude/skills/grill-me/SKILL.md` and say where it applies. They do not repeat the `**Now:**` and `**After:**` lines. `estimate-skill-grill-me-asks-in-rounds` reads the shape.
> - The main agent translates the labels of the shape into the chat language, and a translated label counts as the label of the template.
> - `rule-case-build` has `case-guppi` answer a fact in plain words under a `**Fact:**` line, not as a quoted line. So, for a line the main agent cannot find, `case-guppi` names the file and the line, and the main agent reads the file and quotes the line itself. `rule-case-build` stays as it is. "Do not guess it" stays for every other fact of a Case.
>
> The vault's answer: both items are an `update` with a `ref`, so no vault query ran. `rule-skill-wait-what` carries `deferred_by: [[decision-case-496]]`, so its decision line carries `{supersedes:case 496}`, and the page leaves the backlog (case 429).
> What `case-guppi` found in the frame:
> - `rule-case-protocol` says the main agent asks `case-guppi` "only for a fact of the Case it does not hold". That stays true: a line the main agent read is a fact it holds. `estimate-case-protocol-shows-the-built-case` promises a `SendMessage` "only to ask for a fact of the Case", answered under a `**Fact:**` line. That also stays true, since the file and the line are such a fact. Neither page is changed.
> - `estimate-agent-writing-followed` speaks only of a request for a plain explanation being no complaint. It is not touched.
> - The skill names `.claude/skills/grill-me/SKILL.md` because it does not load that template. The shape reaches that file at the render of 501.1, so Work Mode renders `grill-me` before this skill. No code reads the skill, so no old form is kept.
> - The lesson comes from session 2000, so its fix carries no `{addresses:...}` mark (case 284.2).
> - The Estimate set `pending` is read in a later session (case 428.1).
> - Not done: no script reads a re-explanation, so an invented example is found only at a reading.
>
> Four lines of the old Criterion are not carried word for word. Each one is reworded on purpose:
> - The line on the language and the short sentences is carried into the first `＋` line, which also takes the background.
> - "shows how the thing works on one real case" becomes the real-example line. "names the effect of every choice" becomes the line that points to the question shape.
> - The line on case numbers now says "its own sentences". A `－` line lets a quoted line keep its case numbers.
> - The line on facts from `case-guppi` becomes a `－` line for every other fact. The example line says how a line is found and quoted.

> **problem:**
> The re-explanation of `/wait-what` may show an invented example when no real one is at hand. Its options have no fixed layout, while the rounds it explains now have one.

> **given:**
> `rule-skill-wait-what` — the rule of the skill; its Render changes
> **＋** `.claude/skills/wait-what/SKILL.md` — the file rendered from it
> **＋** `estimate-skill-wait-what-re-pitches` — the promise of the skill; its Criterion replaced whole
> **＋** `.claude/skills/grill-me/SKILL.md` — the template that holds the question shape
> **＋** `estimate-skill-grill-me-asks-in-rounds` — the promise that reads the shape
> **＋** `rule-case-build` — `case-guppi` answers a fact under a `**Fact:**` line
> **＋** `rule-guppi-config` — sets `chat_lang`, the language of the skill
> **＋** `vault/wiki/glossary.md` — the terms the skill uses

> **when:**
> The person types `/wait-what` on `UserPromptSubmit`, or the main agent calls the skill on `PreToolUse Skill` when the person asks in words for a plain explanation of its last text, after `uv run guppi render` wrote `.claude/skills/wait-what/SKILL.md` from `rule-skill-wait-what`.

> **then:**
> `uv run guppi render --check` exits 0: `.claude/skills/wait-what/SKILL.md` equals the Render of `rule-skill-wait-what`, with the name of the language that the `## Render` of `rule-guppi-config` sets for `chat_lang` in place of its placeholder.
> **＋** The main agent writes its last text again — a round, the short text on a Case or a reply — in the language of `chat_lang`. It uses short active sentences with one idea each and opens with a little background.
> **＋** It shows the mechanism on one real example: a line of a page, a file, a ledger or the Case, which the main agent reads itself and quotes as it stands, with its path. For a line it cannot find, it asks the `case-guppi` of the Case by `SendMessage` for the file and the line, then reads the file and quotes the line.
> **＋** When it finds no real example, it says so in one sentence and gives the mechanism without one.
> **＋** Each question of a round it explains, and the options of a short text on a Case or of a reply, take the question shape of `.claude/skills/grill-me/SKILL.md`.
> **＋** Its own sentences hold no case number and no history of a slug. They use the terms of `vault/wiki/glossary.md`, and explain a term in a few words where it first stands.
> **＋** It ends with the open question asked again.
> **－** No example is made up, whether it is marked as made up or not.
> **－** A quoted line keeps its case numbers as written.
> **－** A label of the shape translated into the language of `chat_lang` counts as the label of the template.
> **－** The question shape itself is read by `estimate-skill-grill-me-asks-in-rounds`, not here.
> **－** No other fact of a Case that the main agent does not hold is guessed: it comes from the `case-guppi` of that Case.
> **－** No option and no recommendation of the last text changes.
> **－** The skill starts no Case and writes no ledger line.

```then
update:
- slug: rule-skill-wait-what
  replace:
  - old: |-
      Give a little context first. Then say the mechanism in plain words, with one concrete example of where it goes wrong. For each option, say what changes, as a before and after. Write short sentences, one idea per sentence, in the active voice.

      Leave out case numbers and the history of a slug. Use the terms of `vault/wiki/glossary.md`, and explain a term in a few words where it first stands.

      When you need a fact of a Case that you do not hold, ask the `case-guppi` of that Case by `SendMessage`. Do not guess it.
    new: |-
      Give a little context first. Then say the mechanism in plain words, with one real example of where it goes wrong: a line of a page, a file, a ledger or the Case, quoted as it stands, with its path. Find the line yourself where you can read or search for it. When you cannot find it, ask the `case-guppi` of the Case by `SendMessage` which file and which line hold it, then read the file and quote the line yourself. Never make up an example, not even one marked as made up. When you find no real example, say so in one sentence, and give the mechanism without one.

      Lay out each question of a round, and the options in the short text on a Case or in a reply, in the question shape of `.claude/skills/grill-me/SKILL.md`. Its labels may stand in {{chat_lang}}. Write short sentences, one idea per sentence, in the active voice.

      Leave the case numbers and the history of a slug out of your own sentences. A quoted line keeps its case numbers as written. Use the terms of `vault/wiki/glossary.md`, and explain a term in a few words where it first stands.

      When you need any other fact of a Case that you do not hold, ask the `case-guppi` of that Case by `SendMessage`. Do not guess it.
  change: the re-pitch quotes a real line with its path, found by the main agent or located through case-guppi, never a made-up one; options follow the question shape of the grill-me template (case 502)
- slug: estimate-skill-wait-what-re-pitches
  set:
    status: pending
  change: the Criterion replaced whole — a real quoted example or a plain word that none was found, and options in the question shape of the grill-me template (case 502)
```

```tasks
- [x] update `rule-skill-wait-what`
- [x] update `estimate-skill-wait-what-re-pitches`
- [x] `uv run guppi render`: `.claude/skills/wait-what/SKILL.md`
- [ ] read `estimate-skill-wait-what-re-pitches` — `uv run guppi render --check`; by hand, one run of the skill read in the chat in a later session
```

## Deferred

## Case 503 — The report on the findings of pre-spec is numbered in one sequence and split into two parts

> **context:**
> After `/pre-spec` the agent answers the findings in one report. The skill asks for each finding numbered, with its fix, and the decisions of the person. In session 0137 the first report took its numbers from the answer of `ask-guppi`, regrouped the findings by Case, and ran the numbers out of order. The person could not refer to them. The second report numbered the findings in one sequence and split them into two parts: the findings the agent fixes, then the decisions of the person as questions in the shape of the `grill-me` template. The person preferred it and wants it kept.

> **problem:**
> The skill `/pre-spec` sets neither the numbering in one sequence nor the split into two parts, so the form of the report depends on the agent.

```then
defer:
  - slug: rule-prespec
    type: rule
    purpose: The report on the findings of pre-spec numbers them in one sequence and splits them in two parts — the findings the agent fixes, then the decisions of the person as questions in the grill-me shape; the form of the second report of session 0137, put off in session 0137
```

## Case 504 — A hook asks after each reply of the person whether it holds a complaint

> **context:**
> A complaint of the person about the agent's text or work is a lesson: what is worth keeping is a `lesson` line or a Case. In session 0137 the person complained that the numbering of the report after pre-spec was unreadable. The agent fixed the report and wrote no lesson, because nothing in the flow asks it whether a reply of the person is a complaint.

> **problem:**
> Whether a hook should, after each reply of the person, raise the question "does this reply hold a complaint?", so that a complaint becomes a lesson line.

```then
defer:
  - slug: rule-complaint-becomes-a-lesson
    type: rule
    purpose: After each reply of the person a hook raises the question whether it holds a complaint about the agent's text or work, and a complaint becomes a lesson line; an idea of session 0137, not yet decided
```

## Case 505 — The form of the Retro report is to be discussed again

> **context:**
> The report of `/retro` follows the skeleton of `rule-retro` (cases 468.1, 483): one numbered list of what needs an end, two count lines, and the close in three parts. It has no heading that names it Retro. What the agent noticed in Work Mode stands in the same list as the debt, with no section of its own. The person does not like how the report looks now. One thing is kept as it is: `/work` ends by calling `/retro` at once, and the agent does not stop between them.

> **problem:**
> How the Retro report should look: its heading, its parts and the place of what the agent noticed. The call of `/retro` right after Work Mode stays as it is.

```then
defer:
  - slug: rule-retro
    type: rule
    purpose: Discuss again how the Retro report should look — a heading that names it Retro, its parts, and what the agent noticed in Work Mode set apart from the debt; the call of /retro right after Work Mode stays; raised at the Retro of session 0137
```
