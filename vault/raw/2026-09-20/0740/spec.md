<!-- approved 08:55:25 · session 3228cec5 -->

# Spec — session 0740, 2026-09-20

## Case 261 — `rule-pretask` → `rule-prespec`: the rename in every form (takes up defer 259)

> **context:**
> `rule-pretask` is a Leaf with `enforcement: render`; its Render is the skill `/pre-task`, the check of the ratified set before the Spec is approved. `rule-pretask-hook` is the gate on `PreToolUse ExitPlanMode`, `guppi/pretask.py` and `.claude/settings.json`. Both pages stand `built`, `deferred_by: decision-case-259`; their three Estimates — `estimate-pretask-reconciles`, `estimate-pretask-checks-the-plan`, `estimate-pretask-hook-gates` — all `passed`, and this Case touches all three: the names of the command, the skill, the mark and the tests stand in their Criteria and `method`; by case 204 one Case touches several promises when each item writes `sections: Criterion` itself. The word also lives in the Renders of `rule-skill-hi`, `rule-case-protocol` (→ `CLAUDE.md`), `rule-ask` (→ `ask-guppi.md`), `rule-hook-registry` (→ `settings.json`), in the prose of `rule-ask`, `rule-brief`, `rule-event-log`, `rule-ledger-write`, `rule-retro-commit`, `entity-sprint-migration`, in `index.md`, `case-schema.md`, `glossary.md`, the schemas of entities and estimates, and in the code: `guppi/cli.py`, `guppi/gate.py` (`MARKS`, the mark `pretask`), the docstring of `guppi/pages.py`, `tests/test_pretask.py`, `tests/test_gate.py`, `tests/test_ledger.py`, `Makefile`. The mechanism of 258 — an `update` with `rename` — is built and covered by four tests (434 green at `e69fd95`); its live reading, `estimate-generate-renames`, is the librarian's run on this Case. The slugs `rule-prespec`, `rule-prespec-hook`, `estimate-prespec-*` are free, in `wiki/` and in `archive/`. Decision pages, Lessons, Insights, History, Result, `raw/`, `archive/` and `docs/` are records; they are not rewritten.

> **problem:**
> The name "pre-task" does not say what the skill does: it checks the set before the Spec, it does not ask the vault before a Case. The person keeps "pre-task" for the query before a Case, so one word now names two steps — in `case-schema.md` "pre-task checks the slug" is the query and "pre-task asks for the split" is the check. The mechanical rename moves slugs only; the word in the command, the skill, the mark, the module, the tests and the prose of the live pages has to move separately, and each occurrence needs a judgment on which of the two steps it names.

> **given:**
> An `update` with `rename` moves the page to the new slug, writes History `renamed from`, and every live page of `wiki/`, Decision pages included, that names the old slug — a link, a ref field, the bare word — names the new one; `origin`, History, Result, `raw/` and the archive keep the old name (case 258.1); `glossary.md`, `index.md`, `case-schema.md` and the schemas lie outside the category folders and `retarget` does not walk them.
> **＋** An `update` of an Estimate whose item writes `sections: Criterion` keeps that text; `set: {status: pending}`; that is how one Case touches several promises (case 204).
> **＋** `guppi gate` writes the mark into the event log by the table `MARKS` on the Skill call; the hook on `ExitPlanMode` looks for the mark of this session after its `hi`.
> **＋** The word "pre-task" stays for the query to the vault before a Case — the owner's choice (session 0527); "pre-spec" is the check of the set before the Spec.
> **－** Decision pages, Lessons, Insights, History, Result, `origin`, `raw/`, `archive/`, `docs/` are not rewritten; Lessons and Insights keep their slugs.

> **when:**
> The librarian applies the Spec — `generate` moves the five pages; Work Mode moves the code; the person types `/pre-spec` or the agent calls the skill; `ExitPlanMode` fires.

