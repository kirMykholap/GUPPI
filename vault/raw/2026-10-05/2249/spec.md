<!-- approved 00:26:24 · session 26de285b -->

# Spec — session 2249, 2026-10-05

## Case 675 — The open question of the whole-Spec check leaves the backlog

> **context:**
> At its first run in a session, `/pre-spec` sends one `ask-guppi` run to read the ratified Cases against the vault and against each other. One run over a large Spec returns only part of the problems: `lesson-prespec-one-ask-guppi-run-samples-the-spec` records a run over a Spec of some twenty sub-cases that found 10 findings, and a later run over the same Spec that found 12: 8 of them stand on sub-cases that stood in the plan at the first run, which that run did not name; 2 stand on sub-cases written from the first run's findings after that run; and 1 is the fix of a finding of the first run. Case 674 went back to one run, for its cost, and kept the open question as the draft `rule-prespec-judges-the-spec-whole` in the backlog (case 674.3): whether the one run needs help on a large Spec, and whether it also asks what the Cases together leave unanswered. The person chose to remove the item: the one run stays as it is, the draft page is not needed even in the backlog, no question on what the Cases leave open together is added, and the person will look at the cost of a run alone. So this Case deletes the draft page and adds no measurement and no Estimate of the cost.
> The vault's answer: the Case creates no page, so no vault query on a `create` ran. The Frontier line has the source `backlog`, and the page carries `deferred_by` the Decision of case 674.3, so the delete line carries `{supersedes:case 674.3}`, as case 671.2 did for the draft it deleted. The skill of `rule-prespec` does not change: its report still lists what the run did not check and never says the whole Spec is checked, which stays true. The lesson stays as the record of the sample, under `insight-prespec-after-findings-loop-unruled`.
> The frame. A Grep `rule-prespec-judges-the-spec-whole` over `{vault/wiki/**,guppi/**,.claude/**,tests/**}` printed 3 files: `vault/wiki/brief.md`, `vault/wiki/backlog.md` and `vault/wiki/log.md`. The librarian writes `backlog.md` and `brief.md` from the pages, and `log.md` is history; they were not read, and they stand. The deleted page carries no promise. `estimate-backlog-renders` checks that `## Deferred` of `backlog.md` lists each live page with `deferred_by`; once the page is gone it is not listed, so its Criterion stays true and stands, and it checks this Case. The `make lint` of the librarian's run checks that no live page links to the deleted page.

> **problem:**
> A draft page holds open in the backlog a question the person no longer wants to keep: whether the one `ask-guppi` run of `/pre-spec` needs help on a large Spec, and whether it asks what the Cases together leave unanswered.

> **recommend:**
> - **What to do with the open question now**
>   - Recommended: (b) record the cost of the run at every pre-spec, and decide later; the draft page stays in the backlog.
>   - Answer: the person chose to remove the item: it is not needed even in the backlog, and the person will look at the measurement alone; (a), with the cost left to the person.
> - **Whether the one run asks what the Cases leave open together**
>   - Recommended: (b) do not add it, and drop it from the open question.
>   - Answer: the person removed the whole item, so no such question is added; (b).
> - **Change**
>   - Asked: at pre-spec the person agreed to the fix of a finding: the `context` gave the second run's 12 findings as if all stood in the Spec the first run read, while the lesson says some stood on sub-cases written after that run, so the lesson's own wording is carried into the `context`.
>   - Taken: the `context` gives the 12 findings as the lesson splits them: 8 on sub-cases the first run read, 2 on sub-cases written from its findings after it, 1 on the fix of one of its findings.

> **given:**
> `rule-prespec-judges-the-spec-whole`: the draft page of the backlog item, which this Case deletes.
> **＋** `rule-page-generation`: the rule of `guppi generate`, which deletes the page and retires its defer.
> **＋** `vault/wiki/backlog.md`: the backlog that lists a deferred page with its purpose.
> **＋** `rule-prespec`: the rule of the one `ask-guppi` run at pre-spec, which stays as it is.

> **when:**
> `guppi generate` of `rule-page-generation` applies the decisions of this Case, and `guppi backlog` writes `vault/wiki/backlog.md`.

> **then:**
> `rule-prespec-judges-the-spec-whole` no longer stands under `vault/wiki/`.
> **＋** `vault/wiki/backlog.md` no longer lists it under `## Deferred`.
> **－** `rule-prespec` does not change: its one `ask-guppi` run gets no help on a large Spec and no question on what the Cases leave open together.

```then
delete:
- slug: rule-prespec-judges-the-spec-whole
  impact: the draft of the backlog leaves; the one ask-guppi run of /pre-spec stays as rule-prespec sets it, with no help on a large Spec and no question on what the Cases leave open together; the person looks at the cost of a run alone; the defer of case 674.3 is retired by the supersedes mark of this line
```

```tasks
- [x] delete `rule-prespec-judges-the-spec-whole`
```

## Case 676 — The draft of the subagent rule leaves the backlog

> **context:**
> The draft `rule-subagent-guppi` was to say what a subagent may do in Work Mode, and how a fork that a subagent meets comes back to the main agent as a Case. It holds only its Purpose, and it waits in the backlog in two places: as a page with `deferred_by`, and as a line of `## Backlog` in `entity-sprint-migration`. The backlog counts 29 sessions that put it off, and no Case took it up since case 183. While the backlog was reviewed, the main agent proposed to delete it: what still matters of it is closer to `rule-work-mode`, which stays in the backlog. The person agreed. So this Case deletes the page, and `rule-work-mode` does not change.
> The vault's answer: the Case creates no page, so no vault query on a `create` ran. The Frontier line has the source `backlog`, and the page carries `deferred_by` the Decisions of cases 183, 206, 218, 231, 242, 248, 252, 254, 260, 263, 269, 276, 281, 285, 289, 293, 303, 307 and 322, so the delete line carries one `{supersedes:case N}` for each of them, as case 675 did for the one defer of the draft it deleted. All nineteen Decision pages stand archived: a Glob of their paths under `vault/archive/migration/2026-09-28/1318/decisions/` printed all nineteen, and the same Glob under `vault/wiki/decisions/` printed none. Today `generate.decision` sets such a page `superseded` again, and `guppi cleanup` would then bring it back to the live vault. Case 683 of this session fixes that: an archived Decision that a later Case supersedes stays `archived` where it lies and only takes the later Decision into `superseded_by`, with one History line, while the defers it names are cleared as for any supersede. The nineteen marks of this Case rely on the code of Case 683 standing in the working tree before the librarian's run of this session. Case 683 replaces the Criterion of `estimate-generate-writes-the-decision-page`, whose line on a `supersedes` describes what the nineteen marks do; that Estimate, read in the Retro of this session, checks this part of this Case, and this Case does not change its Criterion again. The one sentence on a subagent's fork that stays in force is in `ratification.md`, the Render of `rule-ratification`: a subagent that hits a fork stops and returns, and never decides; it does not depend on the draft, and it stands.
> The frame. A Grep `rule-subagent-guppi` over `{vault/wiki/**,guppi/**,.claude/**,tests/**}` printed 5 files: `vault/wiki/brief.md`, `vault/wiki/backlog.md`, `vault/wiki/log.md`, `vault/wiki/entities/entity-sprint-migration.md` and `tests/test_sprint.py`. The librarian writes `backlog.md` and `brief.md` from the pages, and `log.md` is history; they were not read, and they stand. In `entity-sprint-migration` the hit is the line of `## Backlog` that links the page. This Case does not change that page: the page carries `deferred_by` the Decision of case 642, and its open Frontier line C9 is Case 680 of this session, which removes the plain lines of the same section and retires that defer. The check of this file sends back a Case that names the page without `{supersedes:case 642}`, and that mark belongs to Case 680, not to this Case. So Case 680 needs one more `replace` pair that removes the line of `[[rule-subagent-guppi]]` from `## Backlog`, so that no live page links to the deleted page; until it does, the `make lint` of the librarian's run reports that link. In `tests/test_sprint.py` the slug names a page of a fixture vault that the test writes itself, so the test does not read the live page and it stands. The deleted page carries no promise. `estimate-backlog-renders` checks that `## Deferred` of `backlog.md` lists each live page with `deferred_by` and each line of the `## Backlog` of the sprint page; once the page and its line are gone, through this Case and Case 680, neither is listed, so its Criterion stays true and stands, and it checks this Case. `estimate-prespec-requires-a-backlog-item-decided-on-its-page` checks that the Case names the page and carries each mark, which the delete line does. The `make lint` of the librarian's run checks that no live page links to the deleted page.

> **problem:**
> A draft page that no Case took up in 29 sessions holds a place in the backlog twice, as a page and as a line of the sprint page, while what still matters of it belongs with `rule-work-mode`.

