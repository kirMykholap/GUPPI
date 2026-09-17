<!-- approved 23:01:04 · session 03093688 -->

# Spec — 2026-09-17, session 1119

## Case 224 — `insight-ledger-hook-reads-only-the-final-text`

> **context:**
> `insight-ledger-hook-reads-only-the-final-text` is the Insight over five lessons on the ledger hook: a `LEDGER` block that is not the last text of its turn "is lost". It was `actioned` by case 137 and reopened by the librarian of 2238 on the fifth lesson, `lesson-ledger-block-followed-by-a-tool-call` (the reply to case 222 ended in a ToolSearch call). Its Proposal asks one thing: read `guppi/ledger.py` against a transcript and settle whether an intermediate assistant text is in the transcript at all. Today `rule-ledger-write` and `CLAUDE.md` (the Render of `rule-case-protocol`) say the text before a tool call is never kept, not in the transcript, not in `last_assistant_message`; the refusal of `guppi gate` prints the same sentence. The Case touches `estimate-ledger-write-lifts` (the old shape, no `method` field — a recut by case 211) and `estimate-case-protocol-loaded` (no `method` field either); it does not touch `estimate-hook-registry-rendered`. No page is created; the lesson is a line the hook writes, `knowledge`, with a `source`.

> **problem:**
> `transcript_texts` has collected every text of the main agent from the transcript since case 55.2, and `tests/test_ledger.py` fixes the case of a text with a block followed by a `tool_use` record — it passes. The transcripts hold the intermediate texts: session 2238 (Claude Code 2.1.272) — 19 of 19 texts followed by a tool call in the same turn, the block of case 222 among them; session 0747 of 2026-09-14 (2.1.270) — the block of case 117, written by the hook 13 seconds later at the `Stop` of the same turn; the session of 2026-09-13 (2.1.269) — the block of case 101, written at the next `Stop` 22 minutes later. The one measured loss is the block of case 109 in that same session: it is absent from the transcript, and nothing explains it. The lines of case 222 are in the ledger (01:25:46), written by the `Stop` at the end of the same turn; "the Stop hook read nothing" was a wrong diagnosis: the agent checked `ledger.md` before the turn had ended. The claim "never kept" in the rule, in `CLAUDE.md` and in the gate's advice is false; one gap is real: a turn that ends in a tool call has no `Stop`, its lines wait for the next `Stop` of the same session, and the last turn of a session has none.

### Case 224.1 — `rule-ledger-write`: the text before a tool call waits for the next `Stop`

> **given:**
> The `Stop` hook `uv run guppi ledger` receives `transcript_path` and `last_assistant_message` at the end of every turn of the main agent.
> **＋** The session's transcript holds every assistant text, a text followed by a tool call in the same turn included (Claude Code 2.1.269–2.1.272, the sessions of 2026-09-13, 2026-09-14 and 2238).
> **＋** `tests/test_ledger.py` and `tests/test_gate.py` fix the behaviour with piped payloads against a temp vault.

> **when:**
> The `Stop` hook fires in a session with a `hi` recorded, or `guppi gate` refuses a `Skill` call for an item of the Spec without a ledger line.

> **then:**
> Every line `- decision[`, `- estimate[`, `- lesson[` inside a `LEDGER` block of any text of the main agent in the transcript, the reply just finished included, lands in `raw/<hi date>/<hi HHMM>/ledger.md` with the time of writing, once — a body already in any `ledger.md` under `raw/` is not written again.
> **＋** A block in a text followed by a tool call in the same turn reaches the ledger at the next `Stop` of the session, with the time of that `Stop`; the reply that ends in the text lands it now.
> **＋** The gate's advice to the agent reads: `The text before a tool call waits for the next Stop: end this reply in text with the LEDGER block, then call /<skill> in the next reply.`
> **－** Without a `hi`: exit 2 with the reason, the ledger untouched; with `stop_hook_active`: exit 0, nothing written.
> **－** The last turn of a session that ends in a tool call has no `Stop` after it; its lines are a finding of Retro, not of the hook.

```then
update:
  - slug: rule-ledger-write
    replace:
      - old: "A reply that ends in a tool call (`Skill`, `ExitPlanMode`) has no `Stop` of its own, and the text before the call is never kept: not in the transcript, not in `last_assistant_message` (measured in sessions L and N). The harness holds the reply back instead of the agent's memory:"
        new: "A reply that ends in a tool call (`Skill`, `ExitPlanMode`) has no `Stop` of its own. The text before the call is kept in the transcript — measured on Claude Code 2.1.269–2.1.272: the blocks of cases 101, 117 and 222 stood in a text followed by a tool call and reached the ledger at the next `Stop` of the session, 22 minutes, 13 seconds and 14 seconds later; one block, case 109 on 2.1.269, was absent from the transcript and is not explained (case 224.1). A block followed by a tool call waits for the next `Stop`; the reply that ends in the text lands it now, with its own time. The harness holds the reply back instead of the agent's memory:"
      - old: "The text before a tool call is never kept: end this reply in text with the LEDGER block, then call /<skill> in the next reply."
        new: "The text before a tool call waits for the next Stop: end this reply in text with the LEDGER block, then call /<skill> in the next reply."
    change: the text before a tool call is kept in the transcript and read at the next Stop; the gate's advice says so (case 224.1)
  - slug: estimate-ledger-write-lifts
    set: {status: pending, method: "pytest in tests/test_ledger.py and tests/test_gate.py with piped payloads against a temp vault; the live reading once by hand — the lines of the Case in the session's ledger.md, written by the hook"}
    change: the Criterion replaced whole — the text before a tool call is read at the next Stop, the gate's advice reworded (case 224.1)
```

```tasks
- [ ] update `rule-ledger-write`: two `replace` pairs in How it works, `change`
- [ ] update `estimate-ledger-write-lifts`: `set: {status: pending, method}`, `change`
- [x] `guppi/gate.py`: the advice to the agent — "waits for the next Stop"
- [x] `tests/test_gate.py`: an assertion on the new advice on the `Skill` path
- [x] read `estimate-ledger-write-lifts`: `pytest tests/test_ledger.py tests/test_gate.py`, plus the lines of this Case in `raw/2026-09-17/1119/ledger.md` written by the hook
```

### Case 224.2 — `rule-case-protocol`: the sentence in `CLAUDE.md`

> **given:**
> `CLAUDE.md` is the Render of `rule-case-protocol`, loaded from the first turn without a read.
> **＋** The transcript keeps the text before a tool call, and the hook reads it at the next `Stop` (224.1).

