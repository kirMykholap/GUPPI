<!-- approved 23:37:56 · session 24564cfb -->

# Session 2252 — sprint plugin

## Case 782 — Pre-spec asks whether a Criterion needs a later session

> **context:**
> `/pre-spec` checks a plan in two ways. Code judges the `method` of an Estimate and reports one that waits for a later session, the librarian or `/hi`, unless a part of it waits for an event it names (cases 670.4, 781). One `ask-guppi` run at the first `/pre-spec` of a session answers open questions over the plan. Nothing asks the same of the `When` and `Then` of a Criterion. In session 1449 the `When` that Case 777 gave `estimate-sprint-close-next-session-opens-the-sprint` asked someone to read the Frontier, the ledger and the pages of the session after the close, while its method ran tests and read skill texts. The `ask-guppi` run caught it only through its question on contradictions, and the Case was built again as Case 779. Cases 780 and 781 left a check of this out. The person chose a judgment over a word list, since a word list cannot tell a Criterion that describes a later session from one that needs to observe it: the fixed `When` of Case 779 still names the librarian's run and the session that closes a sprint. So the `/pre-spec` skill, the Render of `rule-prespec`, asks `ask-guppi` one more question. The `ask-guppi` agent file, the Render of `rule-ask`, stops listing the questions and answers each question the skill sets, in its order, so the list stands in one place. Case 782.1 replaces the Criterion of `estimate-prespec-reconciles`, whose `method` reads the new Renders of both rules at the Retro of the session that changes them and stands. Case 782.2 replaces the Criterion of `estimate-ask-finds` and sets its `method` anew as a reading that waits for an event, since its old one waits for a `/hi` of a later session and `/pre-spec` reports a kept method of that kind. A Case built again after the first `/pre-spec` is not asked the new question: the person chose to keep this Case to `/pre-spec`, and `case-guppi` already judges each option for a reported defect against the rule it breaks (case 780). No code changes, and no `create` stands, so no vault query was run.
>
> In `rule-prespec` the sentence of the questions changes; the sentence on what the run reads already names the `when` and `then` of each Case, and the sentence that a later run dispatches no `ask-guppi` stays true. In `rule-ask` the sentence that lists the questions changes; the paragraph on the confirmation of findings and the line on what the agent did not check stay true. A Grep for `bear out|does not bear|speaks of the thing` over the repository with the glob `!vault/{archive,raw}/**` printed `.claude/skills/pre-spec/SKILL.md`, `.claude/agents/case-guppi.md`, `.claude/agents/ask-guppi.md`, `vault/wiki/rules/rule-case-build.md`, `vault/wiki/rules/rule-prespec.md`, `vault/wiki/rules/rule-ask.md`, `vault/wiki/estimates/estimate-prespec-reconciles.md` and `vault/wiki/estimates/estimate-ask-finds.md`. The two `.claude/` files of the skill and the agent follow their rules by the render. In `rule-case-build` and its Render `case-guppi.md` the words define what a contradiction is for `case-guppi`, not a question of `/pre-spec`, so they stand. No other Estimate of `rule-prespec` or `rule-ask` lists the questions; `estimate-ask-searches-at-prespec` names only the questions of the skill file, which stays true. In both replaced Criteria the line that listed the questions is rewritten, so the check notes it as not carried. The check also notes `then` lines of the two sub-cases that share most of their words; they stand, since one side sets what the main agent dispatches and reports and the other what `ask-guppi` answers. A Grep for `skills/pre-spec|skills" / "pre-spec|ask-guppi\.md|"ask-guppi"|rule-prespec\.md|rule-ask\.md|estimate-prespec-reconciles|estimate-ask-finds` over `tests/` printed `tests/test_casecheck.py`, whose hit passes the agent name `ask-guppi` with a made-up answer and reads none of these files, so no test reads a file this Case changes.

> **problem:**
> A Criterion whose `When` or `Then` needs a reading that only a later session can take passes `/pre-spec` unless the `ask-guppi` run happens to see it as a contradiction, since nothing asks about it by name.

> **recommend:**
> - **What form, if any, should a check on the `When` and `Then` take?**
>   - Recommended: (c) a fourth question for the `ask-guppi` run, a judgment of meaning, since a word list cannot tell describing a later session from needing to observe one.
>   - Answer: (c).
> - **How does the `ask-guppi` side learn about the fourth question?**
>   - Recommended: (b) name the questions only in the skill; `rule-ask` and `estimate-ask-finds` say the agent answers each question the skill sets, in its order.
>   - Answer: agreed, (b).
> - **How is the rewritten `estimate-ask-finds` read?**
>   - Recommended: (a) wait for a named event: a `/pre-spec` run after the render, its answer read in the agent transcript.
>   - Answer: agreed, (a).
> - **Does the builder of a Case also judge this, for Cases built again after the first `/pre-spec`?**
>   - Recommended: (a) no, the Case covers `/pre-spec` only.
>   - Answer: agreed, (a).

### Case 782.1 — The skill asks whether a Criterion needs a later session

> **given:**
> `rule-prespec`: the rule rendered into `.claude/skills/pre-spec/SKILL.md`, which sets the questions of the `ask-guppi` run.
> **＋** `estimate-prespec-reconciles`: its Criterion is replaced whole.
> **＋** `rule-ask`: the rule rendered into `.claude/agents/ask-guppi.md`, which the run follows.
> **＋** `rule-case-protocol`: sets in `vault/wiki/case-schema.md` what a `method` holds, a part that waits for an event it names, and the Estimate of a sprint page `entity-sprint-<id>`.
> **＋** `rule-spec-write`: the hook that writes a Case built again into the plan.
> **＋** `rule-skill-hi` and `/hi`: set the title line of the plan that names a conserved Spec; a `/hi` is one of the moments the new question names.
> **＋** `vault/raw/<date>/<hi HHMM>/frontier.md`: the Frontier, whose findings the agent fixes itself.
> **＋** `estimate-prespec-notes-a-page-another-case-defers`: the check of the note on a page another Case defers.