> **recommend:**
> - Recommended: delete `rule-subagent-guppi`, and retire each of its defers; Case 680 removes its line from the `## Backlog` of `entity-sprint-migration`; `rule-work-mode` stays in the backlog as it is.
>   Answer: ratified as built
> - **Change**
>   - Asked: the person agreed to the fixes of the pre-spec report: say that the nineteen Decisions the delete line supersedes stand archived, that the marks rely on the code of Case 683 in the working tree before the librarian's run, and name `estimate-generate-writes-the-decision-page` as Case 683 replaces it.
>   - Taken: `context` and the `impact` of the delete say so, and `given` names the case file of Case 683.

> **given:**
> `rule-subagent-guppi`: the draft page of the backlog item, which this Case deletes.
> **＋** `rule-page-generation`: the rule of `guppi generate`, which deletes the page and retires the defers.
> **＋** `vault/raw/2026-10-05/2249/cases/case-683.md`: Case 683, which keeps an archived Decision archived when a later Case supersedes it.
> **＋** `vault/wiki/backlog.md`: the backlog that lists a deferred page and each line of the sprint page's `## Backlog`.
> **＋** `rule-work-mode`: the draft of the rest of Work Mode, which stays in the backlog as it is.

> **when:**
> `guppi generate` of `rule-page-generation` applies the decisions of this Case, and `guppi backlog` writes `vault/wiki/backlog.md`.

> **then:**
> `rule-subagent-guppi` no longer stands under `vault/wiki/`.
> **＋** `vault/wiki/backlog.md` no longer lists `rule-subagent-guppi` under `## Deferred`.
> **－** `rule-work-mode` does not change, and it stays in the backlog.

```then
delete:
- slug: rule-subagent-guppi
  impact: the draft of the backlog leaves; what still matters of it is closer to rule-work-mode, which stays in the backlog; a subagent that hits a fork still stops and returns, as ratification.md sets; each defer of its deferred_by is retired by the supersedes marks of this line; the nineteen Decision pages they name stand archived and stay archived by the code of case 683, which stands in the working tree before the librarian's run
```

```tasks
- [x] delete `rule-subagent-guppi`
```

## Case 677 — The idea that a complaint becomes a lesson leaves the backlog

> **context:**
> The draft `rule-complaint-becomes-a-lesson` keeps an idea of session 0137 in the backlog: after each reply of the person a hook asks whether the reply holds a complaint about the agent's text or work, and a complaint becomes a lesson line. Case 504 put it off as a placeholder, and nobody ever decided it; the page holds only its Purpose. The main agent proposed to delete it while the backlog was reviewed, since Retro already writes a lesson line for a finding by its own judgment (`rule-retro`), and `estimate-agent-writing-followed` already takes the person's complaint as the test of the agent's text. The person agreed to close it as proposed. So this Case deletes the draft page and adds no hook, no rule and no Estimate.
> The vault's answer: the Case creates no page, so no vault query on a `create` ran. The Frontier line has the source `backlog`, and the page carries `deferred_by` the Decision of case 504, so the delete line carries `{supersedes:case 504}`, as case 675 did for the draft it deleted. The page has no `estimates` and is governed by no code.
> The frame. A Grep `rule-complaint-becomes-a-lesson` over `{vault/wiki/**,guppi/**,.claude/**,tests/**}` printed 3 files: `vault/wiki/brief.md`, `vault/wiki/backlog.md` and `vault/wiki/log.md`. The librarian writes `backlog.md` and `brief.md` from the pages, and `log.md` is history; they were not read, and they stand. The deleted page carries no promise. `estimate-backlog-renders` checks that `## Deferred` of `backlog.md` lists each live page with `deferred_by`; once the page is gone it is not listed, so its Criterion stays true and stands, and it checks this Case. The `make lint` of the librarian's run checks that no live page links to the deleted page.

> **problem:**
> A draft page holds in the backlog an idea that was never decided and that the person no longer wants to keep: a hook that turns each complaint of the person into a lesson line.

> **recommend:**
> - Recommended: delete the draft page; Retro already writes lessons and the person's complaint already tests the agent's text.
>   Answer: ratified as built

> **given:**
> `rule-complaint-becomes-a-lesson`: the draft page of the backlog item, which this Case deletes.
> **＋** `rule-page-generation`: the rule of `guppi generate`, which deletes the page and retires its defer.
> **＋** `vault/wiki/backlog.md`: the backlog that lists a deferred page with its purpose.

> **when:**
> `guppi generate` of `rule-page-generation` applies the decisions of this Case, and `guppi backlog` writes `vault/wiki/backlog.md`.

> **then:**
> `rule-complaint-becomes-a-lesson` no longer stands under `vault/wiki/`.
> **＋** `vault/wiki/backlog.md` no longer lists it under `## Deferred`.
> **－** No hook asks after a reply of the person whether it holds a complaint.

```then
delete:
- slug: rule-complaint-becomes-a-lesson
  impact: the draft of the backlog leaves; no hook turns a complaint of the person into a lesson line; Retro writes lessons by its own judgment as rule-retro sets it; the defer of case 504 is retired by the supersedes mark of this line
```

```tasks
- [x] delete `rule-complaint-becomes-a-lesson`
```

## Case 678 — The Insight on one judgment in two copies is answered again

> **context:**
> `insight-harness-one-rule-implemented-twice-drifts` says that one judgment of the pipeline lives in two copies of code, which drift apart under a green suite. Case 360 answered it with `rule-one-judgment-one-implementation`, whose text stands in `CLAUDE.md`, and set it `actioned`. The synthesis of session 1343 reopened it: it added the lesson `lesson-orchestration-defer-supersedes-a-parent-without-its-sub-cases`, where the Spec hook read a `{supersedes:case N}` mark as N with its sub-cases, and `prespec` and `materialize` read it as N alone. Case 660 closed that drift as the rule asks: `materialize.in_family` is now the one reading, and `prespec.retired_by` imports it. So the page is open, with severity 1, only for a cause that is already fixed, and it stands in the backlog. The person agreed to set it `actioned` again, and chose that `addressed_by` names the Decision of this Case, the latest, as `rule-insights-schema` asks and as case 611 did for `insight-case-form-chat-form-read-by-no-script`. The History line names case 360 and case 660.
> The frame. `rule-one-judgment-one-implementation` does not change: its Purpose says that it actions this Insight (case 360), and that stays true. Its one Estimate, `estimate-one-judgment-one-implementation-followed`, stands `passed` from its reading of 2026-09-29. The reopening lesson, of 2026-10-05, records a later breach of its Criterion: two readings of one mark, where the Criterion asks that the predicate live in one module and both sides import it. Case 660 closed that breach by `materialize.in_family`, which `prespec.retired_by` imports, so the Criterion holds again of the code. This Case changes no code and no promise, so it does not take that reading again, and the Estimate stands. The cascade of `generate` archives the `clustered` child of an `actioned` Insight, which `estimate-generate-cascades` checks; `guppi backlog` lists only an `open` Insight, which `estimate-backlog-renders` checks. Their Criteria speak of this change and stay true, so they stand and check this Case; the Case creates no Estimate. A Grep `insight-harness-one-rule-implemented-twice-drifts` over `vault/wiki/` printed 5 files: `vault/wiki/backlog.md`, `vault/wiki/log.md`, `vault/wiki/estimates/estimate-synthesis-clusters.md`, `vault/wiki/lessons/lesson-orchestration-defer-supersedes-a-parent-without-its-sub-cases.md` and `vault/wiki/rules/rule-one-judgment-one-implementation.md`. `guppi backlog` writes `backlog.md` again, and `log.md` is history, so these two were not read. The hit in `estimate-synthesis-clusters` is in its Result, a past reading, and it stays true. The lesson keeps its `insight` field, and the cascade archives it. The rule's Purpose stays true, as said above.

> **problem:**
> The Insight stays open in the backlog, but the rule in `CLAUDE.md` answers its pattern, and a fix that followed the rule has already closed the drift of its new lesson.

> **recommend:**
> - **Which decision should the Insight name as its answer?**
>   - Recommended: (a) this Case, the latest decision, with its History line naming the rule and the fix.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the pre-spec report found that the Case did not name `estimate-one-judgment-one-implementation-followed`, the Estimate of the rule that answers the Insight; the person agreed to its fix.
>   - Taken: `context` names that Estimate and says why it stands: case 660 fixed the later breach, and this Case does not take its reading again.

> **given:**
> `insight-harness-one-rule-implemented-twice-drifts`: the Insight that this Case sets `actioned`.
> **＋** `rule-insights-schema`: the shape of an Insight, which asks for one `addressed_by`, the latest.
> **＋** `rule-one-judgment-one-implementation`: the rule in `CLAUDE.md` that answers the pattern.
> **＋** `lesson-orchestration-defer-supersedes-a-parent-without-its-sub-cases`: the `clustered` child that reopened the Insight.
> **＋** `rule-page-generation`: the rule of `guppi generate` and its cascade.
> **＋** `vault/wiki/backlog.md`: the backlog, which lists each `open` Insight.