> **when:**
> A session starts with `CLAUDE.md`, and the agent writes a reply with a `LEDGER` block.

> **then:**
> The agent states the `LEDGER`-block rule and the one-Case-at-a-time rule without a read call.
> **＋** A reply with a `LEDGER` block ends in that text; no tool call follows in the same reply — `CLAUDE.md` says: the text before a tool call waits for the next `Stop` of the session, and the last reply of a session has none.
> **＋** A block a tool call did follow the agent does not call lost before the `Stop` of that turn; at the next `Stop` it checks the ledger, and only a line missing there is a lesson.
> **－** Lines outside a `LEDGER` block — bare, or in a fence with another tag or none — do not reach the ledger.

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "A reply that carries a `LEDGER` block ends in that text. No tool call follows it in the same reply: the text before a tool call is never kept, and the hook reads nothing."
        new: "A reply that carries a `LEDGER` block ends in that text. No tool call follows it in the same reply: the text before a tool call waits for the next `Stop` of the session, and the last reply of a session has none. A block a tool call did follow is not lost until that `Stop` has passed: check the ledger then, and only a line missing there is a lesson."
      - old: "Work Mode ticks the boxes in `raw/<date>/<hi HHMM>/spec.md` in the reply that finishes the task; Retro counts the unticked."
        new: "Work Mode ticks the boxes on code, tests, migrations and readings in `raw/<date>/<hi HHMM>/spec.md` in the reply that finishes the task; `generate` and `render` tick the page and render lines (case 226); Retro counts the unticked."
    change: the text before a tool call waits for the next Stop, not "never kept"; a block is not called lost before that Stop; the page and render lines are ticked by generate and render (cases 224.2, 233)
  - slug: estimate-case-protocol-loaded
    set: {status: pending, method: "One reading at a session start, by hand, plus the preview cases of tests/test_ledger.py."}
    sections:
      Criterion: |
        When:
        A session starts with `CLAUDE.md`.

        Then:
        The agent states the LEDGER-block rule and the one-Case-at-a-time rule without a read
        call.
        **＋** The Case protocol says the Spec is `raw/<date>/<hi HHMM>/spec.md` — the
        `## Deferred` heading, the ticked boxes — and the Frontier
        `raw/<date>/<hi HHMM>/frontier.md`.
        **＋** A reply with a `LEDGER` block ends in that text; no tool call follows in the
        same reply — the text before a tool call waits for the next `Stop` of the session,
        and the last reply of a session has none.
        **＋** A block a tool call did follow the agent does not call lost before the `Stop`
        of that turn; at the next `Stop` it checks the ledger, and only a line missing there
        is a lesson.
        **＋** The Case protocol says Work Mode ticks the boxes on code, tests, migrations and
        readings, and `generate` and `render` tick the page and render lines (case 226).
        **－** A reply whose ledger lines sit outside a `LEDGER` block — bare, or in a fence
        with another tag or none — adds nothing to the session's ledger.
    change: three lines added to the Criterion — the wait for the next Stop, no loss called before it, who ticks which line (cases 224.2, 233)
```

```tasks
- [ ] update `rule-case-protocol`: one `replace` pair in the Render, `change`
- [ ] update `estimate-case-protocol-loaded`: `set: {status: pending, method}`, `sections: Criterion`, `change`
- [ ] `uv run guppi render`: `CLAUDE.md`
- [ ] read `estimate-case-protocol-loaded`: the first turn of the next session, by hand
```

### Case 224.3 — the Insight `actioned`

> **given:**
> The question of the Proposal is answered by a reading of the transcripts: the intermediate text is in the transcript, and the hook collects it.
> **＋** A new lesson of the same pattern reopens an `actioned` Insight (insights/schema).

> **when:**
> The librarian applies the decision, and the next `/hi` assembles the Deferred list of the brief.

> **then:**
> `insight-ledger-hook-reads-only-the-final-text` stands `actioned`, `addressed_by: decision-case-224.3`, and leaves the Deferred list.
> **＋** The lesson `lesson-transcript-keeps-the-text-before-a-tool-call` (`knowledge`, `source` the transcript of 2238) is written in this session; it is not a child of this Insight — its root cause is the opposite of the Insight's pattern — and synthesis does not reopen the Insight on it.
> **＋** The Insight's `pattern` says what was measured: every text of a turn is read at the next `Stop`, a block followed by a tool call waits for it, only the last reply of a session can be lost.
> **－** The fifth lesson and its root cause are not edited — a lesson is not changed by a decision; the correction stands in the new lesson.

```then
update:
  - slug: insight-ledger-hook-reads-only-the-final-text
    set: {status: actioned, addressed_by: "[[decision-case-224.3]]", pattern: "The ledger writer sees every text of a turn at the next Stop; a LEDGER block followed by a tool call waits for it, and only the last reply of a session can be lost (case 224)."}
    change: the question of the Proposal answered by reading the transcripts — the intermediate text is kept and read at the next Stop; the rule, CLAUDE.md and the gate's advice corrected; the pattern says what was measured (cases 224, 233)
```

```tasks
- [ ] update `insight-ledger-hook-reads-only-the-final-text`: `set: {status: actioned, addressed_by}`, `change`
- [x] the lesson line `lesson-transcript-keeps-the-text-before-a-tool-call` in the reply that acknowledges ratification
```

## Case 225 — `rule-carry-over`: the stray `ref` field (takes up case 223)

> **context:**
> `rule-carry-over` (`draft`, parent `rule-end-of-work`) carries a `ref: rule-end-of-work` field beside `parent` — the same lift as on the 15 Estimate pages of case 210 (`lesson-materialize-item-ref-lifted-as-a-page-field`), on a rule page; `rules/schema.yaml` names no `ref`. Case 214.1 keeps `ref` off every page from now on; case 210 named the Estimate pages only, and Work Mode left this one as it stood. Case 223 deferred it to this Plan Mode; today it is the one live page of `wiki/` with `ref:` in its frontmatter — a grep over every category. `set` in `generate` assigns a value and cannot remove a key; an `update` with `change` alone it applies — a History line with the pointer, the page saved. The Case touches no Estimate: no rule changes; `estimate-carry-over-writes` stands `pending` for its own reason.

> **problem:**
> One live rule page carries a field nobody ratified; the one-off of 210 did not cover it, and Retro ratifies no update. `deferred_by: decision-case-223` on the page is cleared only by a ledger line with `{supersedes:case 223}` — and case 210 had no ledger line at all, so its form cannot simply be repeated.

> **given:**
> `rules/schema.yaml` names no `ref` field; the link to the parent is `parent`.
> **＋** `generate` applies an `update` with `change` alone: a History line with the pointer to the Decision page; `{supersedes:case 223}` clears `deferred_by` (case 200.2).
> **－** `set` removes no key; the edit of the field is a script run once by path (`index.md` §1).

> **when:**
> Someone reads the frontmatter of `rule-carry-over` after Work Mode and after the librarian's run.

> **then:**
> `rule-carry-over` carries no `ref` field; `parent`, `governs`, `estimates` and the rest stand as they were.
> **＋** The page's History carries one line on it, written by `generate`: `updated: the stray ref field removed by a one-off script (case 225)`.
> **＋** `deferred_by` on the page is empty; `decision-case-223` is `superseded`.
> **－** Nothing else on the page changes; `make lint` gets no new finding.

```then
update:
  - slug: rule-carry-over
    change: the stray ref field removed by a one-off script (case 225)