> **when:**
> The person invokes `/pre-spec`, or the agent calls the skill, before the Spec is approved, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec` and `.claude/agents/ask-guppi.md` rendered from `rule-ask`.

> **then:**
> The agent runs `uv run guppi prespec --check` on the plan file with `--session <id>`, the eight-character id of the `hi:` line, and reads the first line of the output before the exit code — "no hi recorded for session …; nothing checked" means the wrong value; nothing is translated before the run.
> **＋** A finding in a Case — in its prose or in its body, a wrong fact of its `context` included — goes to the `case-guppi` of that Case by `SendMessage`; its new answer is shown and ratified again, and the hook of `rule-spec-write` writes it into the plan; the agent does not edit the text of a Case in the plan file.
> **＋** A finding in `vault/raw/<date>/<hi HHMM>/frontier.md` or in a line of the session's ledger is fixed there, and the command runs again until it prints no finding.
> **＋** At the first run of `/pre-spec` in the session, the agent dispatches one `ask-guppi` over the plan, or over the conserved Spec that the plan's title line names, as `rule-skill-hi` sets that line, with the absolute path of the plan file, the instruction to judge every Case outside `## Deferred` with its sub-cases, and the instruction to read for each such Case its `context`, `when`, `then` and `then` block and, for an `update` of a rule or an entity, the page's `estimates`; of a Case under `## Deferred` it reads only the slugs of its `defer` items.
> **＋** The questions: which decisions contradict a page of the vault, a rule of the vault, or each other; whether an Estimate the Case does not name speaks of the thing the Case changes; which fact of a `context` — a page's status, a count, a case number, a claim that no page holds a thing — the vault does not bear out; and whether the `When` or `Then` of a Criterion a Case sets asks someone to read or see what only a later session, the librarian's run or a `/hi` produces, when the `method` of that Estimate, in the plan or else on its live page, cannot take that reading in the Case's own session.
> **＋** The agent answers the findings with one report before any Case is sent back: the list of what the `ask-guppi` run did not check; each finding numbered, with the fix it proposes or why it is already known, the findings that need the person apart from those that do not, and the decisions it needs from the person; after the Cases built again on the findings are ratified, it does not call `/pre-spec` again, but runs the check, fixes what it prints, and exits Plan Mode when the check prints no finding.
> **＋** `guppi gate` writes the stamped `prespec` line on the Skill call.
> **－** The last question finds nothing where a part of the `method` waits for an event it names that brings that reading, nor in the Criterion of an Estimate whose target is a sprint page `entity-sprint-<id>`, whose `method` may wait for a later session of its sprint.
> **－** No second `ask-guppi` is dispatched at the first run, and a later run of `/pre-spec` in the session dispatches none.
> **－** The report never says that the whole Spec is checked.
> **－** The agent writes no list of the decisions: the plan is the list.
> **－** The body of a deferred decision is not read, and `ask-guppi` is not asked whether a Case changes a page that another Case of the plan defers: `uv run guppi prespec --check` notes such a pair at every run, as `estimate-prespec-notes-a-page-another-case-defers` sets it.

```then
update:
- slug: rule-prespec
  replace:
  - old: 'Three questions: which of these contradict'
    new: 'The questions: which of these contradict'
  - old: the vault does not bear out (case 388). A later run in the session dispatches no `ask-guppi`
    new: the vault does not bear out (case 388); and whether the `When` or `Then` of a Criterion a Case sets — its `when` and `then`, or the Criterion its item writes — asks someone to read or see what only a later session, the librarian's run or a `/hi` produces, when the `method` of that Estimate, in the plan or else on its live page, cannot take that reading in the Case's own session; a part of the `method` that waits for an event it names and brings that reading, and the Estimate of a sprint page `entity-sprint-<id>`, whose `method` may wait for a later session of its sprint, are no such finding, as `case-schema.md` sets it (case 782). A later run in the session dispatches no `ask-guppi`
  change: the ask-guppi run at pre-spec is also asked whether the When or Then of a Criterion needs a reading only a later session can take (case 782)
- slug: estimate-prespec-reconciles
  set:
    status: pending
  change: the Criterion replaced whole — ask-guppi is also asked whether the When or Then of a Criterion needs a reading only a later session can take
```

```tasks
- [ ] update `rule-prespec`
- [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [ ] update `estimate-prespec-reconciles`
- [ ] read `estimate-prespec-reconciles`
```

### Case 782.2 — Ask-guppi answers each question the skill sets

> **given:**
> `rule-ask`: the rule rendered into `.claude/agents/ask-guppi.md`, whose answer at `/pre-spec` changes.
> **＋** `estimate-ask-finds`: its Criterion is replaced whole and its `method` set anew.
> **＋** `rule-prespec`: the rule rendered into `.claude/skills/pre-spec/SKILL.md`, which sets the questions.
> **＋** `rule-case-protocol`: sets in `vault/wiki/case-schema.md` a `method` that waits for an event it names.
> **＋** `vault/raw/<date>/event_log.md`: the event log that records the dispatch.
> **＋** `.claude/rules/search-leaves-out-decisions.md`: the search rule whose breaks the answer names.

