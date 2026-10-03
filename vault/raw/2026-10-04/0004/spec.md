<!-- approved 00:59:36 · session a17e0a5f -->

# Spec — session 0004, 2026-10-04

## Case 619 — The test page reworded, then deleted

> **context:**
> The last session created the test page `entity-reading-probe` to bring on readings that wait for their moment (case 614). Its `## Purpose` holds the made-up word `quillwort` and the word `bramblewort`. A reword is an `update` item that carries `{old, new}` pairs. At the librarian's run, `guppi generate` replaces each pair as a whole word on every live rule, entity and estimate. The page of the item is the owner, and its text must hold each `new`. The reword has never run live. `estimate-generate-rewords` stands `pending`, and its live leg waits for a librarian's run that applies a reword. While the test page is live, `make lint` reports two findings on it, `schema` and `orphan`. `estimate-sprint-migration-lint-clean` needs `make lint` to exit 0 at the close of the sprint. Case 614 could not do the reword in its own session, because the pair check of `guppi/prespec.py` loads only the pages on disk. That gap still stands, and this Case does not fix it.
>
> This Case does the reword and then deletes the page. The two steps are two sub-cases, and both run at the librarian's run after this session. The docstring of `guppi/generate.py` says it applies the entries of a yaml in order. The decision line of 619.1 comes before the line of 619.2, so the reword runs on the live page and then the delete sets it `archived`. `guppi cleanup` (`rule-cleanup`) then moves the page under `vault/archive/` with its History. Its `reworded` History line therefore stays readable. So do the `log.md` line and the stdout line of the run. If the reword fails and the delete applies, a later `update` still reaches the archived page, because `generate` finds a slug that is not under `vault/wiki/` in the archive. `check_items` of `guppi/prespec.py` keys each item by its kind and slug, so an `update` and a `delete` of one page in one Spec are no finding.
>
> Searches. The Grep `quillwort|bramblewort` (case-insensitive) over `vault/wiki/` printed two files: `brief.md` and `entities/entity-reading-probe.md`. A reword never touches `brief.md`, so the pair hits the test page alone. The owner's `## Purpose` holds `bramblewort`, so the check of the owner's text passes, and the pair check of `guppi/prespec.py` finds the pair on a live page. The Grep `quillwort|bramblewort|reading-probe` (case-insensitive) over `vault/wiki/` printed five files: `brief.md`, `log.md`, `entities/entity-reading-probe.md`, `estimates/estimate-plan-mode-verified.md` and `decisions/decision-case-614.md`. The hit on `estimate-plan-mode-verified` stands in its `## Result`, a record that a reword skips and a delete leaves true. The hit on `decision-case-614` is its `create` list, a record. Its `ref` check in `guppi/lint.py` accepts a slug that an archived page carries. The hits in `brief.md` and `log.md` were not read. The Grep `reword` over `vault/wiki/rules/` printed `rule-case-protocol`, `rule-materialize` and `rule-page-generation`. Each describes how a reword pair is written, carried or applied, and this Case follows each as it stands. The same Grep over `.claude/` printed nothing. `rule-page-generation` carries `deferred_by` `decision-case-469`. Its Problem is whether a supersede of an archived Decision keeps `archived`, and that does not touch this Case.
>
> Done means the following. `estimate-generate-rewords` reads the librarian's run that applies the pair. Its Criterion describes exactly that run, so it stands. Its reading comes at the next `/hi` through the Work list of the brief, since this Case does not set it `pending`. The delete is checked by `estimate-generate-writes` (a `delete` sets `archived` with History `deleted`) and `estimate-cleanup-moves`. Both Criteria stand, because the delete is the kind of entry each describes. At the close of the sprint, `estimate-sprint-migration-lint-clean` reads `make lint`, and its Criterion stands. The Criteria of `estimate-entities-schema-checked` and `estimate-lint-finds-a-broken-link` speak of the findings a page like this one draws while it is live. They stand, because they check `guppi lint` and not this page. The page has an empty `estimates` list. This Case creates no Estimate and replaces no Criterion. No other Case of this session is related.

> **problem:**
> The test page has served its purpose except for one moment: a live reword. It keeps `make lint` red and must be gone before any close of the sprint. The question is how to bring on the reword and remove the page in one session, with each step checked on its own.

