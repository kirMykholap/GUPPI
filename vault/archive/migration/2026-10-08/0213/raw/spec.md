<!-- approved 02:52:14 · session 70a7ddbd -->

# Spec — session 0213, 2026-10-08

## Case 732 — An Ask line waits for the close of a sprint

> **context:**
> At `/hi` the agent writes the brief's `Ask the person` lines under `## Ask` of `frontier.md` and puts each open `A` line to the person as a question in its first reply. Nothing checks whether the moment of that reading has come. At the `/hi` of session 0213 the line of `estimate-hi-writes-frontier` was put to the person, though its question names the `/hi` of the session after the close of a sprint, and no sprint has closed; it would come back the same way at every `/hi` until then. `rule-skill-hi` already lets a `W` line whose `method` names the session that closes a sprint, or the session after that close, stay open and wait (case 670.5); an `A` line had no such rule. The person chose to mirror that rule at `/hi`: an `A` line whose question names one of those two moments stays open under `## Ask` and is not asked until its moment, judged from the line as the brief gives it, with no page opened; the session after a close is the one whose brief opens its `Cases` with `open the next sprint`. The Criterion of `estimate-hi-takes-its-readings` says that each open `A` line is put to the person, so this Case replaces it whole and sets its `purpose` anew; its `method`, the skill text read against the Criterion, stays true. Retro, `rule-handoff` and `rule-brief` stay as they are: they still pass the line on each session, and a waiting line stays open, so `/carry` still carries it as an open `A` line. A Grep of `` `A` line|Ask line|A<n>|## Ask\b `` over `vault/wiki/` printed 20 files and over `.claude/` 5 files. Three hits stand as they are. The first is the sentence of `orchestration.md` that sets the form of the question of an open `A` line at `/hi`, which now covers only the lines that are put. The second is the Criterion of `estimate-orchestration-asks-in-the-grill-me-shape` speaks of the same question in an exception line: the question of an open `A` line at `/hi` keeps its own form. That Criterion stands, since it sets the form of a question that is put, not which lines are put. The third is the exception line of `estimate-hi-writes-frontier` that an `A` line stands open until its work is done, which a waiting line keeps. The rendered `.claude/skills/hi/SKILL.md` follows at the librarian's render, and no code reads this text.

> **problem:**
> `/hi` asks the person for a reading that the person cannot give before a sprint closes, and it asks again at every session until then.

> **recommend:**
> - **Where an Ask line that waits for a later moment is held back**
>   - Recommended: (a) at `/hi`: the line stays under `## Ask`, open, and is not put to the person until its moment, as the rule for a waiting `W` line does.
>   - Answer: agreed, (a).
> - **What the agent reads to judge whether the moment has come**
>   - Recommended: (a) the question on the Ask line as the brief gives it, with no page opened; a question that names no moment is asked as today.
>   - Answer: agreed, (a).
> - **Which moments make an Ask line wait, and how the agent knows a moment has come**
>   - Recommended: (a) the same two moments as the `W` rule: the line is asked at the `/hi` whose brief opens its `Cases` with `open the next sprint`, or in the session the person names as the one that closes the sprint.
>   - Answer: agreed, (a).
> - **Which check proves the change**
>   - Recommended: (a) replace the Criterion of `estimate-hi-takes-its-readings` whole, with an exception line for a waiting `A` line, and set its purpose anew.
>   - Answer: agreed, (a).

> **given:**
> `rule-skill-hi`: the rule whose Render is the skill `/hi`.
> **＋** `.claude/skills/hi/SKILL.md`: the skill file rendered from `rule-skill-hi`.
> **＋** `estimate-hi-takes-its-readings`: its Criterion is replaced whole.
> **＋** `vault/wiki/brief.md`: the brief whose Next session gives the `Work` and `Ask the person` lines.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.

> **when:**
> The person types `/hi` of `.claude/skills/hi/SKILL.md` on `UserPromptSubmit`, and the agent writes `raw/<date>/<hi HHMM>/frontier.md`, whose `## Work` holds the `pending` readings of `vault/wiki/brief.md` and whose `## Ask` holds its readings that only the person can take.