> **when:**
> At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> The answer opens with one line that names what the agent read: the plan file, or the Spec that the plan's title line names, and the Cases it checked.
> **＋** Then stands one numbered list of findings under each question that `.claude/skills/pre-spec/SKILL.md` sets, in the order of that file.
> **＋** Each finding names its Case and the page or the Cases it bears on; a question with no finding says "none".
> **＋** A finding that names a page carrying `deferred_by` gives the `## Problem` of the Decision that field names.
> **＋** After the findings stands one list of what the questions ask that the agent did not check. The list says "none" when the agent checked all of it and its searches broke no rule of `.claude/agents/ask-guppi.md` or of `.claude/rules/search-leaves-out-decisions.md`. Its last lines name each rule of those files that a search broke, one line each, and say whether a finding rests on what that search printed. Then stands a list of the paths of the files the agent read.
> **＋** The dispatch stands in `vault/raw/<date>/event_log.md`.
> **－** The findings are not put under the lines `exists`, `near`, `missing`, `rules` and tags/slug: those lines answer a question whether a thing exists.
> **－** `.claude/agents/ask-guppi.md` does not list the questions of `/pre-spec` itself.
> **－** Nothing but its numbered findings, or "none" alone, stands under a question. No sentence says what the agent checked and found sound, and this includes a clash with another Case that it did not find.
> **－** No summary of the findings, no list of what holds, no index line and no page text reaches the caller.
> **－** An answer with no list of paths holds the promise as well.

```then
update:
- slug: rule-ask
  replace:
  - old: 'and asks which Case of the plan contradicts a page of the vault, a rule of the vault or another Case, which Estimate a Case does not name speaks of the thing the Case changes, and which fact of a `context` the vault does not bear out, answer instead with one numbered list of findings under each question, in that order:'
    new: 'and asks the questions that `.claude/skills/pre-spec/SKILL.md` sets, answer instead with one numbered list of findings under each question, in the order of that file (case 782):'
  change: at pre-spec ask-guppi answers each question the skill sets, in its order, and the agent file lists them no more (case 782)
- slug: estimate-ask-finds
  set:
    status: pending
    method: 'by hand, after a /pre-spec whose ask-guppi runs on .claude/agents/ask-guppi.md as rendered by case 782: the answer of ask-guppi in its agent transcript read against the Criterion and the event log, recorded in the estimate line'
  change: the Criterion replaced whole — one list of findings under each question the skill sets, in its order; the method waits for a /pre-spec after the render
```

```tasks
- [ ] update `rule-ask`
- [ ] `uv run guppi render`: `.claude/agents/ask-guppi.md`
- [ ] update `estimate-ask-finds`
- [ ] read `estimate-ask-finds`
```

## Case 783 — A defer of a check with no page is refused, not written as a stand-in page