migration:
  - what: a one-off script removes the `ref:` line from the frontmatter of vault/wiki/rules/rule-carry-over.md
    pages: 1
```

```tasks
- [x] one-off migration script, run once by path from the scratchpad: remove `^ref: ` from `vault/wiki/rules/rule-carry-over.md`
- [ ] update `rule-carry-over`: `change` alone; `{supersedes:case 223}` on the line
- [x] `make lint`: no new finding; `git diff --stat` — exactly one file (of `vault/wiki/rules/`; the tree holds the code of the other Cases)
```

## Case 226 — `generate` and `render` tick the page lines of the Spec (takes up case 217)

> **context:**
> `rule-page-generation` applies the entries of `materialize.yaml` to pages and knows nothing of the Spec; `rule-render-harness` writes the harness files from the Rule pages and knows nothing of the Spec either. The task lines of a Spec — `- [ ] create `slug``, `update `slug``, `guppi render` — stay open at the end of every session: the librarian is forbidden to read the Spec (`estimate-documentation-completes`), and the agent in Work Mode does none of these actions — the librarian does. Case 216 ticked 21 lines of the 1955 Spec by hand; case 217 deferred the mechanism to this Plan Mode; the 2238 Spec holds 36 unticked lines, 29 of them pages and renders. The yaml lies in the session's folder beside `spec.md`, each entry carries `case`, `kind` and `slug`; `generate` marks an entry `applied` once applied; `render` without a flag writes every governed file and exits 0, `--sync` is the `SessionStart` hook, `--check` writes nothing. The Case creates one new promise per rule and touches none of the five Estimates of `rule-page-generation` nor the two of `rule-render-harness`; the slugs `estimate-generate-ticks-the-spec` and `estimate-render-harness-ticks-the-spec` are free, in `wiki/` and in the archive. The question of 3b — who ticks what — this Case does not settle: the lines on code, tests, migrations and readings stay the agent's, as 217 said.

> **problem:**
> The lines whose work a script does are ticked by nobody: Retro counts them as debt, and every session ends either in a tick by hand after the fact or in false debt.

### Case 226.1 — `generate` ticks the page line

> **given:**
> A yaml entry carries `case`, `kind` and `slug`; the Spec of the unit lies beside the yaml — `raw/<date>/<HHMM>/spec.md`.
> **＋** A Case heading in the Spec is `## Case N — …` or `### Case N.M — …`; its section runs to the next such heading.
> **＋** `tests/test_generate.py` fixes the behaviour on a temp vault with a Spec beside the yaml.
> **－** A Rule-class file entry `generate` does not apply — "applied by hand".

> **when:**
> `guppi generate` applied an entry `create`, `update`, `delete` or `defer` and marked it `applied`.

> **then:**
> In the `spec.md` of the same unit the first unticked line `- [ ] <kind> `<slug>`` in the section of the entry's Case becomes `- [x]`; nothing else in the file changes.
> **＋** Two entries of one kind and slug in one Case tick two lines, in order.
> **－** A line not found, a section not found, no Spec — no error and no stderr line; the entry is `applied` all the same.
> **－** `estimate`, `lesson` and Rule-class file entries, and an entry with `failed`, tick no line; the lines on code, tests, migrations, `read` and `by hand` are the agent's.

```then
create:
  - slug: estimate-generate-ticks-the-spec
    type: estimate
    ref: rule-page-generation
    kind: QA
    purpose: generate ticks, in the Spec beside its yaml, the page line of the Case whose entry it applied
    method: pytest tests/test_generate.py with a Spec beside the yaml, plus one reading of this session's spec.md after the librarian's run
    tags: [harness, workflow, ledger]
update:
  - slug: rule-page-generation
    replace:
      - old: "The mechanism — the shape of every entry and every History line — lives in the docstring of `guppi/generate.py`."
        new: "Once an entry is applied, the script ticks its line in the Spec beside the yaml — `- [ ] <kind> `<slug>`` in the section of the entry's Case — so the Spec's page lines are closed by the one who did the work, and a line not found is no error (case 226.1). The mechanism — the shape of every entry and every History line — lives in the docstring of `guppi/generate.py`."
    change: generate ticks the page line of the Spec once the entry is applied (case 226.1)
```

```tasks
- [ ] create `estimate-generate-ticks-the-spec` (`ref: rule-page-generation`)
- [ ] update `rule-page-generation`: one `replace` in Purpose, `change`; `{supersedes:case 217}` on the line
- [x] `guppi/generate.py`: `tick_spec(unit, case, kind, slug)` after `applied`; docstring; tests first in `tests/test_generate.py`
- [ ] read `estimate-generate-ticks-the-spec`: pytest, plus the page lines of this Spec ticked by the librarian's run
```

### Case 226.2 — `render` ticks the `guppi render` lines

> **given:**
> `guppi render` without a flag writes every governed file and exits 0, or writes nothing and exits 1.
> **＋** The units under `raw/` with a yaml are `units_with`; a yaml is applied whole when every entry carries `applied`.
> **＋** `tests/test_render.py` fixes the behaviour on a temp vault.

> **when:**
> `guppi render` without a flag wrote the files and exits 0.

> **then:**
> In the `spec.md` of every unit under `raw/` whose yaml is applied whole, every unticked task line holding `guppi render` in a code span becomes `- [x]`; nothing else changes.
> **－** `--check` and `--sync` tick nothing; exit 1 ticks nothing.
> **－** A unit without a yaml, with an unapplied or `failed` entry, or marked by `carry.md`, is not touched.