> **recommend:**
> - **One decision or two?**
>   - Recommended: (b) two sub-cases under one Case, the reword first and the delete second, since the reword can fail on its own and its fix differs from the fix of a delete.
>   - Answer: Agreed with the recommendation.
> - **Does the delete wait for the word change to be read?**
>   - Recommended: (a) both in this session. The reading loses nothing with the delete, and the lint findings clear soonest.
>   - Answer: Agreed with the recommendation.

### Case 619.1 — The made-up word replaced across the vault

> **given:**
> `entity-reading-probe` — the test page that owns the pair and holds the old word
> **＋** `rule-page-generation` — `guppi generate` applies a `reword` at the librarian's run
> **＋** `estimate-generate-rewords` — the check whose live leg this run is

> **when:**
> The librarian's run after this session runs `guppi generate` over the `update` of `entity-reading-probe` that carries the reword pair `quillwort` → `bramblewort`.

> **then:**
> `quillwort` becomes `bramblewort` as a whole word in the `## Purpose` of `entity-reading-probe`.
> **＋** `entity-reading-probe` gets one History line `reworded: quillwort → bramblewort` that names the Decision page of this sub-case.
> **＋** The stdout of `guppi generate` has one line for `entity-reading-probe` with its count of replacements.
> **－** No live page other than `entity-reading-probe` changes by the pair, and the status of no Estimate changes.

```then
update:
- slug: entity-reading-probe
  reword:
  - old: quillwort
    new: bramblewort
  change: quillwort replaced by bramblewort across the vault, the live leg of estimate-generate-rewords
```

```tasks
- [x] update `entity-reading-probe`
```

### Case 619.2 — The test page deleted

> **given:**
> `entity-reading-probe` — the test page this sub-case deletes
> **＋** `decision-case-614` — the Decision page whose `create` list keeps the slug
> **＋** `rule-page-generation` — `guppi generate` applies a `delete` at the librarian's run
> **＋** `rule-cleanup` — `guppi cleanup` moves an archived page under `vault/archive/`
> **＋** `rule-lint` — `guppi lint` reports a live page off its schema or named by no page

> **when:**
> The librarian's run after this session runs `guppi generate` over the `delete` of `entity-reading-probe`, after the `update` of Case 619.1, and then runs `guppi cleanup` and `guppi lint`.

> **then:**
> `entity-reading-probe` stands `archived`, with History `deleted` after its `reworded` line.
> **＋** `guppi cleanup` moves `entity-reading-probe` under `vault/archive/`, with its History.
> **＋** `guppi lint` reports no `schema` and no `orphan` finding on `entity-reading-probe`.
> **－** The `create` list of `decision-case-614` keeps the slug, and `guppi lint` reports no `ref` finding for it.

```then
delete:
- slug: entity-reading-probe
  impact: A test page that no live page links to and that has no Estimate. Its slug stays in the create list of decision-case-614 and in the Result of estimate-plan-mode-verified, both records that an archived page keeps true. Its delete removes the schema and orphan findings of make lint.
```

```tasks
- [x] delete `entity-reading-probe`
```

## Case 620 — A line put off by the conserved Spec it runs