> **then:**
> In its first reply, before the question on the order, the agent takes each reading of an open `W` line whose whole method runs now.
> **＋** It reads what the method names from `vault/wiki/brief.md`, `git log`, `git status` and the files and commands the method names.
> **＋** It opens the page of each Estimate it reads and judges the reading against its `## Criterion`.
> **＋** It closes the `W` line of each reading taken `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`, then writes one `estimate[...]` line per reading in a `LEDGER` block of the reply, which ends in text.
> **＋** For each other open `W` line, whose reading cannot run now, it writes one line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` that names the Estimate by slug and asks to fix its method, replace its Criterion or archive it; the `W` line closes `· case N` when that Case is ratified.
> **＋** In the same reply, before the question on the order, it puts each open `A` line to the person as a question: the Estimate by slug and its question.
> **＋** When the person answers one, the agent closes its `A` line `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md` first, then writes its `estimate[...]` line, the answer as its result, in a `LEDGER` block of the reply, which ends in text.
> **－** It reads no transcript of an earlier session.
> **－** A `W` line of an Estimate whose `method` names the session that closes a sprint, or the session after that close, stays open under `## Work` and is no Cases line.
> **－** An `A` line whose question names the session that closes a sprint, or the session after that close, stays open under `## Ask` and is not put to the person. It is put at the `/hi` whose `vault/wiki/brief.md` opens the `Cases` of its Next session with `open the next sprint`, or in the session the person names as the one that closes the sprint. The agent judges this from the line as `vault/wiki/brief.md` gives it, with no page opened.
> **－** The Frontier is still assembled with no page opened. Only the reading step opens the pages of the Estimates it reads.
> **－** At `/hi` the agent changes no page and no file except `raw/<date>/<hi HHMM>/frontier.md`.

```then
update:
- slug: rule-skill-hi
  replace:
  - old: 'Then put each open `A` line to the person as a question, in the same reply, before the question on the order: the Estimate by slug and its question.'
    new: 'Then put each open `A` line to the person as a question, in the same reply, before the question on the order: the Estimate by slug and its question. An `A` line whose question names the session that closes a sprint, or the session after that close, stays open under `## Ask` and is not put to the person: it is put at the `/hi` whose brief opens the `Cases` of its Next session with `open the next sprint`, or in the session the person names as the one that closes the sprint; judge this from the line as the brief gives it, no page opened (case 732).'
  change: an Ask line whose question names the close of a sprint, or the session after it, stays open and is not asked until that session
- slug: estimate-hi-takes-its-readings
  set:
    status: pending
    purpose: Whether /hi takes, in its first reply, each open W reading whose whole method runs now from files and commands, reads no transcript, writes a Cases line for each other open W line but those of the close of a sprint, puts each open Ask line to the person but one that waits for the close of a sprint or the session after it, writes the answer as its reading line, and opens no page but the Estimates it reads
  change: the Criterion replaced whole — an Ask line that waits for the close of a sprint, or the session after it, stays open and is not asked; the purpose set anew
