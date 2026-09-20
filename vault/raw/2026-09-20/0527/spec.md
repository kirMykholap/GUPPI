<!-- approved 07:02:55 · session 8ce3afdd -->

# Spec — 2026-09-20, session 0527

## Case 255 — `rule-spec-capture`: the fork as `additionalContext`

> **context:**
> `rule-spec-capture` is a Leaf, `enforcement: hook`, code `guppi/spec.py`, the `PostToolUse` hook on `ExitPlanMode`. It appends the approved plan to `raw/<date>/<hi HHMM>/spec.md` and then prints one line on stdout with exit 0 — the fork: Work Mode on the Spec or `/carry`, with the session folder and the Spec file (case 190.5). The page says the hook "prints the fork into the context". Two Estimates: `estimate-spec-capture-appends` — the writing of the Spec, untouched by this Case; `estimate-spec-capture-offers-the-fork` — `passed` 2026-09-16 on one pytest, "the live print in the client is read at the next ExitPlanMode", a reading nobody took. Twice, in sessions 2054 and 2253, the line was not in the `ExitPlanMode` result; the agent asked the fork from memory of the rule. The Claude Code documentation: for `PostToolUse` the exit-0 stdout of a hook goes to the debug log and not to the context; a JSON `hookSpecificOutput.additionalContext` reaches the context; exit 2 shows stderr as a warning. The lesson `lesson-hooks-posttooluse-stdout-not-in-context` is written.

> **problem:**
> The promise of 190.5 — the hook prints the fork into the agent's context — was never kept live: the line goes where the agent does not see it. The test checks the text of stdout, not the shape the client reads, so the Estimate passed on a mechanism that does not work. The Case chooses how the line reaches the agent and rewrites the Criterion so that a live reading closes it.

> **given:**
> For `PostToolUse` Claude Code adds to the agent's context only `hookSpecificOutput.additionalContext` from a JSON object on stdout; plain stdout with exit 0 goes to the debug log.
> **＋** A `PostToolUse` hook blocks nothing: the tool has run.
> **－** The path "no `/hi` for this session" — stderr, exit 2 — does not change.

> **when:**
> `guppi spec` has run on `PostToolUse` of `ExitPlanMode` and written the Spec, or found it already there.

> **then:**
> The stdout of the hook is one JSON object: `hookSpecificOutput` with `hookEventName: PostToolUse` and `additionalContext`, holding the fork line — Work Mode on the Spec or `/carry` — with the session folder and the Spec file, and that nothing starts until the person answers.
> **＋** The agent sees this line in the `ExitPlanMode` result.
> **－** Without a Spec, nothing, as before.
> **－** The writing of the Spec does not change: that is the promise of `estimate-spec-capture-appends`.

```then
update:
  - slug: rule-spec-capture
    replace:
      - old: "Having written the Spec, the hook prints the fork"
        new: "Having written the Spec, the hook prints the fork as `hookSpecificOutput.additionalContext`, the one shape in which the stdout of a `PostToolUse` hook reaches the agent (case 255),"
    change: the fork line goes to the agent as additionalContext, not as plain stdout (case 255)
  - slug: estimate-spec-capture-offers-the-fork
    set:
      status: pending
      method: pytest in tests/test_spec.py, the three tests of the printed fork, plus one live reading of the ExitPlanMode result of a session after the change
    change: the Criterion replaced whole — the fork as additionalContext, read live (case 255)
```

```tasks
- [x] update `rule-spec-capture`: `replace` in Purpose — the line goes as `additionalContext`, not as plain stdout
- [x] update `estimate-spec-capture-offers-the-fork`: the Criterion replaced whole, `method` — pytest and a live reading, `pending`
- [x] `guppi/spec.py`: `fork_line` returns the JSON object; the docstring without "which the client adds to the agent's context", with the `hookSpecificOutput` shape
- [x] `tests/test_spec.py`: the three fork tests parse the JSON — `hookEventName`, `additionalContext` with the folder, the file, Work Mode and `/carry`; without a Spec the stdout is empty
- [ ] read `estimate-spec-capture-offers-the-fork`: pytest and the `ExitPlanMode` result of this session
```

## Case 256 — `rule-pretask`: `--session` takes the eight-character session id

