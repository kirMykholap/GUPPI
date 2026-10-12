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

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `Read side by side the finished new texts of all your sub-cases that change one page, and fix a contradiction between them (case 544.1).`
>   - new: `` In a Case with sub-cases, list each behaviour, field and term that a sub-case sets, read side by side every sentence of the new texts of all your sub-cases that speaks of it, whatever page each sub-case changes, and fix a contradiction between them (cases 544.1, 784). For each field, term or command whose behaviour the Case changes, Grep the live pages of `vault/wiki/` outside `decisions/`, and `.claude/`, for its name, and read each hit around its line, a row of `glossary.md` and the `## Criterion` of an Estimate included; a hit in a History line, in `log.md` or in `brief.md` is not read; each hit the change makes false enters the Case, or `context` says why it stands (case 784). ``
>   - change: `case-guppi reads side by side the sentences of all its sub-cases on one behaviour, field or term, whatever page each changes, and searches the live pages and .claude/ for the name of each field, term or command whose behaviour the Case changes (case 784)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] update `estimate-case-build-checks-the-finished-case`
>   - set:
>     ```
>     status: pending
>     purpose: Whether case-guppi checks its finished Case before it answers — the chosen options, the pages that name a slug the change makes false, the live texts that name a field, term or command whose behaviour the change touches, glossary rows and Estimates included, the sentences of a page it changes that state the changed behaviour in other words, the rules that act at the moment the change sets, the Cases of the session its prompt names or the check of its file names in a finding or a note, the purpose and method of an Estimate whose Criterion it replaces, what each search printed and that the context keeps only the searches the Case rests on, the sentences of its sub-cases that speak of one behaviour, field or term whatever page each changes — counted by what ask-guppi still finds at pre-spec
>     method: by hand, the text of .claude/agents/case-guppi.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec, read against the Criterion; the findings of ask-guppi at the /pre-spec of that session, when it ran, read for each Case case-guppi built — a Case that departs from a chosen option, a page naming a changed slug that the Case misses, a glossary row or an Estimate naming a changed field, term or command that the Case misses, a sentence of a page the Case changes that states the changed behaviour in other words and that the Case misses, a rule acting at the same moment that the Case misses, a Case of the session named in the prompt whose page or moment the Case clashes with, an Estimate whose purpose or method still states the promise its replaced Criterion dropped, a claim of context that its search did not print, a search in context that the Case does not rest on, two sub-cases whose texts on one behaviour, field or term contradict — the count of each in the estimate line
>     ```
>   - change: `the Criterion replaced whole — sub-cases read side by side by the behaviour, field or term they speak of, whatever page each changes, and a search for the name of each changed field, term or command (case 784)`
> - [ ] read `estimate-case-build-checks-the-finished-case`

> **ratification:**
> ```
> - decision[case 784][update][rule-case-build]{ref:rule-case-build}
> - decision[case 784][update][estimate-case-build-checks-the-finished-case]{ref:rule-case-build}
> ```
