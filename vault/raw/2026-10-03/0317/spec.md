<!-- approved 04:52:38 · session 5b311f89 -->

# Spec — session 0317, 2026-10-03

## Case 611 — The Stop check refuses a showing of a Case with the agent's own text outside its list and ratification

> **context:**
> When `case-guppi` has built a Case, the main agent shows it in one reply. It sends the Case file. It writes the Case heading with the name in Russian, one list under the heading with a short text on each Case and sub-case, and one `ratification` with the ledger lines. The agent's own text comes only after one horizontal rule. `orchestration.md`, the Render of `rule-orchestration`, sets this layout, and the promise of `estimate-orchestration-shows-the-built-case` states it. The `Stop` run of `guppi/casecheck.py` compares the `ratification` with the stored answer. Since case 562 it also refuses a round of questions that has the agent's own text before it. Nothing reads the other text of a showing: its docstring says that text under the heading outside its sections is not compared. In session 0115 the batch showing after `/pre-spec` put a sentence on the renumbering of Case 608 between the heading of Case 610 and its list. Nothing refused it. The reading of `estimate-orchestration-shows-the-built-case` failed on it (ledger line 18 of `raw/2026-10-03/0115/ledger.md`). `lesson-orchestration-own-sentence-between-heading-and-list` records it. That lesson and `lesson-orchestration-own-text-before-a-prespec-round` reopened `insight-case-form-chat-form-read-by-no-script` at the synthesis of 0115.
>
> The person chose that the check refuse such a note rather than allow it. The check reads the whole showing up to the horizontal rule, heading by heading. The person read text before the heading as part of the showing. The agent's own text written in the turn before its last tool call also stands above the heading in the chat, so this Case judges it too. It uses the same judgment of that text, `texts_before_last_call`, that the check of a round has used since case 562, with no second copy (`rule-one-judgment-one-implementation`). A Case heading here is `## Case N —` or `### Case N.M —`. A sub-case shown alone under its own heading is judged the same way. Any section other than `ratification` under a heading is refused, since `orchestration.md` already forbids showing `given`, `when`, `then` or `tasks`.
>
> The new promise is `estimate-case-check-refuses-text-outside-the-list`, on `rule-case-check`. Three Estimates stand as they are:
> `estimate-case-check-refuses-text-before-a-round` keeps its Criterion, because it speaks only of a turn that holds a round.
> `estimate-case-check-shows-only-the-checked-case` keeps its Criterion. It speaks of the comparison with the stored answer, which does not change. Its line that text under the heading outside its sections is not compared stays true of that comparison. Its line that a showing of the heading, a short text and `ratification` alone passes when its `ratification` equals the answer also stands, because the short text of a showing is the list item that `orchestration.md` sets. That showing passes both the comparison and the new check. A short text that is not a list item is refused by the new check, and that promise does not speak of it.
> `estimate-orchestration-shows-the-built-case` keeps its Criterion word for word, because it already forbids the note. It is read again in a later session.
> The reader in code changes, and the text it enforces already stands in `orchestration.md`, so nothing waits for a render. The refusal loses nothing: a showing carries its ledger lines only as a preview, never in a `LEDGER` block, and the refused reply is shown again. So the check keeps no old form.
>
> The frame contains these facts. `.claude/settings.json` registers six commands on `Stop`: `guppi ledger`, `guppi ratified`, `guppi casecheck`, `guppi context`, `guppi onward` and `guppi onward --plan`. None of the others sets the layout of a showing. The Spec hook `guppi ratified` reads a showing by `showings` and is not changed. A Grep of `casecheck` over `tests/test_ratified.py` printed only calls of `store_of`, `shows_sections`, `shown_text` and `case_file`, not the `Stop` run, so its tests are not touched. In `.claude/skills/pre-spec/SKILL.md`, step 6 shows each Case built again in the showing that `orchestration.md` sets, so the batch is judged like any showing. In the turn of that showing, the last answer of a `case-guppi` opens the turn, and no `**Waiting:**` line stands there.
>
> In `tests/test_casecheck.py`, a multiline Grep of `show\(\s*working,\s*ANSWER` printed six calls, at lines 819, 823, 829, 970, 1320 and 1329:
> Line 819 expects exit 0 with the full answer under its heading, and it changes.
> Lines 823, 829 and 1320 expect exit 2 with reasons that still come.
> Lines 970 and 1329 are the re-fire.
>
> A Grep of `== \(0, ""\)` over the same file printed further `show(` calls that expect exit 0 with sections under a heading, or with a short text that is not a list item. They are at lines 842, 870, 872, 891, 910, 922, 951, 963, 964, 1020 and 1290, the last one on `RECUT`. These now get the layout reason too. Where such a test checks the comparison, it asserts the comparison's reason alone. Where it checks a pass, it shows the list layout, as `SHORT_SHOWING` will with its short text as a list item. The other calls that this Grep printed are not judged by the new check, or already pass it:
> The acknowledging reply, a `DIFF` fence and the short form are at lines 928, 941, 942 and 943.
> A list showing is at line 1001.
> Replies with no Case heading are at lines 1098, 1109, 1111 and 1124.
> A re-fire is at line 1151.
>
> A Grep of `showing of a Case|shows a Case|show(s|n)? the Case` over `vault/wiki/rules/` and `.claude/` printed one file: `vault/wiki/rules/rule-orchestration.md`, the source of `orchestration.md`, which sets the layout this Case enforces.
>
> A Grep of `outside its sections|under the heading` over `vault/wiki/` outside `decisions/`, `.claude/`, `guppi/` and `tests/` printed 13 files. They are `brief.md`, `orchestration.md`, `case-schema.md`, `log.md`, `rules/rule-case-protocol.md`, `lessons/lesson-orchestration-own-sentence-between-heading-and-list.md`, `rules/rule-case-check.md`, `guppi/casecheck.py`, `tests/test_casecheck.py`, `rules/rule-orchestration.md`, `estimates/estimate-case-check-shows-only-the-checked-case.md`, `tests/test_ratified.py` and `guppi/generate.py`. Each one stays true, for these reasons:
> `orchestration.md` and its source set the layout.
> `case-schema.md` and its source `rule-case-protocol` speak of the heading of the Case file.
> The docstring of `guppi/casecheck.py` and the Estimate speak of the comparison.
> The test at line 617 of `tests/test_ratified.py` shows a list under its heading, which the new check passes.
> Line 474 of `guppi/generate.py` speaks of the Spec.
> The hit in `tests/test_casecheck.py` heads the tests of the list showing.
> `brief.md` and `log.md` were not read.
>
> A Grep of `insight-case-form-chat-form-read-by-no-script` over the repository outside `vault/wiki/decisions/` printed 54 files. Six are in `vault/wiki/`: `brief.md`, `backlog.md`, `log.md`, the two lessons, and `rules/rule-case-check.md`, whose Purpose says that until case 419 no script read a Case before its ratification, which stays true. Three are in `vault/raw/2026-10-03/`: `0317/ledger.md`, `0317/frontier.md` and `0115/materialize.yaml`, which are records of the sessions. The other 45 are under `vault/archive/`.
>
> The Insight is set `actioned`, as case 605 did after the check of a round. Its `addressed_by` names `decision-case-611`. Its two live children stand `clustered`, so the cascade of `guppi/generate.py` archives them, and `guppi backlog` drops the Insight's line. Both lessons stand in the ledger of session 0115, so no decision line carries `{addresses}`. The Insight has no `deferred_by`, so no `{supersedes:case N}` block is needed. `insight-workflow-case-schema-silent-on-what-the-scripts-accept` is not touched: it is about the forms the scripts accept in a Case, not about the layout of a showing. The Case makes no `create` without a `ref`, so the vault query was not run.
>
> Not done: `orchestration.md` and the Criteria of the three Estimates above do not change. The comparison of `given`, `when`, `then` and `tasks` in a showing stays in the code, although the new check now refuses a showing of those sections.

> **problem:**
> The rule of how a built Case is shown puts every text of the agent's own after the horizontal rule, but no script reads that part of a showing. In session 0115 a note under the heading of a Case went through, and the reading of `estimate-orchestration-shows-the-built-case` failed. The question was whether such a note is allowed, or whether the `Stop` check of `rule-case-check` refuses it, and how much of the showing the check reads.