> **context:**
> When the person puts an item off, the main agent writes a short Case with one `defer` line per page, and at the librarian's run `guppi generate` adds the decision to the page's `deferred_by`, through which the page enters `backlog.md`. When the page does not exist, `guppi generate` writes a stand-in page with `status: draft` and the fields the Case gave (the `defer` method of `guppi/generate.py`). That fits a rule or an entity page: lint gives such a page one `deferred` finding (case 186.3). For an Estimate it goes wrong. The format of an Estimate page allows only `pending`, `passed` and `failed`, and the stand-in has no `kind`, `target`, `method` or `## Criterion`, so lint would report it several times. No test covers this path (handoff of session 1604, For the next session). Case 781 made Estimates deferrable. A take-back already avoids the problem: it defers the page that each Estimate it creates would check (case 723.1). The person chose that a defer of an Estimate with no page writes no page. The short Case puts off the page the check would test instead. `/pre-spec` reports such a defer, and `guppi generate` fails the entry alone as a backstop. Each part replaces the Criterion of one existing Estimate. A Grep for `^status: draft` over the files `vault/**/estimates/*.md` printed no match, so no stand-in check page stands today and nothing needs to move.
>
> The person left the stand-in Insight page out. `guppi generate` gives it `status: draft` too, a value the Insight format does not allow (`open`, `actioned`, `archived`). Only the librarian creates Insights, so a defer of a missing Insight does not come up in practice. This Case does not fix it, and it stays open for a later Case.
>
> A Grep for ``placeholder page|draft placeholder|a placeholder `draft`|writes a placeholder|a placeholder —`` over `vault/wiki/`, with `log.md` and `brief.md` left out, printed `rule-brief.md`, `glossary.md`, `entity-glossary.md`, `rule-page-generation.md`, `estimate-generate-writes.md` and `estimate-lint-checks-the-statuses.md`. The sentence of `rule-brief` says that every deferred item lives on as a page, a draft stand-in or an open Insight. It stays true, because a check with no page is now put off through a page that stands. Its other hit is a History line. In `estimate-lint-checks-the-statuses` a stand-in is a rule or an entity, which stays true. The Types row of `entity-glossary`, rendered into `glossary.md`, says a defer writes a stand-in page when there is no `ref`, so Case 783.1 adds that an Estimate never gets one. The hit in `rule-page-generation` is the exception for a `create` over a stand-in page, which stays true for a rule or an entity. The line of `estimate-generate-writes` is rewritten by Case 783.1. A Grep for `always created|page is always` over `vault/wiki/`, `.claude/`, `guppi/` and `CLAUDE.md` printed `rule-page-generation.md` and `estimate-materialize-marks-a-comment.md`. The Purpose of `rule-page-generation` says a page is always created, even incomplete, which a refused defer makes false, so Case 783.1 adds the exception. In `estimate-materialize-marks-a-comment` the words say why `generate` applies an entry marked for a comment, which this Case does not touch. A Grep for `placeholder` over `guppi/` printed `guppi/render.py`, `guppi/glossary.py`, `guppi/generate.py`, `guppi/lint.py` and `guppi/materialize.py`. In `render.py` the word means a language placeholder, and in `glossary.py` a page with no `parent`. `is_placeholder` of `lint.py` judges only a rule or an entity, which stays true. The docstrings of `generate.py` and of the routing table of `materialize.py` say a defer with no page writes a stand-in, so both name the Estimate.
>
> In `rule-orchestration`, which Case 783.2 changes and which was read whole, the sentences on what a defer names are the take-back sentence and the sentence that the target of a short Case enters `backlog.md` through its `deferred_by`. The take-back sentence already defers the page an Estimate would check, so it stays true. The new sentence stands after the second one. The Criterion of `estimate-orchestration-defers-in-one-reply` asks for one `defer` item per target. The Criterion of `estimate-orchestration-defer-example-passes-the-hook` speaks of the example block, and the Criterion of `estimate-orchestration-takes-back-a-ratified-case` speaks of the take-back. All three stay true, so they stand. The Estimate that checks the new sentence is the `/pre-spec` finding of Case 783.2. In `entity-glossary`, read whole, the `deferred_by` row, the Estimate row and the Insight row stay true. The Criterion of `estimate-glossary-terms-defined` asks that no row contradict its `where` page, and `rule-case-protocol` says nothing of stand-in pages, so it stands. The `purpose` of `estimate-prespec-checks-the-form-of-an-item` already says an item names a page that exists or is created, so it stands, and so does its `method`. The change to the Purpose of `rule-page-generation` touches no Estimate (case 378.5). The `then` of Case 783.1 is the Criterion of `estimate-generate-writes` as it stands, with one line changed and one `－` line added. It keeps its eleven `＋` lines and one promise. Its `defer` line is rewritten, not dropped, so the check notes it as not carried. The `then` lines of Case 783.2 that speak of a defer share words with lines of Case 783.1. That is meant: 783.1 sets what `guppi generate` does with such a defer, and 783.2 sets what `/pre-spec` reports. These are two promises, checked by two Estimates.
>
> Shared code: a Grep for `def (page_exists|page_paths|archived_paths|live_page)\b` over `guppi/` printed `guppi/generate.py`, `guppi/materialize.py` and `guppi/prespec.py`. `page_exists` of `materialize.py` finds a page under `vault/archive/` at any depth outside `raw/`, whatever folder holds it. `find` of `generate.py`, through `archived_paths`, finds it only in a category folder. So the two answer differently for an Estimate archived outside a folder `estimates/`. Neither is taken as it stands. Case 783.1 adds `has_page` to `materialize.py`, which finds a page only in its own category folder, live or archived outside `raw/`. `guppi generate` and `/pre-spec` both import it, and `generate` asks it before `find`. A page that `has_page` finds is in a category folder, so `find` reaches it too. The tests of both sides put an Estimate in a folder other than `estimates/` under `vault/archive/`, where the two old functions part. A Grep for `has_page` over `guppi/` printed no match, so the name is free. The person was asked about the test of whether a page exists as the one `materialize` uses for a defer. It is now a new shared predicate, because `/pre-spec` found that the two existing functions disagree.
>
> The new finding also falls on a short Case under `## Deferred`. The Render of `rule-prespec` sends a finding in a Case to the `case-guppi` of that Case. A short Case has no `case-guppi`: `rule-orchestration` makes it the agent's own, written with no dispatch, and a wording the person corrects becomes a new short Case with `{supersedes:case N}` (case 405). The new sentence of `rule-orchestration` names that route for this finding, so the sentence of `rule-prespec` stands. It covers a Case that a `case-guppi` built. The rewritten `defer` line of `estimate-generate-writes` promises a stand-in page for a rule or an entity only and promises nothing for an Insight. The code still writes the Insight stand-in, and the docstring of `generate.py` says so only for a rule or an entity. That leaves the Insight defect to a later Case without a promise to replace. Tests that read live files: a Grep for `(ROOT|REPO)\s*/\s*"(vault|\.claude)"` over `tests/` printed `tests/test_case_schema.py`, `tests/test_schemas.py`, `tests/test_orchestration.py` and `tests/test_generate.py`. `test_orchestration.py` reads the blocks tagged `showing` and `defer` of `orchestration.md`. The new sentence adds no block, and the `defer` example names `entity-booking-export`, not an Estimate. `test_case_schema.py` runs the check of `guppi/casecheck.py`, which calls `prespec.judge`, over `case-example.md`. That file holds no `defer` item, so the new finding refuses none of it. `test_schemas.py` and `test_generate.py` read only the live `schema.yaml` files, which this Case does not change.

> **problem:**
> A defer of an Estimate with no page makes `guppi generate` write a stand-in check page whose status the check page format does not allow. Nothing in the session reports such a defer.

> **recommend:**
> - **What should a defer of a check that has no page do?**
>   - Recommended: (a) defer the page the check would test: a defer never makes a stand-in check page, and a defer of a check with no page that reaches `guppi generate` fails there alone.
>   - Answer: agreed, (a).
> - **Should this Case also fix the stand-in Insight page?**
>   - Recommended: (a) leave the Insight out; `context` notes the defect as found and not fixed.
>   - Answer: agreed, (a).
> - **What catches a defer of a check with no page before the librarian's run?**
>   - Recommended: (a) `/pre-spec` reports it, by the same test of whether a page exists that the step before `guppi generate` uses for a defer, and `guppi generate` refuses it as a backstop.
>   - Answer: agreed, (a).
> - **Which existing checks should cover the two changes?**
>   - Recommended: (a) two parts, each rewriting one existing check: `guppi generate` fails the defer and `estimate-generate-writes` is rewritten; `/pre-spec` reports it, the rule for short Cases gains one sentence, and `estimate-prespec-checks-the-form-of-an-item` is rewritten.
>   - Answer: agreed, (a).

