<!-- approved 02:35:04 · session b76bfabb -->

# Spec — session 0112, 2026-10-04

## Case 624 — The handoff says each thing once and lists the readings that wait in Debt alone

> **context:**
> `/handoff` writes `handoff.md`, the report of Retro, in seven sections. Its skill says that a fact stands in one section only: a Case, a box, a reading, a lesson or an observation named in one section is not named in another. `estimate-handoff-holds-each-fact-once` holds the same rule as a `－` line of its Criterion. The check failed at the `/hi` of session 1341 on the handoff of session 0317, which names Case 613.3 in four sections. Cases 618 and 621 put the check off. The handoff of session 0004 breaks the rule too. Its Direct instructions to the librarian list every reading that waits, with its moment. Its Debt names `estimate-hi-takes-a-conserved-spec` and `estimate-prespec-checks-the-frontier` again in its line of `read` slugs. Its notes name readings and lessons that What actually got done lists by line. So the failure comes from how the skill is written, not from one old session. Part of the cause is in the rules. A note on a decision must name the decision, and What actually got done lists every decision. `rule-retro` says that `handoff.md` names every Estimate whose reading cannot be taken yet, and every Estimate the session creates or updates, but it names no section for them. The skill has a Debt line only for the second group.
>
> The person chose three things. The rule now reads: one statement once. A Case, box, reading, lesson or observation may stand in a second section only with what that section's kind adds about it. The readings that wait stand in Debt alone, each with its moment, and the Direct instructions list none of them. The new Criterion is measured on a handoff that the skill wrote after its new text was rendered. This session's handoff is written before the librarian renders the skill, so it does not count. The `When` names the skill as rendered from `rule-handoff`, and the `method` names that report. Three sentences of the Render of `rule-handoff` change. The Purpose still says one section for each kind of content, and that stays true. The Criterion of `estimate-handoff-holds-each-fact-once` is replaced whole. Its `purpose` stated the old promise, and its `method` named no report, so both are set anew. The section names and their order stay. So `estimate-handoff-dispatches`, which reads "the sections that `rule-handoff` names", keeps its Criterion. The handoff of session 0004 would still fail the new Criterion where it says the same thing twice: its notes say that a reading waits for a moment, and its instructions list that reading under the same moment.
>
> `rule-retro` says that a `read` line whose slug the session creates or updates waits for a later session and is neither debt nor the librarian's. The old skill already put the slugs of those lines under `## Debt`, and this Case widens that line. To keep the two texts in line, the skill text and the Criterion now say that the lines of waiting readings stand in the section `## Debt` but are not debt. So the sentence of `rule-retro` stays true and its text does not change. `estimate-retro-loads`, on `rule-retro`, says that an Estimate this session creates or updates gets no reading in this session, and that the handoff names it as a reading of a later session. This Case keeps that: the handoff still names each such Estimate, now in `## Debt` with its moment. Its Criterion does not say in which section, so it stands, and this Case does not name it for an update.
>
> The check of this answer noted that four lines of the old Criterion are not carried. That is on purpose, and new lines replace each of them:
> - The old `When` gains the skill as rendered from `rule-handoff`.
> - The old line on the notes and the instructions gains the words that the instructions list no reading that waits.
> - The old Debt line now lists, in place of the `read` slugs, every Estimate whose reading cannot be taken yet, with its moment, and says that these lines are not debt.
> - The old `－` line on two sections becomes the rule of one statement once.
>
> Every other line is carried word for word.
>
> This Case closes the failed reading put off by Cases 618 and 621. It carries no `{supersedes:case N}`. The front matter of `estimate-handoff-holds-each-fact-once` holds no `deferred_by` field, and its History holds the two lines `deferred · [[decision-case-618]]` and `deferred · [[decision-case-621]]`. The schema asks for one block per Case in a page's `deferred_by`, and here there is none. The Case creates no page, so the vault query was not run.
>
> Frame checks:
> - A Grep of `rule-handoff|estimate-handoff-holds-each-fact-once` over the repository outside `vault/raw/`, `vault/archive/` and `vault/wiki/decisions/` printed 13 files: `glossary.md`, `entity-glossary.md`, `log.md`, `brief.md`, `insight-session-frontier-no-closer-for-an-item-ended-outside-the-plan.md`, `estimate-end-of-work-order.md`, `estimate-handoff-holds-each-fact-once.md`, `estimate-handoff-dispatches.md`, `estimate-hi-takes-a-conserved-spec.md`, `estimate-retro-runs-on-to-the-handoff.md`, `entity-sprint-migration.md`, `rule-end-of-work.md` and `rule-handoff.md`. The hits in `log.md`, `brief.md`, `entity-sprint-migration.md` and `estimate-retro-runs-on-to-the-handoff.md` stand in History or log lines and were not read. The rest name the rule as the gate of the handoff, a child of the end of work, the sections it sets, or a past result, and each stays true.
> - The moment this Case sets is the writing of `handoff.md`. A Grep of the seven section names over the repository outside `vault/raw/` and `vault/archive/` printed the skills `handoff`, `retro`, `carry` and `hi`, `librarian-guppi.md`, `guppi/spec.py`, `orchestration.md`, `brief.md`, `log.md`, the rules `rule-handoff`, `rule-retro`, `rule-brief`, `rule-carry-over`, `rule-skill-hi` and `rule-orchestration`, the Estimates `estimate-handoff-holds-each-fact-once`, `estimate-brief-written`, `estimate-carry-over-writes`, `estimate-hi-writes-frontier`, `estimate-orchestration-defers-in-one-reply`, `estimate-retro-runs-on-to-the-handoff`, `estimate-retro-red-in-the-baseline-is-not-charged`, `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` and `estimate-spec-capture-offers-the-fork`, and the Decision pages of cases 168, 468.1 and 468.2, which were not read. Only `rule-handoff` and its Estimate set what Debt and the Direct instructions hold. `rule-retro` puts a patch in Debt and sends lines to Observations, For the next session and Ask the person, and its Estimates say the same. `rule-brief` and the `librarian-guppi` frame read What actually got done, For the next session and Ask the person by name, and they read no list of waiting readings from the handoff: Readings due come from the pages and the Specs. `estimate-spec-capture-offers-the-fork` and `guppi/spec.py` match only the words "Ask the person" in another sense. No hit is made false.
> - A Grep of `later session` over `estimate-retro-loads.md` printed lines 21, 22 and 28. Lines 21 and 22 are the lines treated above, and line 28 was not read. A Grep of `debt` over the same file printed only line 48, a History line.

