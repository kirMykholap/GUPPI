<!-- approved 23:26:18 · session 104e52a9 -->

# Spec — 2026-09-22, session 2046

## Case 353 — the paragraph on an `update` in one Case: the key in the enumeration, the author's steps at the end (supersedes 341 and 342)

> **context:**
> Cases 341 and 342 of this plan both change one paragraph of the Render of `rule-case-protocol` — the one that describes an `update` — and both add a line to the Criterion of `estimate-case-protocol-loaded`. As a pair they carry three faults. Each writes into the live text the number of the Case it replaced, 337 and 340, whose edits never land and whose Decision pages go to the archive marked superseded, so a reader of `case-schema.md` is sent to a Case that did nothing. They judge one position by opposite standards: 341 puts the requirement for signing a pair — a step of the author — right after the words "it carries no `contract`.", while the `context` of 342 argues that text at that anchor reads as a condition on the shape of an `update` and not as a step of the author. And two `given` lines carry traces: 342's says the paragraph turns to `delete` and `defer` after the anchor, while the next sentence is the one on one promise per Case; 341's names the anchor of case 340, which is gone.
> `rule-case-protocol` stands `draft`; the live reading of its Render is `estimate-case-protocol-loaded`, `passed`; the page's three other Estimates are not touched. `estimate-case-protocol-case-form` stands `pending` and its Criterion already says that a Case names by slug the Estimate it changes; this Case does not change that Criterion, and its reading over the Cases of a session will meet the new step when it is taken.

> **problem:**
> Two Cases divide one paragraph between them, cite the Cases they replaced, and disagree on where a step of the author belongs.

> **given:**
> `case-schema.md` is the Render of `rule-case-protocol`, loaded by `/hi` in every working session; its sentence on the keys of an `update` runs "`set` … `sections` … `replace` (…), `change` (one line for History) and, when the page changes its slug, `rename` (… case 258.1); it carries no `contract`."
> **＋** The description of an `update` ends with the words "unless the part is inside the Criterion, which sets `pending` (case 296)."; the next sentence is the one on one promise per Case.
> **＋** `reword` is a key of a `then` block: `materialize` carries it into the entry (274.3), `generate` replaces the pairs as whole words over every live page, checks the owner and refuses the entry on a pair with no hit (274.1); a slug changes through `rename` (274.1).
> **＋** An `update` of a rule's `Render` touches the Estimate of the live reading of that Render (187); a part inside a Criterion sets the page `pending` with no `set.status` (296).
> **＋** Both anchors stand once each in the page and do not overlap.

> **when:**
> The agent writes the `then` block of a Case that changes an existing page, and reads the description of an `update` in `case-schema.md`.

> **then:**
> In the sentence of `case-schema.md` that enumerates the keys of an `update`, `reword` stands between `replace` and `change`: a list of `{old, new}` pairs replaced as whole words over every live page of `wiki/`, the page of the item being the owner, for a word that changes everywhere — a slug goes through `rename`.
> **＋** `change` and `rename` keep their place: the sentence reads as one list of keys.
> **＋** At the end of the description of an `update`, after the sentence that ends "which sets `pending` (case 296)", two sentences stand: a pair under `replace` or `reword` is signed only after the sentence around every match is read whole and what it names there is said, never from the line a grep printed; and a Case that changes the behaviour of an existing page reads the page's `estimates` and gives an `update` to each one whose Criterion speaks of the change, read as the `then` block is written, not at pre-spec.
> **＋** An Estimate whose Criterion speaks of something else is not named: naming a spare one replaces a sound Criterion.
> **＋** The Criterion of `estimate-case-protocol-loaded` names both additions; the page goes `pending`.
> **－** The words "it carries no `contract`." keep their place, and nothing is added after them.
> **－** `rule-page-generation` does not change: the mechanics of applying a `reword` are described there and stay.
> **－** The Case has no Estimate of its own; the refusal for the pair procedure is 351.