### Case 783.1 — Generate writes no stand-in page for a check

> **given:**
> `rule-page-generation`: the rule of `guppi generate`, whose Purpose says a page is always created.
> **＋** `guppi/generate.py`: the `defer` of an entry and the module docstring.
> **＋** `guppi/materialize.py`: writes the yaml that `guppi generate` applies; its routing table names the defer with no page, and the new `has_page` is the one judgment whether a page stands, which `guppi/generate.py` and `guppi/prespec.py` import.
> **＋** `tests/test_generate.py`: the tests of `guppi generate`.
> **＋** `estimate-generate-writes`: its Criterion is replaced whole.
> **＋** `estimate-generate-fails-alone`: the Estimate of an entry that fails alone.
> **＋** `entity-glossary`: the terms, rendered into `vault/wiki/glossary.md`, whose Types row names the stand-in page of a defer.
> **＋** `vault/wiki/sprint.md`, `vault/wiki/log.md` and `vault/wiki/tags.md`: the files `guppi generate` reads or appends to; the sprint comes from `vault/wiki/sprint.md`, or from `entity-sprint-<id>` when a unit creates it.
> **＋** `vault/archive/`, outside its `raw/` folders: where an entry finds a page that is not under `vault/wiki/`.
> **＋** `vault/wiki/estimates/`, and a folder `estimates/` under `vault/archive/`: where the page of an Estimate stands.

> **when:**
> `guppi generate` applies one entry of a yaml to a page.

> **then:**
> A `create` becomes a page: `type`, the fields of the entry, `status` by category (entity and rule `draft`, estimate `pending`, lesson `new`, insight `open`), `origin`, `sprint` — the `sprint` of the yaml, which `guppi materialize` takes from the first `## <id>` of `sprint.md` or, in a unit whose ledger creates `entity-sprint-<id>`, from that `<id>`, `created` — the yaml's date, `tags`; the body sections from `sections`, `## Purpose` from `purpose` on a rule or an entity; a `ref` lands in the parent's `children` or the target's `estimates` with History `child <slug> added` / `estimate <slug> added`, at the end of the run when the parent comes later in the yaml.
> **＋** An Estimate page carries `purpose`, `method` and `checked` as fields, in that order after `target`, and `deferred_by` after `checked` once a `defer` marks it; `## Criterion` from `sections`; neither `## Context` nor `## Method` is written.
> **＋** A `create` whose slug is a placeholder (`draft`, no `kind`) fills it: `created` and `deferred_by` kept, History `created over placeholder`; any other existing page is a collision, not a rename.
> **＋** An `update` applies `set` to the frontmatter, `sections` as whole replacements, `replace` inside the body (whitespace collapsed, exactly one occurrence), History `updated: <change>`; an `update` of an Estimate with `sections.Criterion` replaces the section whole.
> **＋** An `update`, `estimate`, `delete` or `defer` whose slug is not under `vault/wiki/` finds the page under `vault/archive/` (`raw/` folders excluded) and edits it there.
> **＋** An `estimate` sets `status`, overwrites `## Result`, writes `checked` — the date the `result` opens with, else the yaml's date — and appends History `status: a → b · <ledger pointer>`.
> **＋** A `delete` sets `archived` with History `deleted`; a `delete` outside the vault is a line on stdout, the entry applied, no page written.
> **＋** A `defer` with a page appends the decision slug to `deferred_by` (rule, entity, insight, estimate) with History `deferred`; without a page it writes a placeholder `draft` with the Case's fields and `deferred_by` for a rule or an entity.
> **＋** A `lesson` writes the lesson only, `source` when the line carries it; no Estimate is created.
> **＋** Every ref field is written as `"[[slug]]"`, a list as `["[[a]]", "[[b]]"]`; a slug without a category prefix stays bare; read through the brackets.
> **＋** A `create` in `insights` applies only with the mark `librarian`; a `delete` of an Insight is refused always.
> **＋** History lines and `log.md` lines carry the date of the run and end with `[[decision-case-N]]` or the ledger pointer; `log.md` is appended after each entry; a tag of `new_tags` lands in `tags.md`, a used and undeclared one goes to stderr.
> **－** A `defer` of an Estimate whose page stands neither under `vault/wiki/estimates/` nor in a folder `estimates/` under `vault/archive/` outside a `raw/` folder, by `has_page` of `guppi/materialize.py`, writes no page: the entry fails alone with `generate: <slug>: an Estimate is deferred only with its page — defer the page it would check` on stderr (`estimate-generate-fails-alone`).
> **－** No body section is derived from a ref field; a section the entry does not name under `sections` or reach by `replace` is not touched.
> **－** An `update` of an Estimate whose `set` carries `method` drops no section.
> **－** `criterion_block` on an `update` and an entry of kind `remove_criterion` are not applied: a shape the script does not know — the entry fails alone (`estimate-generate-fails-alone`).

```then
update:
- slug: rule-page-generation
  replace:
  - old: 'A page is always created, even incomplete: red lint is an accurate signal of debt, a decision with no page is the ledger and the vault disagreeing silently.'
    new: 'A page is always created, even incomplete: red lint is an accurate signal of debt, a decision with no page is the ledger and the vault disagreeing silently. An exception is a `defer` of an Estimate with no page: it writes no page and fails as an entry, since a check that was never created has no reading to put off, and the short Case puts off the page it would check instead (case 783).'
  change: a defer of an Estimate with no page writes no placeholder and fails as an entry (case 783)
- slug: entity-glossary
  replace:
  - old: '`defer` postpones, a placeholder page when no `ref`'
    new: '`defer` postpones, a placeholder page when no `ref`, never for an Estimate, which is put off through the page it would check (case 783)'
  change: 'Types: a defer writes no placeholder for an Estimate (case 783)'
- slug: estimate-generate-writes
  set:
    status: pending
  change: the Criterion replaced whole — a defer of an Estimate with no page writes no placeholder and fails alone
```