> **problem:**
> The `/handoff` skill forbids naming any Case, reading or lesson in two sections. A note on a decision must name it, and nothing says where the readings that wait belong. So every handoff the check has read repeats things, and `estimate-handoff-holds-each-fact-once` stays failed.

> **recommend:**
> - **What "each fact once" means**
>   - Recommended: (b) one statement once: a section may name a Case, check or lesson that another section names, when it says something new about it; saying the same thing about it twice is the failure; the skill text and the check's pass condition are both rewritten to say this.
>   - Answer: agreed with the recommendation, (b).
> - **Where the checks that wait for a later session are listed**
>   - Recommended: (a) Debt only: the Debt line is widened to every check that cannot be measured yet, each with the moment it waits for; the instructions to the librarian list no checks.
>   - Answer: agreed with the recommendation, (a).
> - **Which report the new check is measured on**
>   - Recommended: (b) the first report written from the new text: a report of a later session, written after the new skill text takes effect.
>   - Answer: agreed with the recommendation, (b).

> **given:**
> `rule-handoff` — its Render is the text of the `/handoff` skill; three sentences of it change
> **＋** `.claude/skills/handoff/SKILL.md` — the skill rendered from `rule-handoff`
> **＋** `raw/<date>/<hi HHMM>/handoff.md` — the report of Retro that the skill writes
> **＋** `estimate-handoff-holds-each-fact-once` — the check whose Criterion is replaced whole and whose `purpose` and `method` are set anew
> **＋** `rule-retro` — says that the report names every Estimate whose reading cannot be taken yet, and which boxes are debt; unchanged
> **＋** `rule-brief` — reads `## What actually got done` of the report by name; unchanged

> **when:**
> The agent calls `/handoff` on `PreToolUse Skill` after the reply that ends Retro, or the person types `/handoff` on `UserPromptSubmit`, on a clean tree, and the agent runs `.claude/skills/handoff/SKILL.md` as rendered from `rule-handoff` and writes `raw/<date>/<hi HHMM>/handoff.md`.

