<!-- approved 12:43:37 · session c27cd9be -->

# Spec — 2026-09-20, hi 0958

## Case 264 — `estimate-generate-renames`: the History line of 262, and a bare `[[slug]]` in the Spec

> **context:**
> `estimate-generate-renames` is a QA Estimate under `rule-page-generation`, `pending`; its reading — the librarian's run on Case 261 — stands as the line of 09:38:37 in the ledger of `raw/2026-09-20/0740`, not yet applied, and the next walk applies it before the entries of this session (F2). Case 262 took the two bare `[[decision-case-N]]` out of the Criterion, but the `change` text of the same Case carried the placeholder without a code span, and `generate` wrote it into History verbatim — lint raises `ref: body names decision-case-N` again. `generate.replace` does not touch History, so the line cannot be repaired through `replace`; the precedent is 130.1 — the History line edited by hand as a one-off migration, recorded by an `update` with `change`. An `update` of an Estimate replaces its Criterion with the Case's text unless the item writes `sections: Criterion` itself, and sets `pending` unless the item writes a status (case 204). `rule-prespec` stands `draft`; its Estimates are `estimate-prespec-checks-the-plan` (`passed`, pytest) and `estimate-prespec-reconciles` (`pending`, its first live reading is F3 of this session, before Work Mode). The same class of finding was cured three times on Decision pages and on a lesson (130.1, 140, 160); there is no guard before the Spec — `prespec --check` checks the form of the items, not the text of the strings. `lint` and `rule-page-generation` are not touched.

> **problem:**
> The finding stands until the History line changes; and nothing stops a fifth time — a bare `[[slug]]` in any text of the Spec (`change`, `purpose`, `sections`, the blockquotes) reaches a page unchecked.

> **given:**
> `guppi lint` reads every `[[slug]]` in the body of a page as a link and strips code spans before the search; a slug no live or archived page carries is a finding of class `ref`.
> **＋** `guppi generate` applies `sections: Criterion` and `set` of an Estimate `update` as written; `materialize` lifts the Criterion from the Case and sets `status: pending` only when the item writes neither (case 204).
> **＋** The walk of `generate` goes through the session folders in order: the ledger of 0740, then 0958.
> **－** `generate.replace` does not touch `## History`; a History line is edited by hand, a one-off migration (case 130.1).

### Case 264.1 — the History line of 262 in a code span

> **when:**
> `guppi lint` reads `estimate-generate-renames` after the librarian's run of this session.

> **then:**
> No `ref` finding on the page: the placeholder in the History line of 262 stands in a code span, the rest of the line is the text signed in 262.
> **＋** The Criterion is the text of 262 verbatim; `method`, `purpose`, `origin` and Result do not change.
> **＋** The status of the page is the one the reading of 09:38:37 in 0740 leaves: `passed`; no new reading is taken.
> **－** `rule-page-generation`, `lint` and `log.md` are not touched.

```then
update:
  - slug: estimate-generate-renames
    set:
      status: passed
    sections:
      Criterion: |
        Given:
        An `update` item may carry `rename: <new slug>` beside `set`, `sections`, `replace`, `change`; the ledger line names the old slug.
        **＋** The id of a page is its filename; the new slug carries the same category prefix.
        **＋** `origin` is never rewritten; the archive, `raw/`, `log.md` and `brief.md` are not pages.
        **－** A taken slug — live or archived — and a foreign prefix: an error on a `create`, the same on a `rename`.

        When:
        `guppi generate` applies an `update` whose item carries `rename`.

        Then:
        The file `wiki/<category>/<old>.md` becomes `<new>.md`; the page's History gets "renamed from `<old>` · `[[decision-case-N]]`"; the item's `set`, `sections` and `replace` apply to the new file.
        **＋** In every live page of `wiki/` — Decision pages included — every `[[old]]` becomes `[[new]]`, every `REF_FIELDS` value holding the old slug becomes the new one, and the old slug as a whole word in the body outside `## History` and `## Result` becomes the new one; every page touched, Decision pages excepted, gets the History line "ref `<old>` → `<new>` · `[[decision-case-N]]`".
        **＋** The Decision page of the Case is written as today — by the slug of the ledger line, before the entries; the walk retargets its link like any other.
        **＋** The order of application is the order of the yaml: an `update` of the same page from an earlier Case lands on the old file, and the `rename` moves it with the page.
        **－** A taken slug or a foreign prefix: the entry is `failed`, nothing is moved.
        **－** `origin`, `## History` and `## Result` of any page, the archive, `raw/`, `log.md` and `brief.md` are untouched; `guppi sprint` redraws `sprint.md` from the sprint page.
    change: "the History line of 262 quoted by hand — its placeholder `[[decision-case-N]]` in a code span — a one-off migration; the Criterion the text of 262; the status the one the reading of 09:38:37 in raw/2026-09-20/0740 leaves (case 264.1)"
```

```tasks
- [x] by hand: `vault/wiki/estimates/estimate-generate-renames.md`, the History line of 262 — `[[decision-case-N]]` in backticks, a one-off migration
- [x] update `estimate-generate-renames`: `sections: Criterion` the text of 262 verbatim, `set: {status: passed}`, `change`
```

### Case 264.2 — pre-spec: a bare `[[slug]]` in the plan file

> **given:**
> The conditions of the parent.
> **＋** `prespec --check` prints one line per finding on the plan file and exits 1 when it printed any; `tests/test_prespec.py` fixes every class of finding.

> **when:**
> The person invokes `/pre-spec`, and `guppi prespec --check <plan> --session <id>` reads the plan file.

> **then:**
> One line `case N: [[slug]] outside a code span names no page` is printed for every `[[slug]]` in the plan file outside a code span — in the blockquotes and in the strings of the `then` blocks — that has no live or archived page.
> **＋** A slug a `create` of the same plan carries, and a hub file of `wiki/` by its stem or its path, are not a finding.
> **＋** One line per slug and Case, however many times it stands.
> **－** A `[[slug]]` inside backticks, and inside a fenced block tagged other than `then`, is not read.
> **－** `lint` does not change: the finding on the page stands when the text reached it anyway.

```then
create:
  - slug: estimate-prespec-catches-bare-wikilinks
    type: estimate
    ref: rule-prespec
    kind: QA
    purpose: A bare `[[slug]]` in the plan file that names no page is a finding of pre-spec before the Spec is approved
    method: pytest tests/test_prespec.py, the tests of check_bare_links
    tags: [session, workflow, harness, tests]
