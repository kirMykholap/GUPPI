## Case 579 — The main agent names the related Cases of the session, and case-guppi checks them and the replaced Estimate's purpose

> **context:**
> Before it answers, `case-guppi` checks its finished Case. It looks for the pages the change makes false and for the rules that act at the moment the change sets. For the second part it searches `vault/wiki/rules/` and `.claude/`. `estimate-case-build-checks-the-finished-case` measures this check by what `ask-guppi` still finds at `/pre-spec`. The reading of session 2356, ledger line 44, failed with three misses over Cases 561 and 562, which were built after the render that carried case 557.1.
>
> In the first miss, 561.13 changed the shape of the main agent's own questions and missed `rule-skill-hi` and `estimate-hi-takes-its-readings`, which set the question about an open reading at `/hi`. That miss happened under the current text. The handoff of session 2356 puts it down to the size of Case 561, which the backlog page `rule-case-rebuild-cost` holds. In the second miss, 561.3 replaced the Criterion of `estimate-prespec-hook-gates` but left its `purpose` stating the old promise. The rule never names the `purpose` and `method` fields of a replaced Estimate. In the third miss, Case 562 added an end-of-reply check that refused the gathered list of the loop that 561.1 and 561.2 had set earlier in the same session. That loop stood only in the Cases of the session, which are not in `vault/wiki/rules/` or `.claude/` until the librarian's run. Case 571 put the item off.
>
> The person decided that `case-guppi` does not search the Cases of the session. The main agent knows them, so it names each related Case in its prompt to `case-guppi`. That is a Case of the session, ratified or already shown, that changes a page the item names or sets what happens at the same moment. The prompt gives its id, one sentence on what it sets and which pages it changes, and the path of its case file. `case-guppi` reads only the case files the prompt names. The person also decided that, when `case-guppi` replaces an Estimate's Criterion, it rewrites that Estimate's `purpose` and `method` where they state the old promise. The dispatch is a promise of its own, so 579.1 changes `rule-case-protocol` and creates `estimate-case-protocol-names-related-cases-in-the-dispatch`. 579.2 changes `rule-case-build` and replaces the Criterion of `estimate-case-build-checks-the-finished-case`, with a new `purpose` and `method`, and carries `{supersedes:case 571}` on that line. An Estimate carries no `deferred_by`, so only the Decision page of 571 is superseded, as with case 560 in session 2356. The dispatch of this Case already named Cases 577 and 578. Case 578 changes `rule-case-protocol` in the acknowledging-reply paragraph of its Render. The pair of 579.1 stands in the paragraph on who builds a Case, in the same Render section, and the two anchors do not overlap. Case 577 touches neither page nor moment.
>
> The check of the answer noted that six lines of the old Criterion are not carried word for word, and that one `then` line of 579.2 shares most of its words with the `then` of 579.1. Both are on purpose:
> - The old Criterion had seven `＋` lines, and this Case adds two. To stay within seven `＋` lines, the line on a chosen option that cannot hold joins the line on the chosen options. The line on a fact that no slug marks joins the line on the slug search. The part of the hit line on a claim of `context` moves into the line on a claim about a search. Each old promise stands, in the merged line.
> - The shared words describe one thing from two sides: 579.1 says what the main agent puts in its prompt, and 579.2 says what `case-guppi` does with it. Each Criterion reads without the other.
>
> Frame. A Grep of `dispatches it with|the Case id, the Frontier item` over the repository outside `vault/raw/` and `vault/archive/` printed five files: `.claude/agents/case-guppi.md`, `vault/wiki/case-schema.md`, `estimate-case-protocol-shows-the-built-case`, `rule-case-protocol` and `rule-case-build`. The two rendered files follow their rules. `estimate-case-protocol-shows-the-built-case` lists what the dispatch carries and does not say it carries nothing else, so its Criterion stays true and stands. The person chose a new Estimate over replacing that wide promise. `estimate-case-build-writes-the-case` words its `when` the same way and stands for the same reason. A Grep of `dispatch\w*[^.]{0,60}case-guppi|case-guppi[^.]{0,60}dispatch` over `vault/wiki/rules/` printed `rule-orchestration`, `rule-case-protocol`, `rule-ask` and `rule-spec-reconcile`. Over `.claude/` it printed no file. `rule-ask` says that `case-guppi` cannot dispatch a subagent. `rule-spec-reconcile` names the title line of the plan, written before the first dispatch. `rule-orchestration` lists the dispatch among what moves to a file of its own in a later session, and the new clause moves with it. All three stay true. A Grep of `SubagentStop` over `vault/wiki/rules/` printed `rule-case-rebuild-cost`, `rule-case-protocol`, `rule-case-check`, `rule-hook-registry` and `rule-spec-reconcile`. Over `.claude/` it printed `.claude/settings.json`. The `set` of 579.2 carries `status`, `purpose` and `method` together, and the scripts foresee that form:
> - `guppi/prespec.py`, lines 906 to 917, reads the `method` under `set` of an Estimate `update`. It judges that `method` by `names_a_form` of `guppi/lint.py`, which accepts the words `by hand`, and the `method` here opens with them.
> - `guppi/generate.py`, lines 793 to 796, writes each key under `set` onto the page.
> - The hook of `rule-case-check` checked the earlier answer of this Case with this same `set`, and none of its notes spoke of it.
>
> Case 568 set `status` and `purpose` alone, so it is a precedent for `purpose` only. The Purpose of `rule-case-build` says that the agent gets an item and the person's words. It stays true and is not reworded. I read the Criteria of the other Estimates of `rule-case-build`: the ones on the plain round, the record of rounds in `recommend`, the old form and what done means. None speaks of the frame check, so each stands. A Glob of `vault/**/estimate-case-protocol-names-*` printed no file, so the slug is free. The `create` carries a `ref`, so no vault query ran. No code reads the prompt or these texts, so no old form is kept. The main agent's own Cases with too many sub-cases are not addressed here. A Case ratified after the dispatch, while `case-guppi` is still in its rounds, is not covered either, because the prompt is the dispatch alone.