```tasks
- [ ] update `rule-page-generation`
- [x] `guppi/materialize.py`: a new predicate `has_page(project_dir, category, slug)` — true when the page stands under `vault/wiki/<category>/`, or in a folder `<category>` under `vault/archive/` outside a `raw/` folder; its docstring names `guppi/generate.py` and `guppi/prespec.py` as the modules that import it; the line `defer none` of the routing table in the module docstring says that an Estimate gets no placeholder and its entry fails in `generate` (case 783).
- [x] `guppi/generate.py`: in `defer`, an entry of the category `estimates` for which `materialize.has_page` is false fails with `an Estimate is deferred only with its page — defer the page it would check`, before any page is read, and no page is written; the module docstring and the docstring of `defer` say that a placeholder is written for a rule or an entity, never for an Estimate (case 783).
- [x] `tests/test_generate.py`: a `defer` of an Estimate with no page writes no page, prints the line on stderr, exits 1 and lets the other entries apply; so does a `defer` of an Estimate whose file stands under `vault/archive/` in a folder other than `estimates/`, or under a `raw/` folder; a `defer` of an Estimate that stands in a folder `estimates/` under `vault/archive/` appends the decision to its `deferred_by` there.
- [ ] update `entity-glossary`
- [ ] `uv run guppi glossary`
- [ ] update `estimate-generate-writes`
- [ ] read `estimate-generate-writes`
```

### Case 783.2 — Pre-spec reports a defer of a check with no page

> **given:**
> `rule-prespec`: the rule of `/pre-spec`, the target of the Estimate.
> **＋** `rule-orchestration`: the rule rendered into `vault/wiki/orchestration.md`, which sets the short Case of a deferred decision.
> **＋** `guppi/prespec.py`: `check_form`, the check of the form of an item, and the module docstring.
> **＋** `guppi/materialize.py`: `has_page`, the one judgment whether a page stands, which Case 783.1 adds.
> **＋** `guppi/generate.py`: the `defer` that fails an entry of an Estimate with no page by the same judgment, by Case 783.1.
> **＋** `tests/test_prespec.py`: the tests of the check.
> **＋** `vault/wiki/estimates/`, and `vault/archive/` outside its `raw/` folders: where the page of an Estimate stands.
> **＋** `estimate-prespec-checks-the-form-of-an-item`: its Criterion is replaced whole.

> **when:**
> `uv run guppi prespec --check <plan>` reads the items of the plan's `then` blocks.

> **then:**
> A Case whose `then` block holds two or more Estimate items that set a new Criterion — a `create`, or an `update` that names no part of the page by `names_a_part` of `guppi/materialize.py` — is the finding `case N: two promises in one Case — split it`, whether each item writes its Criterion under `sections` or lifts it.
> **＋** An `update` of an Estimate whose page does not exist is the finding `case N: update <slug>: no such Estimate page`.
> **＋** A `defer` of an Estimate whose page stands neither under `vault/wiki/estimates/` nor in a folder `estimates/` under `vault/archive/` outside a `raw/` folder, by `has_page` of `guppi/materialize.py`, is the finding `case N: defer <slug>: no such Estimate page — defer the page it would check`, a short Case under `## Deferred` of the plan included.
> **＋** The judgment is `has_page` of `guppi/materialize.py`, which the `defer` of `guppi/generate.py` imports too.
> **＋** A `create` of an Estimate whose `ref` names neither a live rule or entity nor a rule or entity a `create` item of the plan carries is the finding `case N: create <slug>: ref <ref> names no live page`.
> **＋** An `update` item carrying `file` is the finding `case N: file <path>; the file route is gone (case 320)`, naming the rule that governs the path when one does.
> **＋** A key of an item of any kind that `item_keys` of `guppi/materialize.py` does not give its kind and category — `slug` a key of every kind — is the finding `case N: <kind> <slug>: key <key> is not a key of this item`.
> **－** An `update` of an Estimate that names a part alone — `set` without `status`, a `replace` pair, a section other than `Criterion` — is not counted.
> **－** A `defer` of a rule, an entity or an Insight with no page is not this finding.
> **－** A `create` or a `defer` of a category with no schema file, or of one whose schema rule a decision line of the session creates or updates, is not judged by its keys (case 308.2).

```then
update:
- slug: rule-orchestration
  replace:
  - old: The target of a short Case enters `backlog.md` through the `deferred_by` that `generate` writes.
    new: 'The target of a short Case enters `backlog.md` through the `deferred_by` that `generate` writes. A `defer` of an Estimate names a page that stands: a check not yet created is put off through the rule or entity page it would check, as a take-back does, and `/pre-spec` reports a `defer` of an Estimate with no page; the agent fixes that finding with a new short Case with `{supersedes:case N}` whose `defer` names the page the Estimate would check, as for a wording the person corrects (case 783).'
  change: a defer of an Estimate names a page that stands; a check not yet created is put off through the page it would check, and a pre-spec finding on such a defer is fixed by a new short Case that supersedes it (case 783)
- slug: estimate-prespec-checks-the-form-of-an-item
  set:
    status: pending
  change: the Criterion replaced whole — a defer of an Estimate with no page is a finding
```