> **then:**
> `raw/<date>/<hi HHMM>/handoff.md` is the report of Retro: under `# Handoff — <date>, <slice or topic>` it holds, in order, `## Notes from memory`, `## Direct instructions to the librarian`, `## What actually got done`, `## Debt`, `## Observations`, `## For the next session` and `## Ask the person`.
> **＋** `## Notes from memory` holds only where the person hesitated, what stayed unclear and which decisions carried caveats. `## Direct instructions to the librarian` holds only what to check first and what may duplicate what, and lists no reading that waits.
> **＋** `## What actually got done` holds the ids of the Cases ratified, the code files and tests changed, the result of `make test` and `make style`, and the readings and lessons written, by their ledger line numbers.
> **＋** `## Debt` holds each box of the Spec that is debt and each red test reverted into a patch, with the path of the patch. Under them stands a line with the count of the boxes that wait for the librarian. Then comes one line per Estimate whose reading cannot be taken yet, each one this session creates or updates among them, except one that `## Ask the person` holds: its slug and the moment its reading waits for. These lines stand in the section and are not debt.
> **＋** `## Observations` holds what was noticed in Work Mode and Retro, a red before the work and an expected red among them; `## For the next session` holds what needs a decision.
> **＋** `## Ask the person` holds one line per reading that only the person can take: the Estimate by slug, the mark `needs the person` and the question the person answers.
> **－** No statement stands twice: a Case, box, reading, lesson or observation that one section names stands in another section only with what that section's kind adds about it, such as a caveat or what to check first, and no section says again what another section says of it. The file holds no commit, no number of an item and no end of an item.
> **－** The section names `## Notes from memory`, `## Direct instructions to the librarian` and `## What actually got done` stay, so `rule-brief` reads `## What actually got done` as before.

```then
update:
- slug: rule-handoff
  replace:
  - old: '- `## Direct instructions to the librarian`: what to check first, what may duplicate what.'
    new: '- `## Direct instructions to the librarian`: what to check first, what may duplicate what; no reading that waits, which `## Debt` lists (case 624).'
  - old: 'under them two lines: the count of the boxes that wait for the librarian, and the slugs of the `read` lines whose slug this session creates or updates.'
    new: 'under them a line with the count of the boxes that wait for the librarian, then one line per Estimate whose reading cannot be taken yet, each one this session creates or updates among them, except one that `## Ask the person` holds: its slug and the moment its reading waits for; these lines stand in the section and are not debt (case 624).'
  - old: 'A fact stands in one section only: a Case, a box, a reading, a lesson or an observation named in one section is not named in another (cases 468.2, 531.5).'
    new: 'A thing is said once: a Case, a box, a reading, a lesson or an observation that one section names stands in another section only with what that section''s kind adds about it — a caveat in `## Notes from memory`, what to check first in `## Direct instructions to the librarian` — and no section says again what another section says of it (cases 468.2, 531.5, 624).'
  change: 'a thing is said once: a second section names it only with what its kind adds; the readings that wait stand in Debt alone, each with its moment, and are not debt (case 624)'
- slug: estimate-handoff-holds-each-fact-once
  set:
    status: pending
    purpose: Whether handoff.md, the report of Retro, says each thing once in the section of its kind — a Case, box, reading, lesson or observation named again only with what the second section adds, the readings that wait listed in Debt alone and not counted as debt — with no commit, no number and no end, and keeps the three old section names
    method: one reading by hand, at the /hi of a later session, of a handoff.md written by .claude/skills/handoff/SKILL.md as rendered from rule-handoff after case 624, against the close of its Retro, recorded in the estimate line
  change: the Criterion replaced whole — one statement once, a second section naming a thing only with what its kind adds; the readings that wait in Debt alone, each with its moment, not debt; read on a handoff the rendered skill wrote (case 624)