update:
  - slug: rule-prespec
    replace:
      - old: "for every `create` of an Estimate whose `ref` names no live rule or entity (case 203.1); an Estimate has its own line and its own item (case 189)."
        new: "for every `create` of an Estimate whose `ref` names no live rule or entity (case 203.1), and for every `[[slug]]` outside a code span in the plan — in the blockquotes and in the strings of the `then` blocks — that names neither a live or archived page, nor a slug a `create` of the same plan carries, nor a hub file of `wiki/` (case 264.2); an Estimate has its own line and its own item (case 189)."
    change: "the Render names the finding of --check on a bare `[[slug]]` in the plan file that names no page; the guard of case 264.2"
```

```tasks
- [x] `guppi/prespec.py`: `check_bare_links` — code spans stripped, wikilinks found in the blockquotes and in the strings of the `then` blocks, each slug checked against `wiki/`, `archive/`, the `create` items of the plan and the hub files; called from `check`
- [x] `tests/test_prespec.py`: a bare slug — one line; in backticks — none; a slug of a `create` of the plan — none; a hub file — none; one slug twice — one line; a fenced block tagged other than `then` — none
- [x] create `estimate-prespec-catches-bare-wikilinks`, ref `rule-prespec`, kind `QA`
- [x] update `rule-prespec`: `replace` in the Render — the list of what `--check` prints gains the bare `[[slug]]`; `estimates` filled by `generate`
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [x] read `estimate-prespec-catches-bare-wikilinks`: pytest
```

## Case 265 — seven Estimates with the word `pre-task`: three by the word, four by a recut

> **context:**
> Case 261 renamed `rule-pretask` to `rule-prespec` and moved the word in the code, the tests and the prose of the live pages; the Criteria and `method` of seven Estimates it left to their next `update`. On three the word stands in text of the shape of 193: `estimate-hi-writes-frontier` (`passed`, under `rule-skill-hi`) — its `method` names `guppi pretask --check` and `tests/test_pretask.py`, its Given "`/pre-task` fails on an open line"; `estimate-generate-writes` and `estimate-generate-walks-dates` (`passed`, under `rule-page-generation`) — "`pretask` does not change" and the slug `-pretask-reconciles`. On four the Criterion is in the shape before 193, with `### case N` blocks: `estimate-event-log-records` (`rule-event-log`; the base text plus 111.1, 125, 136.1), `estimate-retro-commit-gates` (`rule-retro-commit`; the base plus 169.1, 180), `estimate-plan-mode-verified` (`rule-plan-mode`, the cross-cutting Estimate of the MOC; one paragraph), `estimate-documentation-completes` (`rule-documentation`; the base plus 73.8, 89.1, 90.3, 100.2, 147.5); on the first three `method` is a section, not a field. Touching one of them is a recut by 211: one Criterion of Given/When/Then in place of the blocks, `method` as a field, `pending` and a reading — one sub-case per page. No other Estimate of these rules is touched.

> **problem:**
> Three pages point at a file, a command and a slug that no longer exist; four cannot be repaired by the word, only by a recut, and the person takes all seven now. The recut folds the blocks into one promise: the lines on a Render, a `contract` or "gets a block" are the bookkeeping of those Cases and do not enter the Criterion.

> **given:**
> `generate` applies `sections: Criterion` and `set` of an item as written; `materialize` lifts the Criterion from the `given`, `when` and `then` of the Case and sets `pending` when the item writes neither (case 204); `generate` refuses a recut without `method` (case 211).
> **＋** `guppi lint` counts the pages with `### case N` blocks as `unmigrated`, and every `pending` page as `unread`.
> **－** Result, History and `origin` are not rewritten.

> **when:**
> The librarian applies the yaml of this session, and `guppi lint` reads the seven pages.

> **then:**
> No `pre-task`, `pretask` or `test_pretask` in the Criterion and `method` of the three pages of the shape of 193: `estimate-hi-writes-frontier` — `method` names `guppi prespec --check` and `tests/test_prespec.py`, Given "`/pre-spec` fails on an open line"; `estimate-generate-writes` and `-walks-dates` — "`lint`, `materialize` and `prespec` do not change" and `-prespec-reconciles`.
> **＋** The rest of the text is the one signed before; the status stays `passed`, the Result stands.
> **＋** The four pages — one sub-case each below; `unmigrated` reads 25.
> **－** `rule-skill-hi`, `rule-page-generation`, the code and the tests are not touched.
> **－** The Criterion of `estimate-hi-writes-frontier` is replaced whole again by 268.2 in the same walk; the word leaves either way, and 268.2 sets its `method`.