> **context:**
> `rule-pretask` is a Leaf, `enforcement: render`, governing `.claude/skills/pre-task/SKILL.md`. Its Render says: run `guppi pretask --check <plan> --session <stamp>`, "the stamp from the `hi:` line". The `hi:` line carries three tokens — the time, the eight-character session id, the folder — and `--session` takes the id alone; `session_stamp` cuts the value to eight characters, so a wrong token answers "no hi recorded for session <8 characters>; nothing checked" on stderr with exit 0, the design of case 213: a check without a `hi` blocks nothing. Twice the agent passed the wrong token: the whole line in 1252, the folder in 2253; both times the check did not run and the run looked clean. The librarian clustered the two lessons into `insight-pretask-session-flag-takes-the-id-not-the-hi-line`, severity 2, `open`, with the proposal: the Render names the id, the second token, and one line on reading the output — its first line, not the exit code. Two Estimates: `estimate-pretask-reconciles` — the live reading of the Render, its Criterion opens with the same phrase "the stamp from the `hi:` line" and is replaced whole; `estimate-pretask-checks-the-plan` — the tests of `--check`, untouched: the code does not change.

> **problem:**
> The text of the rule names the value of the flag with the word "stamp", which in the context also names the whole `hi:` line; the code takes one token of three and answers a wrong one with a silent exit 0. The agent read the text two different ways, and both times `/pre-task` checked nothing. The Render has to name the token exactly and tell the agent to read the first line of the output, not the exit code.

> **given:**
> `guppi pretask --check <plan>` reads the Cases of the plan by their headings, the `then` blocks, the session's `frontier.md` and the session's ledger window; `guppi gate` writes the `pretask` line with the session's stamp on the Skill call.
> **＋** `--session` takes the eight-character session id — the second token of the `hi:` line, between the time and the folder; `session_stamp` cuts any value to eight characters, so a wrong token answers "no hi recorded for session <8 characters>; nothing checked" on stderr with exit 0, and nothing was checked.
> **＋** An Estimate item of a `then` block is a `create` with `ref`, or an `update` with `set: {status: pending}`; its Criterion is the Case's `given`, `when` and `then` unless the item wrote `sections: Criterion` itself (194.1).
> **＋** The tests in `tests/test_pretask.py` fix `--check`; the live reading is the `/pre-task` of this session.
> **－** The `PreToolUse ExitPlanMode` hook (`rule-pretask-hook`) does not change here.
> **－** The code of `guppi pretask` does not change: the exit 0 without a `hi` is the design of case 213.

> **when:**
> The person invokes `/pre-task`, or the agent calls the skill, before the Spec is approved.

> **then:**
> The agent runs `guppi pretask --check` on the plan file with `--session <id>`, the eight-character session id — the second token of the `hi:` line the `UserPromptSubmit` hook put in the context at `/hi`, between the time and the folder (cases 213.3, 256) — and reads the first line of the output before the exit code: "no hi recorded for session …; nothing checked" means the wrong value, and the check did not run; it fixes the plan, the frontier or the line for every finding until the command prints nothing; `guppi gate` writes the stamped `pretask` line into the event log on the Skill call.
> **＋** The agent lists every decision of this Plan Mode, one line each: slug — kind — `purpose` for a `create`, an `update`, a `delete`; a `defer` by its slug and the word `defer`; for an `update` of a rule or an entity, the page's `estimates` and which of them the Case names by slug.
> **＋** `ask-guppi` is dispatched once with the list, the absolute path of the plan file, the instruction to read every Case outside `## Deferred` — `when`, `then`, the `then` block — and two questions: which decisions contradict a page, `index.md` or each other; whether an Estimate the Case does not name speaks of the thing the Case changes.
> **＋** Every finding returned is raised as a Case or named in one line as already known; then Plan Mode exits again.
> **＋** The Insight `insight-pretask-session-flag-takes-the-id-not-the-hi-line` is `actioned`; its two lessons go to the archive by the cascade; a third lesson with the same cause reopens it.
> **－** The body of a deferred decision is not read; a Case that changes a page another Case of the plan defers is still a finding.

```then
update:
  - slug: rule-pretask
    replace:
      - old: "--session <stamp>`, the stamp from the `hi:` line the `UserPromptSubmit` hook put in the context at `/hi` (case 213.3). It prints one line"
        new: "--session <id>`, the eight-character session id — the second token of the `hi:` line the `UserPromptSubmit` hook put in the context at `/hi`, between the time and the folder (cases 213.3, 256). Read the first line of the output before the exit code: 'no hi recorded for session …; nothing checked' means the wrong value, and the check did not run. It prints one line"
    change: "--session takes the eight-character session id, the second token of the hi: line; the first line of the output is read before the exit code (case 256)"
  - slug: estimate-pretask-reconciles
    set: {status: pending}
    change: "the Criterion replaced whole — the session id named as the second token of the hi: line, the first line of the output read (case 256)"
  - slug: insight-pretask-session-flag-takes-the-id-not-the-hi-line
    set: {status: actioned, addressed_by: "[[decision-case-256]]"}
    change: "actioned — the Render of rule-pretask names the eight-character id and the reading of the output's first line (case 256)"
