<!-- approved 20:05:41 · session 77f266cf -->

# Spec — session 1736, 2026-09-30

## Case 547 — The Frontier is shown after every closed Frontier line in Plan Mode

> **context:**
> The Frontier is the list of open items for the session, kept in the session's `frontier.md`. The agent closes a line of it when the item ends. The paragraph of `rule-case-protocol` on the reply that acknowledges a ratification tells the agent to end that reply with a `## Frontier` heading, the lines of `frontier.md` and the question which item is next (case 167). The paragraph on the short form tells the agent to do the same after a defer the person asks for (case 461). No text covers a line closed in any other way. Examples are an `A` line closed by the person's answer, a `W` line closed by a reading, a `C` line that needs no decision, and items closed `[-] … · sprint · defer` or `[-] … · backlog · kept`. In session 1736 the agent closed A1 (`estimate-permissions`) and C3 (`estimate-glossary-terms-defined`) as `· work`. Each reply ended with only the question which item is next, so the person did not see what was still open.
> The Case adds one sentence to the paragraph "Plan Mode and the Frontier" of the Render of `rule-case-protocol`, which renders into `vault/wiki/case-schema.md`, and creates an Estimate for the new promise. The Estimate has a `ref`, so no vault query on its existence was run. A Glob for `estimate-case-protocol-shows-the-frontier*` found no page, so the slug is free.
> Frame. `estimate-case-protocol-acknowledging-reply` and `estimate-case-protocol-defers-in-one-reply` stand. Their triggers are a ratification and a defer, and the new sentence excludes both. `estimate-case-protocol-loaded` checks only that the file equals the Render (case 378.5). The case-form, ledger-line-form and shows-the-built-case Estimates speak of other things.
> Pre-spec found that the first reply of `/hi` can also close `W` lines by a reading. `rule-skill-hi` sets its own form for that reply: the Cases as a checklist with their detail and `- near` lines, `Backlog: N items` last, the Work as one block, and then a wait for the person to pick the order. The rule of this Case therefore holds only after the first reply of `/hi`, and that reply keeps its form. With that bound, the Criterion of `estimate-hi-writes-frontier`, which sets the chat form of the `/hi` reply, stays true and is not touched.
> Search. A Grep for `Frontier` over `.claude/` and over `glossary.md` found no other sentence the change makes false. In `.claude/skills/hi/SKILL.md`, the reply to an `A` answer after the first reply carries a `LEDGER` block and ends in text. A Frontier after the block keeps that true, so `estimate-hi-takes-its-readings` stands. The hits in `.claude/skills/work/SKILL.md`, `.claude/skills/pre-spec/SKILL.md`, `.claude/skills/carry/SKILL.md` and `.claude/agents/librarian-guppi.md` speak of Work Mode, pre-spec and the handoff, where no Frontier is shown. The glossary rows "Plan Mode" and "`/hi`, Frontier" say nothing about what a later reply shows.
> The backlog item `rule-orchestration` (deferred by cases 424 and 546) would move the acknowledging reply into a rule of its own. It stays deferred. This sentence moves with the rest of that paragraph when the item is taken up.

> **problem:**
> A reply that closes a Frontier line with no ratification and no defer does not show the Frontier. The person does not see what is still open before choosing the next item. The rule names the Frontier only for the reply after a ratification and the reply after a defer.

> **recommend:**
> - **When must the agent show the Frontier after it closes a line?**
>   Recommended: every closed line from `/hi` to the end of Plan Mode; Work Mode and Retro unchanged.
>   Answer: agreed, as recommended; the first reply of `/hi` is excluded by the change below.
> - **What does the Frontier look like in these replies?**
>   Recommended: the same form as after a ratification, with the last question as after a defer: which item is next, or whether to run `/pre-spec` when no Cases line is open.
>   Answer: agreed, as recommended.
> - **How is the new behaviour checked?**
>   Recommended: a new Estimate on `rule-case-protocol`; `estimate-case-protocol-acknowledging-reply` stays as it is.
>   Answer: agreed, as recommended.
> - **Should the larger item `rule-orchestration` that was put off come into this Case?**
>   Recommended: leave it in the backlog; this Case adds one sentence to `case-schema.md` through `rule-case-protocol`.
>   Answer: agreed, as recommended.
> - **Change**
>   Asked: at pre-spec, the rule holds after the first reply of `/hi`, and that reply keeps its own form set by `rule-skill-hi`; `rule-skill-hi` enters `given`.
>   Taken: `when`, `then` and the new sentence start after the first reply of `/hi`; a `－` line of `then` keeps the form of that reply; `rule-skill-hi` is in `given`.
> - **Change**
>   Asked: at pre-spec, `context` says that `estimate-hi-writes-frontier` stays true with this bound.
>   Taken: `context` says so.

> **given:**
> `rule-case-protocol`: its Render paragraph "Plan Mode and the Frontier" takes the new sentence
> **＋** `vault/wiki/case-schema.md`: the Render of `rule-case-protocol`, loaded by `/hi`
> **＋** `rule-skill-hi`: sets the form of the first reply of `/hi`, which this Case leaves as it is
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session, whose lines the agent closes
> **＋** `/pre-spec`: the check that closes Plan Mode, named in the last question
> **＋** `estimate-case-protocol-shows-the-frontier-after-a-closed-line`: the new Estimate of the promise
> **＋** `estimate-case-protocol-acknowledging-reply`: the form of the Frontier that the new reply repeats

> **when:**
> After the first reply of `/hi` and before the end of Plan Mode, the agent closes a line of `raw/<date>/<hi HHMM>/frontier.md` in a reply that carries no ratification and no defer. Examples are an `A` line closed by the person's answer, a `W` line closed by a reading, a `C` line that needs no decision, or an item closed `[-] … · sprint · defer` or `[-] … · backlog · kept`.