```

```tasks
- [x] update `rule-skill-hi`
- [x] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [x] update `estimate-hi-takes-its-readings`
- [x] read `estimate-hi-takes-its-readings`
```

## Case 733 — Pre-spec judges the method of a MOC's Estimate by its form

> **context:**
> `/pre-spec` judges the `method` of each Estimate item of a plan by `names_a_form` of `guppi/lint.py`: a `make <target>`, the word `pytest`, a path under `tests/` or the words `by hand`. `make lint` is stricter for an Estimate of a MOC: `check_method` passes there only a `make <target>`, or `by hand` when the children's counted Estimates are readings or a sibling names a target. The check of the Case file runs `prespec.judge`, and so `check_form`, over the Case `case-guppi` writes, so it applies the same test. A MOC's Estimate whose `method` names a test file or `pytest` alone therefore passes both checks in Plan Mode and turns lint red only at the librarian's run. That happened to `estimate-hi-writes-frontier`, whose `method` named the person's answer and `tests/test_prespec.py` without `by hand`; Case 731 fixed that one method and left the gap, and the handoff of session 0050 names it for the next session. The person chose to have pre-spec judge the form alone: on a MOC, a `method` that names neither a `make <target>` nor `by hand` is a finding. The Makefile and the children stay with lint. A page counts as a MOC as the plan leaves it: the live page, or a `create` or an `update` of the plan that writes `kind: MOC`. The test of that form is one predicate in `guppi/lint.py`, which `check_method` calls too, as `CLAUDE.md` sets for one judgment in two places. The check of the Case file calls the same `judge`, so it takes the change with no edit of its own, but in a narrower scope: `judge` builds the blocks `check_form` reads only from the text it is given, and there that text is the Cases of the one file. That check therefore sees a MOC on the live page or in an item of the same file. A MOC that another Case of the session creates, or sets to `kind: MOC`, is seen only by `guppi prespec --check` over the whole plan. The Criterion speaks of `guppi prespec --check` alone, so it makes no claim on that scope. The Criterion of `estimate-case-check-sends-back-a-faulty-case` says that the check of the Case file runs `judge` of `guppi/prespec.py` over the Cases of the file. It stands: this Case changes what `check_form` inside `judge` finds, not how that check calls `judge` or what it stores. The Criterion of `estimate-prespec-catches-a-method-without-a-form` says the MOC branch stays with lint, so this Case replaces it whole: it carries the other lines word for word, drops that line alone, and sets its `purpose` and `method` anew to cover the MOC branch. `estimate-lint-checks-the-method` stands: lint judges each `method` as before, and `tests/test_lint.py` shows that the predicate lifted out of `check_method` leaves its judgment unchanged. A Grep of `branch of a MOC|MOC stays with lint|MOC branch` over the repository, `vault/raw/` and `vault/archive/` left out, printed `guppi/prespec.py` and `vault/wiki/estimates/estimate-prespec-catches-a-method-without-a-form.md`. The first is the docstring of `check_form`, which Work Mode rewrites, and the second is the Criterion this Case replaces. A Grep of `estimate-prespec-catches-a-method-without-a-form` over the same paths printed `vault/wiki/log.md` and `vault/wiki/rules/rule-prespec.md`. The `rule-prespec` hits are its `estimates` list and a History line, which stand. The Render of `rule-prespec` leaves what the check compares to the module docstring of `guppi/prespec.py`, so the page does not change.

> **problem:**
> Pre-spec and the check of the Case file pass a MOC's Estimate whose `method` names a test file or `pytest` alone, which `make lint` reports only at the librarian's run.

> **recommend:**
> - **How much of the MOC test does pre-spec take over?**
>   - Recommended: (a) the form only: on a MOC, a `method` that names neither a `make` target nor `by hand` is a finding; the Makefile and the children stay with lint; one shared function in `guppi/lint.py`.
>   - Answer: agreed, (a).
> - **Which pages count as a MOC when pre-spec judges?**
>   - Recommended: (a) as the plan leaves the page: the live page, a `create` or an `update` of the plan that writes `kind: MOC`.
>   - Answer: agreed, (a).
> - **How is the promise recorded?**
>   - Recommended: (a) replace the Criterion of `estimate-prespec-catches-a-method-without-a-form`, its `purpose` and `method` set anew.
>   - Answer: agreed, (a).

> **given:**
> `estimate-prespec-catches-a-method-without-a-form`: the check of the form of a `method` in the plan; its Criterion, `purpose` and `method` are set anew.
> **＋** `rule-prespec`: the rule the Estimate checks.
> **＋** `guppi/prespec.py`: `check_form` judges the `method` of each Estimate item of the plan.
> **＋** `guppi/lint.py`: `names_a_form`, and `check_method`, whose test of the form of a MOC's `method` becomes one shared predicate.
> **＋** `tests/test_prespec.py`: the unit tests of the findings of `check_form`.
> **＋** `tests/test_lint.py`: the unit tests of `check_method`.
> **＋** `estimate-lint-checks-the-method`: the check of the judgment of `check_method`; its Criterion stands.

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` reads the items of the plan's `then` blocks before the Spec is approved.