> **context:**
> At `/hi` the person can take a conserved Spec: a plan that an earlier session ratified and saved with `/carry`, which this session runs whole by `/box`. `rule-skill-hi` then lets the agent ratify no Case but a short-form defer, and it must close each other open line under `## Cases` of `frontier.md` as put off. There are three marks for that: `[-] … · backlog · kept`, `[-] … · sprint · defer` and `[-] … · defer case N`. The third mark is checked by `check_frontier` of `guppi/prespec.py`. It looks for a `defer` item under Case N only in the plan of the current session. A session that runs a conserved Spec has a plan with one title line only. In session 1416 the Frontier line C4, the failed reading of `estimate-handoff-holds-each-fact-once`, came from the ledger Tail. Case 618 of the conserved Spec of 1341, which the session ran, already put off that Estimate. The agent closed the line `[-] … · ledger · defer case 618`, and `uv run guppi prespec --check` refused it with "frontier: C4 defers to case 618, no defer item under Case 618". The agent then closed the line `[x] … · ledger · work`, which `estimate-hi-takes-a-conserved-spec` does not allow, so that reading failed (1416 L8). The lesson `lesson-session-ledger-item-deferred-by-the-conserved-spec-closed-as-work` records it. The librarian grouped it with an older lesson into `insight-session-frontier-no-closer-for-an-item-ended-outside-the-plan`, which stands `open`.
>
> This Case keeps the mark `defer case N` and lets N be a Case of the conserved Spec that the title line of the plan names. Case 620.1 writes that into `rule-skill-hi` and replaces the Criterion of `estimate-hi-takes-a-conserved-spec`. It also names the close in `rule-orchestration`, in its list of the lines a reply closes with no ratification and no defer. Case 620.2 makes `guppi prespec` accept the mark. It finds the conserved Spec by `conserved_spec_named` of `guppi/box.py`, the function that `guppi/spec.py` already uses to read the same title line, so the judgment lives in one place. Case 620.1 also sets the insight `actioned`. The older lesson of that insight, an agenda item left on the sprint page, already has the mark `[-] … · sprint · defer` (cases 310.5, 356.2). By the cascade of `guppi generate` that `estimate-generate-cascades` checks, each `clustered` child of an `actioned` Insight becomes `archived` with History `archived · insight actioned`. So at the librarian's run both lessons of the insight are archived: `lesson-session-ledger-item-deferred-by-the-conserved-spec-closed-as-work` and `lesson-frontier-has-no-closer-for-a-milestone-item-left-on-the-sprint-page`. The insight stays live and reopens on a recurrence (`rule-insights-schema`). The Criterion of `estimate-generate-cascades` describes exactly this, so it stands. The lesson of 1416 is from another session, so no decision line carries `{addresses:...}` for it (case 284.2). This Case closes the brief item that names the cause (C3 of this session's Frontier) and the failed reading (C5). It adds no stop for a line that fits no mark (Q4).
>
> The frame. The only hook on `PreToolUse` `ExitPlanMode` in `.claude/settings.json` is `uv run guppi prespec`, and its rule is `rule-prespec-hook`. The code of `guppi prespec` changes in Work Mode and runs from the working tree at once. The text of `rule-skill-hi` reaches `.claude/skills/hi/SKILL.md` at the render. In between, the check accepts one more form and refuses nothing it accepted before, so no old form is kept. `conserved_spec_named` needs the folder to hold `carry.md`. `/box` deletes that file, but only after the exit from Plan Mode, which is when the check runs. The two sub-cases name the same marks from two sides: the agent that writes a line, and the check that reads it. Their `then` lines therefore share words, but they make two separate promises. Case 619, the only other Case of this session, touches none of these pages.
>
> The moment is a reply in Plan Mode that closes a Frontier line. The Grep `no ratification and no defer` over `vault/wiki/` printed 6 files: `orchestration.md`, `log.md`, `rule-case-protocol`, `rule-orchestration`, `estimate-orchestration-shows-the-frontier-after-a-closed-line` and `decision-case-547`. The hit in `rule-case-protocol` stands in History, and those in `log.md` and the Decision page were not read. The Render of `rule-orchestration` (rendered as `orchestration.md`) sets how a reply ends when it closes a line with no ratification and no defer. Its list of such closes names `sprint · defer` and `backlog · kept` but not a `defer case N` that a Case of the conserved Spec carries, so 620.1 adds that close to the list. The Criterion of `estimate-orchestration-shows-the-frontier-after-a-closed-line` gives its list as examples, and the reply that takes a conserved Spec ends as it says: the Frontier, then `/pre-spec`. So it stands. The short-form section of `rule-orchestration` describes the reply that carries a short-form defer the person asks for, with its line closed `[-] … · defer case N`. It does not say that every such close has a short Case of its own session, so it stays true. Its sentence giving `[-] … · defer case N` to a decision of any other source that is put off also stays true.
>
> Searches. The Grep `defer case` over `vault/wiki/` printed 42 files: `brief.md`, `orchestration.md`, `log.md`, the two lessons, the insight, `rule-skill-hi`, `rule-case-protocol`, `rule-prespec`, `rule-orchestration`, `estimate-hi-takes-a-conserved-spec`, `estimate-hi-writes-frontier`, `estimate-prespec-checks-the-frontier`, `estimate-orchestration-defers-in-one-reply`, `estimate-orchestration-acknowledging-reply`, and 27 Decision pages, which were not read. The hits in `rule-case-protocol` and `rule-prespec` stand in History and were not read. `rule-skill-hi` holds four hits on three lines. Two hits are on the Render line: one is the close this Case extends, and the other says a sprint item never closes `· defer case N`, which stays true. The other two lines are History. The hits in `brief.md` and `log.md` were not read. The Grep `defer case` over `.claude/` printed only `.claude/skills/hi/SKILL.md`, the render of `rule-skill-hi`. The Grep `runs the conserved Spec` over the repository outside `vault/raw/` printed `.claude/skills/hi/SKILL.md`, `tests/test_spec.py`, `tests/test_box.py`, `estimate-hi-takes-a-conserved-spec`, `rule-skill-hi` and files under `vault/archive/`, which were not read. The title line does not change. The Grep `conserved` over `guppi/` printed `backlog.py`, `box.py`, `materialize.py` and `spec.py`.
>
> Done means the following. Case 620.1 replaces the Criterion of `estimate-hi-takes-a-conserved-spec`. Its `purpose` and `method` still describe what it checks, so they stand. Case 620.2 replaces the Criterion of `estimate-prespec-checks-the-frontier`. Its `purpose` (a closer that agrees with its source) and its `method` (`uv run pytest tests/test_prespec.py`) stand. The Criterion of `estimate-hi-writes-frontier` says that a decision of any other source that is put off closes `[-] … · defer case N`. It does not say who holds Case N, so it stands. The Criteria of `estimate-orchestration-acknowledging-reply` and `estimate-orchestration-defers-in-one-reply` list the same marks, which do not change, so they stand.