> **then:**
> The pages stand as `rule-prespec` (`governs: .claude/skills/pre-spec/SKILL.md`), `rule-prespec-hook` (`implementation_ref: [guppi/prespec.py, .claude/settings.json]`), `estimate-prespec-reconciles`, `estimate-prespec-checks-the-plan`, `estimate-prespec-hook-gates`; every live link to them, the `children` of `rule-plan-mode` included, points at the new slug.
> **＋** The skill is `/pre-spec`; its Render says `uv run guppi prespec --check <plan> --session <id>` and "judges it with its own pre-spec"; the command is `guppi prespec`, the module `guppi/prespec.py`, the tests `tests/test_prespec.py`; the Purpose of both rules names `/pre-spec`, `guppi prespec` and the mark `prespec`.
> **＋** `guppi gate` on a call of `pre-spec` writes `- HH:MM:SS <stamp> prespec`; the hook on `ExitPlanMode` with no `prespec` mark of this session after its `hi` exits 2, and the refusal names `/pre-spec`.
> **＋** The three Estimates are `pending`; the Criterion of each is its current text with the new names, written in the item.
> **＋** The word in the live pages outside the five renamed ones, where it names the check of the set, the skill, the command, the mark or the tests, becomes `pre-spec`, `guppi prespec`, `prespec`, `test_prespec`: the Renders of `rule-skill-hi` ("`/pre-task` fails on an open line"), `rule-case-protocol` ("`/pre-task` checks it"), `rule-ask` ("one at pre-task for the whole set" — Purpose and description), `rule-hook-registry` (`uv run guppi pretask`); the prose of `rule-event-log` (the mark), `rule-ledger-write`, `rule-retro-commit` (the typed `/pre-task`), `rule-brief`, `entity-sprint-migration`; `index.md` (the line "pre-task reconciliation"), `case-schema.md` ("pre-task asks for the split", twice), `glossary.md` (the row Plan Mode, Pre-task: `where` → `rule-prespec`, "`/pre-spec` the check of the set" added).
> **－** Where the word names the query before a Case — "Chosen at pre-task" in the schemas, "pre-task guards / checks the slug", "pre-task finds it", "pre-task queries" in `index.md` and `case-schema.md` — it stays.
> **－** The Criteria and `method` of the Estimates of other rules — `estimate-hi-writes-frontier`, `estimate-event-log-records`, `estimate-retro-commit-gates`, `estimate-plan-mode-verified`, `estimate-generate-writes`, `estimate-generate-walks-dates`, `estimate-documentation-completes` — keep the old word until the next `update` that replaces the Criterion whole; ratified text is not edited by hand (§7).
> **－** The logic of `guppi pretask` and `guppi gate` does not change: the rename and nothing else; the Estimates of the other Renders are not touched.
> **－** The old folder `.claude/skills/pre-task/` goes; `.claude/skills/pre-spec/SKILL.md` appears at the librarian's render, after `generate`.