```

```tasks
- [x] update `rule-handoff`
- [x] update `estimate-handoff-holds-each-fact-once`
- [x] `uv run guppi render`: `.claude/skills/handoff/SKILL.md`
- [ ] read `estimate-handoff-holds-each-fact-once`
```

## Case 625 — The method of four Estimates no longer names a moment no one brings on

> **context:**
> An Estimate's `method` says how its reading is taken and at which moment. At `/hi` the agent takes a pending reading only when every moment its `method` names has come; a reading whose moment has come in no session waits, and its line stays open (`rule-skill-hi`). The `method` of four Estimates names a moment that a normal run never brings, and that no one stages. `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` names a `/work` the person types. `estimate-prespec-onward-sends-the-agent-on` and `estimate-retro-onward-sends-the-agent-to-the-handoff` name a Plan Mode or an end of Retro at which the ledger hook refuses a line. `estimate-retro-runs-on-to-the-handoff` names a Retro at which that hook refuses a line. Session 0004 closed all four `passed` on the person's word (its ledger lines 6, 14, 15 and 16), with that moment written as not exercised. The handoff of 0004 notes that no Case changed the `method`. So the next time a Case sets one of them `pending`, its reading waits for good, or needs the person's word again.
>
> The person chose to drop the moment from the `method` of the four and to keep the change to these four pages: no rule page changes. The Criterion, `purpose` and status of each stay. The behaviour at the dropped moment is still set by `rule-work-mode`, `rule-prespec-onward`, `rule-retro-onward` and `rule-retro`, and it is still promised. `estimate-retro-runs-on-to-the-handoff` already treats a `/retro` the person types this way: its `When` names it, and its `method` does not. In the two hook Estimates, `tests/test_onward.py` keeps covering a refusal of the ledger hook, through the tests that a ledger refusal of the same reply or of a later reply sends the hook on again, in Plan Mode too. Nothing reads a `/work` the person types, or the agent's answer to a refusal at Retro. The person treats a fault there as a lesson when it comes. A change to a part alone sets no status (case 378.4), so the four stay `passed` and no new reading is due. The one Case for four Estimates stands against the rule of one promise per Case because it changes only `method` and no promise, and the person chose one Case.
>
> What done means: no new Estimate. `estimate-lint-reports-a-method-tied-to-a-one-off-moment` checks the form of the four new `method` texts, in pre-spec and in the `make lint` of the librarian's run. `estimate-hi-takes-its-readings` already promises the behaviour this change unblocks: `/hi` takes a reading once every moment its `method` names has come. Its Criterion stands because it reads the moment from the `method` and does not list moments.
>
> Frame checks:
> - A Grep of `^method:.*(ledger hook refuses|refusal of the ledger hook|person types)` over `vault/wiki/estimates/` printed only the four pages. No other `method` names these moments.
> - A Grep of the four slugs over the repository outside `vault/raw/`, `vault/archive/` and `vault/wiki/decisions/` printed `log.md`, `rule-prespec-onward.md`, `rule-retro-onward.md`, `rule-retro.md`, `rule-work-mode.md`, `estimate-case-build-answers-what-done-means.md`, `estimate-generate-renames.md` and `estimate-retro-onward-exits-2-on-an-error.md`. It printed no code file. The hits in the rule pages are their `estimates` fields and History lines. The hits in `estimate-case-build-answers-what-done-means` and `estimate-generate-renames` are in past Results. `estimate-retro-onward-exits-2-on-an-error` uses the Criterion of `estimate-retro-onward-sends-the-agent-to-the-handoff` for the stretch, and that Criterion stays. No hit is made false.
> - A Grep of `not exercised` printed 26 files over `vault/wiki/` and none over `.claude/`. The phrase appears only in Results and `brief.md`, and no rule sets it, so this Case sets nothing about it.
> - The change sets no new moment. It changes what the reading step of `rule-skill-hi` finds in four `method` fields, and the text of that step stays true. The `method` description in `rule-estimates-schema` stays true: each new `method` names the kind of its moment, holds `by hand` or `pytest`, and has no word "first".
> - Case 624 changes `rule-handoff` and `estimate-handoff-holds-each-fact-once` and sets the writing of `handoff.md`. This Case changes neither page and sets no part of that moment. After it, a handoff that lists these four in `## Debt` no longer lists these moments.
>
> The Case creates no page, so the vault query was not run.

> **problem:**
> Four Estimates name in their `method` a moment that a normal run never brings: a `/work` the person types, or a refusal of the ledger hook. Each passed only on the person's word, and when a later Case sets one `pending`, its reading waits for that moment for good. The question is whether the `method` keeps the moment or drops it.

> **recommend:**
> - **Drop or keep the moment that never comes**
>   - Recommended: (a) drop the moment from the `method` of all four; the tests of `tests/test_onward.py` keep covering the refusal path of the two hooks, and a fault at a typed `/work` or in the answer to a refusal shows as a lesson when it comes.
>   - Answer: agreed with the recommendation, (a).
> - **Only these four pages, or a general rule**
>   - Recommended: (a) only the four pages; no sentence is added to `rule-estimates-schema`.
>   - Answer: agreed with the recommendation, (a).
> - **What the pages promise about the moment that was dropped**
>   - Recommended: (a) keep the promises and change only `method`; the four stay `passed`, as `estimate-retro-runs-on-to-the-handoff` already treats a typed `/retro`.
>   - Answer: agreed with the recommendation, (a).
> - **How we know this change is done**
>   - Recommended: (a) no new check; the Case names `estimate-lint-reports-a-method-tied-to-a-one-off-moment` for the form and `estimate-hi-takes-its-readings` for the next reading.
>   - Answer: agreed with the recommendation, (a).
> - **One Case or one sub-case per page**
>   - Recommended: (a) one Case with four page updates, ratified together.
>   - Answer: agreed with the recommendation, (a).