> **then:**
> The reply ends with the heading `## Frontier` and the lines of `raw/<date>/<hi HHMM>/frontier.md` as a checklist, in the form that `estimate-case-protocol-acknowledging-reply` sets. The closed lines are folded into one, the open ones stand one per line with a short title, and the lines put off stand as they are closed.
> **＋** A question follows the Frontier and ends the reply: which open item is next, or, when no line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, whether to run `/pre-spec`.
> **＋** A reply that closes several lines shows one Frontier, after its `LEDGER` block when it carries one.
> **－** The first reply of `/hi` keeps the form that `rule-skill-hi` sets, the lines it closes included.
> **－** A line closed in Work Mode or at Retro shows no Frontier.
> **－** The reply that acknowledges a ratification and the reply that carries a defer keep their own form, as `estimate-case-protocol-acknowledging-reply` sets it.

```then
create:
- slug: estimate-case-protocol-shows-the-frontier-after-a-closed-line
  type: estimate
  ref: rule-case-protocol
  kind: QA
  purpose: Whether a reply after the first reply of /hi that closes a Frontier line in Plan Mode with no ratification and no defer ends with the Frontier and the question which item is next
  method: 'by hand, in a later session: the first reply in Plan Mode after the first reply of /hi that closes a line of frontier.md with no ratification and no defer, read against the Criterion'
  tags:
  - session
  - workflow
update:
- slug: rule-case-protocol
  replace:
  - old: (case 451.1). Plan Mode does not end
    new: '(case 451.1). A reply after the first reply of `/hi` and before the end of Plan Mode that closes a line of `frontier.md` with no ratification and no defer — an `A` line by the person''s answer, a `W` line by a reading, a `C` line that needs no decision, an item closed `[-] … · sprint · defer` or `[-] … · backlog · kept` — ends as the acknowledging reply ends: a heading `## Frontier`, the lines of `frontier.md` as a checklist in its form, and, last, the question which open item is next or, when no line under `## Cases` is open, whether to run `/pre-spec`; a reply that closes several lines shows one Frontier; the first reply of `/hi` keeps the form `rule-skill-hi` sets, and a line closed in Work Mode or at Retro shows none (case 547). Plan Mode does not end'
  change: a reply after the first reply of /hi that closes a Frontier line in Plan Mode with no ratification and no defer shows the Frontier and the question which item is next
```

```tasks
- [ ] update `rule-case-protocol`
- [ ] create `estimate-case-protocol-shows-the-frontier-after-a-closed-line`
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-protocol-shows-the-frontier-after-a-closed-line`
```

## Case 548 — The schema tests match the live Decision schema, and its promise names the tests it runs

> **context:**
> `tests/test_schemas.py` checks each page schema against its live file. One test, written for case 513.1, builds the smallest Decision page the schema accepts, removes `## Context`, and first asserts that the page still holds `## Problem` and `## History`. Case 544.8 made `## Problem` optional, and the librarian rewrote `vault/wiki/decisions/schema.yaml` from its rule page. Now the smallest accepted page holds `## History` alone, so the test fails on its setup before it checks for findings. The brief of session 1306 records the result: 1 failed, 964 passed, 2 skipped. The schema is right. The Criterion of `estimate-decisions-schema-checked` already says that a page without `## Context`, and a page without `## Problem`, get no finding.
> The same file holds three tests that skip themselves until the librarian rewrites a schema file: the test of `method` on an Estimate page (case 506.1), and the two Decision-page tests (cases 513.1 and 544.8). All three files have been rewritten, so the skips no longer happen. They would only hide a regression. A Grep of the repository outside `vault/raw/` and `vault/archive/` for the words of these skips finds them only in `tests/test_schemas.py`.
> The method line of `estimate-decisions-schema-checked` is out of date in two ways. It does not name a page without `## Problem`. Its lint reading also expects findings on the pages of Cases 1–28 for a missing `## Problem`, and the brief says those findings went away with the new schema file. The frame also shows that its command, `pytest tests/test_schemas.py -k decisions`, does not select the two Decision-page tests: pytest matches `-k` against the test names, and theirs contain `decision_page`, not `decisions`. The earlier reading, 4 passed and 1 skipped, fits the five tests that run once for each category. The new method runs `-k decision`, which selects those five tests and the two Decision-page tests. This keeps the person's choice that the method names both pages. The method of `estimate-estimates-schema-checked` has the same gap: `-k estimates` does not select the test of `method`. That promise is outside this Case, so it stays for a later session. A Grep of the repository outside `vault/raw/` and `vault/archive/` for `estimate-decisions-schema-checked` finds `brief.md`, `log.md`, the `estimates` field of `rule-decisions-schema`, and Decision pages, and no code. `brief.md` and `log.md` were not read for this, and the field of `rule-decisions-schema` only links the promise. So no other live text repeats the method.
> `rule-ledger-write` refuses a reading of a promise that a decision line of the same session updates. So the reading of `estimate-decisions-schema-checked`, on today's list of work, waits for a later session. The person chose this over reading the promise today under the old method. The update changes the `method` field alone. The Criterion and the `pending` status stay, and no Criterion is replaced. The Criterion of `estimate-estimates-schema-checked` stands: the test of `method` still checks the same behaviour, and it now runs every time. No reader of a text changes, so no old form needs to be kept. This Case creates no page, so no vault query ran.

> **problem:**
> A test of the Decision schema fails on its own setup after the schema made `## Problem` optional, although the schema and its promise are right. Three tests still skip on text that the schema files no longer hold. The method of the schema's promise names neither the page without `## Problem` nor a command that runs the Decision-page tests, and it expects lint findings that are gone.

> **recommend:**
> - **How should the out-of-date test be fixed?**
>   - Recommended: add `## Problem` to the page in the test, remove `## Context`, and expect no finding.
>   - Answer: agreed.
> - **Should the "skip until the file is rewritten" lines be removed?**
>   - Recommended: remove the skip from all three tests.
>   - Answer: agreed.
> - **Should the method line of the schema's promise be fixed too?**
>   - Recommended: rewrite the method line so that it names a page without `## Context` and a page without `## Problem`, and expects no schema finding on `wiki/decisions/`.
>   - Answer: agreed.
> - **Fix the method line now, or read the promise today?**
>   - Recommended: fix the method line now, and read the promise in a later session.
>   - Answer: fix the method line now; the reading waits for a later session.
> - **Change**
>   - Asked: correct the claim of `context` about the Grep for `estimate-decisions-schema-checked`, so that it states what the Grep printed.
>   - Taken: `context` names the hits `brief.md`, `log.md`, the `estimates` field of `rule-decisions-schema` and Decision pages, and says why none of them repeats the method.