```then
update:
  - slug: rule-case-protocol
    replace:
      - old: "a mapping under `replace` is a shape `generate` rejects), `change` (one line for History)"
        new: "a mapping under `replace` is a shape `generate` rejects), `reword` (a list of `{old, new}` pairs replaced as whole words over every live page of `wiki/`, the page of the item being the owner, for a word that changes everywhere — a slug goes through `rename`, case 274.1), `change` (one line for History)"
      - old: "which sets `pending` (case 296)."
        new: "which sets `pending` (case 296). A pair under `replace` or `reword` is signed only after the sentence around every match is read whole and what it names there is said, never from the line a grep printed (case 353). A Case that changes the behaviour of an existing page reads the page's `estimates` and gives an `update` to each one whose Criterion speaks of the change — read as the `then` block is written, not at pre-spec; an Estimate whose Criterion speaks of something else is left alone, since naming a spare one replaces a sound Criterion (cases 53.2, 353)."
    change: reword among the keys of an update, and the two steps of the author at the end of the description of an update (case 353, supersedes 332.1, 337, 340, 341 and 342)
  - slug: estimate-case-protocol-loaded
    replace:
      - old: "a part inside the Criterion sets `pending` (294, 296)."
        new: "a part inside the Criterion sets `pending` (294, 296); it names `reword` among the keys of an `update`, between `replace` and `change`, and, at the end of the description of an `update`, the requirement for signing a pair of either kind and the step that a Case changing a page reads the page's `estimates` (353)."
    change: the Criterion names reword among the keys of an update and the two steps of the author (case 353)
```

```tasks
- [ ] update `rule-case-protocol` — two `replace` pairs inside the Render: `reword` into the enumeration, the two author's steps at the end of the description of an `update`
- [ ] update `estimate-case-protocol-loaded` — one `replace` pair inside the Criterion; the page goes `pending`
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-protocol-loaded` by its method — one reading at the first `/hi` of a session, by hand, plus the preview cases of `tests/test_ledger.py`
```

## Case 350 — the description of `method` agrees with the code whole (supersedes 343)

> **context:**
> Case 343 set out to repair the promise that a `method` naming one of the four forms earns no finding, and repaired half of it. It made the exception for the Estimate of a MOC and none for the Estimate of a Leaf: `check_method` earns a finding on a `tests/…` path that is not on disk, and on a `make <target>` the Makefile does not hold. A reader of the schema signs `pytest tests/test_x.py` for a file that does not exist and believes it clean. Its second error: the text says a page of the old shape is one with no `method` field, while `is_old_shape` counts a page as old-shaped on any of four triggers — no `method` field, a `## Context` section, a `## Method` section, or a `### case N` block in the Criterion; three of the four hold for pages that do carry the field.
> `rule-estimates-schema` renders `vault/wiki/estimates/schema.yaml`; the live reading is `estimate-estimates-schema-checked`, `passed`, whose Criterion covers the prose as data and does not itself change. The words "the one spelling of a reading" hold once the code task of case 330.1 of the conserved Spec lands: `READING` still stands in `guppi/lint.py`.

> **problem:**
> The text that is to bring the schema into agreement with lint disagrees with it in two more places: what the Estimate of a Leaf may name, and what makes a page old-shaped.

> **given:**
> `vault/wiki/estimates/schema.yaml` is the Render of `rule-estimates-schema`; the agent reads it before a `create` of an Estimate.
> **＋** `check_method` on the Estimate of a Leaf: a path under `tests/` that does not exist earns a finding; a `make <target>` the Makefile does not hold earns a finding; `by hand` is clean; no path, no `pytest` and no target earns a finding.
> **＋** `check_method` on the Estimate of a MOC: a `make <target>` of the Makefile is required; without one `by hand` passes when every child's Estimate is a reading (112.1) or a sibling Estimate of the MOC names such a target (212); `pytest` or a path alone earns a finding.
> **＋** `is_old_shape` counts a page as old-shaped on any of four triggers: no `method` field, a `## Context` section, a `## Method` section, a `### case N` block in the Criterion.
> **＋** `method_of` takes the `method` field, and without it the `## Method` section; 23 live Estimates carry no field and keep the section.
> **＋** An `update` of an Estimate with `sections: Criterion` keeps the written text and does not take the Criterion from the Case (204); the page carries a `method` field, so case 211.2 does not refuse it.