> **given:**
> `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — the reading of `/work`; its `method` changes
> **＋** `estimate-prespec-onward-sends-the-agent-on` — the reading of the hook that sends Plan Mode on; its `method` changes
> **＋** `estimate-retro-onward-sends-the-agent-to-the-handoff` — the reading of the hook that sends Retro on; its `method` changes
> **＋** `estimate-retro-runs-on-to-the-handoff` — the reading of Retro; its `method` changes
> **＋** `tests/test_onward.py` — the tests of a refusal of the ledger hook that the two hook Estimates name
> **＋** `rule-skill-hi` — the reading step at `/hi`, which reads the moments of a `method`; unchanged
> **＋** `rule-estimates-schema` — the form of a `method`; unchanged

> **when:**
> At `/hi`, the agent reads the `method` of `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-prespec-onward-sends-the-agent-on`, `estimate-retro-onward-sends-the-agent-to-the-handoff` or `estimate-retro-runs-on-to-the-handoff` to judge, by the reading step of `rule-skill-hi`, whether each moment of its reading has come.

> **then:**
> The `method` of `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` names only a `/work` the agent calls, and no `/work` the person types.
> **＋** The `method` of `estimate-prespec-onward-sends-the-agent-on` names `tests/test_onward.py` for a refusal of the ledger hook, and a reading by hand at a Plan Mode that closes its last Case, with no refusal of the ledger hook as its moment.
> **＋** The `method` of `estimate-retro-onward-sends-the-agent-to-the-handoff` names `tests/test_onward.py` for a refusal of the ledger hook, and a reading by hand at an end of Retro, with no refusal of the ledger hook as its moment.
> **＋** The `method` of `estimate-retro-runs-on-to-the-handoff` names a run from `/work` to the librarian, and no Retro at which the ledger hook refuses a line.
> **＋** So, by `rule-skill-hi`, the next reading of each of them is taken once the moments its `method` names have come, with no word from the person.
> **－** The Criterion, `purpose` and status of each stay: a `/work` the person types, a refusal of the ledger hook and the agent's answer to it stay promised.
> **－** `rule-estimates-schema` and `rule-skill-hi` stay as they are.

```then
update:
- slug: estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline
  set:
    method: 'uv run guppi render --check; by hand, a /work the agent calls at the fork and a /work that /box calls: the branch, work.md, the ticks of the Spec, the carry.md of the folder and each Expected red line read against the Criterion, and, where a substitution came back empty, the agent''s own run of its command, recorded in the estimate line'
  change: method names no /work the person types, a moment no one brings on (case 625)
- slug: estimate-prespec-onward-sends-the-agent-on
  set:
    method: 'uv run pytest tests/test_onward.py tests/test_ledger.py, which cover a refusal of the ledger hook; by hand at a Plan Mode that closes its last Case: the transcript, the event log and frontier.md, recorded in the estimate line'
  change: method names no Plan Mode at which the ledger hook refuses a line, a moment no one brings on; the tests cover the refusal (case 625)
- slug: estimate-retro-onward-sends-the-agent-to-the-handoff
  set:
    method: 'uv run pytest tests/test_onward.py tests/test_ledger.py, which cover a refusal of the ledger hook; by hand at an end of Retro: the transcript, the event log and handoff.md, recorded in the estimate line'
  change: method names no end of Retro at which the ledger hook refuses a line, a moment no one brings on; the tests cover the refusal (case 625)
- slug: estimate-retro-runs-on-to-the-handoff
  set:
    method: 'by hand at a run from /work to the librarian: the replies of the turn, the ledger, git log and handoff.md read against the Criterion, recorded in the estimate line'
  change: method names no Retro at which the ledger hook refuses a line, a moment no one brings on (case 625)
```

```tasks
- [x] update `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
- [x] update `estimate-prespec-onward-sends-the-agent-on`
- [x] update `estimate-retro-onward-sends-the-agent-to-the-handoff`
- [x] update `estimate-retro-runs-on-to-the-handoff`
```

## Case 626 — ask-guppi answers /pre-spec in findings and the five lines answer whether a thing exists