```

```tasks
- [x] update `rule-pretask`: `replace` in the Render — the id in place of "stamp", the sentence on the first line of the output
- [x] update `estimate-pretask-reconciles`: the Criterion replaced whole, `pending`
- [x] update `insight-pretask-session-flag-takes-the-id-not-the-hi-line`: `status: actioned`, `addressed_by: [[decision-case-256]]`
- [x] `uv run guppi render` at the librarian's run
- [x] read `estimate-pretask-reconciles`: the first `/pre-task` after the render — this session's `/pre-task` with `--session 8ce3afdd` and the first line of the output read, if the person counts it
```

## Case 258 — `update` with `rename`: a page changes its slug by script

> **context:**
> A decision is a `create`, `update`, `delete` or `defer`; the id of a page is its filename; `origin` is never rewritten. An `update` in a `then` block carries `set`, `sections`, `replace`, `change`; `guppi materialize` copies these keys from the item into the yaml, `guppi generate` (`rule-page-generation`, `guppi/generate.py`) applies them to the page found by its slug and writes a History line; a `create` on a taken slug it refuses with an error, never renaming. The links to a page live in the `[[slug]]` of bodies and in the `REF_FIELDS` — `parent`, `children`, `estimates`, `target`, `deferred_by`, `addressed_by`; lint checks them against live and archived pages; `log.md`, `brief.md` and `raw/` are not pages. `rule-page-generation` carries six Estimates, none about moving a file: the Case creates a seventh, `estimate-generate-renames`, the slug free. `rule-materialize` carries nine; `estimate-materialize-assembles` — the assembly of the yaml from ledger and Spec — keeps its Criterion: the key is added in code, the reading is pytest. The Rule-class files that describe `update`: `index.md` §3 and §5, `case-schema.md`, `decisions/schema.md`, `glossary.md`.

> **problem:**
> A page cannot be renamed today except as a `create` of a new one and a `delete` of the old — losing History on the live page, signing Criteria twice, and leaving two pages for one thing. One decision has to change a slug so that the page stays the same page and every link to it in the vault names the new slug.

> **given:**
> An `update` item may carry `rename: <new slug>` beside `set`, `sections`, `replace`, `change`; the ledger line names the old slug.
> **＋** The id of a page is its filename; the new slug carries the same category prefix.
> **＋** `origin` is never rewritten; the archive, `raw/`, `log.md` and `brief.md` are not pages.
> **－** A taken slug — live or archived — and a foreign prefix: an error on a `create`, the same on a `rename`.

### Case 258.1 — `rule-page-generation`: `generate` moves the page and its links

> **when:**
> `guppi generate` applies an `update` whose item carries `rename`.

> **then:**
> The file `wiki/<category>/<old>.md` becomes `<new>.md`; the page's History gets "renamed from `<old>` · [[decision-case-N]]"; the item's `set`, `sections` and `replace` apply to the new file.
> **＋** In every live page of `wiki/` — Decision pages included — every `[[old]]` becomes `[[new]]`, every `REF_FIELDS` value holding the old slug becomes the new one, and the old slug as a whole word in the body outside `## History` and `## Result` becomes the new one; every page touched, Decision pages excepted, gets the History line "ref `<old>` → `<new>` · [[decision-case-N]]".
> **＋** The Decision page of the Case is written as today — by the slug of the ledger line, before the entries; the walk retargets its link like any other.
> **＋** The order of application is the order of the yaml: an `update` of the same page from an earlier Case lands on the old file, and the `rename` moves it with the page.
> **－** A taken slug or a foreign prefix: the entry is `failed`, nothing is moved.
> **－** `origin`, `## History` and `## Result` of any page, the archive, `raw/`, `log.md` and `brief.md` are untouched; `guppi sprint` redraws `sprint.md` from the sprint page.