```then
create:
  - slug: estimate-render-harness-ticks-the-spec
    type: estimate
    ref: rule-render-harness
    kind: QA
    purpose: render, once it wrote the harness and exits 0, ticks the guppi render lines of every Spec under raw/ whose yaml is applied whole
    method: pytest tests/test_render.py, plus one reading of this session's spec.md after the librarian's run
    tags: [harness, render]
update:
  - slug: rule-render-harness
    replace:
      - old: "The rendered files are committed by the librarian, in its own commit (case 89.2)."
        new: "The rendered files are committed by the librarian, in its own commit (case 89.2). Once the plain `guppi render` wrote the files and exits 0, it ticks every unticked task line holding `guppi render` in the `spec.md` of every unit under `raw/` whose yaml is applied whole; `--check`, `--sync` and an exit 1 tick nothing (case 226.2)."
      - old: "the renderer runs with lint, in no phase of the session."
        new: "the renderer runs with lint and as the librarian's step after `cleanup` (case 89.1); the tick of case 226.2 belongs to that step."
    change: render ticks the guppi render lines of the applied Specs under raw/; the Purpose names the librarian's step (cases 226.2, 233)
```

```tasks
- [ ] create `estimate-render-harness-ticks-the-spec` (`ref: rule-render-harness`)
- [ ] update `rule-render-harness`: one `replace` in How it works, `change`
- [x] `guppi/render.py`: the tick after `write_all`; docstring; tests first in `tests/test_render.py`
- [ ] read `estimate-render-harness-ticks-the-spec`: pytest, plus the `guppi render` lines of this Spec ticked by the librarian's run
```

## Case 227 — `sprint.md` is checked, not rendered, at `SessionStart`

> **context:**
> `vault/wiki/sprint.md` is the file `guppi sprint` writes from the page `entity-sprint-migration` (case 209); `rule-sprint` (`draft`, `enforcement: check`, `governs: vault/wiki/sprint.md`) keeps it from a hand edit through the governed-files hook, and the librarian rewrites it after `render` on every run. The harness files with a Render have a second guard in `render --sync`: the `SessionStart` hook prints a diff and rewrites a file that drifted from its page, `/hi` shows it on the `Render:` line, and `make lint` catches the drift with `render --check`. `sprint.md` has neither: `render` does not know it, `make lint` does not compare it; a drift is possible when a librarian run fails between `generate` and `sprint`, or the file is edited past the hook. Flag 3 of the 2238 handoff asked whether it needs a check at `SessionStart` like `render --sync`. The Case creates one promise of `rule-sprint` and does not touch `estimate-sprint-renders-the-backlog`; the slug `estimate-sprint-checks-the-file` is free. The `Makefile` is an `implementation_ref` of `rule-lint`, not a governed file.

> **problem:**
> The file `/hi` assembles the Frontier from is checked against its page by nobody; a drift is seen only by eye.

> **given:**
> `guppi sprint` renders the file from the sprint page; `render --check` is the model: compare in memory, name the file, exit 1, write nothing.
> **＋** `tests/test_sprint.py` fixes the behaviour on a temp vault.
> **－** `make lint` writes nothing to the tree (case 147.7).

> **when:**
> Someone runs `uv run guppi sprint --check`, by hand or through `make lint`.

> **then:**
> When `vault/wiki/sprint.md` differs from the render of the page, one line on stdout — `sprint: vault/wiki/sprint.md differs from entity-sprint-<id>` — and exit 1; when it is the same, silence and exit 0; the file is written in neither case.
> **＋** `make lint` calls it after `render --check`, before `guppi lint`.
> **－** A render error — no page, two, a slug without a page — as with `guppi sprint`: stderr and exit 1.
> **－** Nothing is added at `SessionStart` or in `/hi`.

```then
create:
  - slug: estimate-sprint-checks-the-file
    type: estimate
    ref: rule-sprint
    kind: QA
    purpose: sprint --check names sprint.md when it differs from the render of the sprint page, exit 1, and writes nothing
    method: pytest tests/test_sprint.py, plus make lint after the librarian's run — no sprint line
    tags: [harness, sprint]
update:
  - slug: rule-sprint
    replace:
      - old: "The first `## <id>` heading of the file is the sprint id `sprint_id`, `cleanup` and `archive` read, unchanged."
        new: "The first `## <id>` heading of the file is the sprint id `sprint_id`, `cleanup` and `archive` read, unchanged. `guppi sprint --check` renders in memory and names the file when it differs, exit 1, writing nothing; `make lint` runs it after `render --check` (case 227)."
    change: sprint --check, run by make lint, names a drifted sprint.md (case 227)
  - slug: rule-lint
    replace:
      - old: "`make lint` runs it after `render --check`; both only report, so the Makefile's rule — no target writes to the tree — holds (case 147.7)."
        new: "`make lint` runs it after `render --check` and `sprint --check`; all three only report, so the Makefile's rule — no target writes to the tree — holds (cases 147.7, 227)."
    change: make lint has three steps — sprint --check between render --check and lint (case 227)
```

```tasks
- [ ] create `estimate-sprint-checks-the-file` (`ref: rule-sprint`)
- [ ] update `rule-sprint`: one `replace` in Purpose, `change`
- [ ] update `rule-lint`: one `replace`, `change`
- [x] `guppi/sprint.py`: `--check`; docstring; tests first in `tests/test_sprint.py`
- [x] `Makefile`: `lint` — `uv run guppi sprint --check` as the second line
- [ ] read `estimate-sprint-checks-the-file`: pytest, plus `make lint` after the librarian's run — no `sprint:` line
```

## Case 229 — the sprint: milestones and a backlog

> **context:**
> `entity-sprint-migration` is the sprint page (case 209): its `estimates` are the Definition of done, its `## Backlog` the Slices, each item a wikilink to a page; `guppi sprint` renders `sprint.md` from it, `/hi` reads the file whole and assembles the Frontier — "where the sprint stands" — and the brief puts every deferred target into Deferred (cap 7, ranked by severity and the count of briefs). The result shows in this session: Slice 5 stands in the Frontier every time, `rule-work-mode` in Deferred for nineteen briefs, and the only place for "some day" is a defer with a placeholder page. The Case touches four rules and one Estimate of three of them: `estimate-sprint-renders-the-backlog` (`pending`, the new shape), `estimate-hi-writes-frontier` (`passed`, the old shape — a recut with `set.method`), `estimate-brief-written` (`pending`, the new shape); the Estimates of `entity-sprint-migration` it does not touch. `generate` puts a new section of a page after the existing ones, before History; the order of a category's sections is `SECTION_ORDER` in the code and `entities/schema.md`.