> **recommend:**
> - **A note between the Case heading and its list**
>   - Recommended: (a) the check refuses it; a note goes after the horizontal rule.
>   - Answer: agreed, (a).
> - **How much of the showing the check reads**
>   - Recommended: (b) the whole showing up to the horizontal rule: nothing before the first Case heading, and under each heading only the list, the `ratification` blockquote and blank lines.
>   - Answer: accepted the recommendation, (b).
> - **What checks the new refusal**
>   - Recommended: (a) a new promise of its own on `rule-case-check`; the promise on rounds and the comparison promise stand.
>   - Answer: accepted the recommendation, (a).
> - **The failed reading and the open insight**
>   - Recommended: (a) the promise of `estimate-orchestration-shows-the-built-case` stays word for word and is read again in a later session; the insight is marked as acted on; `insight-workflow-case-schema-silent-on-what-the-scripts-accept` is not touched.
>   - Answer: accepted the recommendation, (a).

> **given:**
> `guppi/casecheck.py` — the `Stop` run that gains the refusal; its docstring says how it works
> **＋** `tests/test_casecheck.py` — the tests of the `Stop` run
> **＋** `.claude/settings.json` — registers `uv run guppi casecheck` on `Stop`
> **＋** `rule-case-check` — the rule of the check; its Purpose gains the refusal
> **＋** `estimate-case-check-refuses-text-outside-the-list` — the new promise
> **＋** `vault/wiki/orchestration.md` — rendered from `rule-orchestration`; sets the layout of a showing that the check enforces
> **＋** `estimate-orchestration-shows-the-built-case` — the promise of the showing, read again
> **＋** `insight-case-form-chat-form-read-by-no-script` — the Insight on rules of the chat form that no script reads, set `actioned`

> **when:**
> `Stop` fires after a reply of the main agent that shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections, not a deferred decision in the short form, and `uv run guppi casecheck` runs on it, as `.claude/settings.json` registers it.

> **then:**
> `uv run guppi casecheck` exits 2 when a line that is not blank stands in the reply before its first Case heading.
> **＋** It exits 2 when a line stands between a Case heading and the next Case heading or the horizontal rule `---` that is not blank, not a list item — a line that opens with `- `, `* ` or a number and `. ` — not a line indented under a list item, and not a line of the `ratification` blockquote, its `> **ratification:**` line and the `>` lines after it.
> **＋** It exits 2 when the main agent wrote text in the turn of the reply before its last tool call, judged by `texts_before_last_call` of `guppi/casecheck.py`, the judgment the check of a round uses.
> **＋** Its reason on stderr quotes the first such text and tells the agent to show the Case again with that text moved after the horizontal rule.
> **＋** The check runs in the same `Stop` run as the comparison of shown Cases with the stored answer and the check of how a round opens, and a reply that more than one of them refuse gives each reason.
> **－** Text after the horizontal rule is not judged.
> **－** A reply with no Case heading that holds a section, the acknowledging reply among them, a fence tagged `DIFF`, and a deferred decision in the short form are not judged.
> **－** On the re-fire (`stop_hook_active`) it exits 0, so the Case shown again after a refusal is not judged again.
> **－** It stores nothing and writes no file.

```then
create:
- slug: estimate-case-check-refuses-text-outside-the-list
  ref: rule-case-check
  kind: QA
  purpose: Whether the Stop run of the Case check refuses a reply that shows a Case with a text of the main agent's own before its first Case heading, under a heading outside the list and the ratification, or before the last tool call of the turn
  method: uv run pytest tests/test_casecheck.py; by hand in a later session, the showings of Cases and the hook's refusals of them read in the transcript
  tags:
  - hooks
  - harness
  - workflow
update:
- slug: rule-case-check
  set:
    purpose: Prevents a Case from being shown to the person in a form the checks of pre-spec refuse, or with other given, when, then, tasks or ratification than the ones that passed them, a round of case-guppi from reaching the main agent with a question out of the form of the grill-me template, a round of case-guppi from being shown after a text of the main agent's own, and a Case from being shown with a text of the main agent's own outside the list under its heading and its ratification
  replace:
  - old: (case 601.1), and a round of `case-guppi` from being shown after a text of the main agent's own (case 562)
    new: (case 601.1), a round of `case-guppi` from being shown after a text of the main agent's own (case 562), and a Case from being shown with a text of the main agent's own outside the list under its heading and its `ratification` (case 611)
  change: the Stop check refuses a showing of a Case with a text of the main agent's own outside the list under its heading and its ratification (case 611)
- slug: insight-case-form-chat-form-read-by-no-script
  set:
    status: actioned
    addressed_by: decision-case-611
  change: 'actioned: the Stop check of rule-case-check refuses a showing of a Case with a text of the main agent''s own outside the list under its heading and its ratification (case 611)'
```