> **given:**
> `tests/test_schemas.py` — the tests of the page schemas on the live files
> **＋** `uv run pytest tests/test_schemas.py` — the command that runs every test of the file
> **＋** `pytest tests/test_schemas.py -k decision` — the command of the method, which selects the tests of the Decision schema by name
> **＋** `vault/wiki/decisions/schema.yaml` — the live schema of a Decision page that the tests read
> **＋** `vault/wiki/estimates/schema.yaml` — the live schema of an Estimate page that the test of `method` reads
> **＋** `estimate-decisions-schema-checked` — the promise of the Decision schema, whose method this Case sets
> **＋** `rule-ledger-write` — the rule that holds a reading of a promise the session changes for a later session

> **when:**
> `uv run pytest tests/test_schemas.py` runs over the live schema files, and the reading of `estimate-decisions-schema-checked` follows its method.

> **then:**
> The test of a Decision page without `## Context` takes the page in the shape, adds `## Problem`, removes `## Context`, and finds no `schema` finding.
> **＋** The test of a Decision page without `## Problem` and the test of an Estimate page without `method` run on every call, and no test of `tests/test_schemas.py` skips on the text of a schema file.
> **＋** A schema file whose required lists go back to their older text makes these tests fail, not skip.
> **＋** `tests/test_schemas.py` passes on the live files of `vault/wiki/decisions/schema.yaml` and `vault/wiki/estimates/schema.yaml`.
> **＋** The method of `estimate-decisions-schema-checked` runs `pytest tests/test_schemas.py -k decision`, which selects the tests for each category and the two Decision-page tests, names a page without `## Context` and a page without `## Problem`, and expects no schema finding on `wiki/decisions/` in `make lint`.
> **－** The Criterion and the `pending` status of `estimate-decisions-schema-checked` do not change.
> **－** The reading of `estimate-decisions-schema-checked` is not taken in this session, as `rule-ledger-write` requires.

```then
update:
- slug: estimate-decisions-schema-checked
  set:
    method: 'pytest tests/test_schemas.py -k decision on the live vault/wiki/decisions/schema.yaml — a page in the shape, a page without ## Context, a page without ## Problem, then one defect at a time; the live reading make lint, no schema finding on wiki/decisions/'
  change: 'the method runs -k decision, names a page without ## Problem, and expects no schema finding on wiki/decisions/ (case 548)'
```