```then
update:
  - slug: rule-pretask
    rename: rule-prespec
    set:
      governs: .claude/skills/pre-spec/SKILL.md
    replace:
      - old: "one `pretask` line with the session's stamp, which is what the pre-task hook looks for"
        new: "one `prespec` line with the session's stamp, which is what the pre-spec hook looks for"
      - old: "name: pre-task"
        new: "name: pre-spec"
      - old: "Run `uv run guppi pretask --check"
        new: "Run `uv run guppi prespec --check"
      - old: "judges it with its own pre-task"
        new: "judges it with its own pre-spec"
    change: "renamed to rule-prespec — the skill /pre-spec, the command guppi prespec, the mark prespec (case 261, supersedes 259)"
  - slug: rule-pretask-hook
    rename: rule-prespec-hook
    set:
      implementation_ref: [guppi/prespec.py, .claude/settings.json]
    sections:
      Purpose: |
        Prevents a Spec from being approved before its decisions were checked against each other
        and the vault. `PreToolUse` on `ExitPlanMode`: in a working session with no `prespec`
        line of this session's stamp after its `hi`, `uv run guppi prespec` exits 2 with the reason, which
        blocks the approval once; the `/pre-spec` call leaves the stamped line through `guppi gate` and the next exit passes. A `prespec` of another stamp or `--------` does not count, and a foreign `session-start` resets nothing (case 136.2). An
        ordinary session, one without `/hi`, is not gated: no governance applies there. The
        same module serves the skill: `uv run guppi prespec --check <plan>` compares the plan
        with the session's ledger lines and frontier (cases 59.1–59.3, 59.6); `/pre-spec` runs
        it, the hook does not. Named `pretask` until case 261.
    change: "renamed to rule-prespec-hook — the hook guppi prespec, the mark prespec, the refusal names /pre-spec (case 261)"
  - slug: estimate-pretask-reconciles
    rename: estimate-prespec-reconciles
    set:
      status: pending
      method: "One reading by hand of the first /pre-spec after the render, written into the estimate line — the exception the Method rule allows"
    sections:
      Criterion: |
        Given:
        `guppi prespec --check <plan>` reads the Cases of the plan by their headings, the `then` blocks, the session's `frontier.md` and the session's ledger window; `guppi gate` writes the `prespec` line with the session's stamp on the Skill call.
        **＋** `--session` takes the eight-character session id — the second token of the `hi:` line, between the time and the folder; `session_stamp` cuts any value to eight characters, so a wrong token answers "no hi recorded for session <8 characters>; nothing checked" on stderr with exit 0, and nothing was checked.
        **＋** An Estimate item of a `then` block is a `create` with `ref`, or an `update` with `set: {status: pending}`; its Criterion is the Case's `given`, `when` and `then` unless the item wrote `sections: Criterion` itself (194.1).
        **＋** The tests in `tests/test_prespec.py` fix `--check`; the live reading is the first `/pre-spec` after the render of case 261.
        **－** The `PreToolUse ExitPlanMode` hook (`rule-prespec-hook`) does not change here.
        **－** The code of `guppi prespec` does not change: the exit 0 without a `hi` is the design of case 213.

        When:
        The person invokes `/pre-spec`, or the agent calls the skill, before the Spec is approved.

        Then:
        The agent runs `guppi prespec --check` on the plan file with `--session <id>`, the eight-character session id — the second token of the `hi:` line the `UserPromptSubmit` hook put in the context at `/hi`, between the time and the folder (cases 213.3, 256) — and reads the first line of the output before the exit code: "no hi recorded for session …; nothing checked" means the wrong value, and the check did not run; it fixes the plan, the frontier or the line for every finding until the command prints nothing; `guppi gate` writes the stamped `prespec` line into the event log on the Skill call.
        **＋** The agent lists every decision of this Plan Mode, one line each: slug — kind — `purpose` for a `create`, an `update`, a `delete`; a `defer` by its slug and the word `defer`; for an `update` of a rule or an entity, the page's `estimates` and which of them the Case names by slug.
        **＋** `ask-guppi` is dispatched once with the list, the absolute path of the plan file, the instruction to read every Case outside `## Deferred` — `when`, `then`, the `then` block — and two questions: which decisions contradict a page, `index.md` or each other; whether an Estimate the Case does not name speaks of the thing the Case changes.
        **＋** Every finding returned is raised as a Case or named in one line as already known; then Plan Mode exits again.
        **＋** The Insight `insight-pretask-session-flag-takes-the-id-not-the-hi-line` is `actioned`; its two lessons go to the archive by the cascade; a third lesson with the same cause reopens it.
        **－** The body of a deferred decision is not read; a Case that changes a page another Case of the plan defers is still a finding.
    change: "renamed with rule-prespec — the Criterion names /pre-spec, guppi prespec, the mark prespec and tests/test_prespec.py (case 261)"
  - slug: estimate-pretask-checks-the-plan
    rename: estimate-prespec-checks-the-plan
    set:
      status: pending
      method: "pytest tests/test_prespec.py, the tests of --check"
    sections:
      Criterion: |
        Given:
        `guppi prespec --check <plan>` reads the Cases of the plan by their headings, the `then` blocks, the session's `frontier.md` and the session's ledger window; `guppi gate` writes the `prespec` line with the session's stamp on the Skill call.
        **＋** An Estimate item of a `then` block is a `create` with `ref`, or an `update` with `set: {status: pending}`; its Criterion is the Case's `given`, `when` and `then` unless the item wrote `sections: Criterion` itself (194.1).
        **＋** The ledger hook finds the session's window by the stamp: the first `hi` of the stamp after its first `session-start`, over the logs from today back to the date of that start (case 213).
        **＋** A rule with several promises is a parent Case that creates the rule and one sub-case per Estimate (`case-schema.md`).
        **＋** The tests in `tests/test_prespec.py` fix `--check`; the live reading is the `/pre-spec` of a session after the render of case 261.
        **－** The `PreToolUse ExitPlanMode` hook (`rule-prespec-hook`) does not change here.

        When:
        `guppi prespec --check <plan>` runs in a session with a `hi`.

        Then:
        One finding per line on stdout, exit 1 on any, 0 and silent when clean; without a `hi` in the session's window, exit 0 and one line on stderr.
        **＋** The stamp is `--session`, else `CLAUDE_SESSION_ID`; with neither, one line on stderr `prespec: no session id; pass --session <stamp> from the hi: line`, exit 2, nothing checked; the last `session-start` of today's log is not read (case 213.1).
        **＋** The session's window is found as the ledger hook finds it — by the stamped `hi`, over the logs back to the date of its `session-start` — so the `hi` of yesterday's session is found after midnight (case 213.1).
        **＋** Lines: a decision line of the window with no item of its kind under its own Case heading; an item with no line; a `defer` line matches a `defer` item, a Rule-class file line an `update` with that `file` or `slug`; an item under another sub-case's heading is a finding.
        **＋** The frontier `raw/<hi date>/<hi HHMM>/frontier.md`: a missing file, an open line, a `case N` whose heading the plan lacks, a `defer case N` with no `defer` item under Case N.
        **＋** Tasks: a Case with a line of a kind other than `defer` and no `tasks` block; an Estimate a `then` block creates or sets `pending` with no task line naming its slug.
        **＋** Governed: an `update` item with `file` on a path a live Rule page governs.
        **＋** Form: a Case whose `then` block holds two or more Estimate items without a written `sections: Criterion` — one promise per Case, split it; an `update` of an Estimate whose page does not exist; a `create` of an Estimate whose `ref` names neither a live rule or entity nor the slug of a `create` item of category `rules` or `entities` in the same plan (case 221).
        **＋** Grammar: every record line of the window — the session's ledger whole plus the date-level ledgers from the `hi` time on — through `materialize.parse_line`; one that does not parse is a finding with its file and line number.
        **＋** A `then` block that does not parse: the error as a finding of its Case.
        **－** No finding on a Leaf `create` without `method`, an `update` without `contract` or a derived slug: those keys are not read.
    change: "renamed with rule-prespec — the Criterion names guppi prespec, the mark prespec, the stderr prefix prespec and tests/test_prespec.py (case 261)"
  - slug: estimate-pretask-hook-gates
    rename: estimate-prespec-hook-gates
    set:
      status: pending
      method: "pytest in tests/test_prespec.py with piped payloads against a temp event log; the live reading once by hand, written into the estimate line"
    sections:
      Criterion: |
        Given:
        A `PreToolUse` payload naming `ExitPlanMode`, with the session's stamp.
        **＋** The ledger hook reads the event logs from today back to the date of this session's `session-start` (`ledger.session_event_logs`, case 55.1).
        **＋** The tests in `tests/test_prespec.py` fix the hook with piped payloads against a temp event log; the live reading is the approval of the next plan after the render of case 261.
        **－** The `--check` pass of `rule-prespec` does not change here.

        When:
        The hook `guppi prespec` on `ExitPlanMode` asks whether `/pre-spec` ran in this session.

        Then:
        With no `prespec` line of this session's stamp after its `hi`, exit 2 with a reason naming `/pre-spec` and the session; with the line, exit 0; any other tool, exit 0.
        **＋** The window is open when the logs hold a `hi` of the session's stamp and a `prespec` of the same stamp after it; a mark of another stamp or `--------` does not count; a foreign `session-start` resets nothing (case 136.2).
        **＋** The logs it reads are the ledger hook's — from today back to the date of this session's `session-start` — so the `hi` and the `prespec` of yesterday's session are found after midnight (case 213.2).
        **－** Without a `hi` of this session the call passes, as before.
    change: "renamed with rule-prespec-hook — the Criterion names guppi prespec, the mark prespec and /pre-spec (case 261)"
  - slug: index
    file: vault/wiki/index.md
    change: "the Plan Mode row of the rules table says pre-spec reconciliation; the query before a Case stays pre-task (case 261)"
  - slug: case-schema
    file: vault/wiki/case-schema.md
    change: "pre-spec asks for the split, twice; pre-task checks the slug stays (case 261)"
  - slug: glossary
    file: vault/wiki/glossary.md
    change: "the row Plan Mode, Pre-task names /pre-spec as the check of the set and rule-prespec in its where column (case 261)"