> **when:**
> The agent reads `vault/wiki/estimates/schema.yaml` before writing a `create` of an Estimate.

> **then:**
> The description of `method` names the four forms as a list: a `make <target>` of the Makefile; the word `pytest`; a path under `tests/`; or the words `by hand` — the one spelling of a reading — with where and when it is taken.
> **＋** It says that naming a form is not enough by itself: a path under `tests/` must exist and a `make <target>` must stand in the Makefile.
> **＋** It says that on the Estimate of a MOC the form is a `make <target>` of the Makefile alone; there `pytest` or a path by itself earns a finding, and `by hand` passes only when every child's Estimate is a reading or a sibling Estimate of the MOC names such a target.
> **＋** It says that a page counts as the shape before case 193 on any of four triggers — no `method` field, a `## Context` section, a `## Method` section, a `### case N` block in the Criterion — and goes into the line `unmigrated`; and that a page with no field which keeps a `## Method` section has that section read as its `method`, so it can earn a `method` finding as well.
> **＋** A `method` that names none of the forms earns a finding of the class `method`.
> **＋** For `Research` what is measured stands beside one of the forms, never instead of one.
> **＋** `estimate-estimates-schema-checked` goes to `pending` with its Criterion unchanged, and is read again after the render.
> **－** The field stays `optional`.

```then
update:
  - slug: rule-estimates-schema
    replace:
      - old: "optional; one line. How the promise is checked: the test command (`make test-x`, `pytest tests/test_x.py`); or where and when it is read by hand — a live reading of a session start, the brief of a librarian's run; or, for Research, what is measured. Written from the Case since case 193."
        new: "optional; one line. How the promise is checked, in one of the four forms lint classifies: a `make <target>` of the Makefile; the word `pytest`; a path under `tests/`; or the words `by hand` — the one spelling of a reading — with where and when it is taken, a session start, the brief of a librarian's run. Naming a form is not enough by itself: a path under `tests/` must exist and a `make <target>` must stand in the Makefile. On the Estimate of a MOC the form is a `make <target>` of the Makefile alone — there `pytest` or a path by itself earns a finding, and `by hand` passes only when every child's Estimate is a reading or a sibling Estimate of the MOC names such a target. A `method` that names none of the forms earns a finding of the class `method`. A page counts as the shape before case 193 on any of four triggers — no `method` field, a `## Context` section, a `## Method` section, a `### case N` block in the Criterion — and goes into the line `unmigrated`; one with no field that keeps a `## Method` section has that section read as its `method`, so it can earn a `method` finding as well. For `Research` what is measured stands beside one of the forms, never instead of one. Written from the Case since case 193 (case 350)."
    change: the description of method names the four forms, what lint checks besides naming one, and the four triggers of the old shape (case 350, supersedes 330.2, 336 and 343)
  - slug: estimate-estimates-schema-checked
    set: {status: pending}
    sections:
      Criterion: |
        Given:
        `rule-render-harness`: the text of a `## Render` section of a page with `render_mode: full`, between its markers, becomes the whole file named by `governs`, without the markers; two `full` pages on one file fail the render (`tests/test_render.py`).
        **＋** `rule-governed-files-hook` refuses a hand edit of a file a live rule governs.
        **＋** `rule-lint` reads from `vault/wiki/<category>/schema.yaml` `properties.required`, `optional`, `values`, `conditional` and `body.required`, `optional`, `conditional`; a missing file is a finding; other keys it does not read.
        **＋** `tests/test_schemas.py` fixes the behaviour on the live `vault/wiki/estimates/schema.yaml`: a page in the shape, then one defect at a time.

        When:
        `guppi render` writes `vault/wiki/estimates/schema.yaml` from `rule-estimates-schema`; `guppi lint` reads a page of `wiki/estimates/`.

        Then:
        The file equals the Render. Lint reads from it: required `type, kind, status, target, origin, sprint, created, tags`; optional `purpose, method, checked`; values `kind: QA | Research`, `status: pending | passed | failed`; the sections `## Criterion` and `## History` required, `## Context`, `## Method`, `## Result` optional, `## Result` required on `passed` and on `failed`.
        **＋** An Estimate page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect.
        **＋** The prose of the former `schema.md` stands in the file as data: `description` — the introduction, the `failed` paragraph, the fields deliberately absent, the two kinds, the Result and Criterion paragraph, verbatim; `fields` and `sections` — the rows of the tables whole; `examples` — the two example pages.
        **－** `vault/wiki/estimates/schema.md` does not exist.
    change: the live reading is due again — the description of method in the Render changed; the Criterion stands (case 350)