> **when:**
> `guppi generate` of `rule-page-generation` applies the decision of this Case and runs its cascade, and `guppi backlog` writes `vault/wiki/backlog.md`.

> **then:**
> `insight-harness-one-rule-implemented-twice-drifts` stands `actioned`, and its `addressed_by` names the Decision of this Case.
> **＋** `lesson-orchestration-defer-supersedes-a-parent-without-its-sub-cases` becomes `archived` by the cascade.
> **＋** `vault/wiki/backlog.md` no longer lists the Insight under `## Deferred`.
> **－** `rule-one-judgment-one-implementation` does not change.

```then
update:
- slug: insight-harness-one-rule-implemented-twice-drifts
  set:
    status: actioned
    addressed_by: decision-case-678
  change: 'actioned: rule-one-judgment-one-implementation in CLAUDE.md answers the pattern (case 360), and materialize.in_family, the one reading of a supersedes mark that prespec imports, closed the drift of the reopening lesson (case 660) (case 678)'
```

```tasks
- [x] update `insight-harness-one-rule-implemented-twice-drifts`
```

## Case 679 — The Insight on the refused `!` commands names its real cause and closes

> **context:**
> Before a call that is not read-only runs, Claude Code checks it with a model call. That covers a `!` command of a skill, and an Agent or SendMessage call in plan mode. When the check gives no verdict, the call is refused. `insight-hi-skill-substitution-checked-by-a-model-call` groups the lessons of this failure. Its `pattern`, `## Pattern` and `## Proposal` name a lapsed login as the cause and `/login` as the cure. Case 246 rejected that Proposal and set the Insight `actioned`. Then `lesson-hi-substitution-gets-no-verdict-from-the-server-side-classifier` found the real cause, and `/login` did not help. The real cause: since client 2.1.282 the check is made by a server-side classifier, and for a `!` substitution that the person types, it gives no verdict. Case 439 listed the `!` commands of `/hi` under `allowed-tools`, so they need no verdict. Case 448 put off the rewrite of the Pattern and Proposal. `lesson-plan-mode-agent-and-sendmessage-pass-the-auto-mode-classifier` then reopened the Insight: in plan mode, Agent and SendMessage calls were refused the same way, and the same calls went through once the server answered again. In the backlog review the person chose to close the Insight as a fault of Claude Code's environment, not of the harness. In the round the person also chose to rewrite the cause first (Q1) and to replace the text of `## Proposal` with the outcome (Q2), since `guppi generate` replaces the text of a section and cannot remove its heading.
> The vault's answer: this Case creates no page, so no vault query on a `create` ran. Per `rule-insights-schema`, an `update` that sets `status: actioned` and `addressed_by` rejects an Insight. Case 246 did the same. The page carries `deferred_by` the Decision of case 448, so the decision line carries `{supersedes:case 448}`. Once the Insight is `actioned`, the cascade of `generate` archives its one live `clustered` lesson. `rule-skill-hi` already states the server-side cause and the `allowed-tools` cure, and it stays as it is.
> The frame. A Grep `insight-hi-skill-substitution-checked-by-a-model-call` over `{vault/wiki/**,guppi/**,.claude/**,tests/**}` printed 4 files: `vault/wiki/backlog.md`, `vault/wiki/log.md`, `vault/wiki/estimates/estimate-backlog-renders.md` and `vault/wiki/lessons/lesson-plan-mode-agent-and-sendmessage-pass-the-auto-mode-classifier.md`. The librarian writes `backlog.md` from the pages, and `log.md` is history, so they stand. The hit in `estimate-backlog-renders` is in its `## Result`, a past reading, so it stands. The lesson names the Insight in its `insight` field, which stays true. A Grep `lapsed login` over `{vault/wiki/**,.claude/**}` printed 3 files: `vault/wiki/backlog.md`, `vault/wiki/log.md` and the Insight page itself. So no rule and no harness file states the old cause. The Insight page carries no Estimate. `estimate-backlog-renders` checks this Case: its Criterion lists an Insight under `## Deferred` only while its `status` is `open`, so once the page is `actioned` it leaves `backlog.md`. That Criterion stays true and stands. `estimate-insights-schema-checked` checks that an `actioned` Insight carries `addressed_by`, and this Case writes it, so that Criterion stands too.

> **problem:**
> An open Insight names a lapsed login as the cause and `/login` as the cure. Later lessons refuted both. The failure comes from Claude Code's server, and the harness has nothing to fix.

> **recommend:**
> - **What the closed Insight says is the cause**
>   - Recommended: (a) rewrite the cause, then close: the `pattern` and `## Pattern` name the server-side check that gives no verdict, the `/login` cure goes, and the Insight is set `actioned` as rejected.
>   - Answer: agreed, (a).
> - **What happens to the Proposal section**
>   - Recommended: (a) replace its text with the outcome: the harness has nothing to fix, and `/hi` gets past the check because its `!` commands are allowed in `rule-skill-hi`.
>   - Answer: agreed, (a).

> **given:**
> `insight-hi-skill-substitution-checked-by-a-model-call`: the Insight that this Case rewrites and closes.
> **＋** `rule-insights-schema`: the form of an Insight and of the `update` that rejects it.
> **＋** `rule-page-generation`: the rule of `guppi generate`, which applies the update, retires the defer and archives the lessons of an `actioned` Insight.
> **＋** `vault/wiki/backlog.md`: the backlog, which lists each `open` Insight.
> **＋** `rule-skill-hi`: the rule that names the `!` commands of `/hi` in `allowed-tools`.

> **when:**
> `guppi generate` of `rule-page-generation` applies the decision of this Case, and `guppi backlog` writes `vault/wiki/backlog.md`.

> **then:**
> `insight-hi-skill-substitution-checked-by-a-model-call` is `actioned`, and its `addressed_by` names the Decision of this Case.
> **＋** Its `pattern` and `## Pattern` name as the cause the server-side check of Claude Code, which gives no verdict on a call that is not read-only.
> **＋** Its `## Proposal` says that the harness has nothing to fix, and that `/hi` gets past the check through the `allowed-tools` of `rule-skill-hi`.
> **＋** No text of the page gives a fresh login as the cure.
> **＋** Its `clustered` lessons are `archived`.
> **＋** `vault/wiki/backlog.md` no longer lists it.
> **－** `rule-skill-hi` does not change.

```then
update:
- slug: insight-hi-skill-substitution-checked-by-a-model-call
  set:
    status: actioned
    addressed_by: decision-case-679
    pattern: A call that is not read-only — a ! command of a skill, an Agent or SendMessage call in plan mode — is checked by Claude Code's server-side classifier before it runs; when that server gives no verdict the call is refused, and the same call passes once the server answers again; a call that a permission rule allows needs no verdict.
  sections:
    Pattern: 'Four lessons, one cause. At /hi of sessions 1119 and 1252 the `!` substitution of `uv run guppi render --sync` was refused with the model reported unavailable; the second lesson took a lapsed login for the cause, since a /hi after /login ran whole. On 2026-09-26, in session 1b191eaf, /hi failed at every run: since client 2.1.282 the server-side classifier gives no verdict for a `!` substitution the person types, and a fresh /login did not help. On 2026-09-28, in session 1318, Agent and SendMessage calls in plan mode were refused the same way, and the same calls passed unchanged once the server answered again. The check is Claude Code''s, made on its server before the call runs; the harness neither makes it nor sees why it fails. A call that a permission rule allows needs no verdict.'
    Proposal: 'Rejected (case 679): the refusal comes from Claude Code''s server, and the harness has nothing to fix. /hi gets past the check, since the `allowed-tools` of `rule-skill-hi` names its `!` commands and an allowed command needs no verdict.'
  change: 'rejected — the cause rewritten: the server-side classifier of Claude Code gives no verdict, not a lapsed login; the /login cure removed; the harness has nothing to fix (case 679)'
```

```tasks
- [x] update `insight-hi-skill-substitution-checked-by-a-model-call`
```

## Case 680 — Old notes leave the Backlog of the migration sprint