> **problem:**
> The Frontier and the brief show everything not closed, whoever's turn it is; an item without a turn has no place but Deferred, where it counts briefs and wears the eye. A sprint is an order, not a list.

### Case 229.1 — the sprint page

> **given:**
> The sprint page is an Entity MOC; its sections are read by `guppi sprint`, the order of a category's sections is set by `SECTION_ORDER`.
> **＋** An item is a line `- [[slug]] — <text>` or `- <text>`; a milestone heading is `### <name>`.
> **－** Order is the content of the page, not a field (`index.md` §6).

> **when:**
> Someone reads `entity-sprint-migration` after the librarian's run.

> **then:**
> The page holds `## Milestones` — the three Slices as today, 3b, 4, 5, with their items — and `## Backlog` with two plain lines: the categories as data of the project; the product model.
> **＋** The sections run `Purpose`, `Milestones`, `Backlog`, `Closed`; `entities/schema.md` names the three as the sections of a sprint page, in this order.
> **－** The Estimates, `purpose` and `Closed` do not change.

```then
update:
  - slug: entity-sprint-migration
    sections:
      Milestones: |
        ### Slice 3b — Work Mode

        - [[rule-work-mode]] — Work Mode: the Spec as tasks with code, the ticked boxes in `spec.md`, the test of each Estimate written first and turned green; cases 183, 206
        - [[rule-subagent-guppi]] — what a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case; cases 183, 206

        ### Slice 4 — conversion of the parked pages by group

        - [[estimate-sprint-migration-leftovers-gone]] — every page of `vault/parked/` and every document of 2026-08 under `docs/` converted, archived or deleted by a decision

        ### Slice 5 — closing

        - [[estimate-sprint-migration-lint-clean]] — `make lint` exit 0: the 31 Decision pages of Cases 1–28 decided, `unmigrated` at zero
        - [[estimate-sprint-migration-merges]] — `make test` green, `migration` merged into `main`
        - [[rule-spec-box]] — the Spec box, case 207, after Slice 3b
      Backlog: |
        - the categories as data of the project: `generate`, `lint`, `materialize` and `ask-guppi` read the category set from `wiki/<category>/schema.yaml`; the development set — entity, rule, estimate — is the default (session 1119)
        - the product model: `applies_to` on a Rule and `rules` on an Entity, `kind: test | measurement | reading`, `ask-guppi` through Entities, the pre-task questions before a product's records (session 1119)
    change: the Slices under Milestones, a Backlog of two plain lines without a page (case 229.1)
  - slug: entities-schema
    file: vault/wiki/entities/schema.md
    change: a sprint page carries Milestones, Backlog and Closed after Purpose, in this order; an item is a wikilink line or a plain line (case 229.1)
```

```tasks
- [ ] update `entity-sprint-migration`: `sections: Milestones, Backlog`, `change`
- [x] update `entities/schema.md`, by hand: the sections of a sprint page
- [x] `guppi/generate.py`: `SECTION_ORDER["entities"]` — `Milestones`, `Backlog`, `Closed` after `How it works`; a test in `tests/test_generate.py`
```

### Case 229.2 — `rule-sprint`: the render by milestone

> **given:**
> The cascade of `generate` sets `built`; `cleanup` sets `archived`; `sprint_id` reads the first `## <id>` heading.
> **＋** The current milestone is the first `### ` under `## Milestones` with an item not done, or with no item.
> **＋** `tests/test_sprint.py` fixes the behaviour on a temp vault.
> **－** The script writes no page of `wiki/`.

> **when:**
> `guppi sprint` runs with a live page `entity-sprint-<id>`.

> **then:**
> The file: `# Sprint`; `## <id>`; Purpose; `**Done when**` — as today; then `## Milestones`: a closed milestone as one line `### [x] <name>`; the current one as the heading `### [ ] <name>` and each item with its status and `deferred_by`, as today; each later one as one line `### [ ] <name> — N items`; then `## Backlog` — each item a line; then `## Closed` as it is.
> **＋** An item `- [[slug]] — <text>` is ticked by the status of its page, as today; an item `- <text>` without a wikilink renders `- [ ] <text>` and is never ticked.
> **＋** A milestone is closed when every item is `[x]`; with no item it is open.
> **－** A slug with no live or archived page: stderr, exit 1, the file not written. `--check` (case 227) compares this same render.

```then
update:
  - slug: rule-sprint
    replace:
      - old: "`guppi sprint` writes it from that page, one tick per item by the status of the page it names."
        new: "`guppi sprint` writes it from that page, one tick per item by the status of the page it names; the `## Milestones` of the page render in order — a closed one as one line, the current one whole, a later one as one line with its count — and the `## Backlog`, the items without a turn, as a list; an item without a wikilink is a plain line, never ticked (case 229.2)."
      - old: "whose `## Backlog` lists the open Slices, each item a wikilink to a page."
        new: "whose `## Milestones` lists the Slices in order and whose `## Backlog` the items without a turn, each a wikilink to a page or a plain line (case 229)."
    change: the render by milestone — the current one whole, the others one line, the Backlog a list, a plain item never ticked; the Purpose names the two sections (cases 229.2, 233)
  - slug: estimate-sprint-renders-the-backlog
    set: {status: pending}
    change: the Criterion replaced whole — the render by milestone (case 229.2)