```then
update:
  - slug: estimate-hi-writes-frontier
    set:
      status: passed
      method: "one reading by hand at the first /hi of the next session, written into the estimate line; unit: the frontier findings of guppi prespec --check in tests/test_prespec.py"
    sections:
      Criterion: |
        Given:
        `/hi` puts `sprint.md` into the context on the first turn; the Frontier is written to `raw/<date>/<hi HHMM>/frontier.md`, one line per item; `/pre-spec` fails on an open line.
        **＋** `sprint.md` shows the current milestone whole and a later one as one line.

        When:
        The person invokes `/hi`, and the agent assembles the Frontier.

        Then:
        The items of the current milestone are Frontier lines; a later milestone, the Backlog and Closed are not.
        **＋** The other sources as today: an unfinished plan first, a hand edit from `Render:`, a failed pull and an unavailable `gh`, a `failed` reading and a lesson of the Tail, the readings `pending`, the flags of the brief; an item the person adds is a new line.
        **＋** Each line `- [ ] F<n> — <title> · <source>`; closed as `[x] … · case N`, `[x] … · work` or `[-] … · defer case N`.
        **－** A decision line of the Tail is not an item.
    change: "the word moved: /pre-task → /pre-spec in the Criterion, guppi prespec --check and tests/test_prespec.py in method; the promise and the reading unchanged, passed kept (case 265)"
  - slug: estimate-generate-writes
    set:
      status: passed
    sections:
      Criterion: |
        Given:
        `guppi generate` applies `set` to the frontmatter and `sections` as whole replacements; the failure of one entry touches no other (`estimate-generate-fails-alone`).
        **＋** The field `method` is one line; `## Method` of the old shape is the same text as a section.
        **＋** The tests in `tests/test_generate.py` fix the behaviour; the live reading is the librarian's run of this session.
        **－** `lint`, `materialize` and `prespec` do not change.

        When:
        The librarian applies the yaml of this session after the build of 211.1.

        Then:
        `estimate-generate-writes`, `-generate-walks-dates`, `-lint-catches`, `-prespec-reconciles`, `-materialize-assembles` carry a `method` field with the text of their `## Method` sections in one line; `## Context` and `## Method` are dropped.
        **＋** `unmigrated` reads 34 after the run: these five, `estimate-prespec-hook-gates` (213.2), `estimate-permissions` (215) and `estimate-brief-written` (209.6) leave the old shape; `estimate-documentation-completes` keeps its `### case` blocks.
        **－** The Criterion of these pages does not change; no `pending` is set — except on `estimate-generate-writes`, whose Criterion 211.1 changes.
    change: "the word moved: the module pretask → prespec and the slug -pretask-reconciles → -prespec-reconciles in the Criterion; the promise and the reading unchanged, passed kept (case 265)"
  - slug: estimate-generate-walks-dates
    set:
      status: passed
    sections:
      Criterion: |
        Given:
        `guppi generate` applies `set` to the frontmatter and `sections` as whole replacements; the failure of one entry touches no other (`estimate-generate-fails-alone`).
        **＋** The field `method` is one line; `## Method` of the old shape is the same text as a section.
        **＋** The tests in `tests/test_generate.py` fix the behaviour; the live reading is the librarian's run of this session.
        **－** `lint`, `materialize` and `prespec` do not change.

        When:
        The librarian applies the yaml of this session after the build of 211.1.

        Then:
        `estimate-generate-writes`, `-generate-walks-dates`, `-lint-catches`, `-prespec-reconciles`, `-materialize-assembles` carry a `method` field with the text of their `## Method` sections in one line; `## Context` and `## Method` are dropped.
        **＋** `unmigrated` reads 34 after the run: these five, `estimate-prespec-hook-gates` (213.2), `estimate-permissions` (215) and `estimate-brief-written` (209.6) leave the old shape; `estimate-documentation-completes` keeps its `### case` blocks.
        **－** The Criterion of these pages does not change; no `pending` is set — except on `estimate-generate-writes`, whose Criterion 211.1 changes.
    change: "the word moved: the module pretask → prespec and the slug -pretask-reconciles → -prespec-reconciles in the Criterion; the promise and the reading unchanged, passed kept (case 265)"
```

```tasks
- [x] update `estimate-hi-writes-frontier`: `sections: Criterion` verbatim with `/pre-spec`, `set: {method: …prespec…, status: passed}`, `change`
- [x] update `estimate-generate-writes`: `sections: Criterion` verbatim with `prespec`, `-prespec-reconciles`, `set: {status: passed}`, `change`
- [x] update `estimate-generate-walks-dates`: the same
- [x] `make lint` after the librarian: no `pre-task`/`pretask` in the Criterion and `method` of the seven pages; `unmigrated: 25`
```

### Case 265.1 — the recut of `estimate-event-log-records`

> **given:**
> The hooks `uv run guppi event <name>` and `uv run guppi gate` run through a pipe with a JSON payload; `session_id` is the stamp.
> **＋** `raw/<date>/event_log.md` is in `.gitignore`; the ledger hook reads the session's `hi` from it.

> **when:**
> A session starts, a tool call completes, the person submits a prompt, the agent calls a skill through `Skill`.

> **then:**
> After the start and one tool call the log carries a `session-start` line with the session's stamp and a `tool` line after it.
> **＋** On `/hi` (trimmed, or `/hi …`), when no `hi` of this stamp follows its first `session-start`: the line `- HH:MM:SS <stamp> hi` and stdout `hi: HH:MM:SS <stamp> → raw/<date>/<HHMM>/`; a second `/hi` writes nothing, stdout `hi: already recorded at HH:MM:SS → raw/<date>/<HHMM>/`; any other prompt is silent; exit 0 either way, an error on stderr only.
> **＋** A call of `pre-spec`, `retro` or `handoff` through `Skill` that the gate lets through appends `- HH:MM:SS <stamp> <mark>` — `prespec`, `retro`, `handoff` — in the form `guppi event` writes; a refusal writes no line; `hi` and other skills get no mark.
> **＋** `git check-ignore` reports the file ignored; a hook invocation with piped stdin exits 0 and finishes under 2 s.

```then
update:
  - slug: estimate-event-log-records
    set:
      status: pending
      method: "pytest in tests/test_event.py and tests/test_gate.py with piped JSON payloads against a temp vault; the git-ignore and timing readings once by hand, through a pipe, written into the estimate line"
    change: "the recut to the shape of case 193: the base text and the blocks 111.1, 125, 136.1 folded into one Criterion, the mark pretask now prespec, method as a field; pending for the reading (case 265.1)"