> **problem:**
> A session that runs a conserved Spec has no valid mark for a Frontier line whose target that Spec already puts off. `rule-skill-hi` gives `defer case N`, but `guppi prespec` looks for Case N only in the session's own plan, which holds no Case. So the agent closed the line `work` by its own judgment, and `estimate-hi-takes-a-conserved-spec` failed.

> **recommend:**
> - **Fix the failed check together with its cause, or on its own?**
>   - Recommended: (a) one Case for both items. The check failed only because the rule has no mark for this line, so it cannot pass until the rule changes.
>   - Answer: (a) one Case for both items.
> - **Which mark closes a line whose put-off is already in the saved plan?**
>   - Recommended: (a) keep `defer case N` and let N point into the conserved Spec that the plan's title line names. `guppi prespec` looks there through the function `/box` already uses.
>   - Answer: Agreed with the recommendation.
> - **Does this Case also close the pattern that groups the two lessons?**
>   - Recommended: (a) mark the insight `actioned` and addressed by this Case, since both of its cases then have a mark.
>   - Answer: Agreed with the recommendation.
> - **Should the agent also stop when a line fits no mark?**
>   - Recommended: (b) leave the stop out of this Case. Every known case has a mark, and a recurrence reopens the insight.
>   - Answer: Agreed with the recommendation.

### Case 620.1 — `/hi` closes a line that the conserved Spec puts off by that Spec's Case

> **given:**
> `rule-skill-hi` — its Render lists the closers of a Frontier line and how a conserved Spec is taken
> **＋** `.claude/skills/hi/SKILL.md` — the skill rendered from `rule-skill-hi`
> **＋** `rule-orchestration` — its Render lists the lines a reply closes with no ratification and no defer
> **＋** `vault/wiki/orchestration.md` — the file rendered from `rule-orchestration`
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier whose lines the agent closes
> **＋** `# Session <hi HHMM> — runs the conserved Spec vault/raw/<date>/<HHMM>/spec.md` — the title line of the plan file of a session that runs a conserved Spec
> **＋** `vault/wiki/backlog.md` — names the `spec.md` of each conserved Spec
> **＋** `rule-spec-box` — `/box` runs the conserved Spec
> **＋** `rule-prespec` — `/pre-spec` checks the plan and the Frontier
> **＋** `estimate-hi-takes-a-conserved-spec` — the check whose Criterion this sub-case replaces
> **＋** `insight-session-frontier-no-closer-for-an-item-ended-outside-the-plan` — the pattern this sub-case marks addressed

> **when:**
> In a session that `/hi` opened from `.claude/skills/hi/SKILL.md` as rendered from `rule-skill-hi`, the person takes a conserved Spec of `## Cases` of `raw/<date>/<hi HHMM>/frontier.md`.