> **then:**
> A `create` of an Estimate, or an `update` carrying `set: {method: …}`, whose `method` names none of the forms lint classifies (a `make <target>`, the word `pytest`, a path under `tests/`, or the words `by hand`) gives one line `case N: <create|update> <slug>: method names no form`, which goes on to name those forms.
> **＋** A `create` of an Estimate with no `method` at all gives the same finding.
> **＋** When the target of the Estimate is a MOC as the plan leaves it — the live page, or a `create` or an `update` of the plan that writes `kind: MOC` — a `method` that names neither a `make <target>` nor `by hand` gives one line `case N: <create|update> <slug>: method of a MOC's Estimate names no make target and is not a reading`, in place of the line of no form.
> **＋** The predicate is one, lifted out of `guppi/lint.py`; `pre-spec` writes no second one.
> **＋** The form of a MOC's `method` is one predicate too, in `guppi/lint.py`, which `check_method` of `make lint` calls as well.
> **－** Existence is not checked in the plan: the file under `tests/` is written in Work Mode and lint checks it later.
> **－** Whether the `Makefile` holds the `make <target>` a MOC's `method` names is left to lint.
> **－** Whether every counted Estimate of the MOC's children is a reading, or a sibling Estimate names a `make <target>`, is left to lint.
> **－** An `update` of an Estimate that writes no `method` gives no line of the form of a MOC's `method`.

```then
update:
- slug: estimate-prespec-catches-a-method-without-a-form
  set:
    status: pending
    purpose: Whether pre-spec refuses an Estimate whose method names none of the forms lint classifies, or, on a MOC, neither a make target nor by hand
    method: uv run pytest tests/test_prespec.py on a temp plan — a create with a prose method, a create with no method, each of the four forms clean, and on a MOC a tests/ path alone and pytest alone as findings, a make target and by hand clean
  change: the Criterion replaced whole — pre-spec judges the method of a MOC's Estimate by its form (case 733)
```

```tasks
- [x] update `estimate-prespec-catches-a-method-without-a-form`
- [ ] `guppi/lint.py`: the test of the form of a MOC's `method` — a `make <target>` or `by hand` — is lifted out of `check_method` into one predicate, which `check_method` calls; the module docstring names it.
- [ ] `guppi/prespec.py`: `check_form` reads the kind of the target as the plan leaves it and judges a MOC's `method` by that predicate; the module docstring and the docstring of `check_form` say so, in place of the words that the branch of a MOC stays with lint.
- [ ] `tests/test_prespec.py`: a MOC target, live, created and set by an `update`, with a `tests/` path alone and `pytest` alone as findings, a `make <target>` and `by hand` clean, and an `update` with no `method` clean.
- [ ] `tests/test_lint.py`: runs green, the judgment of `check_method` unchanged.
- [x] read `estimate-prespec-catches-a-method-without-a-form`
```

## Case 734 — case-guppi lists the sentences a change touches by their meaning

> **context:**
> Before it answers, `case-guppi` looks for the sentences its change makes false. For other pages it searches for the slug of the changed page. Inside a page the Case changes, which it reads whole, nothing tells it how to find those sentences, so it searched for the words of the one sentence it changed. A sentence that states the same rule in other words never came up. In session 0050 this left three sentences of `rule-orchestration` that stated the batch without the new route, and `/pre-spec` found them; Case 730 was built and ratified again (`lesson-case-build-finds-the-sentences-it-changes-by-their-words`). The person chose a reading by meaning of each page the Case changes, and only of those pages: every sentence that states the behaviour the change touches goes on a list, whatever its words.
>
> The new sentence goes into the Render of `rule-case-build` right after the sentence that already asks for a judgment by meaning when no slug marks a fact. The Case replaces the Criterion of `estimate-case-build-checks-the-finished-case`, which checks what `case-guppi` does with its finished Case, with one more line for the list and for the sentences on it that enter the Case; the other lines are carried word for word. Its `purpose` and `method` both list the kinds of miss that the Estimate counts, so this `update` adds the new kind to each. `estimate-case-build-writes-the-case` checks the reading of the frame before the forks, and `estimate-case-build-reads-by-need-and-in-parts` checks that each page the Case changes is read whole. The new step uses that reading and leaves both promises as they are, so both Criteria stand. The Case sets `insight-workflow-case-written-without-reading-the-pages-it-changes` `actioned`, as Case 730.3 did. `rule-insights-schema` makes `addressed_by` the latest decision that fixed the pattern, and a Case of the session writes it as the bare slug (case 712). So the same `update` sets it to `decision-case-734` in place of `decision-case-391.2`, which 730.3 left standing.
>
> A Grep for `estimate-case-build-checks-the-finished-case|insight-workflow-case-written-without-reading-the-pages-it-changes` over `vault/wiki/` printed `brief.md`, `backlog.md`, `log.md`, `lesson-case-build-finds-the-sentences-it-changes-by-their-words.md`, `rule-case-build.md`, `lesson-orchestration-recommended-a-rebuild-that-signed-a-promise-twice.md` and `estimate-materialize-assembles.md`. The same Grep over the repository outside `vault/` printed nothing. `brief.md` and `log.md` are not read. `rule-case-build` is in `given`. The two lessons name the Insight in their `insight` field, which stands. `backlog.md` is written by `guppi backlog` alone (`rule-carry-over`), not by a Case. The hit in `estimate-materialize-assembles` is a past reading that names the `create` of the Estimate, and it stands.