> **context:**
> The `## Backlog` of `entity-sprint-migration` holds five plain notes from September that no Case took up: the product model (session 1119), the three notes on reuse — the edge, the question and the hook (cases 305, 319) — and a template engine for the rendered files (case 301). `guppi backlog` copies each line of that section into `## Deferred` of `vault/wiki/backlog.md`, which every session loads, and it keeps the Backlog of a closed sprint there too (case 628.12), so the notes would stay on that list after the sprint closes. While the backlog was reviewed, the main agent proposed to remove them, and the person agreed. If the product direction is ever taken up, it starts again from `entity-guppi`, which case 616 deferred. The line of `[[rule-subagent-guppi]]` in the same section also leaves. Case 676 of this session deletes that page and does not change this page. The person agreed that this Case removes the line, so that no live page links to the deleted page. The other lines of the section stay: `rule-work-mode`, `rule-spec-box`, `rule-morph` and the merge of `migration` into `main`.
> The vault's answer: the Case creates no page, so no vault query on a `create` ran. The Frontier line C9 has the source `backlog` and names the page, and the page carries `deferred_by` the Decision of case 642, which deferred the close of migration as a session of its own. The check of this file sends back a Case that changes such a page without `{supersedes:case 642}`. The person chose to retire that defer in this Case. The close does not drop out of sight: it stays the milestone line under Slice 5 of the page, which `sprint.md` shows.
> The frame. A Grep `template engine|reuse, the|product model` over `vault/wiki/` printed 3 files: `vault/wiki/backlog.md`, `vault/wiki/log.md` and `vault/wiki/entities/entity-sprint-migration.md`. The librarian writes `backlog.md` from the pages, and `log.md` is history; they stand. The same Grep over `{guppi/**,tests/**,.claude/**}` printed nothing. The Result of `estimate-backlog-renders` counts the five plain lines as of its reading of 2026-09-30. It records a past reading, and it stands. `estimate-backlog-renders` checks this Case: its Criterion says `## Deferred` lists each line of the `## Backlog` of each sprint page and each live page with `deferred_by`. Once the lines and the defer are gone, neither is listed, so the Criterion stays true and stands. `guppi backlog --check` in `make lint` reports a `backlog.md` that differs from its sources. A Grep `Backlog` over `vault/wiki/estimates/estimate-sprint-migration-*.md` printed 2 files: `estimate-sprint-migration-merges.md` and `estimate-sprint-migration-lint-clean.md`. The hits in `estimate-sprint-migration-lint-clean` are History lines, so they stand. The Criterion of `estimate-sprint-migration-merges` says that the merge of `migration` into `main` is a line of the `## Backlog` of `entity-sprint-migration`. This Case keeps that line, so the Criterion stays true and stands.

> **problem:**
> Notes that no Case took up hold places in the backlog that every session loads, and they would stay there after the sprint closes. The line of a page that Case 676 deletes would leave a link to a deleted page.

> **recommend:**
> - **What happens to the postponed close of the sprint**
>   - Recommended: (a) retire the postponement in this Case; the close stays in view as the Slice 5 milestone in `sprint.md`.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the person agreed with the main agent's recommendation on Case 676 that this Case also removes the line of `[[rule-subagent-guppi]]` from `## Backlog`.
>   - Taken: a second `replace` pair removes that line.
> - **Change**
>   - Asked: the person agreed to the fix of a pre-spec finding: `context` must name `estimate-sprint-migration-merges`, whose Criterion speaks of a line of the `## Backlog`, and say why it stands.
>   - Taken: `context` names that Estimate and the search behind it; the Criterion stands because the merge line stays.

> **given:**
> `entity-sprint-migration`: the sprint page whose `## Backlog` loses the lines and whose defer is retired.
> **＋** `rule-page-generation`: the rule of `guppi generate`, which applies the update and retires the defer.
> **＋** `vault/wiki/backlog.md`: the backlog that lists each line of the sprint page's `## Backlog` and each page with `deferred_by`.
> **＋** `vault/raw/2026-10-05/2249/cases/case-676.md`: the Case that deletes `rule-subagent-guppi` and leaves its line to this Case.

> **when:**
> `guppi generate` of `rule-page-generation` applies the decisions of this Case, and `guppi backlog` writes `vault/wiki/backlog.md`.

> **then:**
> The `## Backlog` of `entity-sprint-migration` no longer holds the product model, the three notes on reuse, the template engine or the line of `rule-subagent-guppi`.
> **＋** `vault/wiki/backlog.md` no longer lists those notes under `## Deferred`.
> **＋** `entity-sprint-migration` no longer carries the defer of the close of migration, and `vault/wiki/backlog.md` no longer lists the page under `## Deferred`.
> **－** The other lines of the `## Backlog` of `entity-sprint-migration` stay, and its milestone of the close of migration does not change.

```then
update:
- slug: entity-sprint-migration
  replace:
  - old: |-
      - the product model: `kind: test | measurement | reading`, `ask-guppi` through Entities, the vault-query questions before a product's records (session 1119); `applies_to` and `rules` taken into Slice 3f (case 301)
      - reuse, the edge: `uses` / `used_by` between Entities — `uses` written in the Case on the side that uses, `used_by` computed by the cascade of `generate`, the pair checked by lint, the pattern of `applies_to` / `rules`; no edge Rule → Rule (cases 305, 319)
      - reuse, the question: the vault query before a `create` asks a second question — what of the existing this thing could use, by the index lines of the Entities — and the answer stands in `context`; the Case names what it found in `uses` or says why it is not used (case 319)
      - reuse, the hook: a lint finding on two live Entities naming one path in `code_ref` with no edge between them; a new module written beside an existing one in another file is caught by the question alone, not by a script (case 319)
      - a template engine for the rendered files — one script with the shape of each file declared, once a third render beside `sprint.md` and `glossary.md` appears (case 301)
      - [[rule-work-mode]]
    new: '- [[rule-work-mode]]'
  - old: |-
      - [[rule-subagent-guppi]] — what a subagent may do in Work Mode, and the fork that comes back to the main agent as a Case; cases 183, 206
      - [[rule-spec-box]]
    new: '- [[rule-spec-box]]'
  change: the five plain notes of the Backlog — the product model, reuse three times, the template engine — and the line of rule-subagent-guppi leave; the defer of the close of migration is retired, and the close stays the milestone of Slice 5
```

```tasks
- [x] update `entity-sprint-migration`
```

## Case 682 — The ledger hook asks for the mark of a lesson written after a Case

> **context:**
> When a Case of a session closes the cause of a lesson of the same session, one of two marks links them: a lesson line written after the Case carries `{addressed_by:case N}`, and a decision line written after the lesson carries `{addresses:<lesson slug>}` (case 379). The ledger hook writes the record lines of each reply into the session's ledger. It refuses a lesson line whose `{addressed_by:case N}` has no decision line of Case N before it (case 497.1), but it writes a lesson line with no mark at all without a word. In session 1337 the line `lesson-hooks-subagentstop-fires-before-and-after-the-handback` stayed with no mark, although Case 434 had closed its cause, so the librarian did not link it and the lesson stayed `new`. Case 442 deferred the question onto `rule-ledger-write`. No code can judge whether a Case closed a cause, so the hook can only stop a likely miss and ask the agent.
> The person chose three things. The ledger hook holds a fresh lesson line with no `{addressed_by:...}` once, when a decision line of the session stands before it, and asks the agent: a Case that closed the cause gets the mark on the line written again, and no Case gets the line written again unchanged, which the hook then writes. Every such lesson line is held, not only one that names a page a Case changed. The `{addresses:...}` side is not covered: a decision line with no `{addresses:...}` after an unmarked lesson is not judged, and that stays not done.
> The hold uses the told-once rule of the hook: a stderr line already in a refusal of the hook since the person's last message is not printed again, so the line written again unchanged is written at its `Stop`, and a line from an earlier text is written without a word. An unmarked line is never written beside a marked line of the same slug, so the ledger never holds the lesson twice. Case 682.1 updates `rule-ledger-write`, carries `{supersedes:case 442}` and creates `estimate-ledger-write-asks-for-the-mark-of-a-lesson`, checked by pytest. The form of a ledger line does not change, so no old form is kept; during Work Mode the hook runs from the working tree, and a held line is written again, not lost.
> The frame. `estimate-ledger-write-refuses-a-mark-with-no-decision-line` says that a lesson line with no mark is written as before, which the hold makes false, so Case 682.2 replaces its Criterion whole with that sentence changed; its `purpose` and `method` speak only of a marked line and stand. `estimate-ledger-write-lifts` says that a line a refusal of `rule-ledger-write` refuses does not land while that refusal holds, and that each refused line is told once a stretch; the hold is such a refusal, so its Criterion stands. `estimate-ledger-write-refuses-a-lesson-without-its-prefix` says that a lesson line with the prefix has its mark judged by the check of the mark; that stays true, and a line refused for its prefix is not judged for a missing mark, so it stands. The other Estimates of the page speak of readings, unreadable lines, errors and the kind of a user record, and stand. The other `Stop` hooks of `.claude/settings.json` stand: `guppi onward` already sends the agent on only after the reply that writes the refused lines again (case 596.1), and the Render of `rule-retro` lets the reply that ends Retro be followed by a `LEDGER` block that answers a refusal of the ledger hook, which a lesson line written again with its mark or unchanged is.
> The searches. A Grep of `with no mark|nothing catches|missing mark` over `vault/wiki/` printed `estimate-ledger-write-refuses-a-mark-with-no-decision-line.md`, which enters Case 682.2, `estimate-case-check-requires-a-backlog-item-decided-on-its-page.md`, whose missing mark is a `{supersedes:...}` mark and stands, and `lesson-hooks-a-stop-system-message-shows-no-markdown-in-vs-code.md`, which speaks of a hook's message and stands. A Grep of `refusal of the ledger hook|ledger hook refuses` over `vault/wiki/rules/` and `.claude/` printed `.claude/skills/retro/SKILL.md`, `rule-retro.md`, `rule-ledger-write.md`, `rule-orchestration.md`, `rule-ratification.md` and `rule-session.md`: the first two let a reply answer a refusal of the ledger hook, the hits in `rule-ratification` and `rule-orchestration` name other refusals of the hook and a History line, the hits in `rule-ledger-write` are History lines, and the hit in `rule-session` names the refusal without `/hi`; each stays true and stands. A Glob of `vault/**/*mark-of-a-lesson*` printed nothing, so the new slug is free. Case 681 of this session changes `rule-orchestration` and Case 683 changes `rule-page-generation`; neither changes a page this Case changes.