```tasks
- [ ] update `estimate-decisions-schema-checked`
- [x] `tests/test_schemas.py`: the test of a Decision page without `## Context` adds `## Problem` to the page in the shape itself; the skip on the text of the schema file and the words "Skipped until" of the docstring are removed from the tests of cases 506.1, 513.1 and 544.8
- [x] `uv run pytest tests/test_schemas.py`: every test passes, with no skip but the tests of a conditional on a category that has none
```

## Case 549 — The texts on `deferred_by` point to `rule-case-protocol` for when a supersede clears a defer

> **context:**
> A page carries `deferred_by`, a list of the Decision pages whose `defer` put off work on it. While that list is not empty, the page stands in `backlog.md`. `guppi generate` adds a decision to the list on a `defer`. It takes the decision out only on the pages that a decision line of the later, superseding Case names (case 467.3). So when one earlier Case put off two pages and a later Case supersedes it but names one of them, the other page keeps the defer and stays in the backlog. Several texts describe this rule. Some say that any `supersedes` clears the field: the glossary row `deferred_by`, two sentences each in `rule-rules-schema` and `rule-entities-schema`, the field text of `rule-insights-schema`, and the module docstring of `guppi/materialize.py`. Others state the condition in full: `rule-case-protocol`, whose Render is `case-schema.md`; the glossary row `ref`, `slug`, `supersedes`, corrected by case 541; a clause of `rule-prespec`; and a sentence of `rule-backlog`. The schema texts are rendered into the `schema.yaml` file of each folder, the glossary into `glossary.md`, and `rule-prespec` into the skill file of `/pre-spec`. At case 541 the person chose to leave the looser texts. The handoff of session 1306 carried them on as an open item, and the person now takes them up. The person chose to keep the condition on one page only, `rule-case-protocol`, and to have every other vault text point to it instead of repeating it.
> The texts were found by Greps of `vault/wiki/`: for `clear` in any case, for `deferred_by`, and for the words of the condition (`only from the pages`, `names its page`, `both names the page`), plus a Grep of `guppi/` for `deferred_by`. History lines, `log.md`, `brief.md` and the Decision pages were not read. Some hits stand as they are. `rule-case-check`, the docstrings of `guppi/prespec.py` and `guppi/casecheck.py`, and the check that `rule-prespec` describes all say what a check reports, not when `generate` clears a defer. The Criteria of `estimate-generate-writes-the-decision-page` and `estimate-prespec-requires-a-backlog-item-decided-on-its-page` state the behaviour that their readings measure, and a promise must state what it checks. The docstrings of `guppi/generate.py` describe the code that clears the field. The docstring of `guppi/materialize.py` is wrong today, not made wrong by this Case: it says a `{supersedes}` takes the slug out of the target's `deferred_by`, and it does not say that `generate` does this or on what condition. It enters the Case as a docstring fix, with no test.
> This Case holds only `update` items, so no vault query was run. It adds no hook and changes no reader of a text. No old form needs to be kept. The Estimates of the changed pages were read, and none is touched. `estimate-glossary-terms-defined` asks that no row contradict its `where` page. The row `deferred_by` and its page `rule-rules-schema` change the same way, and the row `ref`, `slug`, `supersedes` points to its own `where` page. The `-schema-checked` Estimates of the three schemas list what each file holds, not the words of the `deferred_by` text. In the Insight one, the rows of the tables stay whole, one text per field. The Estimates of `rule-prespec` and `rule-backlog` speak of what the check reports and of the render. They do not speak of the reason clause or of when an item leaves. The `given` holds more than seven lines because each changed page stands beside the file it renders into. The Case stays whole because one condition holds for every text: each one points to `rule-case-protocol`. A wrong text is fixed the same way in each place, and no promise is touched.

> **problem:**
> The rule for when a supersede clears a defer is written in full on several pages. Some copies leave out the condition that the superseding Case names the page, so they contradict `rule-case-protocol` and the code. The fix must remove the copies that repeat the rule, so that the condition stands in one place and the other texts point to it.

> **recommend:**
> - **Which texts change**
>   - Recommended: the three pages the item names and the Insight schema too, so that every live text that describes clearing `deferred_by` is covered.
>   - Answer: agreed.
> - **How the texts state the condition**
>   - Recommended: each text states the condition in its own words.
>   - Answer: the person asked why the texts should not point to one place instead. One judgment written in several places is several implementations of it. The next question settled this.
> - **Where the condition stands, and what the other texts say**
>   - Recommended: the condition stands on `rule-case-protocol`, and the texts point to it.
>   - Answer: agreed. The person also asked to take in two remarks. First, the glossary row `ref`, `slug`, `supersedes`, which states the condition in full, also becomes a pointer. Second, the other full copies are checked: each vault text either points to `rule-case-protocol` or stands with a reason given in `context`.

> **given:**
> `entity-glossary` — the table of terms whose rows `deferred_by` and `ref`, `slug`, `supersedes` this Case changes
> **＋** `vault/wiki/glossary.md` — the render of the table, loaded at the start of every working session
> **＋** `rule-rules-schema` — the Rule schema, which describes `deferred_by`
> **＋** `vault/wiki/rules/schema.yaml` — its render, read by lint and by the writer of a Rule page
> **＋** `rule-entities-schema` — the Entity schema, which describes `deferred_by`
> **＋** `vault/wiki/entities/schema.yaml` — its render, read by lint and by the writer of an Entity page
> **＋** `rule-insights-schema` — the Insight schema, which describes `deferred_by`
> **＋** `vault/wiki/insights/schema.yaml` — its render, read by lint and by the librarian
> **＋** `rule-prespec` — the skill `/pre-spec`, whose check of a backlog item gives the condition as its reason
> **＋** `.claude/skills/pre-spec/SKILL.md` — the render of `rule-prespec`
> **＋** `rule-backlog` — says when an item leaves `backlog.md`
> **＋** `guppi/materialize.py` — its module docstring describes what a `{supersedes}` does to `deferred_by`
> **＋** `guppi/generate.py` — the code that clears `deferred_by`
> **＋** `rule-case-protocol` — the page that states the condition, which the other texts point to

> **when:**
> A reader reads `vault/wiki/glossary.md` at the start of a session, `vault/wiki/rules/schema.yaml`, `vault/wiki/entities/schema.yaml` or `vault/wiki/insights/schema.yaml` when a page is written, `.claude/skills/pre-spec/SKILL.md` when the skill runs, `rule-backlog` or `guppi/materialize.py`, after the librarian's run wrote the rendered files from their pages.

> **then:**
> The rows `deferred_by` and `ref`, `slug`, `supersedes` of `entity-glossary` and of `vault/wiki/glossary.md` say that `guppi generate` clears a defer on a later `supersedes` under the condition that `rule-case-protocol` sets, and do not state the condition themselves.
> **＋** The text on `deferred_by` in `rule-rules-schema`, `rule-entities-schema` and `rule-insights-schema`, and in `vault/wiki/rules/schema.yaml`, `vault/wiki/entities/schema.yaml` and `vault/wiki/insights/schema.yaml`, says the same, both in the field text and in the sentence on ref fields of the Rule and Entity schemas.
> **＋** `.claude/skills/pre-spec/SKILL.md`, rendered from `rule-prespec`, gives the reason for its check of a backlog item by the same pointer, and `rule-backlog` says by the same pointer when an item leaves `backlog.md`.
> **＋** The module docstring of `guppi/materialize.py` says that `generate` takes the slug of a superseded decision out of a target's `deferred_by` under the condition that `rule-case-protocol` sets.
> **＋** `rule-case-protocol` states the condition, and no text that this Case changes states it again.
> **－** The check that `rule-prespec` describes does not change: it reports the same Frontier lines and pages as before.
> **－** `guppi/generate.py` and the docstrings of its code do not change.

```then
update:
- slug: entity-glossary
  replace:
  - old: written by `guppi generate` on a defer, cleared when a later Case `supersedes` that one;
    new: written by `guppi generate` on a defer and cleared by it on a later `supersedes` of that one, under the condition that `rule-case-protocol` sets;
  - old: '`generate` clears a defer only from the pages that a decision line of the superseding Case names (cases 200.2, 429, 467.3)'
    new: '`generate` clears a defer under the condition that `rule-case-protocol` sets (cases 200.2, 429, 467.3)'
  change: 'the rows deferred_by and ref, slug, supersedes: a supersede clears a defer under the condition that rule-case-protocol sets (case 549)'
- slug: rule-rules-schema
  replace:
  - old: cleared on a `supersedes` by `guppi generate`, never by hand
    new: cleared on a `supersedes` by `guppi generate`, under the condition that `rule-case-protocol` sets, never by hand
  - old: Written by `guppi generate` on a defer, cleared when a later Case `supersedes` that one;
    new: Written by `guppi generate` on a defer and cleared by it on a later `supersedes` of that one, under the condition that `rule-case-protocol` sets;
  change: deferred_by is cleared on a supersedes under the condition that rule-case-protocol sets (case 549)
- slug: rule-entities-schema
  replace:
  - old: cleared on a `supersedes` by `guppi generate`, never by hand
    new: cleared on a `supersedes` by `guppi generate`, under the condition that `rule-case-protocol` sets, never by hand
  - old: Written by `guppi generate` on a defer, cleared when a later Case `supersedes` that one;
    new: Written by `guppi generate` on a defer and cleared by it on a later `supersedes` of that one, under the condition that `rule-case-protocol` sets;
  change: deferred_by is cleared on a supersedes under the condition that rule-case-protocol sets (case 549)
- slug: rule-insights-schema
  replace:
  - old: set by `generate`, cleared by a `supersedes` (case 124.2)
    new: set by `generate` and cleared by it on a later `supersedes`, under the condition that `rule-case-protocol` sets (case 124.2)
  change: deferred_by is cleared on a supersedes under the condition that rule-case-protocol sets (case 549)