> **then:**
> The agent takes the Spec whole, to be run by `/box`, only while the session's ledger holds no decision line other than a `defer`, and after it ratifies no Case but a short-form defer.
> **＋** It closes the line of that Spec `[x] … · work`.
> **＋** It creates the plan file with one title line, `# Session <hi HHMM> — runs the conserved Spec vault/raw/<date>/<HHMM>/spec.md`, the path that `vault/wiki/backlog.md` names for that Spec.
> **＋** It closes each other open line under `## Cases` as left — `[-] … · backlog · kept`, `[-] … · sprint · defer` or `[-] … · defer case N` — and goes on to `/pre-spec`.
> **＋** A line whose target a `defer` item of that Spec puts off closes `[-] … · defer case N`, N being the Case of that Spec that holds the item, and the session writes no short-form Case and no ledger line for it.
> **－** No other line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` closes `[x]`.
> **－** No Case of the conserved Spec is built again or ratified again in this session.
> **－** `.claude/skills/hi/SKILL.md` equals the Render of `rule-skill-hi` and is not edited by hand.

```then
update:
- slug: rule-skill-hi
  replace:
  - old: a short-form Case and its ledger line, and its target enters `backlog.md` through `deferred_by` (case 451.1);
    new: a short-form Case and its ledger line, and its target enters `backlog.md` through `deferred_by` (case 451.1), or a Case of the conserved Spec the session takes, as below (case 620.1);
  - old: close the other open lines under `## Cases` as left, and go on to `/pre-spec`.
    new: close the other open lines under `## Cases` as left — a line whose target a `defer` item of that Spec puts off closes `[-] … · defer case N`, N being the Case of that Spec that holds the item, with no short-form Case and no ledger line of this session (case 620.1) — and go on to `/pre-spec`.
  change: a line whose target a defer item of the conserved Spec puts off closes defer case N with that Spec's Case (case 620.1)
- slug: rule-orchestration
  replace:
  - old: an item closed `[-] … · sprint · defer` or `[-] … · backlog · kept` —
    new: an item closed `[-] … · sprint · defer` or `[-] … · backlog · kept`, a line closed `[-] … · defer case N` by a Case of the conserved Spec the session takes (case 620.1) —
  change: a line closed defer case N by a Case of the conserved Spec is a close with no ratification and no defer (case 620.1)
- slug: estimate-hi-takes-a-conserved-spec
  set:
    status: pending
  change: the Criterion replaced whole — a line put off by a defer of the conserved Spec closes defer case N with that Spec's Case
- slug: insight-session-frontier-no-closer-for-an-item-ended-outside-the-plan
  set:
    status: actioned
    addressed_by: decision-case-620.1
  change: 'actioned: a line put off by a defer of the conserved Spec closes defer case N, and a sprint item left closes sprint defer (cases 356.2, 620.1)'
```

```tasks
- [x] update `rule-skill-hi`
- [x] update `rule-orchestration`
- [x] update `estimate-hi-takes-a-conserved-spec`
- [x] update `insight-session-frontier-no-closer-for-an-item-ended-outside-the-plan`
- [x] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [x] `uv run guppi render`: `vault/wiki/orchestration.md`
- [ ] read `estimate-hi-takes-a-conserved-spec`
```

### Case 620.2 — `guppi prespec` finds Case N in the conserved Spec the plan names

> **given:**
> `guppi/prespec.py` — `check_frontier` judges the closers of the Frontier
> **＋** `guppi/box.py` — `conserved_spec_named` finds the conserved Spec that the title line of a plan names
> **＋** `tests/test_prespec.py` — the tests of the Frontier check
> **＋** `rule-prespec` — `/pre-spec` runs `uv run guppi prespec --check`, and its docstring says what the check compares
> **＋** `rule-prespec-hook` — the `PreToolUse` hook on `ExitPlanMode` runs the same judgment
> **＋** `vault/raw/<date>/<HHMM>/frontier.md` — the Frontier of the session that the check reads
> **＋** `vault/raw/<date>/<HHMM>/spec.md` — the Spec of a conserved Spec, a folder that holds `carry.md`
> **＋** `estimate-prespec-checks-the-frontier` — the check whose Criterion this sub-case replaces

> **when:**
> `uv run guppi prespec --check <plan>` reads the session's `vault/raw/<date>/<HHMM>/frontier.md`, and the title line of `<plan>` may name the `vault/raw/<date>/<HHMM>/spec.md` of a folder that holds `carry.md`.

> **then:**
> A missing file is the finding `frontier: <path> is missing`.
> **＋** An open line under `## Cases` is a finding. An open line under `## Work` or `## Ask` is not.
> **＋** A closed line whose last segment after ` · ` is none of `case N`, `work`, `defer`, `kept` and `defer case N` is a finding.
> **＋** These pairings of box and closer are findings: `[x]` with `defer`, `kept` or `defer case N`, and `[-]` with `case N` or `work`.
> **＋** `defer` is clean only after the source segment `sprint`, the segment before the closer. `kept` is clean only after the source `backlog`. After any other source, each one is a finding.
> **＋** `defer case N` after the source `sprint` or `backlog` is a finding. After another source, it is a finding when there is no `defer` item under Case N in the plan, and none under Case N of the `vault/raw/<date>/<HHMM>/spec.md` that the title line of the plan names.
> **＋** A line closed `case N` is a finding when the plan has no heading of Case N.
> **－** A title line that names no folder holding `carry.md` adds no Case: `defer case N` is then judged against the plan alone.
> **－** A line that is not a box line, such as `Backlog: N items` or an indented `- near` line, is not read. No line of another session's Frontier file is read.