```then
update:
  - slug: rule-page-generation
    replace:
      - old: "placeholder page, `status: draft` and no `kind`, fills that page (case 101.1)."
        new: "placeholder page, `status: draft` and no `kind`, fills that page (case 101.1). An `update` whose item carries `rename: <new slug>` moves the page to the new slug, the same category prefix, and rewrites every link and ref field to it in the live pages of `wiki/`, Decision pages included; a taken or foreign slug fails the entry (case 258.1)."
    change: an update with rename moves the page and rewrites its links; a taken or foreign slug fails the entry (case 258.1)
  - file: vault/wiki/index.md
    change: "§3 the `update` row, §5 the `update` route and the sentence on the slugs of the ledger lines: an item may carry `rename: <new slug>`; the page moves, its links follow, a later rename retargets a Decision page's link (case 258.1)"
  - file: vault/wiki/case-schema.md
    change: "the sentence on what an `update` holds: `rename` (the new slug, the same category prefix; the page moves and every link in the live pages follows) beside `set`, `sections`, `replace`, `change` (case 258.1)"
  - file: vault/wiki/decisions/schema.md
    change: "the `update` row: the slug is the ledger line's; a later rename retargets the link like any link (case 258.1)"
  - file: vault/wiki/glossary.md
    change: "the Types row: an `update` may carry `rename` (case 258.1)"
create:
  - slug: estimate-generate-renames
    type: estimate
    ref: rule-page-generation
    kind: QA
    purpose: An update with rename moves the page to its new slug and rewrites every link to it in the live pages, History and Result untouched
    method: pytest in tests/test_generate.py against a temp vault; the live reading once by hand, the librarian's run on a real rename
    tags: [harness, workflow, tests]
```

```tasks
- [x] update `rule-page-generation`: `replace` in Purpose — one sentence on `rename`
- [x] create `estimate-generate-renames`
- [x] `guppi/generate.py`: `rename` in `update` — the move, the History line, the walk of the live pages, the Decision page, the refusal on a taken or foreign slug
- [x] `tests/test_generate.py`: the move and its History; links, ref fields and the word in a body rewritten, History and Result not; the Decision page; a taken slug; a foreign prefix; `set` after `rename`
- [x] `vault/wiki/index.md` §3 and §5: `update` carries `rename`, by hand
- [x] `vault/wiki/case-schema.md`: "An `update` holds … `rename`", by hand
- [x] `vault/wiki/decisions/schema.md`: the `update` row — the ledger slug, retargeted by a later rename, by hand
- [x] `vault/wiki/glossary.md`: the Types row, by hand
- [ ] read `estimate-generate-renames`: pytest, and the librarian's run on the first real rename
```

### Case 258.2 — `rule-materialize`: `rename` reaches the yaml

> **when:**
> `guppi materialize` assembles an `update` entry from a ledger line and its item in the Spec.

> **then:**
> The entry carries the item's `rename` as it is, beside `set`, `sections`, `replace`, `change`.
> **－** An item without `rename` is as before; `materialize` does not check the value's form, `generate` does.

```then
update:
  - slug: rule-materialize
    replace:
      - old: "Its content is\nlifted from the `then` block of its Case in the Spec."
        new: "Its content is\nlifted from the `then` block of its Case in the Spec — `set`, `sections`, `replace`, `change`, and `rename` when the item carries it (case 258.2)."
    change: the rename key of an update item is carried into the entry (case 258.2)
```

```tasks
- [x] update `rule-materialize`: `replace` in Purpose — the `rename` key
- [x] `guppi/materialize.py`: `rename` among the copied keys of an update and in the docstring's field list
- [x] `tests/test_materialize.py`: an item with `rename` reaches the entry
```

### Case 258.3 — `estimate-materialize-assembles`: `rename` in the list of keys

> **when:**
> `guppi materialize` lifts an `update` entry from a ledger line and its item.

> **then:**
> The Criterion of `estimate-materialize-assembles` names `rename` among the keys lifted from the `then` block: "`fields`, `sections`, `replace`, `change`, `rename`, `impact`"; the rest of the Criterion stands as it is, written whole under `sections: Criterion`; `pending`.

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
        One entry per record line, in ledger order: `case`, `kind`, `category` from the slug prefix, `slug`, `ref`, `source`, `supersedes`, `tags`, `origin`, `line`, `text`, `decision`; from the `then` block — `fields`, `sections`, `replace`, `change`, `rename`, `impact`; what the block lacks is `incomplete`, never invented (case 258.3).
        **＋** Only the keys the category's `schema.yaml` names as fields reach `fields` of a `create` or `defer` entry; the structural keys of the item go where they go — `ref` to the entry, `sections`, `tags`, `file`; a key that is neither is marked `unknown: [key]` on the entry, printed by `--show`, never written to the page, and the entry applies; `incomplete` is counted by `REQUIRED` as before (case 214.1).
        **＋** An Estimate has its own line and its own entry; the `ref` of the line is the Estimate itself.
        **＋** An `update` entry for an Estimate carries `sections.Criterion` — the text the item wrote under `sections: Criterion` itself, else the `given`, `when` and `then` of its Case verbatim with their operands as `Given:`, `When:`, `Then:` — replacing what stood there, and `set: {status: pending}` unless the item set a status itself; the `given` of a sub-case is its parent's when it has none of its own.
        **＋** A `create` entry for an Estimate keeps `kind`, `purpose`, `method`, `tags` as fields; its Criterion the same way: the written text when there is one, else the Case's; `## Context` and `## Method` are not written.
        **＋** One decision entry per Case: `decision`, `case_text`, `targets`; a sub-case inherits `context`, `problem`, `recommend`, `given`, never `when`.
        **＋** An `estimate` line for a page of the same ledger is folded into its `create`; for an earlier page it is an `estimate` entry. The `new_tags` of any Case reach the yaml once. An existing yaml is extended, never rewritten.
        **－** An `update` entry carries no `contract`, and no Estimate is derived from it; a `create` carries no `method`, `estimate_kind` or `estimate_slug`; neither `criterion_block`, `case_removed` nor `remove_criterion` is derived.
        **－** The keys `contract`, `estimate_slug`, `estimate_kind` and `method` on a rule's item are ignored: they reach neither the page, nor `incomplete`, nor `unknown`.
        **－** A line the grammar does not parse goes under `unparsed`; the run goes on.
    change: "the Criterion names rename among the keys lifted from the then block (case 258.3)"