> **context:**
> `ask-guppi` searches the vault for its caller. Its frame, `.claude/agents/ask-guppi.md`, rendered from `rule-ask`, tells it to answer every question in exactly five lines: `exists`, `near`, `missing`, `rules` and tags/slug. The main agent dispatches it at only one moment: once, at the first `/pre-spec` of a session. There the `/pre-spec` skill asks it three questions of another kind: which Case contradicts a page, a rule or another Case; which Estimate a Case does not name speaks of the thing the Case changes; and which fact of a `context` the vault does not bear out. The two texts pull apart, so the form of the answer changes from run to run. `estimate-ask-finds` failed in session 0004 (ledger line 17). Of the four dispatches it read, the answers of sessions 0317 and 1416 opened with numbered findings, and the answer of 0115 held nested lists under the five labels. Case 623 put the item off. The dispatch at the `/pre-spec` of session 0004 (transcript a17e0a5f), which that reading did not read, forced its findings into labels that do not fit. Its `exists` line said that no Case contradicts a page, and its `near` and `missing` lines held contradictions and wrong counts.
>
> The person chose to give `/pre-spec` a form of its own in the frame: one numbered list of findings under each of the three questions, in their order. Each finding names its Case and the page or Cases it bears on, and a question with no finding says "none". The five lines stay the answer to a question whether a thing exists. A list of the paths of the files read may still follow, as case 582 allows. The skill `/pre-spec` and `rule-prespec` stay as they are, so only the frame sets the form. The lines of the Criterion that no normal run exercises are moved to a new Estimate on `rule-ask`, `estimate-ask-query-before-a-create`. They cover a page asked about in either language, the rule a proposal crosses and the state of a slug in the archive. That Estimate is read where the query really runs: in the transcript of `case-guppi`, which runs the recipe itself before a `create` without a `ref`. `estimate-ask-finds` keeps only the dispatch at `/pre-spec`. Its Criterion is replaced whole, and its `purpose` and `method` are set anew, since both state the old promise. `estimate-case-build-writes-the-case` keeps its Criterion. Its line that `case-guppi` runs the query and gives the answer in `context` stays true, and the new Estimate checks the same behaviour from the side of the recipe.
>
> The pre-spec of this session found one more sentence of the frame that the new form left without a place. For a page that carries `deferred_by`, the frame tells the agent to give the `## Problem` of the deferring Decision on the `exists` or `near` line. At `/pre-spec` there is no such line. The person chose to put that Problem in the finding that names the page. A fourth replace pair in `rule-ask` says so, and a line of the new Criterion of `estimate-ask-finds` checks it.
>
> The check of this answer noted that the lines of the old Criterion of `estimate-ask-finds` are not carried word for word. That is on purpose, and each line has a new place:
> - The old `When`, any dispatch with a question, narrows to the dispatch at `/pre-spec`, the only one the main agent makes.
> - The old line on the five lines becomes the line on one numbered list under each question. The five lines leave this Criterion, since no dispatch asks whether a thing exists.
> - The lines on the list of paths, the event log and nothing else reaching the caller are carried, with "the findings" in place of "the five lines".
> - The line on the Grep of the rules is carried word for word.
> - The lines on a page asked in either language, a crossed rule, the state of a named slug, an archived page opened only when asked and the archive never searched by meaning move to 626.2. There they are worded for the `context` of the Case that `case-guppi` builds, not for the lines of an answer.
>
> The check also noted that 626.1 and 626.2 share the line on the Grep of the rules. That is on purpose: both run the same recipe, one when the main agent dispatches the agent at `/pre-spec` and one when `case-guppi` runs it itself. Each Estimate reads that line at its own moment.
>
> `rule-ask` carries `deferred_by` `decision-case-553`, and `backlog.md` lists `rule-ask`. That defer asked that `ask-guppi` and `case-guppi` read Decision pages by one rule. The frame of `case-guppi` now reads Decision pages only as `ask-guppi.md` allows, so both follow one rule already. The person chose to retire the defer with no change on that point. The decision line of 626.1 on `rule-ask` carries `{supersedes:case 553}`. Case 623 deferred `estimate-ask-finds` with a History line and no `deferred_by` field, and `backlog.md` does not list it. So, as in Case 624, no `{supersedes:case 623}` is written.
>
> Frame checks. A Grep of `five lines` over the repository outside `vault/raw/`, `vault/archive/` and `vault/wiki/decisions/` printed 5 files: `brief.md`, `.claude/agents/ask-guppi.md`, `log.md`, `estimate-ask-finds.md` and `rule-ask.md`. The hits in `brief.md` and `log.md` were not read. The other three are changed by 626.1. A Grep of `ask-guppi|ask_guppi` over `guppi/` printed nothing. In `tests/test_casecheck.py`, line 334 shows that the check of `rule-case-check` passes an answer of `ask-guppi` unjudged. So no code reads the form. The moment this Case sets is the answer of `ask-guppi` at `/pre-spec`. A Grep of `ask-guppi.{0,200}(answer|five|form|finding)` over `vault/wiki/rules/*.md` and `.claude/**` printed 4 files: `.claude/agents/case-guppi.md`, `rule-prespec.md`, `rule-orchestration.md` and `rule-case-build.md`. `rule-prespec` sets what to send `ask-guppi` and the main agent's own report, not the form of the agent's answer. `rule-orchestration` sets only that `ask-guppi` asks at `/pre-spec`. `rule-case-build` and `case-guppi.md` have `case-guppi` run the query itself, which keeps the five lines. Each stays true. `estimate-prespec-reconciles` names the three questions and not the form, and `estimate-case-build-checks-the-finished-case` counts what `ask-guppi` finds at `/pre-spec` without a form. Both Criteria stand. `rule-ask` lists only `estimate-ask-finds` in `estimates`. A Glob of `vault/**/estimate-ask-*.md` printed only `estimate-ask-finds.md`, so the new slug is free. Cases 624 and 625 of this session change none of these pages and set nothing at `/pre-spec`. The new Estimate has `ref: rule-ask`, so the vault query was not run.