> **problem:**
> Inside a page it changes, `case-guppi` finds the sentences to fix by the words of the one sentence it changes. A sentence that states the same rule in other words stays false until `/pre-spec` finds it, and the Case is built and ratified again.

> **recommend:**
> - **How the agent finds the sentences a change touches**
>   - Recommended: (a) read each changed page by meaning: list every sentence that states the behaviour the change touches, judged by what it says, not found by a word search; each enters the Case or `context` says why it stands.
>   - Answer: agreed, (a).
> - **Which pages the reading by meaning covers**
>   - Recommended: (a) only the pages the Case changes; other pages are still reached by the slug and moment searches and read around each hit.
>   - Answer: agreed, (a).
> - **Which Estimate checks the fix**
>   - Recommended: (a) add it to `estimate-case-build-checks-the-finished-case`: its Criterion replaced whole with one more line, and its purpose and method gain this kind of miss.
>   - Answer: agreed, (a).
> - **The open Insight**
>   - Recommended: (a) set `insight-workflow-case-written-without-reading-the-pages-it-changes` `actioned`, as the last session did.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build`: the rule whose Render sets how `case-guppi` checks its finished Case.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from `rule-case-build`.
> **＋** `estimate-case-build-checks-the-finished-case`: the check of the finished Case; its Criterion is replaced whole.
> **＋** `insight-workflow-case-written-without-reading-the-pages-it-changes`: the Insight this lesson reopened; set `actioned`.
> **＋** `rule-insights-schema`: the rule that sets `addressed_by` of an `actioned` Insight to the latest decision.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, has built a Case that changes a page and is about to answer with it.

> **then:**
> In each page the Case changes, which it has read whole, it lists each sentence that states the behaviour the change touches, judged by what the sentence says.
> **＋** A sentence that states the same rule in other words than the sentence the Case changes is on that list.
> **＋** Each sentence on that list that the change makes false enters the Case, or its `context` says why it stands.
> **－** The list is not made by a search for the words of the sentence the Case changes.
> **－** A page the Case does not change is still read around the line of each hit of its searches, not whole.

```then
update:
- slug: rule-case-build
  replace:
  - old: For a fact that no slug marks, read the index lines of the recipe of `.claude/agents/ask-guppi.md` and judge them by meaning.
    new: For a fact that no slug marks, read the index lines of the recipe of `.claude/agents/ask-guppi.md` and judge them by meaning. In each page the Case changes, which you read whole, list each sentence that states the behaviour the change touches, judged by what it says and never found by a Grep for the words of the sentence you change, so that a sentence that states the same rule in other words is on the list; each sentence on the list that the change makes false enters the Case, or `context` says why it stands (case 734).
  change: case-guppi lists by meaning each sentence of a page it changes that states the behaviour the change touches, not by a Grep for the words of the changed sentence (case 734)