```

```tasks
- [x] update `rule-pretask`: `rename: rule-prespec`, `set` `governs`, `replace` in Purpose (the mark, "the pre-task hook") and in the Render — four pairs: `name: pre-spec`, `guppi prespec --check`, "its own pre-spec"
- [x] update `rule-pretask-hook`: `rename: rule-prespec-hook`, `set` `implementation_ref`, `sections: Purpose` whole with the new names
- [x] update `estimate-pretask-reconciles`: `rename`, `sections: Criterion` with the new names, `set.method`, `pending`
- [x] update `estimate-pretask-checks-the-plan`: `rename`, `sections: Criterion`, `set.method`, `pending`
- [x] update `estimate-pretask-hook-gates`: `rename`, `sections: Criterion`, `set.method`, `pending`
- [x] `vault/wiki/index.md`: "pre-task reconciliation" → "pre-spec reconciliation", by hand
- [x] `vault/wiki/case-schema.md`: "pre-task asks for the split" → "pre-spec asks for the split", twice, by hand
- [x] `vault/wiki/glossary.md`: the row Plan Mode, Pre-task — `/pre-spec` and `rule-prespec`, by hand
- [x] `git mv guppi/pretask.py guppi/prespec.py`; the docstring and the stderr prefix `pretask: …` → `prespec: …`; `guppi/cli.py` (`"prespec": prespec.run`, the docstring); `guppi/gate.py` (`MARKS = {"pre-spec": "prespec", …}`, the import, the docstring); the docstring of `guppi/pages.py`
- [x] `git mv tests/test_pretask.py tests/test_prespec.py`; `tests/test_gate.py`, `tests/test_ledger.py` — the names of the skill, the mark, the module; `Makefile`
- [x] one-off migration of the word in the live pages by the list in `then`: the Renders of `rule-skill-hi`, `rule-case-protocol`, `rule-ask`, `rule-hook-registry`; the prose of `rule-ask`, `rule-event-log`, `rule-ledger-write`, `rule-retro-commit`, `rule-brief`, `entity-sprint-migration`; acceptance — `grep -rn "pretask\|pre-task" guppi tests .claude Makefile` empty, and in `vault/wiki/` outside decisions, lessons, insights, the Criterion and Method of Estimates, History and Result only the sense of the query remains
- [x] `uv run guppi render` after the migration — `CLAUDE.md`, `.claude/agents/ask-guppi.md`, `.claude/skills/hi/SKILL.md`, `.claude/settings.json` follow their pages
- [x] `git rm -r .claude/skills/pre-task` — the librarian renders the new skill after `generate`
- [x] `make test`, `make style`
- [x] read `estimate-prespec-checks-the-plan`: `pytest tests/test_prespec.py` after the move
- [x] read `estimate-prespec-hook-gates`: pytest after the move; the live part is the approval of the next plan after the render
- [ ] read `estimate-prespec-reconciles`: the first `/pre-spec` — the next session
```

## Case 262 — `estimate-generate-renames`: the placeholder `[[decision-case-N]]` in the Criterion

> **context:**
> `estimate-generate-renames` is a QA Estimate under `rule-page-generation`, created by 258.1, `pending`: pytest is green, the live part is the librarian's run on the first real rename — Case 261 of this session. Its Criterion's `then` quotes the History line `generate` writes twice, with the placeholder `[[decision-case-N]]` as a bare wikilink. `guppi lint` reads every `[[…]]` in a page body as a link and finds `ref: body names decision-case-N, which no live or archived page carries`; a wikilink inside a code span it skips — `links_of` strips code spans before the search. The Decision pages 100.x and 101.x carry the same placeholder in a code span, with no finding. The Case touches no other Estimate of the rule.

> **problem:**
> The ratified text of the Criterion holds the placeholder in a form lint reads as a broken link; the finding stands until the text changes, a reading does not clear it. The choice: repair the Criterion, or leave it as debt.

> **given:**
> `guppi lint` reads every `[[slug]]` in a page body as a link and strips code spans before the search; a slug no live or archived page carries is a finding of class `ref`.
> **＋** An `update` of an Estimate whose item writes `sections: Criterion` keeps that text (case 204); `set: {status: pending}`.
> **－** `origin`, History and Result are not rewritten.

> **when:**
> `guppi lint` reads `estimate-generate-renames` after the librarian's run of this session.

> **then:**
> No `ref` finding on the page: both placeholders stand in a code span, the text of the Criterion is otherwise the one signed in 258.1.
> **＋** The page stays `pending` until its reading on the run of 261.
> **－** The promise and the `method` do not change; `rule-page-generation` is not touched.

```then
update:
  - slug: estimate-generate-renames
    set:
      status: pending
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
    change: "the two placeholders [[decision-case-N]] of the Criterion in code spans, so lint reads no link; the text of 258.1 otherwise (case 262)"