```

```tasks
- [x] update `estimate-event-log-records`: `set: {status: pending, method}`, `change`; the Criterion lifted from this sub-case
- [x] read `estimate-event-log-records`: pytest tests/test_event.py tests/test_gate.py; live — this session's log (`hi` 09:58:48, the mark `prespec` on `/pre-spec`), `git check-ignore`, the time through a pipe
```

### Case 265.2 — the recut of `estimate-retro-commit-gates`

> **given:**
> `guppi gate` runs on `PreToolUse` for `Skill` and on `UserPromptSubmit` for a typed `/pre-spec`, `/retro` or `/handoff`, with or without arguments; a refusal is exit 2 with the reason on stderr, and the client blocks the call.

> **when:**
> The gate receives such a call or prompt.

> **then:**
> `handoff`: a dirty tree — exit 2, the reason "commit first"; a clean tree — exit 0; live, the first `/handoff` from Retro on a dirty tree is refused and passes after the commit.
> **＋** `/retro`: with a `hi` but no `spec.md` in the session's folder, no plan file named by the event log and no `- decision[`, `- estimate[` or `- lesson[` line in the window — exit 2, "gate: /retro refused — nothing to review: no Spec and no ledger line in raw/<date>/<HHMM>/. Ratify a Case or write a reading or a lesson first, then type /retro again.", on the `Skill` path "…then call /retro in the next reply."; otherwise the check of the Spec against the session's ledger — N items without a line — exit 2, "gate: /retro refused — N item(s) of the Spec have no ledger line (case A). Ask the agent to end its reply with the LEDGER block, then type /retro again".
> **＋** Letting through, on either path it writes the same mark `prespec`/`retro`/`handoff` into the event log; a refusal writes no mark.
> **＋** Any other prompt or skill, `/hi` included — exit 0, no output, no mark; without `hi` — nothing to check, exit 0.
> **－** `guppi event prompt` does not change and does not fail.

```then
update:
  - slug: estimate-retro-commit-gates
    set:
      status: pending
      method: "pytest in tests/test_gate.py with piped payloads against a temp repository; the live reading once by hand"
    change: "the recut to the shape of case 193: the base text and the blocks 169.1, 180 folded into one Criterion, /pre-task and pretask now /pre-spec and prespec, method as a field; pending for the reading (case 265.2)"
```

```tasks
- [x] update `estimate-retro-commit-gates`: `set: {status: pending, method}`, `change`; the Criterion lifted from this sub-case
- [x] read `estimate-retro-commit-gates`: pytest tests/test_gate.py; live — the `/retro` and `/handoff` of this session
```

### Case 265.3 — the recut of `estimate-plan-mode-verified`

> **given:**
> The children of `rule-plan-mode` check one mechanism each; this one checks that the two verification points hold across Plan Mode.
> **＋** The vault's answer before a `create` without a `ref` enters the `context` of the Case (case 188).

> **when:**
> A Case proposes a `create`, and later the person approves the plan.

> **then:**
> A `create` for a page whose `purpose` an index line already carries is named in the `context` of the Case before ratification.
> **＋** The pre-spec hook fires before the plan is written — and the plan is still written.

```then
update:
  - slug: estimate-plan-mode-verified
    set:
      status: pending
      method: "make test-plan-mode, the pipeline over tests/test_spec.py and tests/test_prespec.py; the flagging one live reading by hand, written into the estimate line"
    change: "the recut to the shape of case 193: the paragraph as Given/When/Then, the flag in context by 188, the pre-spec hook, tests/test_prespec.py in method as a field; pending for the reading (case 265.3)"
```

```tasks
- [x] update `estimate-plan-mode-verified`: `set: {status: pending, method}`, `change`; the Criterion lifted from this sub-case
- [x] read `estimate-plan-mode-verified`: `make test-plan-mode`; live — the approval of this session's plan after `/pre-spec`; 264.2, a `create` with the vault's answer in `context`
```

### Case 265.4 — the recut of `estimate-documentation-completes`

> **given:**
> The librarian's frame is the Render of `rule-documentation`; its inputs are three: the `handoff.md` of the session's folder, every `materialize.yaml` the walk named, and `tags.md`; the index lines are the Greps `rule-index-check` and `rule-synthesis` name.
> **＋** The librarian works in a clean context; the person is gone.

> **when:**
> `librarian-guppi` starts after the handoff and runs to the end.

> **then:**
> `make test-documentation` — materialize, generate and cleanup as one pipeline — is green.
> **＋** Live, after the run: every decision line of the session's ledger has a Decision page and its target page; no page exists that no ledger line produced.
> **＋** It read only `handoff.md`, the yamls, the four index lines and `tags.md`, plus the wiki pages it names in the report with one of the four reasons of its frame (same or near; a candidate cluster; a script's error; a fact for the brief) and the outcome; no ledger, Spec, plan, Decision page or archive file (the Makefile, `guppi/` and `tests/` are the scripts' own and may be read).
> **＋** It edited no yaml entry beyond the marks and the entries of the index check and the synthesis; its commands are in `event_log.md`; its commit is separate from the session's; it did not stop to ask.
> **＋** After `cleanup` and before the brief it runs `uv run guppi render`, then `uv run guppi sprint`; every line on their stderr is a flag; a file the render could not write is left to the next session start; `make lint` then passes its `render --check` step.
> **＋** After the brief and before the close it runs `uv run guppi archive`; every line on its stderr is a flag; the units it moved and the units it kept, with the reason, go into the report; the session of the run — the latest `<HHMM>/` folder of the run day, else the nearest date back — is skipped, across midnight too; the commit picks the move up.
> **－** An instruction of the handoff to repair a yaml entry, or to read the ledger, a Spec, a Decision page or the archive, is refused and named in the report — what was asked and why; the refusal does not stop the run.
> **－** The ban on reading `vault/archive/` stays.

```then
update:
  - slug: estimate-documentation-completes
    set:
      status: pending
    change: "the recut to the shape of case 193: the base text and the blocks 73.8, 89.1, 90.3, 100.2, 147.5 folded into one Criterion, pre-task gone from it; pending for the reading (case 265.4)"
```

```tasks
- [x] update `estimate-documentation-completes`: `set: {status: pending}`, `change`; the Criterion lifted from this sub-case
- [ ] read `estimate-documentation-completes`: `make test-documentation`; live — the librarian's run of this session, read in the next
```

## Case 266 — `estimate-materialize-assembles`: the `purpose` of a defer is its own key, not a field of the target page

> **context:**
> Case 238 deferred `insight-workflow-code-live-before-the-page-it-reads` with a `defer` block carrying `type` and `purpose`, as `case-schema.md` asks. Since 214.1 `materialize` lifts the keys of an item by the `schema.yaml` of the target's category: a key the schema does not name as a field is `unknown` and never reaches the page. An Insight has no `purpose` field (it has `pattern`), so the `purpose` of the defer became `unknown: [purpose]` and then `incomplete: [purpose]` — the "defer without a purpose" of the brief, though the Spec carries it. `generate.defer` writes `purpose` into a placeholder page only and sets `deferred_by` on an existing one; `deferred_of` reads `purpose` from `fields` for the `## Deferred` section of the Decision page — `decision-case-238` has none. For a Rule and an Entity `purpose` is a schema field and the same line of the Criterion does not break them; the defect shows on an Insight only. `estimate-materialize-assembles` (`passed`) carries that line of 214.1; the other eight Estimates of `rule-materialize` are not touched, and the body of the rule does not describe the lift by the schema.

> **problem:**
> `type` and `purpose` are keys of the `defer` itself, not fields of the target; the check by the target's schema loses them on an Insight, and the Decision page stays without `## Deferred`. One line of the Criterion, `materialize.py` and a test.

> **given:**
> `materialize` lifts the `fields` of a `create` and a `defer` entry by the `schema.yaml` of the target's category; a key outside the schema is `unknown`, never written to the page (case 214.1).
> **＋** `generate.defer` takes `purpose` from `fields` for a placeholder page; `deferred_of` for the `## Deferred` of the Decision page (case 186.1).
> **＋** `tests/test_materialize.py` fixes the behaviour; the live reading is the librarian's run.

> **when:**
> `guppi materialize` lifts a `defer` record against its Spec.

> **then:**
> `type` and `purpose` of a `defer` item reach the `fields` of the entry whatever the target's category — Rule, Entity, Insight; a `purpose` the item lacks is `incomplete: [purpose]`, as today.
> **＋** The other keys of a `defer` item go by the target's schema: one the schema does not name is `unknown`, and the entry applies.
> **＋** The line of 214.1 in the Criterion says so; the rest of the Criterion is the text signed before.
> **－** A `create` does not change; `generate`, `decision-case-238` and the schema of an Insight are not touched.

```then
update:
  - slug: estimate-materialize-assembles
    set:
      status: pending
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
        One entry per record line, in ledger order: `case`, `kind`, `category` from the slug prefix, `slug`, `ref`, `source`, `supersedes`, `tags`, `origin`, `line`, `text`, `decision`; from the `then` block — `fields`, `sections`, `replace`, `change`, `rename`, `impact`; what the block lacks is `incomplete`, never invented (case 258.3).
        **＋** Only the keys the category's `schema.yaml` names as fields reach `fields` of a `create` entry, and of a `defer` entry but for `type` and `purpose` — the defer's own keys, which reach `fields` whatever the target's category, for the placeholder page and for the `## Deferred` of the Decision page; the structural keys of the item go where they go — `ref` to the entry, `sections`, `tags`, `file`; a key that is neither is marked `unknown: [key]` on the entry, printed by `--show`, never written to the page, and the entry applies; `incomplete` is counted by `REQUIRED` as before, and a `defer` without `purpose` is `incomplete: [purpose]` (cases 214.1, 266).
        **＋** An Estimate has its own line and its own entry; the `ref` of the line is the Estimate itself.
        **＋** An `update` entry for an Estimate carries `sections.Criterion` — the text the item wrote under `sections: Criterion` itself, else the `given`, `when` and `then` of its Case verbatim with their operands as `Given:`, `When:`, `Then:` — replacing what stood there, and `set: {status: pending}` unless the item set a status itself; the `given` of a sub-case is its parent's when it has none of its own.
        **＋** A `create` entry for an Estimate keeps `kind`, `purpose`, `method`, `tags` as fields; its Criterion the same way: the written text when there is one, else the Case's; `## Context` and `## Method` are not written.
        **＋** One decision entry per Case: `decision`, `case_text`, `targets`; a sub-case inherits `context`, `problem`, `recommend`, `given`, never `when`.
        **＋** An `estimate` line for a page of the same ledger is folded into its `create`; for an earlier page it is an `estimate` entry. The `new_tags` of any Case reach the yaml once. An existing yaml is extended, never rewritten.
        **－** An `update` entry carries no `contract`, and no Estimate is derived from it; a `create` carries no `method`, `estimate_kind` or `estimate_slug`; neither `criterion_block`, `case_removed` nor `remove_criterion` is derived.
        **－** The keys `contract`, `estimate_slug`, `estimate_kind` and `method` on a rule's item are ignored: they reach neither the page, nor `incomplete`, nor `unknown`.
        **－** A line the grammar does not parse goes under `unparsed`; the run goes on.
    change: "one line of the Criterion: type and purpose of a defer item reach fields whatever the target's category, the other keys by the schema as 214.1 said; pending for the reading (case 266)"
```

```tasks
- [x] `guppi/materialize.py`: the `defer` branch of `_lift_item` — `type` and `purpose` pass the filter by the schema
- [x] `tests/test_materialize.py`: a defer of an Insight with `purpose` → `fields.purpose`, no `unknown`, no `incomplete`; a stray key on the same defer → `unknown`; a defer without `purpose` → `incomplete: [purpose]`
- [x] update `estimate-materialize-assembles`: `sections: Criterion` whole with the line of 266 in place of 214.1, `set: {status: pending}`, `change`
- [x] read `estimate-materialize-assembles`: pytest; live — the librarian's run of this session
```

## Case 267 — `rule-case-protocol`: `context` opens with the mechanism, the bookkeeping is one sentence

> **context:**
> `context` has to tell a reader who has not opened the pages how the thing works today and where it goes wrong. Today the agent fills it with case numbers, page statuses and lists of Estimates — what the audit needs, not the reader — and the substance drowns. The rule allows it: it asks `context` to hold the state of the pages, the vault's answer and "which Estimates the Case touches and which it does not", without saying that this is one sentence and the mechanism comes first; and its cap of seven sentences per story section, checked by no script, packs a big Case into dense pointer sentences instead of shortening it. The text stands in the Render of `rule-case-protocol` (rendered into `CLAUDE.md`) and in `case-schema.md`; the promise on the form of a Case is `estimate-case-protocol-case-form`, the other three Estimates of the rule are not touched.

> **problem:**
> The rule does not separate the substance from the bookkeeping in `context`, so the agent writes the bookkeeping; and its count of sentences bounds nothing the shape does not already bound. A wording is needed that makes the mechanism come first, limits the pointers, and drops the count.

> **given:**
> `CLAUDE.md` is rendered from `rule-case-protocol`; `case-schema.md` is a Rule-class file, applied by hand in Work Mode.
> **＋** `estimate-case-protocol-case-form` is read by hand from the Cases of a session at its close.

> **when:**
> The agent writes a Case in the chat — at its first showing, when shown again after the owner's change, and with sub-cases.

> **then:**
> `context` opens with the mechanism in plain words — what the thing does today and where it goes wrong — for a reader who has not opened the pages.
> **＋** The bookkeeping — the state of the pages the Case changes, the vault's answer, the Estimates of the rule the Case touches and the ones it does not — is one closing sentence.
> **＋** A case number stands in `context` and `problem` only when the Case is about that case.
> **＋** There is no cap of seven sentences; the shape of a story section bounds its length: `context` the mechanism and one sentence of bookkeeping, `problem` one paragraph, `recommend` the choice, the why and the rejected option in one sentence; no line numbers and no quotation, as today; the other lines of the Criterion of `estimate-case-protocol-case-form` do not change.
> **－** `given`, `when`, `then`, `tasks` and the Spec do not change.

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "`context`, `problem` and `recommend` carry no operand, name the slug of the thing described only, and run to seven sentences each at most: `context` says what the thing is and how it works today, for a reader who has not opened the pages — the state of the pages the Case changes lives here — and names which Estimates of the rule the Case touches and which it does not, with no line numbers and no quotation unless the Case is about one; `problem` says what is wrong, or the question answered, in one paragraph; `recommend` says the choice and why, the rejected option in one sentence."
        new: "`context`, `problem` and `recommend` carry no operand and name the slug of the thing described only; no count of sentences — the shape of each bounds it: `context` opens with the mechanism in plain words — what the thing does today and where it goes wrong — for a reader who has not opened the pages, and closes with one sentence of bookkeeping — the state of the pages the Case changes, the vault's answer, the Estimates of the rule the Case touches and the ones it does not; a case number stands in `context` or `problem` only when the Case is about that case; no line numbers and no quotation unless the Case is about one; `problem` says what is wrong, or the question answered, in one paragraph; `recommend` says the choice and why, the rejected option in one sentence (case 267)."
    change: "the sentence on the story sections of the Render: context opens with the mechanism and closes with one sentence of bookkeeping, a case number only when the Case is about it, the cap of seven sentences dropped for the shape of each section (case 267)"
  - slug: case-schema
    file: vault/wiki/case-schema.md
    change: "the paragraph on the story sections under Language: the same sentence as the Render of rule-case-protocol — context opens with the mechanism and closes with one sentence of bookkeeping, a case number only when the Case is about it, no cap of seven sentences (case 267)"
  - slug: estimate-case-protocol-case-form
    set:
      status: pending
    sections:
      Criterion: |
        Given:
        `index.md`, `case-schema.md`, `estimates/schema.md` and `schema.yaml` are Rule-class files: an `update` with `file` and `change`, applied by hand in Work Mode.
        **＋** `CLAUDE.md` is rendered from `rule-case-protocol`; an `update` of the Render touches the Estimate of the live reading of that Render (187).
        **＋** The reading of `estimate-case-protocol-case-form` is the Cases of this session at its close, by hand.

        When:
        The agent writes a Case in the chat — at its first showing, when shown again after the owner's change, and with sub-cases.

        Then:
        `given` holds the conditions of the behaviour; the state of the pages the Case changes goes to `context`.
        **＋** `context` opens with the mechanism in plain words — what the thing does today and where it goes wrong — and closes with one sentence of bookkeeping: the state of the pages, the vault's answer, the Estimates of the rule the Case touches and the ones it does not; a case number stands in `context` or `problem` only when the Case is about that case; no count of sentences — the shape of each story section bounds it (case 267).
        **＋** `given`, `when` and `then` together are the Criterion of the Estimate, copied whole and replacing what stood there.
        **＋** An item that writes `sections: Criterion` itself signs that text, on a `create` and on an `update` alike; the Case's `given`, `when`, `then` are the Criterion of the one Estimate that writes none; that is how one Case touches two Estimates.
        **＋** The Case names by slug the Estimate it changes.
        **＋** `tasks` carries no `contract` line and no "block N" line.
        **－** A `create` carries no `method`, `estimate_kind` or `estimate_slug`: a new promise is an explicit `create` of an Estimate with its own slug.
        **－** The eight sections of the chat form do not change.
    change: "the line on context replaced: the mechanism first, the bookkeeping one closing sentence, a case number only when the Case is about it, no cap of sentences; the other lines as 208.2 left them; pending for the reading (case 267)"
```

```tasks
- [x] update `rule-case-protocol`: `replace` in the Render — the sentence on the story sections
- [x] `vault/wiki/case-schema.md`: the same sentence in the paragraph on the story sections, by hand
- [x] `uv run guppi render`: `CLAUDE.md`
- [x] update `estimate-case-protocol-case-form`: `sections: Criterion` whole, the line on `context` replaced, `set: {status: pending}`, `change`
- [x] read `estimate-case-protocol-case-form`: the Cases of this session at its close, by hand — 267 and after
```

## Case 268 — the Frontier in two lists: Cases and Work

> **context:**
> `/hi` assembles the Frontier as one list `F<n>`, and every line closes as `case N`, `work` or `defer case N`, or `/pre-spec` refuses. One list holds items that need a judgment, readings and commits that are simply done, and `git pull`/`gh`, whose decision already stands in `sprint.md` — closed anew every session. The kind of an item the agent decides today by re-reading the brief; the librarian judges it already — it writes "a Case of the next Plan Mode", "readings due", "standing" in Flags — but as one text. When the brief carries that sort explicitly, `/hi` copies it without opening a page: the kind comes from the source. `prespec.check_frontier` reads the id as the first token and the closer as the last segment — any id fits. The Case changes `rule-brief` with `estimate-brief-written` and `rule-skill-hi` with `estimate-hi-writes-frontier`; `estimate-hi-no-read-calls`, `rule-prespec` and its tests are not touched.

> **problem:**
> One list mixes three kinds of item, the agent cannot see where sub-cases are cut, and what is decided comes back every session. Needed: the kind of an item set by its source, not by reading pages; the librarian sorts, `/hi` places.

> **given:**
> The librarian writes `brief.md` by the frame — the Render of `rule-brief`; `/hi` reads `sprint.md`, `brief.md`, the tail of the ledger, `git status` and the output of its own commands — and nothing else.
> **＋** `prespec.check_frontier`: the id is the first token after `[ ]`, the closer the last segment after ` · `; a line without `[ ]` is not checked.
> **＋** The reading of `estimate-brief-written` is by hand after the librarian's run; of `estimate-hi-writes-frontier` by hand at the first `/hi` of the next session.

### Case 268.1 — `rule-brief`: the section Next session

> **when:**
> The librarian rewrites `vault/wiki/brief.md` at the end of its run.

> **then:**
> The brief holds six sections in order: Where things stand, Readings due, Deferred, Flags, Next session, Readings at the close.
> **＋** Where things stand, Readings due, Deferred, Flags and Readings at the close are as today, their content unchanged.
> **＋** Next session — two lists. `Cases`: what needs a decision — a handoff flag with a question or a request to change the sprint, a `failed` Estimate, a contradiction, a defect the librarian found; one line per item, what and from where. `Work`: what is done without a decision — every `pending` reading of Readings due by its slug, the unticked boxes of the Specs, a ledger line this run did not apply, a dirty tree; one line per item.
> **＋** An item stands in one of the two lists, never in both; a list with no item is the line "none".
> **－** The brief still states no decision: the sort by kind is not a judgment of the work.
> **－** The brief of `/carry` keeps its short shape, without Next session — `rule-brief` and `rule-carry-over` both say so.

```then
update:
  - slug: rule-brief
    replace:
      - old: "- Readings at the close: `make test`, `make lint`, page counts."
        new: "- Next session: two lists, one line per item, an item in one list only, a list with no item the line \"none\" (case 268.1). `Cases`, what needs a decision: a handoff flag with a question or a request to change the sprint, a `failed` Estimate, a contradiction, a defect you found — what and from where. `Work`, what is done without a decision: every `pending` reading of Readings due by its slug, the unticked boxes of the Specs, a ledger line this run did not apply, a dirty tree.\n- Readings at the close: `make test`, `make lint`, page counts."
      - old: "A handoff flag that asks for a change of the sprint goes into Flags as a Case of the next Plan Mode;"
        new: "A handoff flag that asks for a change of the sprint goes into the `Cases` of Next session;"
      - old: "Readings due and Readings at the close are omitted;"
        new: "Readings due, Next session and Readings at the close are omitted;"
    change: "the section Next session between Flags and Readings at the close — the lists Cases and Work, the librarian's sort of what the next session decides and what it does; a handoff flag on the sprint goes there; the carry brief without it (case 268.1)"
  - slug: rule-carry-over
    replace:
      - old: "no Readings due, no Readings at the close;"
        new: "no Readings due, no Next session, no Readings at the close;"
    change: "the carry brief's list of omitted sections names Next session, as the carry sentence of rule-brief does (case 268.1)"
  - slug: estimate-brief-written
    set:
      status: pending
    change: "the Criterion replaced whole — six sections, Next session with the lists Cases and Work (case 268.1)"
```

```tasks
- [x] update `rule-brief`: `replace` in the Render — the section Next session after Flags, the handoff flag sentence, the carry sentence; each `old` checked against the page by grep before the librarian
- [x] update `rule-carry-over`: `replace` — "no Readings due, no Next session, no Readings at the close"
- [x] `uv run guppi render`: `.claude/agents/librarian-guppi.md`, `.claude/skills/carry/SKILL.md`
- [x] update `estimate-brief-written`: `set: {status: pending}`, `change`; the Criterion lifted from this sub-case
- [x] read `estimate-brief-written`: the brief after the librarian's run of this session, by hand — in the next session
```

### Case 268.2 — `rule-skill-hi`: the Frontier as `## Cases` and `## Work`

> **when:**
> The person invokes `/hi`, and the agent assembles the Frontier.

> **then:**
> The Frontier, written to `raw/<date>/<hi HHMM>/frontier.md`, is two lists: `## Cases`, lines `- [ ] C<n> — <title> · <source>`, and `## Work`, lines `- [ ] W<n> — <title> · <source>`; closed as today — `[x] … · case N`, `[x] … · work`, `[-] … · defer case N`.
> **＋** The kind comes from the source. Cases: on a plan branch the unfinished plan, first; the items of the current milestone of `sprint.md`; the `Cases` list of the brief's Next session; the brief's Deferred list; a hand edit shown by `Render:` — the same thing `render --sync` printed at session start; a `failed` reading or a lesson of the ledger's Tail; an item the person adds. Work: the `Work` list of the brief's Next session; a dirty tree by `git status`.
> **＋** The milestone is the current one only; a later one, the Backlog and Closed are not items; a decision line of the Tail is not an item.
> **＋** In the chat the Cases are shown as a list with their detail — the agenda of Plan Mode; the Work as one block; sub-cases are cut in Cases only.
> **＋** A `W` that turns out to need a decision closes `· case N`; a `C` that needs none closes `· work`.
> **－** `Pull:` and `Open issues:` are a Cases item only when `sprint.md` names no decision on them; named, they are not an item — `rule-git-context` says the same.
> **－** `/pre-spec` does not change: an open line of either list is a finding.

```then
update:
  - slug: rule-skill-hi
    replace:
      - old: "Assemble the Frontier from the above and present it as a list: tasks, problems, debt carried over, the items of the sprint's current milestone — the first with an open item or with none — and none of a later milestone, of the Backlog or of Closed (case 229.3); on a plan branch the unfinished plan comes first;"
        new: "Assemble the Frontier from the above in two lists, the kind of each item by its source and no page opened (case 268.2). `## Cases`, what needs a decision: on a plan branch the unfinished plan, first; the items of the sprint's current milestone — the first with an open item or with none — and none of a later milestone, of the Backlog or of Closed (case 229.3); the `Cases` list of the brief's Next session; the brief's Deferred list; a hand edit shown by `Render:`; a `failed` reading or a lesson of the Tail; an item the person adds. `## Work`, what needs none: the `Work` list of the brief's Next session; a dirty tree in `Status:`. In the chat the Cases are the agenda of Plan Mode, one line each with its detail; the Work is one block; sub-cases are cut in Cases only;"
      - old: "what `guppi render --sync` printed at session start or on the `Render:` line above is an item when it shows a hand edit."
        new: "the hand edit is what `guppi render --sync` printed at session start or on the `Render:` line above."
      - old: "A failed pull or an unavailable `gh` is an item on that list, not a reason to stop."
        new: "A failed pull or an unavailable `gh` is a Cases item when `sprint.md` names no decision on it, and not an item when it does; neither is a reason to stop."
      - old: "Write the same list to `vault/raw/<date>/<hi HHMM>/frontier.md`"
        new: "Write the same two lists, under `## Cases` and `## Work`, to `vault/raw/<date>/<hi HHMM>/frontier.md`"
      - old: "`- [ ] F<n> — <title> · <source>`"
        new: "`- [ ] C<n> — <title> · <source>` under `## Cases`, `- [ ] W<n> — <title> · <source>` under `## Work`"
      - old: "an item the person adds is a new line."
        new: "an item the person adds is a new Cases line; a `W` that turns out to need a decision closes `· case N`, a `C` that needs none closes `· work`."
    change: "the Frontier in two lists, Cases and Work, the kind of an item by its source — sprint, the brief's Next session and Deferred, the tail, git status, the person; pull and gh not an item when sprint.md names their decision; C<n> and W<n> lines (case 268.2)"
  - slug: rule-git-context
    replace:
      - old: "context and becomes a Frontier item;"
        new: "context and becomes a Frontier item unless `sprint.md` names its decision (case 268.2);"
    change: "a failing pull is a Frontier item unless sprint.md names its decision (case 268.2)"
  - slug: glossary
    file: vault/wiki/glossary.md
    change: "the row /hi, Frontier: the open items in two lists, Cases — the Plan Mode agenda — and Work, the kind by the source (case 268.2)"
  - slug: estimate-hi-writes-frontier
    set:
      status: pending
      method: "one reading by hand at the first /hi of the next session, written into the estimate line; unit: the frontier findings of guppi prespec --check in tests/test_prespec.py"
    change: "the Criterion replaced whole — the Frontier in two lists, the kind of an item by its source, pull and gh by the sprint page; method names prespec (case 268.2)"
```

```tasks
- [x] update `rule-skill-hi`: `replace` in the Render — six pairs: the Frontier paragraph, the `render --sync` sentence, pull and gh, "Write the same list", `F<n>`, "an item the person adds"; each `old` checked against the page by grep before the librarian
- [x] update `rule-git-context`: `replace` in How it works — "becomes a Frontier item unless `sprint.md` names its decision"
- [x] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [x] `vault/wiki/glossary.md`: the row `/hi`, Frontier — two lists, by hand
- [x] `tests/test_prespec.py`: `check_frontier` reads `C1`/`W1` under headings, an open `W` is a finding, a line without `[ ]` is not checked
- [x] update `estimate-hi-writes-frontier`: `set: {status: pending, method}`, `change`; the Criterion lifted from this sub-case
- [x] read `estimate-hi-writes-frontier`: the first `/hi` of the next session, by hand
```

## Deferred

## Case 269 — Slice 3b: `rule-work-mode`, `rule-subagent-guppi`

> **context:**
> Slice 3b is the current milestone of the sprint: `rule-work-mode` — Work Mode, the Spec as tasks with code, the ticked boxes, the test of each Estimate first, the sentence of `insight-workflow-code-live-before-the-page-it-reads`; `rule-subagent-guppi` — what a subagent may do and the fork that comes back as a Case. Both are `draft` placeholders, deferred ten times, the last by 263. This session took the debts and the two rules of reading — the Case protocol (267) and the Frontier (268) — ahead of it.

> **problem:**
> The person closes this Plan Mode with eight Cases and goes to pre-spec; Slice 3b waits for the next session, the eleventh defer.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: Work Mode as a rule — the Spec as tasks with code, the ticked boxes in spec.md, the test of each Estimate written first and turned green, the sentence of insight-workflow-code-live-before-the-page-it-reads on a check that reads a page the same Spec changes; the first item of the next session
  - slug: rule-subagent-guppi
    type: rule
    purpose: what a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case; with rule-work-mode, the first item of the next session
```