> **problem:**
> The check `case-guppi` runs on its finished Case missed a clash with a Case ratified earlier in the same session, because such a Case is not yet in the rule pages it searches. It also missed an Estimate whose `purpose` still stated the promise its replaced Criterion had dropped. The question was how the related Cases of the session reach `case-guppi`, which Cases count as related, whether the `purpose` and `method` of a replaced Estimate are checked, and how each change is measured.

> **recommend:**
> - **Change the rule, or read the Estimate again?**
>   - Recommended: (b) a Case that adds both checks: `case-guppi` reads the case files of the session for a Case at the same moment or on the same pages, and checks the `purpose` and `method` of an Estimate whose Criterion it replaces.
>   - Answer: none of the options. `case-guppi` must not read the Cases of this session. The main agent knows all the Cases, so it is the main agent's task to tell `case-guppi` that a related Case already exists.
> - **What the main agent writes about a related Case**
>   - Recommended: (a) the id, one sentence on what it sets and which pages it changes, and the path of its case file; `case-guppi` reads that file and no other Case of the session.
>   - Answer: (a).
> - **Which Cases count as related**
>   - Recommended: (a) each Case of the session, ratified or already shown, that changes a page the item names or sets what happens at the same moment.
>   - Answer: (a).
> - **The `purpose` and `method` lines of a replaced Estimate**
>   - Recommended: (a) keep this check: when `case-guppi` replaces a Criterion, it rewrites in the same Case each of those lines that states the old promise.
>   - Answer: (a).
> - **How the change is checked**
>   - Recommended: (a) two sub-cases: a new Estimate on `rule-case-protocol` for the dispatch, and the Criterion of `estimate-case-build-checks-the-finished-case` replaced; both read in a later session after the render.
>   - Answer: (a).

### Case 579.1 — The main agent names the related Cases of the session in its prompt to case-guppi

> **given:**
> `rule-case-protocol` — the Case schema, whose paragraph on who builds a Case sets what the main agent's prompt to `case-guppi` holds
> **＋** `vault/wiki/case-schema.md` — the file rendered from that Render, loaded by `/hi`
> **＋** `estimate-case-protocol-names-related-cases-in-the-dispatch` — the promise this sub-case creates
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the case file of a Case of the session, written by the hook of `rule-case-check`
> **＋** `estimate-case-protocol-shows-the-built-case` — the promise of the dispatch and the showing, whose Criterion stands
> **＋** `raw/2026-10-01/1441/cases/case-578.md` — Case 578, which changes another paragraph of the same Render in this session