```

```tasks
- [x] update `estimate-materialize-assembles`: `sections: Criterion` — one line with `rename`, `pending`
- [x] read `estimate-materialize-assembles`: pytest, one reading for 258.2 and 258.3
```

## Deferred

## Case 259 — `rule-pretask`, `rule-pretask-hook`: the rename to `prespec`

> **context:**
> The skill `/pre-task` — the Render of `rule-pretask` — checks the ratified set before the Spec is approved; the hook `guppi pretask` on `PreToolUse ExitPlanMode` (`rule-pretask-hook`) gates the approval on it. The person keeps the name "pre-task" for the query before a Case and wants the check named "pre-spec" everywhere the name is visible: the skill `/pre-spec`, the page slugs `rule-prespec`, `rule-prespec-hook`, `estimate-prespec-reconciles`, `estimate-prespec-checks-the-plan`, `estimate-prespec-hook-gates`, the module `guppi/prespec.py`, the command `guppi prespec`, the event-log mark `prespec`, the tests; the word in the Renders of `rule-skill-hi`, `rule-case-protocol`, `rule-ask`, `rule-hook-registry`, `rule-retro-commit`, in `glossary.md`, `case-schema.md`, `index.md`, and in the prose and Criteria of the live pages. Lessons and Insights keep their slugs: no decision creates or deletes them. Case 258 of this session builds the mechanism, an `update` with `rename`, and its Estimate is read live on the first real rename.

> **problem:**
> Case 257 was drafted as five `update` items with `rename` plus the code, the Renders and a one-off migration of the word; it is not ratified in this session so that the mechanism of 258 is built and tested before it is used, and so that the Spec of this session stays buildable. The rename is the first item of the next session.

```then
defer:
  - slug: rule-pretask
    type: rule
    purpose: rename to rule-prespec by an update with rename (case 258), with the skill /pre-spec, the module guppi/prespec.py, the command guppi prespec, the mark prespec, the three Estimates and the word in every Render and live page; the first item of the next session
  - slug: rule-pretask-hook
    type: rule
    purpose: rename to rule-prespec-hook in the same Case as rule-pretask; the refusal names /pre-spec, the mark it looks for is prespec
```

## Case 260 — Slice 3b: `rule-work-mode`, `rule-subagent-guppi`

> **context:**
> Slice 3b is the current milestone of the sprint: `rule-work-mode` — Work Mode, the Spec as tasks with code, the ticked boxes, the test of each Estimate first, the sentence of `insight-workflow-code-live-before-the-page-it-reads`; `rule-subagent-guppi` — what a subagent may do and the fork that comes back as a Case. Both are `draft`, deferred by 183, 206, 218, 231, 242, 248, 252, 254; the last defer named them the first item of this session.

> **problem:**
> The session took F5, F2 and F6 — the fork line of `guppi spec`, the `--session` value of pre-task, the rename mechanism — and ends Plan Mode without Slice 3b. The person defers it again; the rename of 259 goes first in the next session, Slice 3b after it.

```then
defer:
  - slug: rule-work-mode
    type: rule
    purpose: Slice 3b, the body of Work Mode with the sentence of insight-workflow-code-live-before-the-page-it-reads; the ninth postponement, after the rename of case 259 in the next session
  - slug: rule-subagent-guppi
    type: rule
    purpose: Slice 3b, the subagent and the fork that comes back as a Case; deferred with rule-work-mode
```