> **problem:**
> The frame of `ask-guppi` requires five lines for every answer, while `/pre-spec`, the one moment the main agent dispatches it, asks for three kinds of findings. The answers swing between the two forms, and `estimate-ask-finds` fails on them. Its lines about a page asked in either language, a crossed rule and an archived slug wait for a dispatch that no normal run makes. The question is which form the answer takes at `/pre-spec`, and where the rest of the check is read.

> **recommend:**
> - **Which form the answer of ask-guppi takes at /pre-spec**
>   - Recommended: (a) a second form for `/pre-spec`: the frame keeps five lines for a question whether a thing exists and sets, for `/pre-spec`, numbered findings under the three questions, each naming its Case and page, "none" for a question with no finding, a file list allowed after; `rule-ask` and the Criterion of `estimate-ask-finds` change.
>   - Answer: agreed with the recommendation, (a).
> - **How the "does it exist" parts of the check get read**
>   - Recommended: (b) read them in the transcript of `case-guppi` when it runs the search itself before a `create`; `estimate-ask-finds` keeps only the dispatch at `/pre-spec`.
>   - Answer: agreed with the recommendation, (b).
> - **The question put off on rule-ask: may ask-guppi open Decision pages**
>   - Recommended: (a) close it as already settled: both agents now read Decision pages by the rule of `ask-guppi.md`; the change of `rule-ask` retires the defer, and nothing about Decision pages changes.
>   - Answer: agreed with the recommendation, (a).
> - **Where the "does it exist" lines of the check go**
>   - Recommended: (a) a new Estimate on `rule-ask`, `estimate-ask-query-before-a-create`, read by hand in a session where `case-guppi` builds a Case with a `create` without a `ref`.
>   - Answer: agreed with the recommendation, (a).
> - **Does the /pre-spec skill also state the form**
>   - Recommended: (a) the form lives in the frame of `ask-guppi` alone; `rule-prespec` and its Estimate stay.
>   - Answer: agreed with the recommendation, (a).
> - **Where the put-off question of a page goes in the /pre-spec answer**
>   - Recommended: (a) in the finding that names the page, by a second replace pair in `rule-ask`; the five-line answer keeps it on the `exists` or `near` line; one more line of the Criterion of `estimate-ask-finds` checks it.
>   - Answer: agreed with the recommendation, (a).

### Case 626.1 — ask-guppi answers /pre-spec with a numbered list under each question

> **given:**
> `rule-ask` — its Render is the text of `.claude/agents/ask-guppi.md`; four passages change
> **＋** `.claude/agents/ask-guppi.md` — the agent rendered from `rule-ask`
> **＋** `estimate-ask-finds` — the check whose Criterion is replaced whole and whose `purpose` and `method` are set anew
> **＋** `.claude/skills/pre-spec/SKILL.md` — sends `ask-guppi` the plan file and the three questions; unchanged
> **＋** `rule-prespec` — the main agent's report built from the findings; unchanged
> **＋** `vault/wiki/rules/` — the rule pages the agent greps first
> **＋** `vault/raw/<date>/event_log.md` — records each dispatch

> **when:**
> At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> The answer opens with one numbered list of findings under each question of `.claude/skills/pre-spec/SKILL.md`, in its order: what contradicts a page, a rule or another Case; an Estimate a Case does not name that speaks of the thing the Case changes; a fact of a `context` the vault does not bear out.
> **＋** Each finding names its Case and the page or the Cases it bears on; a question with no finding says "none".
> **＋** A finding that names a page carrying `deferred_by` gives the `## Problem` of the Decision that field names.
> **＋** After the findings a list of the paths of files the agent read may stand, as the general note of Claude Code asks of a sub-agent.
> **＋** The agent starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs one Grep per other category the question touches.
> **＋** The dispatch stands in `vault/raw/<date>/event_log.md`.
> **－** The findings are not put under the lines `exists`, `near`, `missing`, `rules` and tags/slug: those lines answer a question whether a thing exists.
> **－** No index line, page text or other note reaches the caller beyond the findings and that list of paths.
> **－** An answer with no list after the findings holds the promise as well.