> **when:**
> The main agent dispatches `case-guppi` by an `Agent` call to build the Case of a Frontier item, with `vault/wiki/case-schema.md` rendered from `rule-case-protocol`.

> **then:**
> The prompt of the call names each Case of the session, ratified or already shown, that changes a page the item names or sets what happens at the same moment as the item: the same kind of reply, the same hook event or the same command.
> **＋** Each such Case stands in the prompt by its id, one sentence on what it sets and which pages it changes, and the path of its case file `raw/<date>/<hi HHMM>/cases/case-<N>.md`.
> **＋** The main agent judges which Cases of the session are related, and the prompt does not send `case-guppi` to search the Cases of the session.
> **－** A Case of the session that changes no page the item names and acts at another moment need not stand in the prompt.
> **－** When no Case of the session is related, the prompt names none and holds the Case id, the Frontier item with its source and the person's words.

> **tasks:**
> - [ ] update `rule-case-protocol` — the main agent names the related Cases of the session in its prompt to `case-guppi`
>   - old:
>     ````
>     and the person's words on it — in the prompt of the call, not in the chat — and creates the plan file
>     ````
>   - new:
>     ````
>     and the person's words on it, and each Case of the session, ratified or already shown, that changes a page the item names or sets what happens at the same moment, such as a reply, a hook event or a command, by its id, one sentence on what it sets and which pages it changes, and the path of its case file `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the main agent judging which Cases are related and `case-guppi` reading no other Case of the session (case 579.1) — in the prompt of the call, not in the chat — and creates the plan file
>     ````
>   - change: `the main agent names in its prompt to case-guppi each Case of the session that changes a page the item names or acts at the same moment, with its id, a sentence and its case file (case 579.1)`
> - [ ] create `estimate-case-protocol-names-related-cases-in-the-dispatch`
>   - ref: `rule-case-protocol`
>   - kind: `QA`
>   - purpose: `Whether the main agent's prompt to case-guppi names each Case of the session that changes a page the item names or acts at the same moment, by its id, one sentence on what it sets and the path of its case file`
>   - method: `by hand at the close of a later session after the render, each Agent call to case-guppi in the transcript read against the Cases ratified or shown before it; a related Case not named, and a named Case without its sentence or its case file, counted in the reading line`
>   - tags: `[session, workflow]`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-case-protocol-names-related-cases-in-the-dispatch` — by hand at the close of a later session after the render

> **ratification:**
> ```
> - decision[case 579.1][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 579.1][create][estimate-case-protocol-names-related-cases-in-the-dispatch]{ref:rule-case-protocol}{tags:session,workflow}
> ```

### Case 579.2 — case-guppi checks the named Cases of the session and the purpose of a replaced Estimate

> **given:**
> `rule-case-build` — the rule of `case-guppi`, whose Render sets what its prompt holds and how it checks its finished Case
> **＋** `.claude/agents/case-guppi.md` — the agent file rendered from that Render
> **＋** `estimate-case-build-checks-the-finished-case` — the promise whose Criterion, `purpose` and `method` this sub-case replaces
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the case file of a Case of the session that the prompt names
> **＋** `rule-case-protocol` — the schema, which sets that the main agent names the related Cases in the prompt (579.1)
> **＋** `.claude/agents/ask-guppi.md` — the recipe whose index lines it reads for a fact that no slug marks
> **＋** `vault/wiki/rules/` and `.claude/` — where it searches for a rule acting at the same moment

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, has built a Case and is about to answer with it.

> **then:**
> It puts each option the person chose in its rounds, or the person's own words where they answered outside the options, beside the `then` and `recommend` of the Case, and the Case holds each one; where the frame shows after a round that a chosen option cannot hold as written, its answer is a round on that point, not a Case with another behaviour.
> **＋** For each page whose text the change makes false, it searches the live pages of the vault, leaving out the Decision pages, and the code, for the page's slug, and reads each hit that `given` does not name around the line of the hit; for a fact that no slug marks, it reads the index lines of the recipe of `.claude/agents/ask-guppi.md` and judges them by meaning.
> **＋** When the change sets what happens at a moment — a reply, a hook event, a command — it searches `vault/wiki/rules/` and `.claude/` for the words that name that moment, reads each passage of each hit that sets a form or a behaviour at that moment, and the Case either does not cover that moment or names the other rule in `given`.
> **＋** It reads the case file `raw/<date>/<hi HHMM>/cases/case-<N>.md` of each Case of the session that the prompt of its call names, and no other Case of the session; where that Case changes a page the Case changes or sets what happens at the same moment, the Case does not cover that moment or names the case file in `given`, and its new text of that page does not contradict the text of that Case.
> **＋** When the Case replaces the Criterion of an Estimate, it reads the `purpose` and `method` of that Estimate, and the same `update` sets anew each one that states the old promise.
> **＋** Each hit that the change makes false enters the Case, or its `context` says why it stands.
> **＋** A claim of `context` about a text names the search it rests on: its pattern, the paths it ran over, and each file the search printed, a file it does not read included, or the count it printed; it claims nothing the search did not print.
> **＋** It reads side by side the finished new texts of all its sub-cases that change one page, and the Case holds no contradiction between them.
> **－** A hit in a History line, in `log.md` or in `brief.md` is not read.

> **tasks:**
> - [ ] update `rule-case-build` — `case-guppi` reads the case files of the related Cases its prompt names, and the `purpose` and `method` of an Estimate whose Criterion it replaces
>   - old:
>     ````
>     The caller's prompt holds the Case id, the Frontier item with its source, and the person's words that bear on it;
>     ````
>   - new:
>     ````
>     The caller's prompt holds the Case id, the Frontier item with its source, the person's words that bear on it, and each Case of the session that the main agent judges related to the item, by its id, one sentence on what it sets and the path of its case file (case 579.2);
>     ````
>   - old:
>     ````
>     bound the Case so that it does not cover that moment, or name the other rule in `given` (case 557.1).
>     ````
>   - new:
>     ````
>     bound the Case so that it does not cover that moment, or name the other rule in `given` (case 557.1). Read the case file of each Case of the session that the caller's prompt names, and no other Case of the session: where it changes a page your Case changes or sets what happens at the same moment, bound your Case so that it does not cover that moment, or name its case file in `given`, and read your new text of that page beside its text and fix a contradiction between them (case 579.2). When your Case replaces the Criterion of an Estimate, read the `purpose` and `method` of that Estimate, and set anew in the same `update` each one that states the old promise (case 579.2).
>     ````
>   - change: `case-guppi reads the case file of each related Case of the session that its prompt names, and sets anew the purpose and method of an Estimate whose Criterion it replaces where they state the old promise (case 579.2)`
> - [ ] update `estimate-case-build-checks-the-finished-case`
>   - set: `{status: pending, purpose: "Whether case-guppi checks its finished Case before it answers — the chosen options, the pages that name a slug the change makes false, the rules that act at the moment the change sets, the Cases of the session its prompt names, the purpose and method of an Estimate whose Criterion it replaces, what each search printed, the sub-cases that change one page — counted by what ask-guppi still finds at pre-spec", method: "by hand: at /pre-spec of a later session after the render, the report of ask-guppi read for each Case case-guppi built — a Case that departs from a chosen option, a page naming a changed slug that the Case misses, a rule acting at the same moment that the Case misses, a Case of the session named in the prompt whose page or moment the Case clashes with, an Estimate whose purpose or method still states the promise its replaced Criterion dropped, a claim of context that its search did not print, two sub-cases whose texts on one page contradict; the count of each in the reading line"}`
>   - change: `the Criterion replaced whole — the case files of the related Cases the prompt names, and the purpose and method of an Estimate whose Criterion is replaced; the defer of case 571 retired (case 579.2)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-checks-the-finished-case` — by hand at `/pre-spec` of a later session after the render, the report of ask-guppi read for each Case

> **ratification:**
> ```
> - decision[case 579.2][update][rule-case-build]{ref:rule-case-build}
> - decision[case 579.2][update][estimate-case-build-checks-the-finished-case]{ref:rule-case-build}{supersedes:case 571}
> ```