```tasks
- [ ] update `rule-orchestration`
- [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
- [x] `guppi/prespec.py`: `check_form` reports a `defer` item of an Estimate for which `materialize.has_page` is false, with the line `case N: defer <slug>: no such Estimate page — defer the page it would check`; the module docstring and the docstring of `check_form` name it (case 783).
- [x] `tests/test_prespec.py`: a `defer` of an Estimate with no page, under a Case heading and under `## Deferred`, gives the finding, and so does one whose file stands under `vault/archive/` in a folder other than `estimates/`, or under a `raw/` folder; a `defer` of an Estimate that stands live or in a folder `estimates/` under `vault/archive/`, and a `defer` of a rule with no page, give none.
- [ ] update `estimate-prespec-checks-the-form-of-an-item`
- [ ] read `estimate-prespec-checks-the-form-of-an-item`
```

## Case 784 — case-guppi reads its sub-cases side by side by what they speak of, and searches for each changed field

> **context:**
> Before it answers, `case-guppi` compares the new texts of two of its sub-cases only when both change the same page (case 544.1). It searches the live pages only for the slug of each page whose text the change makes false, and for a fact that no slug marks it reads the index lines of the vault, which hold no glossary row and no Estimate. Case 781 of session 1604 had nine sub-cases over seven rules. Its 781.8 and 781.5 said different things about when an event reading reaches `/hi`, and 781.1 and 781.3 said only `Work` where 781.5 said `Work` or `Ask the person`; these sub-cases changed different pages, so no step compared them. A glossary row of `deferred_by` became false and two Estimates that speak of the change were not named, since neither names a changed slug. The ask-guppi run of `/pre-spec` found them, and the Case was shown three times; the lesson `lesson-case-build-sub-cases-contradicted-each-other` records it. The person chose that `case-guppi` itself lists each behaviour, field and term that a sub-case sets and reads every sentence of all its sub-cases on it side by side, whatever page each one changes, and that it searches the live pages and `.claude/` for the name of each field, term or command whose behaviour the Case changes. The person chose to replace the Criterion of `estimate-case-build-checks-the-finished-case`, which already promises the comparison on one page.
>
> In `rule-case-build`, which I read whole, the sentences that state how `case-guppi` checks its finished Case are: the sentence on the sub-cases that change one page, which this Case rewrites; the sentence on the search for the slug of each page made false and the sentence on the index lines, which stay true, since the new search adds to them; the sentence that defines a contradiction, which stays true; and the `Purpose`, which names no single step and stays true. In `estimate-case-build-checks-the-finished-case` the line on the sub-cases of one page is rewritten, not dropped, so the check notes it as not carried, and one line is added; the other lines are carried word for word. Its `purpose` and `method` name the sub-cases of one page, so the same `update` sets both anew. The `then` holds more than seven `＋` lines because it is that Criterion whole, which already held them; it stays one promise, the check of the finished Case. A Grep for `sub-cases that change one page` over `vault/wiki/` printed `vault/wiki/rules/rule-case-build.md` and `vault/wiki/estimates/estimate-case-build-checks-the-finished-case.md`, and over `.claude/` printed `.claude/agents/case-guppi.md`, the Render of `rule-case-build`; no other text states the step. The hook of `rule-case-check` notes a sentence that two Cases of the session change; it acts on the file at the stop, a moment this Case does not set, so it stands.
>
> Tests that read live files: a Grep for `(ROOT|REPO)\s*/\s*"(vault|\.claude)"` over `tests/` printed `tests/test_case_schema.py`, `tests/test_schemas.py`, `tests/test_generate.py` and `tests/test_orchestration.py`; they read `case-schema.md`, `case-example.md`, `orchestration.md` and the schema files, none of which this Case changes. A Grep for `case-guppi\.md|rule-case-build` over `tests/` printed nothing. The Case adds no code, so no judgment of `guppi/` is copied. No other Case of this session changes these pages. The lesson came from session 1604, so no decision line here carries an `addresses` mark.

> **problem:**
> `case-guppi` writes a Case whose sub-cases contradict each other on one behaviour when they change different pages, and it misses a glossary row or an Estimate that speaks of a changed field without naming a changed page; `/pre-spec` finds these late, and the Case is shown again.

> **recommend:**
> - **Where are the parts of a Case compared with each other?**
>   - Recommended: (a) the building agent compares the parts by meaning: in every Case with parts, before it writes the file, it lists each behaviour, field and term any part sets and reads every sentence of every part on it side by side, whatever page the part changes.
>   - Answer: agreed, (a).
> - **Which texts outside the Case does the agent search for a changed field?**
>   - Recommended: (a) search the live pages outside the Decision pages, and `.claude/`, for the name of each field, term or command whose behaviour the Case changes, glossary rows and the Criterion of each check page included.
>   - Answer: agreed, (a).
> - **Which check page proves the fix?**
>   - Recommended: (a) rewrite the promise of `estimate-case-build-checks-the-finished-case`: its line on parts of one page widened, one line for the field search, its purpose and method set anew, read at this session's Retro.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build`: the rule of `case-guppi`, whose step on its sub-cases changes.
> **＋** `.claude/agents/case-guppi.md`: the Render of `rule-case-build`.
> **＋** `estimate-case-build-checks-the-finished-case`: its Criterion, `purpose` and `method` are replaced.
> **＋** `.claude/agents/ask-guppi.md`: the recipe whose index lines `case-guppi` reads for a fact no slug marks.
> **＋** `rule-case-check`: the hook that checks the file of a Case and names other Cases in a finding or a note.
> **＋** `vault/wiki/glossary.md`: the terms, whose rows the new search reads.
> **＋** `vault/wiki/rules/`: the rules searched for the words that name a moment the change sets.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the case file of each Case of the session that `case-guppi` reads.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, has built a Case and is about to answer with it.