```tasks
- [x] `guppi/casecheck.py`: the `Stop` run refuses a showing with text before its first Case heading, text under a Case heading that is not a list item, its indented line or the `ratification` blockquote, and text of the main agent's own before the last tool call of the turn; the text before the last tool call is judged by the existing `texts_before_last_call`, and the `ratification` blockquote by the existing `RATIFICATION_HEAD` and `quoted_sections`, with no second copy of either; the module docstring says how
- [x] `tests/test_casecheck.py`: tests of each refusal, of a list showing and a batch that pass, of text after the horizontal rule left alone and of the re-fire; the `show(` calls that expect exit 0 with sections under a heading or a short text that is not a list item show the list layout where they check a pass, and assert the comparison's reason alone where they check the comparison
- [x] update `rule-case-check`
- [x] create `estimate-case-check-refuses-text-outside-the-list`
- [x] update `insight-case-form-chat-form-read-by-no-script`
- [ ] read `estimate-case-check-refuses-text-outside-the-list`
- [ ] read `estimate-orchestration-shows-the-built-case`
```

## Case 612 — What the close of a sprint moves to the archive and what it keeps

> **context:**
> A sprint is an Entity Leaf, `entity-sprint-<id>`. Its `estimates` are the sprint's done-conditions, and `guppi sprint` renders it into `vault/wiki/sprint.md`, which `/hi` loads. Nothing closes a sprint today. Under its closing milestone, the sprint page holds only an undecided note (case 478.2). It says the sprint page and its Estimates go to the archive once each has passed. A page leaves the live vault today only through an event of its own. A Decision page leaves when a later Case supersedes it. The lessons of an Insight leave once that Insight is `actioned`. An `open` Insight leaves when no live lesson is left under it. Any page leaves when a Case deletes it. The cascade of `guppi/generate.py` sets `archived`, and `guppi cleanup` (`rule-cleanup`) moves the page under `vault/archive/<sprint>/`. Everything else stays live. The main agent counted the live vault this session: 1003 Decision pages (2.7 MB), 74 lessons, 29 Insights and 195 Estimates, of which 37 are `pending` and 1 is `failed`. The person sees an endless loop of fixes, with readings that hang session after session, and wants the close of a sprint to clean the vault.
>
> In the rounds the person chose what the close does. It archives the sprint's Decision pages, but keeps those that a live page names in `deferred_by` or `addressed_by`. It archives the sprint's `actioned` Insights and its `error` lessons that joined no Insight, and keeps `knowledge` lessons and `open` Insights with their lessons. It archives the sprint page with its own Estimates, and keeps every other `passed` Estimate as the contract of its rule. Before anything moves, it puts each `pending` or `failed` Estimate to the person: read it, carry it into the next sprint, or archive it unread. The person did not decide where the close runs. They see it as a mode of work of its own, not a choice after Plan Mode, and left it for later. So this Case creates `rule-sprint-close` as a draft that holds these choices. The rule has no `enforcement` and no code. The rules schema keeps `enforcement` optional, and the Case that decides where the close runs gives the rule its guard. Not done: where the close runs, how the next sprint opens, and any code.
>
> The sprint page's own Estimates are read at the close itself. Their methods say so:
> - `estimate-sprint-migration-leftovers-gone` reads the tree by hand at the close of the sprint.
> - `estimate-sprint-migration-lint-clean` reads `make lint` at the close.
> - `estimate-sprint-migration-merges` reads `git log` of `main` at the close, and its Criterion calls the cascade's `built` on the sprint page the close of the sprint.
>
> So these Estimates cannot pass before the close runs. In this Case the close runs first and reads the sprint page's own Estimates in it. Pages move only once each of those Estimates has passed, which is when the cascade sets the sprint page `built`. This matches the merge Estimate's wording and the order of 612.4. All three Criteria therefore stand.
>
> The person chose that this sprint closes with a clean lint, so the Criterion of `estimate-sprint-migration-lint-clean` stands. At this sprint's first close, carrying an Estimate forward would leave an `unread` line that fails that Criterion.
>
> The rule's four parts can fail separately and need different fixes, so each part is a sub-case with an Estimate of its own. Each Estimate is read by hand after the first close of a sprint. The four sub-cases share the same trigger and the same shape of result, and each one names a different set of pages. The check of the answer noted that their `then` lines share words, and that is why.
>
> The closing milestone of `entity-sprint-migration` names the new rule as its item, and a plain note there says that where the close runs is not decided. A note keeps the milestone open (`rule-sprint`), and every session sees it in `sprint.md`. No put-off decision is written. That would add a `deferred` line to `make lint`, which the current sprint's clean-lint condition would have to clear.
>
> The vault query of `.claude/agents/ask-guppi.md` ran for the `create` without a `ref`. These are its findings:
> - exists: none. A Glob of `vault/wiki/**/rule-sprint-close*.md` and one of `vault/archive/**/*sprint-close*.md` printed no file, so the slug is free.
> - near: `rule-cleanup` moves a page that already stands `archived` but chooses none; `rule-sprint` renders the sprint page and does not close it; `entity-sprint` is the kind, which carries no Estimate.
> - rules: `lesson-case-build-closes-a-sprint-item-without-the-sprint-page` requires a Case that closes a sprint item to update the sprint page, which 612.1 does.
> - tags: `sprint` and `workflow`, both existing.
>
> `rule-morph` is a line under the `## Backlog` of the sprint page, about the category set, and this Case does not touch it. `applies_to: [entity-sprint]` makes the cascade add the new rule to the `rules` of `entity-sprint`. Its Purpose sentence that the page carries no Estimate stays true, because the new Estimates target the rule.
>
> Some texts say today that a lesson or an Insight leaves only through its Insight, or that an `actioned` Insight stays live for a later lesson to join. These texts become false only when a close first runs, and nothing runs one until the Case that decides where it runs. That Case changes them, and the Purpose of the new rule names them. A Grep of `archived only when|kept for the recurrence|stays live with its|never archived` over the repository outside `vault/wiki/decisions/`, `vault/archive/` and `vault/raw/` printed 5 files:
> - `.claude/agents/librarian-guppi.md`
> - `vault/wiki/insights/schema.yaml`
> - `vault/wiki/rules/rule-synthesis.md`
> - `vault/wiki/rules/rule-insights-schema.md`
> - `vault/wiki/estimates/estimate-synthesis-clusters.md`
>
> The first two are the renders of `rule-synthesis` and `rule-insights-schema`. The pre-spec check named `estimate-synthesis-keeps-actioned-by-the-mark` as well. Its Criterion has a later lesson join an existing `actioned` Insight, which keeps its status. That Insight is no longer live once a close has archived it. A Grep of `archived` over `rule-lessons-schema.md` and `rule-decisions-schema.md` printed the `status` field of each. One says a lesson is archived when its Insight is `actioned`. The other says a Decision page is archived when superseded. These stand until that Case too.
>
> A Grep of `close of (the|a) sprint|sprint clos|closes? the sprint` over `vault/wiki/rules/` and `.claude/` printed one file, `rule-prespec.md`, and the hit is a History line. A Grep of `478\.2|Slice 5` over the repository outside `vault/wiki/decisions/`, `vault/archive/` and `vault/raw/` printed 9 files:
> - `brief.md`
> - `backlog.md`
> - `sprint.md`
> - `log.md`
> - `entity-sprint-migration.md`
> - `estimate-sprint-items-move-only-by-a-case.md`
> - `estimate-hi-writes-frontier.md`
> - `tests/test_sprint.py`
> - `rule-morph.md`
>
> `brief.md` and `log.md` were not read. `sprint.md` is rendered again. The hits in `backlog.md` and `rule-morph.md` are the line of `rule-morph`. The hits in the two Estimates are Results of past readings. The hits in `tests/test_sprint.py` are test fixtures. All of these stay true. The Estimates of `rule-sprint` and `rule-cleanup` speak of the render, of moves by a Case and of the moves of `cleanup`, none of which this Case changes. Case 611 changes `rule-case-check` and an Insight, and sets nothing about a sprint.

> **problem:**
> Nothing closes a sprint, and the live vault only grows. Decision pages, finished Insights, lessons that never recurred and hanging readings stay live for good. The question was what the close of a sprint moves to the archive, what it keeps, how each part is checked, and where the close runs. The person settled everything except where it runs.

> **recommend:**
> - **What happens to the sprint's Decision pages at the close?**
>   - Recommended: (a) archive them, except the ones an open defer names.
>   - Answer: agreed, (a).
> - **What happens to lessons and Insights at the close?**
>   - Recommended: (a) archive actioned Insights and failure lessons that joined nothing; keep fact lessons and open Insights with their lessons.
>   - Answer: agreed, (a).
> - **What happens to the Estimates that passed?**
>   - Recommended: (a) keep them live; the close archives only the sprint page's own Estimates.
>   - Answer: agreed, (a).
> - **What happens to Estimates still pending or failed at the close?**
>   - Recommended: (c) the close settles each one: read it now, carry it into the next sprint, or archive it unread.
>   - Answer: agreed, (c).
> - **Who closes a sprint?**
>   - Recommended: (a) a Case you ratify.
>   - Answer: not one of the options. The close of a sprint is more than a Case: it is a separate skill or agent, more likely a separate mode of work. Where to place it is unclear, and a choice after Plan Mode seems illogical. It needs more thought. Replaced by the question where the close runs.
> - **Where does the close of a sprint run?**
>   - Recommended: (a) record what the close does now, and decide later where it runs.
>   - Answer: agreed, (a); to be thought about later.
> - **Where does the open question of where the close runs stay until you decide it?**
>   - Recommended: (a) a note on the sprint page.
>   - Answer: agreed with the recommendation, (a).
> - **How is the close checked?**
>   - Recommended: (a) four Estimates, one per part, read by hand at the first close.
>   - Answer: agreed with the recommendation, (a).
> - **What happens to the current sprint's clean-lint condition?**
>   - Recommended: (a) replace its Criterion so that Estimates carried into the next sprint may stay unread.
>   - Answer: (b), leave it as it stands; this sprint will close with a clean lint.

### Case 612.1 — The close archives the sprint's Decision pages, except the ones a live page names

> **given:**
> `rule-sprint-close` — the new rule of what the close of a sprint archives and keeps
> **＋** `estimate-sprint-close-archives-the-decisions` — the promise on Decision pages
> **＋** `entity-sprint-<id>` — the sprint page that closes, with the Estimates it lists
> **＋** `vault/wiki/decisions/` — the Decision pages, each with its `sprint`
> **＋** `vault/archive/` — where an archived page stands, moved there by `rule-cleanup`
> **＋** `entity-sprint-migration` and `vault/wiki/sprint.md` — the current sprint page, whose closing milestone names the new rule and keeps a note, and its render by `guppi sprint`
> **＋** `rule-sprint` — the form of a milestone item and of a note

> **when:**
> The close of the sprint `entity-sprint-<id>` runs: the Estimates that `entity-sprint-<id>` lists are read in it first, and its pages move once each of them stands `passed`; someone reads `vault/wiki/decisions/` and `vault/archive/` after it.

> **then:**
> Each Decision page under `vault/wiki/decisions/` whose `sprint` is `<id>` stands under `vault/archive/`.
> **－** A Decision page that a live page names in `deferred_by` or `addressed_by` stays under `vault/wiki/decisions/`.
> **－** A Decision page whose `sprint` is another sprint does not move.

```then
create:
- slug: rule-sprint-close
  type: rule
  kind: Leaf
  purpose: Prevents a closed sprint from leaving its finished work among the live pages, so that the vault does not only grow
  applies_to:
  - entity-sprint
  tags:
  - sprint
  - workflow
  sections:
    Purpose: 'Prevents a closed sprint from leaving its finished work among the live pages, so that the vault does not only grow. The close of `entity-sprint-<id>` reads the Estimates the sprint page lists first, and its pages move only once each of them has passed. Then the Decision pages of the sprint go to the archive, but a Decision page that a live page names in `deferred_by` or `addressed_by` stays (case 612.1). The `actioned` Insights of the sprint go, and its `error` lessons that joined no Insight; its `knowledge` lessons, its `open` Insights and their lessons stay (case 612.2). The sprint page and the Estimates it lists go; every other `passed` Estimate stays, the contract of its rule (case 612.3). Before anything moves, each Estimate that stands `pending` or `failed` is put to the person, who has it read, carries it into the next sprint, or archives it unread (case 612.4). Where the close runs, and how the next sprint opens, are not decided: the Case that decides them gives this rule its guard, and changes the texts that say a lesson, an Insight or a Decision page leaves only through its own event, or that an `actioned` Insight stays live for a later lesson: `rule-insights-schema`, `rule-lessons-schema`, `rule-decisions-schema`, `rule-synthesis`, `estimate-synthesis-clusters` and `estimate-synthesis-keeps-actioned-by-the-mark`.'
- slug: estimate-sprint-close-archives-the-decisions
  type: estimate
  ref: rule-sprint-close
  kind: QA
  purpose: At the close of a sprint its Decision pages go to the archive, but those a live page names in deferred_by or addressed_by
  method: by hand, vault/wiki/decisions/ and vault/archive/ read after the first close of a sprint
  tags:
  - sprint
  - workflow
update:
- slug: entity-sprint-migration
  replace:
  - old: '- the close of a sprint — `entity-sprint-<id>` and the Estimates it lists go to the archive together once each has passed: a done-condition of a sprint has nothing left to guard after the close; not yet decided (case 478.2)'
    new: |-
      - [[rule-sprint-close]] — what the close of a sprint moves to the archive and what it keeps (case 612.1)
      - where the close of a sprint runs — a session of its own, a command or another place: not decided (case 612.1)
  change: 'Slice 5: the close of a sprint is the item rule-sprint-close, and where the close runs is a note, not decided (case 612.1)'
```

```tasks
- [x] create `rule-sprint-close`
- [x] create `estimate-sprint-close-archives-the-decisions`
- [x] update `entity-sprint-migration`
- [x] `uv run guppi sprint`
- [ ] read `estimate-sprint-close-archives-the-decisions`
```

### Case 612.2 — The close archives actioned Insights and failure lessons that joined no Insight

> **given:**
> `rule-sprint-close` — the rule of the close
> **＋** `estimate-sprint-close-archives-done-insights-and-lone-lessons` — the promise on lessons and Insights
> **＋** `entity-sprint-<id>` — the sprint page that closes, with the Estimates it lists
> **＋** `vault/wiki/insights/` and `vault/wiki/lessons/` — the Insights and lessons, each with its `sprint`
> **＋** `vault/archive/` — where an archived page stands
> **＋** `rule-insights-schema`, `rule-lessons-schema` and `rule-synthesis` — say today when a lesson or an Insight leaves; unchanged here

> **when:**
> The close of the sprint `entity-sprint-<id>` runs: the Estimates that `entity-sprint-<id>` lists are read in it first, and its pages move once each of them stands `passed`; someone reads `vault/wiki/insights/`, `vault/wiki/lessons/` and `vault/archive/` after it.

> **then:**
> Each Insight under `vault/wiki/insights/` whose `sprint` is `<id>` and that stands `actioned` stands under `vault/archive/`.
> **＋** Each lesson under `vault/wiki/lessons/` whose `sprint` is `<id>`, whose `kind` is `error` and that stands `new` stands under `vault/archive/`.
> **－** A lesson whose `kind` is `knowledge` stays under `vault/wiki/lessons/`.
> **－** An Insight that stands `open`, and each lesson its `children` lists, stay live.

```then
create:
- slug: estimate-sprint-close-archives-done-insights-and-lone-lessons
  type: estimate
  ref: rule-sprint-close
  kind: QA
  purpose: At the close of a sprint its actioned Insights and its error lessons that joined no Insight go to the archive, and its knowledge lessons and open Insights stay
  method: by hand, vault/wiki/insights/, vault/wiki/lessons/ and vault/archive/ read after the first close of a sprint
  tags:
  - sprint
  - workflow
```

```tasks
- [x] create `estimate-sprint-close-archives-done-insights-and-lone-lessons`
- [ ] read `estimate-sprint-close-archives-done-insights-and-lone-lessons`
```

### Case 612.3 — The close archives the sprint page with its own Estimates and keeps every other passed Estimate

> **given:**
> `rule-sprint-close` — the rule of the close
> **＋** `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest` — the promise on the sprint page and the passed Estimates
> **＋** `entity-sprint-<id>` — the sprint page that closes, with the Estimates it lists
> **＋** `entity-sprint` — the kind, whose Leaf the sprint page is
> **＋** `vault/wiki/entities/` and `vault/wiki/estimates/` — the Entity pages, and the Estimates, each with its `target`
> **＋** `vault/archive/` — where an archived page stands

> **when:**
> The close of the sprint `entity-sprint-<id>` runs: the Estimates that `entity-sprint-<id>` lists are read in it first, and its pages move once each of them stands `passed`; someone reads `vault/wiki/entities/`, `vault/wiki/estimates/` and `vault/archive/` after it.

> **then:**
> `entity-sprint-<id>` and each Estimate its `estimates` lists stand under `vault/archive/`.
> **－** Every other Estimate that stands `passed` stays under `vault/wiki/estimates/`, and the rule or Entity that lists it keeps it in `estimates`.
> **－** The close does not archive the MOC `entity-sprint`.

```then
create:
- slug: estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest
  type: estimate
  ref: rule-sprint-close
  kind: QA
  purpose: At the close of a sprint the sprint page and its own Estimates go to the archive, and every other passed Estimate stays live
  method: by hand, vault/wiki/entities/, vault/wiki/estimates/ and vault/archive/ read after the first close of a sprint
  tags:
  - sprint
  - workflow
```

```tasks
- [x] create `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest`
- [ ] read `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest`
```

### Case 612.4 — The close puts each Estimate not passed to the person before anything moves

> **given:**
> `rule-sprint-close` — the rule of the close
> **＋** `estimate-sprint-close-settles-unread-estimates` — the promise on the Estimates not passed
> **＋** `entity-sprint-<id>` — the sprint page that closes, with the Estimates it lists
> **＋** `vault/wiki/estimates/` — the Estimates, each with its status
> **＋** `vault/archive/` — where an archived page stands
> **＋** `estimate-sprint-migration-lint-clean` — the current sprint's clean-lint condition; unchanged

> **when:**
> The close of the sprint `entity-sprint-<id>` runs: the Estimates that `entity-sprint-<id>` lists are read in it first, and its pages move once each of them stands `passed`; someone reads the record of the close, `vault/wiki/estimates/` and `vault/archive/` after it.

> **then:**
> Before any page of the close moves, the close lists to the person each Estimate under `vault/wiki/estimates/` that stands `pending` or `failed`.
> **＋** For each listed Estimate the person chooses one way: read it now, carry it into the next sprint, or archive it unread.
> **＋** An Estimate read now has its reading in the ledger.
> **＋** An Estimate carried into the next sprint stays under `vault/wiki/estimates/` with its status.
> **＋** An Estimate archived unread stands under `vault/archive/`, and the page that listed it no longer lists it in `estimates`.
> **－** No page of the close moves before the person has chosen for each listed Estimate.

```then
create:
- slug: estimate-sprint-close-settles-unread-estimates
  type: estimate
  ref: rule-sprint-close
  kind: QA
  purpose: At the close of a sprint each pending or failed Estimate is put to the person, who has it read, carries it into the next sprint or archives it unread, before any page moves
  method: by hand, the record of the first close of a sprint, vault/wiki/estimates/ and vault/archive/ read after it
  tags:
  - sprint
  - workflow
```

```tasks
- [x] create `estimate-sprint-close-settles-unread-estimates`
- [ ] read `estimate-sprint-close-settles-unread-estimates`
```

## Case 613 — A check by hand names the kind of its moment, and `/hi` reads a past moment from its transcript

> **context:**
> Each Estimate has a `method` line that says how its promise is checked. Many checks by hand tie their reading to one moment, "the first X after the render": the first `/handoff`, the first `/retro`, the first `/work`. That moment passes once, and nobody reads it. Take `estimate-handoff-holds-each-fact-once`, read "at the first /handoff after the render". `/handoff` runs after Retro has written the session's readings, so no step of that session is left to read it. The next `/hi` takes only readings whose method names `/hi` or the librarian's run. The handoff of session 0115 then listed it as "moment not come". The moment is not lost. The event logs `vault/raw/<date>/event_log.md` name each session by its id and mark `hi`, `prespec`, `retro`, `handoff` and each `Skill` and `Agent` call. The transcript of that session holds the turn until Claude Code deletes it. `rule-work-mode` already says that a moment of an earlier session has come, but no step opens an old transcript. The main agent's diagnosis holds: the tests run at every session, and one reading covers a whole `method`.
>
> The person chose this. A method names the kind of its moment, and any such moment after the render counts, in this session or an earlier one (613.3). The word "first" stays only for an event that has never happened, such as the first close of a sprint in the methods of case 612. `/hi` reads each moment of an earlier session from the transcript of the latest session that held it, part by part (613.2). One predicate in `guppi/lint.py` finds a reading by hand tied to "the first ... after the render" or "the first ... after the change". `make lint` and `pre-spec` both use it (613.1). The waiting Estimates, and the passed ones in the old wording, get their `method` line rewritten. The person did not choose a bulk `passed`: a reading line with no reading behind it is a false record.
>
> These facts come from the searches:
> - A Grep of `^status: (pending|failed)` over `vault/wiki/estimates/` printed 38 files. 613.3 rewrites 27 of them, and 11 keep their method.
> - A Grep of `^method:.*\bfirst\b.*after the (render|change)` over `vault/wiki/estimates/` printed 21 files. Ten of them are waiting Estimates. Ten are passed Estimates, which 613.3 rewrites. The last is `estimate-hi-takes-its-readings`, which 613.2 rewrites.
> - 613.3 also rewrites 17 waiting Estimates that tie their reading to a one-off moment in other words, such as "the first /retro" or "the first compaction".
> - A Grep of `^method:.*\bfirst\b` over the same folder printed 64 files. A passed Estimate among them that does not match the pattern stays as it is.
>
> The 11 waiting Estimates that keep their method fall into two groups:
> - Eight name no one-off moment: `estimate-end-of-work-order`, `estimate-event-log-records`, `estimate-ask-finds`, `estimate-plan-mode-verified`, `estimate-case-build-writes-the-case`, `estimate-session-start-context`, `estimate-orchestration-shows-the-built-case` (case 611 has it read again) and `estimate-synthesis-clusters` (read `passed` at this session's `/hi`).
> - Three are the done-conditions of `entity-sprint-migration`, read at the close of the sprint (case 612). `estimate-sprint-migration-leftovers-gone` names the close of the sprint and `estimate-sprint-migration-merges` the merge to main. Both are one-off moments, but each belongs to that close and comes only once by design. `estimate-sprint-migration-lint-clean` names `make lint`. All three keep their method.
>
> This session changes the Estimates of 613.3, so none of them is read in this session. The ledger hook refuses such a reading, and they are read from the next session on.
>
> These texts and Estimates were checked against the frame:
> - The new finding is a class of its own, `moment`. So `estimate-lint-checks-the-method` keeps its Criterion: it speaks of the `method` finding of the forms.
> - `estimate-prespec-catches-a-method-without-a-form` keeps its Criterion: it speaks of the line "method names no form".
> - `estimate-lint-catches` lists other classes and stays as it is.
> - `estimate-estimates-schema-checked` speaks of the lists of `schema.yaml`, not of the prose of `method`, and stands.
> - Three lines of the old Criterion of `estimate-hi-takes-its-readings` are not carried into 613.2, on purpose. They are the line on which readings `/hi` takes, the line on where it reads them, and the line that a later moment waits. 613.2 replaces each of them.
> - The check of the answer notes that the `then` of 613.3 shares words with the `then` of 613.1 and 613.2. 613.3 rewrites the methods that 613.1 judges and that 613.2 reads, so they speak of the same thing.
> - Lint changes in Work Mode, but the rewritten pages land at the librarian's run. In between, `make lint` shows red on them. Work Mode marks this under `## Expected red` of `work.md`, and Retro makes it a note for the handoff. Lint only goes red, so the check keeps no old form.
> - A Grep of `` /hi`? (takes|reads)|readings? of `?/hi|at `?/hi`? .{0,30}reading `` over the repository outside `vault/wiki/decisions/`, `vault/archive/` and `vault/raw/` printed 11 files. They are `glossary.md`, `librarian-guppi.md`, `carry/SKILL.md`, `log.md`, `entity-glossary.md`, `rule-skill-hi.md`, `estimate-carry-over-writes.md`, `rule-carry-over.md`, `rule-brief.md`, `estimate-hi-takes-its-readings.md` and `lesson-carry-short-brief-drops-the-work-list.md`. `log.md` was not read. The others outside this Case speak of where `/hi` takes its Work list, or of the sprint, and stay true.
> - A Grep of `first reply|previous session|transcript of` over `vault/wiki/rules/` printed seven files. They are `schema.yaml`, `rule-internal-context.md`, `rule-orchestration.md`, `rule-retro-onward.md`, `rule-rules-schema.md`, `rule-skill-hi.md` and `rule-case-protocol.md`. `rule-orchestration` defers the form of the first reply of `/hi` to `rule-skill-hi`. The other hits speak of the handover, of a refusal and of History, and stand.
> - The Work readings of `rule-work-mode` take what `/hi` leaves, and do not change.
> - Cases 611 and 612 change no page of this Case and set nothing at `/hi`.
> - The Case makes no `create` without a `ref`. A Glob of `vault/**/estimate-lint-reports*` printed no file, so the new slug is free.
>
> Not done: an Estimate whose event is rare still waits for it, and the close of a sprint settles it (case 612.4). An Estimate that pairs tests with a check by hand keeps one reading. The 11 waiting Estimates named above keep their method.

> **problem:**
> A check by hand is tied to one moment that passes unread, and no step reads it afterwards, so its Estimate waits for good. The question was how a method names its moment, which step reads a moment that came after its session's readings, how the old wording is caught, and what happens to the Estimates that wait today.

> **recommend:**
> - **How should a check by hand name its moment?**
>   - Recommended: (a) any such moment counts; the method names the kind of moment, and "the first" stays only for an event that has never happened.
>   - Answer: agreed with the recommendation, (a).
> - **Which step reads a moment that comes after its session's readings are written?**
>   - Recommended: (a) the next `/hi` reads it from the previous session's transcript.
>   - Answer: agreed with the recommendation, (a).
> - **What happens to the Estimates that wait today?**
>   - Recommended: (a) this Case rewrites their methods; they are read from the next session on.
>   - Answer: agreed with the recommendation, (a).
> - **What happens to an Estimate whose event is rare or has not happened yet?**
>   - Recommended: (a) it waits for the event, and the close of the sprint settles the rest.
>   - Answer: agreed with the recommendation, (a).
> - **What happens to an Estimate that pairs tests with a check by hand?**
>   - Recommended: (a) keep both parts in one reading.
>   - Answer: agreed with the recommendation, (a).
> - **What happens when a method names more than one moment?**
>   - Recommended: (a) `/hi` reads each part from the session where its moment came.
>   - Answer: agreed with the recommendation, (a).
> - **How is the new form of a method checked?**
>   - Recommended: (a) one pattern in `guppi/lint.py`, used by `pre-spec` and `make lint`, finds a method that ties its check by hand to "the first ... after the render"; a new Estimate read by tests.
>   - Answer: agreed with the recommendation, (a).
> - **What happens to the Estimates that already passed but whose method uses the old wording?**
>   - Recommended: (a) this Case rewrites their methods too; promise and status stand.
>   - Answer: agreed, (a).
> - **Does the pattern also catch "after the change"?**
>   - Recommended: (a) yes, both "after the render" and "after the change".
>   - Answer: agreed, (a).

### Case 613.1 — Lint and pre-spec report a check by hand tied to the first moment after the render or the change

> **given:**
> `guppi/lint.py` and `tests/test_lint.py` — lint, which gains the class `moment` and its predicate, and its tests
> **＋** `guppi/prespec.py` and `tests/test_prespec.py` — pre-spec, which imports the predicate, and its tests
> **＋** `rule-lint` — the rule of lint; its classes live in the docstring of `guppi/lint.py`
> **＋** `rule-prespec` — the rule of pre-spec; its checks live in the docstring of `guppi/prespec.py`
> **＋** `rule-estimates-schema` and `vault/wiki/estimates/schema.yaml` — the `method` field and its render, which gain the form of a moment
> **＋** `vault/wiki/estimates/` — the Estimate pages lint reads
> **＋** the plan file of Plan Mode — the `then` blocks pre-spec reads
> **＋** `estimate-lint-reports-a-method-tied-to-a-one-off-moment` — the new promise

> **when:**
> `uv run guppi lint` reads the `method` field of each live Estimate under `vault/wiki/estimates/`.
> **＋** Or `uv run guppi prespec --check <plan> --session <id>` reads the `method` of a `create` of an Estimate, or of an `update` that carries `set: {method: …}`, in the `then` blocks of the plan file.

> **then:**
> A `method` that holds `by hand` and names the first of something after the render or after the change, with no `;` between the two, is one lint finding of the class `moment`.
> **＋** The same `method` in the plan gives one line `case N: <create|update> <slug>: method ties its reading by hand to the first moment after the render or the change`, which goes on to say that the method names the kind of its moment.
> **＋** Both sides judge by one predicate in `guppi/lint.py`, which `guppi/prespec.py` imports.
> **－** A `method` that names the kind of its moment, with no word "first", gets no such finding.
> **－** A `method` that names the first of an event without "after the render" or "after the change", such as the first close of a sprint, gets no such finding.
> **－** A `method` without `by hand` gets no such finding.
> **－** The finding does not replace the `method` finding of a `method` that names no form.

```then
create:
- slug: estimate-lint-reports-a-method-tied-to-a-one-off-moment
  type: estimate
  ref: rule-lint
  kind: QA
  purpose: Whether lint and pre-spec report a method that ties its reading by hand to the first moment after the render or after the change, by one predicate, and leave a method that names the kind of its moment
  method: uv run pytest tests/test_lint.py tests/test_prespec.py -k moment; the make lint of a later session, no moment finding on wiki/estimates/
  tags:
  - harness
  - workflow
update:
- slug: rule-estimates-schema
  replace:
  - old: with where and when it is taken, a session start, the brief of a librarian's run.
    new: with where and when it is taken, a session start, the brief of a librarian's run. A reading names its moment by its kind — a `/handoff`, a run of `/box`, a compaction — and any such moment after the render counts, in this session or in an earlier one; the word "first" stands only for an event that has never happened. A reading by hand tied to the first of something after the render or after the change is a finding of the class `moment` of lint and a finding of pre-spec, judged by one predicate of `guppi/lint.py` (case 613.1).
  change: a reading names its moment by its kind; a reading by hand tied to the first moment after the render or the change is a finding of lint and pre-spec (case 613.1)
```

```tasks
- [x] `guppi/lint.py`: one predicate of a reading by hand tied to the first moment after the render or the change; the class `moment` in the checks of an Estimate; the module docstring names the class
- [x] `guppi/prespec.py`: imports the predicate and gives the finding line on a `create` or a `set` of `method`; the module docstring names the check
- [x] `tests/test_lint.py` and `tests/test_prespec.py`: tests named `moment` for each wording, "after the render" and "after the change", a kind of moment, the first of an event with no "after", a method without `by hand`, and two clauses split by `;`
- [x] update `rule-estimates-schema`
- [x] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`
- [x] create `estimate-lint-reports-a-method-tied-to-a-one-off-moment`
- [ ] read `estimate-lint-reports-a-method-tied-to-a-one-off-moment`
```

### Case 613.2 — `/hi` reads a moment of an earlier session from the transcript of the session that held it

> **given:**
> `rule-skill-hi` and `.claude/skills/hi/SKILL.md` — the rule of `/hi` and its render, whose reading step changes
> **＋** `estimate-hi-takes-its-readings` — the promise of the reading step, replaced
> **＋** `vault/wiki/brief.md` — the brief whose readings `/hi` takes
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier whose `W` and `A` lines the step closes
> **＋** `vault/raw/<date>/event_log.md` — the event logs, which name each session by the first characters of its id
> **＋** the transcripts of Claude Code — one file per session, its name opening with the session's id
> **＋** `rule-work-mode` — the Work readings, which take what `/hi` leaves; unchanged

> **when:**
> The person types `/hi` on `UserPromptSubmit`, and the agent writes `raw/<date>/<hi HHMM>/frontier.md`, whose `## Work` holds the `pending` readings of `vault/wiki/brief.md` and whose `## Ask` holds its readings that only the person can take.

> **then:**
> In its first reply, before the question on the order, the agent takes each reading of an open `W` line whose every moment, as its `method` names it, is this `/hi` or has come in an earlier session.
> **＋** It reads what the method names from `vault/wiki/brief.md`, `git log`, `git status` and the commands of the method.
> **＋** It reads each moment of an earlier session from the transcript of the latest session that held it, found by the session ids of `vault/raw/<date>/event_log.md`, and each part of the method from the session where its moment came.
> **＋** It opens the page of each Estimate it reads and judges the reading against its `## Criterion`.
> **＋** It closes the `W` line of each reading taken as `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`, then writes one `estimate[...]` line per reading in a `LEDGER` block of the reply, which ends in text.
> **＋** In the same reply, before the question on the order, it puts each open `A` line to the person as a question: the Estimate by slug and its question.
> **＋** When the person answers one, the agent closes its `A` line `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md` first, then writes its `estimate[...]` line, the answer as its result, in a `LEDGER` block of the reply, which ends in text.
> **－** The Frontier is still assembled with no page opened. Only the reading step opens the pages of the Estimates it reads.
> **－** A reading with a moment that has come in no session yet, or whose transcript Claude Code no longer holds, is not taken, and its `W` line stays open.
> **－** A reading whose `method` asks for a `/hi` run of its own, such as one outside plan mode, is not taken at `/hi`.
> **－** At `/hi` the agent changes no page and no file except `raw/<date>/<hi HHMM>/frontier.md`.

```then
update:
- slug: rule-skill-hi
  replace:
  - old: 'take each reading of an open `W` line whose `method` names the `/hi` of a session or the librarian''s run and whose whole method can be done now: from the brief, `git log`, `git status`, the commands the method names, and the transcript of the previous session for the librarian''s report.'
    new: 'take each reading of an open `W` line whose whole method can be done now: each moment its `method` names is this `/hi` or has come in an earlier session (case 613.2). Read what the method names from the brief, `git log`, `git status` and the commands the method names, and each moment of an earlier session — the librarian''s run, `/retro`, `/handoff` or any other — from the transcript of the latest session that held it: the event logs `vault/raw/<date>/event_log.md` name each session by the first characters of its id, and its transcript is the file of Claude Code whose name opens with that id; read each part of the method from the session where its moment came.'
  - old: A reading whose `method` also names a later moment waits for that moment, its `/hi` part read then from the session's first turn; a reading whose `method` asks for a `/hi` run of its own is not taken here (case 508.1).
    new: A reading with a moment that has come in no session yet, or whose transcript Claude Code no longer holds, waits for its next moment, and its line stays open; a reading whose `method` asks for a `/hi` run of its own is not taken here (cases 508.1, 613.2).
  change: /hi reads each moment of an earlier session from the transcript of the latest session that held it, part by part (case 613.2)
- slug: estimate-hi-takes-its-readings
  set:
    status: pending
    purpose: Whether /hi takes, in its first reply, each open W reading whose every moment is that /hi or came in an earlier session, reads each moment of an earlier session from the transcript of the latest session that held it, puts each open Ask line to the person as a question and writes the answer as its reading line, closes each line it ends, opens no page but the Estimates it reads, and leaves a reading with a moment not come, a transcript gone or a /hi run of its own
    method: 'by hand at a /hi of a later session whose open W lines hold a reading whose moment came in an earlier session: the first reply, its tool calls, its LEDGER block and frontier.md read against the Criterion, recorded in the estimate line'
  change: the Criterion replaced whole — /hi reads a moment of an earlier session from its transcript (case 613.2)
```

```tasks
- [x] update `rule-skill-hi`
- [x] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [x] update `estimate-hi-takes-its-readings`
- [ ] read `estimate-hi-takes-its-readings`
```

### Case 613.3 — The methods that tie a reading to a one-off moment name its kind

> **given:**
> `rule-estimates-schema` — the form of a `method`, which 613.1 sets
> **＋** `estimate-generate-rewords` — waiting; its `method` rewritten
> **＋** `estimate-case-check-sends-back-a-ratified-case-in-another-shape` — waiting; its `method` rewritten
> **＋** `estimate-hi-takes-a-conserved-spec` — waiting; its `method` rewritten
> **＋** `estimate-handoff-dispatches` — waiting; its `method` rewritten
> **＋** `estimate-case-check-requires-each-question-of-the-rounds` — waiting; its `method` rewritten
> **＋** `estimate-lint-runs-every-step` — waiting; its `method` rewritten
> **＋** `estimate-ledger-write-lifts` — waiting; its `method` rewritten
> **＋** `estimate-compact-recall-reloads` — waiting; its `method` rewritten
> **＋** `estimate-prespec-onward-sends-the-agent-on` — waiting; its `method` rewritten
> **＋** `estimate-case-check-sends-back-a-faulty-round` — waiting; its `method` rewritten
> **＋** `estimate-case-check-sends-back-a-faulty-case` — waiting; its `method` rewritten
> **＋** `estimate-carry-over-writes` — waiting; its `method` rewritten
> **＋** `estimate-case-check-sends-back-a-case-number-held-by-another-agent` — waiting; its `method` rewritten
> **＋** `estimate-ratification-ledger-line-form` — waiting; its `method` rewritten
> **＋** `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — waiting; its `method` rewritten
> **＋** `estimate-spec-write-reaches-the-approved-spec` — waiting; its `method` rewritten
> **＋** `estimate-spec-box-runs-a-conserved-spec` — waiting; its `method` rewritten
> **＋** `estimate-retro-onward-sends-the-agent-to-the-handoff` — waiting; its `method` rewritten
> **＋** `estimate-retro-loads` — waiting; its `method` rewritten
> **＋** `estimate-orchestration-defers-in-one-reply` — waiting; its `method` rewritten
> **＋** `estimate-retro-runs-on-to-the-handoff` — waiting; its `method` rewritten
> **＋** `estimate-orchestration-signs-a-batch-together` — waiting; its `method` rewritten
> **＋** `estimate-spec-capture-offers-the-fork` — waiting; its `method` rewritten
> **＋** `estimate-work-mode-takes-the-work-readings` — waiting; its `method` rewritten
> **＋** `estimate-where-to-stop-stops-only-on-its-conditions` — waiting; its `method` rewritten
> **＋** `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — waiting; its `method` rewritten
> **＋** `estimate-handoff-holds-each-fact-once` — waiting; its `method` rewritten
> **＋** `estimate-prespec-onward-reads-the-decisions-of-the-session` — passed; its `method` rewritten
> **＋** `estimate-ratification-loaded` — passed; its `method` rewritten
> **＋** `estimate-orchestration-loaded` — passed; its `method` rewritten
> **＋** `estimate-spec-write-writes-a-defer` — passed; its `method` rewritten
> **＋** `estimate-prespec-reconciles` — passed; its `method` rewritten
> **＋** `estimate-retro-red-in-the-baseline-is-not-charged` — passed; its `method` rewritten
> **＋** `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — passed; its `method` rewritten
> **＋** `estimate-harness-make-runs-in-both-shells` — passed; its `method` rewritten
> **＋** `estimate-spec-write-removes-a-superseded-case` — passed; its `method` rewritten
> **＋** `estimate-spec-write-checks-the-written-case` — passed; its `method` rewritten

> **when:**
> Someone reads the `method` of an Estimate that this sub-case rewrites, to know at which moment its reading is taken.

> **then:**
> The `method` names the kind of its moment, and any such moment after the render, in this session or an earlier one, is its moment.
> **＋** The `## Criterion` and the `status` of each Estimate stand.
> **－** No `method` of them ties a reading by hand to the first of something after the render or after the change.

```then
update:
- slug: estimate-generate-rewords
  set:
    method: pytest tests/test_generate.py on a temp vault with three pages and an archive; the live reading a librarian's run that applies a reword
  change: method names the kind of its moment (case 613.3)
- slug: estimate-case-check-sends-back-a-ratified-case-in-another-shape
  set:
    method: uv run pytest tests/test_casecheck.py -k shape, then by hand an answer of case-guppi the hook sends back for this reason
  change: method names the kind of its moment (case 613.3)
- slug: estimate-hi-takes-a-conserved-spec
  set:
    method: 'uv run guppi render --check; by hand, a session whose person takes a conserved Spec at the Frontier: frontier.md, the title line of the plan file and the session''s ledger read against the Criterion'
  change: method names the kind of its moment (case 613.3)
- slug: estimate-handoff-dispatches
  set:
    method: 'by hand at the /handoff of a later session and at the /handoff of a session that /box runs: the event log, handoff.md, the dispatch line and git log'
  change: method names the kind of its moment (case 613.3)
- slug: estimate-case-check-requires-each-question-of-the-rounds
  set:
    method: 'pytest tests/test_casecheck.py -k rounds over a temp agent transcript: a round and a Case whose recommend holds every title, one that misses a title, a title asked in two rounds, a round out of form whose titles are not required, an answer with no round; then by hand a Case the hook sends back for a missing title'
  change: method names the kind of its moment (case 613.3)
- slug: estimate-lint-runs-every-step
  set:
    method: 'by hand, the make lint of the Baseline of a /work of a later session whose backlog step is red: the steps that printed, the page findings of guppi lint and the exit code, recorded in the estimate line'
  change: method names the kind of its moment (case 613.3)
- slug: estimate-ledger-write-lifts
  set:
    method: 'pytest in tests/test_ledger.py and tests/test_gate.py with piped payloads against a temp vault; by hand once, the ledger of a session whose reply that ends Retro follows a refusal of a Stop hook in the same stretch: its lines written at that Stop, with its time'
  change: method names the kind of its moment (case 613.3)
- slug: estimate-compact-recall-reloads
  set:
    method: pytest tests/test_recall.py on a temp project; live — a compaction of a working session, by hand, the hook's text in the context after it
  change: method names the kind of its moment (case 613.3)
- slug: estimate-prespec-onward-sends-the-agent-on
  set:
    method: 'uv run pytest tests/test_onward.py tests/test_ledger.py; by hand at a Plan Mode at which the ledger hook refuses a line of the reply that acknowledges the last ratification: the transcript, the event log and frontier.md, recorded in the estimate line'
  change: method names the kind of its moment (case 613.3)
- slug: estimate-case-check-sends-back-a-faulty-round
  set:
    method: 'uv run pytest tests/test_casecheck.py -k round_form over a temp agent transcript: a round in form, a title line without the colon, a question with no Now line, no lone Options label, no option with an After item and no arrow line, the same faulty round given twice, a Fact answer, an answer with a Case, an unreadable transcript; then by hand a round the hook sends back live, its stderr and the round case-guppi gave again'
  change: method names the kind of its moment (case 613.3)
- slug: estimate-case-check-sends-back-a-faulty-case
  set:
    method: uv run pytest tests/test_casecheck.py -k subagent, then by hand an answer of case-guppi the hook sends back, a file of cases/ it writes, and a live round after a built Case, which is not sent back for that Case and leaves its stored entry and its file as they stood
  change: method names the kind of its moment (case 613.3)
- slug: estimate-carry-over-writes
  set:
    method: uv run guppi render --check; by hand, a /carry after the fork of ExitPlanMode — the tree, vault/wiki/brief.md, carry.md, vault/wiki/backlog.md, the commit and git branch read
  change: method names the kind of its moment (case 613.3)
- slug: estimate-case-check-sends-back-a-case-number-held-by-another-agent
  set:
    method: uv run pytest tests/test_casecheck.py -k clash, then by hand an answer of case-guppi the hook sends back for this reason
  change: method names the kind of its moment (case 613.3)
- slug: estimate-ratification-ledger-line-form
  set:
    method: 'by hand: the ledger and the preview of a session where a lesson and the Case that closes its cause stand together, and of a Case that takes up a decision with more than one Case in its deferred_by'
  change: method names the kind of its moment (case 613.3)
- slug: estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline
  set:
    method: 'uv run guppi render --check; by hand, a /work the agent calls at the fork, a /work the person types and a /work that /box calls: the branch, work.md, the ticks of the Spec, the carry.md of the folder and each Expected red line read against the Criterion, and, where a substitution came back empty, the agent''s own run of its command, recorded in the estimate line'
  change: method names the kind of its moment (case 613.3)
- slug: estimate-spec-write-reaches-the-approved-spec
  set:
    method: uv run pytest tests/test_ratified.py -k approved_spec; by hand, a Case ratified in Work Mode
  change: method names the kind of its moment (case 613.3)
- slug: estimate-spec-box-runs-a-conserved-spec
  set:
    method: 'uv run guppi render --check; by hand, a session that takes a conserved Spec at the Frontier and runs it by /box: git log, the branches, the folders of the session and of the conserved Spec, the dispatch line and the librarian''s commit, recorded in the estimate line'
  change: method names the kind of its moment (case 613.3)
- slug: estimate-retro-onward-sends-the-agent-to-the-handoff
  set:
    method: 'uv run pytest tests/test_onward.py tests/test_ledger.py; by hand at an end of Retro at which the ledger hook refuses a line: the transcript, the event log and handoff.md, recorded in the estimate line'
  change: method names the kind of its moment (case 613.3)
- slug: estimate-retro-loads
  set:
    method: by hand at a /retro, and at a /retro of a session that /box runs, recorded in the estimate line
  change: method names the kind of its moment (case 613.3)
- slug: estimate-orchestration-defers-in-one-reply
  set:
    method: by hand, a decision the person asks to put off, its line of frontier.md closed [-] … · defer case N, in a reply that leaves no line under the Cases heading of frontier.md open; a sprint item put off or a backlog item kept is not this reading
  change: method names the kind of its moment (case 613.3)
- slug: estimate-retro-runs-on-to-the-handoff
  set:
    method: 'by hand at a run from /work to the librarian, and for the answer to a refusal of the ledger hook at a Retro where that hook refuses a line: the replies of the turn, the ledger, git log and handoff.md read against the Criterion, recorded in the estimate line'
  change: method names the kind of its moment (case 613.3)
- slug: estimate-orchestration-signs-a-batch-together
  set:
    method: 'by hand at a Plan Mode of a later session in which the person''s word asks that a ratified Case change: the SendMessage calls and the replies from that word to the acknowledging reply, read in the transcript'
  change: method names the kind of its moment (case 613.3)
- slug: estimate-spec-capture-offers-the-fork
  set:
    method: uv run pytest tests/test_spec.py -k 'fork or box'; by hand, an ExitPlanMode of a session, and an ExitPlanMode of a session that took a conserved Spec
  change: method names the kind of its moment (case 613.3)
- slug: estimate-work-mode-takes-the-work-readings
  set:
    method: 'by hand at a /work and at a /work that /box calls: the replies after the last task, their LEDGER blocks and frontier.md read against the Criterion, recorded in the estimate line'
  change: method names the kind of its moment (case 613.3)
- slug: estimate-where-to-stop-stops-only-on-its-conditions
  set:
    method: 'by hand at a run from /work to the librarian, and at a run of /box: the context of /work and of /box, the replies of the turn and the Spec read against the Criterion, recorded in the estimate line; a condition that does not arise is named as not exercised'
  change: method names the kind of its moment (case 613.3)
- slug: estimate-retro-red-check-of-an-updated-page-is-a-handoff-note
  set:
    method: one reading by hand at a /retro in a session whose work.md names a check under Expected red, recorded in the estimate line
  change: method names the kind of its moment (case 613.3)
- slug: estimate-handoff-holds-each-fact-once
  set:
    method: one reading by hand at a /handoff, against the close of its Retro, recorded in the estimate line
  change: method names the kind of its moment (case 613.3)
- slug: estimate-prespec-onward-reads-the-decisions-of-the-session
  set:
    method: 'uv run pytest tests/test_onward.py; by hand at a Case ratified again with unchanged decision lines in Plan Mode, at the reply that closes the last line under Cases after a later message of the person: the transcript, ledger.md and the times of the files under cases/, recorded in the estimate line'
  change: method names the kind of its moment (case 613.3)
- slug: estimate-ratification-loaded
  set:
    method: uv run guppi render --check; by hand at a /hi of a later session, vault/wiki/ratification.md in the first turn's context and its paragraphs compared with CLAUDE.md, case-schema.md and orchestration.md
  change: method names the kind of its moment (case 613.3)
- slug: estimate-orchestration-loaded
  set:
    method: uv run guppi render --check; by hand at a /hi of a later session, vault/wiki/orchestration.md in the first turn's context and its paragraphs compared with CLAUDE.md, case-schema.md and ratification.md
  change: method names the kind of its moment (case 613.3)
- slug: estimate-spec-write-writes-a-defer
  set:
    method: uv run pytest tests/test_ratified.py -k defer, then by hand a defer the person asks for
  change: method names the kind of its moment (case 613.3)
- slug: estimate-prespec-reconciles
  set:
    method: One reading by hand of a /pre-spec, written into the estimate line — the exception the Method rule allows
  change: method names the kind of its moment (case 613.3)
- slug: estimate-retro-red-in-the-baseline-is-not-charged
  set:
    method: one reading by hand at a /retro in a session whose work.md Baseline holds a failing test or a lint finding line, recorded in the estimate line
  change: method names the kind of its moment (case 613.3)
- slug: estimate-case-build-keeps-the-old-form-until-the-writer-is-live
  set:
    method: one reading by hand at a Case case-guppi builds that changes a reader and the text or writer it reads, recorded in the estimate line
  change: method names the kind of its moment (case 613.3)
- slug: estimate-harness-make-runs-in-both-shells
  set:
    method: by hand, make help, make style, make test and make lint from PowerShell and from Git Bash on Windows, in a session
  change: method names the kind of its moment (case 613.3)
- slug: estimate-spec-write-removes-a-superseded-case
  set:
    method: uv run pytest tests/test_ratified.py -k superseded; by hand, a supersedes of a Case of the same session
  change: method names the kind of its moment (case 613.3)
- slug: estimate-spec-write-checks-the-written-case
  set:
    method: uv run pytest tests/test_ratified.py -k checks_the_written; by hand, a ratification of a session
  change: method names the kind of its moment (case 613.3)
```

```tasks
- [x] update `estimate-generate-rewords`
- [x] update `estimate-case-check-sends-back-a-ratified-case-in-another-shape`
- [x] update `estimate-hi-takes-a-conserved-spec`
- [x] update `estimate-handoff-dispatches`
- [x] update `estimate-case-check-requires-each-question-of-the-rounds`
- [x] update `estimate-lint-runs-every-step`
- [x] update `estimate-ledger-write-lifts`
- [x] update `estimate-compact-recall-reloads`
- [x] update `estimate-prespec-onward-sends-the-agent-on`
- [x] update `estimate-case-check-sends-back-a-faulty-round`
- [x] update `estimate-case-check-sends-back-a-faulty-case`
- [x] update `estimate-carry-over-writes`
- [x] update `estimate-case-check-sends-back-a-case-number-held-by-another-agent`
- [x] update `estimate-ratification-ledger-line-form`
- [x] update `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
- [x] update `estimate-spec-write-reaches-the-approved-spec`
- [x] update `estimate-spec-box-runs-a-conserved-spec`
- [x] update `estimate-retro-onward-sends-the-agent-to-the-handoff`
- [x] update `estimate-retro-loads`
- [x] update `estimate-orchestration-defers-in-one-reply`
- [x] update `estimate-retro-runs-on-to-the-handoff`
- [x] update `estimate-orchestration-signs-a-batch-together`
- [x] update `estimate-spec-capture-offers-the-fork`
- [x] update `estimate-work-mode-takes-the-work-readings`
- [x] update `estimate-where-to-stop-stops-only-on-its-conditions`
- [x] update `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`
- [x] update `estimate-handoff-holds-each-fact-once`
- [x] update `estimate-prespec-onward-reads-the-decisions-of-the-session`
- [x] update `estimate-ratification-loaded`
- [x] update `estimate-orchestration-loaded`
- [x] update `estimate-spec-write-writes-a-defer`
- [x] update `estimate-prespec-reconciles`
- [x] update `estimate-retro-red-in-the-baseline-is-not-charged`
- [x] update `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`
- [x] update `estimate-harness-make-runs-in-both-shells`
- [x] update `estimate-spec-write-removes-a-superseded-case`
- [x] update `estimate-spec-write-checks-the-written-case`
```