- slug: estimate-case-build-checks-the-finished-case
  set:
    status: pending
    purpose: Whether case-guppi checks its finished Case before it answers — the chosen options, the pages that name a slug the change makes false, the sentences of a page it changes that state the changed behaviour in other words, the rules that act at the moment the change sets, the Cases of the session its prompt names or the check of its file names in a finding or a note, the purpose and method of an Estimate whose Criterion it replaces, what each search printed and that the context keeps only the searches the Case rests on, the sub-cases that change one page — counted by what ask-guppi still finds at pre-spec
    method: by hand, the text of .claude/agents/case-guppi.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec, read against the Criterion; the findings of ask-guppi at the /pre-spec of that session, when it ran, read for each Case case-guppi built — a Case that departs from a chosen option, a page naming a changed slug that the Case misses, a sentence of a page the Case changes that states the changed behaviour in other words and that the Case misses, a rule acting at the same moment that the Case misses, a Case of the session named in the prompt whose page or moment the Case clashes with, an Estimate whose purpose or method still states the promise its replaced Criterion dropped, a claim of context that its search did not print, a search in context that the Case does not rest on, two sub-cases whose texts on one page contradict — the count of each in the estimate line
  sections:
    Criterion: |-
      When:
      `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, has built a Case and is about to answer with it.

      Then:
      It puts each option the person chose in its rounds, or the person's own words where they answered outside the options, beside the `then` and `recommend` of the Case, and the Case holds each one; where the frame shows after a round that a chosen option cannot hold as written, its answer is a round on that point, not a Case with another behaviour.
      **＋** For each page whose text the change makes false, it searches the live pages of the vault, leaving out the Decision pages, and the code, for the page's slug, and reads each hit that `given` does not name around the line of the hit; for a fact that no slug marks, it reads the index lines of the recipe of `.claude/agents/ask-guppi.md` and judges them by meaning.
      **＋** In each page the Case changes, which it has read whole, it lists each sentence that states the behaviour the change touches, judged by what the sentence says and not found by a search for the words of the sentence it changes, so that a sentence that states the same rule in other words is on the list; each sentence on that list that the change makes false enters the Case, or its `context` says why it stands.
      **＋** When the change sets what happens at a moment — a reply, a hook event, a command — it searches `vault/wiki/rules/` and `.claude/` for the words that name that moment, reads each passage of each hit that sets a form or a behaviour at that moment, and the Case either does not cover that moment or names the other rule in `given`.
      **＋** It reads the case file `raw/<date>/<hi HHMM>/cases/case-<N>.md` of each Case of the session that the prompt of its call names, and of each Case of the session that the check of `rule-case-check` names in a finding or a note on its file, and no other Case of the session; where that Case changes a page the Case changes or sets what happens at the same moment, the Case does not cover that moment or names the case file in `given`, and its new text of that page does not contradict the text of that Case.
      **＋** When the Case replaces the Criterion of an Estimate, it reads the `purpose` and `method` of that Estimate, and the same `update` sets anew each one that states the old promise.
      **＋** Each hit that the change makes false enters the Case, or its `context` says why it stands.
      **＋** The `context` names a search only when the Case rests on it: a search with a hit that enters the Case, a search with a hit that stands and needs the reason why, or a search that a claim that no text says something rests on; a search that found nothing to change and that no claim rests on is left out.
      **＋** A claim of `context` about a text names the search it rests on: its pattern, the paths it ran over, and each file the search printed, a file it does not read included, or the count it printed; just before it answers, it runs each search that `context` names again, with the pattern and the paths that `context` writes, and the files and counts in `context` are the ones that run printed, not the files it read during the build; it claims nothing the search did not print.
      **＋** It reads side by side the finished new texts of all its sub-cases that change one page, and the Case holds no contradiction between them.
      **－** A hit in a History line, in `log.md` or in `brief.md` is not read.
  change: the Criterion replaced whole — case-guppi lists by meaning each sentence of a page it changes that states the behaviour the change touches; purpose and method name the new kind of miss (case 734)
- slug: insight-workflow-case-written-without-reading-the-pages-it-changes
  set:
    status: actioned
    addressed_by: decision-case-734
  change: 'actioned: case-guppi lists by meaning each sentence of a page it changes that states the behaviour the change touches, not by a Grep for the words of the changed sentence (case 734)'
```

```tasks
- [x] update `rule-case-build`
- [x] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [x] update `estimate-case-build-checks-the-finished-case`
- [x] update `insight-workflow-case-written-without-reading-the-pages-it-changes`
- [x] read `estimate-case-build-checks-the-finished-case`
```