```then
update:
- slug: rule-prespec
  change: the Frontier check takes defer case N from a defer Case of the conserved Spec that the plan's title line names (case 620.2)
- slug: estimate-prespec-checks-the-frontier
  set:
    status: pending
  change: the Criterion replaced whole — defer case N is found in the plan or in the conserved Spec its title line names
```

```tasks
- [x] update `rule-prespec`
- [x] update `estimate-prespec-checks-the-frontier`
- [x] `guppi/prespec.py`: when Case N has no `defer` item in the plan, `check_frontier` reads the `defer` items of the conserved Spec that `conserved_spec_named` of `guppi/box.py` finds in the plan's title line, by `split_cases` and `then_blocks` of `guppi/materialize.py`; the module docstring and the docstring of `check_frontier` say so
- [x] `tests/test_prespec.py`: a `defer case N` line is clean when N holds a `defer` item in the conserved Spec that the title line names; it is a finding when that Case holds no `defer` item; it is a finding when the named folder holds no `carry.md`
- [x] `make test`
- [x] read `estimate-prespec-checks-the-frontier`
```

## Deferred

## Case 621 — The handoff that names a fact in several sections waits again

> **context:**
> `estimate-handoff-holds-each-fact-once` failed at the `/hi` of session 1341, ledger line 2: `handoff.md` of session 0317 names Case 613.3 in four sections, and Cases 611 and 612.1, the two lessons and `estimate-hi-takes-its-readings` in two. Case 618 of session 1341 put it off. In session 0004 the person put the remaining items off again to go to work.

> **problem:**
> The decision on how `/handoff` keeps each fact in one section is put off.

```then
defer:
  - slug: estimate-handoff-holds-each-fact-once
    type: estimate
    purpose: "Whether handoff.md names each Case, box, reading, lesson and observation in one section only; failed at the /hi of session 1341 on the handoff of session 0317"
```

## Case 622 — The failed showing of a built Case waits again

> **context:**
> `estimate-orchestration-shows-the-built-case` failed in session 0115, ledger line 18: the showing of Case 610 put a sentence of its own between the heading of the top-level Case and its list. Case 611 built the `Stop` check of the layout, live since session 0317. Case 617 of session 1341 put it off. In session 0004 the person put the remaining items off again to go to work.

> **problem:**
> The decision on the failed showing is put off until it is read again.

```then
defer:
  - slug: estimate-orchestration-shows-the-built-case
    type: estimate
    purpose: "Whether the main agent shows each built Case by its file, its list and its ratification as case-guppi built it; failed in session 0115 with a sentence between the heading and the list"
```

## Case 623 — The form of the answer of ask-guppi at /pre-spec waits for a later session

> **context:**
> `estimate-ask-finds` failed in session 0004: of the four dispatches of `ask-guppi` at `/pre-spec` since case 582, the answers of sessions 0317 and 1416 open with numbered findings, not with the five lines `exists`, `near`, `missing`, `rules` and tags/slug that `.claude/agents/ask-guppi.md` and the Criterion require, and the answer of 0115 holds nested list lines under the five labels; the `/pre-spec` skill asks the agent for three kinds of findings. The person put the remaining items off to go to work.

> **problem:**
> Which form the answer of `ask-guppi` takes at `/pre-spec` — the five lines, or a form of its own that the rule names — is put off.

```then
defer:
  - slug: estimate-ask-finds
    type: estimate
    purpose: "Whether ask-guppi answers with exactly five lines; failed in session 0004 on the numbered answers of its /pre-spec dispatches in sessions 0317 and 1416"
```