```

```tasks
- [ ] update `rule-sprint`: one `replace` in Purpose, `change`
- [ ] update `estimate-sprint-renders-the-backlog`: `set: {status: pending}`, `change`
- [x] `guppi/sprint.py`: `## Milestones` — current, later, closed; the plain line; docstring; tests first in `tests/test_sprint.py`
- [ ] read `estimate-sprint-renders-the-backlog`: pytest, plus `sprint.md` after the librarian's run
```

### Case 229.3 — `rule-skill-hi`: the Frontier from the current milestone

> **given:**
> `/hi` puts `sprint.md` into the context on the first turn; the Frontier is written to `raw/<date>/<hi HHMM>/frontier.md`, one line per item; `/pre-task` fails on an open line.
> **＋** `sprint.md` shows the current milestone whole and a later one as one line.

> **when:**
> The person invokes `/hi`, and the agent assembles the Frontier.

> **then:**
> The items of the current milestone are Frontier lines; a later milestone, the Backlog and Closed are not.
> **＋** The other sources as today: an unfinished plan first, a hand edit from `Render:`, a failed pull and an unavailable `gh`, a `failed` reading and a lesson of the Tail, the readings `pending`, the flags of the brief; an item the person adds is a new line.
> **＋** Each line `- [ ] F<n> — <title> · <source>`; closed as `[x] … · case N`, `[x] … · work` or `[-] … · defer case N`.
> **－** A decision line of the Tail is not an item.

```then
update:
  - slug: rule-skill-hi
    replace:
      - old: "Assemble the Frontier from the above and present it as a list: tasks, problems, debt carried over, where the sprint stands; on a plan branch the unfinished plan comes first;"
        new: "Assemble the Frontier from the above and present it as a list: tasks, problems, debt carried over, the items of the sprint's current milestone — the first with an open item or with none — and none of a later milestone, of the Backlog or of Closed (case 229.3); on a plan branch the unfinished plan comes first;"
    change: the Frontier takes the current milestone of the sprint only (case 229.3)
  - slug: estimate-hi-writes-frontier
    set: {status: pending, method: "one reading by hand at the first /hi of the next session, written into the estimate line; unit: the frontier findings of guppi pretask --check in tests/test_pretask.py"}
    change: the Criterion replaced whole — the Frontier from the current milestone, the lines and their closing kept (case 229.3)
