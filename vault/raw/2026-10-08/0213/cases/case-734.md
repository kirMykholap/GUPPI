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

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` For a fact that no slug marks, read the index lines of the recipe of `.claude/agents/ask-guppi.md` and judge them by meaning. ``
>   - new: `` For a fact that no slug marks, read the index lines of the recipe of `.claude/agents/ask-guppi.md` and judge them by meaning. In each page the Case changes, which you read whole, list each sentence that states the behaviour the change touches, judged by what it says and never found by a Grep for the words of the sentence you change, so that a sentence that states the same rule in other words is on the list; each sentence on the list that the change makes false enters the Case, or `context` says why it stands (case 734). ``
>   - change: `case-guppi lists by meaning each sentence of a page it changes that states the behaviour the change touches, not by a Grep for the words of the changed sentence (case 734)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] update `estimate-case-build-checks-the-finished-case`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether case-guppi checks its finished Case before it answers — the chosen options, the pages that name a slug the change makes false, the sentences of a page it changes that state the changed behaviour in other words, the rules that act at the moment the change sets, the Cases of the session its prompt names or the check of its file names in a finding or a note, the purpose and method of an Estimate whose Criterion it replaces, what each search printed and that the context keeps only the searches the Case rests on, the sub-cases that change one page — counted by what ask-guppi still finds at pre-spec"
>     method: "by hand, the text of .claude/agents/case-guppi.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec, read against the Criterion; the findings of ask-guppi at the /pre-spec of that session, when it ran, read for each Case case-guppi built — a Case that departs from a chosen option, a page naming a changed slug that the Case misses, a sentence of a page the Case changes that states the changed behaviour in other words and that the Case misses, a rule acting at the same moment that the Case misses, a Case of the session named in the prompt whose page or moment the Case clashes with, an Estimate whose purpose or method still states the promise its replaced Criterion dropped, a claim of context that its search did not print, a search in context that the Case does not rest on, two sub-cases whose texts on one page contradict — the count of each in the estimate line"
>     ```
>   - sections.Criterion:
>     ```
>     When:
>     `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, has built a Case and is about to answer with it.
>
>     Then:
>     It puts each option the person chose in its rounds, or the person's own words where they answered outside the options, beside the `then` and `recommend` of the Case, and the Case holds each one; where the frame shows after a round that a chosen option cannot hold as written, its answer is a round on that point, not a Case with another behaviour.
>     **＋** For each page whose text the change makes false, it searches the live pages of the vault, leaving out the Decision pages, and the code, for the page's slug, and reads each hit that `given` does not name around the line of the hit; for a fact that no slug marks, it reads the index lines of the recipe of `.claude/agents/ask-guppi.md` and judges them by meaning.
>     **＋** In each page the Case changes, which it has read whole, it lists each sentence that states the behaviour the change touches, judged by what the sentence says and not found by a search for the words of the sentence it changes, so that a sentence that states the same rule in other words is on the list; each sentence on that list that the change makes false enters the Case, or its `context` says why it stands.
>     **＋** When the change sets what happens at a moment — a reply, a hook event, a command — it searches `vault/wiki/rules/` and `.claude/` for the words that name that moment, reads each passage of each hit that sets a form or a behaviour at that moment, and the Case either does not cover that moment or names the other rule in `given`.
>     **＋** It reads the case file `raw/<date>/<hi HHMM>/cases/case-<N>.md` of each Case of the session that the prompt of its call names, and of each Case of the session that the check of `rule-case-check` names in a finding or a note on its file, and no other Case of the session; where that Case changes a page the Case changes or sets what happens at the same moment, the Case does not cover that moment or names the case file in `given`, and its new text of that page does not contradict the text of that Case.
>     **＋** When the Case replaces the Criterion of an Estimate, it reads the `purpose` and `method` of that Estimate, and the same `update` sets anew each one that states the old promise.
>     **＋** Each hit that the change makes false enters the Case, or its `context` says why it stands.
>     **＋** The `context` names a search only when the Case rests on it: a search with a hit that enters the Case, a search with a hit that stands and needs the reason why, or a search that a claim that no text says something rests on; a search that found nothing to change and that no claim rests on is left out.
>     **＋** A claim of `context` about a text names the search it rests on: its pattern, the paths it ran over, and each file the search printed, a file it does not read included, or the count it printed; just before it answers, it runs each search that `context` names again, with the pattern and the paths that `context` writes, and the files and counts in `context` are the ones that run printed, not the files it read during the build; it claims nothing the search did not print.
>     **＋** It reads side by side the finished new texts of all its sub-cases that change one page, and the Case holds no contradiction between them.
>     **－** A hit in a History line, in `log.md` or in `brief.md` is not read.
>     ```
>   - change: `the Criterion replaced whole — case-guppi lists by meaning each sentence of a page it changes that states the behaviour the change touches; purpose and method name the new kind of miss (case 734)`
> - [ ] update `insight-workflow-case-written-without-reading-the-pages-it-changes`
>   - set: `{status: actioned, addressed_by: decision-case-734}`
>   - change: `actioned: case-guppi lists by meaning each sentence of a page it changes that states the behaviour the change touches, not by a Grep for the words of the changed sentence (case 734)`
> - [ ] read `estimate-case-build-checks-the-finished-case`

> **ratification:**
> ```
> - decision[case 734][update][rule-case-build]{ref:rule-case-build}
> - decision[case 734][update][estimate-case-build-checks-the-finished-case]{ref:rule-case-build}
> - decision[case 734][update][insight-workflow-case-written-without-reading-the-pages-it-changes]{ref:insight-workflow-case-written-without-reading-the-pages-it-changes}
> ```