- slug: rule-prespec
  replace:
  - old: '`generate` clears a defer only from the pages the superseding Case names (case 467.1)'
    new: '`generate` clears a defer under the condition that `rule-case-protocol` sets (case 467.1)'
  change: the reason of the backlog check points to rule-case-protocol for when generate clears a defer (case 549)
- slug: rule-backlog
  replace:
  - old: a Case that decides it names its page on a decision line and supersedes its defer (case 467.3)
    new: a Case that decides it supersedes its defer under the condition that `rule-case-protocol` sets (case 467.3)
  change: an item leaves when a Case supersedes its defer under the condition that rule-case-protocol sets (case 549)
```

```tasks
- [ ] update `entity-glossary` — the rows `deferred_by` and `ref`, `slug`, `supersedes` point to `rule-case-protocol` for the condition
- [ ] update `rule-rules-schema` — the sentence on ref fields and the field `deferred_by` point to `rule-case-protocol`
- [ ] update `rule-entities-schema` — the sentence on ref fields and the field `deferred_by` point to `rule-case-protocol`
- [ ] update `rule-insights-schema` — the field `deferred_by` points to `rule-case-protocol`
- [ ] update `rule-prespec` — the reason of the check of a backlog item points to `rule-case-protocol`
- [ ] update `rule-backlog` — when an item leaves points to `rule-case-protocol`
- [x] `guppi/materialize.py`: the module docstring says that a `{supersedes:case N}` makes the earlier decision `superseded`, and that `generate` takes its slug out of a target's `deferred_by` under the condition that `rule-case-protocol` sets (case 52.3)
- [ ] `uv run guppi render`: `vault/wiki/rules/schema.yaml`
- [ ] `uv run guppi render`: `vault/wiki/entities/schema.yaml`
- [ ] `uv run guppi render`: `vault/wiki/insights/schema.yaml`
- [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [ ] `uv run guppi glossary`
```

## Case 550 — The parent Decision pages of session 0248 are kept as written

> **context:**
> Case 544.6 gave a Case with sub-cases a decision record of its own in `materialize`, and case 544.7 gave it a Decision page in `generate`. `materialize` goes over every session folder still under `raw/`, including folders it has processed before. So the librarian run of session 1306 added parent records to the older folder `raw/2026-09-30/0248/`, and `generate` wrote `decision-case-534`, `decision-case-538` and `decision-case-539` from them. The handoff of 1306 noted that nobody had decided this for Cases of earlier sessions. Each of the three pages holds the ratified `## Problem` of its Case and a `children` list of its sub-case pages. A Grep of `^(parent|## )` over the sub-case pages of 534, 538 and 539 found `## Problem` on each of them and `parent` on none. Those pages were written before 544, and the Criterion of `estimate-generate-writes-the-decision-page` says existing Decision pages are not rewritten. Parent Cases of archived sessions have no page. The other older folder under `raw/`, `raw/2026-09-30/0138/`, has no sub-case line in its ledger. `guppi archive` moves both older folders out at the first run on a later day (`rule-raw-archive`), so after that no folder from before 544 stays under `raw/`, and the code has no case left to limit. The three pages hold text no Case signed. Case 358 is the model for this: an `update` with `change` alone, which adds one `updated:` History line and changes nothing else. `rule-decisions-schema` allows that line for a Case that signs a page's text after the fact. That same schema text says a sub-case page carries `parent` and no `## Problem`, which the older sub-case pages contradict. The person keeps that sentence as it is: Decision pages move to the archive over time, and an added exception would stay behind to describe pages already archived. No Estimate is touched. The code of `materialize` and `generate` does not change, and the only thing that changes on the three pages is a History line. This Case creates nothing, so no vault query was run.

> **problem:**
> The librarian run of session 1306 wrote parent Decision pages for Cases 534, 538 and 539 of session 0248, and no Case decided that for Cases ratified before case 544. The question was whether to keep these pages, change them or remove them, and whether to limit the code that wrote them.

> **recommend:**
> - **What to do with the three parent pages**
>   Recommended: (a) keep them as they are; their sub-case pages keep no link back.
>   Answer: (a) keep them as they are.
> - **Should `materialize` be limited so that it adds no parent record to an older folder**
>   Recommended: (a) no code change; after the two older folders are archived, the case cannot happen again.
>   Answer: (a) no code change.
> - **Should `rule-decisions-schema` say how sub-case pages written before the new rule look**
>   Recommended: (a) add one sentence: a sub-case page written before case 544 keeps its `## Problem` and carries no `parent`.
>   Answer: (b) leave the text as it is. Decision pages move to the archive over time, and the added sentence would stay behind and describe pages that are already archived.

> **given:**
> `decision-case-534`, `decision-case-538`, `decision-case-539` — the parent pages that the librarian run of session 1306 wrote for Cases of session 0248
> **＋** `rule-decisions-schema` — a decision is not edited; one `updated:` History line of a Case that signs the page's text after the fact is allowed
> **＋** `guppi/materialize.py` — writes the parent record of a Case whose sub-cases stand in a folder under `raw/`
> **＋** `guppi/generate.py` — writes the Decision page of the record and applies an `update` with `change` alone as one History line

> **when:**
> The librarian's `uv run guppi generate` applies this Case.

> **then:**
> `decision-case-534`, `decision-case-538` and `decision-case-539` keep their fields and their `## Problem` as they stand, and the History of each gets one line `updated:` naming this Case as the one that signs the page after the fact.
> **－** The sub-case pages of Cases 534, 538 and 539 do not change: they carry no `parent` and keep their `## Problem`.
> **－** `guppi/materialize.py` and `guppi/generate.py` do not change.
> **－** The text of `rule-decisions-schema` does not change.

```then
update:
- slug: decision-case-534
  change: the parent page written for a Case of session 0248 by the librarian run of session 1306, kept as written and signed after the fact (case 550)
- slug: decision-case-538
  change: the parent page written for a Case of session 0248 by the librarian run of session 1306, kept as written and signed after the fact (case 550)
- slug: decision-case-539
  change: the parent page written for a Case of session 0248 by the librarian run of session 1306, kept as written and signed after the fact (case 550)
```

```tasks
- [ ] update `decision-case-534`
- [ ] update `decision-case-538`
- [ ] update `decision-case-539`
```

## Case 552 — A ledger line that the parser cannot read no longer stops the ledger hook

> **context:**
> At the end of each reply of the main agent, the `Stop` hook `guppi ledger` reads every record line inside a `LEDGER` block of the session's transcript. It checks each fresh line with `parse_line` of `guppi/materialize.py` and appends the lines to the session's `ledger.md`. In session 2026-09-30/1736 the main agent wrote a reading with a space between its brackets: `estimate[estimate-spec-write-copies-the-ratified-case] [passed]`. For that line, the estimate branch of `parse_line` cut the first bracket off and then matched the second bracket at the start of the rest. The rest opened with a space, so the match was None and `.end()` raised `AttributeError`. The lesson branch had the same two steps. The hook caught every exception, printed `ledger: ledger.md not written: <error>` to stderr and exited 0, so nobody saw the failure. It reads the whole session again at each `Stop`, so this one line kept every later line of the session out of the ledger. A dry run of `ledger.run` gave rc 0 and that stderr line. `guppi ratified` failed on the same reply and did not write the short form of Case 551 under `## Deferred`. It reads only the finished reply, so Case 551 must be shown again, and this Case does not change `guppi ratified`. The person chose two fixes. First, `parse_line` returns None where it would raise, and a test covers this. Second, the ledger hook exits 2 on an error. With the person's consent, the main agent built the code of 552.1 before the Spec and outside Work Mode, to unblock the ledger: `parse_line` and its tests in `tests/test_materialize.py`. At 19:47:50 the hook wrote the 20 waiting lines. Line 29 of `vault/raw/2026-09-30/1736/ledger.md` is the line with the space, which now reads as a reading. Line 30 is its corrected copy. `guppi/ledger.py` is unchanged. The tasks of 552.1 stand, and Work Mode ticks them after it checks them. The rounds settled the choices inside the two fixes. `parse_line` reads a space between brackets for every kind of line, as the decision branch already does (552.1). The hook refuses a line that `parse_line` cannot read (552.2). That refusal makes the Criterion of `estimate-ledger-write-lifts` false, because it says every record line lands, so the Criterion is replaced whole with one more `－` line (552.3). The crash exit gets its own Estimate (552.4). The hook reads `stop_hook_active` from the payload inside the same `try`. So an error while it reads the payload exits 0 with the error on stderr: the hook cannot tell a re-fire then, and exit 2 could loop. Only an error after the payload is read exits 2. The other `Stop` hooks in `.claude/settings.json` (`guppi ratified`, `guppi casecheck`, `guppi context`, `guppi onward`) each catch their own errors and exit 0. They stay as they are, and a change to them is a later item. The Criterion of `estimate-materialize-assembles` already says that a line the grammar does not parse goes under `unparsed` and the run goes on. The crash broke that promise, and 552.1 restores it, so that Estimate is not touched. Its readings taken this session stand. A Grep of `parse_line|does not parse|cannot parse` over the live pages of `vault/wiki/` outside `decisions/` found `rule-ledger-tail`, `rule-raw-archive`, `rule-prespec`, `estimate-ledger-tail`, `estimate-raw-archive`, `estimate-prespec-checks-the-plan`, `estimate-spec-write-checks-the-written-case` and `estimate-render-harness-reproduces`, the latter about JSON files. It also found the actioned `insight-ledger-line-written-unchecked` and `insight-materialize-lift-loses-a-schema-field`. Each one reads record lines through `parse_line`, says that a line that does not parse is no finding of its check, or tells the history of a line that did not parse. A wider grammar shared by one function keeps each of them true. The Estimates of `rule-ledger-write` that refuse a reading, a lesson without its prefix and a mark with no decision line judge only lines that `parse_line` reads, so they stand. The check of the answer noted that `then` lines of 552.2, 552.3 and 552.4 share words. The sub-cases stay separate because they make different promises. 552.3 copies the Criterion of `estimate-ledger-write-lifts` as it stands and names the refusal of 552.2 only by its slug. 552.4 exits 2 on an error of the hook, not on a refused line. The ledger hook refuses a reading of an Estimate that a decision line of the session creates or updates (case 428.1). So a reading of `estimate-ledger-write-lifts` taken this session is refused once 552.3 is ratified, and it waits for a later session. Each new Estimate has a `ref`, so this Case runs no vault query. Grep shows that neither new slug exists.

> **problem:**
> An estimate or lesson line with a space between its brackets made `parse_line` raise instead of return. The ledger hook swallowed the error and exited 0, so the line and every later line of the session went unwritten, and nobody was told. The question was how `parse_line` reads such a line, what the hook does with a line it cannot read, how the hook reports its own error, and how these promises are recorded.

> **recommend:**
> - **How the promise of the crash exit is recorded**
>   Recommended: (a) a new Estimate of `rule-ledger-write` for the crash exit; `estimate-ledger-write-lifts` keeps its text.
>   Answer: (a) a new Estimate.
> - **Change**
>   Asked: correct the facts of `context`: the full list of Grep hits, and the ledger as it stands after the code of 552.1 was built and the waiting lines were written.
>   Taken: `context` names the three missing hits and says that none of them is made false. It tells the failure in the past tense, and it says that the code of 552.1 was built before the Spec, that the hook wrote the 20 waiting lines at 19:47:50 with the line with the space at line 29 and its corrected copy at line 30, and that `guppi/ledger.py` is unchanged.

### Case 552.1 — `parse_line` reads a space between brackets and never raises

> **recommend:**
> - **What `parse_line` does with a space between the brackets**
>   Recommended: (b) read it as a decision line is read; return None only for a line it still cannot read.
>   Answer: (b) read it, like a decision line.

> **given:**
> `rule-materialize` — the rule of the lift of the ledger, whose code holds the one parse of a ledger line
> **＋** `guppi/materialize.py` — `parse_line`, the one parse of a ledger line
> **＋** `tests/test_materialize.py` — the tests of the lift and of `parse_line`
> **＋** `estimate-materialize-assembles` — its Criterion sends a line the grammar does not parse to `unparsed`

> **when:**
> A caller passes one ledger line to `parse_line` of `guppi/materialize.py`.

> **then:**
> A `decision`, `estimate` or `lesson` line gives the same record with or without spaces between two of its brackets that follow each other.
> **＋** A line that `parse_line` cannot read returns None, and no exception leaves `parse_line`.
> **－** A line with no space between its brackets gives the same record as before.

```then
update:
- slug: rule-materialize
  replace:
  - old: of the ledger is an entry.
    new: of the ledger is an entry. `parse_line` reads a record line with or without spaces between its brackets, and returns None, never an error, for a line it cannot read (case 552.1).
  change: parse_line reads a space between brackets and returns None, never an error, for a line it cannot read (case 552.1)
```

```tasks
- [ ] update `rule-materialize`
- [x] `guppi/materialize.py`: `parse_line` reads an `estimate` or a `lesson` line with spaces between its brackets, and returns None for a line it cannot read; the docstring says so
- [x] `tests/test_materialize.py`: an `estimate` line and a `lesson` line with a space between the brackets give the record of the same line without it; a broken line of each kind returns None; a line without spaces gives the record it gave before
```

### Case 552.2 — The ledger hook refuses a line it cannot read

> **recommend:**
> - **What the ledger hook does with a line `parse_line` cannot read**
>   Recommended: (b) refuse it at once: not written, exit 2 with one stderr line when it stands in the reply just finished.
>   Answer: (b) refuse it at once.

> **given:**
> `rule-ledger-write` — the rule of the `Stop` hook that writes the ledger lines
> **＋** `guppi/ledger.py` — `run` and the refusals of fresh lines
> **＋** `guppi/materialize.py` — `parse_line`, the one parse of a ledger line
> **＋** `tests/test_ledger.py` — the tests of the hook
> **＋** `estimate-ledger-write-refuses-a-line-it-cannot-read` — the promise this sub-case creates

> **when:**
> The `Stop` hook `uv run guppi ledger` finds a fresh line `- decision[`, `- estimate[` or `- lesson[` in a `LEDGER` block of the session, and `parse_line` of `guppi/materialize.py` returns None for it.

> **then:**
> The line is not written.
> **＋** The other lines of the `Stop` are written as before.
> **＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: line not written — the grammar of a ledger line does not read it: <line>. Write it again in the form of the table in case-schema.md."
> **＋** At every later `Stop`, a refused line from an earlier text of the transcript is skipped without a word.
> **－** A refused line gets no other refusal of the hook and no other stderr line.
> **－** A line already in the ledger of any session is not judged again.
> **－** Without a `hi`, and with `stop_hook_active`, the hook acts as before and judges no line.

```then
create:
- slug: estimate-ledger-write-refuses-a-line-it-cannot-read
  ref: rule-ledger-write
  kind: QA
  purpose: Whether the ledger hook refuses a record line that parse_line cannot read, and says why only for the reply just finished
  method: uv run pytest tests/test_ledger.py — piped payloads and a session ledger in a temp vault
  tags:
  - session
  - hooks
  - harness
  - ledger
update:
- slug: rule-ledger-write
  replace:
  - old: A refused line from an earlier text is judged again at every `Stop`, without a word, until a decision line of its Case stands before it, and is written then.
    new: A refused line from an earlier text is judged again at every `Stop`, without a word, until a decision line of its Case stands before it, and is written then. A line that `parse_line` of `guppi/materialize.py` cannot read is not written, since `materialize` would put it under `unparsed` and the record it holds would be lost (case 552.2); it is judged before the other refusals and gets no other; as for a refused reading, the hook exits 2 with one stderr line per refused line only when the line stands in the reply just finished, skips an older one without a word, and writes the other lines as before.
  change: the hook refuses a line that parse_line cannot read (case 552.2)
```

```tasks
- [ ] update `rule-ledger-write`
- [ ] create `estimate-ledger-write-refuses-a-line-it-cannot-read`
- [x] `guppi/ledger.py`: `run` sets apart each fresh line that `parse_line` cannot read before the other refusals, does not write it, and prints its stderr line when it stands in the reply just finished; the docstring says so
- [x] `tests/test_ledger.py`: a broken line in the reply just finished (exit 2, one stderr line, the other lines written); the same line from an earlier text (exit 0, no word, not written); a broken lesson line gets no refusal for its prefix or mark
- [ ] read `estimate-ledger-write-refuses-a-line-it-cannot-read` — in a later session
```

### Case 552.3 — The main promise of the ledger hook names the new refusal

> **recommend:**
> - **Should the ledger hook's main promise change to allow for the new refusal?**
>   Recommended: (a) add the new refusal to the main promise; it goes back to unchecked.
>   Answer: (a) add the new refusal to the main promise.

> **given:**
> `estimate-ledger-write-lifts` — the promise whose Criterion this sub-case replaces
> **＋** `rule-ledger-write` — the rule of the `Stop` hook that writes the ledger lines
> **＋** `raw/<hi date>/<hi HHMM>/ledger.md` — the session's ledger
> **＋** `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` — a refusal the Criterion names
> **＋** `estimate-ledger-write-refuses-a-lesson-without-its-prefix` — a refusal the Criterion names
> **＋** `estimate-ledger-write-refuses-a-mark-with-no-decision-line` — a refusal the Criterion names
> **＋** `estimate-ledger-write-refuses-a-line-it-cannot-read` — the refusal of 552.2, which the Criterion now names

> **when:**
> The `Stop` hook `uv run guppi ledger` fires at the end of a turn of the main agent, with `transcript_path` and `last_assistant_message` in its payload; or `guppi gate` refuses a `Skill` call for an item of the Spec without a ledger line.

> **then:**
> In a session with a `hi` recorded, every line `- decision[`, `- estimate[`, `- lesson[` inside a `LEDGER` block of any text of the main agent in the transcript, the reply just finished included, lands in `raw/<hi date>/<hi HHMM>/ledger.md` with the time of writing, once — a body already in the ledger of any session is not written again.
> **＋** A block in a text followed by a tool call in the same turn reaches the ledger at the next `Stop` of the session, with the time of that `Stop`; the reply that ends in the text lands it now.
> **＋** The gate's advice to the agent reads "The text before a tool call waits for the next Stop: end this reply in text with the LEDGER block, then call /<skill> in the next reply."
> **－** A line the hook refuses by `estimate-ledger-write-refuses-a-line-it-cannot-read` does not land.
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
  change: the Criterion replaced whole — a line the hook cannot read does not land (case 552.3)
```

```tasks
- [ ] update `estimate-ledger-write-lifts`
- [ ] read `estimate-ledger-write-lifts` — in a later session
```

### Case 552.4 — The ledger hook exits 2 on its own error

> **recommend:**
> - **Which hooks stop the agent when they crash**
>   Recommended: (a) the ledger hook only; the same change for the other hooks is its own item in a later session.
>   Answer: (a) the ledger hook only.
> - **Change**
>   Asked: the sub-case contradicted itself, because an error while the payload is read comes before the hook knows it is a re-fire, and exit 2 there could loop; an error while reading the payload exits 0 with the error on stderr, and an error after the payload is read exits 2.
>   Taken: `when` names an error after the payload is read; `then` exits 2 for it, and a `－` line exits 0 with the error on stderr for an error while the payload is read; the new text of `rule-ledger-write` and the tests say the same.

> **given:**
> `rule-ledger-write` — the rule of the `Stop` hook that writes the ledger lines
> **＋** `guppi/ledger.py` — `run` and its handler of an error
> **＋** `tests/test_ledger.py` — the tests of the hook
> **＋** `estimate-ledger-write-exits-2-on-an-error` — the promise this sub-case creates

> **when:**
> The `Stop` hook `uv run guppi ledger` fires, and an exception rises in `run` of `guppi/ledger.py` after it has read the payload: while it reads the transcript, the event log or the ledger, or while it judges or appends the lines.

> **then:**
> The hook exits 2 with `ledger: ledger.md not written: <error>` on stderr, so the agent sees the error at the end of that reply.
> **＋** A line not yet appended when the error rose waits for the next `Stop` of the session, which reads the transcript again.
> **＋** While the cause stands, the error comes back at every `Stop`.
> **－** An error while the hook reads the payload exits 0 with the error on stderr: the hook cannot tell a re-fire then, and exit 2 could loop.
> **－** With `stop_hook_active` (the re-fire after a block) the hook exits 0 and writes nothing, so it cannot loop.
> **－** A refusal of the hook with no error — no `hi`, or a refused line — keeps its own stderr line and exit.

```then
create:
- slug: estimate-ledger-write-exits-2-on-an-error
  ref: rule-ledger-write
  kind: QA
  purpose: Whether the ledger hook exits 2 with the error on stderr when it raises after reading the payload, and exits 0 on an error while reading the payload and on the re-fire
  method: uv run pytest tests/test_ledger.py — piped payloads, a function of the hook patched to raise
  tags:
  - session
  - hooks
  - harness
  - ledger
update:
- slug: rule-ledger-write
  replace:
  - old: and writes nothing, so it cannot loop.
    new: 'and writes nothing, so it cannot loop. An error of the hook itself after it has read the payload — an exception while it reads the transcript, the event log or the ledger, or judges or appends the lines — exits 2 with `ledger: ledger.md not written: <error>` on stderr, so the agent sees it at the end of that reply; a line not yet appended waits for the next `Stop`, and while the cause stands the error comes back at every `Stop`. An error while it reads the payload exits 0 with the error on stderr, since the hook cannot tell a re-fire then (case 552.4).'
  change: the hook exits 2 on its own error after the payload is read, and 0 on an error while it reads the payload (case 552.4)
```

```tasks
- [ ] update `rule-ledger-write`
- [ ] create `estimate-ledger-write-exits-2-on-an-error`
- [x] `guppi/ledger.py`: `run` reads the payload in its own guard that prints the error and returns 0, and the handler of the rest prints the error and returns 2; the docstring says so
- [x] `tests/test_ledger.py`: a patched `append` that raises gives exit 2 and the stderr line; the same payload with `stop_hook_active` gives exit 0 and writes nothing; a payload that cannot be read gives exit 0 and the stderr line
- [ ] read `estimate-ledger-write-exits-2-on-an-error` — in a later session
```

## Deferred

## Case 551 — A round of case-guppi runs the parts of a list inside one sentence

> **context:**
> The reading of `estimate-case-build-writes-a-plain-round` in session 1736 read the first rounds of `case-guppi` on Cases 547 to 550. Each Context gives the mechanism with an example, its quotations stand as blockquotes, and no number stands alone. But the sentence on what the round decides runs its parts inside one sentence: on 548 and 550 it names three parallel clauses, and on 547 the Context names five examples in one sentence. `.claude/skills/grill-me/SKILL.md` sets a series of two or more parallel clauses one per line. The person put the fix off to take the readings first.

> **problem:**
> The Context of a first round of `case-guppi` carries a list inside a sentence, against the list rule of `grill-me`, so `estimate-case-build-writes-a-plain-round` stays failed.

```then
defer:
  - slug: rule-case-build
    type: rule
    purpose: The Context of a first round of case-guppi writes what the round decides, and a series of examples, one item per line as grill-me sets a list, never inside one sentence; estimate-case-build-writes-a-plain-round failed on this in session 1736
```

## Case 553 — ask-guppi may not open the Decision pages that case-guppi reads

> **context:**
> At the pre-spec of session 1736, `ask-guppi` could not check a claim of Case 550 about `decision-case-538` and `decision-case-539`: its frame `.claude/agents/ask-guppi.md`, the Render of `rule-ask`, forbids opening `vault/wiki/decisions/` except for the `## Problem` of a page's `deferred_by` or a Decision reached through `origin`. `case-guppi` read the same pages while it built the Case. The check of a Case at pre-spec reads less of the vault than the builder of the Case, so a fact about a Decision page in a `context` goes unchecked. The person asked to put the fix off.

> **problem:**
> The two agents that read the vault for a Case follow different rules on Decision pages, so a claim the builder reads from a Decision page cannot be checked at pre-spec.

```then
defer:
  - slug: rule-ask
    type: rule
    purpose: ask-guppi and case-guppi read Decision pages by one rule, so that a claim a Case makes about a Decision page can be checked at pre-spec; today case-guppi opens them and the frame of ask-guppi forbids it but for deferred_by and origin
```