> **then:**
> It puts each option the person chose in its rounds, or the person's own words where they answered outside the options, beside the `then` and `recommend` of the Case, and the Case holds each one; where the frame shows after a round that a chosen option cannot hold as written, its answer is a round on that point, not a Case with another behaviour.
> **＋** For each page whose text the change makes false, it searches the live pages of the vault, leaving out the Decision pages, and the code, for the page's slug, and reads each hit that `given` does not name around the line of the hit; for a fact that no slug marks, it reads the index lines of the recipe of `.claude/agents/ask-guppi.md` and judges them by meaning.
> **＋** For each field, term or command whose behaviour the Case changes, it searches the live pages of the vault, leaving out the Decision pages, and `.claude/`, for its name, and reads each hit around its line, a row of `vault/wiki/glossary.md` and the Criterion of an Estimate included; each hit that the change makes false enters the Case, or its `context` says why it stands.
> **＋** In each page the Case changes, which it has read whole, it lists each sentence that states the behaviour the change touches, judged by what the sentence says and not found by a search for the words of the sentence it changes, so that a sentence that states the same rule in other words is on the list; each sentence on that list that the change makes false enters the Case, or its `context` says why it stands.
> **＋** When the change sets what happens at a moment — a reply, a hook event, a command — it searches `vault/wiki/rules/` and `.claude/` for the words that name that moment, reads each passage of each hit that sets a form or a behaviour at that moment, and the Case either does not cover that moment or names the other rule in `given`.
> **＋** It reads the case file `raw/<date>/<hi HHMM>/cases/case-<N>.md` of each Case of the session that the prompt of its call names, and of each Case of the session that the check of `rule-case-check` names in a finding or a note on its file, and no other Case of the session; where that Case changes a page the Case changes or sets what happens at the same moment, the Case does not cover that moment or names the case file in `given`, and its new text of that page does not contradict the text of that Case.
> **＋** When the Case replaces the Criterion of an Estimate, it reads the `purpose` and `method` of that Estimate, and the same `update` sets anew each one that states the old promise.
> **＋** Each hit that the change makes false enters the Case, or its `context` says why it stands.
> **＋** The `context` names a search only when the Case rests on it: a search with a hit that enters the Case, a search with a hit that stands and needs the reason why, or a search that a claim that no text says something rests on; a search that found nothing to change and that no claim rests on is left out.
> **＋** A claim of `context` about a text names the search it rests on: its pattern, the paths it ran over, and each file the search printed, a file it does not read included, or the count it printed; just before it answers, it runs each search that `context` names again, with the pattern and the paths that `context` writes, and the files and counts in `context` are the ones that run printed, not the files it read during the build; it claims nothing the search did not print.
> **＋** In a Case with sub-cases, it lists each behaviour, field and term that a sub-case sets, reads side by side every sentence of the new texts of all its sub-cases that speaks of it, whatever page each sub-case changes, and the Case holds no contradiction between them.
> **－** A hit in a History line, in `log.md` or in `brief.md` is not read.

```then
update:
- slug: rule-case-build
  replace:
  - old: Read side by side the finished new texts of all your sub-cases that change one page, and fix a contradiction between them (case 544.1).
    new: In a Case with sub-cases, list each behaviour, field and term that a sub-case sets, read side by side every sentence of the new texts of all your sub-cases that speaks of it, whatever page each sub-case changes, and fix a contradiction between them (cases 544.1, 784). For each field, term or command whose behaviour the Case changes, Grep the live pages of `vault/wiki/` outside `decisions/`, and `.claude/`, for its name, and read each hit around its line, a row of `glossary.md` and the `## Criterion` of an Estimate included; a hit in a History line, in `log.md` or in `brief.md` is not read; each hit the change makes false enters the Case, or `context` says why it stands (case 784).
  change: case-guppi reads side by side the sentences of all its sub-cases on one behaviour, field or term, whatever page each changes, and searches the live pages and .claude/ for the name of each field, term or command whose behaviour the Case changes (case 784)
- slug: estimate-case-build-checks-the-finished-case
  set:
    status: pending
    purpose: Whether case-guppi checks its finished Case before it answers — the chosen options, the pages that name a slug the change makes false, the live texts that name a field, term or command whose behaviour the change touches, glossary rows and Estimates included, the sentences of a page it changes that state the changed behaviour in other words, the rules that act at the moment the change sets, the Cases of the session its prompt names or the check of its file names in a finding or a note, the purpose and method of an Estimate whose Criterion it replaces, what each search printed and that the context keeps only the searches the Case rests on, the sentences of its sub-cases that speak of one behaviour, field or term whatever page each changes — counted by what ask-guppi still finds at pre-spec
    method: by hand, the text of .claude/agents/case-guppi.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec, read against the Criterion; the findings of ask-guppi at the /pre-spec of that session, when it ran, read for each Case case-guppi built — a Case that departs from a chosen option, a page naming a changed slug that the Case misses, a glossary row or an Estimate naming a changed field, term or command that the Case misses, a sentence of a page the Case changes that states the changed behaviour in other words and that the Case misses, a rule acting at the same moment that the Case misses, a Case of the session named in the prompt whose page or moment the Case clashes with, an Estimate whose purpose or method still states the promise its replaced Criterion dropped, a claim of context that its search did not print, a search in context that the Case does not rest on, two sub-cases whose texts on one behaviour, field or term contradict — the count of each in the estimate line
  change: the Criterion replaced whole — sub-cases read side by side by the behaviour, field or term they speak of, whatever page each changes, and a search for the name of each changed field, term or command (case 784)
```

```tasks
- [ ] update `rule-case-build`
- [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [ ] update `estimate-case-build-checks-the-finished-case`
- [ ] read `estimate-case-build-checks-the-finished-case`
```