```then
update:
- slug: rule-ask
  replace:
  - old: for the caller and answer in five lines.
    new: for the caller and answer in one of the two forms set at the end.
  - old: give its `## Problem` on the `exists` or `near` line,
    new: give its `## Problem` on the `exists` or `near` line, or, at `/pre-spec`, in the finding that names the page,
  - old: 'Answer with exactly these five lines, each present, "none" when empty:'
    new: 'To a question whether a thing exists — what is close, what is missing, which rule it crosses, which tags fit, whether a slug is free — answer with exactly these five lines, each present, "none" when empty:'
  - old: '- tags/slug: tags that fit, existing first; the named slug — `free`, `live` (with its category), or `archived at <path> by [[decision-case-N]]`, N from the page''s `origin`'
    new: |-
      - tags/slug: tags that fit, existing first; the named slug — `free`, `live` (with its category), or `archived at <path> by [[decision-case-N]]`, N from the page's `origin`

      At `/pre-spec`, where the caller asks which Case of the plan contradicts a page of the vault, a rule of the vault or another Case, which Estimate a Case does not name speaks of the thing the Case changes, and which fact of a `context` the vault does not bear out, answer instead with one numbered list of findings under each question, in that order: each finding names its Case and the page or the Cases it bears on, and a question with no finding says "none" (case 626.1).
  change: ask-guppi answers /pre-spec with one numbered list of findings under each question, the Problem of a page's deferred_by in the finding that names the page; the five lines answer a question whether a thing exists; the defer of case 553 retired, both agents reading Decision pages by the rule of ask-guppi.md (case 626.1)
- slug: estimate-ask-finds
  set:
    status: pending
    purpose: Whether ask-guppi answers the questions of /pre-spec with one numbered list of findings under each question, each finding naming its Case and the page or Cases it bears on, a list of the paths of the files it read allowed after them
    method: 'by hand at the /hi of a later session: the answer of ask-guppi at a /pre-spec after the render of .claude/agents/ask-guppi.md by case 626.1, read in its agent transcript against the event log, recorded in the estimate line'
  change: the Criterion replaced whole — the dispatch at /pre-spec answered by one numbered list of findings under each question, not by the five lines, the Problem of a deferred page in its finding; the lines on a page asked in either language, a crossed rule and an archived slug moved to estimate-ask-query-before-a-create (case 626.1)
```

```tasks
- [x] update `rule-ask`
- [x] update `estimate-ask-finds`
- [x] `uv run guppi render`: `.claude/agents/ask-guppi.md`
- [x] read `estimate-ask-finds`
```

### Case 626.2 — The vault query that case-guppi runs is checked by an Estimate of its own

> **given:**
> `rule-ask` — the recipe of the vault query, the target of the new Estimate
> **＋** `.claude/agents/ask-guppi.md` — the recipe as rendered
> **＋** `.claude/agents/case-guppi.md` — runs the query itself before a `create` without a `ref`
> **＋** `vault/wiki/rules/` — the rule pages the query greps first
> **＋** `vault/archive/` — where a named slug is checked by Glob
> **＋** `estimate-ask-query-before-a-create` — the new Estimate
> **＋** `estimate-case-build-writes-the-case` — already checks that the query runs and its answer stands in `context`; unchanged

> **when:**
> `case-guppi`, following `.claude/agents/case-guppi.md`, builds a Case that proposes a `create` without a `ref` and, before it answers, runs itself the vault query of `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

> **then:**
> It starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs one Grep per other category the question touches.
> **＋** A page that already holds the thing is found by meaning, whether the person's words name it in Russian or in English, and the `context` of the Case names its slug.
> **＋** A proposal that crosses a rule or a lesson, such as a `SessionStart` hook meant to block, names that rule or lesson in the `context`.
> **＋** The slug the Case writes is checked by a Glob over `vault/archive/`, and the `context` says it is free, live with its category, or archived at its path by the Decision that the archived page's `origin` names.
> **＋** An archived page is opened only when the question names its slug and asks what it said or why it was withdrawn.
> **－** The archive is not searched by meaning: a page the `context` names as existing or near is a live page.

```then
create:
- slug: estimate-ask-query-before-a-create
  type: estimate
  ref: rule-ask
  kind: QA
  purpose: Whether the vault query that case-guppi runs before a create without a ref, by the recipe of ask-guppi, starts with the rules, finds an existing page by meaning in either language, and names the rule a proposal crosses and the state of a named slug
  method: 'by hand at the /hi of a later session: the transcript of a case-guppi that built a Case with a create without a ref after the render of .claude/agents/ask-guppi.md by case 626.1, its Grep and Glob calls and the context of its Case read against the Criterion, recorded in the estimate line'
  tags:
  - session
  - workflow
  - harness
```

```tasks
- [x] create `estimate-ask-query-before-a-create`
- [ ] read `estimate-ask-query-before-a-create`
```