```

```tasks
- [x] update `estimate-generate-renames`: `sections: Criterion` — the text of 258.1 with the two `[[decision-case-N]]` in code spans, `pending`
- [ ] read `estimate-generate-renames`: the librarian's run on Case 261 — the same reading as line 160 of the 0527 Spec
```

## Deferred

## Case 263 — Slice 3b: `rule-work-mode`, `rule-subagent-guppi`

> **context:**
> Slice 3b is the current milestone of the sprint: `rule-work-mode` — Work Mode, the Spec as tasks with code, the ticked boxes, the test of each Estimate first, the sentence of `insight-workflow-code-live-before-the-page-it-reads`; `rule-subagent-guppi` — what a subagent may do and the fork that comes back as a Case. Both are `draft`, deferred by 183, 206, 218, 231, 242, 248, 252, 254, 260; the last defer put them after the rename of 259.

> **problem:**
> The session took F1 and F4 — the rename `pretask → prespec` in every form, the placeholder in the Criterion of `estimate-generate-renames` — and ends Plan Mode without Slice 3b: the rename is the whole of Work Mode of this session, and its live readings come first. The person defers Slice 3b again; it is the first item of the next session.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: Slice 3b, the body of Work Mode with the sentence of insight-workflow-code-live-before-the-page-it-reads; the tenth postponement, the first item of the next session
  - slug: rule-subagent-guppi
    type: rule
    purpose: Slice 3b, the subagent and the fork that comes back as a Case; deferred with rule-work-mode
```