```

```tasks
- [ ] update `rule-estimates-schema` — the replace pair in the description of `method` inside the Render
- [ ] update `estimate-estimates-schema-checked` — `set: {status: pending}` and `sections: Criterion` verbatim
- [ ] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`
- [ ] read `estimate-estimates-schema-checked`
```

## Case 344 — the Criterion and the `method` of this Estimate speak of the source segment (supersedes 338.1)

> **context:**
> Case 338.1 of the conserved Spec brings the Criterion of `estimate-prespec-binds-a-sprint-line` to what the code does after case 335: the test runs on the source segment of a Frontier line — the one before the closer — and not on every segment. It changes the `When` and the `－` line and leaves the `method` field in the old wording: the last case of the run there still reads "a line without sprint among its segments". After 335 that case distinguishes nothing. The case that does is a line where the word `sprint` stands inside the slug of a title while the source segment is another word — the false positive `prespec --check` prints today on line C6 of session 1724, whose source is `brief` and whose title holds `estimate-sprint-migration-index-dissolved`.
> The page stands `passed`, its target is `rule-prespec`. Case 335 of the same Spec changes `prespec.check_frontier` and `estimate-prespec-checks-the-plan`, not this page. The page carries no `estimates` field of its own.

> **problem:**
> The Criterion moves to the source segment while the `method` still tells the reader to run the old case; a reading taken by that method measures what the code no longer distinguishes.

> **given:**
> The `When` of the Criterion reads "a Frontier line whose segments hold `sprint`", its `－` line "A line without `sprint` among its segments is read as today".
> **＋** Its `method` ends with the words "a line without sprint among its segments".
> **＋** Case 335 narrows the test to the segment standing before the closer.
> **＋** A `replace` pair whose `old` stands in `## Criterion` changes a part and sets the page `pending` (296); a `set` of a field other than `status` changes that field alone (296).
> **＋** The command of the method stays `uv run pytest tests/test_prespec.py -k sprint`, so the form of `method` holds for lint.

> **when:**
> `uv run guppi prespec --check` reads a Frontier line closed `· case N`.
> **＋** The next reading of the page is taken by its `method` field.

> **then:**
> The `When` of the Criterion speaks of the source segment — the one before the closer — and not of every segment.
> **＋** The `－` line says: a line whose source segment is not `sprint` is read as today; the word inside the slug of a title is not the source.
> **＋** The `method` names as the last case of its run a line whose source segment is not `sprint` while the word stands inside the slug of its title.
> **＋** The `method` keeps its command, `uv run pytest tests/test_prespec.py -k sprint`.
> **－** The rest of the Criterion does not change; the page goes to `pending` and is read again.