```

```tasks
- [ ] update `rule-skill-hi`: one `replace` in the Render, `change`
- [ ] update `estimate-hi-writes-frontier`: `set: {status: pending, method}`, `change`
- [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [ ] read `estimate-hi-writes-frontier`: the first `/hi` of the next session — a Frontier without Slices 4 and 5
```

### Case 229.4 — `rule-brief`: Deferred without what the sprint page holds

> **given:**
> The librarian writes the brief by the frame; Deferred is at most seven, ranked by severity and the count of briefs.
> **＋** The sprint page names its items as wikilinks under `Milestones` and `Backlog`.

> **when:**
> The librarian rewrites `brief.md` at the end of its run.

> **then:**
> A defer target whose page the sprint page names — under any milestone or in the Backlog — is not in Deferred; its count of briefs does not grow.
> **＋** The rest as today: the defer targets of this run, the items of the previous list no `supersedes` retired, every `open` Insight; the cap of seven, the ranking.
> **－** Flags and the other sections do not change; the librarian still never edits `sprint.md`.

```then
update:
  - slug: rule-brief
    replace:
      - old: "and every Insight whose `status` is `open`. Rank by `severity`"
        new: "and every Insight whose `status` is `open` — but never a target the sprint page names, under a milestone or in its Backlog: the sprint is its window, and its count of briefs does not grow (case 229.4). Rank by `severity`"
      - old: "Deferred is the previous brief's list as it stands plus the `defer` items of this Spec by slug;"
        new: "Deferred is the previous brief's list as it stands plus the `defer` items of this Spec by slug, less the targets the sprint page names (case 229.4);"
    change: Deferred leaves out a target the sprint page names, in the librarian's brief and in the /carry brief alike (cases 229.4, 233)
  - slug: estimate-brief-written
    set: {status: pending}
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
        **＋** Deferred — at most seven: the targets of the `defer` entries of this run, the items of the previous list whose decision no `supersedes` retired, every `open` Insight; never a target the sprint page names under a milestone or in its Backlog, whose count of briefs does not grow (case 229.4); ranked by `severity` — its own or that of the related Insight — then by the number of briefs the item stood in; an Insight's line carries its slug, `severity`, `pattern` and its Proposal in one or two sentences.
        **＋** Flags, no limit: entries `incomplete`, `failed`, `near`, `unparsed`; `failed` Estimates; MOC candidates; stale defers; contradictions; the lint output; a handoff flag that asks for a change of the sprint, as a Case of the next Plan Mode.
        **＋** Readings at the close — `make test`, `make lint`, page counts.
        **－** The brief states no decision and no judgment of the work; a change of the sprint is a Case, never the librarian's edit.
    change: the Deferred line — never a target the sprint page names (case 229.4)
```

```tasks
- [ ] update `rule-brief`: one `replace` in the Render, `change`
- [ ] update `estimate-brief-written`: `set: {status: pending}`, `sections: Criterion`, `change`
- [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [ ] read `estimate-brief-written`: the brief after the librarian's run — `rule-work-mode`, `rule-subagent-guppi`, `rule-spec-box` not in Deferred
```

## Case 233 — the corrections of pre-task

> **context:**
> `pretask --check` was clean after three corrections of form: the defer of `index` had no `file:`, F5 ended in the wrong word, F9 pointed at a defer of another plan — closed as `work`. `ask-guppi` read the Spec against the vault and found ten places: five sentences the ratified Cases left stale on the same or a neighbouring page, three promises the Cases did not name, two Cases disagreeing with each other. Every `replace` occurs on its page once. Known and left alone: `estimate-lint-catches` ("`make lint` runs it after `render --check`; neither writes") stays true with three steps; `estimate-documentation-completes` ("`make lint` passes its `render --check` step") too; `estimate-generate-fails-alone` ("a rerun writes nothing") holds because a rerun applies nothing; `rule-lint` "lint runs with the renderer, in no phase of the session" is true. Six corrections went into the ratified Cases in place, without a new line: 224.2 (the "Work Mode ticks the boxes" sentence of `rule-case-protocol` and the line in `estimate-case-protocol-loaded`), 224.3 (the Insight's `pattern`, the new lesson not its child), 226.2 (`rule-render-harness` Purpose: the librarian's step), 229.2 (`rule-sprint` Purpose: the two sections), 229.3 ("or with none"), 229.4 (the `/carry` paragraph of `rule-brief`). Five are new updates, each with its line. One touches `index.md`, which Case 230 defers: by case 186.2 a finding, shown here — the defer is about the definitions of §1 and §6, the change a table row on `sprint.md` and a word in §2.

> **problem:**
> A ratified Case leaves a sentence false on a page it did not name, or a promise unnamed; the vault would say two things.

### Case 233.1 — `rule-harness`: a fourth tool in `make lint`

> **given:**
> `make lint` is `render --check`, `sprint --check`, `guppi lint` (case 227); `rule-sprint` is a child of `rule-documentation`, not of `rule-harness`.
> **＋** `estimate-harness-pipeline` is the old shape — a recut with `set.method`.

> **when:**
> `make lint` and `make test-harness` run; someone reads `rule-harness`.

> **then:**
> The Purpose says: three rules belong to no phase of the session — the renderer, the page `settings.json` is assembled from, lint — and with them the check of `rule-sprint` runs in `make lint`, in this order: the harness files against their pages, the sprint file against its page, then the pages.
> **＋** `make test-harness` is green; `make lint` exits 0 on the committed tree by its first two steps.

```then
update:
  - slug: rule-harness
    replace:
      - old: "They run together in `make lint`, in this order: the harness files are checked against their pages before the pages."
        new: "They run together in `make lint`, with the check of `rule-sprint` (a child of `rule-documentation`) between them, in this order: the harness files are checked against their pages, the sprint file against its page, then the pages (case 227)."
    change: sprint --check joins make lint between render --check and lint (case 233.1)
  - slug: estimate-harness-pipeline
    set: {status: pending, method: "make test-harness over tests/test_render.py and tests/test_lint.py; the live reading of make lint by hand"}
    change: the Criterion replaced whole — make lint with three steps (case 233.1)
```

```tasks
- [ ] update `rule-harness`: one `replace` in Purpose, `change`
- [ ] update `estimate-harness-pipeline`: `set: {status: pending, method}`, `change`
- [ ] read `estimate-harness-pipeline`: `make test-harness`, `make lint` after the build of 227
```

### Case 233.2 — `rule-retro`: the page lines are not debt

> **given:**
> Retro runs before the librarian; `generate` and `render` tick the page and render lines after it (case 226).
> **＋** `estimate-retro-loads` is the old shape — a recut with `set.method`.

> **when:**
> The person invokes `/retro`, and the agent counts the unticked `tasks` of the Spec.

> **then:**
> A `create`, `update` or `defer` line of a page and a `guppi render` line are listed as waiting for the librarian and end in none of the four ways; every other unticked line is debt, as today.
> **－** Nothing else in Retro changes.

```then
update:
  - slug: rule-retro
    replace:
      - old: "the unticked boxes per Case;"
        new: "the unticked boxes per Case — a `create`, `update` or `defer` line of a page and a `guppi render` line listed as waiting for the librarian, who ticks them (case 226), not as debt;"
    change: the page and render lines of the Spec wait for the librarian and are not debt at Retro (case 233.2)
  - slug: estimate-retro-loads
    set: {status: pending, method: "one reading by hand at the first /retro, recorded in the estimate line"}
    change: the Criterion replaced whole — the page and render lines are not debt (case 233.2)
```

```tasks
- [ ] update `rule-retro`: one `replace` in the Render, `change`
- [ ] update `estimate-retro-loads`: `set: {status: pending, method}`, `change`
- [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
- [ ] read `estimate-retro-loads`: the `/retro` of this session
```

### Case 233.3 — the Rule-class files: the sprint and the tick

> **given:**
> `index.md` §1 describes `sprint.md` through `## Backlog` and says in §2 "ticked in Work Mode"; `glossary.md` has the Sprint row; `case-schema.md` says "Work Mode ticks the boxes".
> **－** Defer 230 is about the definitions of §1 and §6, not these lines.

> **when:**
> Someone reads the three files after Work Mode.

> **then:**
> `index.md`: the `sprint.md` row names Milestones and Backlog; §2 reads "ticked in Work Mode; the page and render lines by `generate` and `render` (case 226)". `glossary.md`: the Sprint row — Milestones in order, a Backlog without a turn. `case-schema.md`: the same correction as in 224.2.

```then
update:
  - slug: index
    file: vault/wiki/index.md
    change: the sprint.md row names Milestones and Backlog; §2 — the page and render lines ticked by generate and render (cases 229, 226, 233.3)
  - slug: glossary
    file: vault/wiki/glossary.md
    change: the Sprint row — Milestones in order, a Backlog without a turn (cases 229, 233.3)
  - slug: case-schema
    file: vault/wiki/case-schema.md
    change: Work Mode ticks the lines on code, tests, migrations and readings; generate and render the page and render lines (cases 226, 233.3)
```

```tasks
- [x] update `index.md`, by hand
- [x] update `glossary.md`, by hand
- [x] update `case-schema.md`, by hand
```

### Case 233.4 — `rule-carry-over`: the same Deferred paragraph

> **given:**
> The Render of `rule-carry-over` repeats the `/carry` paragraph of `rule-brief`; `estimate-carry-over-writes` is `pending`, waits for a live `/carry`, and its Criterion says nothing of Deferred.

> **when:**
> The agent calls `carry` after the fork.

> **then:**
> Deferred of the brief is the previous brief's list plus the `defer` items of this Spec by slug, less the targets the sprint page names.
> **－** The Criterion of the Estimate stands as it is.

```then
update:
  - slug: rule-carry-over
    replace:
      - old: "the previous brief's list as it stands plus the `defer` items of this Spec by slug;"
        new: "the previous brief's list as it stands plus the `defer` items of this Spec by slug, less the targets the sprint page names (case 229.4);"
    change: the /carry brief leaves out a target the sprint page names (case 233.4)
  - slug: estimate-carry-over-writes
    set: {status: pending}
    sections:
      Criterion: |
        Given:
        The hook `guppi spec` on `PostToolUse` of `ExitPlanMode` wrote the Spec and printed the fork into the context: go on — Work Mode — or conserve until the next session.
        **＋** The agent asked the person which of the two and got "conserve".
        **＋** `guppi materialize` knows a conserved unit by the file `carry.md` in the session folder (case 190.3) — by its presence, not its content.
        **－** The person does not type `/carry`; the path of the skill is the agent's call on `PreToolUse Skill`.

        When:
        The agent calls the skill `carry` after the person's answer at the fork.

        Then:
        The skill reads the tree; when it holds changes outside the session folder and `vault/wiki/brief.md`, it stops and says: work was done, the ordinary exit applies.
        **＋** Otherwise it rewrites `brief.md` — that is the conservation: the next session starts from it.
        **＋** It puts `carry.md` into the session folder — one line, a flag for `materialize`, not a document; the session that finishes the work deletes it.
        **＋** It runs `make style` and commits `vault/raw/` and `vault/wiki/brief.md`.
        **－** It runs no Work Mode, `/retro`, `/handoff`, librarian, `materialize`, `generate`, `cleanup` or `render`; it writes no page of `vault/wiki/` but the brief.
        **－** The work stays sequential, session after session: one conserved Spec, no parallelism.
        **－** `.claude/skills/carry/SKILL.md` equals the Render of the page; it is not edited by hand.
    change: the Render changed under it — the Deferred paragraph; the Criterion stands as it was (case 233.4)
```

```tasks
- [ ] update `rule-carry-over`: one `replace` in the Render, `change`
- [ ] update `estimate-carry-over-writes`: `sections: Criterion` as it stands, `change`
- [ ] `uv run guppi render`: `.claude/skills/carry/SKILL.md`
```

### Case 233.5 — `estimate-sprint-migration-lint-clean`: a word on the page

> **given:**
> The Criterion describes the sprint page through `## Backlog` with the Slices; 229.1 moves them under `## Milestones`.

> **when:**
> Someone reads the Criterion after the librarian's run.

> **then:**
> The same text with `## Milestones` for the Slices and a line "`## Backlog` — two plain lines"; the status `pending` as it was.

```then
update:
  - slug: estimate-sprint-migration-lint-clean
    set: {status: pending}
    sections:
      Criterion: |
        Given:
        Items 1–4 of the Definition of done are today what `make lint` checks: fields by schema, Estimate pages present, no broken ref, no orphan, no status contradiction.
        **＋** Lint counts the 62 findings of the Decision pages of Cases 1–28 today.

        When:
        Someone reads `make lint` at the close of the sprint.

        Then:
        `make lint` exits 0: no finding in any category, `unmigrated` included — the old Estimate shape is gone, the counter at zero; the one exception is `unread` on the Estimates of the sprint page itself not yet read at that moment.
        **＋** The page `entity-sprint-migration` exists: an Entity MOC, `purpose` the goal of the sprint; `## Purpose` the goal and "open since 2026-09-09"; `## Milestones` — `### Slice 3b`: `rule-work-mode`, `rule-subagent-guppi`; `### Slice 4`: the item of the promise of 209.3; `### Slice 5`: the items of the Estimates of 209.2–209.4 and `rule-spec-box`; `## Backlog` — two plain lines (case 229.1); `## Closed` — Slices 0–3d in one paragraph, 3d closed by session 1955, the recut remainder 42 by lint.
        **－** Item F7 is not done on its own: today's `sprint.md` is replaced by the first render.
    change: the Slices under Milestones, a Backlog of two plain lines (cases 229.1, 233.5)
```

```tasks
- [ ] update `estimate-sprint-migration-lint-clean`: `sections: Criterion`, `change`
```

## Case 234 — `entities/schema.yaml`: the sections of the sprint page

> **context:**
> `entities/schema.md` names `## Milestones`, `## Backlog` and `## Closed` as the sections of the sprint page (case 229.1). Lint compares the prose of a schema with its `schema.yaml` (`schema-prose`) and printed, in Work Mode: `schema.md names section ## Milestones, schema.yaml does not`. Case 229.1 named the `.md` alone; the yaml is its own Rule-class file, `entities-schema-yaml`, and is not edited without a ledger line. A fork of Work Mode, brought back as a Case.

> **problem:**
> One lint finding that was not there before Work Mode; a one-line edit of the yaml, unratified.

> **given:**
> Lint reads `schema.yaml` and compares it with `schema.md` under `schema-prose`.

> **when:**
> Someone runs `guppi lint` after the edit.

> **then:**
> `entities/schema.yaml`: `body.optional` is `## How it works`, `## Milestones`, `## Backlog`, `## Closed`; the `schema-prose` finding is gone — the three sections as three rows of the `.md` table, so the prose names each.
> **－** Nothing else in the schema changes.

```then
update:
  - slug: entities-schema-yaml
    file: vault/wiki/entities/schema.yaml
    change: the three sections of the sprint page under body.optional (case 234)
```

```tasks
- [x] update `entities/schema.yaml`, by hand; the row of `schema.md` split into three
```

## Deferred

## Case 230 — the definitions of Entity, Rule and Estimate

> **context:**
> `entity-sprint-migration` is the first live Entity page, and the vault says in no one place what an Entity is, how it is cut, what it carries and how it stands to a Rule and an Estimate — `index.md` §1 and §6, `glossary.md` and the three schemas each hold a piece. Session 1119 discussed it at length: six candidate definitions, three worked scenarios, the edge between an Entity and a Rule, the kinds of an Estimate, where a user's knowledge goes, whether the model holds without product code. The record is `raw/2026-09-17/1119/categories-discussion.md`. The person wants to think more; the definitions come back as a Case.

> **problem:**
> The agent reads an Entity page without a definition to hold it against and fills the gap by judgment; the person's objection stands that the development categories may be one set among several, not the universal one.

```then
defer:
  - slug: index
    file: vault/wiki/index.md
    type: file
    purpose: "the definitions of Entity, Rule and Estimate for development — or the category set as data of the project; from raw/2026-09-17/1119/categories-discussion.md; the next session"
```

## Case 231 — Slice 3b: `rule-work-mode`, `rule-subagent-guppi`

> **context:**
> `rule-work-mode` and `rule-subagent-guppi` are placeholders, `draft`, `deferred_by: decision-case-183, -206, -218`, `deferred: 15 times since case 29`, the first open milestone of the sprint page. Case 218 put Slice 3b into a session of its own; this session took the ledger Insight, the Spec ticks, the sprint as milestones, the definitions of the categories, and has no room for the Plan Mode of a Slice. By case 229 the two stand in the current milestone of `sprint.md` and reach the next Frontier from there, not from the brief's Deferred list.

> **problem:**
> Work Mode needs a session of its own, as 206 and 218 said; the next one.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: "Work Mode: the Spec as tasks with code, the ticked boxes in spec.md, the test of each Estimate written first and turned green; who ticks which task line — generate and render tick the page and render lines since case 226, the rest is the agent's; the Plan Mode of the next session, the first open milestone of the sprint page"
  - slug: rule-subagent-guppi
    type: rule
    purpose: "what a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case; with rule-work-mode, the next session"
```

## Case 232 — `rule-spec-box`

> **context:**
> `rule-spec-box` is the placeholder of case 207 — a conserved Spec run in a worktree on its own branch, Work Mode only, the librarian once after the merge — `draft`, `deferred_by: decision-case-207, -219`, lint `missing field kind`, `missing field estimates`, `orphan`; it stands in Slice 5 of the sprint page, after Slice 3b.

> **problem:**
> The Spec box presupposes Work Mode; it waits for Slice 3b.

```then
defer:
  - slug: rule-spec-box
    type: rule
    purpose: "the Spec box of case 207 — a conserved Spec run in a worktree on its own branch, Work Mode only, the librarian once after the merge; its open questions as 207 left them: the skill and its conditions, the ledger hook and guppi gate inside a worktree, the cut of a Spec into boxes, a third end of a session, subagent or session; after Slice 3b"
```