> **problem:**
> A lesson line whose cause a Case of the same session closed can be written with no mark, and nothing catches it, so the librarian never links the lesson to its Case.

> **recommend:**
> - **Where the missing mark is caught**
>   - Recommended: (a) the ledger hook holds the line once and asks; a line written again with the mark, or unchanged, is then written.
>   - Answer: agreed, (a).
> - **Which lesson lines the check stops**
>   - Recommended: (a) every unmarked lesson line written after a decision line of the session.
>   - Answer: agreed, (a).
> - **Whether the `{addresses:...}` side is covered too**
>   - Recommended: (a) leave it out, and name it as not done.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec` the person agreed to the fix of a finding: the Criterion of Case 682.2 said a lesson line with no mark that the new check does not hold is written, while Case 682.1 drops an unmarked line beside a marked line of the same slug.
>   - Taken: the Criterion of Case 682.2 now says a lesson line with no mark is written when the new check neither holds nor drops it.

### Case 682.1 — The ledger hook holds an unmarked lesson once and asks

> **given:**
> `rule-ledger-write`: the rule of the ledger hook, whose deferred item this Case takes up.
> **＋** `guppi/ledger.py`: the `Stop` hook `uv run guppi ledger` that judges the fresh lines.
> **＋** `tests/test_ledger.py`: the tests of the hook.
> **＋** `estimate-ledger-write-asks-for-the-mark-of-a-lesson`: the new check of the hold.
> **＋** `estimate-ledger-write-lifts`: the told-once rule the hold uses, which stands.
> **＋** `rule-retro`: the reply that answers a refusal of the ledger hook at the end of Retro, unchanged.
> **＋** `rule-retro-onward`: the hook that sends the agent on after the reply that writes refused lines again, unchanged.

> **when:**
> The `Stop` hook `uv run guppi ledger` of `guppi/ledger.py` finds a fresh `lesson[<slug>]` line in a `LEDGER` block of the session that carries no `{addressed_by:...}`, and a decision line of the session stands before it, in the session's ledger or earlier among the lines of the same `Stop`.

> **then:**
> At the `Stop` of the reply that carries it, the hook holds the line back once, unless it already asked about it since the person's last message.
> **＋** For each held line the hook exits 2 and prints: "ledger: lesson[<slug>] held — did case <N> or case <M> fix its cause? Then add {addressed_by:case <N>}, the Case or sub-case that fixed it, and repeat the line; otherwise repeat it unchanged."
> **＋** The Cases the stderr line names are those whose decision lines stand before the lesson line, in the order first seen.
> **＋** The line lands as it stands once the hook's question about it stands in a refusal since the person's last message, or when it stands only in an earlier text of the transcript.
> **＋** A held line keeps back no other line: the rest of that `Stop` lands in the ledger.
> **－** An unmarked line never lands beside a marked one: `{addressed_by:...}` on a `lesson[<slug>]` line in the session's ledger, or in that `Stop`, drops the unmarked line of the slug.
> **－** The hook asks nothing about a lesson that precedes every decision line of the session, about a line it refuses for its prefix or cannot parse, or about a line that the ledger of some session already holds.
> **－** The hook never asks for `{addresses:...}` on a decision line.
> **－** A session with no `hi` gets no question. The flag `stop_hook_active` changes nothing here, but when it is set and the transcript is unreadable, the hook lets the line land as it stands.

```then
create:
- slug: estimate-ledger-write-asks-for-the-mark-of-a-lesson
  ref: rule-ledger-write
  kind: QA
  purpose: Whether the ledger hook holds once a lesson line with no addressed_by mark written after a decision line of the session, asks for the mark, and then writes the line written again
  method: uv run pytest tests/test_ledger.py — piped payloads and a session ledger in a temp vault
  tags:
  - session
  - hooks
  - harness
  - ledger
update:
- slug: rule-ledger-write
  replace:
  - old: so that the session after the close of a sprint opens the next sprint first (`rule-sprint-close`, case 628.3).
    new: 'so that the session after the close of a sprint opens the next sprint first (`rule-sprint-close`, case 628.3). It holds once a lesson line with no `{addressed_by:case N}` written after a decision line of the session, and asks the agent whether a Case of the session closed its cause: the line written again with the mark, or unchanged, is written (case 682.1).'
  change: the hook holds once a lesson line with no addressed_by mark written after a decision line of the session, and asks for the mark (case 682.1)
```

```tasks
- [x] update `rule-ledger-write`
- [x] create `estimate-ledger-write-asks-for-the-mark-of-a-lesson`
- [x] `guppi/ledger.py`: a function judges each fresh unmarked lesson line after a decision line of the session over the session's ledger followed by the fresh lines; `run` holds it once by the told-once rule, skips it beside a marked line of the same slug, and the docstring says so.
- [x] `tests/test_ledger.py`: tests of the hold, of the line written again unchanged, of the line written again with its mark, of a line from an earlier text, of a lesson with no decision line before it and of the flag with an unreadable transcript; the existing tests whose unmarked lesson follows a decision line answer the hold.
- [x] read `estimate-ledger-write-asks-for-the-mark-of-a-lesson`
```

### Case 682.2 — The check of the mark leaves an unmarked lesson to the new check

> **given:**
> `estimate-ledger-write-refuses-a-mark-with-no-decision-line`: its Criterion is replaced whole.
> **＋** `guppi/ledger.py`: the `Stop` hook `uv run guppi ledger` that judges the mark.
> **＋** `guppi/materialize.py`: the one judgment of the mark, which the hook and `guppi materialize` share.
> **＋** `estimate-ledger-write-asks-for-the-mark-of-a-lesson`: the check of a lesson line with no mark.
> **＋** `estimate-ledger-write-refuses-a-lesson-without-its-prefix`: the check of the prefix, judged first.
> **＋** `estimate-ledger-write-lifts`: the told-once rule of the hook.

> **when:**
> The `Stop` hook `uv run guppi ledger` finds a fresh `lesson[<slug>]` line in a `LEDGER` block of the session, and the line carries `{addressed_by:case N}`.

> **then:**
> When no decision line of Case N stands before the lesson line — in the session's ledger, or earlier among the lines of the same `Stop` — the line is not written.
> **＋** The other lines of the `Stop` are written as before.
> **＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: lesson[<slug>] not written — {addressed_by:case <N>} names no decision line before it in this session; its sub-cases have case <N.1>, case <N.2>: write the line again after the decision line of the Case that closed the cause, naming that Case." The part on the sub-cases stands only when a decision line of a sub-case of N stands in the session.
> **＋** A refused line from an earlier text of the transcript is judged again at every `Stop` until it stands in the ledger. It is written at the first `Stop` where a decision line of Case N stands in the ledger before it. The hook says nothing about it.
> **＋** The hook and `guppi materialize` judge the mark by one function of `guppi/materialize.py`, over the ledger lines in their order, and give the same answer for the same lines.
> **－** A line that `estimate-ledger-write-refuses-a-lesson-without-its-prefix` refuses is not judged for its mark, and gets that refusal's stderr line alone.
> **－** A lesson line whose mark has a decision line of Case N before it is written as before, and so is a lesson line with no mark that `estimate-ledger-write-asks-for-the-mark-of-a-lesson` neither holds nor drops. A line already in the ledger of any session is not judged again.
> **－** Without a `hi` the hook judges no line. With `stop_hook_active` set it judges the line the same, and its stderr line is told once a stretch, as `estimate-ledger-write-lifts` sets it.

```then
update:
- slug: estimate-ledger-write-refuses-a-mark-with-no-decision-line
  set:
    status: pending
  change: the Criterion replaced whole — a lesson line with no mark is judged by estimate-ledger-write-asks-for-the-mark-of-a-lesson (case 682.2)