```then
update:
  - slug: estimate-prespec-binds-a-sprint-line
    set:
      method: "uv run pytest tests/test_prespec.py -k sprint — a line `· sprint · case N` with and without an update of entity-sprint-<id> under Case N, a `[-] … · sprint` line, a line whose source segment is not `sprint` while the word stands inside the slug of its title"
    replace:
      - old: "reads a Frontier line whose segments hold `sprint` and whose closer is `case N`."
        new: "reads a Frontier line whose source segment — the one before the closer — is `sprint` and whose closer is `case N`."
      - old: "**－** A line without `sprint` among its segments is read as today."
        new: "**－** A line whose source segment is not `sprint` is read as today; the word inside the slug of a title is not the source (case 335)."
    change: the Criterion and the method speak of the source segment of a Frontier line (case 344, supersedes 338.1)
```

```tasks
- [ ] update `estimate-prespec-binds-a-sprint-line` — two `replace` pairs inside the Criterion and `set: {method: …}`
- [ ] read `estimate-prespec-binds-a-sprint-line`
```

## Case 351 — the machine that simulates the pairs, with the live reading named (supersedes 345)

> **context:**
> Case 345 gives `pre-spec` a check of the anchors and leaves two defects. First: it changes the Render of `rule-prespec` and does not name `estimate-prespec-reconciles`, the live reading of that Render, `passed`, whose method is one reading by hand of the first `/pre-spec` after the render. That is the breach of case 187 which 341 and 342 exist to repair and which 347, 349 and 350 of this plan all observe. Second: it gives the Insight `addressed_by` as a list of two links, while the schema of an Insight requires one quoted wikilink — unlike `deferred_by`, which the same schema calls a list; all nine live Insights carry one.
> `rule-prespec` stands `built`, a Leaf; the anchor of the pair stands once in it; the pair of case 335 of the conserved Spec touches another span. Two Estimate items in one `then` block each need a written `sections: Criterion`, or one wording is signed twice, so the Criterion of the created Estimate is written out. `estimate-prespec-checks-the-plan` is not named: a new check of `--check` has its own Estimate, as in cases 327 and 331.

> **problem:**
> The Case changes a Render without naming its live reading, and writes `addressed_by` in a form the schema does not know.

> **given:**
> `prespec --check` reads the plan and the live pages of the vault; it has no check of an anchor at all.
> **＋** `generate` applies the pairs in entry order and matches with whitespace collapsed, exactly one occurrence.
> **＋** The pairs of one Spec can touch one span: 314.2 against 310.6.
> **＋** An Insight is the target of the `update` that closes or rejects it; `actioned` sends its `clustered` children to the archive by the cascade.

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` reads the plan before the Spec is approved.

> **then:**
> The `replace` and `reword` pairs of every Case of the plan are applied in entry order to copies of the pages in memory, whitespace collapsed as `generate` collapses it; nothing is written to disk.
> **＋** An anchor that misses, or hits more than once, gives one line with its Case, the page's slug and the opening of its `old`.
> **＋** The anchor is judged against the page as the Spec leaves it, not as it stands today.
> **＋** The Insight moves to `actioned`, its `addressed_by` naming the Decision of this Case.
> **＋** `estimate-prespec-reconciles` goes to `pending` with its Criterion unchanged, and is read again after the render.
> **－** The meaning of the words in their place is not judged by a machine: that half is the requirement for signing a pair in `case-schema.md`.

```then
create:
  - slug: estimate-prespec-simulates-the-pairs
    type: estimate
    ref: rule-prespec
    kind: QA
    purpose: Whether pre-spec catches an anchor that misses or is not unique once the pairs of the Spec are applied in entry order
    method: pytest tests/test_prespec.py on a temp plan over temp pages — an anchor that misses, one that hits twice, and a pair whose old is produced by an earlier Case
    tags: [harness, workflow]
    sections:
      Criterion: |
        Given:
        `prespec --check` reads the plan and the live pages of the vault; it has no check of an anchor at all.
        **＋** `generate` applies the pairs in entry order and matches with whitespace collapsed, exactly one occurrence.
        **＋** The pairs of one Spec can touch one span: 314.2 against 310.6.
        **＋** `tests/test_prespec.py` fixes `--check` on a temp plan over temp pages.

        When:
        `uv run guppi prespec --check <plan> --session <id>` reads the plan before the Spec is approved.

        Then:
        The `replace` and `reword` pairs of every Case of the plan are applied in entry order to copies of the pages in memory, whitespace collapsed as `generate` collapses it; nothing is written to disk.
        **＋** An anchor that misses, or hits more than once, gives one line with its Case, the page's slug and the opening of its `old`.
        **＋** The anchor is judged against the page as the Spec leaves it, not as it stands today.
        **－** The meaning of the words in their place is not judged by a machine.