```

```tasks
- [x] update `estimate-ledger-write-refuses-a-mark-with-no-decision-line`
- [x] read `estimate-ledger-write-refuses-a-mark-with-no-decision-line`
```

## Case 683 — A supersede leaves an archived Decision in the archive

> **context:**
> When a Case carries `{supersedes:case N}`, `guppi generate` sets the page `decision-case-N` to `superseded` and adds the new Decision to its `superseded_by`. The cascade of the same run archives each Decision page under `vault/wiki/decisions/` that stands `superseded`, and `guppi cleanup` moves it to `vault/archive/`. Where `decision-case-N` already stands `archived` in the archive — superseded before, or archived by `guppi sprint-close` — `generate.decision` finds it there and sets it `superseded` again. The cascade does not look in the archive, so `cleanup` sees a page there whose status is no longer `archived` and moves it back to `vault/wiki/decisions/`. The next run archives it again. The page makes a round trip and gains History lines, with no change of meaning. Case 469 put off the fix on `rule-page-generation`, after session 2050 saw it once case 467.3 let one Decision be superseded by two Cases. This session meets it: Case 676 supersedes the Decisions of 19 Cases, from case 183 to case 322, and a Glob `vault/archive/**/decision-case-{183,206,218,231,242,248,252,254,260,263,269,276,281,285,289,293,303,307,322}.md` printed 19 paths, all under `vault/archive/migration/2026-09-28/1318/decisions/`. The code of this Case runs from the working tree as soon as Work Mode writes it, so the librarian's run of this session applies those marks to those 19 pages with the fix.
> The person agreed to take this item up beside Case 682, as a narrow fix of the pipeline: code and a test. The fix is the behaviour the defer of case 469 states: the archived page stays `archived` where it lies and takes the new Decision into `superseded_by`. It gets one History line `superseded by decision-case-M`, since `rule-decisions-schema` dates every change of `superseded_by` in History. The defers that the later Case retires are cleared as for any supersede (case 467.3). The test `test_a_later_case_superseding_the_archived_decision_clears_the_page_it_names` already covers that, and it gains the check that the page stays archived. A page that stands `current` is not changed by this Case: it still becomes `superseded`, and the cascade archives it. The last update in the History of `rule-page-generation` is case 672, which ticks the read lines of an Estimate closed by the person; case 673 updated `rule-orchestration`, by its line in `log.md`. Neither covers this. The step of case 660.3 already leaves an archived sub-case page alone, but `generate.decision` still sets the named page itself `superseded`. The update of `rule-page-generation` carries `{supersedes:case 469}`, which retires its one defer.
> The vault's answer: the Case creates no page, so no vault query on a `create` ran. The frame. A Grep `once a later Case names it|sets the earlier page` over `{vault/wiki/**,guppi/**,.claude/**,tests/**}` printed 4 files: `vault/wiki/glossary.md`, `vault/wiki/estimates/estimate-generate-writes-the-decision-page.md`, `vault/wiki/entities/entity-glossary.md` and `vault/wiki/rules/rule-decisions-schema.md`. The field `status` in the Render of `rule-decisions-schema` says a Decision becomes `superseded` once a later Case names it; that turns false for an archived page, so a pair adds the exception, and `uv run guppi render` writes `vault/wiki/decisions/schema.yaml`. Its Estimate `estimate-decisions-schema-checked` checks the lists and other prose of the file, not this sentence, so it stands. The row `Decision (status)` of `entity-glossary` says the same, so a pair adds the exception there, and `uv run guppi glossary` writes `vault/wiki/glossary.md` from it. `estimate-glossary-terms-defined` checks that no row contradicts its `where` page, which the pair keeps true, so it stands. `estimate-generate-writes-the-decision-page` says what a `supersedes` does to the earlier page, so its Criterion is replaced whole: its line on a `supersedes` gains the words "unless it stands `archived`", and a new line states what an archived page gets, while the other lines stay as they are; its `purpose` and `method` do not state the old promise, and they stand. `estimate-generate-cascades` says the cascade archives a `superseded` Decision page; that stays true, so it stands. The docstring of `guppi/generate.py` states the same sentence across a line break, so the Grep did not print it; the code task rewrites it. `guppi/cleanup.py` does not change: it still brings back a page whose status is no longer `archived`, which an `update` of an archived page needs (case 105.3).

> **problem:**
> A later Case that supersedes a Decision already in the archive sets it `superseded` again, so `cleanup` brings it back to the live vault and the next run archives it again, with History lines that change no meaning.

> **recommend:**
> - Recommended: an archived Decision that a later Case supersedes stays `archived` where it lies and only takes the later Decision into `superseded_by`, with one History line; the code of `generate.decision`, its test, the Criterion of `estimate-generate-writes-the-decision-page`, and the exception written into `rule-decisions-schema` and `entity-glossary`.
>   Answer: ratified as built
> - **Change**
>   - Asked: the person agreed to the fixes of the pre-spec report: the new line of the Criterion narrows the defers it clears to the targets a decision line of the superseding Case names, and `context` counts the archived Decisions of Case 676.
>   - Taken: the new line of the Criterion of `estimate-generate-writes-the-decision-page` names the same condition as the line after it; `context` says that all 19 Decisions that Case 676 supersedes stand in the archive, by a Glob over the 19.

> **given:**
> `rule-page-generation`: the rule of `guppi generate`, whose defer of case 469 this Case takes up.
> **＋** `guppi/generate.py`: `generate.decision`, which applies a `supersedes` to the earlier page.
> **＋** `tests/test_generate.py`: the tests of the Decision page.
> **＋** `estimate-generate-writes-the-decision-page`: its Criterion is replaced whole.
> **＋** `guppi/cleanup.py`: `guppi cleanup`, which moves back from the archive a page that stands other than `archived`.
> **＋** `rule-decisions-schema`: the shape of a Decision page, rendered into `vault/wiki/decisions/schema.yaml`.
> **＋** `entity-glossary`: the terms, rendered into `vault/wiki/glossary.md`.

> **when:**
> `uv run guppi generate` of `guppi/generate.py` applies a Case whose decision line supersedes an earlier Decision page that stands `archived` in the archive; `guppi cleanup` of `guppi/cleanup.py` runs after it.

> **then:**
> The earlier Decision page keeps `status: archived` and stays where it lies in the archive.
> **＋** Its `superseded_by` takes the Decision page of the later Case, with one History line that names that page.
> **＋** Each page that a decision line of the later Case names drops the earlier page from its `deferred_by`, as for a page that stands `current`.
> **＋** `guppi cleanup` does not move the earlier page back among the live Decision pages.
> **－** A Decision page that stands `current` still becomes `superseded`, and the cascade archives it.

```then
update:
- slug: rule-page-generation
  replace:
  - old: and no `deferred_by` is cleared through them (case 660.3);
    new: 'and no `deferred_by` is cleared through them (case 660.3); a page that a later Case supersedes while it stands `archived` stays `archived` where it lies: it takes the later Decision into its `superseded_by`, with one History line, and the `deferred_by` the later Case clears is cleared as for any page (case 467.3), so `cleanup` does not bring it back (case 683);'
  change: a supersede of a Decision already archived keeps it archived and only appends the superseding Case to its superseded_by, so cleanup does not bring it back (case 683)
- slug: estimate-generate-writes-the-decision-page
  set:
    status: pending
  sections:
    Criterion: |-
      When:
      `uv run guppi generate` reaches the first entry of a Case in `materialize.yaml`, or a `decisions` record with no page yet.

      Then:
      One page `vault/wiki/decisions/decision-case-<N>.md` is written: `case`, `status: current`, one list per kind present — `create`, `update`, `delete`, `defer` — the slugs in ledger order; `source` when a line carries one; `supersedes`; `origin`, `sprint`, `created`; `tags`, the union of the targets' tags; the body `## Problem` and `## Recommend` from `case_text` when it carries them, and `## Deferred` with one `### [[slug]]` per target of a `defer` line and its `purpose` verbatim.
      **＋** A record with `children`, a Case with sub-cases, gets its page before the pages of its sub-cases, with `children` their pages as quoted wikilinks, `tags` the union of theirs and no kind list; each page of a sub-case carries `parent`, its parent's page.
      **＋** A record with no `children` whose `case_text` carries no `given` — the short form of a deferred decision — also gets `## Context` from `case_text`, before `## Problem`.
      **＋** The page is written before the first entry of its lines, so their History lines name it.
      **＋** A `supersedes` sets the earlier page `superseded`, unless it stands `archived`, and appends to its `superseded_by`, and does the same to each page in the `children` of the earlier page, at any depth, that stands `current`, a page of an earlier session too. It removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names; an empty `deferred_by` is dropped.
      **＋** An earlier page that stands `archived`, under `vault/archive/` or under `vault/wiki/decisions/`, keeps `status: archived` and its place; it takes the new page into its `superseded_by` with one History line `superseded by decision-case-<N>`, and it removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names, as for a page that stands `current`.
      **＋** A target of the earlier page's `defer` list that no decision line of the superseding Case names keeps the earlier slug in its `deferred_by`; neither does a page reached only through `children` clear a `deferred_by`.
      **＋** An existing page is skipped; a `create` marked `exists` writes no page, but the Decision page of its Case is written.
      **＋** A record with `superseded_by` and no `case_text` gets a two-line body: `## Context` `Superseded by [[decision-case-M]] in its own session, before the Spec was approved; the Case left the Spec (case 299).`, `## Problem` `Decided under [[decision-case-M]].`
      **－** The page holds no `## Given`, no `## When` and no `## Criterion`, and no `## Context` when `case_text` carries `given` or the record carries `children`.
      **－** The Decision pages already written are not rewritten.
      **－** A page whose `superseded_by` already names the new page gets no second History line.
      **－** A page in `children` that stands `archived` or `superseded` is left as it is.
      **－** The page of a sub-case carries no `## Problem`, and a `case_text` with no `recommend` gives no `## Recommend`.
  change: the Criterion replaced whole — a supersedes leaves an earlier page that stands archived archived, and only appends to its superseded_by (case 683)
- slug: rule-decisions-schema
  replace:
  - old: a superseded Decision no longer describes the present (case 104.1);
    new: a superseded Decision no longer describes the present (case 104.1); a page that stands `archived` when a later Case names it stays `archived` and only takes that Case into `superseded_by` (case 683);
  change: a Decision page already archived stays archived when a later Case supersedes it (case 683)
- slug: entity-glossary
  replace:
  - old: '`archived` when the cascade of `generate` then meets it |'
    new: '`archived` when the cascade of `generate` then meets it; a page already `archived` stays `archived` when a later Case names it |'
  change: 'the row Decision (status): a page already archived stays archived when a later Case supersedes it (case 683)'
```

```tasks
- [x] update `rule-page-generation`
- [x] update `estimate-generate-writes-the-decision-page`
- [x] update `rule-decisions-schema`
- [x] update `entity-glossary`
- [x] `guppi/generate.py`: `generate.decision` sets the earlier page `superseded` only when it does not stand `archived`; it still appends to `superseded_by`, writes the History line, clears the defers and supersedes the children; the module docstring on a `supersedes` says so.
- [x] `tests/test_generate.py`: `test_a_later_case_superseding_the_archived_decision_clears_the_page_it_names` asserts the archived page keeps `status: archived`, stays under `vault/archive/`, names `decision-case-4` in `superseded_by` with one History line, and that no page `vault/wiki/decisions/decision-case-2.md` is written; a test that a page standing `current` still becomes `superseded` stands.
- [x] `uv run guppi render`: `vault/wiki/decisions/schema.yaml`
- [x] `uv run guppi glossary`
- [x] read `estimate-generate-writes-the-decision-page`
```

## Case 684 — Items taken up together are shown as one batch

> **context:**
> In this session the person took up five backlog items in one answer. The main agent dispatched a `case-guppi` for each item at once. It then showed each answer alone as it came back: a round, then a built Case for ratification, then another round, while the other builders were still out. The person stopped it, because a batch form had been agreed: wait for every builder, show one list of the questions, and show every Case at once for one ratification. The main agent then took the steps of the batch of case 598.1 for Cases 676 to 680. It wrote a `**Waiting:**` line while builders were out, showed one list of every open question numbered `<Case id>.Q<n>`, with its own question on another Case among them as 676.Q1, and then showed all five Cases in one reply. That worked. The Render of `rule-orchestration` lets Cases be shown together only in the loop after the findings of `/pre-spec` (case 561.2) and in a batch that a change of a ratified Case opens (case 598.1). It says nothing of several items taken up in one answer, so its rule of one Case per reply applied. Session 1831 made the same error with two Cases, as `lesson-orchestration-two-cases-built-side-by-side` records. That lesson belongs to another session, so this Case carries no `{addresses:}` mark (case 284.2).
> This Case replaces Case 681, which was ratified whole. A finding of `/pre-spec` showed that the batch also touches the dispatch: `case-guppi` is dispatched for each item of the batch at once, so no other Case of the batch is ratified or shown yet. Neither the sentence of `## Who builds a Case` on the dispatch nor the Criterion of `estimate-orchestration-names-related-cases-in-the-dispatch` makes the prompt name them. The person chose to widen the Case. That is a second promise, so the Case now has two sub-cases, and it takes a new number. Its decision lines carry `{supersedes:case 681}` (case 610.1). Case 684.1 is Case 681 as ratified and changed. Case 684.2 is the dispatch.
> The person chose these things. The batch opens when one answer of the person takes up two or more Frontier items. The question whether another Case is built again goes into the list of the batch, before any Case is shown. Only the text changes, and no hook is added. A new Estimate checks the batch, beside the existing one. After Case 681 was ratified, the person changed its reading. The batch of Cases 676 to 680 would fail it, because 679, 677, 680 and 676 were shown one by one before the person stopped it. So the reading at Retro of this session reads the next batch in the transcript instead: Cases 682 and 683, taken up together after Case 681 was ratified, with that Case built again in the same batch. Cases 682 and 683 change `rule-ledger-write`, `rule-page-generation`, `rule-decisions-schema` and `entity-glossary`, not `rule-orchestration`. For the dispatch, the prompt also names each other Case of the batch, and the Criterion of `estimate-orchestration-names-related-cases-in-the-dispatch` is replaced whole. Its old `purpose` states the old promise. Its old `method` waits for a later session, which `case-schema.md` no longer allows (case 670.4). So the same `update` sets both anew, and the reading is taken at Retro of this session over the same batch.
> The Render. Three pairs of `replace` in Case 684.1 change it. In `## Plan Mode and the Frontier` the second trigger joins the sentence that names the batch. In `## Who builds a Case` the sentence on the question about another Case says where that question stands in such a batch. In `## Showing and signing a Case` a sentence on the new trigger stands before the steps of the batch, so those steps apply to both triggers. The first sentence of `## Plan Mode and the Frontier` names "a batch, as below", which now covers both triggers, so it stands. One pair in Case 684.2 changes the sentence of `## Who builds a Case` on the dispatch. That pair touches another passage of the section than the pair of Case 684.1.
> The frame. The `Stop` check of `rule-case-check` (`round_opening` in `guppi/casecheck.py`) accepts a reply that opens with a bold label that ends in a colon, such as `**Waiting:**`. In the one-by-one showing it refused a round that opened with the main agent's own sentence. That refusal is correct, and the batch replies of this session passed, so the code does not change. `estimate-orchestration-signs-a-batch-together` speaks of the batch, but its When is the change of a ratified Case. That trigger stays, and its last exception, that outside a batch and the loop the next item waits, stays true with the wider batch, so its Criterion stands. `estimate-orchestration-shows-the-built-case` says that a Case with a line `**Other Case:**` is shown as it stands and that the main agent asks whether the other Case is built again. It does not say when the question comes, so it stays true and stands. Its Criterion also says how `case-guppi` is dispatched, but not which Cases the prompt names, so it stands. `estimate-orchestration-asks-in-the-grill-me-shape` sets the shape of that question, which does not change, and `estimate-orchestration-acknowledging-reply` already covers Cases shown together for one ratification, so both stand. `estimate-orchestration-loaded` promises only that the file equals the Render and is loaded, so it stands (case 378.5). The Render of `rule-prespec` says that inside its loop the rule of one Case at a time does not hold. That stays true, and its loop is not changed. The Render of `rule-case-build` tells `case-guppi` to read the case file of each Case that the prompt names. A Case of the batch whose file does not stand yet is named without a path, so there is nothing to read, and that text stays true. The `SubagentStop` check of `rule-case-check` (`session_clashes`) still compares each answer with the Cases of the session already stored. When the main agent sends a ratified Case of the batch back by `SendMessage`, that is no `Agent` call. That message stays outside the When of Case 684.2. The new Criterion of `estimate-orchestration-names-related-cases-in-the-dispatch` keeps each old line but three. The When names the Frontier by its path. The two exceptions add the Case of the same batch.
> The searches. A case-insensitive Grep of `shows one Case|one Case at a time|next Case until|one agent response` over `vault/wiki/`, without `log.md` and `brief.md`, printed `vault/wiki/orchestration.md`, `vault/wiki/rules/rule-orchestration.md` and `vault/wiki/rules/rule-case-protocol.md`. The hit in `rule-case-protocol` is a History line. The line "One agent response ≈ one Case." stays: the exceptions follow it. A case-insensitive Grep of `Waiting|one reply shows one Case|side by side` over `.claude/` printed `.claude/skills/pre-spec/SKILL.md` and `.claude/agents/case-guppi.md`. The first is the loop of `rule-prespec`, which stands. The second is about the sub-cases that `case-guppi` reads side by side, which is not this moment. A Glob of `vault/**/*taken-together*` printed nothing, so the new slug is free.

> **problem:**
> When the person takes up several Frontier items in one answer, nothing tells the main agent to wait for every builder and show the questions and the Cases together. So it shows each answer alone as it arrives, and the prompt of each builder names none of the other Cases of the batch.

> **recommend:**
> - **When does the batch form apply?**
>   - Recommended: (a) when the person's one answer takes up two or more Frontier items; an item taken up alone is still shown alone.
>   - Answer: agreed, (a).
> - **Where does the main agent's question about changing another Case go in a batch?**
>   - Recommended: (a) it joins the shared list of questions, numbered under the Case that raised it, before any Case is shown; on a yes the other Case joins the batch.
>   - Answer: agreed, (a).
> - **Does only the page enforce the batch form, or does a hook also enforce it?**
>   - Recommended: (a) only the page; no code changes.
>   - Answer: agreed, (a).
> - **Which check says the change is done?**
>   - Recommended: (a) a new Estimate, `estimate-orchestration-signs-items-taken-together`, beside the existing check, which stands.
>   - Answer: agreed, (a).
> - **How is the check read?**
>   - Recommended: (a) at Retro of this session, this session's own batch read in the transcript against the check.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: after the ratification of Case 681, the person asked that the reading try the next two items taken up side by side, and agreed to the items for Cases 682 and 683.
>   - Taken: the `method` of `estimate-orchestration-signs-items-taken-together` now reads, at Retro of this session, the batch of Cases 682 and 683 with Case 681 built again, not the batch of Cases 676 to 680; `context` says why.
> - **Change**
>   - Asked: at `/pre-spec`, a finding showed that the prompt of each builder of a batch names no other Case of the batch, and the person chose to widen the Case so that it does.
>   - Taken: Case 684.2 changes the sentence of `## Who builds a Case` on the dispatch, and replaces the Criterion, `purpose` and `method` of `estimate-orchestration-names-related-cases-in-the-dispatch`, read at Retro of this session over the same batch; the Case is built again as Case 684 with two sub-cases.

### Case 684.1 — Items taken up together are shown as one batch

> **given:**
> `rule-orchestration`: the rule whose Render sets when Cases are shown together.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`, which `/hi` loads.
> **＋** `estimate-orchestration-signs-items-taken-together`: the new check of the batch of items taken up together.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier whose items the person takes up.
> **＋** `case-guppi`: the builder dispatched for each item.
> **＋** `rule-prespec`: the loop after the findings of `/pre-spec`, whose steps the batch takes.
> **＋** `rule-case-check`: the `Stop` check that lets the `**Waiting:**` line pass, unchanged.
> **＋** `estimate-orchestration-signs-a-batch-together`: the check of the batch that a change of a ratified Case opens, which stands.

> **when:**
> In Plan Mode before `/pre-spec`, one answer of the person takes up two or more items of `raw/<date>/<hi HHMM>/frontier.md`, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The main agent dispatches a `case-guppi` for each item, and shows no round and no Case of them alone: they are one batch.
> **＋** While an answer of a `case-guppi` of the batch is out, the main agent ends each turn with one line that opens with the bold label `**Waiting:**`, translated, and names the Cases that have answered and those still out. It writes nothing else in the chat, and `rule-case-check` refuses no such reply.
> **＋** It shows one list of every round that came back, each question numbered `<Case id>.Q<n>`. It sends each answer to the `case-guppi` of its Case, all in one message, until every `case-guppi` of the batch has answered with its Case.
> **＋** A question whether another Case is built again, which a line `**Other Case:**` in a summary of the batch raises, stands in that list, numbered under the Case that raised it, before any Case of the batch is shown. On the person's yes, that other Case goes back to its `case-guppi` and joins the batch.
> **＋** It shows every Case of the batch in one reply, each in the showing that `vault/wiki/orchestration.md` sets, for one ratification. The person ratifies the batch at once or names the ids.
> **－** An item the person takes up alone is shown alone, and the next item waits until its Case is ratified or deferred.
> **－** The loop after the findings of `/pre-spec` stays as `rule-prespec` sets it.

```then
create:
- slug: estimate-orchestration-signs-items-taken-together
  ref: rule-orchestration
  kind: QA
  purpose: Whether, when the person's one answer takes up two or more Frontier items, the main agent shows their rounds in one list and their Cases in one reply for one ratification, with the waits marked
  method: 'by hand at the Retro of session 2249: the replies in its transcript from the dispatch of Cases 682 and 683, taken up together with Case 681 built again, to the reply that acknowledged that batch, read against the Criterion'
  tags:
  - session
  - workflow
update:
- slug: rule-orchestration
  replace:
  - old: and in a batch, when the person's word asks that a Case already ratified change while another Case is built, as `## Showing and signing a Case` sets it (case 598.1).
    new: and in a batch, when the person's one answer takes up two or more items of the Frontier, or when the person's word asks that a Case already ratified change while another Case is built, as `## Showing and signing a Case` sets it (cases 598.1, 684.1).
  - old: in a batch when it is ratified, as `## Showing and signing a Case` sets it (case 629.1);
    new: in a batch when it is ratified, as `## Showing and signing a Case` sets it (case 629.1); in a batch of items the person took up together, the question stands in the list of the batch before any Case of it is shown (case 684.1);
  - old: the two are a batch, and a Case that a Case of the batch asks to change in the same way joins it.
    new: 'the two are a batch, and a Case that a Case of the batch asks to change in the same way joins it. When, before `/pre-spec`, the person''s one answer takes up two or more items of the Frontier, the agent dispatches a `case-guppi` for each of them and shows no round and no Case of them alone: they are a batch too. A question whether another Case is built again, which the line `**Other Case:**` of a summary of that batch raises, stands in the list of its rounds, numbered `<Case id>.Q<n>` under the Case that raised it, before any Case of the batch is shown, and on the person''s yes that other Case goes back to its `case-guppi` and joins the batch (case 684.1).'
  change: 'Frontier items taken up together in one answer are a batch: the questions in one list, every Case shown for one ratification (case 684.1)'
```

```tasks
- [x] update `rule-orchestration`
- [x] `uv run guppi render`: `vault/wiki/orchestration.md`
- [x] create `estimate-orchestration-signs-items-taken-together`
- [x] read `estimate-orchestration-signs-items-taken-together`
```

### Case 684.2 — The prompt of a builder in a batch names the other Cases of the batch

> **given:**
> `rule-orchestration`: the rule whose Render sets what the prompt of `case-guppi` names.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`, which `/hi` loads.
> **＋** `estimate-orchestration-names-related-cases-in-the-dispatch`: its Criterion, `purpose` and `method` replaced.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier whose items the person takes up.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the case file whose path the prompt names.
> **＋** `case-guppi`: the builder the prompt goes to.
> **＋** `rule-case-build`: the rule of `case-guppi`, which reads the case file of each Case the prompt names.

> **when:**
> The main agent dispatches `case-guppi` by an `Agent` call to build the Case of an item of `raw/<date>/<hi HHMM>/frontier.md`, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The prompt of the call names each Case of the session, ratified or already shown, that changes a page the item names or sets what happens at the same moment as the item: the same kind of reply, the same hook event or the same command.
> **＋** Each such Case stands in the prompt by its id, one sentence on what it sets and which pages it changes, and the path of its case file `raw/<date>/<hi HHMM>/cases/case-<N>.md`.
> **＋** When the item is one of two or more items that one answer of the person took up, the prompt also names each other Case of that batch by its id and its Frontier item, and by the path of its case file where that file stands.
> **＋** The main agent judges which Cases of the session are related, and the prompt does not send `case-guppi` to search the Cases of the session.
> **－** A Case of the session that changes no page the item names, acts at another moment and is no Case of the same batch need not stand in the prompt.
> **－** When no Case of the session is related and the item is taken up alone, the prompt names none and holds the Case id, the Frontier item with its source and the person's words.

```then
update:
- slug: rule-orchestration
  replace:
  - old: the main agent judging which Cases are related and `case-guppi` reading no other Case of the session (case 579.1)
    new: the main agent judging which Cases are related and `case-guppi` reading no other Case of the session (case 579.1), and, when the item is one of a batch of items the person took up in one answer, each other Case of that batch by its id and its Frontier item, and by the path of its case file where that file stands (case 684.2)
  change: the prompt of a builder in a batch of items taken up together names each other Case of the batch (case 684.2)
- slug: estimate-orchestration-names-related-cases-in-the-dispatch
  set:
    status: pending
    purpose: Whether the main agent's prompt to case-guppi names each Case of the session that changes a page the item names or acts at the same moment, by its id, one sentence on what it sets and the path of its case file, and each other Case of a batch of items the person took up in one answer
    method: 'by hand at the Retro of session 2249: the Agent calls that dispatched case-guppi for Cases 682 and 683 in its transcript, read against the Criterion; a Case of the batch or a related Case left unnamed counted in the reading line'
  change: the Criterion replaced whole — the prompt of a builder in a batch names each other Case of the batch; the purpose and the method set anew (case 684.2)
```

```tasks
- [x] update `rule-orchestration`
- [x] update `estimate-orchestration-names-related-cases-in-the-dispatch`
- [x] read `estimate-orchestration-names-related-cases-in-the-dispatch`
```