update:
  - slug: rule-prespec
    replace:
      - old: "an Estimate has its own line and its own item (case 189)."
        new: "an Estimate has its own line and its own item (case 189). It then applies the `replace` and `reword` pairs of every Case of the plan to copies of the pages in memory, in entry order, whitespace collapsed as `generate` collapses it, writing nothing, and prints one line for every anchor that misses or hits more than once, with its Case, the page's slug and the opening of its `old` — the anchor judged against the page as the Spec leaves it, not as it stands today (case 351)."
    change: the pairs of the Spec simulated in entry order, an anchor that misses or is not unique reported with its Case (case 351, supersedes 332.2 and 345)
  - slug: estimate-prespec-reconciles
    set: {status: pending}
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
    change: the live reading is due again — the Render gained the simulation of the pairs; the Criterion stands (case 351)
  - slug: insight-workflow-edit-pair-signed-from-a-grep-fragment
    set:
      status: actioned
      addressed_by: decision-case-351
    change: actioned by the two halves of its Proposal — the requirement for signing a pair in case-schema.md and the simulation in pre-spec (case 351)
```

```tasks
- [ ] create `estimate-prespec-simulates-the-pairs`, `ref: rule-prespec`, with its Criterion written out
- [ ] update `rule-prespec` — the replace pair in the Render, after the clause on an Estimate's line (case 189)
- [ ] update `estimate-prespec-reconciles` — `set: {status: pending}` and `sections: Criterion` verbatim
- [ ] update `insight-workflow-edit-pair-signed-from-a-grep-fragment` — `set: {status: actioned, addressed_by: decision-case-351}`
- [x] `guppi/prespec.py` — the simulation of the pairs in entry order, whitespace collapsed as in `generate`
- [x] `tests/test_prespec.py` — an anchor that misses; an anchor that hits twice; a pair whose `old` an earlier Case produces is clean
- [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [x] read `estimate-prespec-simulates-the-pairs`
- [ ] read `estimate-prespec-reconciles`
```

## Case 347 — step 1 of `/carry` names the place of the brief frame, not only the file

> **context:**
> Step 1 of the `/carry` skill — the Render of `rule-carry-over` — tells the agent to rewrite `vault/wiki/brief.md` "by the frame of `rule-brief` (the Render in `.claude/agents/librarian-guppi.md`)". It names the file and not the place in it. The frame stands between the `rule-brief` markers of that file, lines 77–93 today, and nothing in the instruction says so. The event log of the day records what follows: at 20:43:03, five seconds after `Skill: carry`, `grep -n -i "brief" .claude/agents/librarian-guppi.md`, and at 20:43:05 `sed -n '77,92p'` of the same file — the search for the frame and then the read of the marker range. The path of the brief itself is not the defect: step 1 names `vault/wiki/brief.md` in full, and step 3 commits it by name.
> `rule-carry-over` stands `built`, a Leaf, `render_mode: full` over `.claude/skills/carry/SKILL.md`. Its one Estimate is `estimate-carry-over-writes`, `passed`, whose Criterion ends with a `－` line that the skill file equals the Render of the page; case 233.4 handled a change of this Render the same way — the page set `pending`, the Criterion kept. The reading of that Estimate needs a live `/carry`, so it falls to the next conserved session unless this one conserves again.

> **problem:**
> The instruction names the file that holds the frame and not the place in it, so the agent searches for what the instruction could have pointed at.

> **given:**
> The Render of `rule-carry-over` becomes `.claude/skills/carry/SKILL.md` whole; the file is not edited by hand.
> **＋** The frame of `rule-brief` stands between its markers in `.claude/agents/librarian-guppi.md`, which is itself a Render.
> **＋** `guppi render` replaces a line that is exactly `<!-- slug -->` inside a Render with that child's text, so a marker written on a line of its own inside this Render would become an inclusion.
> **＋** An `update` of a rule's `Render` touches the Estimate of the live reading of that Render (187); the live reading here is `estimate-carry-over-writes`, `passed`.

> **when:**
> The agent calls the skill `carry` after the person's answer at the fork and reads step 1.

> **then:**
> Step 1 of the skill names the frame by its place: the text between the `rule-brief` markers of `.claude/agents/librarian-guppi.md`.
> **＋** The markers are named in words, not written as markers, so the renderer does not read the line as an inclusion.
> **＋** `estimate-carry-over-writes` goes to `pending` with its Criterion unchanged, and is read again.
> **－** Nothing else of step 1 changes: the short shape, the omitted sections, the rule for Deferred and the Flags stand as they are.
> **－** `rule-brief` does not change.

```then
update:
  - slug: rule-carry-over
    replace:
      - old: "by the frame of `rule-brief` (the Render in `.claude/agents/librarian-guppi.md`), in its short shape as that frame says:"
        new: "by the frame of `rule-brief` — the text between the `rule-brief` markers of `.claude/agents/librarian-guppi.md` — in its short shape as that frame says:"
    change: step 1 names the place of the brief frame, not only the file that holds it (case 347)
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
    change: the Render changed under it — step 1 names the place of the frame; the Criterion stands (case 347)
```

```tasks
- [ ] update `rule-carry-over` — the replace pair in step 1 inside the Render
- [ ] update `estimate-carry-over-writes` — `set: {status: pending}` and `sections: Criterion` verbatim
- [ ] `uv run guppi render`: `.claude/skills/carry/SKILL.md`
- [ ] read `estimate-carry-over-writes`
```

## Case 349 — one allowed read of the ledger (supersedes 348)

> **context:**
> Case 348 wrote into the ban of the librarian's frame that every ledger line already stands in `materialize.yaml` with its `line`, `text` and `origin`, so the file is never needed. That is false. The ledger of session 0014 holds 64 lines; the yaml's entries cover 1–51, 58 and 60, and `unparsed` is empty. Lines 52–57, 59 and 61–64 have no entry: they are `estimate[...]` readings that folded into entries the run skipped. So the librarian went to the file not because the frame invited it but because the fact was nowhere else — "a ledger line this run did not apply" is the one fact the yaml lacks. A second inaccuracy: the entries the librarian appends at the synthesis carry no `line`, `text` or `origin`, and the frame reads those too.
> `rule-documentation` stands `draft`, a MOC; `estimate-documentation-completes` stands `failed` on this very reading. The gap in `materialize` is recorded as a lesson of this session and is not repaired here.

> **problem:**
> The ban sends the librarian to a place that does not answer the question the brief asks, which makes breaching the frame the only way to obey it.

> **given:**
> The frame of `rule-documentation` bans reading `ledger.md`, `plan.md`, `wiki/decisions/` and `vault/archive/`, and `spec.md` beyond its unticked `- [ ]` lines.
> **＋** The `Work` line of the brief requires the ledger line this run did not apply to be named.
> **＋** `materialize.yaml` holds no entry for a line whose reading folded into an entry the run skipped, and `unparsed` stays empty.
> **＋** A part inside a Criterion sets the page `pending` with no `set.status` (296).
> **＋** An `update` of a rule's `Render` touches the Estimate of the live reading of that Render (187); here it is `estimate-documentation-completes`.

> **when:**
> The librarian writes the `Work` line of the brief and must name the ledger line this run did not apply.

> **then:**
> The ban allows one read of `ledger.md` and no other: the count of its lines and the lines the yaml does not account for; the read is named in the report.
> **＋** The frame says why: a reading that folded into an entry the run skipped gets no entry of its own, so the yaml does not hold every line.
> **＋** Everything else in the ban stands: `plan.md`, `wiki/decisions/`, `vault/archive/`, a Spec beyond its unticked lines, and the ledger for any other purpose stay closed.
> **＋** The Criterion of `estimate-documentation-completes` names that one carve-out in place of its bare "no ledger"; the page goes to `pending`.
> **－** `rule-brief` does not change.
> **－** `rule-materialize` is not repaired here: the gap stands as a lesson.

```then
update:
  - slug: rule-documentation
    replace:
      - old: "what the scripts do with the yaml is written here."
        new: "what the scripts do with the yaml is written here. One read of `ledger.md` is allowed and no other: the count of its lines and the lines the yaml does not account for, for the `Work` line of the brief — a reading that folded into an entry the run skipped gets no entry of its own, so the yaml does not hold every line; name that read in the report (case 349)."
    change: the ban allows one read of the ledger — its line count and the lines the yaml does not account for (case 349, supersedes 333 and 348)
  - slug: estimate-documentation-completes
    replace:
      - old: "no ledger, no other part of a Spec, no plan, Decision page or archive file"
        new: "of the ledger only the count of its lines and the lines the yaml does not account for, named in the report (case 349); no other part of a Spec, no plan, Decision page or archive file"
    change: the Criterion names the one allowed read of the ledger (case 349)
```

```tasks
- [ ] update `rule-documentation` — the replace pair in the ban clause inside the Render
- [ ] update `estimate-documentation-completes` — the replace pair in the line on what it read; the page goes `pending`
- [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [ ] read `estimate-documentation-completes`
```

## Deferred

## Case 352 — the defer narrowed to `rule-skill-hi` (supersedes 346)

> **context:**
> Case 346 of this plan defers `rule-skill-hi` and `rule-prespec` with one question — what a Frontier closer must tell apart. Case 351 of the same plan changes the Render of `rule-prespec`. Case 186.2 stands in the Render of `rule-prespec` itself and in the Criterion of `estimate-prespec-reconciles`: a Case that changes a page another Case of the same plan defers is a finding, with no exception for disjoint spans. The mechanism is the reason — a defer writes `deferred_by` and the cascade takes the page from `built` to `draft`, so the text 351 ratifies would land on a page marked as carrying an open question.
> `rule-skill-hi` stands `draft`, a MOC; `rule-prespec` stands `built`, a Leaf, and this plan changes it in 351 while the conserved Spec changes it in 331 and 335. Case 334 was superseded by 339, 339 by 346; this Case supersedes 346. The `purpose` carries what neither 339 nor 346 said: a session that passes over an item of the sprint leaves no trace anywhere but the Frontier, which dies with the session.

> **problem:**
> The defer of a page and the change of that page stand in one plan. Either the question loses its second page, or the change waits a session.

```then
defer:
  - slug: rule-skill-hi
    type: rule
    purpose: What a Frontier closer must tell apart — whether a Work line closes in a second moment of its own, whether pre-spec requires closed lines under Cases alone, and whether sprint and defer case N stay two closers or become one, the file living one session while the state lives on the pages; and whether a session that passes over an item of the sprint leaves any trace at all, since today it leaves none. The question binds rule-prespec as well, whose closer clause cases 335 and 344 rewrite and whose Render case 351 changes, so that page carries no deferred_by
```
